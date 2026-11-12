<!-- source: library/preprints/arXiv/2026/2026 - Imputing Missing Data in Longitudinal Life-Logging Athlete Data - Sahdra et al.pdf -->
<!-- item: https://arxiv.org/abs/2610.41226 -->
<!-- authors: Saaz Kaur Sahdra, Kalina Yacef, HaeJin Lee, Judy Kay -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-12; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Imputing Missing Data in Longitudinal Life-Logging Athlete Data

                                             I MPUTING M ISSING DATA IN L ONGITUDINAL L IFE -L OGGING
                                                                 ATHLETE DATA

                                                                                              A P REPRINT


                                                              Saaz Kaur Sahdra                                        Kalina Yacef
                                                          Faculty of Computer Science                          Faculty of Computer Science
                                                             University of Sydney                                 University of Sydney
                                                               Sydney, Australia                                    Sydney, Australia
                                                         saaz.sahdra@sydney.edu.au                           kalina.yacef@sydney.edu.au
arXiv:2610.41226v1 [cs.HC] 30 Oct 2026




                                                                                             HaeJin Lee
                                                                                     Faculty of Computer Science
                                                                                        University of Sydney
                                                                                          Sydney, Australia
                                                                                    haejin.lee@sydney.edu.au

                                                                                               Judy Kay
                                                                                      Faculty of Computer Science
                                                                                         University of Sydney
                                                                                           Sydney, Australia
                                                                                      judy.kay@sydney.edu.au


                                                                                           November 2, 2026

                                                                                             A BSTRACT
                                                  Long-term, diverse personal informatics data enables athletes to understand and act on their health
                                                  and performance goals, whether assessing readiness right now, tracking how soreness relates to
                                                  training load over time, or predicting how sleep affects next-day performance. However, the inherent
                                                  missingness in longitudinal data, if handled inappropriately, can bias these analyses. To our knowl-
                                                  edge, no prior work has systematically benchmarked classical and deep learning imputation methods
                                                  on long-term self-tracking data from athlete populations. We evaluate six imputation methods across
                                                  four missingness mechanisms at missingness rates spanning 10-80%. Using seven diverse long-term
                                                  self-tracking datasets from 231 individuals, we assess both point accuracy and the preservation
                                                  of temporal and multivariate structure. Our results show that no single method dominates across
                                                  all conditions and reveal a critical trade-off: while PAIN is superior on point-wise accuracy, deep
                                                  learning methods (BRITS, GRU-D, and GRIN) are better at preserving multivariate and temporal
                                                  structure, particularly under higher missingness. Our findings offer a practical, goal-conditioned
                                                  framework that guides researchers in selecting imputation strategies aligned with both the underlying
                                                  missingness mechanism and the specific analytical goal of long-term self-tracking studies.

                                         Keywords Imputation · Missing Data · Long Term · Athletes · Wearable · User Goals

                                         1     Introduction
                                         1.1   Motivation

                                         Self-tracking wearable devices, such as Fitbit or WHOOP, have significantly changed how individuals view and
                                         understand their health [22, 35, 13, 15]. By building relational models from daily-level self-tracking data, individuals
                                                      Sahdra et al.                                           A P REPRINT



can better understand long-term trends in their health, identify where interventions may help, and evaluate how effective
those interventions are. Within this broader landscape, athletes represent a distinct population. Their training, recovery,
and injury-prevention goals differ fundamentally from general self-trackers [30], often shifting seasonally or directed
by coaches alongside an athlete’s own objectives [11]. They generate unusually rich multi-source data (wearable,
self-report, and coach-logged), and their data carries direct, high-stakes value for performance and injury decisions
[37, 34]. This distinctiveness extends to how their data goes missing. A missing day, for instance, may not indicate a
lapse in tracking at all, but rather a rest day or a competition day, as some sports, such as soccer, prohibit wrist-worn
wearables during games [39]. How this missing data is handled can therefore bias resulting estimates of training-load,
recovery, or performance trends [37, 34, 7]. Yet prior work has not linked individual analytical goals to imputation
choice, leaving a gap between how data is handled and what it is ultimately used for.
This gap matters because an athlete’s goals take several forms: a point-in-time assessment (e.g., "how ready is my body
for a long run today?"), a relational temporal pattern (e.g., "did my soreness track with training load and sleep this
week?"), or a predictive insight (e.g., "does consistent 8+ hours of sleep make tomorrow’s training feel easier?"). The
second and third of these require data spanning a meaningful duration. We define this as long-term monitoring (≥30
daily time points), sufficient to capture weekly and monthly behavioural patterns. Longer collection windows, however,
increase the risk of missingness through device non-wear, synchronisation failures, or battery depletion [7].
Missingness is also not uniform across athletes. It can be person- and context-specific [48]. One athlete may remove
their device during high-intensity sessions, another during sleep, another during low-mood periods. Since these
patterns are themselves informative about the outcome of interest [33], applying a single imputation method across
all athletes risks distorting person-specific inferences. While contextual, group-based models have outperformed
one-size-fits-all approaches elsewhere [23], the effect of imputation choice on person-specific, multivariate insight
remains underexplored for athletes specifically.

1.2   Handling Missing Data

Numerous studies across disciplines have highlighted the importance of addressing missing data, with growing evidence
that imputation strategy choice can meaningfully alter downstream conclusions [16, 7, 37, 3, 35, 4, 13, 9]. For example,
consider estimating the association between sleep duration and next-day resting heart rate from months of wearable
data. If non-wear nights disproportionately follow late-night social events or travel, simple list-wise deletion or mean
imputation can attenuate or even invert the estimated effect, whereas context-aware deep learning (DL) imputation could
potentially recover it by capitalising on missing or self-report data. As more DL imputation methods emerge, researchers
are beginning to compare Multiple Imputation with DL approaches under different missingness conditions [3]. However,
these studies have not yet linked individual analytical goals to imputation choice. Since imputation outputs directly
feed into personalised feedback and trend interpretation, managing missing data is not merely a pre-processing task
but a decision shaping the reliability and interpretability of insights for an individual’s goals. Choosing an appropriate
method is not straightforward, depending on the nature, prevalence, and recoverability of missingness [24]. We extend
this view by proposing that individual analytical goal is another dimension that should inform imputation choice.

1.3   Research Questions

Building on the person-specific missingness challenges described above, we ask how imputation methods support
analysis of long-term, multivariate wearable data across different missingness mechanisms (MCAR, MAR, MNAR, and
Block/Gap, defined in Table 1) and missingness proportions. We examine not only which method is most accurate, but
which best preserves the cross-variable and temporal relationships essential to athlete-monitoring analyses.
RQ1: How accurate are different imputations under different missingness mechanisms and percentages?
RQ2: How do different imputation methods preserve the multivariate relationships and temporal shape of the dataset
under different missingness mechanisms and percentages?
RQ3: Which imputation best serves which types of individual analytical goals?

1.4   Contributions

Our work makes three contributions. First, a comprehensive benchmark identifying which methods achieve the highest
accuracy and best preserve multivariate temporal structure across missingness scenarios. Second, a goal-conditioned
decision framework mapping accuracy–structure trade-offs to specific analytical goals (point-in-time, relational,
predictive), offering concrete guidance on which metric matters most for a given goal. Third, evaluation across diverse
real-world datasets (including WHOOP and Fitbit data), supporting generalisable, cross-device conclusions. This work


                                                            2
                                                       Sahdra et al.                                           A P REPRINT



extends prior research by Choube et al (2025) [7], Tang & Kay (2017) [35], Künzler et al. (2019) [23], Tenan (2023)
[37], and Benson et al. (2021) [3] filling a gap in systematic missing-data benchmarking for athlete populations.


2     Related Work

The analysis of missing data and adherence in longitudinal wearable health and behaviour sensing studies is an
area of interest within Human-Computer Interaction (HCI) and health disciplines. Missingness in life-logging and
wearable datasets can arise from various factors, including but not limited to device non-wear, charging gaps, and user
disengagement or re-engagement. Missingness patterns can follow different and complex mechanisms. Despite its
ubiquity, the treatment of missing data has been largely overlooked in wearable health literature, with many studies
failing to address the implications of their chosen imputation strategy [7, 40].

2.1   Wearable and Self-Report Data from Athletes

An important body of HCI research on wearable and life-logging devices has focused on encouraging physical activity
in inactive or general populations, or supporting chronic health condition management (e.g., [12, 46]). Such studies
often aim to encourage physical activity through personalised recommendation-driven approaches to increase activity
levels or address inactivity-driven health risks. While important, it differs deeply from the potential role of wearables
for very active people, such as athletes.
Athletes generate unique data patterns, often characterised by high variability in physiological states and activity levels,
and distinctive missingness patterns. For example, a missing day may indicate not just a rest day but a competition
day—some as sports, such as soccer, prohibit wrist-worn wearables during games [39]. These individuals also require
distinct analytical approaches, as their goals, such as optimising performance, preventing injury, or monitoring recovery,
differ substantially from those of sedentary populations [30]. Furthermore, individual goals may change seasonally
or be directed by coaches and sport professionals alongside personal short- and long-term goals [11]. Sport science
routinely applies multivariate statistics and advanced modelling techniques to understand complex relationships between
variables such as heart rate, workload, and recovery [14, 2]. Yet, missing data in self-tracking datasets can distort these
inter-varaible relationships and compromise the validity of resulting insights [37].
Handling missing data effectively remains a critical gap in data processing and modelling for athlete populations.
Several studies have shown that missing data handling methods can directly impact the accuracy and interpretability
of downstream analysis. For instance, Choube et al. (2025) [7] demonstrated that imputation technique choice can
significantly alter analysis results for heterogeneous wearable data streams, while Benson et al. (2021) [3] found that, in
athlete workload monitoring, imputation methods leveraging multivariate dependencies consistently outperform simpler
statistical approaches. Together, these studies highlight the need to understand how imputation strategies perform under
the specific conditions generated by athlete populations. Investigating this further could have the potential to inform
personalised performance tracking, injury prevention strategies, and recovery monitoring, ultimately contributing to the
broader field of wearable health analytics and SportHCI.

2.2   Characterising Missingness

HCI has discussed missingness through the lenses of adherence, blocks, gaps, and streaks [36, 35, 27]. Other disciplines,
including health and psychology, have also used a statistical framework to characterise missingness. Rubin’s (1976)
[32] seminal framework on missingness mechanisms categorises three types of missingness. Table 1 presents these,
MCAR, MAR and MNAR, in its first three rows, with definitions (Col 2) and examples (Col 3). Each mechanism has
different statistical approaches for appropriate handling and imputation to avoid bias in downstream analysis. Table 1
also summarises their significance and methods for handling them.
Rubin’s missingness mechanisms remain a cornerstone for understanding missingness in modern research. Interestingly,
real-world multivariate data often exhibit mixtures of these mechanisms, which complicates efforts to apply standard
imputation methods [24]. Many studies within and outside of HCI have identified the challenges with incomplete data
and adherence in long-term life-logging and wearable tracking data (see [36, 35, 27, 3, 34, 3]). Breaks/gaps, both micro
and macro, seem inevitable and have diverse patterns across individuals, making it difficult to model for groups and
populations [35, 13]. Nevertheless, the presence of missing data itself can also contribute to a user’s reflection on
behavioural patterns and the system’s ability to monitor adherence and provide adaptive feedback [13, 35, 4]. This dual
role, where missingness is both an analytical obstacle and a meaningful behavioural signal, underscores the need for
methods that can accommodate rather than ‘correct’ for diverse, individual-specific patterns of missingness.


                                                             3
                                                        Sahdra et al.                                                 A P REPRINT



There is increasing agreement among scholars that long-term analysis results should be contextualised and personalised
to individuals and groups for meaningful insights. Contextualised models account for user receptivity and context,
outperforming generalised models in mobile health interventions [35, 23]. Tenan (2023) [37] and Sharma et. al.
(2026) [34] both demonstrated how datasets in sport science commonly deviate from the MCAR assumption, with
missingness patterns linked to athlete fatigue, non-wear during recovery, or poor performance days. Therefore, handling
missingness within heterogeneous data requires careful consideration of missingness mechanisms, amount, and goal
of analysis. Similarly, Gomer and Yuan (2025) [16] highlighted that a mixture of mechanisms within a single dataset
could significantly distort statistical inferences, particularly under large proportions of MNAR values. Like Choube et
al. (2025) [7], we emphasise the need for explicit testing and reporting of missingness mechanisms in wearable and life-
logging studies, and advocate for participant-level imputation evaluation. This study therefore aims to develop a robust
pipeline of imputation strategies tailored to the specific missingness patterns inherent in wearable and self-tracking
datasets.
Epstein et al. (2021) [13] discuss the challenges of long-term tracking including changing devices due to time, changing
goals, emotional bonds, and the inevitability of gaps or breaks. Researchers need to develop tools and processes to
deal with heterogeneous data from disparate sources with missingness, because the gaps in itself could tell a story on
their own [13]. We agree with Epstein et al. (2021) that gaps should be considered a normal part of the data. However,
to the best of our knowledge, we have not seen a fully developed pipeline that equips researchers with a framework
to handle gaps and missingness of different mechanisms. Since missingness, such as gaps, can be diverse between
users, a generalised model may not adequately capture this person-specific heterogeneity. Building on Xu et al. (2021)
[45], in this study we build the foundation for personalised behaviour modelling for within-person and sample-specific
approaches, as we believe this method will best characterise individual patterns and useful insights.
Table 1: Missingness Mechanisms: This table presents the type and definition of each mechanism as described in the
literature, operationalises it with an example, and connects it to its significance in PI/HCI. Based on imputation methods
and studies identified in our literature review, we also indicate which handling approach is theoretically best suited to
each mechanism. However, these methods and mechanisms have not been systematically benchmarked together on
athlete.
 Missingness Mecha-     Definition                   Example                      Significance to PI/HCI      Applicable     Handling
 nism                                                                                                         Methods
 MCAR      (Missing     Probability of missing-      A sensor randomly fails      Simplest case; analy-       Listwise deletion, pair-
 Completely at Ran-     ness is unrelated to any     to record data due to        sis remains unbiased,       wise deletion, mean im-
 dom)                   observed or unobserved       a transient hardware         but reduced sample size     putation, multiple impu-
                        data.                        glitch, independent of       may affect power and        tation, maximum likeli-
                                                     user behavior.               generalizability.           hood.
 MAR (Missing at        Probability of missing-      Users with lower en-         Common in PI/HCI            Multiple imputation with
 Random)                ness depends only on ob-     gagement scores are          logs; must model miss-      covariates, inverse prob-
                        served variables, not on     less likely to answer        ingness using observed      ability weighting, max-
                        the missing values them-     follow-up questions, but     covariates to avoid bias.   imum likelihood meth-
                        selves.                      engagement scores are                                    ods.
                                                     recorded.
 MNAR (Missing Not      Missingness depends on       Users with very high         High risk of biased con-    Sensitivity analyses, se-
 at Random)             unobserved values, in-       stress are least likely to   clusions about sensitive    lection models, pattern-
                        cluding the missing value    complete self-report sur-    or extreme states; di-      mixture models, explicit
                        itself.                      veys about stress.           rectly impacts design       modeling of missingness
                                                                                  decisions and user mod-     mechanism. Deep Learn-
                                                                                  eling.                      ing methods such as
                                                                                                              BRITS.
 Mechanism        Un-   Underlying missingness       Complex longitudinal         Typical in real-world       Exploratory diagnostics,
 known / Mixed          mechanism is unclear or      app data with device is-     PI/HCI deployments;         multiple     imputation
                        combines MCAR, MAR,          sues, optional questions,    requires careful diag-      under MAR, scenario-
                        and MNAR.                    and avoidance of sensi-      nostics and robustness      based         sensitivity
                                                     tive prompts.                checks.                     analysis. Deep learning
                                                                                                              methods such as BRITS
                                                                                                              and PAIN.
 Block/Gap Pattern      Can be either MAR or         User decides to take off     Typical in real-world       Deep learning methods
 Missingness            MNAR missingness but         wearable due to high         PI/HCI where users          such as BRITS and
                        for longer periods of time   stress (observed or un-      abandon and re-engage       PAIN.
                        (i.e., days).                observed) for a week.        with wearables.



                                                               4
                                                       Sahdra et al.                                          A P REPRINT



2.3   Imputation Strategies

Multivariate analysis often requires complete-case datasets (i.e., datasets with no missing data). For example, standard
linear regression cannot natively handle missing data and will fail or crash if a dataset contains NA values. This
missingness must be handled before running the model to avoid biased results or loss of power. Common ways of
handling such missingness are list-wise deletion, mean imputation, or advanced imputation methods [7]. The type of
missingness mechanism can help us determine which handling method is most appropriate (see Table 1).
When analysing in-the-wild studies or real-world datasets with missingness, traditional "easy" methods of handling
missing data (i.e., list-wise deletion or mean imputation) can be inappropriate for the complex temporal and multivariate
nature of the data. In recent years, researchers have explored both statistical and machine learning based approaches to
imputation. For example, Benson et. al. (2021) [3] evaluated multiple imputation techniques in the context of athlete
workload monitoring, finding that machine learning models outperformed regression-based methods by leveraging the
inherent relationships between variables. Sharma et. al. (2026) [34] propose a layered imputation pipeline to ensure
that athlete-specific inter-individual variability is captured and that latent constructs are considered. Their method also
outperformed traditional models such as Multiple Imputation (MI).
More DL methods are emerging as promising alternatives for handling missing data in multivariate datasets. Some
models leverage temporal dependencies in time series data, while others adapt to incorporate temporal context during
imputation [48]. More recently, graph-based methods have integrated network structures into the imputation process,
enabling the preservation of both temporal and inter-variable relationships [47, 42]. These structure-aware approaches
are particularly relevant for wearable datasets, where physiological signals often exhibit strong correlations across time
and variables. This has the potential to aid users in understanding their multivariate and temporal data.
As previously mentioned, Choube et al. (2025) [7] emphasised the importance of systematically evaluating imputation
strategies, particularly for datasets with heterogeneous and interdependent streams of data, as found in mobile and
wearable sensing studies. They proposed selecting imputation strategies based on the underlying data structure and the
missingness mechanism, which align closely with the goals of this study.
Recent systematic reviews have compared several of these imputation methods in health data contexts and found
that deep learning methods generally outperform statistical approaches for complex, longitudinal health data, though
issues with interpretability and fairness remain [26]. These reviews find that MICE is most widely used [31] and
MICE, BRITS, GRU-D, and GAIN are well-studied in health data [21, 26]. PAIN and GRIN seem promising deep
learning methods but have seen limited application in individual health and wearable datasets. Although deep learning
methods are recommended, no single method is universally optimal, and many methods like PAIN and GRIN remain
under-explored and under-utilised in personal health data [21, 31]. Collectively, these systematic reviews [21, 26, 31]
identify a need for more benchmarking of advanced methods in individual health contexts. This gap, according to the
available literature, has not yet been addressed in conjunction with analytical goals for athlete populations.
Building on this gap, we selected six different imputation methods used on time series data (excluding mean imputation)
that can handle mixed data types: Multiple Imputation by Chained Equations (MICE), Bidirectional Recurrent
Imputation for Time Series (BRITS), Gated Recurrent Unit with Decay (GRU-D), Generative Adversarial Imputation
Network Wasserstein VAE hybrid (WGAIN-VAE), Precision Adaptive Imputation Network (PAIN), and Graphical
Recurrent Imputation Network (GRIN). This selection spans traditional statistical and deep learning approaches, and
deliberately includes under-explored methods (i.e., PAIN and GRIN) alongside well-established ones (i.e., MICE),
directly addressing the benchmarking gap identified above. Each method is further defined under Section 4 Methods.

2.4   Scope and Hypotheses

To the best of our knowledge, no study has evaluated different imputation methods systematically by considering
not only the missingness mechanism, but also the user analytical goal for downstream analysis. This paper directly
addresses this gap by evaluating 6 imputation methods across 4 missingness mechanisms at missingness rates spanning
10-80%, using 7 diverse long-term self-tracking datasets comprising data from 231 individuals. Such variety in datasets
can provide cross-device insights. However, validation of the measurements from the devices used for data collection in
these public datasets is out of scope for this study. The data we use are also limited to daily level aggregation.
We focus on evaluating the imputation methods on the basis of point accuracy and their ability to preserve temporal
and multivariate structure of the data. These metrics allow us to map which type of imputation is optimal for a user’s
analytical goal. We anticipated that each dataset will have users with different missingness characteristics. We also
hypothesise that deep learning methods compared to MI will perform better across MAR, MNAR, and Blocks/Gaps
conditions across all missingness percentages (H1 for RQ1 and RQ2). We expected the quality of imputation to degrade
at 40%-50% missingness or higher, based on previous literature [10, 20]. Finally, we expected that no one imputation


                                                            5
                                                       Sahdra et al.                                           A P REPRINT



method would give best across point accuracy and preserve temporal and multivariate structure of the data (H2 for
RQ3). Rather, we aim to build a decision framework that will guide researchers in determining the best path for their
goals and datasets.


3     Data and Study Design

3.1     Operationalising Long-Term

Our study is based on analyses of at least 4 weeks of data. This threshold is not arbitrary relative to the three analytical
goals introduced. A point-in-time assessment (e.g., "how ready is my body for a long run today?") requires only a
single day’s data and is unaffected by our threshold. A relational temporal pattern (e.g., "did my soreness track with
training load and sleep this week?") requires at least one full weekly cycle to be observable. A predictive insight
(e.g., "Does consistent 8+ hours of sleep make tomorrow’s training feel easier?") requires repeated exposure to the
pattern being tested, which a single week cannot provide, but a month can begin to establish. One month is therefore
the shortest window in which all three goal types, including the two that depend on duration, can be meaningfully
evaluated, while remaining short enough that non-wear, device failure, and athlete dropout remain comparatively rare
compared with longer windows. We treat this as a practical lower bound for this benchmark rather than a claim that one
month is sufficient for all athlete-monitoring purposes. Goals tied to slower physiological adaptations (e.g., detecting
a sustained change in resting heart rate or cardiovascular fitness) are known to require longer observation windows
than the relational and predictive goals we benchmark here, and we return to this as a direction for future work in
Section 7.3.3.

3.2     Datasets

Using 7 diverse long-term self-tracking datasets comprising data from 231 individuals, we evaluated 6 imputation
methods across 4 missingness mechanisms at missingness rates spanning 10–80% (see Appendix A.1 for more
information on which athletes are included in the analysis). The raw public datasets were each cleaned and consecutive
days were forced. After cleaning, for each user in each dataset, the longest available complete-case (or near complete-
case) subset was extracted. These complete or near-complete subsets are treated as ground-truth, as is common practice
in the literature [26, 31]. Using the complete subsets, we simulated missingness under 4 mechanisms at 8 different
proportions. Finally, a suite of imputation methods were applied to these simulated missingness datasets.

3.2.1    Ethics Statement
Six of the seven datasets are public, obtained from Kaggle [29, 17, 18] and research repositories (PMData [38], Human
Rhythms Dataset [49], SoccerMon [28]), released under terms permitting research reuse. As secondary analysis of
de-identified public data, this does not require IRB/Ethics review. We rely on each dataset’s documented consent and
licensing terms and did not independently verify original consent procedures. The seventh dataset is the first author’s
personal WHOOP data, as self-experimentation with no other data subjects, formal IRB/Ethics review was not sought.

3.2.2    Extracting complete-case subsets
We computed each user’s complete subset by first enforcing consecutive days and then identifying the longest continuous
observation window with minimal missingness (≤5%) across all target variables. For larger datasets with longer
timelines, a greater than 60-day window was applied. Users with less than 60 days were excluded. For shorter
few-person datasets, shorter timelines were accepted to provide edge cases. Up to 5% residual missingness with gaps
of at most one day is tolerated and type-aware imputed (numeric: median; logical: modal; categorical: mode). We
acknowledge that this windowing choice, while methodologically necessary, may limit generalisation to the broader
athlete population. Full extraction parameters are detailed in Appendix A.1.

3.2.3    Dataset Summaries
Table 2 summarises the span of days and target variable counts per dataset. Table 3 summarises the metrics available in
each dataset’s complete subset. Full narrative descriptions, collection context, and device/sensor details for each dataset
are provided in Appendix Appendix A.1. In brief:

         • Human Rhythms [49]: 166 college students (including 1 NCAA athlete) tracked via Fitbit and daily surveys
           over 17 months, focused on circadian/ultradian rhythms. Complete subset retained 146 users.


                                                             6
                                                           Sahdra et al.                                                A P REPRINT



       • SoccerMon [28]: 77 elite Norwegian women’s football players, combining PmSys [41] self-report well-
         ness/load data with GPS/sensor data over 2 seasons. Complete subset retained 45 users.
       • Fitbit [29]: 33 consumer Fitbit users (23 with sleep data) over 31 days. This dataset is an edge case under
         our 30-day threshold, included to test generalisability across shorter timelines and consumer-grade devices.
         Complete subset retained 23 users.
       • PMData [38]: 16 users over 5 months, integrating Fitbit, a sports-logging app, and Google Forms. Complete
         subset retained 14 users.
       • Personal WHOOP: First author’s own 2-year WHOOP export (700+ days, 500+ observed), collected via the
         WHOOP Developer API v2 [43]. Complete subset retained 181 days.
       • Public WHOOP [18]: Single-user Kaggle WHOOP export with user-annotated context, spanning 51 days.
         An edge case under our 60-day threshold.
       • Athlete [17]: Single NFL player’s self-published multi-device data (WHOOP, Polar, Oura, MyFitnessPal)
         over 94 days.

Tables 2 and 3 show how these data sets are heterogeneous in terms of size, populations, and the nature of the data
collected.
                    Table 2: Span of days and number of target variables for each dataset across users.

                                                        Span of Days (Complete Subset)            Target Variables
               Dataset                 n complete       Min     Max     Median          Mean      Raw      Complete
               Human Rhythms                    146      55      251         105       127.10       20             13
               Soccermon                         45      80      360         294       257.07       24             26
               Fitbit                            23      21       31          31        29.43       31             14
               PMData                            14      63      152         131       122.36       63             83
               Personal WHOOP                     1      —       181          —            —        70             24
               Public WHOOP                       1      —        51          —            —        26             25
               Athlete                            1      —        94          —            —        43             40
Note. Span is measured in days across users within each dataset. For single-user datasets (n = 1), only the observed span is reported;
minimum, median, and mean are undefined (denoted —). Target variables are counted removing all id columns, admin/metadata
columns, and columns created during cleaning from the original dataset. As some columns were created during cleaning from the
original variable, the complete subset has more columns than the raw for some datasets.



3.3   Naturally Occurring Missingness Mechanisms in Datasets

To characterise missingness in our longitudinal datasets, we implement a staged diagnostic pipeline operationalising the
MCAR/MAR/MNAR taxonomy plus a Block/Gap pattern, while remaining conservative about mechanism identifiability.
The pipeline sequentially tests for MCAR (pattern-wise independence between missingness and variable values), MAR
(whether missingness can be predicted from other observed variables), and MNAR (via run-length and tail-clustering
diagnostics testing whether missingness depends on the unobserved value itself), escalating through these tests via a
priority ladder to assign a single verdict per user-variable combination. Appendix A.2 has full statistical procedures,
thresholds, and correction methods.
Crucially, these mechanisms cannot be identified from data alone, as distinguishing MAR from MNAR requires
knowledge of why values are missing. We therefore use "Undetermined" liberally rather than over-claiming a mechanism
the data cannot adjudicate.

3.4   Simulated Missingness

We construct a controlled benchmark in which the true missingness mechanism is known by design, following the
formal framework of Rubin (1976) [32] and the HCI-defined Block/Gap pattern. We deliberately impose known
missingness onto each user’s complete subset, a process commonly termed "amputation," the standard approach for
missing data simulation studies [16, 7, 26, 31]. Each complete subset per user serves as the ground-truth reference
against which all subsequent amputations and downstream imputations are evaluated. We inject NA values into
each per-user complete subset under four distinct mechanisms (MCAR, MAR, MNAR, Block/Gaps) at eight severity


                                                                  7
                                                           Sahdra et al.                                      A P REPRINT


                             Table 3: Types of metrics in the complete subset across datasets
    Legend: PW = Personal WHOOP; UW = Public WHOOP; AT = Public Athlete; FB = Public Fitbit; PM = Public PMData;
                               SM = Public SoccerMon; HM = Public Human Rhythms.
                 Metric in Complete Subset                              PW   UW    AT   FB    PM    SM   HM
                 Sleep Duration                                         ✓     ✓    ✓     ✓     ✓    ✓    ✓
                 Sleep Stages                                           ✓     ✓    ✓      ·    ✓     ·    ·
                 In-bed Duration                                         ·    ✓    ✓     ✓     ✓     ·   ✓
                 Blood Oxygen                                           ✓     ✓     ·     ·     ·    ·    ·
                 Skin Temp                                              ✓     ✓     ·     ·     ·    ·    ·
                 HRV                                                    ✓     ✓    ✓      ·     ·    ·    ·
                 RHR                                                    ✓     ✓    ✓      ·    ✓     ·    ·
                 Travel                                                 ✓      ·    ·     ·     ·    ·    ·
                 Respiratory Rate                                        ·    ✓    ✓      ·     ·    ·    ·
                 Number of Workouts                                     ✓      ·    ·     ·     ·    ·    ·
                 Heart Rate Zones Time                                  ✓      ·    ·     ·    ✓     ·    ·
                 Max HR                                                  ·    ✓    ✓      ·    ✓    ✓     ·
                 Min HR                                                  ·     ·    ·     ·    ✓     ·    ·
                 Average HR                                              ·    ✓    ✓      ·    ✓     ·    ·
                 SD HR                                                   ·     ·    ·     ·    ✓     ·    ·
                 Activity Type                                          ✓      ·    ·     ·    ✓     ·    ·
                 Activity Distance                                       ·     ·    ·    ✓     ✓     ·    ·
                 Activity Time                                           ·     ·    ·    ✓     ✓     ·    ·
                 Activity Calories                                       ·     ·    ·     ·    ✓     ·    ·
                 Activity HR                                             ·     ·    ·     ·    ✓     ·    ·
                 Team Activity & Type                                    ·     ·    ·     ·    ✓     ·    ·
                 Individual/Team Performance                             ·     ·    ·     ·     ·   ✓     ·
                 Training Load                                           ·     ·    ·     ·     ·   ✓     ·
                 Speed                                                   ·     ·    ·     ·     ·   ✓     ·
                 Steps                                                   ·     ·    ·    ✓     ✓     ·   ✓
                 Injury                                                  ·     ·    ·     ·    ✓    ✓     ·
                 Illness                                                 ·     ·    ·     ·     ·   ✓     ·
                 Weight                                                  ·     ·   ✓     ✓     ✓     ·    ·
                 RPE                                                     ·     ·   ✓      ·    ✓     ·    ·
                 Scripted Intensity                                      ·     ·   ✓      ·     ·    ·    ·
                 Calories in/out                                         ·     ·   ✓    out   out    ·    ·
                 Macros/Micros Nutrition                                 ·     ·   ✓      ·     ·    ·    ·
                 Water Intake                                            ·     ·   ✓      ·    ✓     ·    ·
                 Self-report feeling (i.e., recovery, mood, etc.)        ·    ✓    ✓      ·    ✓    ✓    ✓
                 Recovery activity                                       ·     ·   ✓      ·     ·    ·    ·



levels (10%–80% missingness proportions). We acknowledge that these amputations are not an exhaustive list of how
missingness can manifest in athletes’ real-life data, and discuss this as a limitation in Section 7.3.3.
MCAR masks cells uniformly at random. MAR and MNAR condition missingness on observed covariates (weekend
flags, auxiliary high-value indicators) and on each variable’s own extreme values, respectively, so that missingness
probability depends on observed data (MAR) or on the value itself (MNAR). Block/Gap imposes contiguous per-user
gaps of scaling size, simulating realistic device non-wear periods. All amputations use fixed seeds for reproducibility,
and the realised NA rate (overall and per-variable) is recorded alongside each amputated file. Full weighting schemes,
seed values, and block-placement algorithms are provided in Appendix A.3.

4     Imputation Methods

Six imputation methods are run against every amputated file:

       1. MICE: Multiple Imputation by Chained Equations. [1]
       2. BRITS: Bidirectional Recurrent Imputation for Time Series. [5]
       3. GRU-D: A gated recurrent unit with decay mechanisms for irregular series. [6]
       4. WGAIN-VAE: Generative Adversarial Imputation Network Wasserstein VAE hybrid. [47, 42]


                                                                    8
                                                      Sahdra et al.                                           A P REPRINT



      5. PAIN: Precision Adaptive Imputation Network. [19]
      6. GRIN: Graphical Recurrent Imputation Network. [8]

This selection spans the methodological spectrum from classical statistical MI to recurrent, adversarial, and graph-based
DL, allowing us to evaluate how each fares against mechanisms with known ground truth.
Every method imputes one user at a time, with parallelism occurring across users (N_CORES=16) and never within a
user. For each amputated file, data are split by user, date-sorted, and dispatched to a worker. MICE runs in pure R,
while the deep learning (DL) workers are called through Python. The full pipeline runs twice, governed by two window
strategies: "full," which imputes each user’s entire date-sorted sequence at once (requiring ≥10 rows), and "win30,"
which partitions each user into tumbling 30-day windows, imputes each independently, and re-binds results (users
with <30 rows are skipped). The win30 strategy serves as a sensitivity check against non-stationarity, where a user’s
per-chunk results aggregate into an overall "ok," "partial," or "failed" status. Notably, there is no mean/median fallback.
Failed imputations are skipped and logged rather than crudely filled, preserving ground-truth comparison integrity.
Floors are enforced before any model runs (minimum 10 user rows for MICE/DL, minimum 3 observed values per
column), and chunks with no missing cells are returned unchanged. Full implementation details (hyperparameters,
architecture specifics, and shared training infrastructure) are provided in Appendix A.4.
MICE fills missing values by repeatedly predicting each incomplete variable from the others, producing several
"complete" dataset versions that capture estimation uncertainty. It performs best under MAR, where the probability of
missingness can be explained by observed variables, but does not natively account for time, leaving temporal patterns
unmodelled, precisely the assumption this study examines.
BRITS uses a neural network that reads sequences both forwards and backwards in time, reconstructing missing
values from patterns at both earlier and later time points [5]. It should perform well under MCAR, MAR, and block
missingness, and has also been applied to MNAR settings and to healthcare/physical-activity data, suggesting suitability
for wearable data, though at higher computational cost and interpretability trade-offs than MICE.
GRU-D extends a standard recurrent network with built-in decay mechanisms modelling how the influence of past
observations fades as time gaps grow, explicitly treating missingness patterns as meaningful rather than fixing decay
rates in advance [6].
WGAIN-VAE builds on GAIN’s adversarial framework, in which a generator fills missing values while a discriminator
tries to detect which values were originally missing, pushed toward realism via a "hint" mechanism [47, 42]. The
original GAIN formulation outperforms MICE under MNAR conditions but is not designed for temporal modelling.
The hybrid combines a Wasserstein-GAN with a variational autoencoder (VAE) to add temporal and distributional
stability.
PAIN adapts dynamically to different data types, distributions, and missingness patterns via a three-step process: com-
bining statistical methods, random forests, and autoencoders; adaptively weighting these based on data characteristics;
and refining imputed values to reduce noise [19]. It supports mixed data types and shows promise for health data,
though it remains comparatively under-explored.
GRIN combines a recurrent network for temporal patterns with a graph neural network for variable relationships,
learning representations via bidirectional message passing [8]. It makes no assumptions about the distribution of missing
values but assumes underlying patterns remain stable over time, narrowing its effective use toward MAR scenarios.
All methods handle mixed data types via consistent pre-processing (logical/categorical variables coerced to factors
or numeric), and the three recurrent models (BRITS, GRU-D, GRIN) share common training infrastructure (gradient
clipping, time-limited early stopping). A shared post-processing routine standardises numeric values before modelling
and constrains results within observed-data ranges afterward. Together, these conventions ensure all six methods are
evaluated under a uniform, reproducible protocol, isolating differences in imputation quality to the methods themselves.
Full architectural and hyperparameter detail for each method is provided in Appendix A.4.

5   Evaluation Methods
Our benchmark imposes missingness on complete subsets under known mechanisms, so every imputed value can be
scored against ground truth. All accuracy metrics are computed on truly masked cells. The evaluation is organised
around our research questions: point-level reconstruction accuracy, preservation of multivariate (between-variable)
structure, preservation of temporal (within-variable) structure, and preservation of distributional shape.
A methodological note applies throughout: since standard metrics are typically averaged only over successfully evaluated
users, methods that silently fail on harder users (e.g., shorter series, sparse columns) can post a deceptively low error.


                                                            9
                                                      Sahdra et al.                                           A P REPRINT



We therefore introduce a coverage-penalised family of metrics (prefixed cp-) that deflate each raw metric by the fraction
of attempted users actually evaluated, ensuring low error on a subset is never rewarded over consistent accuracy across
the full sample. At full coverage, each coverage-penalised metric equals its raw counterpart. Pooled (cross-dataset)
versions use sample-size weighting so larger datasets and those with higher coverage contribute proportionally more.
Full derivations for all metrics are provided in Appendix B.

5.1   Point-level reconstruction accuracy

For numeric and ordinal targets, we report normalised RMSE and MAE (NRMSE, NMAE) as primary point-accuracy
measures, enabling comparison across variables and datasets of different scales (Appendix B.1, Eq. (6)). Bias is
recorded as the mean signed residual to distinguish noisy-but-centred methods from those that systematically over- or
under-impute, a failure mode RMSE alone conceals. These three measures (cpNRMSE, cpNMAE, cpNBias) are each
coverage-penalised following the scheme above (Appendix B.1, Eqs. (4)–(3)).

5.2   Preserving multivariate (between-variable) structure

Low point-error does not guarantee inter-variable relationships are preserved. A method could minimise RMSE while
flattening covariance structure, which matters particularly for network-model analyses. We compute two diagnostics.
First, cpCorr is the Pearson correlation between imputed and true values on masked cells, capturing whether rank and
shape are preserved even when absolute level is off. Since correlation is undefined for constant masked vectors, we
track a correlation-specific coverage term alongside standard coverage (Appendix B.2, Eqs. (10)–(16)). Second, cpFrob
and cpPartialFrob compare full and partial correlation matrices (across all numeric/ordinal targets jointly) using the
Frobenius norm of their difference, with partial correlation isolating direct pairwise relationships after conditioning on
all other variables (Appendix B.2, Eqs. (17)–(21)). Because these matrix metrics are computed over each user’s full
series, they are only interpretable at higher missingness levels (50–80%), where a meaningful share of the matrix is
genuinely reconstructed rather than copied through unchanged.

5.3   Preserving temporal (within-variable, over-time) structure

A method can score well on point accuracy while destroying persistence, dynamics, or rhythm. We assess three full-
series temporal diagnostics, computed per user × variable on the complete reconstructed series, since autocorrelation,
differencing, and spectral content are not well-defined on a scattered subset of timepoints. For all three, lower values
indicate better preservation, with 0 denoting perfect fidelity:

       • Autocorrelation error: mean absolute difference in lag-1–3 autocorrelation between true and reconstructed
         series, testing whether persistence (e.g., a high day following a high day) is preserved (Appendix B.3, Eq. (22)).
       • Range-normalised first-difference RMSE: RMSE between first-differenced true and reconstructed series,
         testing whether the magnitude of day-to-day swings is preserved rather than smoothed away (Appendix B.3,
         Eqs. (23)–(24)).
       • Spectral difference: total absolute difference between normalised power spectral densities, testing whether
         periodic (e.g., weekly) structure is preserved (Appendix B.3, Eq. (25)).

We additionally compare performance between full-series and 30-day windowed (win30) imputation strategies. Stability
across the two would indicate robust temporal handling, while degradation under win30 could indicate reliance on
regime-specific context. All temporal metrics use the same coverage-weighted pooling scheme as above (Appendix B.3).

5.4   Preserving distributional shape

Unlike the temporal metrics, which are order-dependent and diagnostic only at higher missingness, distributional
metrics are order-agnostic and masked-cell-only, remaining diagnostic at every missingness level. This matters because
a method can preserve marginal distribution while scrambling temporal order, or vice versa. Both families together are
needed to separate these failure modes.

       • Variance ratio: the ratio of imputed to true variance over masked cells, directly exposing the common "regress-
         to-the-mean" failure that NRMSE cannot detect; a value of 1 indicates perfectly reproduced spread, below 1
         indicates variance collapse, and above 1 indicates inflated variability (Appendix B.4).
       • Kolmogorov-Smirnov (KS) statistic: the maximum gap between true and imputed empirical CDFs, capturing
         whole-distribution mismatch (Appendix B.4).


                                                           10
                                                       Sahdra et al.                                           A P REPRINT



         • 1-Wasserstein distance: the full displacement between true and imputed distributions, complementing KS by
           capturing mismatches spread across the full range rather than concentrated at a single point (Appendix B.4).

KS and Wasserstein distance are likewise coverage-penalised (cpKS, cpWasserstein1) and pooled across datasets using
the same scheme (Appendix B.4, Eqs. (29)–(30)).

6     Results
This section first reports the results for accuracy (RQ1) then, in terms of preservation of multivariate structure, temporal
structure and distributional shape (RQ2). Finally, it compares point accuracy with temporal/distributional structure
and shape (RQ3). This provides a foundation for the discussion in Section 7 which summarises the key ideas in a flow
diagram (Figure 7) for selecting suitable imputations, depending on the goal and data properties.

6.1     RQ1: Imputation Accuracy

6.1.1    Fail Counts
Each user (n=231) was run per method 32 times (4 mechanisms × 8 missingness proportions), giving 7,392 total runs per
method. MICE failed for 7,144 runs, versus only 384 total failures across all other methods combined (Appendix C.1,
Figure 8). This imbalance is why the coverage-penalised metrics below are necessary. A method’s apparent accuracy on
its successfully-imputed users could otherwise misrepresent its reliability across the full sample. Reasons for MICE’s
large failure rate are discussed in Section 7.3.1.

6.1.2    cpNRMSE




Figure 1: cpNRMSE pooled across datasets (n_users_attempted=231), with 95% user-bootstrap confidence bands,
across missingness mechanisms and window strategies.

Figure 1 summarises cpNRMSE pooled across datasets, by mechanism and window strategy. Per-dataset trends are
in Appendix C.2 (Figure 9). MICE exhibits higher cpNRMSE than all DL methods with wider confidence bands,
indicating higher and less stable error. All DL methods remain within 0.1–0.5 cpNRMSE with narrow, overlapping
bands.
Dispersion among DL methods is greatest under Block/Gap, where WGAIN-VAE performs worst for both window
strategies. PAIN attains the lowest pooled cpNRMSE overall, ranking first in 94–100% of user-bootstrap resamples
across nearly all mechanism–strategy combinations (Figure 10, Appendix C.2). The only contested conditions are
MAR/MNAR (full window, 10% missingness), where GRIN claims a share of top ranks, and Block/Gap (full window,
10–20%), where BRITS claims second.


                                                            11
                                                     Sahdra et al.                                         A P REPRINT



Methods fail less and perform better under the full window strategy, especially at higher missingness. Under MNAR
win30, all DL methods spike at 80% missingness to join MICE beyond 0.5 cpNRMSE. No DL method fails on any
dataset below 70% missingness. DL failures emerge only under MNAR at 70–80% (full window, 0.5–0.8 of datasets
evaluable) and under MCAR at 80%/MNAR at 60–80% (win30, 0.3–0.83 evaluable). MICE struggles across all four
mechanisms (0.2–0.6 evaluable throughout). Win30 is markedly more fragile than the full window, especially under
MNAR at high missingness.

6.1.3   cpNMAE
Comparing cpNRMSE and cpNMAE diagnoses error-tail heaviness (Appendix C.3, Figure 11). MICE, BRITS, GRU-D,
PAIN, and GRIN cluster together (ratios ≈1.21–1.37) across most conditions. WGAIN-VAE is a consistent outlier with
a lighter error tail (≈1.08–1.26) despite higher average error. This is most pronounced under Block/Gap, where its ratio
stays 0.1–0.2 below the next-lowest method while the others converge toward 1.30–1.37. This gap disappears under
MNAR win30, where all methods converge toward 1.21–1.28 as evaluable datasets decline.

6.1.4   cpNBias




Figure 2: Coverage-penalised normalised bias (cpNBias), pooled across datasets, by missingness mechanism and
window strategy. Line fading indicates the fraction of datasets evaluable at each missingness percentage; × denotes
complete failure, ◦ denotes no numeric/ordinal target available.

Figure 2 presents cpNBias pooled across datasets. Pairwise comparisons against PAIN and per-dataset breakdowns are
in Appendix C.4 (Figures 12-14). WGAIN-VAE is the only method with a consistent directional bias, under-imputing
across nearly every condition. This shows most severely under Block/Gap (≈-0.4 at 10% missingness, ≈-0.2/-0.3 at
80%), BH-significant (p < .001) throughout.
MICE, BRITS, GRU-D, PAIN, and GRIN remain near-unbiased (within ±0.02) under MCAR, MAR, and Block/Gap.
Under MNAR, bias grows sharply with missingness for all of these methods, but at a markedly more extreme rate for
MICE, worsening further under win30.

6.1.5   Runtime-Accuracy trade-off
Appendix C.5 (Figure 15 and Figure 16) presents per-user runtime against NRMSE. Runtime spread is greater under
win30 (≈1–50s) than full (≈1–10s). PAIN and MICE form the tightest runtime-accuracy clouds under full window, but
PAIN achieves the same profile with substantially greater coverage, so we rank PAIN above MICE. GRIN matches
PAIN/GRU-D’s runtime but shows a higher-error subset (NRMSE 0.6–0.8) under all mechanisms. BRITS shows the
same pattern except under Block/Gap, where it stays within 0.1–0.4 — a reasonable second choice there. GRU-D is
the strongest overall second choice, matching top runtimes while maintaining a tight 0.1–0.4 NRMSE band across all


                                                          12
                                                     Sahdra et al.                                          A P REPRINT



mechanisms. WGAIN-VAE performs worst on this joint criterion, with the widest NRMSE spread and no runtime
advantage.


6.2     RQ3: Preserving multivariate structure

6.2.1    cpCorr




Figure 3: Coverage-penalised correlation (cpCorr), pooled across datasets, by missingness mechanism and window
strategy. Line opacity indicates the fraction of datasets evaluable at each missingness percentage.


Figure 3 presents cpCorr pooled across datasets. Per-dataset detail is in Appendix D.1 (Figure 17). Under MCAR,
MAR, and MNAR (full window), PAIN leads at low missingness (10–20%, ≈0.45) but declines more steeply than other
DL methods, crossing over at ≈40–50% and becoming the lowest-performing DL method by 70–80%. GRIN and
BRITS remain comparatively stable, attaining the highest cpCorr among DL methods at high missingness under these
three mechanisms.
Under Block/Gap, this crossover does not occur: PAIN fails dramatically under the full window (Appendix D.1,
Figure 17), while GRIN and WGAIN-VAE remain flat near zero. BRITS and GRU-D maintain a small, consistent
advantage. MICE performs worst overall, declining near-monotonically and falling below zero in almost all conditions,
with the greatest cross-dataset variability.


6.2.2    cpFrob and cpPartialFrob

We report coverage-penalised Frobenius error for full (cpFrob) and partial (cpPartialFrob) correlation matrices (Ap-
pendix D.2, Figures 18 and 19), where lower indicates better-preserved multivariate structure. A coverage caveat
applies: three of seven datasets (Personal-WHOOP, Public-PMData, Public-SoccerMon) are structurally undefined
across nearly every condition due to zero-variance variables. This is a dataset property, not an imputation-quality
signal. We therefore treat the pooled summary as illustrative, carried effectively by only four datasets (Public-Athlete,
Public-Fitbit, Public-HumanRhythms, Public-WHOOP).
The pooled plot shows a sharp rise under win30 MNAR at 70–80% missingness, driven almost entirely by Public-
Fitbit and Public-HumanRhythms. This is a coverage artefact rather than evidence of worse covariance structure.
Public-Athlete and Public-WHOOP show a stable, flat baseline across methods. These findings indicate correlation
and multivariate structure preservation are not fully redundant. PAIN’s cpCorr advantage at low missingness does not
translate to a cpFrob advantage, where it performs comparably to MICE.


                                                          13
                                                      Sahdra et al.                                           A P REPRINT




Figure 4: Coverage-penalised cpACF, cpFirstDiff, and cpSpectral, pooled across datasets, by missingness mechanism
and window strategy. Lower indicates better-preserved temporal structure. Line/point size indicates the fraction of
datasets evaluable at each missingness percentage.



6.3     Preserving temporal structure

Figure 4 shows cpACF (persistence), cpFirstDiff (dynamics), and cpSpectral (rhythm) pooled across datasets, where
0 denotes perfect preservation. Per-dataset detail is in Appendix E (Figures 20-22. As full-series metrics, higher
missingness is the more informative comparison.
Temporal structure is well preserved by DL methods until the most extreme missingness. MICE is again a dominant
outlier, rising away from the DL cluster at higher missingness, while DL methods remain flat near-floor, except under
MNAR win30 at 70–80% missingness, where all DL methods rise (≈2.3–2.6), though less than MICE. Per-dataset
results show both patterns are driven heavily by Public-Fitbit, which has the richest day-to-day autocorrelation structure.
MICE is a consistent outlier there across cpACF/cpFirstDiff from ≈30% missingness onward. cpSpectral shows a
similar pattern, with all methods rising together under MNAR win30 at 60–80% missingness, indicating periodic
structure becomes unrecoverable at higher missingness regardless of imputer in these dataset-mechanism-strategy
interactions.


6.4     Preserving distributional shape

6.4.1    Variance Ratio

Figure 5 shows the pooled variance ratio (imputed/true variance; 1 = ideal). Per-dataset detail is in Appendix F
(Figure 23). Under MCAR and MNAR, all methods cluster near ideal across most of the range. Under MAR, BRITS,
GRU-D, WGAIN-VAE, and GRIN show isolated spikes to 105 -106 , reflecting occasional over-dispersion rather than a
systematic trend. MICE and PAIN sit consistently just below ideal, indicating mild, stable under-dispersion.
PAIN is the exception under Block/Gap (full window). It collapses to a near-zero variance ratio across the entire
missingness range. This is the signature of imputing a near-constant value across contiguous gaps. Every other method
remains near or above ideal. This collapse is consistent across six of seven datasets (Appendix F, Figure 23).


                                                           14
                                                    Sahdra et al.                                         A P REPRINT




Figure 5: Variance ratio (imputed/true variance over masked cells), pooled across datasets, by missingness mechanism
and window strategy. 1 (dashed line) = ideal; below 1 = collapse; above 1 = over-dispersion. Line/point size indicates
the fraction of datasets evaluable at each missingness percentage.



6.4.2    cpKS and cpWasserstein1

Under all mechanisms, MICE is the dominant outlier, while DL methods sit flush against the ideal line (Appendix F,
Figures 24-27). The MNAR win30 facet is a partial breakdown regime: BRITS, GRU-D, PAIN, and GRIN rise
alongside MICE at 70–80% missingness, though by a smaller margin.


6.5     Point Accuracy vs. Temporal/Distributional Structure and Shape

Figure 6 presents per-user cpNRMSE and cpCorr as forest plots (full window). The win30 equivalents are in Ap-
pendix G.1 (Figure 32). Each horizontal line represents one user, ordered by mean cpNRMSE within dataset. The
dark grey point marks that user’s mean across the 8 missingness percentages, and the whisker spans their full range
(min-max) across those percentages. A long whisker indicates a user whose accuracy is highly sensitive to missingness
severity, while a short whisker indicates stability across the missingness range for that individual.
Combined with PAIN’s leading cpNRMSE, low cpNBias, and favourable runtime-accuracy trade-off, PAIN delivers
strong point accuracy at low cost. GRIN, GRU-D, and BRITS are comparable on accuracy alone. MICE’s poor
cpNRMSE, large positive cpNBias, and high failure count mark it as the least reliable method overall. WGAIN-VAE
shows systematic under-imputation with a comparatively light error tail, at higher computational cost.
Under MCAR, MAR, and MNAR, PAIN’s per-user whiskers resemble other DL methods. Under Block/Gap (full
window), however, PAIN’s cpCorr panel scatters near zero without smooth ordering, with wide, asymmetric whiskers,
though it performs better under win30 for this mechanism (Appendix G.1). BRITS, GRU-D, WGAIN-VAE, and GRIN
retain smoother, low-dispersion cpCorr ordering under Block/Gap. This is corroborated by the variance-ratio results
(Figure 5). PAIN’s leading cpNRMSE co-occurs with severe variance collapse under Block/Gap (≈ 10−13 ), while
every other method remains near ideal. Across all mechanisms, MICE’s whiskers are longer and shifted higher than any
DL method’s.
Appendix G (Figures 28 and 29) presents point accuracy jointly with multivariate structure and variance preservation.
All methods cluster near-ideal on both axes under all mechanisms for the full window, except under MNAR win30 at
high missingness, where methods separate from the ideal cluster simultaneously. MICE deviates most, while BRITS,
GRU-D, WGAIN-VAE, and GRIN rise together by a smaller margin, and PAIN rises by a comparably smaller margin
on cpFrob.


                                                         15
                                                    Sahdra et al.                                        A P REPRINT




Figure 6: Per-user cpNRMSE and cpCorr forest plots, full window strategy, by method (rows) and missingness
mechanism (columns). Within each mechanism, the light   16 panel shows per-user cpNRMSE (point accuracy, lower
is better) and the dark panel shows per-user cpCorr (structure preservation, higher is better). Each line is one user;
the point marks their mean across 8 missingness percentages, and the whisker spans their min–max range across
those percentages (longer whisker = more sensitive to missingness severity). Take-away: PAIN matches top methods
on cpNRMSE across all mechanisms, but its cpCorr panels collapse into near-zero with wider wiskers (i.e., greater
sensitivity to missingness severity). PAIN’s disordered scatter specifically under Block/Gap, clearly exposes an
accuracy/structure trade-off.
                                                       Sahdra et al.                                            A P REPRINT



7     Discussion

The central contribution of this work is a goal-conditioned decision framework for imputing missing data in long-term,
multivariate, athlete-specific wearable datasets. Figure 7 summarises this in a flowchart to guide the selection of the
appropriate imputation mechanism, based on our experiments. Rather than asking "which imputation method is best?",
we show that the right question is "best for what?" and that the answer depends systematically on whether a researcher’s
analytical goal is point-in-time assessment, relational/temporal pattern detection, or predictive insight. In this section,
we first present this framework and the reasoning behind each of its recommendations i.e., RQ3 (Section 7.1), then
substantiate it with the underlying evidence: how missingness manifests in athlete data (Section 7.2), and how methods
perform on accuracy and on multivariate/temporal structure across mechanisms and missingness rates i.e., RQ1 and
RQ2 (Section 7.3). Together, these results give practitioners and researchers a practical, evidence-backed guide for
handling missing data in similar datasets.

7.1     A Goal-Conditioned Decision Framework for Imputation (RQ3)

Choube et al. (2025) [7] argue that "researcher[s] should choose right evaluation metrics to evaluate imputation strategies
depending on their end goal." We operationalise this principle for athlete datasets by identifying three recurring types
of analytical goal: point-in-time assessment (e.g., "how ready is my body for a long run today?"), relational temporal
pattern detection (e.g., "did my soreness track with training load and sleep duration this month?"), and predictive
insight (e.g., "does sleeping 8+ hours and eating more carbs make next-day training feel easier?"). Consistent with
Choube et al. [7], we find that no single imputation method dominates across all three goals. This directly confirms
H2: no single method is simultaneously optimal for point accuracy and for preserving temporal/multivariate structure
(Section 7.3.2 alongside Figure 1 and Figure 3 provide the clearest evidence, where PAIN leads on cpNRMSE but
collapses on cpCorr under Block/Gap). Instead, the appropriate choice depends on which property of the reconstructed
signal the downstream question actually interrogates (i.e., point-wise accuracy, marginal/multivariate structure, or
conditional structure). Figure 7 summarises these recommendations. The remainder of this subsection explains the
reasoning behind each branch, and Sections 7.2 and 7.3 provide the supporting evidence.
Across all three goals, two cross-cutting recommendations hold. First, our coverage-penalised metric suite is what
makes these per-goal recommendations possible. The coverage-penalised metric suite disentangles failure modes (bias,
variance collapse, structural distortion) that raw error metrics alone would conflate, letting us pinpoint where and why
each method fails rather than simply that it does (evidence in Section 7.3). Second, across datasets and conditions,
the win30 windowing strategy degrades performance most under MNAR missingness. We recommend against this
mechanism-window pairing for all three goal types, and treat the full-window strategy as the default (Section 7.3.1).

7.1.1    Goal 1: Point-in-time assessment.
For questions about a single value at a specific point in the time series (e.g., an athlete or coach asking how training went
in Friday’s strength session) the relevant property to optimise is point-wise reconstruction accuracy. We recommend
PAIN. PAIN attains the lowest cpNRMSE under almost all conditions, shows minimal systematic bias, and has a
predictable, low computational cost (Section 7.3.2). Its accuracy is not an artefact of rare catastrophic errors being
averaged away, and it offers the most attractive runtime-accuracy trade-off among the deep learning methods, particularly
under the full-window strategy. GRIN, GRU-D, and BRITS are comparable alternatives for practitioners who prefer to
standardise on a single structure-preserving method across goals. We do not recommend WGAIN-VAE. Its conservative,
mean-reverting behaviour and high computational cost are not offset by any accuracy advantage.

7.1.2    Goal 2: Relational temporal pattern detection.
For questions about how signals co-vary over time (e.g., whether an athlete’s carbohydrate intake correlates with
sleep duration) the priority shifts to multivariate structure preservation, examining how cross-channel covariation,
temporal dynamics, and marginal spread are retained (Section 7.3.2). The recommendation here is more conditional
than for Goal 1. For missingness below 40% under MCAR, MAR, and some MNAR conditions with a full-window
strategy, PAIN remains a reasonable choice if runtime is also a priority. However, PAIN degrades sharply at higher
missingness rates, systematically collapsing variance, so we strongly advise against using PAIN under Block/Gap
missingness specifically, where this collapse is most severe. Above 40% missingness, BRITS and GRIN are the more
dependable structure-preservers, with a flatter performance decay, though both degrade faster under MNAR. This
40% breakpoint is consistent with our expectation, grounded in prior literature [10, 20], that imputation quality would
degrade meaningfully at or above this threshold. For Block/Gap missingness specifically, we recommend BRITS as the
best-available option, with the caveat that "best available" is not the same as "reliable". Like other DL methods (except


                                                            17
                                                                Sahdra et al.                                                    A P REPRINT



                                                                                                                   Goal 3
                Goal 1                                            Goal 2
                                                                                                                 Predictive /
             Point-in-time                                       Relational
                                                                                                                 conditional

                      any
                                                                                                                        any
                                                                Mechanism?
                  PAIN
             all mech. & %                                                                                           BRITS
                                                                                                                      GRIN
             Reliable: top-ranked;                                                                                   GRU-D
             perform well                                                                                        all mech. & %
                                             Sparse                                        Contiguous
             Best-available: top-         (MCAR/MAR)                                      (MNAR/Block-
             ranked; not necessar-                                                           Gap)
             ily perform well

                                      PAIN             BRITS
                                     10–30%             GRIN                       PAIN                 BRITS
                                                       GRU-D                      BRITS                  GRIN
                                                       30–80%                     10–30%                GRU-D†
                                                                                                        30–80%

                                                       †
                                                        Block/Gap is hostile to covariation recovery for
                                                       all methods (cpCorr → 0); Goal-2/3 picks here are
                                                       best-available, not reliable. Full-window strategy
                                                       only.


Figure 7: Decision flowchart for goal-conditioned imputation-method selection (full-window strategy). Read top-to-
bottom: start at your analysis goal (Goal 1–3), follow the branches through missingness mechanism and percentage
where shown, and select the listed method(s) at each leaf. Green leaves denote Reliable recommendations (con-
sistently top-ranked across multiple evaluation metrics and performed well). Orange leaves denote Best-available
recommendations (top-ranked among tested methods, but not necessarily performing well). Point-in-time (Goal 1) and
predictive/conditional (Goal 3) tasks require no mechanism- or percentage-specific branching, so PAIN and [BRITS,
GRIN, GRU-D] are recommended uniformly across all mechanisms and missingness levels, respectively. For relational
tasks (Goal 2) under contiguous (MNAR/Block-Gap) missingness, all methods’ between-variable correlation recovery
collapses toward zero (cpCorr→ 0), therefore the Goal-2 picks shown here are best-available rather than reliable, and
apply to the full-window strategy only.


PAIN), BRITS cpCorr still clusters just above the zero line, reflecting a general difficulty recovering between-variable
relationships under this mechanism.


7.1.3   Goal 3: Predictive / conditional insight.

Conditional "if X and Y, then Z" questions (e.g., what affects an athlete’s next-day readiness) concern direct depen-
dencies among channels after accounting for others. We recommend BRITS and GRIN, the most stable methods
across conditions for this goal, again as a best-available rather than fully reliable recommendation. GRU-D is a
comparable method as well. We consider PAIN, WGAIN-VAE, and MICE inappropriate for this goal given PAIN’s
structure-preservation deficits (Goal 2), WGAIN-VAE’s systematic under-imputation, and MICE’s outright failures
(Section 7.3.1).


7.1.4   Combining goals in practice.

In practice, researchers often pursue multiple goals simultaneously, and deployment on athlete- or coach-facing systems
requires balancing reconstruction quality against computational cost, especially at scale.
For the combination of point-in-time and relational goals (e.g., an accurate readiness estimate today and a faithful
account of how readiness has covaried with sleep and load), no single method optimises both. PAIN wins on accuracy
but collapses spread and structure, while BRITS and GRIN preserve structure without leading on accuracy. BRITS is
the most defensible compromise under Block/Gap missingness (lower cpNRMSE, higher cpCorr than GRIN). GRIN is
a defensible competitor under MCAR, MAR, and MNAR (lower cpNRMSE, higher cpCorr than BRITS). GRU-D is a
reasonable third fallback, performing comparably on cpNRMSE and cpCorr while offering a tighter runtime-accuracy
profile than GRIN.


                                                                      18
                                                       Sahdra et al.                                           A P REPRINT



For the combination of relational and predictive goals, both of which depend on recovering covariation (marginal
and conditional, respectively), the recommendation is unambiguous. The same trio, b BRITS, GRU-D, and GRIN,
dominates both axes. As above, we recommend the full-window strategy over win30.
For the combination of point-in-time and predictive goals (an accurate value today plus trustworthy conditional structure),
the tension is sharpest, since structure-preservation is volatile across datasets and users. Again, our recommendation
is best-available rather than most-reliable. BRITS, GRU-D, and GRIN perform similarly and show relative stability
across missingness rates, so we suggest differentiating between them by runtime-accuracy trade-off. Given that BRITS
has previously performed well on health records and biomedical sensor data [21], a domain athlete-specific data may
resemble, we lean toward recommending BRITS here.
These recommendations are collectively reflected in Figure 7. The remainder of this section presents the evidence
underlying them.

7.2     Evidence I: Characterising Missingness Mechanisms

The decision framework above hinges on first identifying which missingness mechanism is present in a dataset, since
this determines which branch of Figure 7 applies. This subsection establishes that athlete data exhibits genuinely
distinct missingness mechanisms worth distinguishing, and that doing so is non-trivial.
There are a variety of reasons why data can be missing, and the nature of that missingness in athlete-specific datasets
is itself informative [3, 34]. Missing data can be a strong behavioural signal in its own right [7]. Yet the nature of
missingness remains under-reported in the literature [7]. We build on prior work to characterise missingness across four
mechanisms: Missing Completely at Random (MCAR), Missing at Random (MAR), Missing Not at Random (MNAR),
and Block/Gap. The traditional MCAR/MAR/MNAR taxonomy is useful but not always the most meaningful and
useful categorisation [24], which is why HCI researchers have additionally focused on "gaps" as a distinct, practically
meaningful pattern [36]. Across the 231 users in our study, we observe a wide range of missingness patterns (tested
using methods outlined in Section 3.3,) with clear differences in downstream performance across all four mechanisms
(Section 7.3). There is heterogeneity in the manifestation of missingness patterns, and testing what mechanism is
present for an individual’s data can help our decision-making. This confirms that illuminating what kind of missingness
is present in a dataset is a necessary first step for choosing an imputation strategy suited to a researcher’s end goal, the
premise on which Figure 7 is built.

7.3     Evidence II: Accuracy and Structural Performance Across Methods (RQ1, RQ2)

Having established that missingness mechanisms are meaningfully distinct, we now turn to how imputation methods
perform against them, the evidence base for the per-goal recommendations in Section 7.1. We ask how imputation
accuracy varies across methods, mechanisms, and missing percentages (RQ1), and how well imputations preserve
multivariate and temporal structure under the same conditions (RQ2). The headline finding is that there is no one-
size-fits-all answer. While clear failure modes exist for athlete long-term, multi-modal, multivariate data, choosing the
best method is nuanced and goal-dependent. Point accuracy is strongly governed by missingness mechanism, while
multivariate-structure preservation is governed by both mechanism and the amount of missingness, consistent with
prior athlete-imputation studies [34, 3].

7.3.1    Why MICE fails so often.
MICE is the clear worst coverage-penalised performer on both point accuracy and multivariate structure, indicating
pervasive rather than mechanism-specific unreliability. Its high failure count quantifies how often it produced no valid,
evaluable reconstruction at all. This is unsurprising: MICE was designed for cross-sectional inference and pooled
multiple-imputation estimates, not long per-user time series, and is validated primarily under MCAR/MAR assumptions,
whereas our evaluation was strictly per-user and spanned varying mechanisms. Over 80% of logged MICE failures
were labelled ‘residual_na > 0‘, meaning MICE ran but left cells unimputed. Although it typically succeeded on most
columns, each failing chunk saw one or more target columns skipped entirely, whose original missing cells remained
NA (we deliberately did not implement a fallback to capture these failures across all imputation methods). Columns
were skipped for one of three reasons: (1) too little data to learn from (fewer than 3 non-missing values remaining in
the chunk); (2) the column appeared constant; or (3) failure on one column crashed the full chunk. Athletes often show
many such near-constant variables, as tracked daily habits can be highly consistent. More broadly, sport science data
exhibits non-linear patterns, substantial individual variability (visible in our forest plots, Figure 6 and Figure 32), and
temporal dependencies [34, 3]. These are the conditions under which MICE’s distributional assumptions are hard to
validate [34], so its failure here is not unexpected.


                                                            19
                                                      Sahdra et al.                                           A P REPRINT



Interestingly, the win30 windowing strategy reduces MICE’s failure rate and tames its error tail, suggesting its
breakdown is partly a function of context length. By constraining reconstruction to a bounded 30-day window, the
long-range extrapolation responsible for MICE’s most catastrophic misses is removed, at the cost of longer and more
variable runtime. Overall, these results point to clear practical limitations of applying MICE to long-term multivariate
athlete data, and motivates our recommendation against it for any of the three analytical goals (Section 7.1).

7.3.2   Comparing deep learning methods.
PAIN’s reliability on point accuracy, combined with its low computational cost and corroborating cpNMAE results,
suggests its strong cpNRMSE performance is genuine rather than masking rare catastrophic errors. This strengthens
the case for its point-accuracy reliability, underpinning its Goal 1 recommendation above. WGAIN-VAE, by contrast,
shows a combination of systematic under-imputation and a light error tail consistent with a conservative, mean-reverting
imputer. Its high computational cost is not offset by a corresponding accuracy advantage, which is why we exclude
it from all three goal recommendations. Our results partially support H1. Deep learning methods in our evaluation
do outperform MICE on both point accuracy and structure preservation across all four mechanisms, including the
hypothesised MAR, MNAR, and Block/Gap conditions. However, PAIN breaks the pattern under Block-Gap.
PAIN’s strong aggregate point accuracy does not hold uniformly across mechanisms, which is precisely why its Goal 2
(relational) recommendation above is conditional rather than unqualified. Under Block/Gap missingness, individual
users’ cpCorr swings between reasonable and near-zero (or negative) correlation depending on missingness percentage,
rather than degrading gradually. This is a pattern specific to PAIN among the methods examined. Read alongside
the variance-ratio collapse, PAIN’s Block/Gap failure is not confined to the pooled variance-ratio floor. We see even
at the individual-user level, correlation with ground truth becomes unstable and frequently indistinguishable from
noise. BRITS, GRU-D, and GRIN, by contrast, preserve user-level stability in both metrics throughout. This decouples
point accuracy from shape preservation specifically for PAIN under Block/Gap. Therefore, the method with the best
reconstruction accuracy is simultaneously the method with the most severe spread collapse, which is why BRITS,
GRU-D, and GRIN are the more broadly trustworthy choice wherever user-level stability in both point accuracy and
variable structure matters (Goals 2 and 3).
Beyond PAIN and WGAIN-VAE, BRITS, GRU-D, and GRIN emerge as serious competitors wherever preserving
distributional and multivariate structure jointly with point accuracy matters, even though their raw point accuracy
alone does not always match PAIN’s. This is the basis for their Goal 2/3 recommendations. Our finding on BRITS
coincides with Kazijevs and Samad (2023) [21], who applied BRITS to health records and biomedical sensor data,
a domain athlete datasets can resemble. Our results support their finding that BRITS performs well under MNAR
missingness (of which Block/Gap is a form), across time series lengths, datasets, and high missingness rates. We also
observe heterogeneity in how DL methods perform across individual users, but all achieve broadly satisfactory results,
supporting Liu et al. (2023) [26].

7.3.3   Limitations
Several limitations bound the generality of our conclusions. First, our MICE implementation pools its five completed
datasets into a single point estimate by averaging numeric values and taking the modal category, in order to support point-
wise comparison against ground truth across all methods on a common footing. This collapses the between-imputation
variance that is MICE’s principal statistical advantage. Although we note that MICE naturally captures the uncertainty in
its estimates through its multiple-imputation design, our evaluation pipeline discards this uncertainty to produce a single
completed dataset. This is a defensible simplification for our point-accuracy and structure-preservation comparisons,
but it means our results do not reflect MICE’s performance when used as intended, i.e., with its multiple imputations
retained and pooled downstream via Rubin’s rules rather than averaged upfront. Researchers specifically interested
in uncertainty quantification, rather than point reconstruction, should not treat our MICE results as representative of
the method’s full capability, and may find MICE more competitive under an evaluation protocol that preserves its
between-imputation variance.
Second, our two breakdown regimes constitute threats to validity for any goal that touches structure or dynamics.
Under MNAR/win30 every method spikes simultaneously across temporal-structure and distributional metrics at
70-80% missingness. Furthermore, Block/Gap collapses cpCorr to a narrow band around zero for all methods. Since
these are precisely the mechanisms most likely to arise in real wearable and self-report data, our goal-conditioned
recommendations should be read as conditional on missingness remaining below these extremes.
Our analysis operates at a daily aggregation level and does not examine minute-to-minute signals, so conclusions
about temporal-structure preservation pertain to day-scale rhythms rather than intra-day dynamics where reconstruction
difficulty and relative ordering of methods could differ. We also did not incorporate device wear time per day as an


                                                            20
                                                      Sahdra et al.                                           A P REPRINT



explicit covariate or masking driver. As non-wear itself is a primary generator of MNAR micro gaps in life-logging data,
excluding it means our synthetic mechanisms may understate the difficulty of real deployments. Future studies can build
on our daily aggregated pipeline to include daily non-wear time and develop a minute-to-minute pipeline. Our analysis
also assumed the DL methods to have implicitly captured lagged dependencies through their sequence modelling, which
is consistent with the full window strategy’s superior robustness. However, future studies can explicitly evaluate lagged
observations within the win30 imputation window as a means of anchoring inter-series modelling.
Although real datasets typically can exhibit multiple co-occurring missingness mechanisms, we imputed under one
mechanism at a time. Interactions between mechanisms with a single time-series are therefore not captured and the
observed method rankings may shift under mixed regimes. Future work can explore these interactions explicitly to
supplement our work. A wider more systematically varied set of missingness patterns would be needed to bootstrap and
stress-test our findings. We identify this as the most important direction for future work before the goal-conditioned
recommendations can be treated as broadly generalisable.

8   Conclusion
Missing data in wearable and life-logging datasets from athletes has received comparatively little attention in HCI,
despite this population’s distinctive behavioural, physiological, and goal-driven data patterns. We characterised
missingness across 231 users under four mechanisms and systematically benchmarked six imputation methods, spanning
statistical and deep learning approaches, on point accuracy, multivariate structure, temporal structure, and distributional
shape.
No single method dominates across all analytical goals, mechanisms, and missingness levels. PAIN is the strongest
choice for point-wise reconstruction under most conditions, while BRITS, GRU-D, and GRIN are more broadly
dependable wherever multivariate or temporal structure must be preserved alongside accuracy, particularly under
Block/Gap and at higher missingness rates. We recommend the full window strategy over win30, and caution against
MNAR/win30 regimes specifically, where reconstruction quality degrades sharply across all methods.
These findings contribute a practical, goal-conditioned decision framework for researchers handling missing data in
long-term, multivariate, athlete wearable and life-logging datasets, an area where such guidance has been largely absent,
and demonstrate the value of evaluating imputation quality along multiple complementary axes rather than accuracy
alone. As noted in our limitations (Section 7.3.3), these recommendations are bounded by the missingness patterns
we simulated, our daily aggregation level, and the assumption of single, non-interacting mechanisms. Extending this
work to mixed missingness regimes, finer-grained temporal resolutions, and explicit non-wear modelling are the most
important next steps toward generalising these findings for real-world SportHCI deployment.

References
 [1] M. J. Azur, E. A. Stuart, C. Frangakis, and P. J. Leaf. Multiple imputation by chained equations: what is it and
     how does it work? International Journal of Methods in Psychiatric Research, 20(1):40–49, 2011.
 [2] C. Bailey. Longitudinal Monitoring of Athletes: Statistical Issues and Best Practices. Journal of Science in Sport
     and Exercise, 1:217–227, 2019.
 [3] L. C. Benson, C. Stilling, O. B. A. Owoeye, and C. A. Emery. Evaluating methods for imputing missing data from
     longitudinal monitoring of athlete workload. Journal of Sports Science and Medicine, 20(2):188–196, 2021.
 [4] Frank Bentley, Konrad Tollmar, Peter Stephenson, Laura Levy, Brian Jones, Scott Robertson, Ed Price, Richard
     Catrambone, and Jeff Wilson. Health mashups: Presenting statistical patterns between wellbeing data and context
     in natural language to promote behavior change. ACM Trans. Comput.-Hum. Interact., 20(5), November 2013.
 [5] Wei Cao, Dong Wang, Jian Li, Hao Zhou, Yitan Li, and Lei Li. Brits: bidirectional recurrent imputation for time
     series. In Proceedings of the 32nd International Conference on Neural Information Processing Systems, NIPS’18,
     page 6776–6786, 2018.
 [6] Zhengping Che, Sanjay Purushotham, Kyunghyun Cho, David Sontag, and Yan Liu. Recurrent neural networks
     for multivariate time series with missing values. Scientific Reports, 8(1):6085, 2018.
 [7] Akshat Choube, Sohini Bhattacharya, Rahul Majethia, Jiachen Li, Vedant Das Swain, and Varun Mishra. Imputa-
     tion matters: A deeper look into an overlooked step in longitudinal health and behavior sensing research. Proc.
     ACM Interact. Mob. Wearable Ubiquitous Technol., 9(4), December 2025.
 [8] Andrea Cini, Ivan Marisca, and Cesare Alippi. Filling the g_ap_s: Multivariate time series imputation by graph
     neural networks, 2022.


                                                            21
                                                     Sahdra et al.                                         A P REPRINT



 [9] Anurika Priyanjali De Silva, Margarita Moreno-Betancur, Alysha Madhu De Livera, Katherine Jane Lee, and
     Julie Anne Simpson. A comparison of multiple imputation methods for handling missing values in longitudinal
     data in the presence of a time-varying covariate with a non-linear association with time: a simulation study. BMC
     Medical Research Methodology, 17(1):114, 07 2017.
[10] Joseph R. Dettori, Daniel C. Norvell, and Jens R. Chapman. The sin of missing data: Is all forgiven by way of
     imputation? Global Spine Journal, 8(8):892–894, 2018.
[11] Don Samitha Elvitigala, Armağan Karahanoğlu, Andrii Matviienko, Laia Turmo Vidal, Dees Postma, Michael D
     Jones, Maria F. Montoya, Daniel Harrison, Lars Elbæk, Florian Daiber, Lisa Anneke Burr, Rakesh Patibanda,
     Paolo Buono, Perttu Hämäläinen, Robby Van Delden, Regina Bernhaupt, Xipei Ren, Vincent Van Rheden, Fabio
     Zambetta, Elise Van Den Hoven, Carine Lallemand, Dennis Reidsma, and Florian (Floyd) Mueller. Grand
     Challenges in SportsHCI. In Proceedings of the CHI Conference on Human Factors in Computing Systems, pages
     1–20, Honolulu HI USA, May 2024. ACM.
[12] Daniel A. Epstein, Clara Caldeira, Mayara Costa Figueiredo, Xi Lu, Lucas M. Silva, Lucretia Williams, Jong Ho
     Lee, Qingyang Li, Simran Ahuja, Qiuer Chen, Payam Dowlatyari, Craig Hilby, Sazeda Sultana, Elizabeth V.
     Eikey, and Yunan Chen. Mapping and taking stock of the personal informatics literature. Proc. ACM Interact.
     Mob. Wearable Ubiquitous Technol., 4(4), December 2020.
[13] Daniel A. Epstein, Parisa Eslambolchilar, Judy Kay, Jochen Meyer, and Sean A. Munson. Opportunities and
     Challenges for Long-Term Tracking. In Evangelos Karapanos, Jens Gerken, Jesper Kjeldskov, and Mikael B.
     Skov, editors, Advances in Longitudinal HCI Research, pages 177–206. Springer International Publishing, Cham,
     2021. Series Title: Human–Computer Interaction Series.
[14] Juliana Exel and Peter Dabnichki. Precision Sports Science: What Is Next for Data Analytics for Athlete
     Performance and Well-Being Optimization? Applied Sciences, 14(8):3361, April 2024.
[15] Thomas Fritz, Elaine M. Huang, Gail C. Murphy, and Thomas Zimmermann. Persuasive technology in the real
     world: a study of long-term use of activity sensing devices for fitness. In Proceedings of the SIGCHI Conference
     on Human Factors in Computing Systems, CHI ’14, page 487–496, New York, NY, USA, 2014. Association for
     Computing Machinery.
[16] Brenna Gomer and Ke-Hai Yuan. A realistic evaluation of methods for handling missing data when there is a
     mixture of mcar, mar, and mnar mechanisms in the same dataset. Multivariate Behavioral Research, 58:988–1013,
     2023.
[17] Justin Hilliard. Nfl daily performance dataset (justin hilliard). Kaggle, 2024. Accessed: 2026-04-13.
[18] Andrew Jin. Whoop dataset. Kaggle, 2025. Accessed: 2026-04-13.
[19] Harsh Joshi, Rajeshwari Mistri, Manasi Mali, Nachiket Kapure, and Parul Kumari. Precision adaptive imputation
     network : An unified technique for mixed datasets, 2025.
[20] K. P. Junaid, Tanvi Kiran, Madhu Gupta, Kamal Kishore, and Sujata Siwatch. How much missing data is too
     much to impute for longitudinal health indicators? A preliminary guideline for the choice of the extent of missing
     proportion to impute with multiple imputation by chained equations. Population Health Metrics, 23(1):2, Feb
     2025. PMID: 39893454; PMCID: PMC11787761.
[21] Maksims Kazijevs and Manar D. Samad. Deep imputation of missing values in time series health data: A review
     with benchmarking. Journal of Biomedical Informatics, 144:104440, 2023.
[22] Elisabeth T. Kersten-van Dijk, Joyce H. D. M. Westerink, Femke Beute, and Wijnand A. IJsselsteijn. Personal in-
     formatics, self-insight, and behavior change: A critical review of current literature. Human–Computer Interaction,
     32(5–6):268–296, 2017.
[23] Florian Künzler, Varun Mishra, Jan-Niklas Kramer, David Kotz, Elgar Fleisch, and Tobias Kowatsch. Exploring
     the state-of-receptivity for mhealth interventions. Proc. ACM Interact. Mob. Wearable Ubiquitous Technol., 3(4),
     September 2020.
[24] Katherine J Lee, John B Carlin, Julie A Simpson, and Margarita Moreno-Betancur. Assumptions and analysis
     planning in studies with missing data in multiple variables: moving beyond the mcar/mar/mnar classification.
     International Journal of Epidemiology, 52(4):1268–1275, 08 2023.
[25] Roderick J. A. Little. A test of missing completely at random for multivariate data with missing values. Journal of
     the American Statistical Association, 83(404):1198–1202, 1988.
[26] Mingxuan Liu, Siqi Li, Han Yuan, Marcus Eng Hock Ong, Yilin Ning, Feng Xie, Seyed Ehsan Saffari, Yuqing
     Shang, Victor Volovici, Bibhas Chakraborty, and Nan Liu. Handling missing values in healthcare data: A
     systematic review of deep learning-based imputation techniques. Artificial Intelligence in Medicine, 142:102587,
     2023.


                                                          22
                                                     Sahdra et al.                                         A P REPRINT



[27] Jochen Meyer, Merlin Wasmann, Wilko Heuten, Abdallah El Ali, and Susanne C.J. Boll. Identification and
     classification of usage patterns in long-term activity tracking. In Proceedings of the 2017 CHI Conference on
     Human Factors in Computing Systems, CHI ’17, page 667–678, New York, NY, USA, 2017. Association for
     Computing Machinery.
[28] Cise Midoglu et al. A large-scale multivariate soccer athlete health, performance, and position monitoring dataset.
     Scientific Data, 11(1):553, 2024.
[29] Möbius. Fitbit fitness tracker data. Kaggle, 2024. Accessed: 2026-04-13.
[30] Amon Rapp and Lia Tirabeni. Self-tracking while doing sport: Comfort, motivation, attention and lifestyle of
     athletes using personal informatics tools. International Journal of Human-Computer Studies, 140:102434, August
     2020.
[31] Wenhui Ren, Zheng Liu, Yanqiu Wu, Zhilong Zhang, Shenda Hong, Huixin Liu, and on behalf of the Missing
     Data in Electronic health Records (MINDER) Group. Moving beyond medical statistics: A systematic review on
     missing data handling in electronic health records. Health Data Science, 4, 2024.
[32] Donald B Rubin. Inference and missing data. Biometrika, 63(3):581–592, 1976.
[33] Baljinder K. Sahdra, Mercedes G. Woolley, Cristóbal Hernández, William Li, Steven C. Hayes, Joseph Ciarrochi,
     Michael P. Twohig, and Micheal E. Levin. Time series machine learning for idionomic process-based treatment
     planning: A tutorial on tsboruta. Journal of Contextual Behavioral Science, 40:100983, April 2026.
[34] Srishti U. Sharma, Hetav Raval, Vishal Barot, Srikrishnan Divakaran, Tolga Kaya, Christopher Taber, and Mehul S.
     Raval. Data-driven imputation for cohort studies using collegiate basketball data. SN Computer Science, 7(4):288,
     2026.
[35] Lie Ming Tang and Judy Kay. Harnessing long term physical activity data—how long-term trackers use data
     and how an adherence-based interface supports new insights. Proc. ACM Interact. Mob. Wearable Ubiquitous
     Technol., 1(2), June 2017.
[36] Lie Ming Tang, Jochen Meyer, Daniel A. Epstein, Kevin Bragg, Lina Engelen, Adrian Bauman, and Judy
     Kay. Defining adherence: Making sense of physical activity tracker data. Proc. ACM Interact. Mob. Wearable
     Ubiquitous Technol., 2(1), March 2018.
[37] Matthew S. Tenan. Missing data in sport science: A didactic example using wearables in american football. Sports
     Medicine, 53:1109–1116, 2023.
[38] Vajira Thambawita, Steven Alexander Hicks, Hanna Borgli, Håkon Kvale Stensland, Debesh Jha, Martin Kristoffer
     Svensen, Svein-Arne Pettersen, Dag Johansen, Håvard Dagenborg Johansen, Susann Dahl Pettersen, Simon Nord-
     vang, Sigurd Pedersen, Anders Gjerdrum, Tor-Morten Grønli, Per Morten Fredriksen, Ragnhild Eg, Kjeld Hansen,
     Siri Fagernes, Christine Claudi, Andreas Biørn-Hansen, Duc Tien Dang Nguyen, Tomas Kupka, Hugo Lewi
     Hammer, Ramesh Jain, Michael Alexander Riegler, and Pål Halvorsen. Pmdata: A sports logging dataset. In
     Proceedings of the 11th ACM Multimedia Systems Conference, MMSys ’20, page 231–236, New York, NY, USA,
     2020. Association for Computing Machinery.
[39] The International Football Association Board. Law 4 - the players’ equipment. https://www.theifab.com/
     laws/latest/the-players-equipment/, 2026. Accessed: 2026-10-26.
[40] Bugra Varol, Imran Kurt Omurlu, and Mevlut Ture. Review of simulation studies evaluating imputation methods
     in high-dimensional datasets. WIREs Computational Statistics, 17(3), September 2025.
[41] Kennet Khang Vuong. Pmsys: a monitoring system for sports athlete load, wellness & injury monitoring. 2015.
[42] Yunsheng Wang, Xinghan Xu, Lei Hu, Jianwei Liu, Xiaohui Yan, and Weijie Ren. Continuous imputation of
     missing values in time series via a new wgain-vae model. Physica A: Statistical Mechanics and its Applications,
     647:129914, 2024.
[43] WHOOP. Whoop api docs: Whoop for developers, 2025.
[44] WHOOP. How whoop works: Health monitoring, sleep tracking, recovery insights, 2026.
[45] Xuhai Xu, Prerna Chikersal, Janine M. Dutcher, Yasaman S. Sefidgar, Woosuk Seo, Michael J. Tumminia,
     Daniella K. Villalba, Sheldon Cohen, Kasey G. Creswell, J. David Creswell, Afsaneh Doryab, Paula S. Nurius,
     Eve Riskin, Anind K. Dey, and Jennifer Mankoff. Leveraging collaborative-filtering for personalized behavior
     modeling: A case study of depression detection among college students. Proc. ACM Interact. Mob. Wearable
     Ubiquitous Technol., 5(1), March 2021.
[46] Sofia Yfantidou, Pavlos Sermpezis, and Athena Vakali. 14 years of self-tracking technology for mhealth—literature
     review: Lessons learned and the past self framework. ACM Trans. Comput. Healthcare, 4(3), September 2023.


                                                          23
                                                      Sahdra et al.                                         A P REPRINT



[47] Jinsung Yoon, James Jordon, and Mihaela van der Schaar. GAIN: Missing data imputation using generative
     adversarial nets. In Jennifer Dy and Andreas Krause, editors, Proceedings of the 35th International Conference on
     Machine Learning, volume 80 of Proceedings of Machine Learning Research, pages 5689–5698. PMLR, 10–15
     Jul 2018.
[48] Samira Zahmatkesh and Philipp Zech. Spatio-temporal missing data imputation: A systematic literature review
     with a focus on statistical and machine learning-based approaches. ACM Comput. Surv., 58(10), apr 2026.
[49] Chong Zhao, Maria Cardei, Matthew Clark, Runze Yan, and Afsaneh Doryab. Biobehavioral rhythms in everyday
     life: Data and models for capturing cyclic behavior in naturalistic settings. In Proceedings of the ACM on
     Interactive, Mobile, Wearable and Ubiquitous Technologies, volume 9. Association for Computing Machinery,
     2025.


A     Methodological Transparency & Reproducibility Appendix (META)
A.1     Extended Dataset Descriptions

This appendix provides full descriptive detail for each of the 7 datasets summarised in Section 3.2.3, supporting
reproducibility and dataset-selection transparency.

A.1.1    Complete-Case Extraction Parameters
We computed each user’s complete subset by first enforcing consecutive days and then identifying the longest continuous
observation window with minimal missingness (≤5%) across all target variables. This is a necessary methodological
choice; we acknowledge that selecting such windows may limit generalisation to the rest of the athlete population. For
larger datasets with longer timelines (e.g., Human Rhythms), a greater than 60-day window was applied, and users
with less than 60 days were excluded. For shorter few-person datasets (e.g., Public WHOOP), shorter timelines were
accepted to make the most of the data at hand and to provide edge cases. Up to 5% residual missingness with gaps of at
most one day is tolerated. A type-aware imputation is applied for these minimal gaps: numeric columns use the median,
logical columns use the modal false/true value, and categorical columns use the mode. These complete subsets define
the simulation ground truth used throughout the study.

A.1.2    SoccerMon
The SoccerMon dataset [28] is a large-scale longitudinal sports science public dataset focused on elite women’s football
(soccer). The dataset combines two main categories of athlete-monitoring data collected from 77 professional female
players in the Norwegian top division: (1) subjective self-report data such as wellness and training load questionnaires
collected via PmSys [41], (2) objective sensor-based data such as GPS tracking and other load indicators. The raw
dataset has over nine thousand parquet and csv files containing minute level data from sensor-based data and daily level
data for subjective data. For this study, we aggregated all data to the daily level, which provided 38,000+ observations,
across all individuals over 2 seasons (51.45% missing data). The complete subset extract retained 45 out of the 77
individuals.

A.1.3    Human Rhythms
The Human Rhythms Dataset [49] is a longitudinal public dataset designed to study human behavioural rhythms and
physiological patterns. It consists of Fitbit, mobile, and daily survey data collected from 166 college students between
August 2021 and January 2023. 1 participant was reported to be an elite athlete (NCAA), and the dataset could contain
unreported student-athletes (non-NCAA). This dataset captures multivariate metrics such as activity levels, sleep, and
mood. The purpose of this dataset is unique as it focuses on circadian and ultradian rhythms, providing temporal
perspective on human behaviour. The dataset also includes contextual metrics, such as COVID data, weather, and
university events. For this study, we retain the Fitbit and survey streams across 166 processed participants with 36,000+
observations (29.33% missing data). The complete subset yielded 146 users.

A.1.4    Fitbit
Fitbit is one of the most widely used consumer-grade wearables, offering a broad range of health and fitness tracking
features. Fitbit devices measure metrics such as steps, heart rate, calories burned, and sleep patterns, making them
popular for both general health monitoring and research applications. We use a public Fitbit dataset available on Kaggle
[29]. 23 of the 33 users had sleep-tracking data, with a total of 600+ observations across 31 days and 31 variables


                                                           24
                                                       Sahdra et al.                                           A P REPRINT



(19.54% missing data). The complete subset extracted 23 users. This dataset provides an edge case scenario of less than
30 days of data of wearable users. We are unsure whether these users are athletesfo which could be contributing to this
datasets "outlier" like results where MICE and other methods deviated most. Nevertheless, these are daily wearable
users. Combining such a dataset in this study enables evaluation of generalisability across different wearable devices,
time frames, and a wider, heterogeneous consumer sample.

A.1.5    PMData
PMData is a public sport-logging dataset of 16 persons spanning five months, that integrates data from multiple
life-logging sources, including Fitbit wearables, a sports logging app, and Google Forms [38]. It is designed to support
research on personal health and behaviour, offering a rich, multivariate dataset with diverse data streams. PMData
includes metrics such as physical activity, injuries, sleep, heart rate, nutrition, and mood. It is uniquely suited to
studying the interplay between physiological and contextual factors. The multi-source nature of PMData introduces
heterogeneous resolutions and missingness patterns, which are critical for stress-testing imputation and network analysis
robustness. The raw dataset has 63 variables with 2000+ observations across 152 days (30.16% missing days). The
complete subset extracted retained 14 users.

A.1.6    Personal WHOOP
The first author’s personal WHOOP data, collected over two years, provides a single-user longitudinal dataset with 500+
days of history and 16 naturally occurring data gaps. WHOOP is a wearable device designed for athletes and fitness
enthusiasts, offering advanced tracking of physiological and behavioural metrics. Unlike general-purpose wearables
like Fitbit or Apple Watch, WHOOP focuses on optimising human performance and recovery by providing detailed
insights into physiological cycles [44]. Physiological cycles are defined as a Sleep-to-Sleep cycle to provide recovery
insights based on natural sleep patterns rather than a fixed 24-hour clock. WHOOP collects measures such as heart rate
variability (HRV), sleep stages, strain, and recovery scores. The device also allows users to log behavioural data daily
on the app interface journal feature, such as alcohol consumption, stress levels, nutrition, and subjective recovery [44].
WHOOP is particularly suitable for multivariate analysis. These features make WHOOP highly relevant for this study,
as it provides both physiological and behavioural data streams that are prone to missingness.
Physiological and activity data were extracted programmatically using the official WHOOP Developer API v2 with
OAuth 2.0 authentication [43], which provides authenticated, granular access to the cycles, sleep, recovery, and workout
endpoints. The resulting dataset was structured at the daily (cycle) level, with each row containing aligned sleep,
recovery, and activity variables. The richness and longitudinal span of this dataset (700+ days with 500+ observed)
enabled extraction of a clean complete-case window over 181 days.

A.1.7    WHOOP Dataset
The Public WHOOP Dataset [18] is a Kaggle-hosted, real-world, single-user WHOOP export that includes WHOOP
derived physiological metrics alongside contextual annotations entered by the user. The raw dataset downloaded from
Kaggle had 53 observations across 51 days. This dataset is another edge-case that is less than 60-days.

A.1.8    NFL Athlete Dataset
This long-term public dataset, available on Kaggle [17], contains daily performance data for a National Football League
(NFL) player. NFL is a premier professional American football league in the United States. This player self-published
their data and integrates data from WHOOP, Polar, Oura Ring, and MyFitnessPal. The dataset including metrics for
sleep, nutrition, training intensity, and recovery, providing a detailed view of the athlete’s physiological and performance
trends. A complete-case subset was extracted spanning 94 days. This dataset is particularly valuable for studying the
application of wearable data analytics in high-performance sports.

A.2     Mechanism Detection Pipeline

This appendix provides the full statistical procedure underlying the staged diagnostic pipeline summarised in Section 3.3,
used to characterise naturally occurring missingness mechanisms (MCAR, MAR, MNAR, Block/Gap) in each of our
seven datasets.

A.2.1    MCAR testing
We first test MCAR using a pattern-wise chi-square test, binning each variable into terciles and testing independence
between missingness pattern and bin, with Bonferroni correction across variables. MCAR is rejected at p<0.05,


                                                            25
                                                      Sahdra et al.                                         A P REPRINT



consistent with Little’s (1988) [25] classic formulation, under which missingness is unrelated to observed or unobserved
values. Since such tests are sample-size sensitive, we gate the result behind a power heuristic: it is trusted only when
n≥500, at least three distinct missingness patterns exist, and minimum expected cell count ≥5. We additionally compute
co-missingness (correlation among variables’ missingness indicators), flagging |r|>0.3 as possible device-level dropout
rather than genuine MAR.

A.2.2    MAR testing
When MCAR is rejected, we probe for MAR by fitting logistic regressions to predict each variable’s missingness from
other variables, synthesised temporal predictors, and user-supplied covariates, using missing-indicator augmentation.
Benjamini-Hochberg (BH)–adjusted likelihood-ratio p-values below the alpha flag a MAR signal is used to operationalise
missingness’ dependence on observed data.

A.2.3    MNAR testing
We assess MNAR via two tests: (1) a long-run signal (run-length encoding of missing streaks, flagged when ≥50% of
missing days fall in runs ≥5), and (2) a tail-clustering test, evaluated against a 200-shuffle permutation null with BH
correction, checking whether values adjacent to gaps disproportionately fall in distribution extremes (bottom/top 10%).
This aims to capture missingness that could be dependent on the unobserved value itself.

A.2.4    Verdict assignment
A single verdict is assigned via a priority ladder: unavailable MCAR test → "Undetermined (test unavailable)"; MCAR
not rejected with adequate power → "MCAR (not rejected)"; MCAR not rejected but underpowered → "Undetermined
(low power)". If MCAR is rejected, the pipeline escalates through tail-clustering, combined MAR+MNAR, long-
run MNAR, MAR, and finally co-missingness. Crucially, these mechanisms cannot be identified from data alone.
Distinguishing MAR from MNAR requires knowledge of why values are missing. We use "Undetermined" liberally
rather than over-claiming a mechanism the data cannot adjudicate.

A.3     Simulated Missingness Construction

This appendix provides the full construction procedure underlying the four simulated missingness mechanisms sum-
marised in Section 3.4.
To ensure MAR and MNAR mechanisms depart from pure randomness in a controlled way, we condition on three
signals. First, a weekend logical flag marks Saturday and Sunday. Second, one or two auxiliary variables are chosen as
the highest-variance numeric columns or the most balanced categorical ones, paired with a flag marking rows where
the auxiliary is "high" (top quartile for numeric variables, modal category otherwise). Third, per-target self-low and
self-high flags mark each variable’s own low values (bottom quartile) and high values (top quartile). Logical or binary
columns use TRUE/FALSE or 0/1, and categorical columns distinguish rare from common categories.
For every dataset, missingness is injected at proportions of 10, 20, 30, 40, 50, 60, 70, and 80%, each using a fixed seed
for reproducibility (SEED_MCAR = 2121, SEED_MAR = 4242, SEED_MNAR = 6363, SEED_BLOCK = 8484, offset
by the proportion). The four mechanisms are implemented as follows:
MCAR: We compute the total number of cells to mask (rows × targets × proportion), then sample that many cell
positions uniformly at random across the target matrix and set them to NA, so that missingness is unrelated to any
values.
MAR: We build a weight matrix in which weekend rows receive weight 3 across all targets, and rows where an auxiliary
variable is "high" receive weight 2 on the other targets. These weights are scaled so the overall NA fraction reaches
the target proportion (capped at 0.95 per cell), and a per-column draw then determines which cells become NA. The
pipeline logs the resulting weekend-versus-weekday missing rates to confirm the intended dependence on observed
values.
MNAR: The weight rules key off each variable’s own values. A row receives weight 4 where that variable falls in its
low range (self-low) and weight 3 where it falls in its high range (self-high), so that extreme values are preferentially
deleted, inducing missingness that depends on an artificial "unobserved" value.
Block/Gap: These represent realistic contiguous gaps in the data (e.g., a device not being worn). Operating per user,
we convert the target proportion into a number of missing days, partition these into blocks whose size scales with
severity (3 days at ≤20%, 5 at ≤40%, 7 at ≤60%, else 10), and use a rolling-sum scan to place non-overlapping blocks
at random valid positions, blanking all target variables across the contiguous rows. More specifically, for each block


                                                           26
                                                      Sahdra et al.                                          A P REPRINT



size b (processed largest-first), we compute a length-b moving sum over a binary occupancy vector, select all window
positions with zero sum (i.e., fully free), sample one uniformly at random, and mark it occupied before placing the next
block, blanking all target variables across the resulting contiguous rows.
For each of the 8 proportions × 4 mechanisms, we write the amputated CSV (e.g., MAR_30pct.csv) and record both
the realised overall NA rate (actual versus target percentage) and per-variable NA rates. Each dataset directory thus
receives 32 amputated files, 4 metadata files, and cross-dataset summaries.

A.4     Imputation Method Implementation Details

This appendix provides full implementation detail for each of the six imputation methods summarised in Section 4,
supporting reproducibility.

A.4.1    Window strategies and shared infrastructure
The defining architectural principle is that every method imputes one user at a time, so parallelism occurs across users
(N_CORES=16) and never within a user. For each amputated file, the data are split by the user column, each user’s
rows are date-sorted, and each user is dispatched to a worker. MICE runs in pure R, whereas the deep-learning (DL)
workers are called through Python. The full pipeline runs twice, governed by two window strategies. The first, "full,"
imputes the entire per-user, date-sorted sequence at once, providing the richest retrospective context. This strategy
requires users to have at least 10 rows. The second, "win30," partitions each user into tumbling 30-day windows,
imputes each window independently, and re-binds the results. Users with fewer than 30 rows are skipped and logged.
The win30 strategy serves as a sensitivity and robustness check against non-stationarity. A user’s per-chunk results are
aggregated into an overall status of "ok," "partial," or "failed," depending on how many chunks succeeded. Notably,
there is no mean or median fallback. If imputation fails for a user, that user is skipped and logged rather than crudely
filled, preserving the integrity of the downstream ground-truth comparison. Before any model runs, several floors are
enforced: a minimum of 10 user rows for MICE and DL methods, and a minimum of 3 observed values per column. A
chunk containing no missing cells is returned unchanged.

A.4.2    MICE
Multiple Imputation by Chained Equations (MICE) [1] fills missing values by repeatedly predicting each incomplete
variable from the others. For each variable with missing data, a model is built from observed data, and missing values
are filled by drawing from that model’s predictions. This cycle repeats across all variables several times, producing
several different "complete" versions of the dataset for analysis. Because MICE generates several predictions per
missing value rather than one, it naturally captures the uncertainty its estimates. It works best when data are Missing at
Random (MAR), meaning the chance a value is missing can be explained by other observed variables, making it widely
used in health and wearable studies. However, because it assumes MAR, MICE does not naturally account for time. It
can be adapted using lagged variables (past values as predictors), but this raises computational cost for large datasets,
and the standard version still treats each time point independently, leaving time-based patterns unmodelled, precisely
one assumption this study examines.
In our implementation, MICE generates 5 complete datasets over 10 cycles, seeded at 2121 for reproducibility. A
setup pass automatically selects a prediction method and predictor columns for each variable. We assign methods by
column type: predictive mean matching (filling a value using an observed value from a similar data point) for numeric
columns; logistic regression for true/false columns; and polytomous regression (predicting one of several categories)
for multi-category columns. Each target column uses at most 20 predictors, or one-third of available rows, whichever
is smaller. The five completed datasets are then combined: numeric values are averaged, and categorical values are
set to the most common prediction, with true/false columns temporarily treated as categories during this step. If any
value remains missing, that portion is marked failed. This mirrors the standard MICE approach of generating several
completed datasets and pooling them into one.

A.4.3    BRITS
Bidirectional Recurrent Imputation for Time Series (BRITS) is a deep learning method using a neural network that reads
sequences both forwards and backwards in time to fill missing values [5]. It treats each missing value as something to be
learned and refined, using patterns from both earlier and later time points to reconstruct what is missing. BRITS should
perform well under MCAR, MAR, and block missingness and has also been applied to MNAR settings. The original
paper tested it on healthcare and physical-activity data, suggesting suitability for wearable data. It captures complex
patterns across time and variables, but requires substantial data and is harder to interpret and more computationally


                                                           27
                                                       Sahdra et al.                                            A P REPRINT



demanding than MICE. To handle mixed data types, BRITS requires manual preparation: logical and categorical
variables are coerced to factors or numeric values.
In our implementation, two recurrent network units (one reading forward, one backward) each maintain an internal
"memory" that fades at a rate learned by the model, based on the time gap since the last observation. At each step, the
model makes two estimates (from recent history and from other variables) and blends them using a learned weighting.
Originally observed values are always kept as-is. The model is trained to minimise errors on observed values across
both estimates, while encouraging the forward and backward readings to agree.

A.4.4   GRU-D
GRU-D extends a standard recurrent neural network with built-in decay mechanisms modelling how the influence of
past observations fades as time gaps grow [6]. As with BRITS, mixed data types require the same manual preparation.
It fills each missing value using a weighted mix of the last observed value and the overall column average, combined
with a learned temporal pattern and decay rates for both inputs and memory, accounting for irregular timing. GRU-D
explicitly models time gaps through masking, and is described as an "effective solution to characterise the missing
patterns of not missing-completely-at-random time series data with masking and time interval" [6]. While the original
paper does not explicitly test it where missingness depends on the unobserved value itself, it treats missingness patterns
as meaningful and learns decay rates from data rather than fixing them in advance [6]. Our implementation uses a
single forward-reading network with two decay mechanisms, one pulling missing inputs toward the column average,
and one decaying the model’s memory. A final linear model predicts values from this decayed memory, trained only on
observed values.

A.4.5   WGAIN-VAE
Our adversarial imputer builds on GAIN, which uses two competing neural networks: a generator that fills missing
values, and a discriminator that tries to detect which values were originally missing [47, 42]. This competition, guided
by a "hint" mechanism giving partial information about which values were missing, pushes the generator toward
realistic imputations. The same manual preparation of categorical variables applies. The original GAIN paper found it
outperforms MICE under MNAR conditions [47, 42]. However, standard GAIN is not designed for temporal modelling
and may underperform time-aware models under MNAR especially.
Our implementation combines a Wasserstein-GAN (a more stable training variant) with a variational autoencoder (VAE,
a model that learns compressed data representations) [42]. The generator reads sequences using a recurrent VAE, paired
with a bidirectional critic network trained using a hint mask, a gradient penalty for stability, and three critic updates per
generator update. Data are rescaled to 0–1 per column, the critic step is skipped for very short sequences (fewer than 8
points), and at prediction time the model averages 10 stochastic samples with the deterministic pass.

A.4.6   PAIN
PAIN is a recent method designed to adapt dynamically to different data types, distributions, and missingness patterns
[19]. It uses a three-step process: (a) combining statistical methods, random forests (an ensemble of decision trees),
and autoencoders (neural networks learning compressed data representations); (b) adaptively weighting these methods
based on data characteristics; and (c) refining imputed values to reduce noise. PAIN supports mixed data types and
shows promise for health data, though further research is needed.
Our implementation is layered and each layer completion is tracked. The first layer blends column mean, median, and
nearest-neighbour KNN imputation, weighted by missingness severity. The second uses an iterative random forest,
imputing one column at a time from least-to-most missing, for up to three passes. A de-noising autoencoder then refines
and averages with this output. The final layer clips values to a realistic range (based on observed 5th–95th percentiles,
extended for natural spread) and rounds whole-number columns.

A.4.7   GRIN
GRIN combines a recurrent network for time patterns with a graph neural network (a model learning relationships
between variables as a network) for variable relationships, learning representations via bidirectional message passing
[8]. This enables imputation in datasets with multiple interdependent variables and shows strong potential for wearable
health data. Although GRIN makes no assumptions about the distribution of missing values, it assumes underlying
patterns remain stable over time [8], narrowing its effective use toward MAR scenarios.
Our implementation learns a network of relationships between variables, passing information using the model’s best
current estimate rather than placeholder zeros, so artificial zeros never distort learned relationships. A recurrent unit


                                                             28
                                                        Sahdra et al.                                       A P REPRINT



carries information through time, and the final prediction combines this temporal information with variable-relationship
information.

A.4.8    Shared Training Infrastructure and Post-Processing
All models are organised into per-user batches. The three recurrent models (BRITS, GRU-D, GRIN) share further
common infrastructure: time gaps are calculated in both directions, and training uses gradient clipping (preventing
unstable updates), a 300-second time limit, and early stopping after 10 attempts without improvement. A common
post-processing routine applies to all deep learning methods: numeric values are standardised before processing and
converted back afterward, and results are constrained within a reasonable range of observed data. Together, these
conventions ensure all six methods are evaluated under a uniform, reproducible protocol, isolating differences in
imputation quality to the methods themselves.

B     Evaluation Metric Derivations
B.1     Point-level reconstruction accuracy

NRMSE. To account for survivorship bias, we propose a coverage-penalised NRMSE (cpNRMSE). Standard NRMSE
is averaged only over users actually evaluated; this silently drops users with shorter series or sparse columns where the
method fails, which can produce a deceptively low NRMSE. cpNRMSE deflates apparent accuracy by the coverage
achieved:

                                                              n_users_eval
                                              coverage =                                                              (1)
                                                            n_users_attempted

                                                                     NRMSE
                                                 cpNRMSE =                                                            (2)
                                                                     coverage

cpNRMSE was preferred over a weighted F-score or a 1 − NRMSE recasting to preserve interpretability and avoid
unnecessary assumptions. At full coverage, cpNRMSE = NRMSE, remaining on the same scale and directly comparable.
It diverges only as coverage drops; at coverage = 0, both NRMSE and cpNRMSE are coded NA. cpNRMSE strictly
increases as error rises and as coverage falls—the intended ranking behaviour, where low error on everyone outranks
low error on an easy subset. Dividing by coverage is the natural first-order selection-bias correction and requires no
arbitrary rescaling into (0, 1), which an F-style harmonic mean would force.
For each missingness-percentage × method combination, each dataset’s contribution to the pooled failure rate is:
                                                                          .X
                                     contributiond = 100 × nfailed
                                                            d                   nattempted
                                                                                 d                                    (3)
                                                                            d

Using a common denominator means segments stack to a value with real interpretation (the overall pooled failure rate),
and larger datasets contribute proportionally to how many users they represent.
Pooled NRMSE is the coverage-weighted (by neval
                                           d ) mean of per-dataset NRMSEs—standard sample-size weighting for
combining group means—and pooled coverage is total evaluated ÷ total attempted:
                                                                                       ,P
                                               NRMSEpool                 eval
                                                                                               neval
                                                                 P
                                      pool                            d nd NRMSEd            Pd  d
                          cpNRMSE            =           =               P eval                   att                 (4)
                                                  c̄                        d nd              d nd

which simplifies to:

                                                                att        eval
                                                            P         P
                                                 pool        d nd      d nd NRMSEd
                                     cpNRMSE            =                                                             (5)
                                                                            eval 2
                                                                      P         
                                                                        d nd

where, summing over datasets d:

        • natt
           d = users attempted,


                                                                29
                                                       Sahdra et al.                                          A P REPRINT



       • neval
          d = users evaluated,
       • NRMSEd = that dataset’s mean NRMSE.

This preserves partial-missingness information that a naive collapse would discard, so a pooled point resting on 1-of-5
datasets is visibly less trustworthy than one resting on 5-of-5.
MAE. MAE carries the identical scale-dependence problem as RMSE, so we normalise and coverage-penalise
identically:

                                                                 MAE
                                                    NMAE =                                                              (6)
                                                                 range

                                                                  NMAE
                                                 cpNMAE =                                                               (7)
                                                                 coverage
where range is RMSE divided by NRMSE. NMAE mirrors the NRMSE definition, landing on the same dimensionless
scale and feeding the same cross-dataset and window-comparison rollups.
Bias. Raw bias carries the same survivorship bias as NRMSE, so it is averaged only over successfully evaluated users,
and a coverage-penalised Bias is calculated analogously. Bias’s optimum is 0, it is unbounded, and symmetric about
that optimum; dividing the signed value by coverage < 1 therefore always pushes it away from 0 (worse), regardless of
sign—the same clean behaviour cpNRMSE relies on, requiring no 1 − x recast.
We first normalise bias to the same range used for NRMSE:

                                        RMSE                         bias          NRMSE
                             range =               ⇒     nbias =          = bias ×                                      (8)
                                       NRMSE                        range          RMSE
This places bias on the same normalised scale as NRMSE and NMAE (0 = unbiased; sign = direction). The same
coverage term then yields:

                                                                   nbias
                                                  cpNBias =                                                             (9)
                                                                 coverage

B.2   Preserving multivariate (between-variable) structure

cpCorr. Correlation is calculated per user × variable as the Pearson correlation between complete (ground-truth) and
imputed values, computed only over masked cells (the same cells scored by RMSE). Because this is not a correlation
over the whole series, correlation inherits the same survivorship bias as NRMSE: a method that quietly drops hard users
can post a flattering correlation. Pearson correlation is additionally undefined whenever either the true or imputed vector
of masked values is constant within a user × variable cell—a failure mode not captured by coverage alone, requiring a
separate correlation-coverage term:

                                                                  ncorrDef ined
                                           corr_definedness =                                                         (10)
                                                                   ncorrRows

                                     corr_coverage = coverage × corr_definedness                                      (11)
The two terms are multiplied because they are sequential, independent filters on the same pool of cells: a cell must first
survive whole-user attrition (coverage), and among surviving cells, some further fraction still fail to yield a defined
correlation (corr_definedness).
Because correlation is bounded in [−1, 1], signed, and inverted relative to NRMSE (higher is better), dividing correlation
directly by coverage < 1 does not consistently move it toward "worse." We therefore recast:

                                                              1 − corr
                                                cpCorr =                                                              (12)
                                                           corr_coverage
This recast retains the same properties as cpNRMSE: at full coverage, cpCorr = corr, and cpCorr strictly worsens as
corr falls or coverage falls, regardless of corr’s sign.


                                                            30
                                                       Sahdra et al.                                         A P REPRINT



Pooled cpCorr follows the same principles as pooled cpNRMSE:

                                                  eval
                                             P
                                               d nd corrd
                                corrpool =     P eval                                                                (13)
                                                  d nd

                                          P eval                                   P corr_defined
                                             n                                        n
                           coveragepool = Pd datt ,         corr_definednesspool = Pd dcorr_rows                     (14)
                                            d nd                                     d nd


                      corr_coveragepool = coveragepool × corr_definednesspool                                        (15)

                                                    1 − corrpool
                             cpCorrpool = 1 −                                                                        (16)
                                                 corr_coveragepool

where, summing over datasets d:
       • natt                   eval
          d = users attempted, nd = users evaluated—the same counts cpNRMSE’s pooling uses;
       • ncorr_rows
          d         = (user × variable) cells attempted for correlation, ncorr_defined
                                                                           d           = how many yielded a defined
         correlation;
       • corrd = that dataset’s mean correlation, weighted by neval  d   in the pooled mean (same weighting as
         NRMSE_pooled).
Pooling corr_definedness as a ratio of summed counts (rather than averaging per-dataset fractions) means a dataset
contributing only a handful of evaluable cells does not receive the same vote as one contributing thousands.
cpFrob. For each user, we compare the full and partial correlation matrix of the complete data against the same matrix
computed on reconstructed data, across every numeric/ordinal target variable jointly, using the Frobenius norm of the
difference:
                                                                   v
                                                                   u p X
                                                                       p 
                                                                   uX                   2
                         corr_matrix_frob = Rtrue − Rimp F        =t       Rtrue − Rimp
                                                                                    ij      ij                       (17)
                                                                       i=1 j=1


where Rtrue and Rimp are the p × p Pearson correlation matrices of the complete and imputed target variables. A value
of 0 means every pairwise relationship was reproduced exactly; the score grows with the number and size of distorted
pairs.
                                                                   v
                                                                   u p X
                                                                       p 
                                                                   uX                     2
                         partial_corr_frob = P true − P imp F     =t       P true − P imp
                                                                                    ij     ij                        (18)
                                                                       i=1 j=1


where P true and P imp are partial-correlation matrices, whose off-diagonal entry Pij is the correlation between variables
i and j after conditioning on all remaining variables. This is the sharper test: two variables may still appear related in
Eq. (17) simply because both depend on a third, well-reconstructed variable, whereas partial correlation isolates the
direct relationship.
corr_matrix_frob and partial_corr_frob are already proper losses (nonnegative, zero at perfect reconstruction, unbounded
above, lower-is-better)—the same shape as NRMSE—so, unlike cpCorr, they can be deflated directly:

                                        nrel_defined
                    rel_definedness =                                                                                (19)
                                         nrel_rows

                       rel_coverage = coverage × rel_definedness                                                     (20)

                                        corr_matrix_frob                             partial_corr_frob
                             cpFrob =                    ,        cpPartialFrob =                                    (21)
                                          rel_coverage                                 rel_coverage


                                                             31
                                                        Sahdra et al.                                             A P REPRINT



rel_definedness (Eq. (19)) is, of users for which a relationship row exists, the fraction whose row yielded a finite
Frobenius norm. It exists for the same reason corr_definedness did: a relationship row can return NA even for a
successfully imputed user—either the cell had fewer than two numeric/ordinal target variables from which to build a
matrix, or the correlation/partial-correlation matrix came out non-finite (e.g., near-singular or near-constant columns).
This failure mode is invisible to coverage alone, necessitating the additional definedness term.
Unlike cpCorr, these are computed over each user’s entire series with observed cells copied through unchanged; only
masked cells differ between true and imputed matrices. At low missingness targets, most of both matrices is therefore
literally identical data, so a small Frobenius norm reflects "most of the series was untouched," not "structure was
preserved." These metrics should be read only at the high missingness end (50–80%), where a real share of each matrix
is genuinely reconstructed.

B.3   Preserving temporal (within-variable, over-time) structure

We use three full-series temporal metrics, computed on each user’s entire per-user series (observed cells copied through,
only masked cells reconstructed) rather than on scattered masked cells alone, because autocorrelation, differencing, and
spectral content are not well-defined on a random subset of timepoints. Each metric is computed at the granularity of
one row per user × variable and then pooled. For a given user u and variable v, let x = (x1 , . . . , xT ) denote the true
series and x̂ = (x̂1 , . . . , x̂T ) the reconstruction over T observed time steps. For all three metrics, lower is better (0
denotes perfectly preserved temporal structure).
Autocorrelation error. This directly tests persistence: does a high day tend to be followed by a high day in the
reconstruction, as in reality? We compute the lag-k autocorrelation ρk of each series and take the mean absolute error
over lags 1–3:

                                         3                                        PT
                                  1X                                               t=k+1 (xt − x̄)(xt−k − x̄)
              acf_lag1_3_erru,v =    ρk (x) − ρk (x̂) ,                ρk (x) =       PT                      .          (22)
                                  3                                                      t=1 (xt − x̄)
                                                                                                       2
                                       k=1

Range-normalised first-difference RMSE. This captures dynamics/roughness: whether the reconstruction reproduces
the magnitude of daily swings, or smooths them into a flat line. We take the RMSE between the first-differenced true
and reconstructed series, where ∆xt = xt − xt−1 :
                                                      v
                                                      u             T
                                                  raw
                                                      u        1 X               2
                                    firstdiff_rmse = t
                                                  u,v                  ∆xt − ∆x̂t .                                      (23)
                                                             T − 1 t=2

Since this raw quantity is expressed in each variable’s native units, it cannot be pooled across heterogeneous variables
and datasets. We therefore apply the same range-recovery normalisation used for cpNBias and cpNMAE, rescaling
by the ratio of the normalised to the raw RMSE of the level series, equivalently, dividing by the range Ru,v =
max(x) − min(x):

                                                                                                  raw
                                                                    NRMSEu,v   firstdiff_rmseu,v
                       firstdiff_rmseu,v = firstdiff_rmseraw
                                                         u,v ×               =                   .                       (24)
                                                                    RMSEu,v           Ru,v
This yields a unit-free quantity that is directly comparable across all variables and datasets.
Spectral difference. This captures rhythm: whether weekly or otherwise periodic structure survives, or is washed out.
Let Px (f ) and Px̂ (f ) be the power spectral densities of the true and reconstructed series across frequencies f . We
quantify the discrepancy in spectral content as the total absolute difference between the two spectra after normalising
each to unit total power:

                                              X                                          Px (f )
                         spectral_diffu,v =       P̃x (f ) − P̃x̂ (f ) ,    P̃x (f ) = P          ′
                                                                                                     .                   (25)
                                              f                                          f ′ Px (f )

Normalising each spectrum to unit total power isolates shape—which rhythms are present, and in what relative
proportion—from overall signal energy.
Pooling. Consistent with our other metrics, each quantity in Equations (22), (24), and (25) is computed per user ×
variable and then aggregated using the coverage-weighted pooling scheme described in Appendix B.1, so that datasets


                                                              32
                                                      Sahdra et al.                                          A P REPRINT



and variables with more evaluable cells contribute proportionally and the reported aggregates remain survivorship-aware.
First differences in Equation (23) are taken over consecutive observed time steps, consistent with the missingness mask
defined in Section 3.4.

B.4   Preserving distributional shape

The temporal metrics above test whether the series moves through time correctly (persistence, dynamics, rhythm),
since in a time series the ordering of observations is itself informative. These are computed on the full reconstructed
series and therefore carry a low-missingness dilution caveat: at small missingness targets the metric is dominated by
untouched observed cells, so it is only trustworthy at the 50–80% end.
The distributional metrics introduced here are complementary in two deliberate ways. First, they are order-agnostic:
they interrogate the marginal distribution (the spread and shape of the reconstructed values) independently of temporal
ordering. Second, they are masked-cell-only, evaluated exclusively on held-out targets (like cpCorr), and therefore free
of the dilution caveat—diagnostic at every missingness level. Since a method can preserve the marginal distribution
perfectly while scrambling temporal order (or vice versa), both families are required to separate these two failure modes.
For a given user u and variable v, let M denote the set of masked cells, x = {xi : i ∈ M } the true masked values, and
x̂ = {x̂i : i ∈ M } the corresponding imputed values.
Variance ratio. This directly measures whether the method reproduced the spread of the masked values—precisely
the quantity to which NRMSE is blind, since a method that regresses every target toward the mean scores well on
MAE/NRMSE while destroying the distribution. It is defined as the ratio of imputed to true variance over the masked
cells:

                                                             1
                                                                 P           ¯2
                                                  Var(x̂)   |M |  i∈M (x̂i − x̂)
                                   var_ratiou,v =         = 1 P                  2
                                                                                   .                                 (26)
                                                  Var(x)    |M |  i∈M (xi − x̄)

A value of 1 denotes perfectly reproduced spread; values below 1 indicate variance collapse (over-smoothing), and
values above 1 indicate inflated variability. This metric exposes the regress-to-the-mean trap directly, which is why we
additionally examine it against NRMSE. Variance ratio is deliberately not coverage-penalised: the central optimum and
near-zero collapse make any log-deflation blow up, so it is kept on a raw log scale with an ideal line at 1.
Kolmogorov-Smirnov statistic. The KS statistic is the maximum absolute gap between the two empirical cumulative
distribution functions (CDFs), catching whole-distribution mismatch that variance ratio alone would miss:

                                         KS_statu,v = sup Fx (z) − Fx̂ (z) ,                                         (27)
                                                          z

where Fx and Fx̂ are the empirical CDFs of the true and imputed masked values. It ranges over [0, 1], with 0 denoting
identical distributions.
1-Wasserstein distance. Where KS reports a single worst-point discrepancy on the CDF, the 1-Wasserstein (earth-
mover’s) distance integrates the entire displacement, capturing both how far and how much of the distribution must
move. For one-dimensional distributions this equals the L1 area between the two CDFs:
                                                         Z ∞
                                     Wasserstein1u,v =             Fx (z) − Fx̂ (z) dz.                              (28)
                                                          −∞

This complements the KS statistic: a small KS can coexist with a large Wasserstein distance when the mismatch is
spread across the whole range rather than concentrated at a single point. Unlike the unit-free KS statistic, Wasserstein
distance is expressed in the variable’s own units. For pooling across heterogeneous variables and datasets we apply the
same range normalisation used elsewhere, dividing by the target range Ru,v = max(x) − min(x).
cpKS and cpWasserstein1. Let cu,v ∈ (0, 1] denote the coverage for user u and variable v (the fraction of masked
target cells for which the method produced a valid imputation), with base distances computed over those evaluable
masked cells. The coverage penalty divides the raw distance by cu,v , so that a method reconstructing only a subset of
the masked distribution is penalised in proportion to what it left unimputed:

                                                     1
                                        cpKSu,v =       sup Fx (z) − Fx̂ (z) ,                                       (29)
                                                    cu,v z

                                                              33
                                                     Sahdra et al.                                        A P REPRINT



                                                               Z ∞
                                                    1 1
                            cpWasserstein1u,v =     ·                Fx (z) − Fx̂ (z) dz,                         (30)
                                                cu,v Ru,v       −∞

where Fx and Fx̂ are the empirical CDFs of the true and imputed masked values, and Ru,v = max(x) − min(x) is the
target range applied to render cpWasserstein1 unit-free and poolable across variables. Aggregation across datasets uses
the same coverage-weighted pooling scheme as our other metrics (Appendix B.1).




                                                          34
                                                     Sahdra et al.                                         A P REPRINT



C     Supplementary Imputation Accuracy Results
C.1   Fail Counts by Method and Missingness Percentage

Figure 8 reports the number of users for which each method failed to produce a valid, evaluable reconstruction, broken
down by missingness percentage across all datasets and imputation methods. This supports the coverage-penalisation
rationale developed in Appendix B.1. A method with a low raw error but a high fail count is misrepresenting its
reliability unless deflated by coverage.




        Figure 8: Failed user counts per missingness percentage across all datasets and imputation methods.


C.2   Supplementary cpNRMSE Results

This appendix provides supplementary cpNRMSE results supporting Section 6.1.2 of the main text: per-dataset (non-
pooled) trends across all mechanisms and window strategies, the full-range view alongside its zoomed counterpart, and
the rank-stability analysis underlying the main text’s claims about PAIN’s dominance.
The per-dataset, non-pooled view shown in Figure 9 complements the pooled Figure 1 in the main text by showing
where each dataset sits relative to the overall trend, rather than collapsing all seven into a single line.
Figure 10 is the rank-stability analysis which quantifies, via user-bootstrap resampling, how often each method achieves
the lowest cpNRMSE, substantiating the main text’s claim that PAIN’s point-accuracy advantage is stable rather than an
artefact of a single sample.




                                                          35
                                                  Sahdra et al.                                      A P REPRINT




   Figure 9: cpNRMSE per dataset (clipped y-axis [0,1]), across missingness mechanisms and window strategies.




Figure 10: Rank stability: probability that each method achieves the lowest cpNRMSE, estimated via user-bootstrap
resampling, across missingness mechanisms, window strategies, and missingness percentages.



                                                       36
                                                     Sahdra et al.                                         A P REPRINT



C.3   Supplementary cpNMAE Results

Figure 11 shows the RMSE/MAE ratio used as an error-tail diagnostic. Values near 1 indicate uniformly distributed
errors, while higher values flag methods whose error is driven by occasional large-magnitude misses rather than
consistent small deviations.




Figure 11: Error-tail diagnostic: RMSE/MAE ratio by method, missingness mechanism, and window strategy. A
ratio of 1 (dashed line) is the theoretical floor, indicating uniformly distributed errors. By Jensen’s inequality, RMSE
always bounds p MAE from above, with equality only when every error has identical magnitude. A ratio of ≈ 1.25
(dotted line, π/2) is the expected value under Gaussian-distributed errors, making it a more realistic baseline than
the strict uniform-error floor. Values climbing meaningfully above this line indicate a heavier error tail (occasional
large-magnitude misses). Line opacity reflects the fraction of datasets evaluable at each missingness percentage.


C.4   Supplementary cpNBias Results

We present supplementary cpNBias results supporting the main text with figures showing the per-user signed-bias
gap against PAIN, its statistical significance via paired Wilcoxon tests (BH-corrected), and the per-dataset breakdown
underlying the pooled trends.
The lollipop plot below (Figure 12) summarises, for each method, the median per-user signed-bias gap relative to PAIN,
with filled points marking statistically significant differences. The tile heatmap (Figure 13) presents the same paired
comparison in a complementary format, making it easier to scan significance patterns across the full grid of mechanisms
and window strategies at once. Finally, the per-dataset breakdown (Figure 14) shows how coverage-penalised signed
bias varies by individual dataset, complementing the pooled trends discussed in the main text.




                                                          37
                                                   Sahdra et al.                                       A P REPRINT




Figure 12: Median per-user signed-bias gap (method minus PAIN) across missingness mechanisms and window
strategies. Filled points denote BH-significant differences (p < .05); values above zero indicate the method over-
imputes relative to PAIN, below zero indicates under-imputation relative to PAIN.




Figure 13: Paired signed-bias gap vs. PAIN (Wilcoxon, BH-corrected). Colour indicates the median per-user nbias
difference (red = over-imputes relative to PAIN, blue = under-imputes); asterisks denote significance (*BH p < .05,
**p < .01, ***p < .001).




                                                        38
                                                  Sahdra et al.                                     A P REPRINT




Figure 14: Coverage-penalised normalised bias (signed), by individual dataset, missingness mechanism, and window
strategy. Plot is clipped at [-0.5, 0.5].




                                                       39
                                                   Sahdra et al.                                       A P REPRINT



C.5   Runtime-Accuracy Trade-off: Full Detail

The two figures (Figure 15 and Figure 16) below present per-user runtime plotted against per-user NRMSE, faceted by
missingness mechanism and method, for the full and win30 window strategies respectively, supporting the runtime-
accuracy discussion in the main text.




Figure 15: Runtime vs. accuracy per user, full window strategy, by missingness mechanism and method. Each point is
one user; colour indicates % missing.




                                                        40
                                                  Sahdra et al.                                     A P REPRINT




Figure 16: Runtime vs. accuracy per user, win30 window strategy, by missingness mechanism and method. Each point
is one user; colour indicates % missing.


D     Preserving Multivariate Structure
D.1   Supplementary cpCorr Results

Figure 17 breaks down coverage-penalised correlation (cpCorr) by individual dataset, missingness mechanism, and
window strategy, complementing the pooled view in the main text and making visible the dataset-level divergence
underlying PAIN’s crossover behaviour at high missingness.




                                                       41
                                                     Sahdra et al.                                        A P REPRINT




Figure 17: Coverage-penalised correlation (cpCorr) by individual dataset, missingness mechanism, and window strategy.
Bottom-strip glyphs: × all failed; ◦ no numeric/ordinal target; △ correlation undefined (zero variance). Y-axis clipped
to [−1.5, 1].




                                                          42
                                                      Sahdra et al.                                         A P REPRINT



D.2   Supplementary cpFrob and cpPartialFrob Results

The pooled plot (Figure 18) shows coverage-penalised Frobenius error for both the full correlation matrix and the partial
correlation matrix, averaged across datasets. The per-dataset breakdown (Figure 19) makes explicit which datasets are
structurally undefined for this metric (marked by the bottom-strip glyphs) versus which contribute a genuine, evaluable
signal.




Figure 18: Coverage-penalised Frobenius error of the imputed vs. true correlation matrix (top row) and partial
correlation matrix (bottom row), pooled across datasets, by missingness mechanism and window strategy. Line opacity
indicates the fraction of datasets evaluable at each missingness percentage.




                                                           43
                                                     Sahdra et al.                                          A P REPRINT




Figure 19: Coverage-penalised Frobenius error by individual dataset, missingness mechanism, and window strategy.
Solid lines: full correlation matrix; dashed lines: partial correlation matrix. Bottom-strip glyphs: △ correlation matrix
undefined (zero-variance variable); ◦ no numeric/ordinal target available.


E    Supplementary Preserving Temporal Structure Results
The three figures below (Figure 20, Figure 21, and Figure 22) present the per-dataset breakdown of the three full-series
temporal metrics introduced in Appendix B.3 (autocorrelation error, first-difference RMSE, and spectral difference),
complementing the pooled view in the main text and isolating which datasets drive the MICE-outlier and MNAR/win30
breakdown patterns discussed there.




                                                          44
                                                 Sahdra et al.                                     A P REPRINT




Figure 20: cpACF (lag-1-3 autocorrelation error, persistence) by individual dataset, missingness mechanism, and
window strategy.




                                                      45
                                                  Sahdra et al.                                      A P REPRINT




Figure 21: cpFirstDiff (first-difference RMSE, day-to-day dynamics) by individual dataset, missingness mechanism,
and window strategy.




                                                       46
                                                   Sahdra et al.                                        A P REPRINT




Figure 22: cpSpectral (spectral-content difference, rhythm) by individual dataset, missingness mechanism, and window
strategy.




                                                        47
                                                     Sahdra et al.                                        A P REPRINT



F   Supplementary Distributional Shape Results
Figure 23 shows the per-dataset breakdown of variance ratio, confirming that PAIN’s variance collapse under Block/Gap
missingness is consistent across multiple datasets rather than isolated to one. The pooled and per-dataset cpKS results
below (Figure 24 and Figure 26) show MICE as the dominant outlier across mechanisms, with the DL methods sitting
close to the ideal line except under the shared MNAR/win30 breakdown at high missingness. The corresponding
cpWasserstein1 results (Figure 25 and Figure 27) tell the same story using the full displacement between distributions
rather than the single worst-point CDF gap.




Figure 23: Variance ratio by individual dataset, missingness mechanism, and window strategy. 1 (dashed line) = ideal.




                                                          48
                                                  Sahdra et al.                                      A P REPRINT




Figure 24: Coverage-penalised KS statistic, pooled across datasets, by missingness mechanism and window strategy.
Lower = better.




          Figure 25: Coverage-penalised, range-normalised 1-Wasserstein distance pooled over datasets.




                                                       49
                                                Sahdra et al.                                       A P REPRINT




Figure 26: Coverage-penalised KS statistic by individual dataset, missingness mechanism, and window strategy.




                                                     50
                                                   Sahdra et al.                                       A P REPRINT




Figure 27: Coverage-penalised, range-normalised 1-Wasserstein distance by individual dataset, missingness mechanism,
and window strategy.




                                                        51
                                                      Sahdra et al.                                           A P REPRINT



G    Supplementary Trade-off Results: Accuracy vs. Multivariate Structure and Variance
     Preservation
The pooled trade-off plots (Figure 28 and Figure 29) below jointly visualise point accuracy against multivariate structure
preservation and against variance preservation, substantiating the main text’s claim that no single method dominates on
both axes simultaneously. The per-dataset versions of both trade-offs (Figure 30 and Figure 31) show that this pattern,
in particular PAIN’s Block/Gap collapse, holds consistently at the individual-dataset level rather than being an artefact
of pooling.




Figure 28: Accuracy vs. multivariate structure (full-series, pooled), by missingness mechanism and window strategy.
Bottom-left = ideal; faded points indicate low % missing, where the full-series cpFrob metric is diluted by untouched
observed cells; arrows trace rising missingness.




Figure 29: Accuracy vs. variance preservation (the regress-to-the-mean trade-off), pooled across datasets, by missingness
mechanism and window strategy. Dashed line = ideal (variance ratio = 1, log scale); far-left and floor = accurate-but-flat;
point size indicates % missing.




                                                            52
                                                    Sahdra et al.                                        A P REPRINT




Figure 30: Accuracy vs. multivariate structure (full-series), by individual dataset, missingness mechanism, and window
strategy. Bottom-left = ideal; faded points indicate low % missing; point size indicates % missing.




                                                         53
                                                    Sahdra et al.                                       A P REPRINT




Figure 31: Accuracy vs. variance preservation, by individual dataset, missingness mechanism, and window strategy.
Dashed line = ideal (variance ratio = 1, log scale); arrows trace rising missingness; point size indicates % missing.




                                                         54
                                                       Sahdra et al.                                            A P REPRINT



G.1    Supplementary Forest Plots: Per-User cpNRMSE and cpCorr (win30)

The forest plot Figure 32 presents the win30 counterpart to the full-window forest plots in the main text, showing
per-user cpNRMSE and cpCorr by method and missingness mechanism under the 30-day windowed imputation strategy.

H     Generative AI Use Disclosure
Generative AI Anthropic Claude Sonnet 4.5 was used to assist in testing and debugging the analysis code described in
this paper, including identifying syntax errors, flagging logical inconsistencies, and suggesting diagnostic checks during
development. All code logic, statistical methods, experimental design, analysis, interpretation, and written content are
the sole work of the authors, who take full responsibility for the accuracy, validity, and integrity of the content presented
in this paper.

I     Analysis Code
Analysis code and first author’s personal dataset used in this study can be provided via contacting first author.




                                                             55
                                                 Sahdra et al.                                     A P REPRINT




                                                        56
Figure 32: Per-user cpNRMSE and cpCorr forest plots, win30    window strategy, by method (rows) and missingness
mechanism (columns). Light = cpNRMSE, dark = cpCorr. Each line is one user, ordered by mean cpNRMSE within
dataset; point = mean across 8 missingness percentages; whisker = range (min-max) across those percentages.
