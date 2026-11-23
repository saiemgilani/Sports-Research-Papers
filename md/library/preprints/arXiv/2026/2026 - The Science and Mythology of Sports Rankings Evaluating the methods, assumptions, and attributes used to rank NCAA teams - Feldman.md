<!-- source: library/preprints/arXiv/2026/2026 - The Science and Mythology of Sports Rankings Evaluating the methods, assumptions, and attributes used to rank NCAA teams - Feldman.pdf -->
<!-- item: https://arxiv.org/abs/2611.27886 -->
<!-- authors: Lawrence Feldman -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-23; equations, tables and figures are NOT preserved - consult the PDF for those -->

# The Science and Mythology of Sports Rankings: Evaluating the methods, assumptions, and attributes used to rank NCAA teams

                                                              The Science and Mythology of Sports Rankings:
                                                         Evaluating the methods, assumptions, and attributes used to
                                                                            rank NCAA teams
                                                                                                   Lawrence Feldman†
                                                                                                 laf@laxnumbers.com

                                                                                                  Contributors:
arXiv:2611.27886v1 [stat.AP] 20 Nov 2026




                                                                 The Men’s Division I Lacrosse Selection Criteria and Ranking Committee (SCR),
                                                                                       formerly chaired by Lars Tiffany.‡


                                               Abstract: Selecting a sports-ranking system is not a purely mathematical decision. It also requires agreement about
                                               what the ranking should mean and what institutional purpose it should serve. This paper distinguishes four related
                                               but different tasks in sports ranking: prediction, retrospective evaluation, championship selection, and seeding;
                                               compares the governing philosophies of major ranking families; and identifies recurring errors in ranking debates. A
                                               descriptive comparison of nine NCAA Division I sport settings illustrates how schedule density, scoring environment,
                                               cross-conference connectivity, head-to-head meetings, and common-opponent availability vary from sport to sport.
                                               The central premise is that no ranking methodology is value-free. Every system reflects choices about evidence,
                                               competitive merit, and which tradeoffs are acceptable. The paper therefore offers a structured, multi-objective
                                               framework for evaluating ranking systems according to their intended purpose/goal rather than naming one universally
                                               superior method. Its principal contribution is to make the philosophical and institutional assumptions behind ranking
                                               decisions explicit, comparable, and testable.
                                               Keywords: Sports ranking; NCAA; seeding; predictive rankings; retrospective evaluation; NPI, RPI, NET, BCS.

                                               1.   Introduction: The purpose of rankings                                   ratings estimate the relative strength of all teams. A se-
                                                                                                                            lection committee adds human judgment and context. A
                                               Sports rankings do more than simply place teams in or-
                                                                                                                            hybrid system combines and weights multiple forms of
                                               der. They may, for instance, determine access to tourna-
                                                                                                                            evidence. Each approach reflects a different philosophy
                                               ments, influence seeding and scheduling, shape public
                                                                                                                            of competitive merit and creates tradeoffs among predic-
                                               perception, and limit access to institutional opportuni-
                                                                                                                            tive performance, deservingness, transparency, simplic-
                                               ties. However, debates about ranking systems often be-
                                                                                                                            ity, fairness, and public trust.
                                               gin with disagreement about results, rather than agree-
                                                                                                                               Consequently, the central question is not simply,
                                               ment about what the best system should accomplish.
                                                                                                                            "Which ranking is correct?" A more useful starting
                                                  No ranking methods are value-free. Resume-based
                                                                                                                            point is "What is this ranking supposed to mean and
                                               systems emphasize real-world wins and losses. Power
                                                                                                                            what decision is it intended to support?" A system
                                           †
                                             Lawrence Feldman served on the Coaches Committee for Division                  designed to predict future games may not be appropriate
                                             I men’s lacrosse for the past three years as an advisor. He founded            for determining which teams have earned championship
                                             Laxpower, a web site that rated lacrosse teams from 1997 to 2019               access. Similarly, a method suitable for selecting a
                                             and played lacrosse at the University of Pennsylvania. Before that,
                                             he earned his PhD in aerospace engineering and worked as an engi-
                                                                                                                            tournament field may not be the best for seeding it.1
                                             neer/computer analyst in the USAF, Lawrence Livermore Laboratory                  This paper provides a framework for discussing those
                                             (LLL), and Los Alamos National Laboratory (LANL).
                                           ‡                                                                            1
                                             Lars Tiffany was the former head lacrosse coach at the University of           A post on an NCAA webpage clarifies that the basketball selection
                                             Virginia, leading the team to national championships in ’19 and ‘21.           committee tends to use results-based (win/loss) methods more than
                                             He attended Brown University where he was team captain and later               predictive (power rating) methods for selection; still, they prefer
                                             served as head coach.                                                          predictive methods for seeding (McGuire, 2025; Analytics, 2016).


                                                                                                                    1
    distinctions. First, it separates prediction, retrospec-                        predict winners, scoring margins, or win probabilities.3
    tive evaluation, selection, and seeding as distinct de-                         Prediction therefore asks: Which team is most likely to
    cision tasks that require different standards of success.                       perform better in the rest of the season or post-season
    Second, it organizes twenty-five mathematical, institu-                         tournament?
    tional, and competitive qualities into a common frame-                            This is an important question, but not necessarily the
    work for evaluating ranking systems. Third, it com-                             same as asking which team has earned selection based
    pares major families of ranking methods according to                            on its performance during the season. A team may be
    the philosophies of merit they embody rather than treat-                        highly rated because it is, for some reason, expected to
    ing their numerical outputs as directly interchangeable.                        succeed in the future even though another similar team
    Fourth, it uses nine NCAA Division I sport settings to                          has compiled the more "deserving" body of work.
    show why differences in schedule density, scoring, and
    competitive-network connectivity make universal multi-                          2.2   Retrospective Evaluation
    sport assumptions problematic.                                                  Retrospective systems evaluate what teams have accom-
        The paper is not intended to defend a particular rank-                      plished in games already played and commonly consider
    ing system or identify one universally superior method.                         wins and losses, opponent quality, strength of sched-
    It is conceptual and descriptive: it proposes a framework                       ule, head-to-head results, and/or other evidence from a
    and testable research agenda, but it does not claim that                        team’s complete body of work. Unlike predictive sys-
    one method has been proved superior. The objective is                           tems, their primary purpose is not to forecast future per-
    to provide coaches, administrators, analysts, and gov-                          formance.
    erning bodies with a common vocabulary for evaluating                              Retrospective evaluation therefore asks: Which team
    whether a ranking system is appropriate for its intended                        has earned the stronger record of accomplishment? This
    purpose.                                                                        question is closely associated with the idea of the "most
                                                                                    deserving" team.
    2.    Ranking tasks: Prediction, retrospective                                     Deservingness is not self-evident: different systems
          evaluation, selection, and seeding                                        may emphasize total wins, schedule difficulty, head-to-
    Before debating formulas, stakeholders should identify                          head results, or other criteria and consequently reach
    the decision a ranking is intended to support. A method                         different conclusions.4
    can simultaneously be excellent for forecasting and a
    poor basis for championship selection; conversely, a                            2.3   Selection
    resume-based selector can accurately reflect past accom-                        Selection is about converting evidence about teams into
    plishment while offering little information about future                        decisions about which have earned access to the champi-
    performance. Separating tasks is one way to clarify nec-                        onship tournament bracket. This task often considers ret-
    essary tradeoffs.2                                                              rospective achievement, predictions about team strength,
                                                                                    scheduling or geographic fairness, victory in conference
    2.1    Prediction                                                               championships, or some combination of these objec-
    Predictive systems estimate how teams are likely to per-                        tives.5
    form in future games, and methods designed primarily
    for this purpose include power ratings, margin-based
    models, betting-market estimates, and, more recently,                       3
                                                                                  According to Barrow et al. (2013), among the most predictive rank-
    machine-learning models.                                                      ing methods are least squares (regression-based) and random-walker
       The performance of a predictive system can be evalu-                       methods, especially those "utilizing score-differential data."
                                                                                4
                                                                                  Coleman (2005) posits that "maximizing retrodictive accuracy" (ret-
    ated using future results, including how accurately they
                                                                                  rospective accuracy, in other words), "is equivalent to minimizing"
                                                                                  cases where "a past game’s winner is ranked behind its loser." This
                                                                                  definition of retrospective accuracy aligns with the common sense
2
    The computer is "only the little black box" that outputs rankings             and oft-repeated idea that "you have to value winning" (Irmer, 2024).
                                                                                5
    according to the set of principles and tradeoffs devised by a human.          Quotas like those previously used by Division II football or the Paris
    Rankings are the quantitative result of the particular tasks a method         2024 Olympics might be justifiable, depending on the sporting land-
    is designed to solve (Stern, 2006).                                           scape (NCAA, 2025; FIBA, 2024).


                                                                            2
       Selection therefore asks: Which teams should receive                  producing tournament seeding are related but often sub-
    access to the championship tournament and according                      tly distinct standards. Stakeholders who fail to identify
    to what definition of merit?                                             which standard to apply risk appearing to disagree on
       This is not merely a mathematical question. The gov-                  evidence despite actually asking different questions.
    erning organization must decide which evidence is rel-
    evant, how to balance competing considerations, and
                                                                             3. Stakeholder objectives and desired at-
    how to justify consequential decisions to teams that are
                                                                                tributes
    included or excluded from the tournament.

    2.4   Seeding                                                            Ranking systems should not be judged solely by, as they
                                                                             often are, whether they produce a preferred ordering of
    Seeding begins after the championship field has been se-                 teams. Just because a team is ranked higher or lower
    lected and is intended to arrange teams within the tour-                 than expected does not mean that a method has failed to
    nament bracket in a way that reflects relative quality and               "accurately" judge their performance. Moreover, revers-
    promotes competitive balance. Seeding often consid-                      ing the position of one ranking to satisfy an imaginary
    ers predictions about team strength more than selection,                 ideal risks undesirable outcomes elsewhere on that same
    which, as discussed, typically stresses deservingness                    ranking list.
    (McGuire, 2025). Seeding decisions may be influenced
    by geography, travel, hosting requirements, conference                      Thus, one should clearly define the objectives and pri-
    rematches, and other operational constraints.6                           orities an ideal ranking system should satisfy and evalu-
       Note that a method appropriate for choosing which                     ate the said system based on these qualities, instead of
    teams belong in the field is not automatically the best                  an imagined ideal list (Keeney and Raiffa, 1993).
    method for ordering them.                                                   The following four clusters contain a "menu" of at-
       Seeding therefore asks: How should the selected                       tributes that ranking systems may be designed to satisfy,
    teams be placed within the tournament?                                   providing a common vocabulary and a useful checklist
                                                                             for discussing ranking methods without presuming that
    2.5   On the best vs. most deserving debate
                                                                             any particular philosophy must prevail.
    Ranking disagreements frequently arise when the terms
    "best" and "most deserving" are treated as though they                    Table 1: Twenty-Five Attributes of Ranking Systems
    mean the same thing. Whereas the best team is gen-
    erally understood to be most likely to perform well in                   Cluster 1: Trust, openness, and accountability
    future competition, the most deserving is the one judged
                                                                             Transparency · Simplicity · Consistency ·
    to have earned recognition through its completed body
                                                                             Accountability · Justifiability · Reproducibility ·
    of work. The concepts overlap but produce different
                                                                             Institutional confidence
    conclusions.
       Some methods combine elements of both predictive                      Cluster 2: Mathematical and analytical soundness
    and retrospective approaches in an attempt to reconcile                  Mathematical integrity · Data and inputs · Predictive
    the underlying philosophical choice about which objec-                   validity · Stability throughout the season · Robustness ·
    tive should receive priority.                                            Task-specific accuracy
                                                                             Cluster 3: Practicality and sustainability
    2.6   Conclusions on ranking tasks
                                                                             Ease of implementation · Administrative efficiency ·
    In practice, each ranking system should be evaluated                     Resistance to manipulation · Adaptability · Viability
    according to the task(s) it was built to solve.
       Accuracy in forecasting future results, assessing a                   Cluster 4: Fairness and competitive incentives
    team’s body of work, making tournament selections, and                   Fairness · Scheduling · Respecting head-to-head results
6
                                                                             · Balancing the margin of victory · Incentive alignment
    In addition, seeding may or may not adjust for sudden changes to         · Geographic equity · Philosophical coherence
    team strength such as, for instance, injury, potentially improving
    upon solely results-based methods (Gray and Schwertman, 2012).


                                                                         3
    3.1     Sources of our attributes                                                ings produced by their chosen method? By identifying
                                                                                     who or what institution is accountable for the results of
    Attributes were assembled from several complementary
                                                                                     a ranking system, stakeholders ensure against arbitrary
    sources: discussions with coaches and administrators on
                                                                                     decisions.
    the MD1 Lacrosse Selection Criteria and Ranking Com-
    mittee (SCR), published work on ranking and decision                             3.2.5    Justifiability
    methods, public expectations about fairness and trans-                           Does the explanation for ranking one team above an-
    parency, experience from years of operating sports rat-                          other correspond to what actually happened on the field?
    ing systems, and practical lessons from existing NCAA                            A system can be transparent but misguided and the rea-
    approaches.                                                                      sons given for a ranking should be grounded in real com-
       They are intentionally broad and concern mathemat-                            petitive outcomes.
    ical performance, governance, communication, incen-
                                                                                     3.2.6    Reproducibility
    tives, and trust and are not assumed to be equally impor-
    tant in every sport or institutional setting.                                    Can an independent, qualified analyst reproduce the
       A useful discussion of these attributes should first                          same results given the same data and exact method-
    identify non-negotiable(s), establish priorities among                           ology? Reproducibility is a safeguard against hidden
    remaining attributes, and acknowledge that necessary                             manipulation or mistakes and opens the door for exter-
    trade-offs between priorities reflect the values and com-                        nal validation, including "what-if" analysis by coaches
    petitive structure of the sport in question.                                     and fans.
                                                                                     3.2.7    Institutional confidence
    3.2     Cluster 1: Trust, openness, and accountability
                                                                                     Do stakeholders trust the institution overseeing the rank-
    3.2.1    Transparency                                                            ings to act fairly, competently, and without improper
    Can stakeholders access the system’s logic and inspect                           influence? Even mathematically sound systems can lose
    its formulas, weights, and inputs? If not, they cannot                           credibility if the body overseeing them is perceived as
    assess whether it is fair. Transparency is the foundation                        partial, inconsistent, or insufficiently accountable.
    of public trust.7
                                                                                     3.3 Cluster 2: Mathematical and analytical sound-
    3.2.2    Simplicity
                                                                                         ness
    Can coaches, administrators, media, and fans easily iden-
                                                                                     3.3.1    Mathematical integrity
    tify inputs and explain how the method works? Com-
    plexity is not a virtue. The simpler a system is, the more                       Are the system’s operations, assumptions, and re-
    likely it is to be used correctly, discussed accurately, and                     lationships mathematically valid?        Mathematically
    accepted widely.                                                                 sound methods use well-defined procedures and valid
                                                                                     reasoning to produce results that are reasonably stable.
    3.2.3    Consistency
                                                                                     3.3.2    Data and inputs
    Are the same rules applied across the teams and seasons
    without "ad hoc" changes? Inconsistent rules produce                             Does the system use all relevant information and justify
    suspicions of unfairness. If two teams with identical                            any meaningful data it excludes? A system that ignores
    bodies of work receive different treatment, the system                           legitimate data may produce rankings that feel incom-
    loses credibility.                                                               plete, biased, or arbitrary.
    3.2.4    Accountability                                                          3.3.3    Predictive validity
    Is a clearly identified person or institution responsible                        Does the system predict future performance better than
    for explaining, defending, and answering for the rank-                           chance or other reasonable benchmarks? Predictive va-
                                                                                     lidity is one potential test for whether a ranking succeeds
7
    Both committee-based and complex mathematical models can suffer                  in capturing team strength.8
    from a lack of transparency. One class of models beginning to be
    used for sports ranking are machine learning-based methods, which
                                                                                 8
    typically suffer from an inherent lack of interpretability Doshi-Velez           Barrow et al. (2013) tests predictive validity in a variety of goal-
    and Kim (2017).                                                                  differential and win-loss metrics, finding that the least squares meth-


                                                                             4
    3.3.4    Stability throughout the season                                    of its conference structure, or slight adjustment in data
    Do rankings stabilize as additional games are played?                       sources should not require a ground-up rebuild of the
    Early-season rankings are based on limited evidence and                     ranking system’s methodology.
    may change substantially as schedules become more                           3.4.5    Long-term viability
    connected, so a credible system should generally be-                    Will the system remain effective, relevant, and well-
    come more stable as results accumulate, reaching a sta-                 accepted across many seasons? Trusted systems produce
    ble state near the end of a season.9                                    reliable results despite changing conditions.
    3.3.5    Robustness
                                                                                3.5     Cluster 4: Fairness and competitive incentives
    Does the ranking system remain reasonably stable when
    small changes are made to the data or assumptions?                          3.5.1    Fairness
    Large changes suggest overfitting and measurement er-                       Do teams with similar competitive achievements receive
    ror and reduce confidence in the method’s rankings.                         similar treatment in the rankings? Fairness is not purely
    3.3.6    Task-specific accuracy                                             mathematical; it depends on shared intuitions about
    Does the system accurately perform its ranking task (pre-                   what deserves recognition.
    diction, retrospective evaluation, selection, or seeding)?                  3.5.2    Schedule integrity
    Accuracy cannot be evaluated without knowing what                           Does the system properly account for schedule difficulty
    success looks like. Strong performance in one task does                     and reward performance rather than mere exposure to
    not imply accuracy in another.10                                            strong opponents? Schedule difficulty provides impor-
                                                                                tant context for a team’s record, however, merely facing
    3.4     Cluster 3: Practicality and sustainability
                                                                                strong opponents (thanks to conference affiliation or ge-
    3.4.1    Ease of implementation                                             ographic boundaries) is not as important as performing
    Can the system be implemented without specialized ex-                       successfully against them.
    pertise or expensive infrastructure? Ease of implementa-                       A credible system distinguishes strength of opposition
    tion goes hand-in-hand with simplicity and verifiability.                   from accomplishment against that opposition.11

    3.4.2    Administrative efficiency                                          3.5.3    Respect for head-to-head results
    Can rankings be produced accurately and on time for                     When two teams are otherwise comparable, does the sys-
    committees, teams, media, and fans? Slow approaches                     tem appropriately reflect the result of their head-to-head
    are assumed to be worse than equivalent quicker ones.                   meeting? In competitive sports, head-to-head results are
                                                                            regularly seen as the "gold standard" by coaches, teams,
    3.4.3    Resistance to manipulation                                     and the public.12
    Does the system resist strategies of untoward manipula-
                                                                                3.5.4    Balancing margin of victory data
    tion such as strategic scheduling, running up the score,
    or other gamesmanship? Procedure should not influence                       If making use of margins of victory, does the system ex-
    team strategy or behavior before and during a contest.                      tract meaningful information from scores without intro-
                                                                                ducing noise from "garbage time" or encouraging teams
    3.4.4    Adaptability                                                       to run up the score? Margins of victory can distinguish
    Can the system accommodate changes in sport structure,                      between narrow wins and dominant performances, but
    scheduling, and data availability without losing its gov-
    erning principles? The evolution of a sport, realignment

                                                                           11
   ods based on the margin of victory are among the most predictive.          Evidence of conference bias in selection and seeding like that de-
9
   Ochieng et al. (2022) provides an approach for comparing rating            tailed in Coleman et al. (2010) and Paul and Wilson (2015) might
   methods based on stability over time using rolling and expanding           relate to a failure to accurately account for scheduling differences.
                                                                           12
   windows, finding that Massey and PageRank methods are more sta-            Coleman (2005) points out that, while results should be maximally
   ble than win percentage, least square, and eigenvector methods.            respected, situations often arise in which "team A beats team B, team
10
   Whereas predictive accuracy measures future outcomes, retrospec-           B defeats team C, and team C beats team A," or a more complicated
   tive accuracy might require other standards.                               cycle of more than 3 teams.


                                                                       5
     they must be handled carefully.13                                               4. Structural challenges in intercollegiate com-
     3.5.5    Incentive alignment                                                       petition
     Does the system encourage behavior that makes the                               Ranking systems built on sound principles still operate
     sport more competitive, fair, and sportsmanlike?14                              under difficult mathematical and institutional constraints.
                                                                                     Teams play uneven schedules, data is limited, results are
     3.5.6    Geographic equity
                                                                                     sensitive, and definitions of fairness, accuracy, and de-
     Does the system avoid systematically advantaging or                             servingness are contested. In addition, systems must
     disadvantaging teams because of geography, travel, or                           satisfy the practical (and sometimes varied) needs of
     scheduling access? Geographic location affects travel                           coaches, administrators, governing bodies, and the pub-
     costs and scheduling options.                                                   lic.
     3.5.7    Philosophical coherence                                                   This section examines the principal challenges that
                                                                                     confront all ranking systems and explains why no one
     Does the system express a clear and defensible philoso-
                                                                                     method can completely eliminate uncertainty and con-
     phy of competitive merit? A system without philosophi-
                                                                                     troversy.
     cal coherence produces rankings that may be mathemat-
     ically correct but intuitively unsatisfying.                                    4.1    Sparse data
     3.6     Conclusion on attributes                                                Intercollegiate schedules provide only a limited sample
                                                                                     of the possible comparisons among teams.
     Together, these twenty-five attributes provide a broad vo-
                                                                                        Most teams play only a small proportion of the
     cabulary for discussing ranking systems. No system will
                                                                                     other teams in their division, and the amount of cross-
     score perfectly on every attribute. They are not a scor-
                                                                                     conference competition varies substantially by sport.
     ing formula and need not be weighted. Their purpose is
                                                                                     Consequently, ranking systems must estimate relation-
     to make visible and discussable the assumptions behind
                                                                                     ships between teams that have not played one another
     ranking decisions.
                                                                                     and may have few common opponents.


13
     "A 15-run win isn’t five times more informative than a 3-run win,"              better" (Analysis, 2011).
                                                                                14
     as noted by Alexander (2026), but especially at low sample sizes,               Goodhart (1975)’s famous adage that "When a measure becomes a
     margin of victory can make win percentage predictions "substantially            target, it ceases to be a good measure."


                          Table 2: Selected Characteristics of Nine NCAA Division I Team-Sport Settings

                                         Games        Avg. total        Avg.               Cross-conf.    Head-to-head       Common-opponent
     Sport                Teams        per team           score       margin                      play    connectivity         connectivity
     Football (FBS)           136         12–13               53           19                    40%          Low                  Medium
     Basketball (M)           365         31–32              150        12–16                 35–55%          Low                  Medium
     Basketball (W)           363            30              130        16–17                 35–45%          Low                  Medium
     Baseball                 308         55–60               13            5                 45–60%          Low                  Medium
     Softball                 308         50–60               10            5                 50–70%          Low                   High
     Lacrosse (M)              77         15–16               23            6                    50%          Low                   High
     Lacrosse (W)             133            17               23            7                    50%          Low                   High
     Ice hockey (M)            63         35–40                6            2                    30%         Medium                 High
     Ice hockey (W)            45         35–45                5            3                    25%         Medium                 High
       Note. Figures are approximate and describe the 2025–26 academic year. Total score is the sum of both teams’ scores; margin is the
       absolute difference. Games per team indicates approximate schedule length rather than a calculated season average. Head-to-head and
       common-opponent connectivity are qualitative estimates of the percentages of distinct team pairs within each sport that met directly
       or shared at least one opponent, respectively. These categories illustrate broad scheduling differences; they are not verified percentage
       calculations or measures of pairwise comparisons resolved.


                                                                            6
   These limitations are most apparent in the large                 to improve analytical performance, address unusual cir-
middle-tier conferences and among bubble teams,                     cumstances, or promote fairness.
where small differences can change ranking lists, some-                Each modification produces both benefits and costs,
times drastically. Final scores and scoring margins can             and must be weighed against its loss of transparency,
provide additional information for ranking purposes.                reproducibility, or explainability. The central question is
                                                                    whether the incremental gain in, say, accuracy justifies
4.2   Scope and transferability                                     the added complexity and potentially making the method
Whereas the NCAA aims to apply a common algorithm                   harder to understand and defend.
for team strength ratings across NCAA Division II and
                                                                    4.5   Iterative procedures
III team sports in the NCAA Power Index (NPI), trans-
ferability should not be assumed merely because similar             Some ranking methods, like the NPI, require an iter-
inputs are available. Sports and divisions differ in ways           ative process to reach "convergence" in which teams’
that influence how reliably a ranking system can com-               ratings depend partly on the ratings of their opponents.
pare teams.                                                         Because those opponent rankings are themselves being
   The data in Table 2 illustrate how the number of teams,          calculated, the system begins with initial values and re-
games per team, schedule density, scoring frequency and             peatedly updates the rankings until subsequent changes
variance, divisional and regional structure, and degree             become sufficiently small — hence, convergence.
of cross-conference play can influence the network con-                Iteration is not inherently a mathematical weakness,
nectivity of sporting data and comparison paths among               nor does it necessarily mean that a method is nonlin-
team pairs.                                                         ear. The primary concern is transparency: independent
   More cross-conference play allows information to dif-            users must know the starting conditions, formulas, ad-
fuse between teams; less play leaves conferences as rela-           justment rules, stopping criteria, and treatment of excep-
tively isolated clusters. As illustrated, the availability of       tional cases to reproduce the published results. Without
head-to-head and common-opponent comparisons varies                 that information — or the original code — verification
substantially across the nine settings. A common multi-             becomes considerably more difficult.
sport algorithm may be administratively attractive, but it
should be validated separately in each sport and division.          4.6   Clustering and false precision
                                                                    Ranking systems often produce clusters of rankings
4.3   Human bias
                                                                    whose estimated differences in team strength are small
Human judgment can introduce conscious or uncon-                    relative to the uncertainty of the underlying data. A
scious bias into ranking and selection decisions.                   formula may assign each team a distinct numerical
   Committee members may represent particular con-                  value (even with multiple decimal places of precision)
ferences, regions, or institutions, creating actual or              that nevertheless fails to correspond with meaningful
perceived conflicts of interest. Mathematical systems               competitive separation.
such as the RPI or NPI can reduce reliance on human                    This concern is especially important near selection
judgment, but their design still reflects human choices             and seeding boundaries, i.e. "on the bubble," where a
about data, weights, parameters, and definitions of                 small rating difference can produce a consequential in-
merit. Neither committees nor algorithms eliminate                  stitutional decision.
bias entirely; credible governance should instead make                 Systems should therefore report or examine sensitiv-
potential sources of bias visible and establish procedures          ity to perturbation, uncertainty, and the stability of close
for limiting their influence.                                       comparisons rather than assuming that every numerical
                                                                    ordering represents a clear difference in team quality or
4.4   Compromising on simplicity with "ad hoc"                      accomplishment.
      adjustments
                                                                    4.7   Gaming the system
While simplicity is an important attribute for coaches,
administrators, media, and the public’s understanding               As mentioned earlier, teams may adjust their scheduling
of a method, additional components may be necessary                 or game strategy to improve their rankings, a form of

                                                                7
strategic response to adverse incentives.                        4.10    Disproportionally weak teams
   Win-loss algorithms may, for instance, incentivize
                                                                 Conferences with especially weak opponents present
programs to avoid risky match-ups and optimize strength
                                                                 a difficult design problem. Sometimes even a victory
of schedule calculations. Margin-informed systems may
                                                                 against a weak team can cause a team’s rating to decline
reduce some of these incentives by rewarding quality of
                                                                 as a result of a given ranking system’s strength of sched-
performance at the potential cost of creating pressure
                                                                 ule calculation.
to score even after a game’s outcome is no longer in
doubt. Methods may employ caps, diminishing returns,                Game scores help avoid some of this effect by consid-
or game-state adjustments to discourage such behavior            ering how a team performed, but they may over-reward
at the cost of introducing additional parameters.                extreme scoring differentials against weak teams unless
   No ranking system is completely resistant to manipu-          margins are duly tapered or capped.
lation; the objective is to identify what incentives exist          A credible method should neither reward teams for
and ensure that they remain consistent with competitive          scheduling weak opposition nor penalize them for play-
integrity and sportsmanship.                                     ing required opponents, and coaches should know in
                                                                 advance how such games will affect their rankings.
4.8   Choosing a goal cutoff
                                                                 4.11    Late-season games
Margin of victory-informed systems cap or taper scoring
differentials to reduce the influence of extreme results         Games played later in a season may better reflect a
and discourage unnecessary late-game scoring.                    team’s strength come time for the championship tour-
    A cap set too low may discard useful information             nament for various reasons, including roster changes,
about team strength, causing the system to approximate           improvements in strategy, or improvements in physical
a binary win-loss model. A cap set too high may add              fitness.
little predictive information while increasing the risk of          Ranking systems must determine whether to weight
incentivizing bad sportsmanship or false prediction.             games equally or to give greater weight to late-season
    The appropriate threshold may differ by sport because        games. Recency weighting may better reflect strength
scoring frequency, game structure, competitive balance,          at the cost of undervaluing early victories and creat-
and expectations regarding sportsmanship vary. Caps              ing scheduling inequities in which teams cannot control
should therefore be treated as parameters requiring em-          when they play their most important games.
pirical validation and review rather than as self-evident
or universal.                                                    4.12    Conclusion on structural challenges

4.9   Valuing head-to-head results                               To recap: as mentioned, ranking systems for college
                                                                 sports face unique, sometimes contradictory challenges,
In the author’s experience, a common objection to rank-
                                                                 including: sparse data with little transferability and con-
ings reads something like: "We beat that team, so why
                                                                 nectivity, the risk of human bias, compromises between
are they ranked ahead of us?" Head-to-head results carry
                                                                 simplicity and ad-hoc improvements, the risk of non-
a unique intuitive and competitive importance.
                                                                 convergence and false prediction, sportsmanship con-
   When all other factors are assumed to be equal, a             cerns, the salience of head-to-head results, the choice of
victory by team A over team B should guarantee that              a goal differential cutoff or recency bias, and, occasion-
team A earns a higher ranking, but one game may not              ally, conferences with especially weak teams. A perfect
outweigh evidence from an entire season, particularly if         universally applicable system probably does not exist.
the teams have different schedules and if other results
strongly favor team B that lost in a direct meeting or,
                                                                 5.     Families of ranking methods
notably, if team A lost to a team C which team B beat.
   A credible system should specify in advance how               Ranking systems can be grouped by structure and phi-
it handles head-to-head evidence and should be inter-            losophy of merit. The below categories are not mutually-
pretable enough to explain when broader season perfor-           exclusive and real systems often combine elements from
mance overrides a head-to-head result.                           more than one.

                                                             8
        Table 3: Types of Ranking Systems and Examples                       incentives they generate are consistent with the sport’s
                                                                             competitive values.
     Type                                            Example
                                                                             5.3 Adjustable parameter (Weighted) Systems (ex:
     Win–loss resume                                 RPI
                                                                                 the NCAA Power Index or NPI)
     Margin of victory                               Power ratings
     Adjustable parameter (weighted)                 NPI                     These systems combine multiple components through
     Expert judgment (committee)                     CFP                     specific weights, modifiers, or other adjustable parame-
     Multi-factor composite                          NET                     ters, including (in the case of the NPI) win percentage,
     Consensus                                       BCS                     location weights, quality win bonuses, and a dial for the
     Market-based                                    Oddsmakers              number of wins until unfavorable victories are dropped
     Artificial intelligence or machine learning     —                       from consideration (i.e., minimum wins retained).
                                                                                The parameters or weights can be adjusted by rank-
                                                                             ing authorities to produce different outcomes suitable for
     5.1 Win-loss resume systems (ex: the Rating Per-                        specific sports, conferences, or seasons, allowing adapta-
         centage Index or RPI)                                               tion to differences in the length of the schedule, scoring
     These rating systems evaluate accomplishment through                    patterns, the size of the home-field advantage, and the
     wins, losses, and opponent records. The Rating Per-                     data environment.
     centage Index (RPI) is a familiar example of a win-loss                    However, flexibility creates a justification problem,
     resume method.                                                          as stakeholders seek (especially when given adverse re-
        Win-loss resume systems are comparatively easy to                    sults) information about how each parameter was se-
     describe and use inputs that are widely available across                lected, what evidence supports it, and how sensitive the
     sports. They tend to include adjustments for whether                    final rankings are to alternative values. Arbitrary pa-
     teams won and the quality of their schedules to adjust                  rameters, even when established in advance and clearly
     for differing regular season schedules.                                 documented, can be perceived as an attempt to produce
        Their principal limitation is that they necessarily treat            a preferred ranking outcome.
     narrow and dominant victories as equally valuable: a
     virtue when data are plentiful, less-so when data are                   5.4 Expert judgment or committee-based systems
     sparse. In college sports, win-loss systems may occa-                       (ex: the College Football Playoff Committee)
     sionally fail to consistently produce accurate or statisti-             This type of ranking system relies on a committee or
     cally significant solutions due to a lack of data connect-              panel to evaluate quantitative evidence alongside con-
     ing disparate teams or conferences.                                     textual information like injuries, unusual scheduling cir-
                                                                             cumstances, late-season changes in strength, head-to-
     5.2 Margin of victory (MOV) systems (ex: Power                          head context, and any other information that formal mod-
         rating systems)                                                     els may omit.
     Margin of victory systems treat the size of a game result                  Challenges include transparency, reproducibility,
     as valuable information about relative team strengths,                  consistency, and accountability. Outside observers
     usually employing safeguards like cutoffs to limit the                  often lack knowledge about how individual criteria
     influence of extreme scores and discourage unnecessary                  were weighted, whether comparable cases were treated
     bad sportsmanship.                                                      similarly, and what evidence proved to be ultimately
        Margin-informed methods preserve information that                    decisive.
     win-loss systems discard, which has been shown to im-                      Their legitimacy therefore depends on clearly stated
     prove predictive accuracy in Barrow et al. (2013) and                   criteria, procedures for managing conflicts of interest,
     several other studies.                                                  and detailed explanations of consequential decisions.
        Their suitability depends on both analytical con-
     straints (the data environment)15 and whether the

15
     Margin of victory systems are often less necessary in conferences       where each team plays every other.


                                                                         9
5.5 Multi-factor composite systems (ex: The NCAA                   against subsequent results.16
    Evaluation Tool, or NET, for basketball)                          Market prices are not intended to reward season-long
                                                                   accomplishment or determine championship deserving-
These systems combine multiple types of information to             ness. They may also be influenced by relative liquidity
represent several dimensions of team performance. NET,             constraints, betting biases, risk-management practices,
used in DI basketball, illustrates the broad approach, in-         and the different amount of attention afforded to certain
cluding 1) a metric for adjusted net efficiency based on           teams or sports.
points per possession, opponent points per possession,                While market information can provide a valuable pre-
opponents strength, and the location of the game played            dictive benchmark, it’s inherently opaque, difficult or
and 2) a team value index based on wins and losses.                impossible to reproduce, and, may be inappropriate as a
  A multi-factor system may capture information that a             stand-alone selection system.
simpler measure omits, potentially improving the eval-
uation of team strength, deservingness, and schedule               5.8 Artificial intelligence or machine-learning sys-
performance.                                                           tems
  Its principal challenge is explainability. As the num-           AI methods identify patterns and uncover complex re-
ber of inputs, adjustments, and interactions increases,            lationships that traditional models may overlook, poten-
so does the difficulty of understanding why one team is            tially improving predictive performance when sufficient
ranked above another.                                              high-quality training data are available.
                                                                      Unfortunately, they are often opaque and many fail to
5.6 Consensus systems (ex: the old Bowl Champi-                    set independently-verifiable, easily-repeatable standards
    onship Series or BCS, at least in part)                        for the evaluation of team strength.
                                                                      Their applicability to the four sports ranking tasks
These systems combine multiple rankings derived from               identified above requires further study.
various types of models or expert polls to produce a final
result that does not depend entirely on one method’s               5.9   Randomization
results.                                                          While not a system, randomization provides a useful
   A consensus system reduces sensitivity to any unusual          boundary case. Results should be meaningfully distin-
or spurious assumptions made by any single component              guishable from random chance, not just at the top or
method, revealing areas of broad agreement.                       bottom of a ranking list but also "on the bubble."
   Their value depends on the quality and diversity of
                                                                   6.    Common myths about ranking systems
the systems being combined. If components use similar
assumptions, share the same biases, or measure differ-             Discussions about ranking systems are often shaped by
ent concepts of merit, combining them may reinforce                assumptions that appear reasonable but do not withstand
weaknesses or produce a result that isn’t coherently in-           careful examination. These misconceptions obscure the
terpretable. A credible consensus system must explain              actual purpose of rankings, exaggerate the capabilities of
why each component was included, how components                    mathematical models, and confuse disagreements about
were weighted, and what the combined result means.                 value-choices with technical disputes.
                                                                     Table 4 (top of next page) highlights a few myths
5.7 Market-based systems (ex: the Las Vegas odds-                  and/or misconceptions worth keeping in mind when
    makers or online platforms)                                    choosing an optimal system.

These systems use betting lines or other market infor-
mation to estimate expected game outcomes and, there-
                                                              16
fore, relative team strength. They often inherently and            Nick Saban pointed to oddsmakers as source of information about
                                                                   team strength after Alabama was not selected in 2022: "When they
rapidly incorporate new statistical analysis, injury and           told me that we would be favored against three out of the four
other team news, public expectations, and judgments of             teams that got in the playoff, I’m like, why aren’t we in the play-
market participants. Their performance can be evaluated            offs?"(Flaherty, 2022)


                                                             10
      Table 4: Common Myths About Sports Rankings                  7.3   Match data and methodology to task

Accuracy is all that matters.                                      Determine which data should legitimately influence
Transparency, fairness and trust are also important.               rankings. These data potentially include game results
                                                                   such as wins and losses, scoring margins, and opponent
The best team is automatically the most deserving.
                                                                   quality or other factors such as injury reports, market
Defining deservingness requires value judgments.
                                                                   information, and human intuition.
Computer rankings are entirely objective.                             Build a ranking methodology using one or more of
Computers are machines that do arithmetic and logic. They
omit bias only if humans design their algorithms to do so.
                                                                   those identified in section 5 to effectively convert data
                                                                   into a ranking list.
More complexity equals better rankings.
Complexity can cause overfitting and confuse underlying
                                                                   7.4   Test close cases and unintended consequences
assumptions.
Artificial intelligence will eventually create the perfect         A ranking system should be evaluated on relatively dif-
ranking system.                                                    ficult cases and not just on the best and worst teams in
It may identify complex patterns and improve predictions,          a sports division. Sensitivity analysis should examine
but it cannot determine what a ranking ought to value.             whether small changes in results, weights, caps, or as-
Controversy means failure.                                         sumptions produce outsized changes in outcomes. Such
Disagreement is inevitable given incomplete schedules,             testing helps distinguish meaningful differences from
conflicting definitions of merit, and genuine uncertainty.         methodological instability.
                                                                      Ensure that your ranking system’s rules do not unduly
                                                                   influence team strategy or behavior by incentivizing, for
7.     Practical framework for choosing a system                   instance, unfair scheduling or score manipulation.
A productive evaluation should begin with a purpose
                                                                   7.5 Specify governing bodies and communication
rather than a preferred method, formula, or outcome.
                                                                       procedures and conduct regular reviews
The following framework provides a sequence applica-
ble for use by governing bodies, committees, coaches,              Carefully document methodology, data sources, rules in
and analysts.                                                      case of tight decisions, and procedures for revising the
                                                                   system in the future. Assign responsibility for explain-
7.1 Determine the ranking task and define "merit"                  ing and defending the rankings.
                                                                      Regular reviews are an appropriate part of ranking,
State whether this system is intended for prediction, ret-         but changes should be evidence-based, transparent, and
rospective evaluation, championship selection, seeding,            applied consistently, rather than just in response to a
or some combination of these ends.                                 single controversial result.
   Then specify what the ranking of one team over an-
other is supposed to indicate about those two teams. Is            8.    Conclusions
the higher ranked team stronger, more deserving, more
likely to succeed in a tournament, or some combination             The central lesson of this paper is straightforward: rank-
of these concepts?                                                 ing intercollegiate teams involves selecting formulas,
                                                                   committee processes, or hybrid approaches that make
                                                                   choices along the lines of competing philosophies of
7.2     Establish priorities and nonnegotiables
                                                                   merit.
Decide which attributes, of those listed in section 3, this           Prediction, retrospective evaluation, championship se-
ranking system should satisfy. Options may include                 lection, and seeding are related but distinct tasks. A
transparency, reproducibility, predictive validity, resis-         system designed to forecast future performance may not
tance to some type of gaming, or others. Distinguish               also identify the teams with the strongest regular season
priorities from requirements and acknowledge any in-               resumes. A method appropriate for selecting a champi-
herent conflicts between them.                                     onship field may not be the best for seeding it.

                                                              11
   The structure of intercollegiate competition limits            9.    Statements and Declarations
what rankings can accomplish. Sparse and uneven
                                                                  9.1   Data
schedules, limited cross-conference competition, differ-
ences between sports and divisions, and closely matched           The descriptive data summarized in Table 2 were ob-
bubble teams create uncertainty that no one method                tained from d1field.com. Some are loose estimates from
can eliminate. Limitations are especially important               other sources. They are intended to illustrate the dif-
near tournament cutoffs, where small methodological               ferences inherent in different NCAA sporting environ-
choices may determine which teams are selected to                 ments.
compete.
   For these reasons, ranking systems should be judged            9.2   Acknowledgments
by more than just their "accuracy." Mathematical sound-           This overview of ranking systems for NCAA sports was
ness and empirical performance are as important as                inspired by conversations with the NCAA Men’s Divi-
transparency, simplicity, reproducibility, fairness, the          sion I Lacrosse Selection Criteria and Ranking Commit-
alignment of incentives, explanatory fidelity, and insti-         tee (SCR) about the creation of a ranking system called
tutional confidence. Complex mathematical algorithms,             Powerwise (PWR) that may see future use. Matthew
human judgment, market information, and AI-informed               Bomparola prepared the final manuscript by rewriting
approaches can contribute useful evidence, but none are           large sections of the paper and editing any remaining
automatically appropriate for official use.                       text. He did not use artificial intelligence.
   To conclude: no ranking system is likely to eliminate
controversy or incorporate all desirable attributes. Cred-        9.3   Use of artificial intelligence
ible systems should instead seek to define their purpose,
make tradeoffs visible, apply principles consistently, and        The author used ChatGPT as an editorial assistant dur-
explain their decisions in terms that stakeholders can un-        ing the preparation of the first draft manuscript. The tool
derstand. The most useful question in sports ranking              assisted with organization, drafting, clarity, and presen-
is therefore not "Which ranking is correct?" but "What            tation. That being said, the research questions, concep-
should this ranking mean?"                                        tual framework, selection of attributes, data, substantive
                                                                  judgments, interpretations, and conclusions were devel-
                                                                  oped and approved by the human author. The author
                                                                  accepts full responsibility for the accuracy, originality,
                                                                  and integrity of the manuscript.




                                                             12
References
Zach Alexander. Mlb elo rating model explained: How we project the 2026 season, 2026. URL https://birdlandmetrics.
  com/articles/projection-model.
Skeptical Sports Analysis. The case for dennis rodman, part 3/4(c)—beyond margin of victory, 2011. URL https:
  //skepticalsports.com/the-case-for-dennis-rodman-part-34cbeyond-margin-of-victory/.
ESPN Sports Analytics.           BPI and strength of record: Reshaping the debate of best and most
  deserving.           ESPN.com, 2016.                URL https://www.espn.com/blog/statsinfo/post/_/id/125983/
  bpi-and-strength-of-record-reshaping-the-debate-of-best-and-most-deserving.
Daniel Barrow, Ian Drayer, Peter Elliott, Garren Gaut, and Braxton Osting. Ranking rankings: an empirical compari-
  son of the predictive power of sports ranking methods. Journal of Quantitative Analysis in Sports, 9(2):187–202,
  2013. doi: 10.1515/jqas-2013-0013.
B. Coleman. Minimizing game score violations in college football rankings. Interfaces, 35:483–496, 2005.
B. Jay Coleman, J. Michael Dumond, and Allen K. Lynch. Evidence of bias in ncaa tournament selection and seeding.
  Managerial and Decision Economics, 31:431–452, 2010.
Finale Doshi-Velez and Been Kim. Towards a rigorous science of interpretable machine learning. arXiv, 2017. doi:
  10.48550/arXiv.1702.08608.
FIBA. Qualification system: Paris 2024 olympics—3x3 Basketball, 2024. URL https://parigi2024.coni.it/en/schedule/
  roadtoparis2024/qualification-system/3x3-basket/56-3x3-basketball/file.html. Version dated January 29, 2024.
Kevin Flaherty. Nick saban questions alabama exclusion from 2022 college football playoff, 2022. URL https://
  247sports.com/article/nick-saban-questions-alabama-exclusion-from-2022-college-football-playoff-211785579/.
Charles Goodhart. Problems of monetary management : the u.k. experience. Papers in monetary economics, 1975.
Kathy L. Gray and Neil C. Schwertman. Comparing team selection and seeding for the 2011 ncaa men’s basketball
  tournament. Journal of Quantitative Analysis in Sports, 2012. doi: 10.1515/1559-0410.1369.
J. Irmer.      Rating the power rankings.            The Orbit, 2024.      URL https://rmhsorbit.com/3372/news/
  rating-the-power-rankings/. Author listed as J. Irmer (’25).
Ralph L. Keeney and Howard Raiffa. Decisions with multiple objectives. Cambridge Books, 1993. URL https:
  //ideas.repec.org//b/cup/cbooks/9780521438834.html.
Corbin McGuire. NCAA tournament selection myths. NCAA.org, 2025. URL https://www.ncaa.org/
  media-center-debunking-ncaa-tournament-myths/.
NCAA. Division II proposal 2025-8: Automatic qualification—football. Legislative Services Database, 2025. URL
  https://web3.ncaa.org/lsdbi/search/proposalView?id=108003. Effective August 1, 2025.
Peter Juma Ochieng, András London, and Miklós Krész. A forward-looking approach to compare ranking methods
  for sports. Multidisciplinary Digital Publishing Institute, 2022. doi: 10.3390/info13050232. URL https://www.
  mdpi.com/2078-2489/13/5/232.
Rodney J. Paul and Mark Wilson. Political correctness, selection bias, and the ncaa basketball tournament. Journal
  of Sports Economics, 2015. doi: 10.1177/1527002512465413. URL https://journals.sagepub.com/doi/10.1177/
  1527002512465413.
H. S. Stern. In favor of a quantitative boycott of the bowl championship series. Journal of Quantitative Analysis in
  Sports, 2006. doi: 10.2202/1559-0410.1031. URL https://doi.org/10.2202/1559-0410.1031.




                                                        13
