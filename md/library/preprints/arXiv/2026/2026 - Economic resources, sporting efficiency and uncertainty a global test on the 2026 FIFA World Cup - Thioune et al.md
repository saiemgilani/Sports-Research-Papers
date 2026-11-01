<!-- source: library/preprints/arXiv/2026/2610.28344.pdf -->
<!-- arXiv:2610.28344 | submitted 2026-10-20 | https://arxiv.org/abs/2610.28344 -->

# Economic resources, sporting efficiency and uncertainty: a global test on the 2026 FIFA World Cup

```text
                                                Economic resources, sporting efficiency and
                                           uncertainty: a global test on the 2026 FIFA world cup
                                                                     Thierno Thioune1 and Babacar Mbaye Ndiaye2
                                           1
                                               Laboratory for Analysis, Research and Study of Development, University of Cheikh Anta
                                                                Diop, Dakar, Senegal, thierno.thioune@ucad.edu.sn
arXiv:2610.28344v1 [math.OC] 20 Oct 2026




                                                2
                                                  Laboratory of Mathematics of Decision and Numerical Analysis, University of Cheikh
                                                             Anta Diop, Dakar, Senegal, babacarm.ndiaye@ucad.edu.sn


                                                                                       October 21, 2026


                                                                                            Abstract
                                                       A related paper [1] developed a stochastic optimization framework in which football per-
                                                  formance combines GDP/population-based potential with a latent mean-reverting efficiency
                                                  process. The framework was applied to a cross-section of the 24 national teams participating
                                                  in AFCON 2025. This paper applies the same methodology to the full 48-team 2026 FIFA
                                                  World Cup, extending the analysis beyond Africa without modifying the underlying model.
                                                  Using GDP, population, FIFA ranking data, and complete tournament outcomes, it evaluates
                                                  the framework against a global sample spanning all six confederations. Two findings emerge.
                                                  First, GDP and population explain only 9% of single-tournament performance variance, com-
                                                  pared with 33% for FIFA points. This gap is consistent with the model’s distinction between
                                                  systematic performance and match-specific idiosyncratic shocks. Second, using the less noisy
                                                  FIFA-points measure, the African pattern persists globally: Morocco, Senegal, Argentina, Croa-
                                                  tia, Portugal, and Uruguay emerge as leading GDP-relative over-performers. Conversely, several
                                                  major economies, including the United States, Germany, Japan, and South Korea, underperform
                                                  their GDP-implied potential. As in the related paper, we interpret the residual as a symmetric,
                                                  non-structurally identified conditional performance residual, rather than an SFA-consistent ef-
                                                  ficiency estimate. We also quantify the extent to which its cross-country variance mechanically
                                                  reflects the underlying performance measure. The GDP-rank/simulated-performance-rank cor-
                                                  relation is robust to the choice of the model’s un-identified dynamic parameters (κ, σ) across a
                                                  wide grid.

                                           Keywords: economic capacity, football performance, FIFA World Cup, stochastic optimization,
                                           uncertainty, cross-country efficiency, stochastic frontier analysis.


                                           1      Introduction
                                           The related paper on African football [1] models national-team performance Yi,t as the product
                                           of an economic-potential production function f (Xi,t ) and a latent, mean-reverting log-efficiency
                                           process θi,t = ezi,t , plus an idiosyncratic shock εi,t :

                                                                                                                                    θi,t = ezi,t .
                                                                                                                  
                                                  Yi,t = θi,t f (Xi,t ) + εi,t , dzi,t = κi (z̄i − zi,t ) + γi ui,t dt + σi dWi,t ,                (1)



                                                                                                 1
The related paper derives Equation (1) as the state equation of a discounted stochastic control
problem, gives the associated Hamilton–Jacobi–Bellman equation and optimal investment rule,
and proves a verification theorem under explicit growth conditions [1, Sections 3.2–3.5]. It also
positions the resulting efficiency measure explicitly relative to the stochastic frontier and data
envelopment analysis (SFA/DEA) traditions [1, Section 2.4]. This paper does not repeat that
derivation: it reuses only the state equation (1) and the related paper’s cross-sectional estimation
strategy, applied here for the first time outside Africa. That paper estimated the model on a cross-
section of the 24 Africa Cup of Nations 2025 teams. The 2026 FIFA World Cup, the first 48-team
edition and jointly hosted by the United States, Canada, and Mexico, concluded on 19 July 2026
with Spain’s 1–0 extra-time victory over Argentina. It provides a natural large-scale out-of-sample
test of whether the GDP/population–efficiency relationship observed for AFCON persists globally
across all six confederations.
This paper applies the framework unchanged: the same production function f (Xi ) = A·GDPiα1 P opαi 2 ,
cross-sectional estimation with heteroskedasticity-robust inference, stochastic simulation of (1), and
sensitivity analysis over (κ, σ). As in [1], the collinear GDP pci = GDPi /P opi regressor is excluded.
As in the paper [1], we relabel the estimated residual a conditional performance residual through-
out, and we quantify explicitly how much of it is, by construction, a restatement of the performance
measure used to estimate it (Section 4.2). Section 2 briefly restates, in this global setting, what
such a residual is and is not relative to SFA/DEA. Section 3 describes the data: all 48 qualified
teams, their real GDP, population and FIFA ranking points, and the actual, complete 2026 World
Cup result. Section 4 reports two regressions with robust inference – one on the actual tournament
outcome, one on FIFA points – compares them, and quantifies circularity for both. Section 5 runs
the simulation and sensitivity analysis. Section 6 discusses what generalizes from Africa to the
world, and what does not.


2    Relation to stochastic frontier analysis and DEA
As discussed at length in the related paper [1, Section 2.4], the residual estimated below is not a
structurally identified efficiency term in the sense of stochastic frontier analysis [SFA; 2] or data
envelopment analysis [DEA; 3]. Both SFA and DEA are static methods that decompose or bound
a one-sided inefficiency term relative to a best-practice frontier, estimated from a snapshot of
inputs and outputs. The quantity we estimate here by OLS, zi = ln(Yi ) − ln    d f (GDPi , P opi ), is a
symmetric residual: it can be positive or negative, mixes ordinary noise with any genuine efficiency
component, and no distributional assumption separates the two. We therefore refer to it throughout
as a conditional performance residual – performance conditional on GDP and population – rather
than as a validated efficiency parameter. The Section 4.2 quantifies exactly how much of its cross-
country variance is mechanically determined by the fit of the underlying regression rather than
by any independent efficiency signal. The contribution of both papers lies not in improving static
efficiency estimation relative to SFA or DEA, but in providing a dynamic control framework once
such an efficiency measure is observed. This distinction, discussed in [1, Section 2.4], applies
unchanged to the global sample considered here.




                                                   2
3     Data
3.1    The 48 qualified teams
The 2026 World Cup expanded the field from 32 to 48 teams for the first time. Slot allocation by
confederation: UEFA 16, CAF 10 (9 direct plus DR Congo via the intercontinental play-off), AFC 9
(8 direct plus Iraq via the intercontinental play-off), CONCACAF 6 (three hosts – Canada, Mexico,
USA – plus Panama, Haiti and Curaçao), CONMEBOL 6, OFC 1 (New Zealand)1 . Economic data:
nominal GDP and GDP per capita, from the IMF World Economic Outlook database directly (April
2026 edition), 2026 projections;2 population is computed as GDP/GDP pc. FIFA ranking data:
FIFA Men’s World Ranking points, from the FIFA World Ranking directly, ranking dated 20 July
2026.3
A data limitation, disclosed. England and Scotland compete as separate national teams but
are not sovereign states and have no independent GDP or population statistics; both are assigned
the United Kingdom’s GDP and population as the best available proxy.
This is a genuine approximation, not a modeling choice. It mechanically produces a large negative
conditional performance residual for whichever of the two has the lower FIFA ranking (Scotland),
simply because both are compared to the same (larger, UK-wide) economic potential. We flag
every instance where this affects the results below.

3.2    The actual 2026 World Cup result
Champion: Spain. Runner-up: Argentina. Third place (beating France 6–4 in a ten-goal match):
England. Fourth place: France. Quarter-final losers: Morocco (to France), Belgium (to Spain),
Norway (to England), Switzerland (to Argentina).4 Following the coarse, independently verifiable
scoring scale of [1] (chosen for direct comparability): Champion= 6, Runner-up= 5, 3rd= 4,
4th= 3.5, quarter-final exit= 2.5, and every other team (round of 32, round of 16 or group-stage
exit)= 1.


4     Results
4.1    Two regressions, robust inference, and why they disagree
We estimate, by OLS on the N = 48 qualified teams,

                              ln(Yi ) = ln A + α1 ln GDPi + α2 ln P opi + zi ,

once with Yi equal to the actual World Cup 2026 performance score (regression A), and once with
Yi equal to FIFA ranking points (regression B, our primary measure). Table 1 reports both, with
heteroskedasticity-robust (HC3) standard errors and the joint test H0 : α1 = α2 = 0, appropriate
given the modest sample size and the very different variance structure of the two outcome variables.
The gap between the two R2 s (0.09 vs. 0.33) is itself a substantive finding, not noise to be explained
away, and robust inference sharpens rather than changes this reading. In regression (A), 40 of
   1
     Compiled from FIFA/CAF/UEFA/CONCACAF qualification records and the March 2026 inter-confederation
play-off tournament (winners: DR Congo and Iraq, from a six-team pool that also included Bolivia, Jamaica, New
Caledonia and Suriname).
   2
     International Monetary Fund, World Economic Outlook database, April 2026 edition, https://www.imf.org/
en/Publications/WEO.
   3
     FIFA World Ranking, https://www.fifa.com/fifa-world-ranking, ranking date 20 July 2026.
   4
     Cross-checked against contemporaneous match reports (NPR, CBS News, ESPN, beIN Sports; July 2026).


                                                      3
Table 1: Two cross-sectional regressions on the same 48 teams. HC3 robust standard errors in
parentheses.
                                                  α̂1 (GDP)              α̂2 (Population)                        R2 (adj.)           Joint test H0 : α1 = α2 = 0
                                                               ∗∗
     (A) Actual WC2026 score             0.109 (0.050)                     −0.065 (0.047)                 0.091 (0.050)              F = 2.44, p = 0.099
     (B) FIFA points (primary)          0.034 (0.011)∗∗∗                    0.003 (0.012)                 0.328 (0.298)              F = 13.32, p < 0.001
∗∗
     p < 0.05, ∗∗∗ p < 0.01 (robust t-tests, individual coefficients).


the 48 teams share the same pre-quarter-final score, making their residuals mechanically equal to
zi = −ln
       d f (GDPi , P opi ). Thus, these residuals largely reflect the coarse scoring structure rather
than an independent performance signal (Figure 1), explaining the extreme negative residual of the
United States.
                                                                         Conditional performance residual from the actual
                                                                          WC2026 result alone (single tournament, large
                                                                             idiosyncratic-shock share -- see caveat)

                                                   Spain
                                             Argentina
                                               England
                                                  France
                                               Morocco
                                               Belgium
                                                Norway
                                            Switzerland
                                            Cabo Verde
                                                Senegal
                                             DR Congo
                                                    Haiti
                                               Curacao
                                                 Tunisia
                                           Cote d'Ivoire
                                                  Ghana
                                                  Jordan
                                Bosnia and Herzegovina
                                              Paraguay
                                            Uzbekistan
                                                     Iran
                                               Ecuador
                                                   Egypt
                                                     Iraq
                                                 Algeria
                                                Panama
                                           South Africa
                                               Uruguay
                                              Colombia
                                                 Croatia
                                               Portugal
                                          New Zealand
                                                Czechia
                                                   Brazil
                                                   Qatar
                                                 Mexico
                                                 Turkiye
                                           Saudi Arabia
                                                 Austria
                                           South Korea
                                                Sweden
                                                   Japan
                                           Netherlands
                                                Canada
                                              Australia
                                               Scotland
                                              Germany
                                                     USA

                                                            0.50       0.25 0.00 0.25 0.50 0.75 1.00 1.25                            1.50
                                                                    ziWC = ln(YiWC2026) lnf(GDPi, Popi) (tie-affected, see caveat)



Figure 1: Conditional performance residual from the actual WC2026 result alone (regression A):
40 of 48 teams are tied, so their ordering is driven almost mechanically by −ln
                                                                             d  f (GDPi , P opi ).

Although GDP is individually significant in regression (A) ((p = 0.029), the joint test is only
marginally significant ((p = 0.099) and explanatory power remains low. With a coarse, heavily
tied outcome, these results are not contradictory and should be interpreted jointly rather than in

                                                                                    4
isolation. More fundamentally, a single-elimination tournament provides only a thin realization of
the idiosyncratic shock εi,t , whereas FIFA points aggregate performance over a much longer horizon.
By averaging out these shocks, FIFA points better capture the systematic component θi,t f (Xi,t )
targeted by the model. This is exactly what the related paper’s own state-space formulation
anticipates: a noisier, higher-frequency Y identifies θ less precisely than a smoothed one. We
therefore use regression (B) – FIFA points, directly comparable to the AFCON paper’s own measure,
and jointly significant at p < 0.001 – as the primary measure for the simulation below, and use (A)
only as a qualitative check.
A validation check. Despite the low R2 of regression (A), the FIFA-implied performance ranking
exhibits predictive content for actual tournament outcomes. Of the eight 2026 quarter-finalists,
six (Argentina, Spain, Morocco, France, England, and Belgium) rank among the FIFA-implied top
10 by zi . FIFA World Cup 2026 Quarterfinal Fixtures confirms these six were among the eight
quarter-finalists. Norway and Switzerland, the exceptions, are precisely two of the tournament’s
best-documented surprise runs.

4.2   Quantifying circularity in both regressions
As emphasized in the revised related paper, the correlation between an OLS residual and its de-
pendent variable is not free evidence of an independent signal: by construction, Corr(zi , ln Yi ) =
√
  1 − R2 for any regression, regardless of what Yi measures. We compute this explicitly for both
regressions here.
For regression (A) (actual WC2026 score, R2 = 0.091),
                                                    √
                          Corr ziW C , ln YiW C2026 = 1 − 0.091 = 0.954,
confirmed numerically at 0.9537. This extremely high mechanical correlation is the same phe-
nomenon already flagged qualitatively above (the tie artifact): with such a low R2 , the residual is,
for practical purposes, almost the raw (log) outcome itself, re-centered.
For regression (B) (FIFA points, R2 = 0.328),
                                                 √
                            Corr zi , ln(FIFAi ) = 1 − 0.328 = 0.820,
confirmed numerically at 0.8197, and the Spearman rank correlation between the country ranking
implied by zi and the raw FIFA-points ranking is 0.801 (p < 0.001). This is close to, and slightly
higher than, the corresponding figure in the AFCON study (0.808 for the Pearson correlation, 0.734
for the Spearman rank correlation, on N = 24).
As in the related paper, claims of GDP-relative over-performance should be interpreted in light
of the modest explanatory power of GDP and population (R2 = 0.33). Thus, “over-performance”
denotes a conditional deviation from the model-implied benchmark rather than a direct measure
of efficiency.
The residual likely also captures omitted factors, including institutional quality, diaspora and ex-
patriate players, football tradition, and demographic structure. Reliable data on these factors are
unavailable across the full 48-country, six-confederation sample, limiting their explicit inclusion in
the analysis. We requalify zi as a conditional performance residual accordingly, including in the
abstract, rather than as a validated efficiency parameter.

4.3   Conditional performance residuals (FIFA points, primary measure)
Figure 2 plots zi for all 48 teams. The largest positive residuals are Argentina, Spain, Morocco,
Croatia, France, Portugal, Senegal, England, Belgium and Uruguay. The largest negative resid-
uals are New Zealand, Saudi Arabia, Haiti, Scotland (data-limitation caveat above), Iraq, South

                                                  5
Africa, Jordan, Ghana, USA and Uzbekistan. Morocco and Senegal, the two leading African
over-performers in [1], again rank among the largest over-performers globally. This provides out-
of-sample support for the related paper’s central finding, albeit subject to the circularity caveat
discussed above.
Several of the world’s largest economies under-perform their GDP/population potential: the USA
($32.4 trillion GDP, largest in the field, z = −0.09), Germany (z ≈ −0.01, borderline), Japan
(z = −0.03), South Korea (z = −0.07) and Canada (z = −0.07).

                                                             Conditional performance residual (FIFA points, primary
                                                             measure): over- vs under-performance relative to GDP
                                                                      and population (48 WC2026 teams)

                                    Argentina
                                          Spain
                                      Morocco
                                        Croatia
                                         France
                                      Portugal
                                       Senegal
                                      England
                                      Belgium
                                      Uruguay
                                     Colombia
                                  Netherlands
                                          Brazil
                                   Cabo Verde
                                   Switzerland
                                      Ecuador
                                     Paraguay
                                        Mexico
                                       Norway
                                  Cote d'Ivoire
                                            Iran
                                          Egypt
                                        Algeria
                                        Austria
                                     Germany
                                       Panama
                                    DR Congo
                       Bosnia and Herzegovina
                                          Japan
                                      Curacao
                                        Tunisia
                                        Turkiye
                                       Sweden
                                     Australia
                                  South Korea
                                       Canada
                                       Czechia
                                          Qatar
                                   Uzbekistan
                                            USA
                                         Ghana
                                         Jordan
                                  South Africa
                                            Iraq
                                      Scotland
                                           Haiti
                                  Saudi Arabia
                                 New Zealand

                                                   0.20      0.15 0.10 0.05 0.00 0.05 0.10 0.15 0.20
                                                          conditional performance residual zi = ln(FIFAi) lnf(GDPi, Popi)



Figure 2: Conditional performance residual zi (FIFA points regression, primary measure) for all 48
World Cup 2026 teams.



5     Simulation and sensitivity
5.1   Simulation and GDP-rank vs. performance-rank
As in [1], each team is simulated forward from zi,0 = z̄i = zi under (1) with shared illustrative
parameters (κ = 0.7, σ = 0.30, γ = 0.6, c = 1, constant investment u = 0.2, horizon T = 5 years,
fi the GDP/population-based fitted potential).


                                                                          6
As in the related paper, setting z̄i = zi is an identification assumption rather than a normalization.
It enables simulation from a single cross-section without estimating z̄i , but mechanically preserves
each country’s initial relative standing rather than identifying it endogenously.
Figure 3 shows a positive rank correlation (0.562) between GDP and simulated performance, while
substantial deviations highlight the role of the conditional performance residual. This pattern is
consistent with the AFCON analysis, where the corresponding correlation was 0.62.

                                                                                       GDP rank vs. simulated performance rank
                                                                                              (rank correlation = 0.56)
                                                             0        CONCACAF
                                                                      UEFA                                     Argentina
                                                                      AFC
                                                                      CAF                                                               Morocco
                                                                      CONMEBOL                                             Portugal
                                                                      OFC
                                                             10
                                                                                                                                                  Croatia
                     Simulated performance rank (1 = best)




                                                                                                                                                                 Senegal
                                                                                                                                                       Uruguay
                                                             20

                                                                                      Australia
                                                                                    Canada
                                                                                              South Korea
                                                             30
                                                                         Scotland


                                                                                                     Saudi Arabia

                                                             40


                                                                                                                                  New Zealand

                                                             50
                                                                  0                  10                      20                30                     40                   50
                                                                                                            GDP rank (1 = richest)


Figure 3: GDP rank versus simulated performance rank, 48 World Cup 2026 teams, by confedera-
tion.


5.2   Sensitivity to (κ, σ)
As in the AFCON study, κ and σ are not calibrated, since a single cross-section cannot identify
dynamic parameters. The same limitation arose in [1, Section 6.1.1], where calibration from a four-
edition AFCON panel was abandoned rather than reported as a potentially spurious point estimate.
We check robustness over the same grid, κ ∈ {0.3, 0.5, 0.7, 1.0, 1.5}, σ ∈ {0.10, 0.20, 0.30, 0.40, 0.50}
(Monte Carlo, N = 8,000 paths per cell). The rank correlation stays in a narrow band, [0.560, 0.578],
across all 25 combinations (Figure 4) – comparable to, if slightly wider than, the AFCON result
([0.605, 0.643] under the same recomputation).
Across the parameter grid, the five highest-ranked teams take only two closely related configu-
rations: {Argentina, Brazil, England, France, Spain} or {Argentina, England, France, Morocco,
Spain}. The five lowest-ranked teams are similarly stable, with the two configurations differing
only by Cabo Verde and Ghana.
At the baseline parameters, Morocco, Senegal, Croatia, Uruguay, and Portugal are the five largest
over -performers relative to GDP rank. Conversely, Scotland, Saudi Arabia, Canada, New Zealand,
and South Korea exhibit the largest under -performance.

                                                                                                                     7
The central empirical pattern persists from the 24-team AFCON sample to the 48-team global
field: GDP matters, while the conditional performance residual has a stronger marginal effect.
This result is robust to the choice of the unidentified structural parameters κ and σ.

                             Rank correlation (GDP vs. simulated performance)
                               across ( , ): baseline =0.7, =0.3 marked
                                                                                0.5775
                       0.3     0.565     0.569     0.568       0.578   0.570

                                                                                0.5750

                       0.5     0.568     0.570     0.560       0.563   0.561
                                                                                0.5725




                                                                                     rank correlation
                                                                                0.5700
                       0.7     0.567     0.570     0.568       0.567   0.562

                                                                                0.5675
                       1.0     0.568     0.569     0.566       0.578   0.564
                                                                                0.5650

                       1.5     0.570     0.569     0.563       0.560   0.564    0.5625

                               0.10      0.20      0.30        0.40    0.50



Figure 4: Rank correlation between GDP and simulated performance across a 5 × 5 grid of (κ, σ),
48 World Cup 2026 teams; baseline marked with a star.



6     Discussion
6.1   What generalizes from Africa to the world
Three results from [1] replicate at global scale. First, GDP and population alone leave the majority
of cross-country variation in footballing strength unexplained (R2 = 0.33 here vs. 0.35 in the 24-
country AFCON regression) – essentially the same order of magnitude, now confirmed on a sample
twice the size and drawn from every confederation, not just one.
In both cases, roughly two-thirds of the residual’s cross-country variance mechanically reflects the
underlying performance measure (Section 4.2). Thus, this consistency indicates stability in the
model’s fit rather than independent evidence of an efficiency channel.
Second, Morocco and Senegal emerge as leading over-performers in both studies. This provides
out-of-sample corroboration, as the World Cup analysis uses a distinct comparison set of 46 non-
African teams and an independent tournament outcome.
Third, the GDP-rank/performance-rank correlation is positive but firmly below 1 in both settings
(0.562 here, 0.62 in Africa), and in both cases this finding is robust to the choice of the model’s
un-identified dynamic parameters over a wide grid.

6.2   What is new here
The World Cup exercise also surfaces a finding the single-confederation AFCON study could not:
the sharp contrast between a single-tournament outcome and an aggregated ranking as the per-
formance measure Yi . With R2 = 0.09, World Cup outcomes are only weakly explained by GDP


                                                           8
and population, while the tied scoring of 40 mid-table exits induces a strong mechanical resid-
ual–outcome correlation (0.954; Section 4.2). By contrast, FIFA points, aggregated over several
years and many matches, are substantially more explained by economic fundamentals (R2 = 0.33),
reinforcing the GDP/conditional-performance distinction.
This is a clean illustration, with real data, of the model’s own distinction between the systematic
term θi,t f (Xi,t ) and the idiosyncratic shock εi,t : single knockout tournaments are dominated by
the latter, long-run rankings by the former.
This finding cautions against interpreting any single tournament, African or global, as a clean mea-
sure of genuine efficiency. It reinforces the need for a multi-edition panel to calibrate κ and ,σ and
to identify the conditional performance residual using richer controls and a properly specified SFA
decomposition.

6.3   Remarks
As in [1]: this is a single cross-section, not a panel, so zi is a snapshot (“footballing strength
relative to GDP and population, as of the concluded World Cup 2026”), not a fully identified
structural efficiency parameter in the SFA sense (Section 2), and κ, γ, c, σ are shared across all 48
teams by necessity, with the z̄i = zi identification assumption flagged explicitly in Section 5. The
England/Scotland UK-proxy issue (Section 3) mechanically penalizes Scotland’s residual and should
not be read as a substantive claim about Scottish football governance. Finally, the actual-result
regression’s low R2 should not be read as “GDP does not matter for World Cup performance”.
This reflects the small-sample nature of a single knockout tournament. The FIFA-points regression,
based on the same 48 teams and covariates and jointly significant at p < 0.001, nevertheless
reproduces the GDP/conditional-performance split observed in Africa.


7     Conclusion
Applying the framework of [1] unchanged to the 48-team 2026 FIFA World Cup confirms its cen-
tral finding at the global level: economic resources determine potential, while a sizeable GDP-
independent component drives performance above or below it. Following the related paper’s revised
methodology, we interpret this component as a conditional residual, noting its mechanically strong
correlation with the underlying performance measure (Corr = 0.82) and its absorption of unmod-
eled factors. Morocco and Senegal are over-performers both within Africa and globally; several of
the world’s richest football economies under-perform their potential, with robust statistical sup-
port for the joint explanatory role of GDP and population (p < 0.001) despite individually modest
elasticities.


References
[1] Thierno Thioune and Babacar Mbaye Ndiaye. Economic resources, sporting efficiency and
    uncertainty: a stochastic optimization model of football performance in africa. 2026. URL
    https://arxiv.org/abs/2610.06967.

[2] Dennis Aigner, C. A. Knox Lovell, and Peter Schmidt. Formulation and estimation of stochastic
    frontier production function models. Journal of Econometrics, 6(1):21–37, 1977.

[3] Abraham Charnes, William W. Cooper, and Edwardo Rhodes. Measuring the efficiency of
    decision making units. European Journal of Operational Research, 2(6):429–444, 1978.


                                                  9

```
