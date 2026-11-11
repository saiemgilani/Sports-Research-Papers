<!-- source: library/preprints/arXiv/2026/2026 - When Do Sports Leagues Stop Being Competitive Bayesian Detection of Competitive-Balance Eras from Match-Level Data - Li et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.07335 -->
<!-- authors: Xinran Li, Maoran Xu, Guanyu Hu -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-11; equations, tables and figures are NOT preserved - consult the PDF for those -->

# When Do Sports Leagues Stop Being Competitive? Bayesian Detection of Competitive-Balance Eras from Match-Level Data

                                            When Do Sports Leagues Stop Being
                                             Competitive? Bayesian Detection of
                                          Competitive-Balance Eras from Match-Level
                                                            Data
                                                                            Xinran Li
                                                Department of Statistics, University of Illinois Urbana-Champaign
                                                                            Maoran Xu
                                                          Department of Statistics, Indiana University
arXiv:2611.07335v1 [stat.AP] 5 Nov 2026




                                                                               and
                                                                           Guanyu Hu∗
                                                Department of Statistics and Probability, Michigan State University
                                                                                         Abstract
                                                     Competitive balance shapes outcome uncertainty, fan interest, and league reg-
                                                 ulation, yet standard measures summarize realized standings and cannot separate
                                                 structural ability differences from match-level randomness. We develop a Bayesian
                                                 framework that infers structural competitive balance from longitudinal match out-
                                                 comes. Team abilities are obtained by projecting Gaussian auxiliary variables onto a
                                                 graph-fused ℓ1 polytope whose radius measures total pairwise ability variation. The
                                                 projection places positive probability on exact ties, so statistically indistinguishable
                                                 teams form explicit rank tiers. The radius equals realized ability variation when-
                                                 ever the constraint binds, linking it to parity, detectability, and structural inequality.
                                                 An adaptive finite-regime model lets competitive eras recur, emerge, and disappear
                                                 while team hierarchies remain season specific. Simulations show accurate recovery of
                                                 regimes, radii, abilities, and tiers. Applied to 25 English Premier League seasons, the
                                                 model identifies a persistent shift to a more stratified league beginning in 2005/06,
                                                 with 2010/11 the only later return to the compressed regime. It also shows that a
                                                 close title race can coexist with wide league-wide separation and that head-to-head
                                                 results can separate clubs level on points. The framework gives leagues a model-based
                                                 measure of balance to inform debates on revenue sharing and financial regulation.

                                          Keywords: Bradley–Terry Model, Mixture of Finite Mixtures, Sports Economics, Rank
                                          Cluster
                                            ∗
                                             Xinran Li: xinran28@illinois.edu; Maoran Xu: mx13@iu.edu; Guanyu Hu: huguanyu@msu.edu.
                                          Maoran Xu and Guanyu Hu are joint corresponding authors.


                                                                                             1
1     Introduction
Rankings are used in many settings, including universities (Usher and Savino, 2009; Gold-
stein and Spiegelhalter, 1996), online platforms (Hong et al., 2019; Zhang et al., 2018),
forecasting (Leitner et al., 2010; Glickman, 1999), gene studies (Boulesteix and Slawski,
2009), and recommendation systems (Picoto et al., 2019; Rendle et al., 2009). A ranking
is easy to interpret, but the comparisons behind it are often sparse, noisy, and hetero-
geneous. Consequently, the inferential question is not only which item ranks higher, but
also whether the observed comparisons provide enough information to distinguish their
underlying abilities. Probabilistic paired-comparison models provide a natural framework
for this problem. The Bradley–Terry–Luce model (Bradley and Terry, 1952; Luce, 1959)
and its extensions (Davidson, 1970; Caron and Doucet, 2012; Karlé and Tyagi, 2023) form
a standard foundation for modeling relative ability. Classical formulations treat abilities
as fixed, while dynamic extensions allow strengths to vary over time through smoothing,
state-space models, and stochastic processes (Glickman, 1999; Cattelan et al., 2013; Tian
et al., 2024). Substantial work has also addressed scalable optimization (Hunter, 2004;
Maystre and Grossglauser, 2015), Bayesian inference (Mollica and Tardella, 2021), spectral
estimation (Tian et al., 2024), and high-dimensional theory (Fang et al., 2026). A common
structural feature nevertheless remains: latent abilities are typically assigned continuous
distributions on unconstrained spaces and are therefore almost surely distinct. Such models
naturally produce a strict ordering even when the data support only a coarser hierarchy.
    This issue is particularly important when similarity among competitors is itself scien-
tifically meaningful. Competitive balance in professional sports is one such setting. A
competitively balanced league is one in which teams have comparable underlying strength,
making outcomes less predictable and potentially sustaining fan interest and league value



                                             2
(Vrooman, 1995; Fort and Quirk, 1995; Szymanski, 2001, 2003; Zimbalist, 2002; Fort and
Maxcy, 2003; Humphreys, 2002). From this perspective, the central quantity is not simply
the dispersion of observed standings, but the degree of inequality in the latent abilities that
generate those standings. A model should therefore distinguish persistent structural dif-
ferences from game-level randomness and should allow genuine statistical parity to emerge
rather than rule it out by construction.
   Existing measures of competitive balance largely operate on realized outcomes. Com-
mon examples include Herfindahl–Hirschman-type indices (Owen et al., 2007), Gini and
dispersion measures (Utt and Fort, 2002), and football-specific indices (Manasis et al.,
2013; Manasis and Ntzoufras, 2014; Manasis et al., 2022). These measures are useful de-
scriptively, but they do not provide a generative model that separates latent ability inequal-
ity from random variation. Other work treats competitive strength as dynamic (Cairns,
1987; Schmidt, 2001; Koop, 2004; Penn and Berridge, 2019; Plumley et al., 2018), includ-
ing Bayesian and state-space approaches for evolving team abilities (Baio and Blangiardo,
2010; Lopez et al., 2018). These formulations capture temporal variation but generally
retain continuously distributed latent strengths, so exact parity and rank tiers are not
explicit parts of the latent structure.
   The ranking literature has addressed related questions through partial orders, clustered
rankings, shared consensus structures, and sparse difference models (Marden, 1996; Deng
et al., 2014; Li et al., 2022; Murphy and Martin, 2003; Busse et al., 2007; Dunson and
Peddada, 2008; Pearce and Erosheva, 2025a,b; Piancastelli and Friel, 2025). The ranking
lasso, for example, groups Bradley–Terry abilities by shrinking selected pairwise differ-
ences exactly to zero (Masarotto and Varin, 2012). These approaches show that ranking
uncertainty and latent grouping are closely related, but they do not directly provide a sin-
gle structural parameter that simultaneously measures competitive balance, induces exact


                                              3
rank tiers, and evolves across historical periods.
   We address this gap by restricting each period’s latent ability vector to a graph-fused
ℓ1 polytope, whose radius controls total variation across the comparison graph. Although
ℓ1 constraints appear in Bayesian ℓ1 -ball models (Xu and Duan, 2023) and fused regular-
ization (Tibshirani et al., 2005; She, 2010; Ma and Huang, 2017), we instead project an
unconstrained Gaussian auxiliary vector onto the polytope. Because the projection can
land on lower-dimensional faces, exact zero ability contrasts have positive probability and
rank tiers arise directly from the generative mechanism. The radius also measures compet-
itive imbalance. When the constraint binds, it equals the realized total of pairwise ability
gaps, making it a property of the teams rather than a season’s points table. Larger radii
imply greater stratification; at the parity boundary, all teams belong to one tier. The radius
also determines how many matches are needed to detect a departure from parity, bounds
the signal-to-noise ratio of Lopez et al. (2018), and yields a structural Gini coefficient. It
thus places these measures on a common scale with posterior uncertainty. To allow the
competitive environment to change, we let the radius follow a finite-regime process. Exist-
ing regimes can recur, new ones can appear, and unused ones can disappear, with a birth
penalty inspired by mixture-of-finite-mixtures models (Miller and Harrison, 2018). This
estimates the number of competitive eras without fixing it in advance. Regimes describe
competitive environments, not team identities. Two seasons in the same regime share a
radius but generally have different abilities: st = st′ implies rt = rt′ , whereas typically
θt ̸= θt′ . A league can therefore remain equally stratified while its leading clubs change. In
the Premier League, 2015/16, won by Leicester City, and 2019/20, won by Liverpool, be-
long to the same high-dispersion regime. Grouping seasons by balance rather than rankings
lets the model address league structure rather than particular clubs.
   This paper makes three contributions to the study of competitive balance. First, we


                                              4
propose a model-based measure of structural balance. When the constraint binds, the
polytope radius equals the realized dispersion of team abilities, so it describes the teams
rather than a season’s points table. Its posterior uncertainty helps distinguish genuine
changes in balance from unusual results. Near parity, the same radius links the signal-to-
noise ratio of Lopez et al. (2018), a structural Gini coefficient, and the number of matches
needed to detect a departure from parity. Second, the projection prior assigns positive
probability to exact ties. Teams that the data cannot distinguish share a rank tier, with
tiers estimated from the model rather than imposed afterward. This helps separate genuine
ability gaps from single-season noise. Third, we infer competitive eras without fixing their
number in advance. Seasons in the same era share a level of balance but not necessarily
the same leading clubs. The model therefore groups seasons by league stratification rather
than by winners, and changes in league structure are estimated within a probability model
rather than judged from a time series of indices.
   Applied to 25 seasons of the English Premier League, the framework finds a persistent
shift to a more stratified league beginning in 2005/06, with 2010/11 the only later return to
the compressed regime. It shows that a close title race, as in 2011/12, can coexist with wide
separation across the rest of the table, that home advantage evolves separately from balance,
and that head-to-head results can separate clubs that finished level on points, as Arsenal
and Liverpool did in 2006/07. Leading clubs change throughout the stratified era, from
Manchester United and Chelsea to Manchester City, Leicester City, and Liverpool, while
the league’s overall level of separation stays the same. A second application to the National
Basketball Association (Supplementary Material, Appendix G), a closed league with very
different parity mechanisms, shows recurrent switching between regimes rather than a single
lasting shift. These results move the assessment of competitive balance from retrospective
summaries of points toward inference on parity, hierarchy, and structural change, which is


                                             5
the evidence leagues need when weighing revenue sharing, financial regulation, or format
reform.



2     Motivating Data
To motivate our methodological development, we consider match-level outcomes from 25
consecutive seasons of the English Premier League (EPL), from 1995/96 through 2019/20
(Basini et al., 2023). The EPL provides a natural setting for studying structural com-
petitive balance. Each season follows a complete double round-robin schedule, with every
team playing every other team once at home and once away, yielding a balanced and fully
connected comparison network. Although the league size remains fixed, team member-
ship changes through promotion and relegation. The study period also spans substantial
changes in broadcasting revenue, club ownership, and financial resources that have mo-
tivated longstanding debates about competitive inequality (Basini et al., 2023). Table 1
summarizes the main characteristics of the data.

       Table 1: Summary of the English Premier League data, 1995/96 to 2019/20.
    Characteristic                                       Value
    Seasons                                           25 (1995/96–2019/20)
    Teams per season                                  20
    Matches per season                                380 (double round robin)
    Total matches                                     9,500
    Distinct clubs over the study period              47
    Outcome categories                                home win / draw / home loss
    Overall proportions (home win / draw / home loss) 46.5% / 25.6% / 27.9%
    Seasonal draw proportion (range)                  18.7%–31.3%


    Data structure. For each season, we represent the match results as a complete directed

                                            6
outcome network on the 20 participating teams, with no self-loops. The directed edge from
team i to team j records the outcome of the match in which i hosted j, classified as a home
win, draw, or home loss. This representation preserves opponent-specific outcomes and
home advantage information that would otherwise be lost when results are aggregated into
final standings. Draws account for 25.6% of all matches and provide important information
about competitive similarity. We therefore retain them as a separate ordered outcome
category rather than combining them with wins or losses.
   Why the points table is not enough. Figure 1 illustrates the limits of assessing
competitive balance from final standings alone. Panel (A) shows variation in the standard
deviation of final points across 25 seasons, but this may reflect either underlying team
abilities or random match outcomes. Panel (B) shows that league-wide dispersion and
championship closeness need not coincide. In 2011/12, Manchester City and Manchester
United finished level on 89 points, while third-placed Arsenal were 19 points behind. A close
title race therefore coexisted with substantial league-wide inequality. Panel (C) shows that
equal point totals can hide informative match results. In 2006/07, Arsenal and Liverpool
both finished with 68 points, but Arsenal beat Manchester United twice, whereas Liverpool
lost both meetings. Panel (D) compares the points distributions in 1995/96, 2011/12, and
2019/20, highlighting differences in the separation between leading clubs and the rest. Final
points, title margins, and individual results capture different aspects of competition; none
alone identifies structural inequality in team abilities.
   Together, these observations motivate three questions that guide our framework and
subsequent case study:
(Q1) Has structural competitive balance changed over time, and if so, when? The variation
      in points dispersion shown in Panel (A) motivates investigating whether the 25 seasons
      contain persistent changes in underlying competitive inequality. We examine whether


                                               7
           (A) Dispersion of final points                                                                                                                                              (B) Title-winning margin versus dispersion
                                                                                                                                                                                                           20
                                                1995/96                 2011/12                 2019/20
                              20




                                                                                                                                                                                    Title-winning margin
        SD of final points
                                                                                                                                                                                                           15
                              18

                              16                                                                                                                                                                           10

                              14
                                                                                                                                                                                                            5

                              12
                                                                                                                                                                                                            0

                                1995/96                1999/00                  2003/04                     2007/08                 2011/12                 2015/16       2019/20                                      12      14          16         18         20
                                                                                                            Season                                                                                                              SD of final points

           (C) 2006/07 match outcomes                                                                                                                                               (D) Final points of selected seasons

                                                                                                                                                                                                                1995/96                 2011/12                  2019/20
                                                                                                                                                                                    MUN                                      MCI                       LIV
                             MUN                                                                                                                              MUN 2-0 LIV
                                                                                                                                                                                    NEW                                      MUN                       MCI
                             CHE                                                                                                                              LIV 0-1 MUN
                                                                                                                                                                                          LIV                                ARS                      MUN
                              LIV
                                                                                                                                                                                    AVL                                      TOT                      CHE
                             ARS                                                                                                                              MUN 0-1 ARS
                             TOT                                                                                                                                                    ARS                                      NEW                       LEI
                                                                                                                                                              ARS 2-1 MUN
                             EVE                                                                                                                                                    EVE                                      CHE                      TOT

                             BOL                                                                                                                                                    BLA                                      EVE                      WOL
                                                                                                                                                              ARS 3-0 LIV
                             REA                                                                                                                                                    TOT                                       LIV                     ARS
                                                                                                                                                              LIV 4-1 ARS
        Home team




                             POR                                                                                                                                                    NFO                                      FUL                      SHU
                             BLA                                                                                                                                                    WHU                                      WBA                      BUR
                             AVL                                                                                                                                                    CHE                                      SWA                      SOU
                             MID                                                                                                                                                     MID                                     NOR                      EVE
                             NEW                                                                                                                                                    LEE                                      SUN                      NEW
                             MCI                                                                                                                                                    WIM                                      STK                      CRY
                             WHU                                                                                                                                                    SHW                                      WIG                      BHA
                             FUL                                                                                                                                                    COV                                      AVL                      WHU
                             WIG
                                                                                                                                                              Home win              SOU                                      QPR                       AVL
                             SHU
                                                                                                                                                                                     MCI                                     BOL                      BOU
                             CHA                                                                                                                              Draw
                                                                                                                                                                                    QPR                                      BLA                      WAT
                             WAT                                                                                                                              Home loss
                                                                                                                                                                                    BOL                                      WOL                      NOR
                                    MUN
                                          CHE
                                                LIV
                                                      ARS
                                                            TOT
                                                                  EVE
                                                                        BOL
                                                                              REA
                                                                                    POR
                                                                                          BLA
                                                                                                AVL
                                                                                                      MID
                                                                                                            NEW
                                                                                                                  MCI
                                                                                                                        WHU
                                                                                                                              FUL
                                                                                                                                    WIG
                                                                                                                                          SHU
                                                                                                                                                CHA
                                                                                                                                                      WAT




                                                                                                                                                                                                           0      50   100          0     50    100          0     50   100
                                                                                    Away team
                                                                                                                                                                                                                                    Final points




  Figure 1: Descriptive features of the English Premier League data, 1995/96–2019/20.

     these seasons can be grouped into a small number of recurring competitive regimes
     without fixing their number in advance, and whether the timing of structural changes
     corresponds to developments in English football.
(Q2) Which teams are statistically distinguishable within a season? The opponent-specific
     outcomes in Panel (C) illustrate that similar aggregate performance can conceal dif-
     ferent patterns of competition. Rather than imposing a strict ordering of all 20 teams,
     we investigate whether match outcomes support exact latent rank tiers and whether


                                                                                                                                                               8
     these tiers reveal competitive relationships that final standings cannot capture.
(Q3) Is structural competitive balance distinct from title-race closeness and home advan-
     tage? Panels (B) and (D) illustrate that championship competitiveness and overall
     league inequality need not coincide. We investigate whether league-wide dispersion
     in latent abilities evolves separately from the closeness of the title race and season-
     specific home effects.
   These questions speak directly to sports economics. The uncertainty-of-outcome hy-
pothesis (Rottenberg, 1956) links fan demand and league value to uncertainty about sport-
ing contests, motivating mechanisms such as revenue sharing, salary caps, draft systems,
and financial fair-play regulations (Fort and Quirk, 1995; Vrooman, 1995; Szymanski, 2003;
Zimbalist, 2002). (Q1) asks whether changes in broadcasting revenue, club ownership, or
resource distribution coincide with persistent shifts in structural competitive balance rather
than random fluctuations in descriptive indices (Utt and Fort, 2002; Lopez et al., 2018).
(Q2) identifies statistically distinguishable competitive groups, including a possible “league
within a league” of persistently dominant teams (Penn and Berridge, 2019; Plumley et al.,
2018). (Q3) distinguishes match, seasonal, and championship uncertainty (Cairns, 1987;
Szymanski, 2003): a close title race may coexist with a stratified league, with different im-
plications for attendance, broadcasting demand, and incentives outside the leading group.
   Conventional indices based on points dispersion or concentration (Humphreys, 2002;
Owen et al., 2007; Manasis et al., 2013) summarize realized outcomes but cannot separate
persistent ability differences from match-level randomness or quantify uncertainty about
whether clubs are genuinely distinguishable. Figure 1 therefore motivates a probabilistic
framework that uses match-level paired comparisons to estimate structural competitive bal-
ance, identify recurring regimes, and assign clubs with similar latent abilities to exact rank
tiers. Section 6 revisits (Q1)–(Q3) using the EPL data; a National Basketball Association


                                              9
analysis in the Supplementary Material (Appendix G) assesses broader applicability.



3     A Geometric Framework for Structural Competi-
      tive Balance

3.1     Projection-induced paired-comparison model
We consider longitudinal paired-comparison data over periods t = 1, . . . , T . Let I =
{1, . . . , N } denote the competitors and Dt = {(itg , jtg , htg , ytg ) : g = 1, . . . , Gt }, where
htg is a contextual covariate such as home advantage and ytg ∈ {−1, 0, 1} denotes a loss,
draw, or win for competitor itg . Let θt = (θt1 , . . . , θtN )⊤ denote latent abilities, subject to
1⊤ θt = 0, and let ηt denote a period-specific contextual effect. Writing xtg = eitg − ejtg ,
define ∆tg = x⊤
              tg θt + ηt htg .

    We use an ordered Bradley–Terry likelihood (Bradley and Terry, 1952; Luce, 1959;
Davidson, 1970):


                    Pr(ytg ≤ c | θt , ηt , κ) = σ(κc+2 − ∆tg ),     c ∈ {−1, 0},                  (1)


where σ(u) = {1 + exp(−u)}−1 . The binary Bradley–Terry model is recovered by removing
the draw category.
    When htg is constant across comparisons, (ηt , κ) is identified only up to a common
location shift. We therefore impose κ1 = −κ2 and κ2 > 0, so that the draw region is
symmetric about zero and ηt carries the contextual location shift.
    Let Et denote the multiset of scheduled comparisons and At ∈ R|Et |×N its oriented
                                                          P
incidence matrix. The graph total variation is ∥At θt ∥1 = (i,j)∈Et |θti − θtj |. Repeated


                                                 10
meetings may either be counted with multiplicity or counted once, provided the same
convention is used for both At and rt .
   For rt > 0, define


                        Kt (rt ) = {ϑ ∈ RN : ∥At ϑ∥1 ≤ rt , 1⊤ ϑ = 0}.                     (2)


The radius rt therefore controls the amount of latent ability variation permitted by the
competitive environment.
   Following the geometric idea of Bayesian ℓ1 -ball priors (Xu and Duan, 2023) and related
fused regularization (Tibshirani et al., 2005), we introduce βt ∼ N (0, σβ2 IN ) and set


                           θt = ΠKt (rt ) (βt ) = arg min ∥ϑ − βt ∥22 .                    (3)
                                                    ϑ∈Kt (rt )


Projection onto lower-dimensional faces of Kt (rt ) can set graph contrasts exactly to zero,
so exact ability ties and rank tiers arise directly from the latent model.

Theorem 3.1 (Posterior propriety). Suppose all primitive unknowns are assigned a proper
joint prior. Then, for every finite comparison design {Dt }Tt=1 , the posterior distribution is
proper.

   The bounded paired-comparison likelihood ensures posterior propriety for a fully speci-
fied model with proper priors. Because the allocation step in Section 4 is not derived from
an established joint regime prior, this theorem does not assert propriety or exactness of the
algorithm-induced regime distribution.

Proposition 3.2 (Identifiability of the linear predictor and thresholds). Fix a period and
suppress t. Suppose the comparison graph is connected and there are no d ∈ RN and c ̸= 0


                                               11
satisfying 1⊤ d = 0 and x⊤                                                          G
                         g d = −chg for every g = 1, . . . , G. Then (θ, η) 7→ (∆g )g=1 is

injective on {θ : 1⊤ θ = 0} × R.
   If additionally κ1 = −κ2 and κ2 > 0, then the map from (θ, η, κ2 ) to the collection of
three-category probabilities in (1) is injective. Without this anchoring, when hg ≡ h, the
model is identified only up to (θ, η + c, κ + ch1).

   This anchoring is needed in both applications because every comparison has a designated
home entity, so htg ≡ 1; the non-collinearity condition then holds because each season
contains a home-and-away pair, for which xg′ = −xg forces c = 0.

Proposition 3.3 (Positive probability of exact ties). Fix rt > 0 and suppose the compari-
son graph is connected. Let F be a nonempty face of Kt (rt ) on which (At ϑ)e = 0 for some
edge e. Then RF = {b : ΠKt (rt ) (b) ∈ relint(F )} has positive Lebesgue measure and hence
Pr{(At θt )e = 0 | rt } > 0. Such a face exists for N ≥ 3, so the projection prior assigns
positive probability to exact latent ties for every rt > 0.


3.2     Geometry and interpretation of the structural radius
Let H = IN − N −1 11⊤ denote the projection onto the zero-sum subspace, write θt (r) =
ΠKt (r) (βt ), and define Zt = ∥At Hβt ∥1 .

Theorem 3.4 (Radius saturation). For every r ≥ 0,


                                     ∥At θt (r)∥1 = min{r, Zt }.                       (4)


Equivalently, θt (r) = Hβt when r ≥ Zt , whereas ∥At θt (r)∥1 = r when r < Zt .

   Thus, whenever the geometric constraint binds, the radius is not merely an upper bound:
it equals the realized structural variation.

                                                 12
Corollary 3.5 (Monotone structural ordering). For 0 ≤ r1 < r2 , ∥At θt (r1 )∥1 ≤ ∥At θt (r2 )∥1 ,
with strict inequality whenever r1 < Zt . Moreover, for Mt (r) = E{∥At θt (r)∥1 },
                                     Z r
         Mt (r) = E{min(r, Zt )} =         Pr(Zt > u) du,      Mt′ (r) = Pr(Zt > r) > 0.        (5)
                                       0


Hence Mt (r) is strictly increasing for every finite r.

Proposition 3.6 (Piecewise-affine projection path). Fix t, βt , and R < ∞. The path
r 7→ θt (r) is continuous and piecewise affine on [0, R]. Thus there exists 0 = b0 < b1 < · · · <
bQ = R such that θt (r) is affine on each (bq−1 , bq ). Every pairwise contrast θti (r) − θtj (r) is
therefore affine within each segment, so the rank-tier partition can change only at finitely
many radius values on every compact interval.

Lemma 3.7 (Two-block extreme points). Assume the comparison graph is complete and
                                     P
each dyad is counted once, so ∥Aϑ∥1 = i<j |ϑi − ϑj |. A vector θ ∈ K1 is an extreme point
if and only if it takes exactly two distinct values. Equivalently, for some nonempty proper
S ⊂ I, θ = ±(1S − |S|N −1 1)/{|S|(N − |S|)}. In particular, supθ∈K1 θi = 1/N , attained at
S = {i}.


3.3    Structural radius and calibration to existing balance mea-
       sures
The radius provides a structural capacity for ability inequality. A reciprocal-radius sum-
mary E(rt−1 | D) is finite only under conditions on the radius prior near zero (Lemma A.1 in
Appendix A), which the exponential prior used here does not satisfy. We therefore use ra-
dius posterior summaries and the finite realized-variation functional Mt (r) = E{min(r, Zt )}
rather than a reciprocal index.

                                                 13
   For comparisons across systems with different graph sizes or densities, we report the
normalized radius,


                      ret = rt /|Et |,    V t (rt ) = E{min(rt , Zt )}/|Et |.            (6)


The first quantity measures normalized capacity for pairwise ability variation, whereas the
second is the expected realized mean absolute graph contrast under the Gaussian auxiliary
prior. These interpretations coincide only when the radius constraint is active. Cross-league
comparisons require a consistent convention for repeated dyads and graph weights.
   Suppress t and write Kr = {θ : ∥Aθ∥1 ≤ r, 1⊤ θ = 0}. The following local results use the
binary Bradley–Terry model Pr(Yij = 1 | θ) = σ(θi − θj ), with analogous local conclusions
for the ordered model.

Theorem 3.8 (Single-block parity limit). Suppose the comparison graph is connected and
θ(r) ∈ Kr . As r ↓ 0, θ(r) → 0, and hence Pr(Yij = 1 | θ(r)) → 1/2 for every compared pair.
Moreover, there exists LA < ∞ depending only on the graph such that ∥θ(r)∥∞ ≤ LA r.
   For the ordered model, the limiting cell probabilities are those of (1) with ∆g = ηhg .
They reduce to threshold-only probabilities when hg = 0 or η = 0. At r = 0, θ1 = · · · =
θN = 0, so all competitors belong to one latent rank tier.

   For entity i, define its expected win probability against the field and its maximum
departure from parity by

                             1 X
                wi (θ) =              σ(θi − θj ),     δi (r) = sup wi (θ) − 12 .        (7)
                           N − 1 j̸=i                            θ∈Kr



Lemma 3.9 (Local linearity of structural drift). Assume the graph is connected and the
schedule is complete. Let ϱi = supθ∈K1 θi . Then, as r ↓ 0, δi (r) = cA,i r + O(r3 ) with

                                                14
cA,i = N ϱi /{4(N − 1)}. For the complete graph, ϱi = 1/N , so cA,i = {4(N − 1)}−1 and
δi (r) = r/{4(N − 1)} + O(r3 ).

   The preceding result determines how rapidly the amount of data required to detect
departure from parity increases as r approaches zero.

Theorem 3.10 (Inverse-square detection law). Fix entity i and a complete symmetric
schedule. Suppose i plays m conditionally independent comparisons, each won with prob-
ability wi (θ), and let Wm denote its number of wins. Consider the level-α test that re-
                                        √
jects parity when |Wm − m/2| > z1−α/2 m/2. For type-II error rate ν ∈ (0, 1), assume
1 − ν > α and let dα,ν > 0 solve Φ(d − z1−α/2 ) + Φ(−d − z1−α/2 ) = 1 − ν. Define
mi (r; α, ν) = min{m ≥ 1 : supθ∈Kr Prθ (reject) ≥ 1 − ν}. Then, as r ↓ 0,

                                                d2α,ν −2
                               mi (r; α, ν) =          r {1 + o(1)}.                            (8)
                                                4c2A,i

For the complete graph, the multiplicative constant is 4(N − 1)2 d2α,ν . The familiar approx-
imation dα,ν ≈ z1−α/2 + z1−ν neglects the lower tail of the two-sided power function.

Remark 3.11 (Why the horizon is fixed). A sequential rule of the form Ti∗ = inf{m ≥
              √
1 : |Sm | > cα m} does not provide valid infinite-horizon type-I error control. By the law
                                          √
of the iterated logarithm, lim supm |Sm |/ m = ∞ almost surely under parity. An always-
                         √
valid boundary of order m log log m or a mixture boundary restores sequential validity, but
introduces an additional logarithmic factor. We use the fixed-horizon formulation because
it matches the seasonal design and yields the explicit rate in (8).

Remark 3.12 (Regime of validity of the local expansions). Lemma 3.9, Theorem 3.10,
and Theorem 3.14 are local results as r ↓ 0. For a complete graph, the largest permitted
contrast is of order r/N , so the relevant empirical scale is ret = rt /|Et | rather than rt itself.

                                                 15
   In the simulations with N = 20 and r ∈ {100, 200, 400}, the normalized radii are
re ∈ {0.53, 1.05, 2.11}. For the two-tier configurations used there, the linear Gini approx-
imation overstates Gstruct by approximately 8%, 31%, and 108%, respectively. The local
expansions should therefore be interpreted near the parity boundary rather than as numer-
ical approximations at the radii observed in the applications. In contrast, Theorem 3.4,
Corollary 3.5, and Proposition 3.13 hold for all r.


3.4    Signal-to-noise and inequality functionals
Following Lopez et al. (2018), define SNR(θ) = Var(θ)/ Var(ξ), where logistic noise has
Var(ξ) = π 2 /3 and, under 1⊤ θ = 0, Var(θ) = N −1 N    2
                                                  P
                                                   i=1 θi .


Proposition 3.13 (Radius-bounded signal-to-noise ratio). If the comparison graph is com-
plete and θ ∈ Kr , then

                                     r2                                3r2
                     Var(θ) ≤               ,     SNR(θ) ≤                      .        (9)
                                N 2 (N − 1)                     π 2 N 2 (N − 1)

The bound is attained, up to permutation and sign, by a two-block configuration with block
sizes 1 and N − 1.
                                                        √
   For a general connected graph, CA = sup{∥ϑ∥2 /( N ∥Aϑ∥1 ) : ϑ ̸= 0, 1⊤ ϑ = 0} < ∞,
                                                                               √
and Var(θ) ≤ CA2 r2 and SNR(θ) ≤ 3CA2 r2 /π 2 ; for the complete graph, CA = {N N − 1}−1 .

   Using wi (θ) from (7), define

                                    N   N
                             1 XX                                         1 X
             Gstruct (θ) =                 |wi (θ) − wj (θ)|,      w̄ =       wi (θ).   (10)
                           2N 2 w̄ i=1 j=1                                N i

For the complete comparison system, w̄ = 1/2 exactly because σ(u) + σ(−u) = 1.


                                                16
Theorem 3.14 (Local geometric Gini law). Assume a complete schedule with each dyad
counted once. Uniformly over θ ∈ Kr as r ↓ 0,

                               1      X                             r
           Gstruct (θ) =                  |θi − θj | + O(r3 ) ≤            + O(r3 ).        (11)
                           2N (N − 1) i<j                       2N (N − 1)

Thus structural inequality is locally linear in the geometric radius.

    These results put several notions of competitive balance on a common geometric scale.
As r ↓ 0, θ → 0, mi (r; α, ν) ≍ r−2 , SNR(θ) = O(r2 ), and, under a complete symmetric
schedule, Gstruct (θ) = O(r). At the same time, Theorem 3.4 gives r an exact finite-sample
interpretation whenever the constraint is active. Thus the structural radius links latent
parity, rank tiers, statistical detectability, and structural inequality within one probabilistic
construction.



4     Dynamic Competitiveness via Adaptive
      Finite Regimes
The geometric framework of Section 3 characterizes structural competitive balance within
a period through the radius of the graph-fused ℓ1 polytope. We extend this construction
to longitudinal comparisons by allowing the radius to vary across periods while sharing
information among periods with similar competitive environments. Rather than fixing
the number of regimes in advance, we use an adaptive occupied-state representation in
which existing regimes may recur, new regimes may emerge, and unoccupied regimes are
removed. This construction is motivated by finite-mixture and mixture-of-finite-mixtures
methods (Miller and Harrison, 2018), but the regime allocation mechanism is specified


                                               17
directly below rather than through a conventional Dirichlet transition prior.


4.1    Dynamic geometric model
Let st denote the competitive regime assigned to period t = 1, . . . , T , and define the
occupied regime set A = {s1 , . . . , sT } and its cardinality Kact = |A|. Each occupied regime
k ∈ A is associated with a positive radius rk , so the structural radius for period t is rt = rst .
   Conditional on the regime assignment, latent abilities and contextual effects follow


                  βt ∼ N (0, σβ2 IN ),    θt = ΠKt (rst ) (βt ),   ηt ∼ N (0, ση2 ),          (12)


where Kt (r) is defined in (2), and match outcomes follow the ordered Bradley–Terry like-
lihood (1). The ordered-logit thresholds κ are held fixed.
   The regime assignments characterize competitive environments rather than team identi-
ties. In particular, st = st′ implies rt = rt′ , but generally θt ̸= θt′ . Seasons sharing the same
radius may therefore exhibit different rankings and rank-tier structures. This separation
is important for longitudinal sports data, where the degree of league-wide inequality may
remain stable even as the leading competitors change.
   For the occupied regimes, we specify the hierarchical radius distribution rk | αr ∼
Exponential(αr ), k ∈ A, with αr ∼ Gamma(ar , br ), where the Gamma distribution is
parameterized by shape and rate. This hierarchy controls the scale of structural variation
while allowing regimes to represent distinct competitive environments. Because the radius
distribution is continuous, the occupied radii are almost surely distinct under this prior and
can be ordered as 0 < r(1) < · · · < r(Kact ) . By Corollary 3.5, increasing radii correspond to
increasing expected latent ability dispersion for a fixed comparison design.



                                                 18
4.2     Adaptive regime allocation
We update the regime sequence through an occupied-state allocation rule that balances
temporal persistence with the creation of additional competitive environments. Immedi-
ately before updating st , let A = {1, . . . , m} denote the occupied regimes, after temporarily
removing the current assignment when computing transition counts. Let n−t
                                                                       kl denote the

number of transitions from regime k to regime l excluding transitions involving period
t, and write n−t
                   P −t
              k· =    l nkl . For interior periods, let i = st−1 and j = st+1 , and define

bm = γ/m, where γ > 0.
    For an existing regime k ∈ A, the incoming and outgoing transition factors are

                                                   n−t
                                                    kj + I{t > 1, i = k = j} + atr bm
             It (k) = n−t
                       ik + atr bm ,    Ot (k) =                                        ,       (13)
                                                        n−t
                                                         k· + I{t > 1, i = k} + atr


with I1 (k) = 1 and OT (k) = 1 at the boundary periods. The indicator terms account for
the dependence between the two adjacent transitions when the proposed state coincides
with the preceding state. These factors incorporate observed transition frequencies and
favor the reuse of previously occupied competitive environments.
  For a candidate radius r, define the period-specific likelihood ft (r) = Lt {ΠKt (r) (βt ), ηt , κ},
where Lt (θt , ηt , κ) = G
                        Q t
                         g=1 p(ytg | θt , ηt , κ). The allocation score for an existing regime is

wt (k) = It (k)Ot (k)ft (rk ).
    A new regime is represented by candidate 0, with transition factors It (0) = atr bm and
Ot (0) = bm , again with I1 (0) = OT (0) = 1. The propensity to introduce an additional
regime is controlled by the birth multiplier Bm = λ(m + 1)γ/{m(m + mγ)}, where λ > 0.
    To evaluate the new-regime likelihood, we approximate integration over the exponen-
tial radius distribution using J prior-quantile grid points, fet,0 = J −1 J ft (rgrid ) (Ap-
                                                                         P
                                                                                  j=1       j

pendix C.1). The resulting new-regime score is wt (0) = Bm It (0)Ot (0)fet,0 .


                                                   19
   The allocation probabilities used by the algorithm are

                                                 wt (c)
              Pr{st = c | current} =             P           ,            c ∈ A ∪ {0}.       (14)
              alg                        wt (0) + k∈A wt (k)

   When the new-regime candidate is selected, its initial radius is drawn from the same
grid according to

                                                                     .P
                                                                          J
                Pr(rnew = rjgrid | new, t, current) = ft (rjgrid )                 grid
                                                                          l=1 ft (rl    ).   (15)
                alg


The radius is subsequently updated on its continuous support using the Metropolis–Hastings
step described in Appendix C.1. After reassignment, regimes without occupied periods are
removed and the remaining labels are compacted.
   The parameters atr , γ, and λ have distinct roles: they control transition-count smooth-
ing, baseline allocation mass, and the tendency to introduce new regimes, respectively.
Temporal persistence is induced by the observed transition counts rather than by an addi-
tional diagonal-specific persistence parameter.
   The allocation rule is an adaptive computational construction. Although each update
defines a proper conditional probability distribution over its candidate states, the rule
is not asserted to be the exact collapsed conditional of a conventional MFM-HMM prior.
Consequently, unless compatibility with a joint regime distribution and posterior invariance
are established, uncertainty summaries involving the regime assignments are interpreted as
approximations generated by the specified allocation procedure.




                                                 20
4.3    Distinguishability of competitive regimes
The regime representation is informative when distinct radii correspond to distinguishable
distributions of observed comparisons. For a fixed comparison graph A, let θ(r) = ΠK(r) (β)
and V (r) = ∥Aθ(r)∥1 . By Corollary 3.5, E{V (r1 )} < E{V (r2 )} for 0 < r1 < r2 , so the
structural radius provides a strictly ordered measure of expected latent ability dispersion.
   To characterize the corresponding observed-data distributions, let X denote a fixed
comparison design and define
                           ZZ
          g(y | r, X ) =        p{y | ΠK(r) (β), η, κ, X } ϕN (β; 0, σβ2 IN ) ϕ(η; 0, ση2 ) dβ dη.   (16)


Let P be the set of home-and-away pairs of X , comparisons g ̸= g ′ with (ig′ , jg′ ) = (jg , ig ),
                P
and let SX (r) = (g,g′ )∈P Prr {I(yg = 1) ̸= I(yg′ = 1)}, under (16), be the expected number
of such pairs in which exactly one home side wins.

Assumption 4.1 (Emission separation). For the comparison design X , the function r 7→
SX (r) is strictly increasing over the radius range under consideration.

Proposition 4.1 (Distinguishability of competitive environments). Suppose Assumption 4.1
holds on R ⊂ (0, ∞). Then, for any r1 , r2 ∈ R, r1 ̸= r2 implies g(· | r1 , X ) ̸= g(· | r2 , X ).

Proof. SX (r) is a functional of g(· | r, X ) and is injective on R.

   Near the parity boundary the condition holds whenever P is nonempty, as in every
season of both applications: for any connected graph and any law of η, each term of
SX equals its parity value plus cr2 + o(r2 ) with c > 0 and is strictly increasing on some
(0, r̄] (Lemma B.2, Appendix B). Covariances of repeated meetings are unsuitable, because
integrating over η adds a radius-dependent term of indefinite sign (Remark B.3). The


                                                    21
lemma is local; at the fitted radii Assumption 4.1 remains an assumption, with numerical
support in Appendix H.
    At larger radii, the constraint binds less frequently. By Theorem 3.4, the projected
abilities approach the centered unconstrained Gaussian draw as the radius becomes large
relative to Zt = ∥At Hβt ∥1 . The quantity Pr(Zt > r) = Mt′ (r) therefore characterizes the
sensitivity of expected structural variation to changes in the radius.
    The geometric model and the regime allocation mechanism serve complementary pur-
poses. The former defines structural competitive balance and allows exact rank tiers within
each period, while the latter groups periods with recurring levels of structural inequality.
The occupied regime count Kact , regime radii, and temporal allocations provide a summary
of changing competitive environments without requiring the same team hierarchy across
periods.



5     Bayesian Inference and Simulation Validation

5.1    Bayesian Inference
Posterior inference uses a blockwise Markov chain Monte Carlo procedure, given in full
in Appendix C (Algorithm 1). Each sweep updates the auxiliary abilities βt by elliptical
slice sampling, recomputing the projection θt = ΠKt (rst ) (βt ), a convex quadratic program, at
every likelihood evaluation; updates the period home effects ηt by random-walk Metropolis–
Hastings; updates each occupied radius rk by a Metropolis–Hastings step on log rk and
draws the shared rate αr from its Gamma full conditional; and finally reallocates the
periods one at a time with the adaptive rule of Section 4.2, creating new regimes through
a grid of prior radius quantiles and deleting empty ones. The threshold κ is held fixed.



                                              22
Because the allocation kernel is specified algorithmically rather than derived as an exact
collapsed update, we treat the output as an approximate posterior: given the regime path,
the updates of βt , ηt , rk and αr leave the conditional posterior invariant, but summaries
that average over regime paths (the distribution of Kact , memberships, co-clustering and
transition frequencies, and to a lesser degree all intervals) describe this sampler, and their
calibration is checked in Appendix E.4.
    The retained draws are post-processed into interpretable point summaries. State labels
are first ordered by increasing radius. The number of regimes K
                                                              b is the most frequent value

of Kact , and the regime path and radii are taken from the Dahl draw, the draw with K
                                                                                    b

regimes whose period co-clustering matrix is closest in Frobenius norm to its average over
the draws. Team tiers are summarized season by season: in the draws where the season
belongs to its Dahl regime, the tiers of a draw are its groups of exactly equal abilities, the
estimated tiers are the SALSO estimate of these partitions (Dahl et al., 2022), and abilities
are posterior means averaged within tiers. Home effects are summarized by posterior means,
and mixing is assessed with trace plots, split-R
                                               b and effective sample sizes (Appendix H).


5.2    Simulation Validation
We simulate from the model to check recovery of the regime path, the radii, the home effect
and the within-season tiers, and to check that seasons with the same radius but different
tier structures are assigned to the same regime. Eight settings cross the number of regimes
(radii 200 and 400, or 100, 200 and 400), the number of seasons (T = 20 or 40) and the
within-regime ability structure, with 50 replicates each. Every season has 20 teams and 380
three-outcome matches in a double round robin. In the heterogeneous settings one regime
alternates between a two-tier and a three-tier configuration with the same radius. Mean
regime-path adjusted Rand index (ARI) is at least 0.985 in every setting, heterogeneous

                                             23
ones included, so seasons sharing a radius are almost always placed in the same regime,
whatever their tiers. This is because regimes share only a radius: each season is allocated
according to how well its own abilities fit under each regime’s radius, not according to
its tier structure. The number of regimes is recovered in 92–98% of two-regime replicates
and in 84–94% of three-regime replicates. Each miss adds one regime, which in 26 of the
28 misses absorbs only one or two seasons. Radius estimates concentrate near their true
values (Figure S1), home-effect mean squared error is 0.013–0.016, and mean tier ARI is
0.84–0.94, lower than for the regime path, because each regime pools information across
several seasons whereas the tiers of a season are estimated from its 380 matches alone.
Equal-tailed 95% credible intervals cover the true home effects in 93–96% of cases and the
true abilities in 97–99%, and the smallest set of regime counts holding 95% of the draws
contains the true number in 98–100% of replicates (Appendix E.4).
   Thinning the schedule separates regime identification from estimation precision. In
the two-regime setting with T = 20, retaining each match independently with probability
p ∈ {1.0, 0.9, 0.8, 0.7, 0.6} leaves regime recovery almost unchanged: the number of regimes
is recovered in 98–100% of replicates and mean regime-path ARI stays above 0.98 with
40% of matches removed. Each regime persists for five seasons, so even 228 matches per
season leave enough information to place every season. The loss falls instead on estimation
precision, with ability mean squared error rising from 0.026 to 0.074, mean tier ARI falling
from 0.94 to 0.89 and the radius estimates spreading out. Appendix E gives the designs,
the full results (Table S2) and the missing-data analysis (Table S3). Appendix F gives the
computational settings.




                                            24
6    Competitive Balance in the English Premier League
We fit the model to the 25 Premier League seasons described in Section 2, with the same
model and sampler as in the simulations. Hyperparameters were set by running short
pilot chains and then comparing neighboring configurations with match-level conditional
WAIC, which led to (σβ , ar , br ) = (2, 10, 200), where σβ is the prior standard deviation of
the auxiliary abilities. Nearby configurations gave very similar WAIC values, so we treat
this as a stable local choice rather than a uniquely optimal one. We ran two chains of
50,000 iterations each, discarded the first 5,000 of each as burn-in, and retained 90,000
draws. The threshold was fixed at κ2 = 0.65, home effects had independent N (0, 1) priors,
and posterior summaries follow Appendix C.3. Convergence diagnostics are reported in
Appendix H. Figure 2 summarizes the results.


(Q1) Has competitive balance changed, and when? The results suggest a persis-
tent shift toward greater structural inequality beginning in the mid-2000s. The sampler
favors two competitive regimes, which are occupied in 67.4% of retained draws. The Dahl-
representative radii are 97.1 for the relatively balanced State 1 and 155.4 for the more
stratified State 2. All seasons from 1995/96 through 2004/05 are assigned to State 1,
followed by a transition to State 2 in 2005/06. The league remains in State 2 for five
consecutive seasons, briefly returns to State 1 in 2010/11, and is assigned to State 2 from
2011/12 onward. Conditional on two regimes, the estimated self-transition frequencies are
0.71 and 0.85 for States 1 and 2, respectively, indicating greater persistence in the more
stratified regime. These findings suggest a sustained change in league-wide competitive
structure rather than isolated fluctuations in seasonal outcomes. The timing is consistent
with previous evidence of increasing competitive inequality in English football during the
mid-2000s (Basini et al., 2023).

                                             25
                                         160                                                                                                                                                                                                                                                                                                                                                                                                                        Posterior mean
                                                                                                                                                                                                                                                                                     0.8                                                                                                                                                                            90% CrI




            Competitive-balance radius




                                                                                                                                                                                                                                                             Home-advantage effect
                                         140
                                                                                                                                                                                                                                                                                     0.6



                                         120
                                                                                                                                                                                                                                                                                     0.4


                                                                                                                                                                                                                          Dahl radius
                                         100
                                                                                                                                                                                                                          90% CrI
                                                                                                                                                                                                                                                                                     0.2
                                                                                                                                                                                                                          Posterior median
                                                                                                                                                                                                                  State
                                         80                                                                                                                                                                       1     2
                                                                                                                                                                                                                                                                                     0.0
                                                      6

                                                            7

                                                                    8

                                                                             9

                                                                                     0

                                                                                           1

                                                                                                   2

                                                                                                            3

                                                                                                                  4

                                                                                                                          5

                                                                                                                                   6

                                                                                                                                           7

                                                                                                                                                 8

                                                                                                                                                         9

                                                                                                                                                                  0

                                                                                                                                                                        1
                                                                                                                                                                              12

                                                                                                                                                                                       3

                                                                                                                                                                                               4

                                                                                                                                                                                                     5

                                                                                                                                                                                                             6

                                                                                                                                                                                                                      7

                                                                                                                                                                                                                            8

                                                                                                                                                                                                                                    9

                                                                                                                                                                                                                                             0




                                                                                                                                                                                                                                                                                                6

                                                                                                                                                                                                                                                                                                      7

                                                                                                                                                                                                                                                                                                              8

                                                                                                                                                                                                                                                                                                                    9

                                                                                                                                                                                                                                                                                                                            0

                                                                                                                                                                                                                                                                                                                                  1

                                                                                                                                                                                                                                                                                                                                          2

                                                                                                                                                                                                                                                                                                                                                3

                                                                                                                                                                                                                                                                                                                                                        4

                                                                                                                                                                                                                                                                                                                                                               5

                                                                                                                                                                                                                                                                                                                                                                      6

                                                                                                                                                                                                                                                                                                                                                                               7

                                                                                                                                                                                                                                                                                                                                                                                     8

                                                                                                                                                                                                                                                                                                                                                                                             9

                                                                                                                                                                                                                                                                                                                                                                                                   0

                                                                                                                                                                                                                                                                                                                                                                                                         1
                                                                                                                                                                                                                                                                                                                                                                                                             12

                                                                                                                                                                                                                                                                                                                                                                                                                       3

                                                                                                                                                                                                                                                                                                                                                                                                                              4

                                                                                                                                                                                                                                                                                                                                                                                                                                     5

                                                                                                                                                                                                                                                                                                                                                                                                                                             6

                                                                                                                                                                                                                                                                                                                                                                                                                                                    7

                                                                                                                                                                                                                                                                                                                                                                                                                                                             8

                                                                                                                                                                                                                                                                                                                                                                                                                                                                        9

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        0
                                                                                                                                                                      –1




                                                                                                                                                                                                                                                                                                                                                                                                       –1
                                                  –9

                                                          –9

                                                                   –9

                                                                         –9

                                                                                 –0

                                                                                         –0

                                                                                               –0

                                                                                                        –0

                                                                                                                –0

                                                                                                                         –0

                                                                                                                               –0

                                                                                                                                       –0

                                                                                                                                               –0

                                                                                                                                                     –0

                                                                                                                                                              –1




                                                                                                                                                                                   –1

                                                                                                                                                                                           –1

                                                                                                                                                                                                   –1

                                                                                                                                                                                                         –1

                                                                                                                                                                                                                  –1

                                                                                                                                                                                                                          –1

                                                                                                                                                                                                                                   –1

                                                                                                                                                                                                                                         –2




                                                                                                                                                                                                                                                                                            –9

                                                                                                                                                                                                                                                                                                    –9

                                                                                                                                                                                                                                                                                                          –9

                                                                                                                                                                                                                                                                                                                  –9

                                                                                                                                                                                                                                                                                                                        –0

                                                                                                                                                                                                                                                                                                                                –0

                                                                                                                                                                                                                                                                                                                                      –0

                                                                                                                                                                                                                                                                                                                                              –0

                                                                                                                                                                                                                                                                                                                                                     –0

                                                                                                                                                                                                                                                                                                                                                            –0

                                                                                                                                                                                                                                                                                                                                                                    –0

                                                                                                                                                                                                                                                                                                                                                                           –0

                                                                                                                                                                                                                                                                                                                                                                                   –0

                                                                                                                                                                                                                                                                                                                                                                                         –0

                                                                                                                                                                                                                                                                                                                                                                                                 –1




                                                                                                                                                                                                                                                                                                                                                                                                                   –1

                                                                                                                                                                                                                                                                                                                                                                                                                           –1

                                                                                                                                                                                                                                                                                                                                                                                                                                  –1

                                                                                                                                                                                                                                                                                                                                                                                                                                         –1

                                                                                                                                                                                                                                                                                                                                                                                                                                                   –1

                                                                                                                                                                                                                                                                                                                                                                                                                                                         –1

                                                                                                                                                                                                                                                                                                                                                                                                                                                                     –1

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    –2
                                                                                                                                                                            –




                                                                                                                                                                                                                                                                                                                                                                                                              –
                                                                                                                                                                   10




                                                                                                                                                                                                                                                                                                                                                                                                      10
                                                 95

                                                       96

                                                               97

                                                                        98

                                                                              99

                                                                                      00

                                                                                              01

                                                                                                       02

                                                                                                             03

                                                                                                                     04

                                                                                                                              05

                                                                                                                                    06

                                                                                                                                            07

                                                                                                                                                    08

                                                                                                                                                             09



                                                                                                                                                                         11

                                                                                                                                                                                12

                                                                                                                                                                                        13

                                                                                                                                                                                                14

                                                                                                                                                                                                        15

                                                                                                                                                                                                                 16

                                                                                                                                                                                                                       17

                                                                                                                                                                                                                               18

                                                                                                                                                                                                                                        19




                                                                                                                                                                                                                                                                                           95

                                                                                                                                                                                                                                                                                                 96

                                                                                                                                                                                                                                                                                                         97

                                                                                                                                                                                                                                                                                                               98

                                                                                                                                                                                                                                                                                                                       99

                                                                                                                                                                                                                                                                                                                             00

                                                                                                                                                                                                                                                                                                                                     01

                                                                                                                                                                                                                                                                                                                                           02

                                                                                                                                                                                                                                                                                                                                                   03

                                                                                                                                                                                                                                                                                                                                                          04

                                                                                                                                                                                                                                                                                                                                                                 05

                                                                                                                                                                                                                                                                                                                                                                          06

                                                                                                                                                                                                                                                                                                                                                                                07

                                                                                                                                                                                                                                                                                                                                                                                        08

                                                                                                                                                                                                                                                                                                                                                                                              09



                                                                                                                                                                                                                                                                                                                                                                                                           11

                                                                                                                                                                                                                                                                                                                                                                                                                  12

                                                                                                                                                                                                                                                                                                                                                                                                                        13

                                                                                                                                                                                                                                                                                                                                                                                                                                14

                                                                                                                                                                                                                                                                                                                                                                                                                                       15

                                                                                                                                                                                                                                                                                                                                                                                                                                              16

                                                                                                                                                                                                                                                                                                                                                                                                                                                        17

                                                                                                                                                                                                                                                                                                                                                                                                                                                                18

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                19
                                                                                                                                               Season                                                                                                                                                                                                                              Season




                                                                                                                                                                                                                                                                                                                                                                               2010–11 Premier League
                                                                                                                                                                                                                                                                                                                  MUN

                                                                                                                                                                                                                                                                                                                    MCI

                                                                                                                                                                                                                                                                                                                  CHE

             MUN                                                                                                                                                                                                                                                                                                  ARS
                ARS                                                                                                                                                                                                                                                                                               TOT
                CHE
                                                                                                                                                                                                                                                                                                                    LIV
                         LIV
                     MCI                              ×        ×        ×        ×                 ×                                                                                                                                                                                                              EVE
                  TOT
                                                                                                                                                                                                                                                                                     Stronger                     FUL
                SHU                          ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×                 ×        ×       ×        ×       ×       ×         ×        ×        ×        ×        ×   ×
                                                                                                                                                                                                                                                                                                                    AVL
                   LEE                                                                                                        ×        ×        ×        ×        ×       ×        ×       ×       ×         ×        ×        ×        ×        ×   ×   ×

               BHA                           ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×       ×        ×       ×       ×         ×        ×        ×        ×                                                                         SUN

                        IPS                  ×        ×        ×        ×        ×                          ×        ×        ×        ×        ×        ×        ×       ×        ×       ×       ×         ×        ×        ×        ×        ×   ×   ×                                                        WBA
            NEW                                                                                                                                                           ×                                                             ×
                                                                                                                                                                                                                                                                                                                  NEW
                  EVE
                                                                                                                                                                                                                                                                                                                  BOL
                         LEI                 ×                                                              ×                 ×        ×        ×        ×        ×       ×        ×       ×       ×         ×

                   AVL                                                                                                                                                                                                                  ×        ×   ×                                                            STK
                 WIM                                                                      ×        ×        ×        ×        ×        ×        ×        ×        ×       ×        ×       ×       ×         ×        ×        ×        ×        ×   ×   ×
                                                                                                                                                                                                                                                                                                                  WIG
                                                                                                                                                                                                                                                                                                                                                                                                                                                                90% CrI
               BUR                           ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×                ×       ×       ×         ×                 ×
                                                                                                                                                                                                                                                                                                                  BLA                                                                                                                                           Posterior mean
               COV                                                                                 ×        ×        ×        ×        ×        ×        ×        ×       ×        ×       ×       ×         ×        ×        ×        ×        ×   ×   ×
                                                                                                                                                                                                                                                                                                                                                                                                                                                                Tier ability
               SOU                                                                                                                     ×        ×        ×        ×       ×        ×       ×                                                                                                                        BIR
            SHW                                                                           ×        ×        ×        ×        ×        ×        ×        ×        ×       ×        ×       ×       ×         ×        ×        ×        ×        ×   ×   ×
                                                                                                                                                                                                                                                                                                                  BLP                                                                                                                                   Tier (1 = strongest)
                DER                          ×                                                              ×        ×        ×        ×        ×                 ×       ×        ×       ×       ×         ×        ×        ×        ×        ×   ×   ×                                                                                                                                                                                              1       2       3       4       5    6
                                                                                                                                                                                                                                                                                                                  WOL
            WOL                              ×        ×        ×        ×        ×        ×        ×        ×                 ×        ×        ×        ×        ×                                ×         ×        ×        ×        ×        ×

                REA                          ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×                          ×       ×        ×       ×                 ×        ×        ×        ×        ×   ×   ×                                                        WHU
     Team




            WHU                                                                                                      ×        ×                                                            ×
                                                                                                                                                                                                                                                                                                                                  −1.0                      −0.5                     0.0                     0.5                       1.0                              1.5
                     MID                                       ×                                                                                                          ×        ×       ×       ×         ×        ×        ×                 ×   ×   ×
                                                                                                                                                                                                                                                                                                                                                                                             Latent ability
                 BLA                                                             ×        ×                                                                                                        ×         ×        ×        ×        ×        ×   ×   ×

                CRY                          ×        ×                 ×        ×        ×        ×        ×        ×                 ×        ×        ×        ×       ×        ×       ×       ×

               CHA                           ×        ×        ×                 ×                                                                       ×        ×       ×        ×       ×       ×         ×        ×        ×        ×        ×   ×   ×

              BOU                            ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×       ×        ×       ×       ×         ×        ×

                      BIR                    ×        ×        ×        ×        ×        ×        ×                                            ×                 ×                        ×       ×         ×        ×        ×        ×        ×   ×   ×
                                                                                                                                                                                                                                                                                                                                                                               2006–07 Premier League
               BRA                           ×        ×        ×        ×                          ×        ×        ×        ×        ×        ×        ×        ×       ×        ×       ×       ×         ×        ×        ×        ×        ×   ×   ×
                                                                                                                                                                                                                                                                                                                  MUN
                NFO                                            ×                 ×        ×        ×        ×        ×        ×        ×        ×        ×        ×       ×        ×       ×       ×         ×        ×        ×        ×        ×   ×   ×

                  WIG                        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×                                                                              ×        ×        ×        ×        ×   ×   ×                                                        CHE
                BOL                                   ×                 ×        ×        ×                                                                                                        ×         ×        ×        ×        ×        ×   ×   ×
                                                                                                                                                                                                                                                                                                                  ARS
                   FUL                       ×        ×        ×        ×        ×        ×                                                                                                                           ×        ×        ×        ×       ×
                                                                                                                                                                                                                                                                                                                    LIV
                  STK                        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×                                                                                           ×   ×

                SUN                          ×                 ×        ×                                            ×        ×                 ×                                                                                                ×   ×   ×                                                        EVE
             SWA                             ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×       ×        ×                                                                 ×   ×
                                                                                                                                                                                                                                                                                                                  TOT
               WAT                           ×        ×        ×        ×                 ×        ×        ×        ×        ×        ×                 ×        ×       ×        ×       ×       ×         ×        ×
                                                                                                                                                                                                                                                                                                                  POR
               POR                           ×        ×        ×        ×        ×        ×        ×        ×                                                                      ×       ×       ×         ×        ×        ×        ×        ×   ×   ×

               QPR                                    ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×       ×        ×                         ×                 ×        ×        ×   ×   ×                                                        REA

               CAR                           ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×       ×        ×       ×       ×                  ×        ×        ×        ×       ×                           Weaker                       BOL
              NOR                            ×        ×        ×        ×        ×        ×        ×        ×        ×                 ×        ×        ×        ×       ×        ×                                  ×                 ×        ×   ×
                                                                                                                                                                                                                                                                                                                    AVL
            WBA                              ×        ×        ×        ×        ×        ×        ×                 ×                          ×        ×                ×                                                                          ×   ×

                 HUL                         ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×                         ×       ×       ×                           ×                 ×   ×   ×                                                        BLA

               BAR                           ×        ×                 ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×       ×        ×       ×       ×         ×        ×        ×        ×        ×   ×   ×                                                          MID
                  BLP                        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×       ×                ×       ×         ×        ×        ×        ×        ×   ×   ×
                                                                                                                                                                                                                                                                                                                  NEW
               HUD                           ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×        ×       ×        ×       ×       ×         ×        ×        ×        ×                ×
                                                                                                                                                                                                                                                                                                                  FUL
                                         6

                                                  7

                                                          8

                                                                    9

                                                                             0

                                                                                      1

                                                                                               2

                                                                                                        3

                                                                                                                4

                                                                                                                          5

                                                                                                                                   6

                                                                                                                                            7

                                                                                                                                                     8

                                                                                                                                                              9

                                                                                                                                                                      0

                                                                                                                                                                              1

                                                                                                                                                                              2

                                                                                                                                                                               3

                                                                                                                                                                               4

                                                                                                                                                                               5

                                                                                                                                                                               6

                                                                                                                                                                               7

                                                                                                                                                                               8

                                                                                                                                                                               9

                                                                                                                                                                               0




                                                                                                                                                                                                                                                                                                                                                                                                                                                                    90% CrI
                                                                                                                                                                            –1
                              –9

                                             –9

                                                        –9

                                                                 –9

                                                                          –0

                                                                                   –0

                                                                                           –0

                                                                                                     –0

                                                                                                              –0

                                                                                                                       –0

                                                                                                                                –0

                                                                                                                                         –0

                                                                                                                                                 –0

                                                                                                                                                           –0

                                                                                                                                                                    –1




                                                                                                                                                                            –1

                                                                                                                                                                            –1

                                                                                                                                                                            –1

                                                                                                                                                                            –1

                                                                                                                                                                            –1

                                                                                                                                                                            –1

                                                                                                                                                                            –1

                                                                                                                                                                            –1

                                                                                                                                                                            –2




                                                                                                                                                                                                                                                                                                                    MCI
                                                                                                                                                                         10
                            95

                                           96

                                                      97

                                                               98

                                                                        99

                                                                                 00

                                                                                         01

                                                                                                   02

                                                                                                            03

                                                                                                                     04

                                                                                                                              05

                                                                                                                                       06

                                                                                                                                               07

                                                                                                                                                         08

                                                                                                                                                                  09




                                                                                                                                                                         11

                                                                                                                                                                         12

                                                                                                                                                                         13

                                                                                                                                                                         14

                                                                                                                                                                         15

                                                                                                                                                                         16

                                                                                                                                                                         17

                                                                                                                                                                         18

                                                                                                                                                                         19




                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Posterior mean
                                                                                                                                                Season                                                                                                                                                            WHU                                                                                                                                               Tier ability

                                                                                                                                                                                                                                                                                                                  WIG
                                                                                                                                                                                                                                                                                                                                                                                                                                                        Tier (1 = strongest)
                                                                                                                                                                                                                                                                                                                  SHU                                                                                                                                       1       2       3       4       5
                                                                                                                                                                                                                                                                                                                                                                                                                                                            6       7       8       9       10
                                                                                                                                                                                                                                                                                                                  CHA

                                                                                                                                                                                                                                                                                                                  WAT

                                                                                                                                                                                                                                                                                                                            −1.5              −1.0                 −0.5              0.0               0.5              1.0                  1.5                    2.0                          2.5

                                                                                                                                                                                                                                                                                                                                                                                             Latent ability




Figure 2: Posterior summaries for the English Premier League, 1995/96 to 2019/20. Upper
panels: season-specific competitive-balance radius and home-advantage effect with 90%
credible intervals. Lower left: longitudinal team tiers, with crosses marking seasons in
which a club was not in the league. Right: team abilities and tiers for 2010/11 (State 1)
and 2006/07 (State 2); circles are posterior means, segments 90% credible intervals, and
triangles tier-level estimates.

                                                                                                                                                                                                                                                     26
   Importantly, a common competitive regime does not imply an unchanged team hierar-
chy. Figure 2 shows that the identities of leading clubs vary considerably within State 2,
from Manchester United, Chelsea, Arsenal, and Liverpool in earlier seasons to Manchester
City and Tottenham Hotspur in later periods. Leicester City reaches the leading tier dur-
ing its 2015/16 championship season, while Liverpool does so in 2019/20, although both
seasons belong to the same more stratified regime.


(Q2) Which teams can the data tell apart? The inferred tiers reveal differences in
the granularity of team hierarchies across seasons. In the relatively balanced 2010/11 sea-
son, the representative partition contains six tiers, with Manchester United occupying the
leading tier, followed by Manchester City, Chelsea, Arsenal, and Tottenham Hotspur, and
a broad lower tier containing many of the remaining clubs. Only three points separated
second-placed Chelsea from fourth-placed Arsenal in the final standings. This relatively
compressed hierarchy is qualitatively consistent with Basini et al. (2023), who report a
79.9% posterior probability of a single-block structure in 2010/11, compared with proba-
bilities exceeding 95% for two blocks in the adjacent seasons. Their competitive blocks and
our latent ability tiers, however, represent different statistical quantities. In contrast, the
more stratified 2006/07 season contains ten representative tiers, with a 61-point difference
between champions Manchester United and last-placed Watford.
   The 2006/07 season also illustrates the information provided by opponent-specific com-
parisons. Arsenal and Liverpool both finished with 68 points, with Liverpool placed third
on goal difference. Nevertheless, the representative hierarchy places Arsenal in a stronger
tier. Arsenal defeated champions Manchester United in both league meetings, whereas
Liverpool lost both. These results illustrate differences in performance against a common
opponent that are not reflected in aggregate point totals. While these head-to-head results


                                              27
are illustrative rather than conclusive, the model estimates relative strengths using the full
network of match outcomes.


(Q3) Is structural balance distinct from title-race closeness and home advan-
tage? The results suggest that these dimensions of competition evolve differently. In
2011/12, Manchester City and Manchester United finished level on 89 points, with the
championship decided on goal difference. Nevertheless, the season is assigned to the more
stratified regime, while third-placed Arsenal finished 19 points behind the leading pair.
This illustrates that a closely contested title race can coexist with substantial league-wide
inequality. The structural radius characterizes dispersion in latent abilities across all teams
rather than the competitive gap between the leading contenders.
   Home advantage exhibits a distinct temporal pattern. The estimated home effect is
positive in every season, with posterior means ranging from approximately 0.27 in 2015/16
to 0.69 in 2009/10, and all reported 90% credible intervals excluding zero. Home advan-
tage is generally smaller after 2011/12, whereas the league remains in the more stratified
regime throughout this period. These findings suggest that changes in home advantage and
structural competitive balance need not coincide, supporting their separate representation
within the paired-comparison framework.


Implications. The EPL analysis illustrates the value of distinguishing structural com-
petitive balance from descriptive measures based on final standings. The regime-specific
radius provides an interpretable measure of league-wide latent ability dispersion, while the
inferred tiers identify groups of clubs with similar competitive strengths. Together, these
quantities provide complementary information about when competitive inequality changes
and how team hierarchies evolve. Such evidence can inform discussions of revenue sharing,



                                              28
financial regulation, and competition design, although the present findings are descriptive
rather than causal. Historical developments in English football provide context for the
inferred regimes but are not included as explanatory variables in the model. A comple-
mentary analysis of the National Basketball Association, a closed league with different
institutional mechanisms for promoting competitive balance, is presented in the Supple-
mentary Material (Appendix G) and illustrates recurrent switching between competitive
regimes rather than a single sustained shift.



7     Discussion
We treat competitive balance as a property of teams rather than season outcomes. Abilities
are generated by projecting a Gaussian draw onto a graph-fused ℓ1 polytope: when the
constraint binds, its radius equals the realized total of pairwise ability gaps, and because
the projection lands on a face with positive probability, the model supports exact ties and
posterior probabilities for rank tiers. Near parity, the radius connects the signal-to-noise
ratio of Lopez et al. (2018), a structural Gini coefficient, and the number of matches needed
to detect a departure from parity. Applied to the Premier League, the fitted model favors
two eras, with a lasting shift toward greater stratification in 2005/06 and only one later
return to the compressed regime, in 2010/11; the tiers also capture information missed by
the standings, such as head-to-head results between clubs level on points. In the NBA,
regimes alternate rather than shift once, and the home effect is smallest in the attendance-
restricted 2020/21 season.
    The approach has limitations. The radius measures inequality in team abilities, not
outcomes, so outcome-based indices may remain more useful for predictive balance; abil-
ities are fixed within seasons; victory margins are reduced to three ordered categories;


                                                29
within-era drift is absorbed into regime changes; the regime summaries come from an ap-
proximate allocation kernel whose invariant distribution is not established; the number of
regimes depends on γ and λ; and each likelihood evaluation requires a quadratic program
that will become costly for larger comparison graphs. Natural extensions address several
of these points directly. Letting the radius depend on covariates such as revenue sharing or
spending regulation would allow associations between regulatory or institutional changes
and structural balance to be estimated, although causal evaluation of such policies would
require additional identification assumptions. Because the likelihood is defined on an arbi-
trary comparison graph, the schedule itself becomes a design variable: given an estimated
radius and ability vector, one can evaluate proposed formats—balanced versus unbalanced
schedules, playoff cut lines, group-stage draws, seeding rules—by the distribution of termi-
nal ranks and title probabilities they induce, and search over formats for a target trade-off
between fairness and suspense (Szymanski, 2003; Groh et al., 2012; Kendall and Lenten,
2017). An ordinal or continuous margin model would likewise recover information the
three-category outcome discards and would let the framework speak to in-game compet-
itive balance rather than only ex ante balance, which matters for broadcast economics,
where suspense within a match drives viewership (Ely et al., 2015); a richer outcome scale
would also sharpen the home-effect estimates, extracting more signal from the attendance-
restricted 2020/21 season, a rare natural experiment on crowd effects (Bryson et al., 2021).
Finally, the prior applies unchanged beyond team sports. Chess, esports, grant review, and
language-model preference data all involve paired comparisons in which genuine ties mat-
ter, and faster projection approximations or variational methods would help make these
applications practical.




                                             30
References
Baio, G. and M. Blangiardo (2010). Bayesian hierarchical model for the prediction of
  football results. Journal of Applied Statistics 37 (2), 253–264.
Basini, F., V. Tsouli, I. Ntzoufras, and N. Friel (2023). Assessing competitive balance in
  the English Premier League for over forty seasons using a stochastic block model. Journal
  of the Royal Statistical Society: Series A (Statistics in Society) 186 (3), 530–556.
Best, M. J. (1996). An algorithm for the solution of the parametric quadratic programming
  problem. In H. Fischer, B. Riedmüller, and S. Schäffler (Eds.), Applied Mathematics and
  Parallel Computing, pp. 57–76. Physica-Verlag, Heidelberg.
Boulesteix, A.-L. and M. Slawski (2009). Stability and aggregation of ranked gene lists.
  Briefings in Bioinformatics 10 (5), 556–568.
Bradley, R. A. and M. E. Terry (1952). Rank analysis of incomplete block designs: I. The
  method of paired comparisons. Biometrika 39 (3/4), 324–345.
Bryson, A., P. Dolton, J. J. Reade, D. Schreyer, and C. Singleton (2021). Causal effects of
  an absent crowd on performances and refereeing decisions during Covid-19. Economics
  Letters 198, 109664.
Busse, L. M., P. Orbanz, and J. M. Buhmann (2007). Cluster analysis of heterogeneous
  rank data. In Proceedings of the 24th International Conference on Machine Learning,
  pp. 113–120.
Cairns, J. (1987). Evaluating changes in league structure: the reorganization of the Scottish
  football league. Applied Economics 19 (2), 259–275.
Caron, F. and A. Doucet (2012). Efficient Bayesian inference for generalized Bradley–Terry
  models. Journal of Computational and Graphical Statistics 21 (1), 174–196.
Cattelan, M., C. Varin, and D. Firth (2013). Dynamic Bradley–Terry modelling of sports
  tournaments. Journal of the Royal Statistical Society Series C: Applied Statistics 62 (1),
  135–150.
Dahl, D. B., D. J. Johnson, and P. Müller (2022). Search algorithms and loss functions for
 bayesian clustering. Journal of Computational and Graphical Statistics 31 (4), 1189–1201.
Davidson, R. R. (1970). On extending the Bradley-Terry model to accommodate ties in


                                             31
  paired comparison experiments. Journal of the American Statistical Association 65 (329),
  317–328.
Deng, K., S. Han, K. J. Li, and J. S. Liu (2014). Bayesian aggregation of order-based rank
  data. Journal of the American Statistical Association 109 (507), 1023–1039.
Dunson, D. B. and S. D. Peddada (2008). Bayesian nonparametric inference on stochastic
 ordering. Biometrika 95 (4), 859–874.
Ely, J., A. Frankel, and E. Kamenica (2015). Suspense and surprise. Journal of Political
  Economy 123 (1), 215–260.
Fang, S., R. Han, Y. Luo, and Y. Xu (2026). Recent advances in the Bradley–Terry model:
  theory, algorithms, and applications. arXiv:2601.14727.
Fort, R. and J. Maxcy (2003). Competitive balance in sports leagues: an introduction.
  Journal of Sports Economics 4 (2), 154–160.
Fort, R. and J. Quirk (1995). Cross-subsidization, incentives, and outcomes in professional
  team sports leagues. Journal of Economic Literature 33 (3), 1265–1299.
Glickman, M. E. (1999). Parameter estimation in large dynamic paired comparison ex-
  periments. Journal of the Royal Statistical Society Series C: Applied Statistics 48 (3),
  377–394.
Goldstein, H. and D. J. Spiegelhalter (1996). League tables and their limitations: statis-
 tical issues in comparisons of institutional performance. Journal of the Royal Statistical
 Society: Series A (Statistics in Society) 159 (3), 385–409.
Groh, C., B. Moldovanu, A. Sela, and U. Sunde (2012). Optimal seedings in elimination
  tournaments. Economic Theory 49 (1), 59–80.
Hong, Y. A., C. Liang, T. A. Radcliff, L. T. Wigfall, and R. L. Street (2019). What
  do patients say about doctors online? a systematic review of studies on patient online
  reviews. Journal of Medical Internet Research 21 (4), e12521.
Humphreys, B. R. (2002). Alternative measures of competitive balance in sports leagues.
 Journal of Sports Economics 3 (2), 133–148.
Hunter, D. R. (2004). MM algorithms for generalized Bradley-Terry models. The Annals
 of Statistics 32 (1), 384–406.



                                            32
Karlé, E. and H. Tyagi (2023). Dynamic ranking with the BTL model: a nearest neighbor
 based rank centrality method. Journal of Machine Learning Research 24 (269), 1–57.
Kendall, G. and L. J. A. Lenten (2017). When sports rules go awry. European Journal of
  Operational Research 257 (2), 377–394.
Koop, G. (2004). Modelling the evolution of distributions: an application to Major League
 Baseball. Journal of the Royal Statistical Society: Series A 167 (4), 639–655.
Leitner, C., A. Zeileis, and K. Hornik (2010). Forecasting sports tournaments by ratings
  of (prob) abilities: A comparison for the EURO 2008. International Journal of Forecast-
  ing 26 (3), 471–481.
Li, X., D. Yi, and J. S. Liu (2022). Bayesian analysis of rank data with covariates and
  heterogeneous rankers. Statistical Science 37 (1), 1–23.
Lopez, M. J., G. J. Matthews, and B. S. Baumer (2018). How often does the best team
  win? A unified approach to understanding randomness in North American sport. The
  Annals of Applied Statistics 12 (4), 2483–2516.
Luce, R. D. (1959). Individual Choice Behavior: A Theoretical Analysis. Wiley.
Ma, S. and J. Huang (2017). A concave pairwise fusion approach to subgroup analysis.
 Journal of the American Statistical Association 112 (517), 410–423.
Manasis, V., V. Avgerinou, I. Ntzoufras, and J. J. Reade (2013). Quantification of com-
 petitive balance in European football. IMA Journal of Management Mathematics 24 (3),
 363–375.
Manasis, V. and I. Ntzoufras (2014). Between-seasons competitive balance in European
 football: review of existing and development of specially designed indices. Journal of
 Quantitative Analysis in Sports 10 (2), 139–152.
Manasis, V., I. Ntzoufras, and J. J. Reade (2022). Competitive balance measures and the
 uncertainty of outcome hypothesis in European football. IMA Journal of Management
 Mathematics 33 (1), 19–52.
Marden, J. I. (1996). Analyzing and Modeling Rank Data. CRC Press.
Masarotto, G. and C. Varin (2012). The ranking lasso and its application to sport tourna-
 ments. The Annals of Applied Statistics 6 (4), 1949–1970.



                                           33
Maystre, L. and M. Grossglauser (2015). Fast and accurate inference of Plackett–Luce
 models. Advances in Neural Information Processing Systems 28, 172–180.
Miller, J. W. and M. T. Harrison (2018). Mixture models with a prior on the number of
 components. Journal of the American Statistical Association 113 (521), 340–356.
Mollica, C. and L. Tardella (2021). Bayesian analysis of ranking data with the Extended
 Plackett–Luce model. Statistical Methods & Applications 30 (1), 175–194.
Murphy, T. B. and D. Martin (2003). Mixtures of distance-based models for ranking data.
 Computational Statistics & Data Analysis 41 (3-4), 645–655.
Owen, P. D., M. Ryan, and C. R. Weatherston (2007). Measuring competitive balance
 in professional team sports using the Herfindahl–Hirschman index. Review of Industrial
 Organization 31 (4), 289–302.
Pearce, M. and E. A. Erosheva (2025a). Bayesian rank-clustering. Psychometrika 90 (3),
  904–931.
Pearce, M. and E. A. Erosheva (2025b). Modeling preferences: a Bayesian mixture of
  finite mixtures for rankings and ratings. Journal of the American Statistical Associa-
  tion 120 (551), 1621–1632.
Penn, R. and D. Berridge (2019). Competitive balance in the English Premier League.
  European Journal for Sport and Society 16 (1), 64–82.
Piancastelli, L. S. and N. Friel (2025). The clustered Mallows model. Statistics and Com-
  puting 35 (1), 21.
Picoto, W. N., R. Duarte, and I. Pinto (2019). Uncovering top-ranking factors for mobile
  apps through a multimethod approach. Journal of Business Research 101, 668–674.
Plumley, D., G. Ramchandani, and R. Wilson (2018). Mind the gap: an analysis of com-
  petitive balance in the English Football League system. International Journal of Sport
  Management and Marketing 18 (5), 357–375.
Rendle, S., C. Freudenthaler, Z. Gantner, and L. Schmidt-Thieme (2009). BPR: Bayesian
  personalized ranking from implicit feedback. In Proceedings of the Twenty-Fifth Confer-
  ence on Uncertainty in Artificial Intelligence, pp. 452–461.
Rockafellar, R. T. (1970). Convex Analysis. Princeton, NJ: Princeton University Press.



                                           34
Rottenberg, S. (1956). The baseball players’ labor market. Journal of Political Econ-
  omy 64 (3), 242–258.
Schmidt, M. (2001). Competition in Major League Baseball: the impact of expansion.
  Applied Economics Letters 8 (1), 21–26.
She, Y. (2010). Sparse regression with exact clustering. Electronic Journal of Statistics 4,
  1055–1096.
Szymanski, S. (2001). Income inequality, competitive balance and the attractiveness of
  team sports: some evidence and a natural experiment from English soccer. Economic
  Journal 111 (469), F69–F84.
Szymanski, S. (2003). The economic design of sporting contests. Journal of Economic
  Literature 41 (4), 1137–1187.
Tian, X., J. Shi, X. Shen, and K. Song (2024). A spectral approach for the dynamic
  Bradley–Terry model. Stat 13 (3), e722.
Tibshirani, R., M. Saunders, S. Rosset, J. Zhu, and K. Knight (2005). Sparsity and smooth-
  ness via the fused lasso. Journal of the Royal Statistical Society Series B: Statistical
  Methodology 67 (1), 91–108.
Usher, A. and M. Savino (2009). A global survey of university ranking and league tables.
  In The Routledge International Handbook of Higher Education, pp. 255–264. Routledge.
Utt, J. and R. Fort (2002). Pitfalls to measuring competitive balance with Gini coefficients.
  Journal of Sports Economics 3 (4), 367–373.
Vrooman, J. (1995). A general theory of professional sports leagues. Southern Economic
  Journal 61 (4), 971–990.
Xu, M. and L. L. Duan (2023). Bayesian inference with the ℓ1 -ball prior: solving com-
 binatorial problems with exact zeros. Journal of the Royal Statistical Society Series B:
 Statistical Methodology 85 (5), 1538–1560.
Zhang, Y., X. Feng, Y. Wu, and J. Xiao (2018). The dynamics of online ratings with
  heterogeneous preferences in online review platform. Chaos, Solitons & Fractals 109,
  26–30.
Zimbalist, A. (2002). Competitive balance in sports leagues: an introduction. Journal of
  Sports Economics 3 (2), 111–121.

                                             35
                      Supplementary Material
Appendices A–H form the Supplementary Material referred to in the main text.



A      Proofs for Section 3
This appendix collects the proofs of the results stated in Section 3, together with Lemma A.1
on the reciprocal-radius summary. Throughout, H0 = {ϑ ∈ RN : 1⊤ ϑ = 0} denotes the
zero-sum subspace, H = IN − N −1 11⊤ the orthogonal projection onto it, and the period
index is suppressed where no ambiguity arises.

Proof of Theorem 3.1. Let Λ denote the collection of all primitive unknowns and let Q(dΛ)
denote their proper joint prior. The projection map (3) is the argmin of a strictly convex
function over a closed convex set depending continuously on (βt , rt ), hence is single valued
and continuous, and therefore Borel measurable; consequently Λ 7→ L(D | Λ) is measurable.
Every factor in (1) lies in (0, 1) for finite arguments, so


                               0 < L(D | Λ) ≤ 1      for every Λ,


where the upper bound holds because the likelihood is a product of probabilities. Therefore
the normalizing constant satisfies
                               Z                     Z
                      p(D) =       L(D | Λ)Q(dΛ) ≤       Q(dΛ) = 1 < ∞.


For the lower bound, L(D | ·) is strictly positive everywhere and Q is a probability measure,
so p(D) > 0 by monotone convergence applied to the sets {L ≥ 1/n}, whose union has



                                              36
Q-measure one. Hence 0 < p(D) < ∞ and the posterior Q(dΛ | D) = L(D | Λ)Q(dΛ)/p(D)
is a well-defined probability measure.

Proof of Proposition 3.2. Suppose (θ, η) and (θ′ , η ′ ) produce identical linear predictors. Let


                                    d = θ − θ′ ,        c = η ′ − η.


Then
                                           x⊤
                                            g d = −chg


for every comparison and 1⊤ d = 0.
    If c = 0, then di = dj for every compared pair. Connectivity implies that d is constant,
and the zero-sum constraint implies d = 0. If c ̸= 0, this contradicts the non-collinearity
condition of Proposition 3.2. Thus d = 0 and c = 0, which proves the first claim.
    For the second claim, fix a comparison g and write the observed cell probabilities as
(p−1 , p0 , p1 ). From (1),


                          σ(κ1 − ∆g ) = p−1 ,       σ(κ2 − ∆g ) = p−1 + p0 ,


and since σ is a strictly increasing bijection from R onto (0, 1) these determine κ1 − ∆g and
κ2 − ∆g uniquely. Hence the cell probabilities identify the two differences, and therefore
identify the gap κ2 − κ1 together with κ1 − ∆g . Under the anchoring κ1 = −κ2 we have
κ2 − κ1 = 2κ2 , so κ2 is identified, and then ∆g = κ1 − (κ1 − ∆g ) is identified for every g.
Applying the first claim to (∆g )G
                                 g=1 identifies (θ, η).

    For the final claim, suppose hg ≡ h is constant. Then ∆g (θ, η + c) = ∆g (θ, η) + ch for
every g, and replacing κ by κ + ch1 leaves both differences κ1 − ∆g and κ2 − ∆g , and hence
all cell probabilities, unchanged. The stated family is therefore observationally equivalent,


                                                   37
and the anchoring κ1 = −κ2 , κ2 > 0 selects one member of it.

Proof of Proposition 3.3. Write K = Kt (rt ) and let H0 = {ϑ : 1⊤ ϑ = 0}, a linear subspace
of dimension N − 1. Because the graph is connected, null(At ) ∩ H0 = {0}, so K is compact,
and it contains a relatively open neighborhood of the origin in H0 ; hence aff(K) = H0 and
dim K = N − 1.
   Existence of a face with a vanishing contrast. Since K is compact and convex it has an
extreme point v. Suppose, for contradiction, that (At v)e ̸= 0 for every e ∈ Et . Then the
signs se = sign{(At v)e } are locally constant, so on a neighborhood V of v in H0 the map
                                                         P
ϑ 7→ ∥At ϑ∥1 coincides with the linear functional ϑ 7→ e se (At ϑ)e . Consequently K ∩ V
coincides with the intersection of V with a closed half-space of H0 . Every point of such
an intersection lies in a relatively open segment contained in K whenever dim H0 − 1 =
N − 2 ≥ 1, contradicting extremality of v. Hence for N ≥ 3 some contrast vanishes at v,
and F = {v} is a face of the required type.
   Positive measure of RF . Let F be any nonempty face of K with dim F = d, let L denote
the direction space of aff(F ), so dim L = d, and let NF denote the normal cone to K at
any point of relint(F ), which does not depend on the choice of that point. By the standard
normal decomposition of Euclidean projection onto a closed convex set (Rockafellar, 1970,
Sec. 13),
                         RF = Π−1
                               K {relint(F )} = relint(F ) + NF ,


since ΠK (b) = x if and only if b − x ∈ NK (x). Because aff(K) = H0 , the normal cone
at a point of relint(F ) decomposes as NF = N                    eF ⊂ H0 ∩ L⊥ is the
                                             eF ⊕ span(1), where N

normal cone computed within H0 and has nonempty interior relative to H0 ∩ L⊥ , a space of
dimension N − 1 − d. Hence NF has nonempty interior relative to L⊥ , which has dimension
N − d. Choosing a relatively open subset B ⊂ relint(F ) of dimension d and a subset


                                              38
C ⊂ NF open in L⊥ , the sum B + C is open in RN = L ⊕ L⊥ and contained in RF .
Therefore RF has positive Lebesgue measure.
   Conclusion. Every b ∈ RF projects into relint(F ) and hence satisfies (At θt )e = 0. The
Gaussian auxiliary distribution has a strictly positive density on RN , so it assigns positive
probability to every set of positive Lebesgue measure, giving Pr(βt ∈ RF ) > 0 and hence
Pr{(At θt )e = 0 | rt } > 0.

Proof of Theorem 3.4. Among all vectors satisfying 1⊤ ϑ = 0, the unique minimizer of


                                          ∥ϑ − βt ∥22


is Hβt .
   If Zt ≤ r, then Hβt ∈ Kt (r), so it remains the unique minimizer under the additional
graph-variation constraint. Hence
                                         θt (r) = Hβt

and
                                      ∥At θt (r)∥1 = Zt .

   Now suppose Zt > r and write ϑ⋆ = θt (r). Suppose, for contradiction, that ∥At ϑ⋆ ∥1 < r.
The set
                     U = {ϑ ∈ H0 : ∥At ϑ∥1 < r},        H0 = {ϑ : 1⊤ ϑ = 0},

is open in H0 because ϑ 7→ ∥At ϑ∥1 is continuous, and ϑ⋆ ∈ U. Since ϑ⋆ minimizes the
convex function ϑ 7→ ∥ϑ − βt ∥22 over Kt (r) ⊃ U and lies in the open subset U of H0 , it
is a local minimizer of that function over all of H0 . A convex function has no strict local
minimizer other than its global minimizer, so ϑ⋆ minimizes ∥ϑ − βt ∥22 over H0 , whence



                                              39
ϑ⋆ = Hβt by uniqueness. But then


                               ∥At ϑ⋆ ∥1 = ∥At Hβt ∥1 = Zt > r,


contradicting ∥At ϑ⋆ ∥1 < r. The graph-variation constraint is therefore active, giving


                                        ∥At θt (r)∥1 = r.


Combining the two cases yields (4). For r = 0 and a connected graph, Kt (0) = {0} and
both sides of (4) vanish, so the identity also holds at the endpoint.

Proof of Corollary 3.5. By Theorem 3.4, ∥At θt (r)∥1 = min(r, Zt ) for the given βt , and
r 7→ min(r, Zt ) is nondecreasing, with min(r1 , Zt ) = r1 < min(r2 , Zt ) when r1 < Zt . This
gives the pathwise inequality ∥At θt (r1 )∥1 ≤ ∥At θt (r2 )∥1 and its strict version. Moreover
                                                Z r
                                min(r, Zt ) =         I(Zt > u) du,
                                                 0


and the integrand is nonnegative and jointly measurable, so Tonelli’s theorem gives Mt (r) =
                 Rr
E{min(r, Zt )} = 0 Pr(Zt > u) du, the identity in (5).
   It remains to establish the regularity claims. Since the graph has at least one edge
and null(At ) ∩ H0 = {0} under connectivity, At Hβt is a nondegenerate Gaussian vector on
the contrast space, so Zt = ∥At Hβt ∥1 is a norm of a nondegenerate Gaussian vector and
therefore has a continuous distribution on [0, ∞) with Pr(Zt = 0) = 0. Hence u 7→ Pr(Zt >
u) is continuous, and the fundamental theorem of calculus applied to this integral identity
yields that Mt is continuously differentiable on (0, ∞) with Mt′ (r) = Pr(Zt > r). Finally Zt
has unbounded support, because At Hβt ranges over all of the contrast space with positive
Gaussian density, so Pr(Zt > r) > 0 for every finite r, which gives Mt′ (r) > 0 in (5) and

                                                40
strict monotonicity of Mt .

Proof of Proposition 3.6. Introduce auxiliary variables u ∈ R|Et | and write the graph-
variation constraint as
                                −u ≤ At ϑ ≤ u,        1⊤ u ≤ r.

Together with 1⊤ ϑ = 0, the projection problem becomes a quadratic program in (ϑ, u)
whose objective 12 ∥ϑ − βt ∥22 is convex and whose constraints are linear with a right-hand
side that is affine in the scalar parameter r; only the single constraint 1⊤ u ≤ r involves
r. The objective is strictly convex in the ϑ-block and constant in u, so the optimal u is
not unique whenever 1⊤ u < r at the optimum; the optimal ϑ, however, is unique, since it
is the projection of βt onto the closed convex set Kt (r). All statements below refer to the
ϑ-block.
   By the theory of parametric quadratic programming with a right-hand side depending
affinely on a scalar (see, e.g., Best, 1996), the optimal-value function is piecewise quadratic
and the unique optimal ϑ(r) is a piecewise affine, Lipschitz continuous function of r: on
the set of r for which a given optimal basis (equivalently, a given active set together with
a choice of linearly independent active constraints) remains optimal, ϑ(r) solves a fixed
linear Karush–Kuhn–Tucker system whose right-hand side is affine in r, and is therefore
affine in r. Since there are finitely many candidate active sets, the interval [0, R] is covered
by finitely many maximal subintervals on which ϑ(r) is affine, which gives the partition
0 = b0 < b1 < · · · < bQ = R. Continuity across the breakpoints follows from continuity
of the projection map Kt (r) 7→ ΠKt (r) (βt ) in r, which in turn follows from continuity of
r 7→ Kt (r) in the Hausdorff metric together with nonexpansiveness of Euclidean projection.
   Within each segment, θti (r) − θtj (r) is a difference of affine functions of r and hence
affine. Such a function is either identically zero on the segment or has at most one zero in


                                              41
its interior, so on [0, R] the rank-tier partition changes at most finitely often, apart from
ties that persist throughout a segment.

Proof of Lemma 3.7. Let θ ∈ K1 be an extreme point and let u1 > · · · > up be its distinct
values, with multiplicities n1 , . . . , np summing to N . On the open region


     O = {ϑ : ϑ has value pattern (u′1 > · · · > u′p ) with the same block assignment},


identified with {u′ ∈ Rp : u′1 > · · · > u′p }, both constraints defining K1 are affine in u′ : the
zero-sum constraint reads l nl u′l = 0, and, because the complete-graph total variation is
                            P


                                            X
                                  ∥Aϑ∥1 =           nl nl′ (u′l − u′l′ ),
                                             l<l′


the constraint ∥Aϑ∥1 ≤ 1 is affine on O and is active at θ, since ∥Aθ∥1 = 1 for any extreme
point (a point with ∥Aθ∥1 < 1 lies in the relative interior of K1 and so is not extreme).
   Suppose p ≥ 3. The affine set

                       n          X             X                         o
                    A = u′ ∈ Rp :   nl u′l = 0,   nl nl′ (u′l − u′l′ ) = 1
                                       l                 l<l′


is defined by two linear equations, so dim A ≥ p − 2 ≥ 1. Since u ∈ A and O is open in Rp ,
there is ε > 0 and a direction d ̸= 0 with u ± εd ∈ A ∩ O. The corresponding vectors θ± lie
in K1 , are distinct, and satisfy θ = (θ+ + θ− )/2, contradicting extremality. Hence p ≤ 2. If
p = 1 the zero-sum constraint forces θ = 0, which has ∥Aθ∥1 = 0 ̸= 1. Therefore p = 2.
   Writing S for the block on which θ takes its larger value, the zero-sum and unit-variation




                                                    42
constraints determine θ uniquely up to sign and give

                                           1S − |S|N −1 1
                                    θ=±                   ,                                (1)
                                           |S| (N − |S|)

where 1S is the indicator vector of S: with k = |S| and d the gap between the two levels,
∥Aθ∥1 = k(N − k)d = 1 and the larger value is (N − k)d/N . Conversely, fix a nonempty
                                                                       P
proper subset S with k = |S| and consider the linear functional ϑ 7→      i∈S ϑi on K1 .
                     P P                            P            P             P
Summing the identity i∈S j ∈S/ (ϑi − ϑj ) = (N − k)   i∈S ϑi − k    / ϑj = N
                                                                  j ∈S            i∈S ϑi ,

which uses 1⊤ ϑ = 0, gives

        X            1 XX               1 XX               1 X               1
              ϑi =         (ϑi − ϑj ) ≤       |ϑi − ϑj | ≤       |ϑi − ϑj | ≤ .            (2)
        i∈S
                     N i∈S              N i∈S              N i<j             N
                          j ∈S
                            /                   j ∈S
                                                  /


Equality throughout forces ϑi ≥ ϑj for all i ∈ S, j ∈
                                                    / S, and ϑi = ϑj for all pairs lying inside
S or inside its complement, so ϑ is constant on each block; the zero-sum and unit-variation
constraints then pin it down as the vector (1). Hence that vector is the unique maximizer
       P
of ϑ 7→ i∈S ϑi over K1 , and a unique maximizer of a linear functional over a convex set is
an extreme point. The negatives are extreme by symmetry.
   Finally, taking S = {i} in (2) gives ϑi ≤ 1/N for every ϑ ∈ K1 , with equality at the
vector (1) for S = {i}. Hence supθ∈K1 θi = 1/N .

Lemma A.1 (Finiteness of the reciprocal-radius summary). Suppose the radius prior has
                     R∞
density pr satisfying 0 u−1 pr (u) du < ∞; a sufficient condition is pr (u) = O(ua−1 ) as
u ↓ 0 for some a > 1. Then E(rt−1 | D) < ∞ for every finite design. The condition fails
for the exponential radius prior of Section 4.1, whose density is positive at zero.

Proof of Lemma A.1. Write Λ for the full parameter as in Theorem 3.1. Since 0 < L(D |



                                              43
Λ) ≤ 1 and p(D) > 0,

                                         E{rt−1 L(D | Λ)}   E(rt−1 )
                         E(rt−1 | D) =                    ≤          ,
                                               p(D)          p(D)

where the expectations on the right are under the prior. Conditioning on st = k and
                                R∞
averaging, E(rt−1 ) = E(rk−1 ) = 0 u−1 pr (u) du < ∞ by assumption.

Proof of Theorem 3.8. Connectivity implies null(A) = span(1), so the linear map ϑ 7→ Aϑ
is injective on the zero-sum subspace H0 . Since H0 is finite dimensional, the two norms
ϑ 7→ ∥Aϑ∥1 and ϑ 7→ ∥ϑ∥∞ on H0 are equivalent, so there exists LA < ∞ with


                          ∥ϑ∥∞ ≤ LA ∥Aϑ∥1            for every ϑ ∈ H0 .


Applying this to θ(r) ∈ Kr ⊂ H0 and using ∥Aθ(r)∥1 ≤ r gives ∥θ(r)∥∞ ≤ LA r, which yields
θ(r) → 0 together with the stated uniform rate; no separate compactness or limit-point
argument is needed.
   For the binary model, |θi (r) − θj (r)| ≤ 2LA r → 0 and σ is continuous, so Pr(Yij = 1 |
θ(r)) = σ(θi − θj ) → σ(0) = 1/2. For the ordered model, ∆g = x⊤
                                                               g θ(r) + ηhg → ηhg , and

substituting into (1) gives the limiting cell probabilities stated in Theorem 3.8 by continuity
of σ.

Proof of Lemma 3.9. Because the constraint ∥Aϑ∥1 ≤ r is positively homogeneous, Kr =
rK1 on the zero-sum subspace, and K1 is symmetric under ϑ 7→ −ϑ because ∥Aϑ∥1 is even.
Hence
                              sup θi = rϱi ,        inf θi = −rϱi ,                        (3)
                              θ∈Kr                  θ∈Kr

and ϱi < ∞ because connectivity makes K1 compact, while ϱi > 0 because K1 contains a
relatively open neighborhood of the origin in the zero-sum subspace.

                                               44
   By Theorem 3.8 there is LA < ∞ with ∥θ∥∞ ≤ LA r for every θ ∈ Kr , so all contrasts
satisfy |θi − θj | ≤ 2LA r. Using the expansion σ(u) = 12 + u/4 + O(u3 ), valid uniformly on
                      P
bounded sets, and j θj = 0,

                     1    1     X                         1    N
          wi (θ) =     +             (θi − θj ) + O(r3 ) = +         θi + O(r3 ),
                     2 4(N − 1) j̸=i                      2 4(N − 1)

where the remainder is uniform over θ ∈ Kr . Taking the supremum of the absolute value
over Kr and using (3) together with the symmetry of Kr gives δi (r) = cA,i r + O(r3 ) with
cA,i = N ϱi /{4(N − 1)}.
   For the complete graph, the extreme points of K1 are the two-block vectors of Lemma 3.7;
among these, θi is largest for the vector isolating entity i, namely v = {ei − N −1 1}/(N − 1),
which satisfies ∥Av∥1 = 1 and vi = 1/N . Hence ϱi = 1/N .

Proof of Theorem 3.10. Write w = wi (θ) and ε = w−1/2. Under θ, Wm is Binomial(m, w).
By the Berry–Esseen theorem the normal approximation to the distribution of (Wm −
     p
mw)/ mw(1 − w) has error O(m−1/2 ) uniformly in w bounded away from 0 and 1, and
by Lemma 3.9 the relevant w satisfy w → 1/2 as r ↓ 0. Hence the power of the test that
                                √
rejects when |Wm − m/2| > z1−α/2 m/2 equals
                  √                   √
                  2 m ε − z1−α/2       −2 m ε − z1−α/2
                                                      
                Φ    √             +Φ     √              + O(m−1/2 ),
                      1 − 4ε 2              1 − 4ε 2


                                                                      √ √
using w(1 − w) = (1 − 4ε2 )/4, so that the standard deviation of Wm is m 1 − 4ε2 /2 and
                                      √                                √     √
the two rejection thresholds ±z1−α/2 m/2 standardize to (±z1−α/2 − 2 m ε)/ 1 − 4ε2 .
The power is strictly increasing in |ε|, so the supremum over θ ∈ Kr in the definition of
mi (r; α, ν) is attained at |ε| = δi (r), the maximal departure from parity defined in (7).
   Write P (d) = Φ(d−z1−α/2 )+Φ(−d−z1−α/2 ). Then P (0) = 2Φ(−z1−α/2 ) = α, P (d) → 1

                                              45
as d → ∞, and P ′ (d) = ϕ(d − z1−α/2 ) − ϕ(d + z1−α/2 ) > 0 for d > 0. Since 1 − ν > α, the
equation P (d) = 1 − ν therefore has the unique positive root dα,ν of Theorem 3.10. With
        √                                          p
xm = 2 m δi (r), the maximal power equals P {xm / 1 − 4δi (r)2 } + O(m−1/2 ). As r ↓ 0 we
                                                               p
have δi (r) → 0, so a power of 1 − ν > α requires m → ∞, and 1 − 4δi (r)2 = 1 + O(r2 ).
Along the horizons at which the power crosses 1 − ν, continuity and strict monotonicity of
P give
              √                                                d2α,ν 
             2 m δi (r) = dα,ν 1 + o(1) ,     that is    m=             1 + o(1) .
                                                               4δi (r)2
Both terms of P remain of order one in this limit: the lower-tail term tends to Φ(−dα,ν −
z1−α/2 ) > 0, not to zero, which is why the constant is dα,ν rather than z1−α/2 + z1−ν . Since
mi (r; α, ν) is the least integer m with power at least 1 − ν and the power is increasing in
m, the displayed value differs from mi (r; α, ν) by at most one, which is absorbed in the
o(1) factor because the right-hand side diverges. Substituting δi (r) = cA,i r + O(r3 ) from
Lemma 3.9 yields (8). For the complete graph cA,i = {4(N − 1)}−1 , so d2α,ν /(4c2A,i ) =
4(N − 1)2 d2α,ν .

Proof of Proposition 3.13. For the complete graph, Kr is compact on the zero-sum sub-
space, and the convex function θ 7→ i θi2 attains its maximum over a compact convex
                                     P

set at an extreme point. By Lemma 3.7 applied to Kr = rK1 , every extreme point takes
exactly two distinct values, say k coordinates equal to x and N − k equal to y for some
1 ≤ k ≤ N − 1. The zero-sum condition gives


                                    kx + (N − k)y = 0.


Writing d = x − y, the complete-graph total variation is


                                      k(N − k)|d| = r

                                             46
at the maximizing boundary. Thus

                             r                   N −k                 k
                     d=            ,        x=        d,        y=−     d.
                          k(N − k)                N                   N

Therefore
                                                     r2
                                   Var(θ) =                 .
                                               N 2 k(N − k)
This is maximized when k(N − k) is minimized, namely at k = 1 or k = N − 1, giving

                                                     r2
                                   Var(θ) ≤                 .
                                                N 2 (N − 1)

Division by π 2 /3 yields the SNR bound.
   For a general graph, the definition of CA implies

                                  ∥θ∥2
                                  √ ≤ CA ∥Aθ∥1 ≤ CA r.
                                    N

Squaring gives Var(θ) ≤ CA2 r2 , and division by π 2 /3 gives the general SNR bound.

Proof of Theorem 3.14. By Theorem 3.8 there is LA < ∞ with |θi − θj | ≤ 2LA r for every
θ ∈ Kr , so all remainders below are uniform over Kr , with constants depending on N and
on the graph but not on θ. For small ability contrasts,

                                          1 θi − θj
                          σ(θi − θj ) =     +       + O(|θi − θj |3 ).
                                          2    4




                                                47
Hence

                                       1    1     X
                           wi (θ) =      +             (θi − θj ) + O(r3 )
                                       2 4(N − 1) j̸=i
                                       1    N
                                 =       +        θi + O(r3 ),
                                       2 4(N − 1)
        P
using   j θj = 0. Therefore


                                                    N
                          wi (θ) − wj (θ) =               (θi − θj ) + O(r3 ).
                                                 4(N − 1)

Since |a + ε| = |a| + O(|ε|) and w̄ = 1/2 exactly, the double sum in (10) satisfies

            N X
              N
            X                          X                       N     X
                      |wi − wj | = 2         |wi − wj | =                |θi − θj | + O(r3 ),
            i=1 j=1                    i<j
                                                            2(N − 1) i<j


and dividing by 2N 2 w̄ = N 2 gives

                    1     N     X
                                                      3         1      X
   Gstruct (θ) =      ·             |θi − θ j | + O(r   ) =                |θi − θj | + O(r3 ).
                   N 2 2(N − 1) i<j                         2N (N − 1) i<j

For the complete graph,
                                       X
                                             |θi − θj | = ∥Aθ∥1 ≤ r,
                                       i<j

which gives (11).




                                                     48
B     Proofs for Section 4
The two lemmas below concern a single period, so the index t is suppressed. Throughout,
A is the oriented incidence matrix of a connected graph on I (repeated edges allowed),
K = K(1) = {u ∈ H0 : ∥Au∥1 ≤ 1}, D = maxu∈K ∥u∥2 < ∞, θ(r) = ΠK(r) (β) with
θ(0) = 0, and K(r) = rK. For u ∈ K, NK (u) denotes the normal cone of K at u in RN and
Ne (u) = NK (u) ∩ H0 . Since K ⊂ H0 , NK (u) = N
                                               e (u) ⊕ span(1), and x = ΠK (b) if and only if

x ∈ K and Hb − x ∈ N
                   e (x). Because the graph is connected, K is a polytope that contains

a neighborhood of 0 in H0 , so it is full dimensional in H0 (proof of Proposition 3.3).

Lemma B.1 (Small-radius vertex limit).         (i) A point w is an extreme point of K if and
     only if, for some nonempty proper S ⊂ I such that S and I \ S both induce connected
     subgraphs (equivalently, the edges joining S to its complement form a minimal cut),

                                              1S − |S|N −1 1
                                       w=±                   ,                            (4)
                                                  |∂S|

     where |∂S| ≥ 1 is the number of edges, counted as in A, joining S to its complement.

 (ii) For Lebesgue-almost every β ∈ RN the linear functional u 7→ β ⊤ u has a unique
     maximizer v(β) over K, which is an extreme point, and there exists r̄(β) ∈ (0, ∞]
     such that
                            θ(r) = r v(β)       for every 0 < r ≤ r̄(β).                  (5)

     Moreover v(−β) = −v(β) and v(cβ) = v(β) for c > 0.

(iii) For Lebesgue-almost every β, the path r 7→ θ(r) is continuous and piecewise affine
     on [0, ∞) with finitely many pieces, every slope has Euclidean norm at most D, and
     hence ∥θ(r) − θ(r′ )∥2 ≤ D|r − r′ | for all r, r′ ≥ 0.


                                              49
   By (i) and (ii), for every connected graph the latent ability vector near parity has exactly
two tiers, S(β) and its complement. For the complete graph with each dyad counted once,
|∂S| = |S|(N − |S|) and (4) reduces to Lemma 3.7, because on the complete graph every
nonempty proper S satisfies the connectivity condition.

Proof of Lemma B.1. (i) Let w be an extreme point. Then ∥Aw∥1 = 1, since a point with
∥Aw∥1 < 1 has a neighborhood in H0 contained in K. Let E0 be the set of edges e with
(Aw)e = 0, and let C1 , . . . , Cc be the vertex sets of the connected components of the graph
(I, E0 ). Every edge joining two different components has a nonzero contrast at w, and w is
constant on each Cl . Let W be the space of vectors in H0 that are constant on each Cl , so
dim W = c−1, and let ςe = sign{(Aw)e } for e ∈
                                             / E0 . On W , the contrasts of the edges in E0
vanish identically, and for u ∈ W sufficiently close to w the contrasts of the edges outside
                                                                             P
E0 keep the signs ςe , so ∥Au∥1 = ℓ(u) with the linear functional ℓ(u) = e∈E     / 0 ςe (Au)e .

Since ℓ(w) = 1 and ℓ(0) = 0, ℓ is not identically zero on W , and {u ∈ W : ℓ(u) = 1}
is an affine subspace of dimension c − 2 through w. Its points near w satisfy ∥Au∥1 = 1
and therefore lie in K. If c ≥ 3, this subspace contains a segment through w in its relative
interior, contradicting extremality. If c = 1, w is constant and, being zero-sum, equals 0,
contradicting ∥Aw∥1 = 1. Hence c = 2, w equals a on S = C1 and b on C2 = I \ S with
a ̸= b, and both sets induce connected subgraphs because they are components of (I, E0 ).
Writing k = |S|, the zero-sum condition gives a = (N − k)(a − b)/N and b = −k(a − b)/N ,
while ∥Aw∥1 = |∂S| |a − b| = 1; together these give (4). Connectivity of the graph gives
|∂S| ≥ 1.
   Conversely, let w be given by (4) with S and I \ S connected, so w ∈ K and ∥Aw∥1 = 1,
and suppose w = (y + z)/2 with y, z ∈ K. Then 1 = ∥Aw∥1 ≤ (∥Ay∥1 + ∥Az∥1 )/2 ≤ 1,
so equality holds edge by edge: |(Aw)e | = {|(Ay)e | + |(Az)e |}/2 for every e. For an edge
inside S or inside its complement, (Aw)e = 0, so (Ay)e = (Az)e = 0. Because both sides

                                              50
are connected, y and z are constant on S and on its complement, and being zero sum they
are multiples of 1S − |S|N −1 1. For a cut edge, (Ay)e and (Az)e have the sign of (Aw)e ,
and ∥Ay∥1 = ∥Az∥1 = 1, so y = z = w. Hence w is extreme.
   (ii) Every c ∈ H0 attains its maximum over the polytope K at some extreme point w,
that is c ∈ N
            e (w), so the finitely many polyhedral cones N
                                                         e (w) cover H0 . Their relative

boundaries, and any of them with empty interior relative to H0 , lie in finitely many hy-
perplanes of H0 ; the preimages of these under β 7→ Hβ are hyperplanes of RN and hence
Lebesgue-null. If c lies in the relative interior of N
                                                     e (w), then w is the unique maximizer

of u 7→ c⊤ u: if u ∈ K, u ̸= w and c⊤ u = c⊤ w, then c′ = c + ε(u − w) ∈ N
                                                                         e (w) for small

ε > 0, yet c′⊤ (u − w) = ε∥u − w∥22 > 0, which is impossible. Because β ⊤ u = (Hβ)⊤ u for
u ∈ H0 , for almost every β the vector Hβ lies in the relative interior of N
                                                                           e (w) for exactly

one extreme point w = v(β), which is then the unique maximizer of u 7→ β ⊤ u. The two
invariances follow from K = −K and from the invariance of the maximizer under positive
scaling of the functional.
   Fix such a β and write w = v(β). Since K(r) = rK, θ(r) = r ΠK (β/r) for r > 0, and
by the projection characterization above, ΠK (β/r) = w if and only if Hβ/r − w ∈ N
                                                                                 e (w),

equivalently Hβ − rw ∈ N             e (w) is a cone. The set {r ≥ 0 : Hβ − rw ∈ N
                       e (w) because N                                           e (w)}

is closed and convex, and it contains a neighborhood of 0 in [0, ∞) because Hβ is a relative
                  e (w). It is therefore an interval [0, r̄(β)] (or [0, ∞)) with r̄(β) > 0, which
interior point of N
proves (5). In addition, Hβ − rw lies in the relative interior of N
                                                                  e (w) for 0 ≤ r < r̄(β),

because it lies on the segment between a relative interior point and a point of the cone.
   (iii) For a nonempty face F of K, let LF be the direction space of aff(F ), PF the
orthogonal projection onto LF , and qF = Πaff(F ) (0) the point of aff(F ) nearest the origin,
so that ∥qF ∥2 ≤ minu∈F ∥u∥2 ≤ D. If x = ΠK (b) ∈ relint(F ), then (b − x)⊤ (u − x) ≤ 0
for all u ∈ F , and applying this to u and to 2x − u ∈ F (valid for u ∈ F close to x) gives


                                               51
b − x ⊥ LF ; hence x = Πaff(F ) (b) = PF b + qF . The sets RF = Π−1                        N
                                                                 K {relint(F )} partition R ,

and each is the intersection of the preimage of the relatively open polytope relint(F ) under
the affine map b 7→ PF b + qF with the polyhedral set {b : b − PF b − qF ∈ NK (xF )}, where
xF is any point of relint(F ). Hence the boundaries of all the RF lie in a finite union H of
affine hyperplanes of RN .
   Exclude the Lebesgue-null set of β that lie in a hyperplane of H passing through the
origin. The open ray {β/r : r > 0} then meets each hyperplane of H in at most one point,
so (0, ∞) splits into finitely many open intervals, on each of which β/r stays in the interior
of a single RF . On such an interval, θ(r) = r{PF (β/r) + qF } = PF β + rqF , which is affine
with slope qF of norm at most D. The map r 7→ θ(r) is continuous on (0, ∞) because
θ(r) = rΠK (β/r) and ΠK is continuous, and it is continuous at 0 because ∥θ(r)∥2 ≤ rD. A
continuous piecewise-affine function with finitely many pieces and slopes bounded by D is
D-Lipschitz.

   For a pair i ̸= j write


           δr = θi (r) − θj (r),   wij (β) = vi (β) − vj (β),   cij = E{wij (β)2 },


with β ∼ N (0, σβ2 IN ). By the scale invariance in Lemma B.1(ii), cij does not depend on σβ .
Since K = −K implies ΠK(r) (−b) = −ΠK(r) (b) and the law of β is symmetric, the process
(θ(r))r≥0 has the same law as (−θ(r))r≥0 . In particular E a(δr ) = 0 for odd a, and, writing
δr′ = dδr /dr, E{b(δr )δr′ } = 0 for even b. By Lemma B.1(iii), for almost every β the map
                                              √               √
r 7→ δr is absolutely continuous with |δr′ | ≤ 2D and |δr | ≤ 2Dr.
   For a period with hg ≡ 1, two comparisons g, g ′ of the dyad {i, j} have orientations
sg , sg′ ∈ {−1, 1}, with sg = 1 when i is the home side. Since x⊤
                                                                g θ(r) = sg δr , their linear




                                              52
predictors are
                              ∆g = η + sg δr ,        ∆g′ = η + sg′ δr ,

so the home effect enters both with a positive sign and the ability contrast changes sign
with the orientation. A home-and-away pair has sg sg′ = −1. Write qk (∆), k ∈ {−1, 0, 1},
for the cell probabilities in (1), and note that q1 (∆) = σ(∆ − κ2 ).

Lemma B.2 (Second-order emission separation at small radii). Fix a connected graph, a
pair i ̸= j, and κ2 > 0, and let β ∼ N (0, σβ2 IN ) be independent of η.

  (i) cij > 0, and f (r) = E(δr2 ) is absolutely continuous with f ′ (r) = 2cij r + o(r) for almost
      every r as r ↓ 0; in particular f (r) = cij r2 + o(r2 ).

 (ii) (Conditional covariance.) Let g ̸= g ′ be comparisons of {i, j} in the same period, fix
                                                             P
      η, let ψ be a function on {−1, 0, 1}, and let mψ (∆) = k ψ(k)qk (∆). Then


                  Covr {ψ(yg ), ψ(yg′ ) | η} = sg sg′ m′ψ (η)2 cij r2 + o(r2 ),   r ↓ 0.         (6)


      For the home-win indicator m′ψ (η) = σ ′ (η − κ2 ) > 0, for the away-win indicator
      m′ψ (η) = −σ ′ (η + κ2 ) < 0, and for the draw indicator m′ψ (η) = σ ′ (κ2 + η) − σ ′ (κ2 − η),
      which vanishes if and only if η = 0.

(iii) (Marginal home-and-away discordance.) Let (g, g ′ ) be a home-and-away pair of {i, j},
      let η have any distribution independent of β, and let


                                Sgg′ (r) = Prr {I(yg = 1) ̸= I(yg′ = 1)}


      under the emission distribution (16). With x = η − κ2 , set Q2 (η) = 2σ ′ (x){1 −


                                                 53
      2σ(x)}2 + 4σ ′ (x)2 and Q̄2 = E Q2 (η). Then Q̄2 > 0,


                                 Sgg′ (r) = Sgg′ (0) + 12 Q̄2 cij r2 + o(r2 ),                  (7)


      and there is rij > 0 such that Sgg′ is strictly increasing on [0, rij ].

Proof of Lemma B.2. (i) Suppose wi = wj for every extreme point w of K. Because K is
the convex hull of its extreme points, ui = uj for every u ∈ K. But u = ε(ei − ej ) lies in
H0 and satisfies ∥Au∥1 ≤ 1 for small ε > 0, and ui − uj = 2ε, a contradiction. Hence some
extreme point w has wi ̸= wj . By the proof of Lemma B.1(ii), v(β) = w whenever Hβ lies
in the relative interior of N
                            e (w). This cone has nonempty interior relative to H0 , because

the normal cone of a face of dimension d of a polytope that is full dimensional in H0 has
dimension N − 1 − d (proof of Proposition 3.3). Since Hβ has a positive density on H0 ,
the event has positive probability and cij ≥ (wi − wj )2 Pr{v(β) = w} > 0.
    By absolute continuity and Fubini’s theorem, with integrand bounded by 4D2 u,
                                      Z r
                            f (r) =         φ(u) du,        φ(u) = E(2δu δu′ ).
                                       0


By Lemma B.1(ii), on the event {u < r̄(β)} the path is δu = uwij near u, so 2δu δu′ = 2uwij
                                                                                         2
                                                                                            .
       2
Using wij ≤ 2D2 and |2δu δu′ | ≤ 4D2 u,

                            2
    |φ(u) − 2ucij | ≤ 2u E{wij ; r̄(β) ≤ u} + E{|2δu δu′ |; r̄(β) ≤ u} ≤ 8D2 u Pr{r̄(β) ≤ u}.


Since r̄(β) > 0 almost surely, Pr{r̄(β) ≤ u} → 0, so φ(u) = 2cij u + o(u), and integrating
gives f (r) = cij r2 + o(r2 ).
    (ii) Given (θ, η) the outcomes are independent, so Covr {ψ(yg ), ψ(yg′ ) | η} = Cov{m(η +
sg δr ), m(η + sg′ δr )}, with m = mψ and the covariance taken over β. The function m is a

                                                       54
finite combination of logistic functions, so its derivatives of every order are bounded; let
M3 = sup |m′′′ |. Taylor’s theorem gives m(η + sδ) = m(η) + Xs with


                    Xs = s m′ (η)δ + 12 m′′ (η)δ 2 + Rs ,   |Rs | ≤ M3 |δ|3 /6.


Hence Cov{m(η + sg δr ), m(η + sg′ δr )} = Cov(Xsg , Xsg′ ). Expanding, the main term is
sg sg′ m′ (η)2 Var(δr ) = sg sg′ m′ (η)2 f (r), because Eδr = 0. The term Cov(δr , δr2 ) = Eδr3
vanishes by symmetry. Each remaining term is a covariance involving δr2 or Rs together
                                                                           √
with a factor of order at least δr ; since |Rs | ≤ M3 |δr |3 /6 and |δr | ≤ 2Dr, each is O(r4 ).
Part (i) then gives (6).
    For the derivatives, q1 (∆) = 1 − σ(κ2 − ∆) and q−1 (∆) = σ(−κ2 − ∆), so q1′ (∆) =
σ ′ (κ2 − ∆), q−1
               ′
                  (∆) = −σ ′ (κ2 + ∆) and q0′ = −q1′ − q−1
                                                        ′
                                                           , using that σ ′ is even. Since σ ′ is
even and strictly decreasing on [0, ∞), σ ′ (κ2 +η) = σ ′ (κ2 −η) if and only if |κ2 +η| = |κ2 −η|,
that is η = 0, given κ2 > 0.
    (iii) Let m = q1 and p± = m(η±δ), the home-win probabilities of the two matches when
sg = 1 (the case sg = −1 swaps the two and leaves the event unchanged). By conditional
independence,


        Pr{I(yg = 1) ̸= I(yg′ = 1) | θ, η} = Q(η, δr ),     Q(η, δ) = p+ + p− − 2p+ p− .


The function Q(η, ·) is even and smooth, and its derivatives are bounded uniformly in
(η, δ). Hence ∂δ Q(η, δ) = Q2 (η)δ + R(η, δ) with |R| ≤ M4 |δ|3 /6, where M4 = sup |∂δ4 Q|
and Q2 (η) = ∂δ2 Q(η, 0). Differentiating, ∂δ2 p± |0 = m′′ (η) and ∂δ2 (p+ p− )|0 = 2m(η)m′′ (η) −
2m′ (η)2 , so
                            Q2 (η) = 2m′′ (η){1 − 2m(η)} + 4m′ (η)2 .



                                                 55
With m(∆) = σ(∆ − κ2 ) we have m′ = σ ′ and m′′ = σ ′ (1 − 2σ) evaluated at x = η − κ2 ,
which gives the stated form and Q2 (η) ≥ 4σ ′ (x)2 > 0, hence Q̄2 > 0 for every distribution
of η.
   For fixed η and almost every β, r 7→ Q(η, δr ) is absolutely continuous with derivative
∂δ Q(η, δr )δr′ , which is bounded. By Fubini’s theorem and the independence of η and β,
                              Z rn                    o     Z rn                  o
                                            ′                    1
        Sgg′ (r) − Sgg′ (0) =     Q̄2 E(δu δu ) + ρ(u) du =        Q̄
                                                                 2 2
                                                                      φ(u) + ρ(u)  du,
                              0                               0

                                         √     √
with |ρ(u)| ≤ E|R(η, δu )δu′ | ≤ (M4 /6)( 2Du)3 2D = 23 M4 D4 u3 . By part (i), the integrand
equals Q̄2 cij u + o(u), which is positive on (0, rij ] for some rij > 0. This proves strict
monotonicity on [0, rij ] and, after integration, (7).

Remark B.3 (Why covariances of repeated meetings are not used). Integrating (6) over η
does not give the marginal covariance. With µ(η, r) = E{m(η + sδr )}, which by symmetry
does not depend on s,

                                                                 
            Covr {ψ(yg ), ψ(yg′ )} = Eη Covr {ψ(yg ), ψ(yg′ ) | η} + Varη {µ(η, r)}.


By the expansion in part (ii), µ(η, r) = m(η) + 21 m′′ (η)f (r) + O(r4 ) uniformly in η.
The leading r2 coefficient of the marginal covariance is therefore cij [sg sg′ E{m′ (η)2 } +
Covη {m(η), m′′ (η)}]. For a home-and-away pair (sg sg′ = −1), the sign of this coefficient
depends on the law of η and on κ2 , so a sum of such covariances need not be monotone in
r. The discordance probability in part (iii) is a function of δr that is even, with positive
curvature at zero for every value of η, and so avoids this cancellation.

   The dynamic model inherits deterministic control of the latent abilities from the pro-
jection constraint.

                                               56
Assumption B.1 (Comparison-graph regularity). Let τt denote the smallest constant such
that
                                        ∥θ∥1 ≤ τt ∥At θ∥1                               (8)

for every θ ∈ RN satisfying 1⊤ θ = 0. Assume τmax = supt τt < ∞.

Proposition B.4 (Regime-controlled ability bound). Under Assumption B.1, ∥θt ∥1 ≤
τt rst ≤ τmax rst for every period t. Consequently,


                                 max ∥θt ∥1 ≤ τmax max rk ,                             (9)
                                1≤t≤T                 1≤k≤Kact


with Kact = |A| the number of occupied regimes (Section 4.1). The bound is deterministic
given the regime radii.

Proof of Proposition B.4. By construction,


                                          θt ∈ Kt (rst ),


so
                                         ∥At θt ∥1 ≤ rst .

Applying (8) gives
                                  ∥θt ∥1 ≤ τt ∥At θt ∥1 ≤ τt rst .

Taking the maximum over periods yields (9).


B.1     Posterior tail bound on the ability process
Proposition B.4 bounds the abilities in terms of the realized regime radii. Averaging that
bound over the prior turns it into an explicit posterior tail bound. Fix the state sequence

                                                57
s1:T , with Kact ≤ T occupied regimes, so that the remaining unknowns have the proper
prior of Section 4.1, and suppose Assumption B.1 holds and ar > 1. Under the prior,
E(rk ) = E(αr−1 ) = br /(ar − 1); set R⋆ = Kact br /(ar − 1). Then for every fixed dataset and
every B > 0,                                             
                                                                     τmax R⋆
                        Pr       max ∥θt ∥1 > B D, s1:T       ≤                  ,       (10)
                             1≤t≤T                                B p(D | s1:T )
where p(D | s1:T ) ∈ (0, 1] is the marginal likelihood given the state sequence. That
maxt ∥θt ∥1 is finite with posterior probability one already follows from Theorem 3.1; the
content of (10) is the explicit rate in B, which exhibits the dependence of the posterior tail
on the number of regimes and the prior mean radius, inflated by the graph constant τmax .
The bound involves the unknown p(D | s1:T ) and is therefore not directly computable.

Proof of (10). By Proposition B.4, maxt ∥θt ∥1 ≤ τmax maxk≤Kact rk , so for any c > 0

                                                                  
               Pr max ∥θt ∥1 > τmax c D, s1:T ≤ Pr max rk > c D, s1:T .
                    t                                         k≤Kact


Since 0 < L(D | Λ) ≤ 1, for any event E we have Pr(E | D, s1:T ) ≤ Pr(E | s1:T )/p(D | s1:T ),
where the probability on the right is under the prior. Bounding the maximum by the sum,

                                KXact
                                                 Kact br
                   E max rk s1:T ≤      E(rk ) =         = R⋆ < ∞.
                      k≤Kact                     a r −1
                                   k=1


Markov’s inequality then gives Pr(maxk≤Kact rk > c | s1:T ) ≤ R⋆ /c, so

                                                                      R⋆
                        Pr max ∥θt ∥1 > τmax c D, s1:T ≤                          .
                                 t                                 c p(D | s1:T )

Setting c = B/τmax yields (10).



                                                 58
C      Posterior Computation and Summaries

C.1     Posterior computation
Each sweep of the sampler updates, in turn, the auxiliary abilities, the home effects, the
occupied-state radii and their shared rate, and the state sequence. The projected abilities
are deterministic functions of the auxiliary variables and the radii, so they are recomputed
when needed rather than sampled. For season t, write Lt (θt , ηt , κ) = G
                                                                         Q t
                                                                           g=1 p(ytg | θt , ηt , κ)

for the likelihood contribution, with cell probabilities from (1) and the threshold κ held
fixed, and
                             ℓt (βt ; ηt , κ, r) = log Lt {ΠKt (r) (βt ), ηt , κ}                (11)

for the log-likelihood as a function of the auxiliary abilities.
    The auxiliary abilities have prior βt ∼ N (0, σβ2 IN ) and are updated by elliptical slice
sampling with target proportional to exp{ℓt (βt ; ηt , κ, rst )} ϕN (βt ; 0, σβ2 IN ), recomputing the
projection at every likelihood evaluation with the solver of Appendix C.2. Each home effect
has an independent N (0, ση2 ) prior and is updated by a Gaussian random walk, ηt⋆ = ηt + ζt
with ζt ∼ N (0, ςη2 ), accepted with probability

                                  Lt (θt , ηt⋆ , κ)       (ηt⋆ )2 − ηt2
                                                                      
                           min 1,                   exp −                  .
                                  Lt (θt , ηt , κ)             2ση2

    The occupied radii follow rk | αr ∼ Exponential(αr ) with shared rate αr ∼ Gamma(ar , br )
in the shape–rate parameterization. Writing Tk = {t : st = k} for the seasons in state
k, each radius is updated by a random walk on the log scale, log rk⋆ = log rk + ζk with




                                                     59
ζk ∼ N (0, ςr2 ), and accepted with probability min(1, Ar ), where

                                             r⋆ Y Lt {ΠKt (rk⋆ ) (βt ), ηt , κ}
                    Ar = exp{−αr (rk⋆ − rk )} k                                            (12)
                                             rk t∈T Lt {ΠKt (rk ) (βt ), ηt , κ}
                                                        k



and rk⋆ /rk is the Hastings correction for the log-scale proposal (Appendix D.1). Given the
Kact occupied radii, the rate has the conjugate update

                                                                      K
                                                                                   !
                                                                      X act

                      αr | r1:Kact ∼ Gamma ar + Kact , br +                   rk       .   (13)
                                                                      k=1


   Opening a new state requires the season likelihood averaged over the unknown radius,
R∞                      R1
 0
   ft (r) αr e−αr r dr = 0 ft {Fα−1
                                  r
                                    (q)} dq, where Fα−1
                                                      r
                                                        (q) = − log(1 − q)/αr is the exponential
quantile function. After αr is updated, we take J equally spaced probabilities qj = 0.05 +
0.90(j − 1)/(J − 1), j = 1, . . . , J, and the corresponding quantiles
                                                                     
                                                       log(1 − qj )
                             rjgrid = max         −6
                                                10 , −                    ,                (14)
                                                           αr

which stay fixed for the state sweep that follows. The new-state likelihood

                                                J
                                             1X
                                      ft,0 =
                                      e            ft (rjgrid )                            (15)
                                             J j=1

is an equally weighted approximation of the integral over q, so no additional density or
Jacobian factor enters; the outer 5% of prior probability on each side is omitted. It enters
the score wt (0) = Bm It (0)Ot (0)fet,0 of Section 4.2, and the same grid supplies the initial
radius in (15). We use J = 15 in all analyses. Once a state is occupied, its radius is
updated by (12) and is no longer restricted to grid values.


                                                  60
   The seasons are then reallocated one at a time by (13)–(15). The candidates for season
t are all currently occupied states, including the current state of t even when t is its only
member, together with one new state. Empty states are deleted after each reassignment and
the remaining labels compacted, so no fixed state capacity is kept. This allocation kernel is
not the exact collapsed update of a finite hidden Markov model with symmetric Dirichlet
transition rows: its cell pseudo-counts atr bm sum to atr γ while the outgoing denominator
contains atr , and the birth multiplier Bm is set algorithmically rather than derived from a
prior on the number of states. Posterior invariance has not been established for this step,
and we treat the sampler output as an approximate posterior. Algorithm 1 summarizes
one sweep.




                                             61
Algorithm 1 Blockwise inference procedure
Require: Data D; current (s1:T , r1:Kact , αr , β1:T , η1:T ); fixed threshold and hyperparame-
    ters.
Ensure: One computational sweep.
 1: for t = 1, . . . , T do
 2:     Update βt by elliptical slice sampling, evaluating the projected likelihood in (11).
 3: end for
 4: for t = 1, . . . , T do
 5:     Update ηt by Gaussian random-walk Metropolis–Hastings.
 6: end for
 7: for each occupied state k do
 8:     Update rk using (12).
 9: end for
10: Draw αr from (13).
11: Construct the radius grid in (14).
12: for t = 1, . . . , T do
13:     Compute and normalize the state scores in (13)–(14).
14:     Draw the new allocation; if a new state is selected, initialize its radius using (15).
15:     Remove empty states and compact the remaining labels.
16: end for
17: Recompute θt = ΠKt (rst ) (βt ) for all seasons.
18: Store the draw after ordering state labels by increasing radius.



C.2     Computation of the projection step
The projection is the convex quadratic program

                                 1
          ΠKt (r) (βt ) = arg min ∥ϑ − βt ∥22   subject to ∥At ϑ∥1 ≤ r,   1⊤ ϑ = 0.       (16)
                               ϑ 2


In all analyses reported here the comparison graph is the unweighted complete graph with
each dyad counted once, and (16) has an exact solution. For every ϑ, with order statistics
ϑ(1) ≤ · · · ≤ ϑ(N ) , ∥At ϑ∥1 = N
                                P
                                  i=1 (2i − N − 1)ϑ(i) , and the projection preserves the order



                                                62
of βt . If ∥At Hβt ∥1 ≤ r the solution is Hβt . Otherwise, let v be the values of Hβt in
increasing order, wi = 2i − N − 1, and ϑ(λ) the isotonic regression of v − λw. The sorted
solution is ϑ(λ) with λ > 0 solving w⊤ ϑ(λ) = r, found by a one-dimensional search, and it
is then returned to the original order. Because 1⊤ v = 0, 1⊤ w = 0, and isotonic regression
preserves the mean, the zero-sum constraint holds automatically. Isotonic regression pools
adjacent values, which is how the exact ties of Proposition 3.3 arise in computation. For
general comparison graphs, primal–dual or ADMM algorithms can exploit the graph-fused
structure.

Proposition C.1 (Almost-everywhere differentiability). Let U (βt ) = −ℓt (βt ; ηt , κ, rst ) +
∥βt ∥22 /(2σβ2 ) be the negative log posterior kernel for βt . For fixed (rst , ηt , κ), U (βt ) is con-
tinuous and differentiable almost everywhere with respect to Lebesgue measure on RN . See
Appendix D.2 for a proof.


C.3      Posterior summaries
The point estimates used in the simulations and in the applications are computed from
the retained draws of Algorithm 1. At each retained iteration m, the occupied radii are
          (m)               (m)
sorted, rσm (1) ≤ · · · ≤ rσm (K (m) ) , and the state labels are permuted to match, so smaller
labels always mean smaller radii.
    The number of states is estimated by the empirical mode Kb of K (m) , with ties broken

in favor of the smaller value. Over the draws M b = {m : K (m) = K}
                                                         K
                                                                  b we form the season

co-clustering matrix
                                              1     X     (m)  (m)
                                  C̄tt′ =              I{st = st′ }                                (17)
                                            |MKb | m∈M
                                                     K
                                                     b




                                                   63
and select the Dahl representative draw

                                                                    (m)          (m)      (m)
                 m⋆ = arg min ∥C (m) − C̄∥2F ,                    Ctt′ = I{st          = st′ }.                  (18)
                           m∈MK
                              b



                                                                                  (m⋆ )               (m⋆ )
The state path and the radii both come from this draw, ŝt = st                           and r̂t = rŝt      , so the
reported radius is the one paired with the representative path.
   Team tiers and abilities are summarized season by season from the draws in which
                                                                    (m)
season t belongs to its Dahl state, St = {m ∈ MKb : st                    = ŝt }. In each such draw the tiers
are the groups of teams with exactly equal abilities, which the exact projection produces
                                                                  (m)
with positive probability (Proposition 3.3); write ct                   for this partition of the teams. The
                                                                                        (m)
estimated tiers ĉt are the SALSO estimate (Dahl et al., 2022) of {ct                         : m ∈ St } under the
variation of information loss, with at most as many tiers as the most frequent number of
tiers among these partitions, and are labeled in decreasing order of ability. Each team’s
reported ability is its posterior mean averaged over its estimated tier,

                                           1              X          1 X (m)
                         θ̂ti =                                              θ .                                 (19)
                                  |{j : ĉtj = ĉti }| j:ĉ =ĉ     |St | m∈S tj
                                                          tj   ti            t



Home effects are summarized by their posterior means over all M retained draws, η̂t =
            (m)
M −1 M
    P
      m=1 ηt . The distribution of K, the season co-clustering frequencies and the radius

draws convey the uncertainty around these point estimates.
   The figures of the applications also show, for each season, the posterior median and 90%
credible interval of the season radius and the posterior mean and 90% credible interval of
each team’s ability over St . These intervals average over regime allocations and are therefore
approximate in the sense of Section 5.




                                                     64
C.4     Diagnostics
For the two-chain real-data analyses, we inspect trace plots of the season-assigned radii rst ,
the home effects and selected components of θt , compare the distribution of the number of
occupied states K between chains, and compute split-R b and effective sample sizes for the

continuous parameters. The proposal scales of the two Metropolis–Hastings updates are
fixed within each run, and their acceptance rates are recorded as a further check on mixing.



D      Derivations for Appendix C

D.1     Hastings correction for the log-scale radius proposal
The factor rk⋆ /rk in (12) is the Hastings correction for the asymmetric proposal on rk
induced by a symmetric random walk on log rk . Since log rk⋆ | log rk ∼ N (log rk , ςr2 ),
writing rk⋆ = elog rk +ζk with ζk ∼ N (0, ςr2 ) and applying the change-of-variables Jacobian
|dζk /drk⋆ | = 1/rk⋆ gives proposal density q(rk⋆ | rk ) = ϕ(ζk /ςr )/(ςr rk⋆ ). By symmetry of ϕ in
ζk ↔ −ζk ,
                               q(rk | rk⋆ )   ϕ(ζk /ςr )/(ςr rk )    rk⋆
                                            =                      =     ,
                               q(rk⋆ | rk )   ϕ(ζk /ςr )/(ςr rk⋆ )   rk
which is exactly the factor appearing in (12).


D.2     Proof of Proposition C.1
Proof of Proposition C.1. The Euclidean projection onto a closed convex polyhedron is
Lipschitz continuous and piecewise affine, the affine pieces corresponding to the partition
of RN induced by the active face of the polyhedron at each point; this is a standard
consequence of parametric quadratic programming applied to a fixed polyhedral feasible


                                                  65
set. Since Kt (rst ) is polyhedral — the constraint ∥At ϑ∥1 ≤ rst admits a finite halfspace
representation, intersected with the hyperplane 1⊤ ϑ = 0 — the map βt 7→ ΠKt (rst ) (βt )
is differentiable except on a finite union of lower-dimensional boundaries between affine
pieces, a set of Lebesgue measure zero. The likelihood is smooth in the projected abilities
away from these boundaries, and the Gaussian quadratic term is smooth everywhere, so
U (βt ) is differentiable everywhere except on this measure-zero set.



E     Simulations
This appendix gives the simulation designs summarized in Section 5.2 and the full results.
The study asks whether the model recovers the number of states, the state sequence, the
radii, the team abilities and the tiers, across two or three states, 20 or 40 seasons, and one
or two ability patterns per state. Each of the eight settings is replicated 50 times.


E.1     Simulation Settings
Every season has N = 20 teams playing a double round robin, so each pair meets once at
each venue and a season contains 2 20
                                     
                                   2
                                       = 380 matches. When team i hosts team j in season
                                          ∗
t, the latent performance difference is Yijt = θti − θtj + ηt + ξijt , where ξijt is a standard
logistic error with variance π 2 /3 as in Section 3.4, and the observed outcome is
                                     
                                            ∗
                                     
                                     
                                     
                                      1, Yijt > κ2 ,
                                     
                               Yijt = 0,  −κ2 ≤ Yijt ∗
                                                        ≤ κ2 ,
                                     
                                     
                                     
                                     −1, Y ∗ < −κ ,
                                     
                                           ijt        2




                                              66
that is, a home win, draw or home loss. We set ηt = 0.30 and κ2 = 0.30 in every season. This
is the ordered likelihood (1) with κ1 = −κ2 , so the simulated data satisfy the anchoring
of Section 3.1 by construction. The radius of an ability vector is its total variation on
the complete graph, with each of the 20
                                         
                                       2
                                           = 190 pairs counted once, r(θ) = ∥Aθ∥1 =
P
   i<j |θi − θj |.

   All designs are built from two kinds of ability vector. The two-tier vector


                                  ua = (−a, . . . , −a, a, . . . , a)
                                        | {z } | {z }
                                                 10           10


has radius r(ua ) = 200a, so u1/2 , u1 and u2 have radii 100, 200 and 400. The three-tier
vector
                        v = (−4/3, . . . , −4/3, 0, . . . , 0, 4/3, . . . , 4/3)
                             |      {z        } | {z } |             {z       }
                                        5               10              5

has radius 200, the same as u1 , but a different tier structure. In the baseline settings
every state keeps a single ability vector. In the heterogeneous settings the radius-200 state
alternates between u1 and v from one occurrence to the next, starting with u1 , so the
model has to place two different tier structures in the same state. Table S1 lists the eight
settings.
   In every design a state persists for several seasons and recurs after other states have
intervened. One comparison is not one-factor: at T = 40 the two-state heterogeneous
design switches state every five seasons, whereas the two-state baseline switches every ten,
so it is a more dynamic design rather than the baseline with only the ability patterns
changed. The model was fitted with the sampler and posterior summaries of Section 5 and
Appendix C.3, with the hyperparameters, allocation tuning parameters and summary rules
of Appendix F held fixed across replicates.


                                                  67
Table S1: Simulation designs. States with radius 100, 200 and 400 use u1/2 , u1 and u2 ,
except that in the heterogeneous settings the radius-200 state alternates between u1 and
v, starting with u1 . k m denotes m consecutive seasons in state k, and (·)×2 a sequence
repeated twice.
 K Radius-200 vector Radii              State sequence, T = 20 State sequence, T = 40
 2    u1                   200, 400          (15 , 25 , 15 , 25 )         (110 , 210 , 110 , 210 )
 3    u1                   100, 200, 400     (15 , 25 , 35 , 25 )         (15 , 25 , 35 , 25 )×2
 2    u1 , v alternating   200, 400          (15 , 25 , 15 , 25 )         (15 , 25 , 15 , 25 )×2
 3    u1 , v alternating   100, 200, 400     (15 , 25 , 35 , 25 )         (15 , 25 , 35 , 25 )×2


E.2       Simulation Results
Table S2 reports means over the 50 replicates of each setting, with Monte Carlo standard
errors in parentheses, and Figure S1 shows the radius estimates.

Table S2: Simulation results over 50 independent replicates. K is the true number of states,
T the number of seasons, and P the number of ability patterns per state (P = 1: baseline
settings; P = 2: heterogeneous settings).
K    T    P K recovery       State ARI                θ-MSE           Class ARI                η-MSE
2    20   1      0.98      0.9901 (0.0059)     0.0260 (0.0014)      0.9414 (0.0032)      0.0154 (0.0006)
2    40   1      0.98      0.9990 (0.0010)     0.0214 (0.0006)      0.9441 (0.0019)      0.0156 (0.0005)
2    20   2      0.92      0.9891 (0.0060)     0.0434 (0.0014)      0.9039 (0.0037)      0.0155 (0.0006)
2    40   2      0.98      0.9970 (0.0022)     0.0432 (0.0010)      0.9027 (0.0025)      0.0157 (0.0005)
3    20   1      0.90      0.9879 (0.0050)     0.0340 (0.0012)      0.8858 (0.0040)      0.0152 (0.0008)
3    40   1      0.84      0.9894 (0.0036)     0.0325 (0.0009)      0.8847 (0.0031)      0.0147 (0.0005)
3    20   2      0.90      0.9852 (0.0062)     0.0549 (0.0018)      0.8405 (0.0053)      0.0146 (0.0008)
3    40   2      0.94      0.9905 (0.0041)     0.0538 (0.0012)      0.8404 (0.0039)      0.0128 (0.0004)




                                                 68
                           (a) 2 states, 20 seasons                              (b) 2 states, 40 seasons                                  (c) 3 states, 20 seasons                                 (d) 3 states, 40 seasons
                             One pattern per state                                 One pattern per state                                     One pattern per state                                    One pattern per state


                     400                                                   400                                                       400                                                      400
Estimated radius r




                                                      Estimated radius r




                                                                                                                Estimated radius r




                                                                                                                                                                         Estimated radius r
                     300                                                   300                                                       300                                                      300


                     200                                                   200                                                       200                                                      200


                     100                                                   100                                                       100                                                      100


                      0                                                     0                                                         0                                                        0
                             State 1       State 2                                 State 1       State 2                                   State 1   State 2   State 3                              State 1   State 2   State 3



                           (e) 2 states, 20 seasons                              (f) 2 states, 40 seasons                                  (g) 3 states, 20 seasons                                 (h) 3 states, 40 seasons
                            Two patterns at r = 200                               Two patterns at r = 200                                   Two patterns at r = 200                                  Two patterns at r = 200


                     400                                                   400                                                       400                                                      400
Estimated radius r




                                                      Estimated radius r




                                                                                                                Estimated radius r




                                                                                                                                                                         Estimated radius r
                     300                                                   300                                                       300                                                      300


                     200                                                   200                                                       200                                                      200


                     100                                                   100                                                       100                                                      100


                      0                                                     0                                                         0                                                        0
                             State 1       State 2                                 State 1       State 2                                   State 1   State 2   State 3                              State 1   State 2   State 3
                                                                                                            True radius




Figure S1: Radius estimates across the eight simulation settings. Dashed horizontal seg-
ments mark the true radii.

                       The state path is recovered well in every setting. Mean state ARI lies between 0.985
and 0.999, and in each of the four pairs of designs it is higher with 40 seasons than with
20. The number of states is recovered in 92% to 98% of two-state replicates and in 84% to
94% of three-state replicates. Every miss overestimates the number of states by one, and
the extra state is small: it holds a single season in 22 of the 28 misses and at most two
seasons in 26, usually at the start or end of a block. In these replicates the posterior is split
between the two values, with typically about a third of its mass on the true number. A
longer series does not reliably remove such misses, since recovery rises from 92% to 98% in
the two-state heterogeneous design but falls from 90% to 84% in the three-state baseline.
                       Abilities and tiers are recovered closely. θ-MSE is between 0.021 and 0.055 and is

                                                                                                            69
slightly lower at T = 40 than at T = 20 in every pair. Class ARI ranges from 0.903 to
0.944 with two states and from 0.840 to 0.886 with three. It is lowest in the three-state
heterogeneous designs, where the radius-200 state alternates between a two-tier and a three-
tier configuration. The alternation costs tier recovery but not regime recovery: mean state
ARI is 0.985 to 0.997 in the heterogeneous designs and 0.988 to 0.999 in the corresponding
baselines, so seasons that share a radius but not a tier structure are almost always placed
in the same state.
   The radius estimates in Figure S1 lie close to the truth, with the mean Dahl estimate
within 8% of the true radius in every setting, and the radii of different states are clearly
separated. Home effects are estimated equally well throughout, with mean squared error
between 0.0128 and 0.0157, and the main error of the model across all eight designs is an
occasional extra state that absorbs one or two seasons.


E.3     Robustness to Missing Games
To examine robustness to incomplete match records, we extended the baseline two-state
setting with T = 20 seasons by independently retaining each scheduled match with proba-
bility p ∈ {1.00, 0.90, 0.80, 0.70, 0.60}. The resulting missingness mechanism is fixture-level
missing completely at random (MCAR). The complete double round-robin schedule con-
tains 380 matches per season, so the five settings retain approximately 380, 342, 304, 266
and 228 matches per season. A new retention mask is generated independently for every
replicate and retention level. All other data-generating parameters, prior specifications,
MCMC settings and posterior-summary rules are those of the complete-data two-state
T = 20 setting, and each setting has 50 independent replicates.
   Table S3 reports the Monte Carlo means, with one row for each retention probability.
The reduction column gives the expected percentage of scheduled matches removed, 100(1−

                                              70
p)%. For K recovery, State ARI and Class ARI, the values in parentheses are absolute
differences from the complete-data baseline; for the MSE measures they are percentage
changes relative to the baseline. Radius recovery is shown in Figure S2.

Table S3: Robustness to fixture-level MCAR missingness over 50 independent replicates.
Values in parentheses give changes relative to the complete-data baseline. Changes in
recovery and ARI are absolute differences, whereas changes in MSE are relative percentages.
      Retention p Reduction K recovery State ARI        θ-MSE     η-MSE     Class ARI

          1.00        0%         0.980      0.9901       0.0260   0.0154     0.9414
                                 1.000       0.9880      0.0310   0.0169     0.9355
          0.90       10%       (+0.020)    (-0.0021)    (+19.0%) (+10.3%)   (-0.0059)
                                 1.000       0.9920      0.0401   0.0191     0.9245
          0.80       20%       (+0.020)   (+0.0019)     (+54.0%) (+24.3%)   (-0.0170)
                                 0.980       0.9861      0.0516   0.0220     0.9114
          0.70       30%        (0.000)    (-0.0040)    (+98.1%) (+43.4%)   (-0.0300)
                                 0.980       0.9828      0.0736   0.0260     0.8859
          0.60       40%        (0.000)    (-0.0072)   (+182.7%) (+69.3%)   (-0.0555)


   Removing matches has almost no effect on the regime structure. The number of states
is recovered in every replicate at p = 0.9 and p = 0.8 and in 49 of 50 at the other three
retention levels, and mean state ARI stays above 0.98 even with 40% of the matches
removed. The misses at p = 0.7 and p = 0.6 add one state, with one and four seasons
respectively. Each season still has about 228 matches at p = 0.6, and the states persist
for five seasons at a time, so there is enough information to place each season. The small
changes in the recovery of the number of states across retention levels are within Monte
Carlo error.
   The loss of information falls on the parameters that are estimated season by season.
Relative to the complete data, θ-MSE rises by 19% at p = 0.9, 54% at p = 0.8, 98% at
p = 0.7 and 183% at p = 0.6. Over the same range, mean class ARI drops from 0.941 to
0.886, and η-MSE rises by 69% at the lowest retention level.

                                            71
                                              (a) p = 1.0                                                                               (b) p = 0.9                                                                               (c) p = 0.8


                              400                                                                                 400                                                                                       400
         Estimated radius r




                                                                                             Estimated radius r




                                                                                                                                                                                       Estimated radius r
                              300                                                                                 300                                                                                       300


                              200                                                                                 200                                                                                       200


                              100                                                                                 100                                                                                       100


                               0                                                                                   0                                                                                         0
                                    State 1                                State 2                                            State 1                                State 2                                            State 1                 State 2




                                                                                           (d) p = 0.7                                                                               (e) p = 0.6


                                                                     400                                                                                       400
                                                Estimated radius r




                                                                                                                                          Estimated radius r




                                                                     300                                                                                       300


                                                                     200                                                                                       200


                                                                     100                                                                                       100


                                                                      0                                                                                         0
                                                                                 State 1                                State 2                                            State 1                                State 2
                                                                                                                                    True radius




Figure S2: Recovery of the competitive-balance radius under fixture-level MCAR miss-
ingness. Each boxplot summarizes state-specific radius estimates across 50 independent
replicates, using the median across seasons within each replicate and state. Dashed seg-
ments mark the true radii, r1 = 200 and r2 = 400.




                                                                                                                                        72
   Figure S2 shows the same pattern for the radius. The estimates stay near their true
values, but they spread out as matches are removed: the central 95% of the radius-200
estimates spans 33 units with complete data and 63 units at p = 0.6.
   Under independent fixture-level missingness of up to 40% in this dense double round
robin, the model still identifies the regimes, while the abilities, tiers and radii become less
precise. These conclusions apply to matches missing at random and not to missing teams,
missing seasons or missing connected parts of the schedule.


E.4     Calibration and Sampling Diagnostics
Table S4 compares posterior uncertainty with the truth in the eight main settings and in the
four missing-data settings. Equal-tailed 95% credible intervals cover the true home effect
in 93% to 96% of season replicates and the true team abilities in 97% to 99%. Because
the allocation kernel is approximate, the regime frequencies below are not exact posterior
probabilities, and this table checks their calibration directly. The smallest set of values of
K holding 95% of the draws contains the true number in at least 98% of replicates, and
on average 0.77 to 0.95 of the draws have the true number. The frequency with which two
seasons share a state averages 0.96 to 0.99 for pairs that truly share a state and at most
0.017 for pairs that do not. Grouping the season pairs of the eight main settings by this
probability, every pair with probability above 0.95 truly shares a state and no pair below
0.05 does, and in each intermediate group the observed frequency is at least the average
probability.
   Table S5 summarizes the behaviour of the sampler. The radius and home-effect propos-
als are accepted at rates of 0.18 to 0.35 and 0.86 to 0.90. The number of occupied states
changes 98 to 259 times on average among the 5,000 retained draws, so the chains move
between values of K rather than settling on one, and the frequency of the true K in the first

                                              73
Table S4: Calibration over 50 replicates per setting; the bottom rows are the missing-data
settings with retention probability p. Columns 4–5: coverage of equal-tailed 95% credible
intervals for the home effects and team abilities. Column 6: proportion of replicates whose
95% set of values of K contains the true K. Column 7: mean frequency of the true K in
the draws. Columns 8–9: mean frequency with which two seasons share a state, for pairs
in the same true state and in different true states.
            K T       P    η      θ     K set Pr(Ktrue ) Same state Different states
             2   20   1   0.95   0.99   1.00     0.90       0.978         0.004
             2   40   1   0.95   0.99   1.00     0.95       0.994         0.000
             2   20   2   0.95   0.98   1.00     0.86       0.974         0.001
             2   40   2   0.95   0.98   1.00     0.89       0.981         0.001
             3   20   1   0.94   0.98   1.00     0.82       0.974         0.004
             3   40   1   0.93   0.99   0.98     0.77       0.980         0.003
             3   20   2   0.93   0.97   1.00     0.83       0.976         0.005
             3   40   2   0.96   0.97   0.98     0.80       0.975         0.003
              p = 0.9     0.95   0.99   1.00     0.91       0.977         0.005
              p = 0.8     0.94   0.98   1.00     0.91       0.977         0.005
              p = 0.7     0.95   0.99   1.00     0.91       0.973         0.010
              p = 0.6     0.94   0.98   1.00     0.88       0.959         0.017




                                                  74
and second halves of the retained draws differs by at most 0.03. The state path reaches an
adjusted Rand index of 0.99 with the truth after 305 to 639 iterations on average and after
at most 4,325 iterations in any replicate, within the 5,000-iteration burn-in. Two teams in
the same true tier have exactly equal abilities in 54% to 63% of the draws, and two teams
in different tiers in 0.1% to 5.4%.

Table S5: Sampling diagnostics over 50 replicates per setting; the bottom rows are the
missing-data settings with retention probability p. Acceptance rates of the radius and
home-effect updates; mean number of changes in the number of occupied states among
the retained draws; frequency of the true K in the first and second halves of the retained
draws; first iteration at which the state path reaches an adjusted Rand index of 0.99, mean
(maximum) over replicates; and the proportion of draws in which two teams have exactly
equal abilities, for pairs in the same true tier and in different true tiers.
K T       P r acc. η acc. K changes Pr(Ktrue ): halves ARI ≥ 0.99 Tie, same Tie, different
 2   20   1   0.25   0.87     133        0.90 / 0.90    410 (904)     0.63       0.001
 2   40   1   0.18   0.87      98        0.95 / 0.95   487 (1113)     0.63       0.001
 2   20   2   0.26   0.87     149        0.86 / 0.87    457 (989)     0.60       0.016
 2   40   2   0.19   0.87     115        0.90 / 0.89   520 (1099)     0.60       0.017
 3   20   1   0.35   0.86     259        0.80 / 0.83   418 (2165)     0.63       0.040
 3   40   1   0.28   0.86     237        0.77 / 0.76   464 (1058)     0.63       0.039
 3   20   2   0.35   0.86     248        0.83 / 0.83   441 (1386)     0.60       0.054
 3   40   2   0.28   0.86     232        0.79 / 0.81   639 (1507)     0.60       0.053
  p = 0.9     0.26   0.88     135        0.91 / 0.91   463 (4325)     0.61       0.002
  p = 0.8     0.27   0.89     149        0.91 / 0.91    381 (838)     0.59       0.005
  p = 0.7     0.29   0.89     154        0.91 / 0.90    327 (773)     0.57       0.008
  p = 0.6     0.30   0.90     174        0.87 / 0.88    305 (724)     0.54       0.013




                                             75
F     Implementation Details for the Simulation Study

F.1     Prior Specification and Computation
All twelve simulation settings use the same prior and sampler settings. The auxiliary
abilities have prior βt ∼ N (0, σβ2 IN ) with σβ = 6, each home effect has an independent
N (0, 1) prior, and the state-specific radii follow rk | αr ∼ Exponential(αr ) with αr ∼
Gamma(ar , br ) in the shape–rate parameterization and (ar , br ) = (10, 200). The threshold
is held at its true value κ2 = 0.30. The latent state sequence is updated with the allocation
rule of Section 4.2, with (atr , γ, λ) = (2.5, 0.5, 0.5), and new states are proposed with the
J = 15 point radius grid (14); occupied radii are then updated by the log-scale random walk
(12) and are not restricted to grid values. The proposal standard deviations are ςr = 0.16
for log rk and ςη = 0.05 for ηt .
    Each chain starts from a single state with radius 1/αr , where αr = ar /br , auxiliary
abilities drawn from N (0, 0.12 ) and home effects equal to zero. It runs for 10,000 iterations,
and the first 5,000 are discarded as burn-in. With eight replicates run in parallel on
an Apple M5 laptop, one replicate took about 15 minutes with T = 20 and about 31
minutes with T = 40, and the 600 replicates of the twelve settings took about 26 hours
in total. The data of replicate ℓ are generated with seed s0 + 10,000 ℓ and the chain
is run with seed s0 + 10,000 ℓ + 777, where s0 = 2026 for the two-state settings, s0 =
20261001 for the three-state settings except the heterogeneous design with T = 40, and
s0 = 20261201 for that design. In the missing-data study the retention mask uses seed
s0 + 10,000 ℓ + 500,000,000 + 1000p and the chain seed is increased by 1,000,000 × 100p.




                                              76
F.2     Posterior Summaries
The point estimates are those of Appendix C.3: the Dahl-draw state path and radii (which
are the radii plotted in Figure S1), the SALSO tiers and tier-averaged abilities (19), and
the posterior-mean home effects. SALSO is run with the R package salso using 64 random
initializations and a fixed seed. The θ-MSE is computed from the tier-averaged abilities,
and class ARI is computed between the estimated and true team partitions separately for
each season and then averaged across seasons within each replicate.



G      National Basketball Association (NBA) (2004/05
       to 2023/24)
The second application uses regular-season games from the 20 NBA seasons from 2004/05
to 2023/24, with each season a comparison graph on the 30 franchises. Unlike the Premier
League, the NBA is a closed league that regulates parity directly through the draft, the
salary cap and the luxury tax. The study period begins with the 2004/05 expansion to 30
teams, so the league size is the same in every season, and it includes the 2019 draft lottery
reform, which flattened the lottery odds of the worst teams to discourage tanking, and the
play-in tournament introduced in 2020.
    NBA games cannot end in a tie, so we classify each game by the final margin, the home
score minus the away score: a home win if it exceeds five points, a home loss if it is below
−5, and a close game, treated as a draw, otherwise. This allows the same three-category
ordered-logit likelihood to be used in both applications. The schedule is unbalanced, and
a pair of franchises can meet up to four times, or five for seven pairs in 2023/24, when
in-season tournament knockout games counted toward the regular season. Each meeting


                                             77
enters the likelihood separately, but the graph that defines the radius constraint remains
the unweighted complete graph on the 30 franchises, with 30
                                                               
                                                             2
                                                                 = 435 pairs, including the
five pairs that did not meet in the shortened 2019/20 season; the results of Section 3
require only that this graph be connected. The data contain 24,038 games. A full season
has 1,230, but fewer were played in the lockout-shortened 2011/12 season, in 2012/13,
when one game was cancelled and not replayed, and in the COVID-19-affected 2019/20
and 2020/21 seasons, and we use only the games that were played. Games at the neutral
2020 Orlando venue keep their designated home team, so htg = 1 for every game, as in
Section 3.1. Franchise labels are harmonized across relocations and renamings, such as
Seattle and Oklahoma City or New Jersey and Brooklyn.
   The model, MCMC settings, threshold κ2 = 0.65, home-effect priors, radius grid and
posterior summaries are those of the Premier League analysis in Section 6. The radius
hyperparameters were calibrated separately with the same pilot chains and conditional
WAIC, giving (σβ , ar , br ) = (2, 10, 350). Convergence diagnostics are in Appendix H.




                                             78
                                                                                                                                                                                                                                                          0.6                                                                                                                                                                          Posterior mean
                                      340
                                                                                                                                                                                                                                                                                                                                                                                                                                       90% CrI


         Competitive-balance radius




                                                                                                                                                                                                                                  Home-advantage effect
                                                                                                                                                                                                                                                          0.5
                                      320

                                                                                                                                                                                                                                                          0.4
                                      300

                                                                                                                                                                                                                                                          0.3
                                      280
                                                                                                                           Dahl radius                                                                                                                    0.2
                                                                                                                           90% CrI
                                      260
                                                                                                                           Posterior median
                                                                                                                                                                                                                                                          0.1
                                                                                                                    State
                                      240                                                                           1     2
                                                                                                                                                                                                                                                          0.0
                                                 5

                                                          6

                                                                   7

                                                                            8

                                                                                     9

                                                                                              0

                                                                                                     1

                                                                                                           12


                                                                                                                     3

                                                                                                                              4

                                                                                                                                       5

                                                                                                                                                6

                                                                                                                                                         7

                                                                                                                                                                  8

                                                                                                                                                                           9

                                                                                                                                                                                    0

                                                                                                                                                                                             1

                                                                                                                                                                                                      2

                                                                                                                                                                                                               3

                                                                                                                                                                                                                        4




                                                                                                                                                                                                                                                                     5

                                                                                                                                                                                                                                                                              6

                                                                                                                                                                                                                                                                                       7

                                                                                                                                                                                                                                                                                                8

                                                                                                                                                                                                                                                                                                         9

                                                                                                                                                                                                                                                                                                                  0

                                                                                                                                                                                                                                                                                                                           1

                                                                                                                                                                                                                                                                                                                                 12


                                                                                                                                                                                                                                                                                                                                           3

                                                                                                                                                                                                                                                                                                                                                    4

                                                                                                                                                                                                                                                                                                                                                             5

                                                                                                                                                                                                                                                                                                                                                                       6

                                                                                                                                                                                                                                                                                                                                                                                7

                                                                                                                                                                                                                                                                                                                                                                                         8

                                                                                                                                                                                                                                                                                                                                                                                                   9

                                                                                                                                                                                                                                                                                                                                                                                                            0

                                                                                                                                                                                                                                                                                                                                                                                                                     1

                                                                                                                                                                                                                                                                                                                                                                                                                              2

                                                                                                                                                                                                                                                                                                                                                                                                                                        3

                                                                                                                                                                                                                                                                                                                                                                                                                                                    4
                                                                                                   –1




                                                                                                                                                                                                                                                                                                                         –1
                                             –0

                                                      –0

                                                               –0

                                                                        –0

                                                                                 –0

                                                                                          –1




                                                                                                                    –1

                                                                                                                             –1

                                                                                                                                    –1

                                                                                                                                             –1

                                                                                                                                                      –1

                                                                                                                                                              –1

                                                                                                                                                                       –1

                                                                                                                                                                                –2

                                                                                                                                                                                         –2

                                                                                                                                                                                                  –2

                                                                                                                                                                                                           –2

                                                                                                                                                                                                                    –2




                                                                                                                                                                                                                                                                 –0

                                                                                                                                                                                                                                                                          –0

                                                                                                                                                                                                                                                                                   –0

                                                                                                                                                                                                                                                                                            –0

                                                                                                                                                                                                                                                                                                     –0

                                                                                                                                                                                                                                                                                                              –1




                                                                                                                                                                                                                                                                                                                                       –1

                                                                                                                                                                                                                                                                                                                                                –1

                                                                                                                                                                                                                                                                                                                                                         –1

                                                                                                                                                                                                                                                                                                                                                                  –1

                                                                                                                                                                                                                                                                                                                                                                            –1

                                                                                                                                                                                                                                                                                                                                                                                     –1

                                                                                                                                                                                                                                                                                                                                                                                               –1

                                                                                                                                                                                                                                                                                                                                                                                                        –2

                                                                                                                                                                                                                                                                                                                                                                                                                 –2

                                                                                                                                                                                                                                                                                                                                                                                                                             –2

                                                                                                                                                                                                                                                                                                                                                                                                                                       –2

                                                                                                                                                                                                                                                                                                                                                                                                                                               –2
                                                                                                            –




                                                                                                                                                                                                                                                                                                                                  –
                                                                                                  10




                                                                                                                                                                                                                                                                                                                      10
                                            04

                                                     05

                                                              06

                                                                       07

                                                                                08

                                                                                         09




                                                                                                         11

                                                                                                                12

                                                                                                                         13

                                                                                                                                  14

                                                                                                                                           15

                                                                                                                                                    16

                                                                                                                                                             17

                                                                                                                                                                      18

                                                                                                                                                                               19

                                                                                                                                                                                        20

                                                                                                                                                                                                 21

                                                                                                                                                                                                          22

                                                                                                                                                                                                                   23




                                                                                                                                                                                                                                                                04

                                                                                                                                                                                                                                                                         05

                                                                                                                                                                                                                                                                                  06

                                                                                                                                                                                                                                                                                           07

                                                                                                                                                                                                                                                                                                    08

                                                                                                                                                                                                                                                                                                             09




                                                                                                                                                                                                                                                                                                                               11

                                                                                                                                                                                                                                                                                                                                      12

                                                                                                                                                                                                                                                                                                                                               13

                                                                                                                                                                                                                                                                                                                                                        14

                                                                                                                                                                                                                                                                                                                                                                 15

                                                                                                                                                                                                                                                                                                                                                                           16

                                                                                                                                                                                                                                                                                                                                                                                    17

                                                                                                                                                                                                                                                                                                                                                                                             18

                                                                                                                                                                                                                                                                                                                                                                                                       19

                                                                                                                                                                                                                                                                                                                                                                                                                20

                                                                                                                                                                                                                                                                                                                                                                                                                         21

                                                                                                                                                                                                                                                                                                                                                                                                                                  22

                                                                                                                                                                                                                                                                                                                                                                                                                                              23
                                                                                                                              Season                                                                                                                                                                                                                Season




                                                                                                                                                                                                                                                                                                                                      2016–17 NBA regular season
                                                                                                                                                                                                                                                                     GSW
                                                                                                                                                                                                                                                                     SAS
                                                                                                                                                                                                                                                                      LAC
                                                                                                                                                                                                                                                                     TOR
                                                                                                                                                                                                                                                                     HOU
                                                                                                                                                                                                                                                                      CLE
                                                                                                                                                                                                                                                                      UTA
                                                                                                                                                                                                                                                                     BOS
                                                                                                                                                                                                                                                                     OKC
                                                                                                                                                                                                                                                                     POR
                                                                                                                                                                                                                                                                     DEN
                                                                                                                                                                                                                                                                      MIA
              SAS                                                                                                                                                                                                                                                    WAS
                                                                                                                                                                                                                                                                     MEM
              DAL                                                                                                                                                                                                                                                     IND
            BOS                                                                                                                                                                                                                                                       ATL
                                                                                                                                                                                                                                                                      MIL
             DEN                                                                                                                                                                                                                                                      CHI
         GSW                                                                                                                                                                                                                                                          DET
                                                                                                                                                                                                                            Stronger                                 CHA
                  MIA                                                                                                                                                                                                                                                 MIN
                                                                                                                                                                                                                                                                      DAL                                                                                                                                                     90% CrI
              PHX
                                                                                                                                                                                                                                                                                                                                                                                                                              Posterior mean
                                                                                                                                                                                                                                                                     NOP
           HOU                                                                                                                                                                                                                                                                                                                                                                                                                Tier ability
                                                                                                                                                                                                                                                                     SAC
              LAC                                                                                                                                                                                                                                                    NYK
                                                                                                                                                                                                                                                                     ORL                                                                                                                                                 Tier (1 = strongest)
               UTA                                                                                                                                                                                                                                                     PHI                                                                                                                                               1    2    3    4      5     6
                                                                                                                                                                                                                                                                      LAL                                                                                                                                                7    8    9    10     11    12
             TOR
                                                                                                                                                                                                                                                                     PHX
           OKC                                                                                                                                                                                                                                                       BKN
                   MIL                                                                                                                                                                                                                                                                     −1.0                   −0.5                  0.0                      0.5                     1.0                    1.5                          2.0
                LAL                                                                                                                                                                                                                                                                                                                                  Latent ability
  Team




                   CHI
               CLE
                   IND
         MEM
                                                                                                                                                                                                                                                                                                                                      2010–11 NBA regular season
                 ATL
                                                                                                                                                                                                                                                                      MIA
            POR                                                                                                                                                                                                                                                      SAS
                                                                                                                                                                                                                                                                      CHI
            NOP
                                                                                                                                                                                                                                                                      LAL
             ORL                                                                                                                                                                                                                                                      DAL
                                                                                                                                                                                                                                                                     ORL
               DET
                                                                                                                                                                                                                                                                     OKC
                    PHI                                                                                                                                                                                                                                              BOS
          WAS                                                                                                                                                                                                                                                        DEN
                                                                                                                                                                                                                            Weaker                                   POR
             NYK                                                                                                                                                                                                                                                     MEM
                  MIN                                                                                                                                                                                                                                                HOU
                                                                                                                                                                                                                                                                     NOP
            BKN                                                                                                                                                                                                                                                        PHI
            CHA                                                                                                                                                                                                                                                      PHX
                                                                                                                                                                                                                                                                     NYK
             SAC                                                                                                                                                                                                                                                      ATL
                                                                                                                                                                                                                                                                     GSW
                                      5

                                              6

                                                          7

                                                                   8

                                                                            9

                                                                                     0

                                                                                               1

                                                                                               2

                                                                                                                3

                                                                                                                         4

                                                                                                                                  5

                                                                                                                                           6

                                                                                                                                                    7

                                                                                                                                                             8

                                                                                                                                                                      9

                                                                                                                                                                               0

                                                                                                                                                                                        1

                                                                                                                                                                                                 2

                                                                                                                                                                                                          3

                                                                                                                                                                                                                    4
                                                                                            –1
                              –0

                                              –0

                                                       –0

                                                                –0

                                                                         –0

                                                                                  –1




                                                                                            –1

                                                                                                            –1

                                                                                                                      –1

                                                                                                                               –1

                                                                                                                                        –1

                                                                                                                                                 –1

                                                                                                                                                          –1

                                                                                                                                                                    –1

                                                                                                                                                                             –2

                                                                                                                                                                                      –2

                                                                                                                                                                                               –2

                                                                                                                                                                                                        –2

                                                                                                                                                                                                                 –2




                                                                                                                                                                                                                                                                      UTA
                                                                                         10
                            04

                                            05

                                                     06

                                                              07

                                                                       08

                                                                                09




                                                                                         11

                                                                                                          12

                                                                                                                    13

                                                                                                                             14

                                                                                                                                      15

                                                                                                                                               16

                                                                                                                                                        17

                                                                                                                                                                  18

                                                                                                                                                                           19

                                                                                                                                                                                    20

                                                                                                                                                                                             21

                                                                                                                                                                                                      22

                                                                                                                                                                                                               23




                                                                                                                                                                                                                                                                      IND
                                                                                                                         Season                                                                                                                                       MIL
                                                                                                                                                                                                                                                                      DET                                                                                                                                             90% CrI
                                                                                                                                                                                                                                                                                                                                                                                                                      Posterior mean
                                                                                                                                                                                                                                                                     CHA
                                                                                                                                                                                                                                                                                                                                                                                                                      Tier ability
                                                                                                                                                                                                                                                                      LAC
                                                                                                                                                                                                                                                                     SAC
                                                                                                                                                                                                                                                                     TOR                                                                                                                                              Tier (1 = strongest)
                                                                                                                                                                                                                                                                      MIN                                                                                                                                       1    2   3        4     5      6     7
                                                                                                                                                                                                                                                                     BKN                                                                                                                                        8    9   10       11    12     13    14
                                                                                                                                                                                                                                                                     WAS
                                                                                                                                                                                                                                                                      CLE
                                                                                                                                                                                                                                                                                       −1.5                       −1.0                 −0.5                       0.0                        0.5                      1.0                           1.5

                                                                                                                                                                                                                                                                                                                                                     Latent ability




Figure S3: Posterior summaries for the NBA, 2004/05 to 2023/24. Upper panels: season-
specific competitive-balance radius and home-advantage effect with 90% credible intervals.
Lower left: longitudinal team tiers. Right: team abilities and tiers for 2016/17 (State 1)
and 2010/11 (State 2); circles are posterior means, segments 90% credible intervals, and
triangles tier-level estimates.
                                            79
   The sampler favors two states, which are occupied in 87.7% of retained draws. The Dahl
draw gives radii of 269.8 for the more balanced State 1 and 338.5 for the more stratified
State 2, about 25% larger. Unlike the Premier League, the NBA switches back and forth
between the two. The seasons 2004/05 to 2006/07 are in State 1, followed by nine seasons
in State 2 from 2007/08 to 2015/16. The league then returns to State 1 in 2016/17 and
2017/18, to State 2 in 2018/19 and 2019/20, to State 1 from 2020/21 to 2022/23, and to
State 2 in 2023/24, so 12 of the 20 seasons are in the stratified state. Among draws with
two states, the average self-transition frequencies are 0.52 for State 1 and 0.78 for State 2,
so stratified spells tend to last longer than balanced ones.
   Within seasons, the tiers need not follow the order of total wins, because close games
count as draws and abilities are estimated from all opponent-specific results. In 2010/11
Chicago had the best record at 62–20, ahead of San Antonio at 61–21 and Miami at 58–
24, but the model places Miami alone in the top tier, San Antonio second and Chicago
third. Miami had 52 decisive wins, 20 draws and 10 decisive losses, against 45, 25 and
12 for Chicago, and Chicago’s three wins over Miami came by three, four and one point,
so all three count as draws. Miami later beat Chicago 4–1 in the Eastern Conference
Finals, which was not used in estimation. The season followed LeBron James’s move from
Cleveland to Miami: Cleveland fell from 61–21 to 19–63 and is in the bottom tier. With
fourteen tiers in total, the large State 2 radius reflects separation across the whole league
rather than the dominance of one team.
   The lower-radius 2016/17 season shows the opposite case. Golden State, with 67 wins
after signing Kevin Durant, is alone in the top tier and San Antonio is second, but below
them many teams are close: the model finds twelve tiers, and 14 of the 30 teams share
one middle tier. A single dominant team therefore does not imply a large radius, which
measures how widely abilities are spread across the league. The same season also shows


                                             80
the role of head-to-head results. Boston finished first in the Eastern Conference at 53–29,
ahead of Cleveland at 51–31, yet Cleveland is in the fifth tier and Boston in the sixth.
Cleveland had 40 decisive wins and 20 draws, against 36 and 25 for Boston, and won three
of their four meetings by six, six and 23 points, while Boston’s four-point win counts as a
draw. Cleveland went on to beat Boston 4–1 in the Eastern Conference Finals.
    Across seasons, San Antonio stays in strong tiers for much of the earlier period, and
Golden State rises to a lasting place near the top, drops sharply in 2019/20 and then
recovers. As in the Premier League, seasons in the same state need not have the same
leading teams.
    The posterior mean home effect is positive in every season, ranging from about 0.16 to
0.51 with an average of 0.37, and is smallest in 2020/21, when attendance was restricted.
This is a season-specific effect in the observation model rather than a causal effect of
crowds. Finally, a season-level measure of dispersion allows the timing of parity reforms to
be compared with changes in balance. The 2019 lottery reform and the play-in tournament
were followed by three seasons in State 1, from 2020/21 to 2022/23, before a return to
State 2 in 2023/24. This timing is only descriptive and does not show that the reforms
caused the shift.



H      Computational Diagnostics for the Real-Data Anal-
       yses
For each dataset, we ran two independently initialized chains for 50,000 iterations, dis-
carding the first 5,000 as burn-in. The allocation parameters are those of the simulations,
(atr , γ, λ) = (2.5, 0.5, 0.5), with the J = 15 point radius grid, and the proposal standard
deviations are ςr = 0.20 for log rk and ςη = 0.16 for ηt . Run in parallel on the same laptop,

                                             81
each chain took about 56 minutes for the Premier League and about 61 minutes for the
NBA. All diagnostics were computed using the 45,000 retained draws per chain. We moni-
tored the number of occupied states K, the season-assigned radius rst , the home-advantage
effect ηt , the shared radius rate αr , and all team-season ability components θti . The diag-
nostics used the full posterior samples, allowing the number and assignments of states to
vary across draws.
   Figures S4–S9 show the traces and empirical distributions from both chains. Faint lines
represent individual draws, with every twentieth draw shown for the radius and home-
advantage traces to improve readability. Solid lines represent means over non-overlapping
blocks of 500 iterations. All numerical diagnostics and empirical distributions of K were
computed from the full, unthinned samples.
   For the Premier League, K = 2 was the most frequent outcome in both chains, ac-
counting for 69.2% and 65.6% of retained draws, respectively. The proportions with K = 3
were 27.4% and 31.0%. For the NBA, the proportions with K = 2 were 87.7% and 87.8%.
Thus, both datasets favored a two-state representation, with greater uncertainty about a
third state in the Premier League. The rank-normalized split-Rb values for K were 1.0018

for the Premier League and 1.0009 for the NBA.
   The home-advantage effects showed close agreement between chains, with maximum R
                                                                                  b

values of 1.0007 for the Premier League and 1.0004 for the NBA. For the season-assigned
radii, the corresponding maxima were 1.0134 and 1.0049. Four of the 25 Premier League
radius components had R b > 1.01, compared with none of the 20 NBA components. Among

team abilities, all 500 Premier League components had R
                                                      b < 1.01 (maximum 1.0085), while

14 of the 600 NBA components exceeded 1.01 (maximum 1.0187). Across all monitored
scalar quantities, the minimum bulk and tail effective sample sizes were approximately 476
and 706 for the Premier League, and 231 and 214 for the NBA.


                                             82
    Overall, the diagnostics indicate good cross-chain agreement for most monitored quan-
tities. The relatively larger R
                              b values were confined to a small number of Premier League

radius components and NBA team abilities.


Monte Carlo check of emission separation. Lemma B.2 establishes Assumption 4.1
only near r = 0. As Monte Carlo evidence at the fitted radii, and not as a proof of
separation at all radii, we evaluated SX (r) under (16) at the settings of both applications:
the complete-graph constraint, σβ = 2, η ∼ N (0, 1) and κ2 = 0.65. The home effect
was integrated by 60-point Gauss–Hermite quadrature, and β by Monte Carlo with 20,000
draws shared across radii. Under the complete-graph constraint the pairwise contrasts are
exchangeable, so SX (r) = |P| Spair (r), where |P| = 190 in every Premier League season and
645–945 in the NBA. On grids of spacing 20 over [0, 600] (N = 20) and 46.7 over [0, 1400]
(N = 30), both including the fitted radii, every increment of Spair was positive, at least 4.9
Monte Carlo standard errors from zero. For the Premier League, Spair = 0.443 at r = 97.1
and 0.487 at r = 155.4, so the expected SX differs by about 8 between the two states,
comparable to a binomial standard deviation of about 7 for a single season, so this statistic
separates the two states only weakly within any one season. For the NBA, Spair = 0.456 at
r = 269.8 and 0.478 at r = 338.5. The increments shrink as the constraint stops binding:
Pr(Z > r) falls below 0.5 near r = 430 for the Premier League and near r = 980 for the
NBA, whereas it exceeds 0.999 at all four fitted radii.




                                             83
                                                                  EPL | Number of occupied states
                                                                           Chain 1              Chain 2
                        (a) K trace                                                                                                     (b) K distribution
                                                                                                                                  1.0
                    6

                                                                                                                                  0.8
                    5




                                                                                                          Empirical probability
Occupied states K




                    4                                                                                                             0.6


                    3                                                                                                             0.4


                    2
                                                                                                                                  0.2

                    1
                                                                                                                                  0.0
                               10k         20k            30k             40k             50k                                                1        2         3         4      5   6
                                                 MCMC iteration                                                                                              Occupied states K




                                Figure S4: Diagnostics for the number of occupied states K in the Premier League. Left:
                                retained traces and block means. Right: empirical distributions normalized separately for
                                each chain.




                                                                                     84
                                                             EPL | Season-assigned radius
                                                                          Chain 1             Chain 2



           180                                                                                                                            180
                                       120                                                                    150
                                                                    120
           120
                                                                                                              100                         120
                                        60
                                                                     60
            60
                                                                                                               50                          60
                                         0                            0
                 10k      30k    50k         10k      30k     50k          10k         30k              50k         10k      30k    50k         10k      30k    50k
                       1995-96                     1996-97                          1997-98                               1998-99                     1999-00

           180
                                                                    180
                                       150                                                                                                150
           120                                                                                                120
                                                                    120
                                       100                                                                                                100
            60                                                                                                 60
                                                                     60
                                        50                                                                                                 50
                 10k      30k    50k         10k      30k     50k          10k         30k              50k         10k      30k    50k         10k      30k    50k
                       2000-01                     2001-02                          2002-03                               2003-04                     2004-05


           200                                                                                                                            200
Radius r




                                                                    200
                                       150
           150                                                                                                150
                                                                                                                                          150
                                                                    150
                                       100
           100                                                                                                100                         100
                                                                    100
                                        50
                 10k      30k    50k         10k      30k     50k          10k         30k              50k         10k      30k    50k         10k      30k    50k
                       2005-06                     2006-07                          2007-08                               2008-09                     2009-10


           160                                                                                                                            180
                                       180                                                                    200

                                                                    150
                                                                                                              150                         120
            80                         120

                                                                    100
                                                                                                              100                          60
             0                          60
                 10k      30k    50k         10k      30k     50k          10k         30k              50k         10k      30k    50k         10k      30k    50k
                       2010-11                     2011-12                          2012-13                               2013-14                     2014-15

                                                                    200
                                       200                                                                    240
           150                                                                                                                            180

                                                                    150
                                       150                                                                    180
           100                                                                                                                            120

                                                                    100                                       120
            50                         100
                                                                                                                                           60
                 10k      30k    50k         10k      30k     50k          10k         30k              50k         10k      30k    50k         10k      30k    50k
                       2015-16                     2016-17                          2017-18                               2018-19                     2019-20




                        Figure S5: Season-assigned-radius traces for all 25 Premier League seasons. The traces
                        reflect variation in both state assignments and radii across posterior draws.
                                                                     85
                                                                          EPL | Home advantage
                                                                                 Chain 1             Chain 2



                                              0.8
                                                                                                                     0.8
                                                                           0.8                                                                   0.8
                  0.8
                                              0.4
                                                                                                                     0.4
                                                                           0.4                                                                   0.4
                  0.4
                                              0.0

                        10k      30k    50k         10k      30k    50k           10k         30k              50k         10k      30k    50k         10k      30k    50k
                              1995-96                     1996-97                          1997-98                               1998-99                     1999-00

                                              0.8
                                                                                                                     0.8                         0.8
                  0.8                                                      0.8
                                              0.4
                                                                                                                     0.4                         0.4
                  0.4                                                      0.4

                                              0.0
                                                                                                                     0.0
                                                                                                                                                 0.0
                        10k      30k    50k         10k      30k    50k           10k         30k              50k         10k      30k    50k         10k      30k    50k
                              2000-01                     2001-02                          2002-03                               2003-04                     2004-05
Home effect eta




                                                                                                                     0.8

                  0.8                         0.8
                                                                           0.8
                                                                                                                                                 0.8
                                                                                                                     0.4

                  0.4                         0.4                          0.4
                                                                                                                                                 0.4
                                                                                                                     0.0

                        10k      30k    50k         10k      30k    50k           10k         30k              50k         10k      30k    50k         10k      30k    50k
                              2005-06                     2006-07                          2007-08                               2008-09                     2009-10


                                                                           0.8                                       0.8                         0.8
                  0.8                         0.6


                                                                           0.4                                       0.4                         0.4
                                              0.3
                  0.4

                                              0.0                          0.0                                       0.0                         0.0
                        10k      30k    50k         10k      30k    50k           10k         30k              50k         10k      30k    50k         10k      30k    50k
                              2010-11                     2011-12                          2012-13                               2013-14                     2014-15


                                                                           0.8                                       0.8                         0.8
                                              0.8
                  0.4
                                                                           0.4                                       0.4                         0.4
                                              0.4
                  0.0
                                                                           0.0                                       0.0                         0.0

                        10k      30k    50k         10k      30k    50k           10k         30k              50k         10k      30k    50k         10k      30k    50k
                              2015-16                     2016-17                          2017-18                               2018-19                     2019-20




                               Figure S6: Home-advantage-effect traces for all 25 Premier League seasons. Gray-blue and
                               muted red indicate the two chains.
                                                                          86
                                                              NBA | Number of occupied states
                                                                       Chain 1              Chain 2
                        (a) K trace                                                                                                 (b) K distribution
                                                                                                                              1.0
                    4

                                                                                                                              0.8




                                                                                                      Empirical probability
Occupied states K




                    3
                                                                                                                              0.6



                                                                                                                              0.4
                    2


                                                                                                                              0.2

                    1
                                                                                                                              0.0
                               10k         20k            30k         40k             50k                                                   1             2             3    4
                                                 MCMC iteration                                                                                          Occupied states K




                                Figure S7: Diagnostics for the number of occupied states K in the NBA. Left: retained
                                traces and block means. Right: empirical distributions normalized separately for each
                                chain.




                                                                                 87
                                                             NBA | Season-assigned radius
                                                                          Chain 1              Chain 2


           360
                                                                    320                                                                    350
                                       320
                                                                                                               360
           300
                                                                    240                                                                    300
                                       240
                                                                                                               300
           240
                                                                                                                                           250
                                                                    160
                 10k      30k    50k         10k      30k     50k          10k           30k             50k         10k      30k    50k         10k      30k    50k
                       2004-05                     2005-06                           2006-07                               2007-08                     2008-09


                                                                    360                                        360
           350                         350
                                                                                                                                           360
                                                                    300
                                                                                                               300
           300                         300
                                                                                                                                           300
                                                                    240
                                       250                                                                     240
           250
Radius r




                                                                                                                                           240
                 10k      30k    50k         10k      30k     50k          10k           30k             50k         10k      30k    50k         10k      30k    50k
                       2009-10                     2010-11                           2011-12                               2012-13                     2013-14


                                                                                                               360
           360                                                                                                                             360
                                       350                          320
                                                                                                               300
           300                                                                                                                             300
                                       300
                                                                    240
                                                                                                               240
           240                                                                                                                             240
                                       250
                 10k      30k    50k         10k      30k     50k          10k           30k             50k         10k      30k    50k         10k      30k    50k
                       2014-15                     2015-16                           2016-17                               2017-18                     2018-19


                                       360                          360
           360                                                                                                 320
                                                                                                                                           360

                                       300                          300
           300                                                                                                 240
                                                                                                                                           300
                                       240                          240

           240                                                                                                 160
                                                                                                                                           240
                 10k      30k    50k         10k      30k     50k          10k           30k             50k         10k      30k    50k         10k      30k    50k
                       2019-20                     2020-21                           2021-22                               2022-23                     2023-24




                        Figure S8: Season-assigned-radius traces for all 20 NBA seasons, reflecting variation in
                        both state assignments and radii.




                                                                                    88
                                                                          NBA | Home advantage
                                                                                  Chain 1              Chain 2



                                              0.6                           0.6
                                                                                                                                                   0.6
                  0.6                                                                                                  0.6

                                              0.4                           0.4
                  0.4                                                                                                  0.4                         0.4


                                              0.2                           0.2
                        10k      30k    50k         10k      30k    50k            10k           30k             50k         10k      30k    50k         10k      30k    50k
                              2004-05                     2005-06                            2006-07                               2007-08                     2008-09


                                                                           0.75
                  0.6                         0.6
                                                                                                                       0.6
                                                                                                                                                   0.4
                                                                           0.50
                  0.4                         0.4
                                                                                                                       0.4
                                                                                                                                                   0.2
Home effect eta




                  0.2                                                      0.25
                                              0.2
                        10k      30k    50k         10k      30k    50k            10k           30k             50k         10k      30k    50k         10k      30k    50k
                              2009-10                     2010-11                            2011-12                               2012-13                     2013-14


                                              0.6
                                                                                                                                                   0.6
                                                                            0.6
                                                                                                                       0.4
                  0.4
                                              0.4
                                                                                                                                                   0.4
                                                                            0.4                                        0.2
                  0.2
                                              0.2
                                                                                                                                                   0.2
                                                                            0.2                                        0.0
                        10k      30k    50k         10k      30k    50k            10k           30k             50k         10k      30k    50k         10k      30k    50k
                              2014-15                     2015-16                            2016-17                               2017-18                     2018-19


                                              0.4                                                                      0.6                         0.4

                  0.4                                                       0.4

                                              0.2                                                                      0.4
                                                                                                                                                   0.2
                  0.2                                                       0.2
                                              0.0                                                                      0.2
                                                                                                                                                   0.0
                  0.0                                                       0.0
                        10k      30k    50k         10k      30k    50k            10k           30k             50k         10k      30k    50k         10k      30k    50k
                              2019-20                     2020-21                            2021-22                               2022-23                     2023-24




                               Figure S9: Home-advantage-effect traces for all 20 NBA seasons. Gray-blue and muted red
                               indicate the two chains.




                                                                                            89
