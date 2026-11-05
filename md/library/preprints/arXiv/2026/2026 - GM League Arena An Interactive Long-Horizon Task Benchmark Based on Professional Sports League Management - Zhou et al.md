<!-- source: library/preprints/arXiv/2026/2026 - GM League Arena An Interactive Long-Horizon Task Benchmark Based on Professional Sports League Management - Zhou et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.05147 -->
<!-- authors: Junkai Zhou, Ziming Pan, Zhaoyi Zhang -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-05; equations, tables and figures are NOT preserved - consult the PDF for those -->

# GM League Arena: An Interactive Long-Horizon Task Benchmark Based on Professional Sports League Management

                                            GM League Arena: An Interactive Long-Horizon Task Benchmark
                                            Based on Professional Sports League Management
                                            Junkai Zhou, Ziming Pan, Zhaoyi Zhang
                                            Long-horizon decision-making under sustained competition requires large language models (LLMs) to balance
                                            immediate investment with future resource needs. However, local success in multi-step interactions can not
                                            adequately capture cumulative decision effects or demonstrate long-term goal achievement under resource
                                            constraints and sustained competition. To address this gap, we introduce GM Bench, a benchmark for managing
                                            professional sports teams across seasons under resource constraints and competition among teams. We build the
                                            environment simulators for four sports and add financial constraints, player demands, and market mechanisms
                                            to establish a unified task across sports. Diverse rosters of comparable strength are constructed from real-
arXiv:2611.05147v1 [cs.CL] 3 Nov 2026




                                            world player data, and each LLM is evaluated as a team general manager to assess its long-term management
                                            capabilities. We evaluate competitive performance, cash reserves, and cross-season improvement across four
                                            sports. Over five NBA seasons, Claude Opus 5.5 ranks first among 29 LLMs, while GPT-6 Astra and GPT-6.1
                                            Sol combine strong performance with larger cash reserves.




                                        1 Introduction
                                        In complex environments, large language models need to understand rules, take actions, and revise decisions using
                                        feedback. Recent benchmarks span scientific tasks [3, 10], web interaction [4, 13], and long-horizon games [11, 15].
                                        In long-horizon competition, participant interactions shape resource values and action opportunities, and strategies
                                        and demands evolve with the environment; models must balance current investment, future resources, and subsequent
                                        choices. Evaluating this ability requires evolving environments that link interactions and resource dynamics to cumulative
                                        decision outcomes.
                                        Sports management provides a concrete setting for studying this process, making it possible to track how the model
                                        coordinates current inputs with future returns through a series of decisions: trades and costly signings can strengthen a
                                        team in the current season while depleting future assets and limiting roster flexibility. These effects unfold as seasons
                                        progress, while rivals continue to improve their rosters, prompting further resource reallocation. We therefore formulate
                                        team management across seasons as a long-horizon evaluation task, tracing how interactive decisions shape competitive
                                        performance and resources over time to test whether models can turn local interactions into sustainable long-term
                                        management outcomes.
                                        We introduce GM Bench, which models team management across seasons with two components: interactive subjects
                                        and the simulation environment. The interactive subjects comprise LLM general managers (GMs), players and agents;
                                        only LLMs serving as GMs are evaluated. GMs draft, sign, and trade players using visible information while competing
                                        for market resources. Players and agents share a general LLM with a fixed configuration to express demands and
                                        negotiate. The environment uses the National Basketball Association (NBA) as its primary setting and comprises three
                                        modules: League Rules, Player & Team Analysis, and Competition Simulation. A built-in engine simulates games and
                                        enforces rules, while financial constraints and market signals shape management decisions.
                                        We extend a unified task linking GMs, players, institutional rules, and information channels to hockey, baseball, and
                                        American football to assess long-term management under different rules and resources. Real-world player ratings are
                                        used to construct five roster types: balanced, single-star, dual-star, offensive, and defensive. Evaluation uses uniform
                                        information conditions and comparable initial strength while preserving differences in star configurations and offensive
                                        or defensive emphasis. The proposed metrics report competitive performance across seasons, terminal cash, and seasonal
                                        trajectories, while action logs are analyzed to assess execution reliability and resource costs.
                                        Experiments across four sports reveal substantial differences in the long-term management capabilities of LLMs. The six
                                        leading NBA models remain among the top seven in each additional sport. In the NBA evaluation, for example, Claude
                                        Opus 5.5 ranks first and wins three championships over five seasons; GPT-6 Astra and GPT-6.1 Sol combine sustained


                                                                                                    1
       Performance
                             Champions
              Trade                                                         Champions                                                                                                                        Rebuild
                                                Management                                                                                   Win-Now            Aggressive Build        Steady Build
             Addition                                                                             Rigid
                                                 Overload Shortened                              Tactics
                                                           Rotation
                                                                                                                 Champions                                                                             Champions
                                                                                                                                              System       Champions
                                                                                                                                              Stability
                                Failed          Veteran
                             Adjustments        Signing                                    Unbalanced                                                                                                                      Rebuild
            Increased                                                                       Rotation                     Key Player                                                 Strong Offense
           Investment                                                                                                      Injured                                                     & Defense
                                                                              Poor                                                                                                                                          Steady
                                                                         Collaboration                                                   Substitute                                                                          Build
                                                                                                               Defensive                Unsuitability               Veteran
                                                     Refined                                                   Upgrade                                    Strategy  Absence                                  Finals Loss
                                                     Rotation                                                                                           Improvement                               Rotation
                                 Defensive                                    Workouts                                     Offensive
               Intensive           Drills                                                                                  Struggles                                                      Key     Upgrade
                Training                                                                                                                                                               Substitute          Resources
                                                                                                                                                                                                            Run-out
                                                                                             Tactical                                                                  Fatigue                                         Aggressive
                                                                                           Adjustments                                                                                          Fitness                  Build
                                                                                                                                                                                              Maintenance

                                                                                                                 Roster                                   Veteran
                                                                                                                                        Rotation          Decline
                                                           Rookie            Specialized          Coaching      Overhaul                Tweaks                                                                             Win-Now
           Stockpile                NBA Draft             Breakout            Training             Change                    Core
          Draft Picks                                                                                                      Extension                                                                      Missed
                                                                                                                                                                                                          Playoffs            Time
       Regular Season      Playoffs Offseason    Regular Season      Playoffs Offseason    Regular Season     Playoffs   Offseason     Regular Season       Playoffs    Offseason   Regular Season     Playoffs   Offseason

                  Season 1                                   Season 2                                      Season 3                                Season 4                                      Season 5


Figure 1 Illustrative performance trajectories of four team management strategies over five seasons show that early competitive gains
can diminish, whereas rebuilding and sustained investment can yield delayed benefits.


gains with larger cash reserves. Grok 4.7 achieves stronger competitive returns with less remaining cash, whereas
Kimi K3 combines steady improvement with a larger financial buffer. MiMo-V2.6-Pro retains substantial cash despite
declining performance. Sonnet faces unaffordable renewals after an NBA championship run. These cases highlight the
need to coordinate acquisition, retention, and financing for sustained long-term performance. Our contributions are
threefold:

      • We introduce GM Bench across four sports, combining multiple role competition and interactions to evaluate
        long-horizon resource allocation by LLMs.
      • We develop a protocol jointly reporting competitive performance, terminal resources, and seasonal trajectories,
        with five roster types of comparable strength from real-world player data for strategy comparisons.
      • We evaluate cross-season management and cross-sport generalization through action logs, and trading diagnostics,
        analyzing feedback use and long-term decision effects.

2 Task Definition

2.1    Roles and Management Objectives
Each evaluated LLM serves as a team GM, managing players and assets through selection, trades, and contract renewals.
Players share a general LLM for interactions, while the environment handles match simulation and player rotation.
The objective is to improve competitive performance across seasons by balancing current roster investment with future
resource needs under resource constraints. We model the task as a partially observable stochastic game:
                                                                                         G = (I, S, A, P, O, U, H),                                                                                                                  (1)
where I is the team set, S comprises roster, contract, financial, and market states, and A is the joint GM action space.
P governs state transitions, O determines information visibility, U represents management outcomes, and H is the
decision horizon across seasons.

2.2    State Dynamics and Outcomes

Each GM observes team state, player demands, and public market information through oit . Model mi for team i
conditions its actions on this observation and available history hit , while the environment advances under joint action at :
                                                                       ait ∼ πmi (· | oit , hit ),                    st+1 ∼ P (· | st , at ).                                                                                       (2)
Changes caused by actions persist and enter subsequent observations according to disclosure rules. The task combines
repeated decisions, state dependencies across phases, and delayed feedback. Outcome vector Ui reports competitive
performance, resource status, and long-term improvement, capturing cumulative returns and their resource costs.


                                                                                                                 2
                      Interactive Subjects of the NBA Simulator                                Shared NBA Environment               Multiple
           General Managers                      Player Agents & Players                                                           Scenarios
                                                                                                    League Rules
                                                      Communicate                                   Salary Cap & Matching
                                                        Demands
                                                                                                    Luxury Tax & Settlement
                                                       General LLM



             Generative LLMs                          Social Media                                 Player & Team Analysis
                                                      Public Rumors                                Player Training Statistics
          Management Action                           Rookie Player Updates                        Team Performance Data

              Draft             Free
                               Agency                 Club State & Options                         Competition Simulation
                                                      Rosters & Capital                            Match-Day Procedures
             Trade             Renewal                Ability & Availability                       Season Schedule                   ……

                                                                 Evaluation System

                 Competitive Performance                   Resources & Finances                               Long-term Improvement
                 Wins / Losses · Elo · Ranking             Funds · Contracts · Future Assets                  Win-Rate Gain · Seasonal Trends




Figure 2 Overview of GM Bench, illustrated with the NBA environment and extended to hockey, baseball, and American football.
LLM general managers interact with players and their agents within a shared simulator that enforces league and financial rules, while
evaluation tracks competitive performance, resources and finances, and cross-season improvement.


3 NBA Environment
The NBA instance draws inspiration from ZenGM1 , and models a NBA environment with league rules, LLM-based
management, financial constraints, and role interactions.

3.1   League Foundations
Player Data and State. Initial rosters are constructed from real NBA player data based on player ratings. Growth and
aging change ratings, while injuries affect availability and on-court performance. Game outcomes depend on player
condition, roster composition, and random events, allowing the effects of roster adjustments to emerge throughout the
season.


Core Rules and Financial Settings. The environment implements the following rules and financial mechanisms: (1)
Game and season rules, which define game procedures and regular-season and playoff schedules; (2) Salary cap,
which restricts payroll allocation and player acquisition; (3) Luxury tax, which imposes additional costs when payroll
exceeds the tax threshold; (4) Financial condition, which updates cash balances using revenue, operating expenses, and
luxury tax, with balances carried forward throughout the seasons.

3.2   Market Interactions and GM Actions
Player Demands and Market Signals. All players share an LLM that expresses trade demands based on team
performance, playing roles, and contract status. Player representatives generate trade requests and public rumors. GMs
combine these signals with roster needs to assess player value, conduct negotiation, and make offers.


Management Actions and Execution. GMs receive information on players, finances, and league rules and can
perform four types of management actions: (1) Drafting, selecting rookie players; (2) Signing, signing free players;
(3) Trading, negotiating and revising offers involving players and draft picks with other GMs; (4) Contract renewal,
negotiating salaries with players after each season.
   1 https://github.com/zengm-games/zengm




                                                                       3
4 General Sports Management
Differences in drafting, transfers, and registration across sports are implemented through the corresponding rules and
game, while role interactions, intertemporal resource dependencies, and delayed feedback form a unified evaluation
structure, as shown in Figure 2. GM Bench extends the NBA task to hockey, baseball, and American football to assess
long-term management under different rules and roster needs.

4.1   Evaluation Target: General Manager
Each evaluated LLM serves as a team GM, allocating resources based on rosters, contracts, future assets, and market
signals to improve competitive performance across seasons. Sports management follows a common feedback loop that
links these decisions over time: GM actions change team states, shaping competitive and market outcomes that inform
subsequent decisions. Within this loop, roster changes affect current strength, future payroll flexibility, and tradable
assets, requiring GMs to coordinate immediate personnel decisions with long-term resource commitments.

4.2   Environment Roles: Players and Agents
Players and agents are both non-player characters (NPCs) rather than evaluation targets. They provide interaction
partners and market signals by expressing individual demands and communicating trade opportunities, respectively.


Players: Expressing Personal Demands. All players share a general LLM with a fixed configuration. Based on
individual circumstances, they express preferences over competitive prospects, playing roles, and compensation and
participate in renewal negotiations. These preferences inform GM negotiation and resource allocation, while the
simulator handles player development, injuries, and game performance.


Agents: Trade Requests and Public Rumors. Agents generate trade requests and public rumors for rostered players
according to disclosure rules, turning individual circumstances into market signals. Private requests may remain
undisclosed, while public rumors indicate potential trading opportunities. GMs weigh these signals against player
condition, contract obligations, and roster needs when deciding whether to act.

4.3   System Environment
The system validates actions, advances games, and scores outcomes. Stochastic simulation and built-in management
policies update league states and provide feedback for subsequent GM decisions.


League and Teams. The league checks contract renewals and financial compliance. Teams negotiate through LLMs,
and agreements are validated before execution. Under the predefined season format, regular-season records determine
standings and playoff eligibility, while playoffs decide the champion. At season end, the system settles revenue and
expenses, opens drafting, signing, and renewal windows, and carries roster, contract, and financial states into the next
season.


Coaches and Game Engine. Coaches and the game engine handle in-game decisions, translating roster configurations
into outcomes shaped by roster, player, and randomness. GMs use this feedback to assess roster adjustments.


Media and Market Information. The system controls the timing and visibility of player demands, public rumors,
and media reports, while journalists and social media disseminate information. Draft windows provide prospect names,
positions, ratings, and values, helping GMs identify market opportunities and assess roster fit.

5 Data Sources and Evaluation
We construct teams with comparable initial strength but distinct management needs from real-world player data to
compare model strategies. Evaluation tracks competitive performance, resource retention, and long-term improvement,


                                                           4
           Balanced               Star                 Twins                    Offense               Defense        All Styles Overlay
                SC                   SC                   SC                         SC                   SC                   SC
      DC                   DC                    DC                        DC                    DC                    DC


                      BL                  BL                      BL                      BL                    BL                  BL


      OI                   OI                    OI                        OI                    OI                    OI
                DI                   DI                   DI                         DI                   DI                   DI




Figure 3 Schematic profiles of the five team types. Balanced emphasizes an evenly distributed roster; Star centers on one standout
player; Twins features two leading players; Offense prioritizes offensive ability; and Defense emphasizes defensive ability. The axes
represent roster balance (BL), single-star contrast (SC), dual-core advantage (DC), offensive index (OI), and defensive index (DI).
Larger radial values indicate stronger emphasis on the corresponding characteristic. The final panel overlays all five profiles for
comparison.


capturing cumulative decision returns and future investment capacity.

5.1        Player Data and Team Initialization
For each of the four sports, we construct five roster types from real-world player data based on ratings, as shown in
Figure 3, with comparable initial strength but distinct needs for bench depth, support for core players, and offensive
or defensive improvement: (1) Balanced, with relatively even strength across starters and reserves; (2) Star, centered
on one standout star with weaker supporting players; (3) Twins, led by two core players; (4) Offense, emphasizing
shooting; (5) Defense, emphasizing defensive ability.

5.2        Evaluation Metrics
We report competitive performance, resource and financial status, and long-term improvement across four sports to
characterize management returns and resource costs.


Competitive Performance. A common Elo protocol [5] measures relative competitive performance within each
                                                (0)
league. All N teams start each of T seasons at Ri,s = R0 = 1500, with no rating carryover. Games are processed
                            (g)
chronologically, with Ri,s denoting the rating of team i after rated league game g in season s. For teams i and j, the
pre-game expected score is
                                                                 1
                                           pi,s,g =          (g−1)  (g−1)
                                                                             ,                                      (3)
                                                           (Rj,s −Ri,s )/400
                                                    1 + 10
with pj,s,g = 1 − pi,s,g . Both ratings are updated from the same pre-game values:
                                                 (g)      (g−1)                      
                                               Rk,s = Rk,s        + K yk,s,g − pk,s,g ,                                                  (4)

for k ∈ {i, j}. The observed score yk,s,g is 1 for a win, 0 for a loss, and 0.5 for a draw where permitted. We fix
K = 20 for all teams and games; nonparticipants retain their ratings. Updates reward unexpected wins more strongly
                                  PN     (g)
and preserve the league-wide total i=1 Ri,s = N R0 .
With Ms rated games in season s, we report mean season-end Elo:
                                                                                     T
                                                         (M )                     1X
                                               Ei,s = Ri,s s ,             Ei =         Ei,s .                                           (5)
                                                                                  T s=1

Higher E i indicates stronger performance. We also report cumulative regular-season wins, losses, draws where
applicable, and seasonal rank.




                                                                       5
Resources and Finances. Terminal cash Ci is the available balance after revenue and expenses are settled at the
end of the management horizon, reflecting capacity for subsequent investment. Cash and competitive records jointly
reveal the trade-off between resource retention and competitive returns. Active contracts and future assets can provide
additional context on team resources.


Long-Term Improvement. Seasonal win-rate and cash track management performance. We define improvement as
the difference between mean win rates in the final and initial w seasons:
                                                       T                     w
                                                 1     X                 1 X
                                          Gi =                  vi,s −         vi,s ,                                    (6)
                                                 w                       w s=1
                                                     s=T −w+1

where vi,s = Wi,s /(Wi,s + Li,s ) is the regular-season win rate excluding draws, and w is prespecified (2w ≤ T ).
Positive and negative Gi indicate improvement and decline, respectively. Together with E i , records, and terminal
resources, Gi characterizes long-term management outcomes.

6 Experiments

6.1   Experimental Settings
Models and Configuration. The evaluation comprises 31 LLMs from 12 families: OpenAI (7), Anthropic (4), Gemini,
DeepSeek, and Qwen (3 each), Grok, GLM, MiMo, and Doubao (2 each), and Kimi, MiniMax, and HY (1 each); the
details are shown in Appendix B. The experiments span five seasons (2022-2026). We use official APIs with high
reasoning effort where supported; more details are shown in Appendix C.


Baseline. We design Native GM as a rule-based management baseline: (1) Player valuation: players are valued using
ability, age, potential, contracts, and injuries; (2) Strategy selection: team results and roster composition guide strategy
selection, contention prioritizes current strength, while rebuilding favors young players, draft picks, and inexpensive
contracts; (3) Contract management: signings prioritize high-value free agents under salary constraints; renewals
consider contract costs and player willingness.

6.2   Overall Results and Model Comparisons
Overall Competitive Performance. In NBA setting, initially comparable teams show substantial divergence across
seasons, as shown in Table 1. Elo ranges from 1071.0 to 1977.3, with Claude Opus 5.5 ranking first and winning
three championships, followed by GPT-6 Astra and GPT-6.1 Sol. Opus, Astra, and Sonnet collectively win all five
championships. Regular-season wins span 35 to 47 in the first season and 8 to 76 in the final season, this widening
spread captures the cumulative effects of management over time.


Native Policy as a Strategic Reference. The native policy ranks 14th in the NBA setting, with regular-season wins
rising from 39 to 49. Thirteen LLMs rank above it and 16 below, including Gemini 3.8 Flash, GPT-5.6 Terra, and
DeepSeek-V4.1-Flash. These results highlight room for improvement in the long-term management capabilities of many
current LLMs.


Strategic Capacity Across Model Generations. Long-term management performance varies substantially across
model generations, as shown in Table 1. Within families, GPT-6 Astra and GPT-6.1 Sol outperform GPT-4o, DeepSeek-
V4-Pro exceeds DeepSeek-R1. Differences also emerge across tiers within the same generation, with Qwen3.8-Max
exceeding Qwen3.8-Flash. However, older models can outperform newer releases both within and across families:
GPT-4o exceeds Hy4 Preview and MiMo-V2.6-Flash, while Gemini 3.1 Pro Preview outperforms Gemini 3.8 Flash.

6.3   Resource Allocation Across Seasons
Star Acquisition and Competitive Returns. Trading observations and terminal cash balances reveal contrasting
investment styles, as shown in Table 1: Claude 5 GMs actively trade for championship contention, whereas GPT-6 GMs


                                                             6
Rank        Model              Elo Wins Losses Cash                Rank          Model             22 23 24 25 26 Gi
 1 Claude Opus 5.5            1977.3    446    66    312.48         1 Claude Opus 5.5              44 54 65 74 76 +31.71
 2 GPT-6 Astra                1907.7    427    89    1006.62        2 GPT-6 Astra                  45 50 61 69 73 +28.66
 3 GPT-6.1 Sol                1838.7    400   101    1152.33        3 GPT-6.1 Sol                  45 49 60 67 71 +26.83
 4 Claude Sonnet 5.5          1813.3    385    98    308.05         4 Claude Sonnet 5.5            43 54 75 65 56 +14.63
 5 Claude Fable 5.1           1794.4    377   106     419.07        5 Claude Fable 5.1             38 49 64 67 66 +28.05
 6 Grok 4.7                   1784.3    347   121     585.74        6 Grok 4.7                     36 46 50 59 63 +24.39
 7 Gemini 3.1 Pro Preview     1753.1    334   131     -21.63        7 Gemini 3.1 Pro Preview       42 51 64 57 46 +6.10
 8 Grok 4.6                   1713.6    316   150     443.52        8 Grok 4.6                     38 46 49 55 57 +17.07
 9 Kimi K3                    1698.8    308   130     868.23        9 Kimi K3                      42 46 55 58 62 +19.51
10 DeepSeek-V4-Pro            1666.3    275   161     255.43       10 DeepSeek-V4-Pro              36 44 46 53 56 +17.68
11 GLM-5.3                    1652.6    279   161     188.42       11 GLM-5.3                      47 52 53 54 57 +7.32
12 Qwen3.8-Max                1602.5    250   189     292.10       12 Qwen3.8-Max                  41 42 48 48 52 +10.37
13 GPT-6 Luna                 1582.6    249   190     -41.43       13 GPT-6 Luna                   37 48 54 46 38 −0.61
14 Native GM strategy         1575.0    240   196     96.78        14 Native GM strategy           39 44 46 48 49 +8.54
15 Gemini 3.8 Flash           1525.7    220   217     111.40       15 Gemini 3.8 Flash             40 40 41 42 43 +3.05
16 GPT-5.6 Terra              1499.0    196   232     527.42       16 GPT-5.6 Terra                44 38 38 38 38 −3.66
17 MiniMax M3                 1451.8    193   226     106.26       17 MiniMax M3                   39 38 38 38 41 +1.22
18 DeepSeek-V4.1-Flash        1418.4    178   232     294.00       18 DeepSeek-V4.1-Flash          47 38 37 36 38 −6.71
19 Qwen3.8-Flash              1388.5    154   256     428.19       19 Qwen3.8-Flash                37 35 34 32 32 −4.88
20 Qwen3.8-27B                1361.6    154   256     460.73       20 Qwen3.8-27B                  35 33 32 32 32 −2.44
21 Doubao-Seed-2.1-Pro        1331.0    133   277     335.05       21 Doubao-Seed-2.1-Pro          35 32 27 27 27 −7.93
22 GLM-5.3-Flash              1305.8    117   293     581.30       22 GLM-5.3-Flash                40 36 25 24 27 −15.24
23 MiMo-V2.6-Pro              1275.4    105   305     925.41       23 MiMo-V2.6-Pro                40 37 23 22 22 −20.12
24 Gemini 3.5 Flash-Lite      1255.2    106   304      65.99       24 Gemini 3.5 Flash-Lite        42 34 22 24 23 −17.68
25 GPT-4o                     1206.4     91   319     360.08       25 GPT-4o                       46 35 29 23 19 −23.78
26 DeepSeek-R1                1167.2     81   329     167.76       26 DeepSeek-R1                  39 32 18 19 17 −21.34
27 Claude Haiku 4.5           1150.6     61   349     244.02       27 Claude Haiku 4.5             41 32 18 14 15 −26.83
28 Hy4 preview                1124.7     53   357      81.31       28 HY4 Preview                  46 32 18 13 12 −32.32
29 MiMo-V2.6-Flash            1107.2     51   359     -40.19       29 MiMo-V2.6-Flash              43 31 22 14 8 −31.71
30 Doubao-Seed-2.1-Turbo      1071.0     42   368     354.07       30 Doubao-Seed-2.1-Turbo        43 32 18 12 14 −29.88

Table 1 NBA results on GM Bench. Each       denotes one champi- Table 2 NBA regular-season wins and long-term improvement.
onship. Best values are bold and highlighted; second-best values Rank follows Table 1. Gi is the change in average win rate
are underlined. Negative cash is highlighted in red.             from 2022–2023 to 2025–2026 (w = 2), expressed in percentage
                                                                 points.


favor cautious acquisitions. Opus acquires stars and wins three championships, while Astra and Sol preserve larger cash
buffers for future roster adjustments. Grok 4.7 achieves stronger competitive returns with less remaining cash, whereas
Kimi K3 combines sustained improvement with greater financial flexibility. These comparisons highlight competitive
returns and future investment capacity as joint criteria for assessing star acquisitions.


Championship Peaks and Roster Continuity. Peak success and sustained improvement can diverge, as shown
in Table 2. Sonnet wins a championship and peaks at 75 regular-season wins in 2024 before falling to 65 and 56.
Sol improves steadily from 45 to 71, achieving a larger Gi . Fable records 67 and 66 wins in the final two seasons
and achieving Gi = 28.05 percentage points without a championship. Renewal observations show that Sonnet faces
unaffordable salary demands and loses valuable players, highlighting the need to coordinate acquisition and retention.


Financial Feedback and Investment Capacity. Cash balances complement competitive results as a measure of
investment capacity. Astra and Sol retain 1006.62 and 1152.33, respectively, compared with 312.48 for Opus. MiMo-
V2.6-Pro retains 925.41 in cash but ranks 23rd, with regular-season wins falling from 40 to 22, showing high balances
may coexist with weak competitive returns. Cash deficits occur at different competitive levels: Gemini 3.1 Pro Preview
(rank 7, −21.63), GPT-6 Luna (rank 13, −41.43), and MiMo-V2.6-Flash (rank 29, −40.19). These management cases



                                                               7
            (a) American football                             (b) Ice hockey                                  (c) Baseball
Rank             Model              Elo Cash      Rank         Model              Elo Cash      Rank         Model              Elo Cash
       1 Claude Opus 5.5          1870.1 228.19      1 Claude Opus 5.5          1855.4 63.10       1 GPT-6 Astra              1895.5 203.05
       2 Claude Sonnet 5.5        1761.6 78.00       2 GPT-6.1 Sol              1824.0 59.27       2 Claude Opus 5.5          1860.4 -33.64
       3 GPT-6.1 Sol              1760.0 205.34      3 Claude Sonnet 5.5        1768.8 40.08       3 GPT-6.1 Sol              1780.0 149.24
       4 Kimi K3                  1750.0 86.48       4 Gemini 3.1 Pro Preview   1754.7 138.45      4 Qwen3.8-Max              1776.2 386.26
       5 GPT-6 Astra              1745.0 163.94      5 GPT-6 Astra              1750.0 0.18        5 Claude Sonnet 5.5        1769.4 527.73
       6 Claude Fable 5.1         1736.3 236.92      6 Claude Fable 5.1         1747.8 116.69      6 Grok 4.7                 1747.2 447.90
       7 Grok 4.7                 1733.0 422.70      7 Grok 4.7                 1739.5 44.86       7 Claude Fable 5.1         1737.1 32.27
       8 Gemini 3.1 Pro Preview   1714.4 210.74      8 Kimi K3                  1665.4 267.86      8 Native GM strategy       1727.0 406.52
       9 DeepSeek-V4-Pro          1714.3 117.67      9 Grok 4.6                 1617.6 320.32      9 Gemini 3.1 Pro Preview   1719.6 373.27
      10 GLM-5.3                  1700.0 233.54     10 DeepSeek-V4-Pro          1591.9 176.44     10 GPT-6 Luna               1707.3 323.11
      11 Grok 4.6                 1663.8 215.06     11 Native GM strategy       1572.7 -18.21     11 Grok 4.6                 1695.1 287.21
      12 GPT-6 Luna               1644.4 178.54     12 Qwen3.8-Max              1569.3 49.08      12 GLM-5.3                  1666.9 264.28
      13 Gemini 3.8 Flash         1630.4 191.05     13 Qwen3.8-Flash            1557.6 116.02     13 DeepSeek-V4-Pro          1623.5 242.39
      14 Qwen3.8-Max              1559.7 271.95     14 Gemini 3.8 Flash         1545.9 6.45       14 Kimi K3                  1616.6 357.41
      15 GPT-5.6 Terra            1547.8 102.12     15 GPT-5.4 Mini             1544.4 10.93      15 MiniMax M3               1540.1 -41.12
      16 DeepSeek-V4.1-Flash      1518.7 93.57      16 GPT-5.6 Terra            1429.3 -43.07     16 Doubao-Seed-2.1-Pro      1505.6 -686.43
      17 MiniMax M3               1468.9 -67.53     17 DeepSeek-V4.1-Flash      1415.2 6.97       17 GLM-5.3-Flash            1476.3 42.31
      18 Qwen3.8-Flash            1401.8 161.60     18 GLM-5.3                  1391.0 75.21      18 Qwen3.8-27B              1441.3 151.91
      19 Native GM strategy       1386.1 262.38     19 Qwen3.8-27B              1390.2 217.59     19 GPT-5.6 Terra            1441.1 43.03
      20 MiMo-V2.6-Pro            1385.0 74.50      20 MiniMax M3               1380.2 -58.10     20 MiMo-V2.6-Pro            1380.5 -609.77
      21 Qwen3.8-27B              1365.1 391.39     21 GPT-5.4 Nano             1347.0 69.68      21 Gemini 3.8 Flash         1378.0 -14.77
      22 GPT-5.4 Mini             1352.7 196.24     22 GPT-6 Luna               1333.0 51.33      22 DeepSeek-V4.1-Flash      1350.9 21.55
      23 Gemini 3.5 Flash-Lite    1320.5 123.38     23 GLM-5.3-Flash            1317.6 204.81     23 Gemini 3.5 Flash-Lite    1346.8 -39.27
      24 Doubao-Seed-2.1-Pro      1315.4 37.75      24 Doubao-Seed-2.1-Pro      1290.5 -39.41     24 Qwen3.8-Flash            1302.4 106.73
      25 GLM-5.3-Flash            1310.2 248.22     25 GPT-4o                   1251.1 17.16      25 Claude Haiku 4.5         1263.8 172.99
      26 DeepSeek-R1              1258.2 173.47     26 MiMo-V2.6-Pro            1237.3 -10.39     26 GPT-4o                   1256.5 60.17
      27 MiMo-V2.6-Flash          1245.0 42.79      27 Claude Haiku 4.5         1235.6 321.47     27 DeepSeek-R1              1237.9 165.93
      28 GPT-5.4 Nano             1220.8 211.02     28 DeepSeek-R1              1191.0 80.67      28 Hy4 preview              1216.5 206.73
      29 Hy4 preview              1210.6 126.84     29 Doubao-Seed-2.1-Turbo    1186.8 119.83     29 Doubao-Seed-2.1-Turbo    1146.9 -22.45
      30 GPT-4o                   1193.3 210.78     30 Hy4 preview              1166.3 -11.50     30 MiMo-V2.6-Flash          1084.9 53.63
      31 Doubao-Seed-2.1-Turbo    1163.5 169.85     31 MiMo-V2.6-Flash          1157.1 -5.79
      32 Claude Haiku 4.5         1105.3 221.24     32 Gemini 3.5 Flash-Lite    1118.8 -36.56


Table 3 Elo rankings and terminal cash in (a) American football, (b) ice hockey, and (c) baseball. The highest value in each column
and sport is bold and highlighted; the second-highest is underlined. Negative cash is highlighted in red. The native GM strategy is
boxed.


illustrate linked financial pressures: salary commitments tie up future revenue, while weak results reduce revenue and
constrain reinvestment.

6.4      Results Across Additional Sports
American Football. Claude Opus 5.5 leads American football, matching its first-place NBA result, while Kimi K3
ranks fourth compared with ninth in the NBA, as shown in Table 2. The six highest-ranked NBA models remain in the
top seven in all three additional sports, showing consistent competitive strength across settings. The native GM strategy
ranks 19th, below its NBA placement of 14th. Grok 4.7 combines seventh place with the highest terminal cash, showing
that competitive leadership and cash retention remain distinct across settings.


Ice Hockey. Opus again leads ice hockey, followed by GPT-6.1 Sol, preserving their strong NBA standings. Financial
outcomes transfer less uniformly: Astra, one of the two NBA cash leaders, ranks fifth but retains only 0.18, whereas
Haiku holds the largest balance despite ranking 27th. The native GM strategy ranks 11th, above its NBA and American
football placements, but finishes with negative cash. Across evaluated teams, terminal deficits occur in 8 of 32 hockey
teams and 7 of 30 baseball teams, compared with 1 of 32 in American football and 3 of 30 in the NBA. These results
show that stronger competitive performance can coexist with financial strain.



                                                                      8
Baseball. GPT-6 Astra leads baseball, compared with second in the NBA and fifth in both American football and ice
hockey. Qwen3.8-Max and Kimi K3 reverse their relative positions: Qwen ranks 14th in American football and fourth
in baseball, while Kimi ranks fourth and 14th, respectively. Opus, which leads the other three sports, ranks second
but ends with negative cash. Its aggressive investment leads to bankruptcy late in the evaluation, followed by player
departures and a series of losses. Sonnet combines fifth place with the highest cash balance, further illustrating how
financial rankings shift across sports. The native GM strategy ranks eighth. Together, these experiments assess how
LLMs adapt resource allocation across sports to sustain competitive performance and future investment capacity.

7 Related Work
Interactive Evaluation. Interactive benchmarks evaluate sequential actions and coordination in executable envi-
ronments [9, 20]. WebArena, AppWorld, and TheAgentCompany cover web, application, and workplace work-
flows [14, 16, 19], while BrowserGym unifies web-agent evaluation [4]. τ 2 -bench tests agent–user collaboration in a
shared environment [2], and BALROG evaluates planning and exploration across games [11].


Long-Term Management and Competition. Recent benchmarks examine the long-term effects of management
decisions. Vending-Bench, EcoGym, and EnterpriseArena evaluate sustained business operation and resource allo-
cation [1, 7, 8]. Market-Bench, Vending-Bench Arena, and CoffeeBench study procurement, pricing, and trading in
multi-agent markets [12, 18]. E-Commerce Bench grounds year-long operations in real product and supplier data,
linking repeated supplier negotiations, cash-flow management, and long-term returns [6].


Sports Management. Sports management links player development, contract constraints, and performance across
seasons. FM-Bench combines long-term management, model competition, and equal-budget drafting in a synthetic
football world [15]. FromPitch2Board uses paired seeds and controlled configurations to examine models, agent
scaffolds, management roles, and evaluation horizons [17]. GM Bench evaluates cross-season resource allocation under
competition across four sports, using real player data, roster types of comparable strength, and a shared LLM for player
demands and negotiation.

8 Conclusion
We introduced GM Bench, an interactive benchmark for long-horizon sports management. A shared task across four
sports connects competition among LLM general managers, player interactions, and persistent resource constraints
to outcomes across seasons. Experiments reveal distinct balances between championship pursuit, financial flexibility,
and roster continuity. Renewal trajectories link competitive success to subsequent retention demands, highlighting
anticipation of future commitments as a key element of sustained improvement. By jointly tracking competitive
performance, cash reserves, and seasonal trajectories, GM Bench makes cumulative decision effects observable and
evaluates the ability to sustain progress under competition.

Limitations
League Configuration. Each sport is instantiated through a specified simulator and league configuration. The unified
task structure supports evaluation across four sports, while contract systems, roster constraints, financial rules, and
competition formats remain specific to each implementation. Extending the benchmark to other leagues requires
corresponding rule and interface adaptations.


Observation Horizon. Decisions are assessed over a finite number of seasons, capturing cumulative competitive
and financial effects within the evaluation window. Full player careers and distant future assets may extend beyond
this horizon. Longer evaluations would help characterize delayed player development, aging, and the outcomes of
commitments that mature after the evaluation ends.


Evaluation Cost. Multi-season evaluation with interacting LLM roles requires repeated inference and simulation.
Expanding coverage to additional models, random seeds, and league configurations increases computational cost and


                                                           9
evaluation time. More efficient execution and parallelization of independent runs could facilitate broader experimental
coverage.

Ethical Considerations
GM Bench uses real-player data to initialize simulated states. Player demands, negotiations, and market rumors are
generated as fictional scenario content and do not represent the actual views, intentions, or conduct of the individuals
portrayed. We interpret these interactions within their simulated roles and restrict evaluation conclusions to model
behavior. All management actions are executed within the simulator, and benchmark outputs are not intended to guide
real-world recruitment, contract negotiations, or financial decisions.
We comply with applicable source licenses and attribution requirements when reusing data and software. We document
the provenance and intended use of datasets, prompts, and trajectories, and exclude private personal information and
confidential content from shared materials. Our paper distinguishes source player attributes from generated interactions,
avoiding the presentation of synthetic statements as factual reports about real individuals.

References
 [1] Axel Backlund and Lukas Petersson. 2025. Vending-bench: A benchmark for long-term coherence of autonomous agents. arXiv
     preprint arXiv:2502.15840.
 [2] Victor Barres, Honghua Dong, Soham Ray, Xujie Si, and Karthik Narasimhan. 2025. τ 2 -bench: Evaluating conversational
     agents in a dual-control environment. Preprint, arXiv:2506.07982.
 [3] Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi Liao, Chen Wei, Zitong Lu, et al.
     2025. Scienceagentbench: Toward rigorous assessment of language agents for data-driven scientific discovery. In International
     Conference on Learning Representations, volume 2025, pages 96934–96990.
 [4] De Chezelles, Thibault Le Sellier, Sahar Omidi Shayegan, Lawrence Keunho Jang, Xing Han Lù, Ori Yoran, Dehan Kong,
     Frank F Xu, Siva Reddy, Quentin Cappart, et al. 2024. The browsergym ecosystem for web agent research. arXiv preprint
     arXiv:2412.05467.
 [5] Arpad E Elo. 1978. The rating of chessplayers, past and present. (No Title).
 [6] Wei Fan, Xinjie Shen, Xudong Guo, Jianhong Tu, Yang Su, Yinger Zhang, Lianghao Deng, Fengyu Wang, Baohua Dong,
     Yangqiu Song, et al. 2026. E-commerce bench: Evaluating llm agents on long-horizon autonomous business operation. arXiv
     preprint arXiv:2608.30730.
 [7] Yi Han, Yan Wang, Lingfei Qian, Haohang Li, Yupeng Cao, Yueru He, Xueqing Peng, Nanhan Shen, Yitao Xu, Yankai Chen,
     et al. 2026. Can llm agents be cfos? benchmarking long-horizon resource allocation in an uncertain enterprise environment.
     arXiv preprint arXiv:2603.23638.
 [8] Xavier Hu, Jinxiang Xia, Shengze Xu, Kangqi Song, Yishuo Yuan, Guibin Zhang, JinCheng Ren, Boyu Feng, Li Lu, Tieyong
     Zeng, et al. 2026. Ecogym: Evaluating llms for long-horizon plan-and-execute in interactive economies. arXiv preprint
     arXiv:2602.09514.
 [9] Chang Ma, Junlei Zhang, Zhihao Zhu, Cheng Yang, Yujiu Yang, Yaohui Jin, Zhenzhong Lan, Lingpeng Kong, and Junxian He.
     2024. Agentboard: An analytical evaluation board of multi-turn llm agents. Advances in neural information processing systems,
     37:74325–74362.
[10] Bodhisattwa Prasad Majumder, Harshit Surana, Dhruv Agarwal, Bhavana Dalvi Mishra, Abhijeetsingh Meena, Aryan Prakhar,
     Tirth Vora, Tushar Khot, Ashish Sabharwal, and Peter Clark. 2025. Discoverybench: Towards data-driven discovery with large
     language models. In International Conference on Learning Representations, volume 2025, pages 4556–4579.
[11] Davide Paglieri, Bartłomiej Cupiał, Samuel Coward, Ulyana Piterbarg, Maciej Wołczyk, Akbir Khan, Eduardo Pignatelli,
     Łukasz Kuciński, Lerrel Pinto, Rob Fergus, et al. 2025. Balrog: Benchmarking agentic llm and vlm reasoning on games. In
     International Conference on Learning Representations, volume 2025, pages 96666–96702.
[12] Issa Sugiura, Daichi Hattori, Kazuo Araragi, Keita Ogawa, Shota Onose, Taro Makino, Teppei Usuki, and Takashi Ishida.
     2026. Coffeebench: Benchmarking long-horizon llm agents in heterogeneous multi-agent economies. arXiv preprint
     arXiv:2606.16613.
[13] Megh Thakkar, Nicolas Chapados, Christopher Pal, et al. 2025. Webarena verified: Reliable evaluation for web agents. In
     Workshop on Scaling Environments for Agents.
[14] Harsh Trivedi, Tushar Khot, Mareike Hartmann, Ruskin Manku, Vinty Dong, Edward Li, Shashank Gupta, Ashish Sabharwal,
     and Niranjan Balasubramanian. 2024. Appworld: A controllable world of apps and people for benchmarking interactive coding
     agents. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
     pages 16022–16076.


                                                               10
[15] Tianyou Wang, Chongyang Gao, Kezhen Chen, Dong Chen, Yinghao He, Donghan Li, Wangcheng Xu, Hongjiu Zhang, and Chi
     Li. 2026. Fm-bench: A benchmark for long-horizon management with competing agents. arXiv preprint arXiv:2608.18423.
[16] Frank Fangzheng Xu, Yufan Song, Boxuan Li, Yuxuan Tang, Kritanjali Jain, Mengxue Bao, Zora Wang, Xuhui Zhou, Zhitong
     Guo, Murong Cao, et al. 2026. Theagentcompany: benchmarking llm agents on consequential real world tasks. Advances in
     Neural Information Processing Systems, 38.
[17] Peiyu Zang. 2026. Frompitch2board: Benchmarking llm agents in long-horizon football management. arXiv preprint
     arXiv:2609.34710.
[18] Yushuo Zheng, Huiyu Duan, Zicheng Zhang, Yucheng Zhu, Xiongkuo Min, and Guangtao Zhai. 2026. Market-bench:
     Benchmarking large language models on economic and trade competition. In Proceedings of the 64th Annual Meeting of the
     Association for Computational Linguistics (Volume 1: Long Papers), pages 39893–39906.
[19] Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk,
     Daniel Fried, et al. 2024. Webarena: A realistic web environment for building autonomous agents. In International Conference
     on Learning Representations, volume 2024, pages 15585–15606.
[20] Kunlun Zhu, Hongyi Du, Zhaochen Hong, Xiaocheng Yang, Shuyi Guo, Daisy Zhe Wang, Zhenhailong Wang, Cheng Qian,
     Xiangru Tang, Heng Ji, et al. 2025. Multiagentbench: Evaluating the collaboration and competition of llm agents. In Proceedings
     of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 8580–8622.




                                                                11
A Benchmark Comparison
Table 4 compares representative benchmarks along four design dimensions: Demand negotiation incorporates demands
from LLM-driven personnel into resource allocation; Needs adaptation tests strategy adjustment across teams with
comparable initial strength but different configuration needs; Intertemporal diagnostics traces long-term action benefits
and subsequent resource constraints through controlled comparisons or state replay; Institutional adaptation evaluates
strategies across sports rules and resources within a unified management task. We also report the number of interacting
agent roles in each environment.

                                  Interacting agents                            Demand            Needs          Long-term      Institutional
Benchmark                                                                      negotiation      adaptation                       adaptation
                                  per environment                                                                diagnostics
EcoGym [8]                        1 management agent                                ×                ×               △                ×
EnterpriseArena [7]               1 CFO agent                                       ×                ×               △                ×
FM-Bench Arena [15]               16 managers (15 LLM + 1 scripted)                 ×                ×               ✓                ×
Market-Bench [18]                 20 LLM retailers                                  ×                ×               ×                ×
CoffeeBench [12]                  6 LLM firms (1 evaluated + 5 reference)           ×                ×               △                ×
E-Commerce Bench [6]              1 manager + up to 576 supplier NPCs               ×                ×               ×                ×
GM Bench                          30 GMs + NNPC NPCs (NBA)                          ✓                ✓               ✓                ✓

                            Table 4 Interaction scales and evaluation designs of representative benchmarks.
Notes. ✓: explicit support; △: related comparisons of memory, frameworks, or incentives; ×: no documented support under the stated definitions.
Counts include management agents and negotiation NPCs, excluding evaluators and simulated consumer demand. E-Commerce Bench provides a
pool of 576 supplier NPCs with rule-based economic decisions and LLM-rendered dialogue; each episode may contact only a subset. NNPC counts
player and agent NPCs in the NBA instance of GM Bench.



B Model List
The model list comprises 31 distinct models, with 29 shared across all four sports. Basketball and baseball each use
these 29 models plus one scripted baseline, yielding 30 participants to match the number of teams in the National
Basketball Association (NBA) and Major League Baseball (MLB), respectively. American football and ice hockey
additionally include GPT-5.4 Mini and GPT-5.4 Nano, yielding 31 models plus the scripted baseline, or 32 participants,
to match the number of teams in the National Football League (NFL) and National Hockey League (NHL), respectively.
The details are shown in Table 5.

Group                           Model identifiers

OpenAI                          GPT-6 Astra; GPT-6.1 Sol; GPT-6 Luna; GPT-5.6 Terra; GPT-4o; GPT-5.4 Mini; GPT-5.4 Nano.
Anthropic                       Claude Opus 5.5; Claude Sonnet 5.5; Claude Fable 5.1; Claude Haiku 4.5.
Gemini                          Gemini 3.1 Pro Preview; Gemini 3.8 Flash; Gemini 3.5 Flash-Lite.
DeepSeek                        DeepSeek-V4-Pro; DeepSeek-V4.1-Flash; DeepSeek-R1.
Qwen                            Qwen3.8-Max; Qwen3.8-Flash; Qwen3.8-27B.
Grok                            Grok 4.7; Grok 4.6.
GLM                             GLM-5.3; GLM-5.3-Flash.
MiMo                            MiMo-V2.6-Pro; MiMo-V2.6-Flash.
Doubao                          Doubao-Seed-2.1-Pro; Doubao-Seed-2.1-Turbo.
Kimi                            Kimi K3.
MiniMax                         MiniMax M3.
HY4                             Hy4 preview.

Baseline                        Native GM strategy.

                                                Table 5 Models used across the four sports.




                                                                      12
C Reproducibility Details

C.1   Evaluation Scope and Language
The benchmark covers basketball, American football, ice hockey, and baseball. Section 5.1 describes five roster types
for each sport: Balanced, Star, Twins, Offense, and Defense. All model interactions use English text. Table 1 reports
30 NBA entries, comprising 29 LLM deployments and one scripted baseline. Table 3 reports 32 entries for American
football, 32 for ice hockey, and 30 for baseball, each including the scripted baseline. These counts describe the reported
model-policy entries. Random-seed repetitions are reported separately below.

C.2   Inference and Experimental Selection
All evaluated models are accessed through their official APIs. Configurable reasoning effort is set to high for every
model that supports this setting. The total API expenditure for the experiments is approximately USD 15,000, as reported
in Section 6.1. The local Python interpreter is version 3.9.6.

C.3   Runs and Result Aggregation
Each reported full-horizon model evaluation consists of one complete five-season run covering 2022–2026. Token
expenditure constrained the number of full-horizon repetitions. Multiple short-horizon tests with different random seeds
were used for cross-checking. The reported full-horizon results remain single-run measurements; short-horizon tests are
not counted as independent five-season replications.
Section 5.2 defines the aggregation used in the result tables. Elo is the arithmetic mean of season-end ratings over the
five seasons, with ratings initialized to 1500 at the start of each season and updated using K = 20 and a 400-point
logistic scale. Terminal cash is measured at the end of the evaluation horizon. Table 2 reports regular-season wins
by year and the difference in mean win rate between 2022-2023 and 2025-2026 (w = 2), expressed in percentage
points. The five seasons form a temporally dependent trajectory. The tables do not report confidence intervals across
independent full-horizon runs.




                                                           13
