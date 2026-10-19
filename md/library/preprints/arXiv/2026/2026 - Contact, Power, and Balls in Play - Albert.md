<!-- source: library/preprints/arXiv/2026/2026 - Contact, Power, and Balls in Play - Albert.pdf -->
<!-- arXiv:2610.21836 | https://arxiv.org/abs/2610.21836 | filed 2026-10-19 -->

# Contact, Power, and Balls in Play: A Three-Rate Decomposition of Batting Average and the Disappearance of the .400 Hitter

                                                                     Contact, Power, and Balls in Play:
                                                         A Three-Rate Decomposition of Batting Average
                                                               and the Disappearance of the .400 Hitter
                                                                                           Jim Albert
arXiv:2610.21836v1 [stat.AP] 15 Oct 2026




                                                          Department of Mathematics and Statistics, Bowling Green State University



                                                                                            Abstract

                                                Batting average factors exactly as BA = c {h + (1 − h) b}, where c is the rate of avoiding a
                                                strikeout, h is the home-run rate among non-strikeout at-bats, and b is batting average on balls
                                                in play (BABIP). The bracketed term is the rate f at which non-strikeout at-bats become hits,
                                                so the decomposition nests the two-factor identity BA = cf . Using the 256 major-league hitters
                                                with at least 300 at-bats in 2025, every season from 2004 to 2025, and 20,357 qualifying seasons
                                                from 1901 to 2019, we ask which rates behave like skills and how the corresponding abilities
                                                are related. Over 19 consecutive-season pairs the median year-to-year correlation is 0.86 for c,
                                                0.74 for h and 0.41 for b; batting average (0.44) is no more repeatable than BABIP. A trivariate
                                                logistic-normal random-effects model gives single-season reliabilities of 0.91, 0.76 and 0.30, and a
                                                talent correlation between contact and power of -0.67 (95% profile interval -0.75 to -0.57), while
                                                BABIP talent is only weakly related to either. Historically, the negative covariance between c
                                                and f , which was near zero in the dead-ball era, explains why batting averages have become
                                                less dispersed, and so why no one has hit .400 since 1941. That covariance runs almost entirely
                                                through home runs: removing the contact–power channel from the 2010s covariance recovers
                                                72% of the gap between modern and dead-ball dispersion in batting-average talent.

                                           Keywords: batting average; BABIP; empirical Bayes; multivariate random effects; reliability;
                                           shrinkage; .400 hitter


                                           1    Introduction
                                           Batting average is the oldest summary of hitting and one of the most studied quantities in sports
                                           statistics. It served as the running example in the empirical Bayes work of Efron and Morris (1975,
                                           1977), and Brown (2008) used it to compare empirical Bayes and Bayes predictors within a season.
                                           These analyses treat a hitter’s batting average as a single binomial proportion whose true value
                                           is estimated by shrinking the observed average toward a common mean (Morris, 1983). Batting
                                           average is notoriously unstable from season to season, and a large literature, popular and academic,
                                           attributes much of that instability to chance (Albert and Bennett, 2001).


                                                                                                 1
    Batting average is, however, a composite. An at-bat ends in a strikeout or it does not; a non-
strikeout at-bat is a home run or a ball in play; and a ball in play is a hit or an out. These three
events depend on the hitter in different ways. Avoiding strikeouts reflects pitch recognition and
bat-to-ball skill. Home runs need no help from the defense and depend mostly on how hard and
at what angle the ball is struck. Whether a ball in play falls for a hit depends also on fielders,
parks and chance. McCracken (2001) argued that pitchers have little control over hits on balls in
play, and the same reasoning underlies the use of batting average on balls in play (BABIP) as an
indicator of hitter luck (Tango et al., 2007).
    Several authors have used a partial version of this structure. Bickel (2004) wrote batting average
as the product of one minus the strikeout rate and the in-play average to explain why .400 has
become so hard to reach. Albert (2005) fitted beta-binomial random-effects models to several
hitting rates and found that strikeout and home-run rates are far more ability-driven than batting
average, and Albert (2016) showed that predicting component rates separately and recombining
them improves forecasts of aggregate measures. What has not been examined is the joint structure
of the components: how the underlying abilities are correlated once sampling noise is removed, and
how that correlation has changed over the history of the game.
    This paper writes batting average exactly as the product of three rates and asks three questions:
    1. Which rates behave like stable skills, and how much of each rate’s cross-sectional variation
      reflects ability rather than chance (Sections 4 and 5)?

    2. How are the three abilities related once chance is removed, and what does the dependence
      imply for estimating an individual hitter’s ability (Section 5)?

    3. Gould (1986, 1996) attributed the disappearance of the .400 hitter to a narrowing of the
      distribution of batting averages. Which components drove that narrowing (Section 6)?
The answers are that strikeout avoidance and home-run hitting are skills while BABIP is mostly
noise; that contact and power abilities are strongly negatively correlated; and that the emergence
of this contact–power trade-off, rather than a convergence of hitting talent, accounts for most of
the reduced dispersion of modern batting averages.


2     Data and the decomposition
2.1    The identity
For a hitter with AB at-bats, SO strikeouts, HR home runs and H hits, define

                        AB − SO                HR                   H − HR
                   c=           ,       h=           ,      b=                .                   (1)
                          AB                 AB − SO             AB − SO − HR

We call c the contact rate, h the home-run rate and b BABIP. Our b differs from the conventional
BABIP only in omitting sacrifice flies from the denominator. Because ch = HR/AB and c(1−h)b =



                                                  2
Table 1: Four 2025 hitters with similar batting averages and different combinations of contact rate c, home-
run rate h and BABIP b.

                Player              AB      H    SO        HR        BA       c      h         b
                Aaron Judge         541   179    160       53    0.331    0.704   0.139    0.384
                Miguel Andujar      321   102     49       10    0.318    0.847   0.037    0.351
                Jonathan Aranda     370   117    107       14    0.316    0.711   0.053    0.414
                Jacob Wilson        486   151     39       13    0.311    0.920   0.029   0.318


(H − HR)/AB,

                     H                                                  H
              BA =      = c {h + (1 − h) b} = c f,              f=           = h + (1 − h) b,           (2)
                     AB                                              AB − SO

exactly, for every hitter and season. The finishing rate f is the proportion of non-strikeout at-
bats that become hits. Writing BA = cf gives the coarser two-factor view used by Bickel (2004);
splitting f into h and b separates the part of finishing that the defense cannot affect from the part
it can. Among the 2025 hitters the identity holds to within 1e-16; 3 of them hit no home runs.
    As an illustration, Aaron Judge had 541 at-bats in 2025 and struck out 160 times, so c =
381/541 = 0.704. Of the 381 non-strikeout at-bats, 53 were home runs (h = 0.139), and 126 of the
remaining 328 balls in play fell for hits (b = 0.384). His 179 hits in 541 at-bats give BA = 0.331.

2.2    Samples
All data come from the Lahman database (Friendly et al., 2026), analyzed in R (R Core Team,
2024). Stints with different teams in a season are combined. The main sample consists of the 256
hitters with at least 300 at-bats in 2025. For repeatability we use every season from 2004 to 2025
with the same threshold. For the historical analysis we use the 20,357 American, National and
Federal League player-seasons from 1901 to 2019 with at least 300 at-bats and a recorded strikeout
total; the Negro Leagues, recently added to the database, are excluded because their strikeout
records are incomplete. Seasons are grouped by decade.


3     The cross-section in 2025
3.1    Equal averages, different compositions
Table 1 shows four 2025 hitters whose averages fall between .311 and .331. Judge and Jacob Wilson
reached similar averages by opposite routes: Judge with a low contact rate, a home-run rate nearly
five times Wilson’s and a high BABIP; Wilson with the second-highest contact rate among qualifiers
and little power. Jonathan Aranda had the highest home-run rate, and Miguel Andujar the highest
BABIP, among the other hitters within twenty points of Judge’s average.
    Figure 1 shows the pairwise relationships among the three rates for all 256 hitters. Contact and
home-run rates are strongly negatively correlated (r = −0.53, 95% interval -0.61 to -0.43). BABIP


                                                       3
          Contact rate vs home-run rate                  Contact rate vs BABIP                      Home-run rate vs BABIP
 0.15   r = -0.53                                r = -0.12                                    r = -0.09
                                          0.40                                        0.40



 0.10                                     0.35                                        0.35



                                          0.30                                        0.30
 0.05


                                          0.25                                        0.25

 0.00
         0.60       0.70   0.80   0.90            0.60       0.70       0.80   0.90          0.00         0.05    0.10       0.15


Figure 1: Pairwise relationships among contact rate c, home-run rate h and BABIP b for the 256 hitters
with at least 300 at-bats in 2025. Lines are least-squares fits; r is the Pearson correlation.


is only weakly related to contact (r = −0.12) and to home-run rate (r = −0.09). At the two-factor
level the correlation between c and f is -0.40 (-0.50 to -0.29). The familiar observation that hitters
who rarely strike out do less damage when they make contact is therefore, in 2025, primarily a
statement about home runs.

3.2      A variance decomposition
Taking logarithms of (2) gives log BA = log c + log f , so the cross-sectional variance decomposes
exactly as
                            Var(log BA) = Var(log c) + Var(log f ) + 2 Cov(log c, log f ).                                   (3)

In 2025 the three terms are 0.0072, 0.0095 and -0.0066, summing to 0.0102. The two factors
contribute comparable variance, but because they are negatively correlated the observed dispersion
of batting average is 39% smaller than it would be if c and f varied independently (0.0167). This
covariance term is the quantity that drives the historical argument of Section 6.
   Because f is a sum rather than a product, Var(log f ) cannot be split exactly. Linearizing about
the means h̄, b̄ and f¯,

                               1n        2                 2
                                                                                                o
                Var(log f ) ≈ ¯2 (1 − b̄) Var(h) + (1 − h̄) Var(b) + 2(1 − b̄)(1 − h̄) Cov(h, b) .                           (4)
                              f

In 2025 the three terms are 0.0029, 0.0080 and -0.0008, shares of 29%, 80% and -8%; their sum
is within 5.2% of the exact Var(log f ). On observed rates, then, BABIP accounts for most of the
variation in finishing. Much of that variation is sampling noise, however. Subtracting the average
binomial variance p(1 − p)/n from each observed variance removes 66% of the variance of b but
only 21% of that of h, after which the home-run and BABIP terms account for 55% and 65% of
the total. Once chance is removed, power and BABIP contribute about equally to differences in


                                                                    4
                               Contact rate                            Home-run rate                            BABIP
                                                     0.15
                    r = 0.82                                r = 0.73                                 r = 0.28

            0.90
                                                                                              0.35
                                                     0.10
2025 rate




            0.80
                                                                                              0.30

            0.70                                     0.05


                                                                                              0.25
            0.60
                                                     0.00
                    0.60     0.70     0.80    0.90      0.00       0.05         0.10   0.15              0.26   0.30    0.34   0.38
                                                                        2024 rate

Figure 2: 2024 and 2025 rates for the 176 hitters with at least 300 at-bats in both seasons. The dashed
line is y = x.


finishing ability.


4             Which rates are skills?
A rate that measures ability should be repeatable. For each pair of consecutive seasons from 2004
to 2025 we correlate each rate across the hitters who qualified in both seasons. The 2020 season, in
which almost no one reached 300 at-bats, drops out, leaving 19 pairs with a median of 183 hitters
each.
            Figure 2 shows the 2024–2025 pair (176 hitters). Contact and home-run rates repeat closely
(r = 0.82 and 0.73); BABIP barely does (r = 0.28). Figure 3 shows that the pattern holds in every
pair. The year-to-year correlation ranges from 0.81 to 0.88 for c (median 0.86), from 0.66 to 0.80
for h (median 0.74), and from 0.24 to 0.52 for b (median 0.41). For batting average it ranges from
0.30 to 0.53 (median 0.44): the composite is no more repeatable than its noisiest component.


5             A trivariate random-effects model
5.1                Model and estimation
Repeatability uses two seasons. A random-effects model extracts the same information from a
single season and also estimates how the three abilities are related. Because the three outcomes
are nested, each can be modeled as binomial conditional on the one before it. For hitter i,

                           ABi − SOi ∼ Bin(ABi , ci ),                                        logit(ci ) = µc + ui ,
                                    HRi ∼ Bin(ABi − SOi , hi ),                               logit(hi ) = µh + vi ,           (5)
                           Hi − HRi ∼ Bin(ABi − SOi − HRi , bi ),                             logit(bi ) = µb + wi ,



                                                                        5
                                            1.0



                                            0.8



                 Year-to-year correlation   0.6



                                            0.4



                                            0.2



                                            0.0

                                                      Contact         Home-run         BABIP              Batting
                                                       rate             rate                              average


Figure 3: Year-to-year correlations for each of the 19 consecutive-season pairs from 2004 to 2025. Horizontal
bars mark the medians.

Table 2: Maximum likelihood estimates for model (5), 2025 season (logit scale). Wald intervals for the
means; profile-likelihood intervals for the standard deviations and correlations.

           Parameter                              Interpretation                               Estimate     95% interval
           µc                                     league contact rate (0.771)                     1.211     (1.164, 1.258)
           µh                                     league home-run rate (0.045)                   -3.059     (-3.128, -2.989)
           µb                                     league BABIP (0.299)                           -0.853     (-0.870, -0.835)
           σc                                     talent SD, contact                              0.369     (0.335, 0.407)
           σh                                     talent SD, home runs                            0.494     (0.439, 0.556)
           σb                                     talent SD, BABIP                                0.078     (0.053, 0.100)
           ρch                                    talent correlation, contact and home runs       -0.67     (-0.75, -0.57)
           ρcb                                    talent correlation, contact and BABIP           -0.22     (-0.45, 0.00)
           ρhb                                    talent correlation, home runs and BABIP         -0.23     (-0.48, 0.02)


with (ui , vi , wi )⊤ ∼ N3 (0, Σ) and Σ unstructured, with standard deviations σc , σh , σb and correla-
tions ρch , ρcb , ρhb . Given the abilities, the three binomial outcomes are conditionally independent
because they are determined by disjoint sets of at-bats. We fit (5) by maximum likelihood with the
Laplace approximation in lme4 (Bates et al., 2015), stacking the three outcomes and specifying an
unstructured covariance for the three random intercepts, and compute profile-likelihood intervals
for the variance components.
   Table 2 gives the estimates for 2025. The means correspond to league rates of 0.771 for contact,
0.045 for home runs and 0.299 for BABIP. On the logit scale the spread of talent is largest for home
runs (σh = 0.494), intermediate for contact (σc = 0.369), and small for BABIP (σb = 0.078).




                                                                                 6
5.2    Talent correlations
The estimated correlation between contact and home-run abilities is ρ̂ch = −0.67, noticeably
stronger than the raw correlation of -0.53. Sampling noise inflates the variance of each observed
rate without changing their covariance, so observed correlations are attenuated toward zero (Spear-
man, 1904); the model removes that attenuation. Covariances between observed rates need no such
correction, because the three rates are computed from disjoint sets of at-bats and their sampling
errors are independent. BABIP ability is only weakly related to the other two abilities (ρ̂cb = −0.22,
ρ̂hb = −0.23), and neither interval clearly excludes zero.

5.3    Single-season reliability
By the delta method, the sampling variance of hitter i’s observed logit for a rate p based on n
trials is approximately τi2 = 1/{n p̂(1 − p̂)}; we add 12 to success and failure counts so that a season
with no home runs remains finite. The ratio wi = σ 2 /(σ 2 + τi2 ) is the fraction of between-hitter
variation in that rate that reflects ability, the reliability of classical test theory (Lord and Novick,
1968). Averaged over the 2025 hitters the reliability is 0.91 for contact, 0.76 for home runs and
0.30 for BABIP. The mean noise standard deviations are 0.114, 0.285 and 0.121: home-run rates
are noisier than BABIP in absolute terms, but their talent spread is more than six times larger.
These single-season reliabilities agree closely with the multi-season correlations of Section 4, as
they should, since reliability and test–retest correlation estimate the same quantity when ability is
stable.

5.4    Trivariate shrinkage
                                                                                2 , τ 2 , τ 2 ). Under
Let zi hold hitter i’s observed logits minus (µc , µh , µb ) and let Ti = diag(τi,c  i,h i,b
a normal approximation to the binomial likelihood on the logit scale, the posterior mean of his
abilities is
                                         θ̂i = Σ (Σ + Ti )−1 zi .                                   (6)

When Σ is diagonal, (6) reduces to shrinking each rate separately by its own reliability, the familiar
James–Stein form (Efron and Morris, 1975). When it is not, the off-diagonal terms let each observed
rate inform the estimates of the other abilities.
    Table 3 and Figure 4 show the conditional modes from the fitted model, which use the full bino-
mial likelihood. Contact and home-run rates barely move; the mean absolute adjustments are 0.005
and 0.005. BABIP moves much more (mean adjustment 0.018): Judge’s observed .384 becomes an
estimated ability of 0.308, close to the league mean of 0.299, and Aranda’s .414 becomes 0.326. The
correlations matter for individual hitters. Shrinking Judge’s BABIP by its own reliability alone
gives 0.325, whereas (6) gives 0.309, because his high home-run rate, through ρ̂hb < 0, points to a
lower BABIP ability. Averaged over hitters, the correlations shift the BABIP estimate by 0.004.




                                                    7
    Table 3: Observed 2025 rates and model estimates (conditional modes) for the four hitters of Table 1.

                                    Contact rate               Home-run rate            BABIP
             Player              observed       estimate   observed     estimate   observed   estimate
             Aaron Judge            0.704          0.694       0.139       0.118      0.384      0.308
             Miguel Andujar         0.847          0.833       0.037       0.032      0.351      0.305
             Jonathan Aranda        0.711          0.712       0.053       0.049      0.414      0.326
             Jacob Wilson           0.920          0.899       0.029       0.023      0.318     0.294



                                       Jonathan Aranda
                   0.40


                                                                                       Aaron Judge


                                    Miguel Andujar
                   0.35
           BABIP




                                 Jacob Wilson


                   0.30




                   0.25




                          0.00                   0.05                      0.10                      0.15
                                                        Home-run rate

Figure 4: Observed 2025 home-run rate and BABIP (gray) and model estimates (blue) for the 256 qualifiers.
Arrows run from observed to estimated; the four hitters of Table 1 are highlighted. The arrows are nearly
vertical: BABIP is shrunk strongly toward the league mean, home-run rate much less.


6      A historical perspective on the .400 hitter
6.1     Gould’s argument and the two-factor decomposition
Among American, National and Federal League hitters with at least 300 at-bats there have been
13 seasons of .400 or better since 1901, the last in 1941. Gould (1986, 1996) argued that .400
disappeared not because hitters became worse but because the distribution of batting averages
narrowed: as play improved and the talent pool deepened, the distance between ordinary and
exceptional hitters shrank, trimming both tails. The standard deviation of batting average among
qualifiers did fall, from 0.037 in the 1900s to 0.030 in the 1940s (about 19%), and has been nearly
constant since (0.029 in the 2010s; Figure 5a).
     Decomposition (3) shows where the narrowing came from. Table 4 reports its terms by decade,


                                                           8
          (a) SD of batting average                  (b) Talent variance                         (c) Correlation of c and f

                                                                                           0.0
 0.0350                                      0.009

                                                                                  log c
                                                                                          −0.2
 0.0325                                      0.006
                                                                                  log f

 0.0300                                                                                   −0.4
                                             0.003


 0.0275
          1900   1925   1950   1975   2000                   1950          2000              1900    1925   1950   1975   2000

                                                            Decade

Figure 5: Qualifying AL, NL and FL hitters by decade, 1900s–2010s. (a) Standard deviation of batting
average; ticks mark the 13 seasons of .400 or better. (b) Talent-scale variances of log c and log f (observed
variances minus average sampling variance). (c) Correlation between c and f , observed (dashed) and with
sampling noise removed (solid).


on the observed scale and, after subtracting the average delta-method sampling variance (1−p)/(np)
from Var(log c) and Var(log f ), on the talent scale. Sampling noise matters most for f , accounting
for 36% of the observed variance of log f in the 1900s and 51% in the 2010s. Three trends emerge
(Figure 5b,c).
   1. Strikeout avoidance did not homogenize. Its talent variance on the log scale grew by a factor
          of about 4.6 from the 1900s to the 2010s.

   2. The talent variance of finishing roughly halved (ratio 0.50), consistent with Gould’s picture
          of a converging talent pool.

   3. The two factors were essentially uncorrelated in the dead-ball era (talent correlation 0.09),
          while since the 1960s the observed correlation has stayed between -0.38 and -0.31 (talent
          correlation -0.53 in the 2010s).
    A counterfactual makes the role of the covariance precise. On the talent scale, the variance of
log BA fell from 0.0131 in the 1900s to 0.0059 in the 2010s. Combining the 2010s talent variances of
log c and log f with the 1900s covariance gives 0.0132, essentially the dead-ball level. The growth in
the spread of contact ability and the narrowing of finishing ability roughly offset, and the reduced
spread of modern batting averages is due almost entirely to the stronger negative covariance between
the two factors. Gould’s account is therefore incomplete: a .400 season requires excellence in both
c and f at once, and the modern game rarely produces that combination.

6.2        The trade-off runs through home runs
The three-rate decomposition identifies which part of finishing trades off against contact. Figure 6
and Table 5 show the correlations among c, h and b by decade. The correlation between contact
and home runs was close to zero in the 1900s (-0.04), when home runs were rare, fell to -0.40 in


                                                                9
Table 4: Decomposition (3) by decade for qualifying hitters. Columns 3–8 are observed quantities; the last
three remove binomial sampling noise from the variances of log c and log f and from their correlation.

                                                                                                Talent scale
  Decade        n SD(BA) Var(log c) Var(log f )            2Cov Var(log BA) r(c, f ) Var(log c) Var(log f ) r(c, f )
  1900s       1105     0.037      0.0018      0.0170    0.0007         0.0195    0.07      0.0015           0.0109     0.09
  1910s       1276     0.035      0.0017      0.0147   -0.0004         0.0160   -0.04      0.0014           0.0088    -0.06
  1920s       1241     0.035      0.0012      0.0132   -0.0009         0.0136   -0.11      0.0011           0.0081    -0.15
  1930s       1296     0.033      0.0018      0.0123   -0.0013         0.0128   -0.15      0.0016           0.0071    -0.20
  1940s       1211     0.030      0.0021      0.0107   -0.0010         0.0119   -0.10      0.0019           0.0050    -0.16
  1950s       1227     0.030      0.0027      0.0111   -0.0017         0.0121   -0.16      0.0024           0.0053    -0.23
  1960s       1581     0.029      0.0042      0.0121   -0.0044         0.0118   -0.32      0.0038           0.0062    -0.46
  1970s       2038     0.029      0.0040      0.0130   -0.0046         0.0124   -0.33      0.0037           0.0072    -0.45
  1980s       2114     0.028      0.0046      0.0110   -0.0044         0.0112   -0.31      0.0042           0.0052    -0.47
  1990s       2229     0.030      0.0050      0.0115   -0.0048         0.0116   -0.32      0.0045           0.0059    -0.47
  2000s       2545     0.028      0.0056      0.0105   -0.0057         0.0104   -0.38      0.0051           0.0051    -0.56
  2010s       2494     0.029      0.0077      0.0111   -0.0066         0.0122   -0.37      0.0071           0.0054   -0.53

Table 5: Correlations among the three rates by decade for qualifying hitters. h̄ is the mean home-run
rate. Columns headed r are observed correlations; “talent r” columns divide the observed covariance by
noise-corrected standard deviations. The last column is the home-run term’s share of approximation (4).

      Decade         n SD(BA)        h̄ r(c, f ) r(c, h) r(c, b) r(h, b) talent r(c, h) talent r(c, b) HR share
      1900s     1105      0.037   0.005     0.07   -0.04      0.08    0.35         -0.06             0.10          1%
      1920s     1241      0.035   0.014    -0.11   -0.40      0.01    0.30         -0.46             0.01         10%
      1940s     1211      0.030   0.020    -0.10   -0.45      0.10   -0.01         -0.51             0.16         18%
      1960s     1581      0.029   0.033    -0.32   -0.49     -0.09    0.05         -0.56            -0.15         24%
      1980s     2114      0.028   0.031    -0.31   -0.58     -0.03   -0.09         -0.66            -0.05         24%
      2000s     2545      0.028   0.042    -0.38   -0.54     -0.11    0.00         -0.62            -0.19         27%
      2010s     2494      0.029   0.045    -0.37   -0.58     -0.08   -0.09         -0.67            -0.13        25%



the 1920s as the home run entered the game, and reached -0.58 by the 2010s. The correlation
between contact and BABIP was small in every decade. Hitters who struck out more did not do
systematically better or worse on balls in play; they hit more home runs.
   Linearizing f makes the attribution explicit:

                               Cov(c, f ) ≈ (1 − b̄) Cov(c, h) + (1 − h̄) Cov(c, b).                                      (7)

The home-run term accounts for 76% of Cov(c, f ) in the 1960s and 80% in the 2010s, and for more
than all of it from the 1920s through the 1950s, when the BABIP term was slightly positive.

6.3    Home runs became part of finishing
Figure 7 applies approximation (4) by decade. In the 1900s the average qualifying hitter homered
in about one of every 200 non-strikeout at-bats (h̄ = 0.005), and home runs accounted for only
1% of the variation in finishing rates; finishing was essentially BABIP. By the 2010s the mean
home-run rate was about nine times higher (h̄ = 0.045), and home runs accounted for 25% of
that variation (40% once sampling noise is removed). Over the century the talent variance of h


                                                             10
      Correlation across qualifying hitters
                                              0.2




                                              0.0
                                                                                               Contact vs BABIP
                                                                                               Home runs vs BABIP
                                              -0.2



                                                                                               Contact vs finishing
                                              -0.4




                                              -0.6                                             Contact vs home runs

                                                     1920   1940   1960        1980   2000   2020
                                                                          Decade

Figure 6: Observed correlations among the three rates, and between contact and finishing (dashed), for
qualifying hitters in each decade, 1900s–2010s.


grew about 33-fold, while that of b fell to 0.64 of its 1900s level. Power became a second, growing
dimension along which hitters differ, and it is the dimension that trades off against contact.

6.4                     How much did the contact–power trade-off matter?
Equation (7) supports a narrower counterfactual than the one above: keep everything about the
2010s except the contact–home-run channel. Dividing (7) by c̄f¯ approximates Cov(log c, log f );
for the 2010s it gives -0.0033, matching the exact value of -0.0033. Setting the home-run term to
zero leaves -0.0007, and the talent-scale variance of log BA becomes 0.0112. That is 72% of the
way from the actual 2010s value (0.0059) to the value with dead-ball covariance (0.0132). Roughly
three-quarters of the reduced dispersion of modern batting-average talent is attributable to the
trade-off between avoiding strikeouts and hitting home runs.


7     Discussion
The identity BA = c{h + (1 − h)b} separates batting average into two components that behave
like skills and one that behaves largely like noise. Strikeout avoidance and home-run rate are
highly repeatable and highly reliable within a single season; BABIP is neither, and it is the main
reason batting average is so unstable. Because the identity is exact, the variance decompositions
and counterfactuals of Sections 3 and 6 require no modeling assumptions beyond the linearization
in (4) and (7), whose accuracy we check in the Appendix. The random-effects model adds esti-
mates of the talent correlations and a trivariate shrinkage estimator that lets each rate inform the



                                                                          11
     Spread in finishing rate   0.015



                                                                                    Total

                                0.010
                                                                                    BABIP




                                0.005


                                                                                    Home runs


                                0.000
                                                                                    Overlap
                                        1920   1940   1960            1980   2000    2020
                                                             Decade

Figure 7: Approximation (4) of Var(log f ) by decade: the home-run term, the BABIP term and the
covariance (overlap) term. The dashed line is the exact Var(log f ).


others, extending the component approach of Albert (2016) by modeling the dependence between
components.
   The historical analysis refines Gould’s explanation for the disappearance of the .400 hitter.
Batting averages did become less dispersed, but not because hitters became more alike: the spread
of contact ability grew substantially. What changed is that, beginning in the 1920s, the hitters
who make the most contact have tended to hit the fewest home runs. A modern .400 season would
require a hitter who rarely strikes out, hits for power, and enjoys a favorable season on balls in
play, a combination that has been rare since the home run became central to the game.
   Several limitations should be noted. First, BABIP reflects both contact quality and defense;
batted-ball tracking data could separate the two. Second, home-run rates depend on parks and on
the baseball itself, so part of what we call power is environmental. Third, at-bats exclude walks,
hit-by-pitches and sacrifices, so the rates describe the at-bat outcomes that enter batting average
rather than all plate appearances. Fourth, the 300-at-bat threshold selects hitters whose teams
kept playing them, which may truncate the lower tails of the rates. Fifth, the model is fit to one
season at a time; a model with player effects shared across seasons, or a fully Bayesian fit with
priors on Σ (Gelman and Hill, 2007), would give sharper estimates and full posterior uncertainty
for the correlations. Finally, the historical analysis establishes when the contact–power trade-off
emerged, not why. Changes in pitching, in hitters’ approaches, and in how teams value strikeouts
relative to power are all candidates.




                                                         12
Acknowledgments and use of AI tools
The analyses and this manuscript were produced in collaboration with Claude (Anthropic), a large
language model. The author posed the research questions, chose which directions to pursue, and
reviewed the results. Claude wrote the R code, carried out the computations, drafted the text, and
assembled the references. Claude is not listed as an author because it cannot take responsibility
for the work; the author takes full responsibility for the content, including any remaining errors. A
single R script reproduces every number, table and figure and is available from the author.


References
Albert, J. (2005). Does a baseball hitter’s batting average measure ability or luck? STATS: The
  Magazine for Students of Statistics, (44):3–6. Fall 2005/Winter 2006 issue.

Albert, J. (2016). Improved component predictions of batting and pitching measures. Journal of
  Quantitative Analysis in Sports, 12(2):73–85.

Albert, J. and Bennett, J. (2001). Curve Ball: Baseball, Statistics, and the Role of Chance in the
  Game. Copernicus Books, New York.

Bates, D., Mächler, M., Bolker, B., and Walker, S. (2015). Fitting linear mixed-effects models using
  lme4. Journal of Statistical Software, 67(1):1–48.

Bickel, J. E. (2004). Why it’s so hard to hit .400: New insights into an old statistic. The Baseball
  Research Journal, 32:15–21.

Brown, L. D. (2008). In-season prediction of batting averages: A field test of empirical Bayes and
  Bayes methodologies. The Annals of Applied Statistics, 2(1):113–152.

Efron, B. and Morris, C. (1975). Data analysis using Stein’s estimator and its generalizations.
  Journal of the American Statistical Association, 70(350):311–319.

Efron, B. and Morris, C. (1977). Stein’s paradox in statistics. Scientific American, 236(5):119–127.

Friendly, M., Dalzell, C., Monkman, M., and Murphy, D. (2026). Lahman: Sean ‘Lahman’ Baseball
  Database. R package version 14.0-0.

Gelman, A. and Hill, J. (2007). Data Analysis Using Regression and Multilevel/Hierarchical Models.
  Cambridge University Press, Cambridge.

Gould, S. J. (1986). Entropic homogeneity isn’t why no one hits .400 any more. Discover.

Gould, S. J. (1996). Full House: The Spread of Excellence from Plato to Darwin. Harmony Books,
  New York.



                                                  13
Lord, F. M. and Novick, M. R. (1968). Statistical Theories of Mental Test Scores. Addison-Wesley,
  Reading, MA.

McCracken, V. (2001). Pitching and defense: How much control do hurlers have?                 Baseball
  Prospectus. January 23, 2001.

Morris, C. N. (1983). Parametric empirical Bayes inference: Theory and applications. Journal of
  the American Statistical Association, 78(381):47–55.

R Core Team (2024). R: A Language and Environment for Statistical Computing. R Foundation
  for Statistical Computing, Vienna, Austria.

Spearman, C. (1904). The proof and measurement of association between two things. The American
  Journal of Psychology, 15(1):72–101.

Tango, T. M., Lichtman, M. G., and Dolphin, A. E. (2007). The Book: Playing the Percentages in
  Baseball. Potomac Books, Washington, DC.



A     Accuracy of the linear approximations
Approximation (4) replaces Var(log f ) by a first-order expansion of log{h + (1 − h)b} about (h̄, b̄).
In 2025 the approximation is within 5.2% of the exact value. Across the twelve decades from the
1900s to the 2010s the relative error has median 0.9% and maximum 2.4%. Approximation (7),
divided by c̄f¯, reproduces the exact 2010s value of Cov(log c, log f ) to four decimal places (-0.0033
versus -0.0033).
    Noise corrections subtract the average binomial sampling variance from each observed variance:
p(1 − p)/n on the rate scale, with n = AB for c, AB − SO for h and AB − SO − HR for b, and
(1 − p)/(np) on the log scale. Covariances are not corrected, because the three rates are computed
from disjoint sets of at-bats and their sampling errors are independent. “Talent” correlations in
Tables 4 and 5 divide the observed covariance by the noise-corrected standard deviations.




                                                  14
