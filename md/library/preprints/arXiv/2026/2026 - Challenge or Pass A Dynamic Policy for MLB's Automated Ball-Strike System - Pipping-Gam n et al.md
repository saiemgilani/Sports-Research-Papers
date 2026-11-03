<!-- source: 2026 - Challenge or Pass A Dynamic Policy for MLB's Automated Ball-Strike System - Pipping-Gam n et al.pdf -->
<!-- arXiv:2610.39452, 2026-10-29 · abstract from the arXiv API; PDF saved under library/ -->
<!-- arXiv roundup 2026-11-03 -->

# Challenge or Pass? A Dynamic Policy for MLB's Automated Ball-Strike System

**Jonathan Pipping-Gamón, Zach Sissman, Lila Dodson, Abraham J. Wyner**

arXiv:[2610.39452](https://arxiv.org/abs/2610.39452), submitted 2026-10-29.

## Abstract

Under Major League Baseball's automated ball-strike (ABS) challenge system, players must weigh the value of overturning a call against the risk of losing a challenge they may need later. We develop a policy that values an overturn through its effect on expected runs, accounting for the count, outs, and runners on base. Using pitch tracking and game records, we reconstruct challenge opportunities, including calls that players let stand. A Bayesian model represents players' imperfect impressions of pitch location and uses them to estimate overturn probabilities, with uncertainty calibrated from historical challenge decisions. Dynamic programming compares the expected gain with the future cost of losing a challenge, accounting for the stage of the game, the number of challenges remaining, and opportunities on both offense and defense. We develop the policy using games before the 2026 All-Star break and evaluate it without refitting on 983 games played afterward. Along the recorded sequence of opportunities, the policy recovers 0.536 modeled correction runs per game across both teams, compared with 0.452 under observed decisions, an improvement of 18.5%. The gain is 0.084 runs per game, with a 95% bootstrap interval of [0.065, 0.103]. The policy makes more challenges and recovers more value per successful review despite a lower overturn rate. These results show why overturn rate alone can be a misleading measure of challenge strategy.
