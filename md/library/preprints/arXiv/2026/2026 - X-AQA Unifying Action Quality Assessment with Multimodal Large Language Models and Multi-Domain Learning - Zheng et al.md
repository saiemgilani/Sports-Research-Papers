<!-- source: library/preprints/arXiv/2026/2026 - X-AQA Unifying Action Quality Assessment with Multimodal Large Language Models and Multi-Domain Learning - Zheng et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.28548 -->
<!-- authors: Kaili Zheng, Wei Ding, Yuchen Ding, Kaiwen Wang, Xun Zhu, Chenyi Guo, Yudong Zhang, Ji Wu -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-24; equations, tables and figures are NOT preserved - consult the PDF for those -->

# X-AQA: Unifying Action Quality Assessment with Multimodal Large Language Models and Multi-Domain Learning

                                                        X-AQA: Unifying Action Quality Assessment with Multimodal
                                                           Large Language Models and Multi-Domain Learning

                                                                 Kaili Zheng1
                                                                            Wei Ding2 Yuchen Ding3 Kaiwen Wang1 Xun Zhu1
                                                                            Chenyi Guo1 * Yudong Zhang1 * Ji Wu1,4,5 *
                                                                   1
                                                                     Department of Electronic Engineering, Tsinghua University
                                                       2
                                                         Carnegie Mellon University 3 Baidu, Inc. 4 College of AI, Tsinghua University
                                                          5
arXiv:2611.28548v1 [cs.AI] 21 Nov 2026




                                                            Beijing National Research Center for Information Science and Technology



                                                (a) X-AQA-40K Dataset                            (b) Unified Assessment                  (c) X-AQA-Bench Evaluation

                                                                                                              Assessment Criteria
                                                                                                              (when available)
                                                                                                        •   Official scoring rules
                                                                                         Video &        •   Clinical assessment scales
                                            Competitive Sports       Fitness Exercises
                                                                                         Question       •   Expert-defined guidelines




                                                                                                   X-AQA Model

                                              Rehabilitation          General Skills     Score    8.5       Category Incorrect

                                                 4 domains · 22 data sources             Text     Keep your back straight …


                                         Figure 1. Overview of X-AQA. (a) We curate the X-AQA-40K dataset from 22 data sources across four domains to train a unified AQA
                                         model. (b) Through multi-domain learing, we obtain X-AQA, a single MLLM that produces scores, categories, or textual assessments,
                                         with assessment criteria provided when available. (c) X-AQA achieves strong performance across assessment tasks on X-AQA-Bench.


                                                                     Abstract                                    answering format, incorporating dataset-specific annota-
                                                                                                                 tion guidelines and official scoring rules when available.
                                         Action Quality Assessment (AQA) aims to evaluate the qual-              Using this corpus, we fine-tune Qwen3.5-9B to develop a
                                         ity of human actions, yet existing methods are predomi-                 single MLLM capable of handling diverse AQA tasks. We
                                         nantly developed and evaluated on individual datasets with              further establish X-AQA-Bench, which evaluates both in-
                                         different task formulations and assessment criteria. We                 distribution (ID) performance on datasets represented dur-
                                         introduce X-AQA, the first unified training and evalua-                 ing training and out-of-distribution (OOD) generalization
                                         tion framework for general-purpose AQA with multimodal                  on four held-out datasets. The resulting model outper-
                                         large language models (MLLMs). We construct X-AQA-                      forms all evaluated open-source MLLMs on X-AQA-Bench
                                         40K, a training corpus comprising 40,163 samples from                   and achieves competitive performance relative to propri-
                                         22 data sources across four domains: competitive sports,                etary MLLMs. Ablation studies further demonstrate that
                                         fitness exercises, rehabilitation, and general skills. We               multi-domain joint training and explicitly providing assess-
                                         convert heterogeneous annotations into a unified question-              ment criteria in prompts both improve OOD generaliza-
                                                                                                                 tion. X-AQA establishes a unified foundation for advancing
                                            * Corresponding authors:                                             general-purpose AQA across diverse real-world domains.
                                         Chenyi Guo (guochy@mail.tsinghua.edu.cn)                                Data and models are released at here.
                                         Yudong Zhang (zhangyd16@mails.tsinghua.edu.cn)
                                         Ji Wu (wuji_ee@mail.tsinghua.edu.cn)


                                                                                                             1
1. Introduction                                                       systematically evaluate AQA performance and generaliza-
                                                                      tion. It includes in-distribution (ID) evaluation on held-out
Action Quality Assessment (AQA) aims to evaluate how                  samples from datasets represented during training and out-
well human actions are performed [52], with applications              of-distribution (OOD) evaluation on four held-out source
spanning competitive sports [66], fitness exercises [50], re-         datasets.
habilitation [35], and general skills [20]. Unlike action
                                                                          We fine-tune Qwen3.5-9B [54] on X-AQA-40K to ob-
recognition, which focuses on what action is performed,
                                                                      tain X-AQA, a unified AQA model. On the ID split of X-
AQA evaluates how well the action is performed accord-
                                                                      AQA-Bench, X-AQA surpasses all evaluated open-source
ing to task-specific objectives and assessment criteria. AQA
                                                                      and proprietary MLLMs on all four metrics. In particular,
tasks take diverse forms, including performance scoring,
                                                                      X-AQA achieves an SRCC of 0.607, compared with 0.465
execution error detection, relative skill assessment, and tex-
                                                                      for GPT-6.1 Sol [46]. On the OOD split, X-AQA outper-
tual feedback generation [5, 49]. Assessment criteria also
                                                                      forms all evaluated open-source MLLMs on all four met-
vary across domains, including official scoring rules in
                                                                      rics and achieves competitive performance relative to pro-
competitive sports, standardized clinical assessment scales
                                                                      prietary MLLMs. For textual feedback, X-AQA achieves a
in rehabilitation, and expert-defined guidelines for identify-
                                                                      BERTScore of 0.871, compared with 0.862 for Gemini 3.8
ing execution errors. Due to this diversity, existing AQA
                                                                      Flash [26]. Ablation studies further demonstrate the ben-
methods are typically developed for individual datasets,
                                                                      efits of multi-domain learning and explicit assessment cri-
with architectures and learning objectives tailored to their
                                                                      teria for generalization to unseen datasets. On the OOD
assessment tasks and supervision.
                                                                      split, multi-domain learning raises the SRCC from 0.107 to
    To move beyond dataset-specific AQA, recent studies
                                                                      0.244, while providing assessment criteria increases macro-
have explored cross-action learning. Specifically, Parmar
                                                                      F1 from 0.470 to 0.557. Overall, X-AQA can address di-
and Morris [48] train a shared C3D-LSTM model across
                                                                      verse AQA tasks and generalize to unseen datasets.
multiple action categories, while MoAKE [65] introduces
                                                                          Our main contributions are summarized as follows:
a mixture-of-experts architecture to capture diverse action
patterns and adaptively aggregate action knowledge. Al-               • We construct X-AQA-40K, a training corpus comprising
though these methods demonstrate the benefits of cross-                  samples from 22 datasets across four domains. It brings
action learning, they primarily focus on numerical score                 heterogeneous assessment tasks and available assessment
prediction. AQA, however, encompasses a broader range                    criteria into a shared question-answering format.
of assessment tasks, including numerical scoring, categori-           • We establish X-AQA-Bench, a unified benchmark span-
cal judgments, and textual feedback. Multimodal large lan-               ning numerical, categorical, and textual assessment, with
guage models (MLLMs) offer a promising foundation for                    ID and OOD splits for evaluating AQA performance and
unifying these tasks through their multimodal understand-                generalization.
ing and instruction-following capabilities [6, 38]. Recent            • We develop X-AQA, a unified MLLM for diverse AQA
studies have examined MLLMs for AQA, identifying chal-                   tasks that outperforms all evaluated open-source MLLMs
lenges in fine-grained execution understanding and qual-                 across all benchmark metrics and achieves competitive
ity judgment [22, 76]. However, how to effectively train                 performance relative to proprietary MLLMs. Ablation
MLLMs using heterogeneous AQA supervision and evalu-                     studies show that multi-domain learning and explicit as-
ate their generalization to unseen datasets remains underex-             sessment criteria improve OOD generalization.
plored.
    In this paper, we introduce X-AQA, the first unified train-       2. Related Work
ing and evaluation framework for general-purpose AQA
                                                                      2.1. Action Quality Assessment
with MLLMs, as illustrated in Fig. 1. We construct X-AQA-
40K, a training corpus comprising 40,163 samples from 22              AQA has been studied across datasets spanning diverse do-
datasets across four domains: competitive sports, fitness             mains, with different assessment objectives and annotation
exercises, rehabilitation, and general skills. We unify het-          schemes. Numerical scoring is widely studied in compet-
erogeneous annotations into question-answer pairs covering            itive sports, with methods employing direct score regres-
numerical scoring, categorical judgments, and textual feed-           sion or reference-based contrastive regression [71]. Be-
back, while preserving the assessment objectives and label            yond the choice of regression strategy, some methods ex-
semantics of each source. When available, dataset-specific            plicitly model how an overall performance score is com-
annotation guidelines and official scoring rules are incorpo-         posed. For example, FineGrade [36] predicts difficulty
rated into the prompts to make the assessment criteria ex-            and execution scores separately and enforces their addi-
plicit. Using this corpus, we perform multi-domain joint              tive relationship according to official gymnastics scoring
training to develop a single MLLM capable of addressing               rules. Numerical assessment is also used in rehabilita-
diverse AQA tasks. We further establish X-AQA-Bench to                tion, where KIMORE [11–13] provides clinician-assigned

                                                                  2
                                              Competitive Sports                                                              13,904 (34.6%)
                                              FineFS [34] (2,000)              CricketVision [43] (2,000)          ExpertAF [5] (2,000)
                                              Ego-Exo4D [27] (1,980)           MultiSenseBadminton [55] (1,663)    CoT-AFA [53] (1,599)
                                              MTL-AQA [49] (1,059)             AQA-7 [48] (803)                    RG [72] (800)
                                              Fitness Exercises                                                               12,976 (32.3%)
          X-AQA-40K                           QEVD [47] (4,000)                EgoExo-Fitness [37] (2,636)         CoT-AFA [53] (2,340)
                                              Fitness-AQA [50] (2,000)         FLAG3D [58, 59] (2,000)
              40,163
           training samples                   Rehabilitation                                                                    3,729 (9.3%)
                                              LLM-FMS [64] (1,451)             REHAB24-6 [14, 15] (727)            ExeCheck [28] (600)
                                              KERAAL [45] (540)                UpperLimb [44] (411)
                                              General Skills                                                                   9,554 (23.8%)
                                              LASANA [24] (2,906)              CaptainCook4D [51] (2,000)          Ego-Exo4D [27] (2,000)
                                              AIxSuture [29] (2,000)           CPR-Coach [61] (648)

                                                   X-AQA-Bench (7,101 test samples)
  ID    300       272     350      339       300   200   300       544             600         300     300   300   80   400    96 187       300

OOD                       T3Set [41] (700)                         Fitness-7 [21] (348)        KIMORE [11] (348)        JIGSAWS [25] (339)

Figure 2. Composition of X-AQA-40K and X-AQA-Bench. X-AQA-40K comprises 40,163 training samples from 22 data sources across
four domains, with Ego-Exo4D and CoT-AFA each spanning two domains. X-AQA-Bench contains 7,101 test samples, including 5,366 ID
samples from datasets represented during training and 1,735 OOD samples from four held-out datasets. RG denotes Rhythmic Gymnastics.


scores for therapeutic exercises. Beyond numerical scor-                     2.3. MLLMs for AQA
ing, categorical assessment addresses tasks such as execu-
tion error identification and proficiency classification. For                MLLMs have been explored for action assessment tasks
instance, FLEX [69] provides annotations of exercise exe-                    that involve quality judgments and natural-language feed-
cution errors, while Ego-Exo4D [27] includes proficiency                     back. ExpertAF develops a multimodal model that gener-
annotations for diverse physical skills. Textual assessment                  ates expert commentary and corrective demonstrations from
provides descriptive feedback on action execution. MTL-                      action videos and body poses. ProfVLM [9] formulates
AQA explores commentary generation alongside score pre-                      multi-view proficiency assessment as conditional language
diction, while FLEX and Ego-Exo4D incorporate corrective                     generation, jointly predicting proficiency levels and expert-
feedback and expert commentary, respectively. Overall, ex-                   like commentary. For interactive fitness coaching, Panchal
isting AQA methods are typically developed and evaluated                     et al. [47] introduce the QEVD benchmark and a stream-
within the task settings defined by individual datasets.                     ing model that provides appropriate feedback during on-
                                                                             going exercises. Beyond developing task-specific models,
2.2. Cross-Action Learning for AQA                                           recent studies have systematically evaluated the AQA capa-
                                                                             bilities of general-purpose MLLMs. Freitas et al. investi-
Beyond dataset-specific AQA, several studies have explored                   gate model performance across AQA domains, tasks, and
sharing assessment knowledge across different action cate-                   prompting strategies. FitAQA evaluates fine-grained visual
gories. For example, Parmar and Morris investigate cross-                    perception, correctness judgment, and temporal error local-
action knowledge transfer by jointly training a shared C3D-                  ization. However, existing research has yet to establish a
LSTM model on multiple actions. MoAKE introduces a                           unified framework for training MLLMs on heterogeneous
mixture-of-experts architecture to capture complementary                     AQA supervision and evaluating their generalization across
action knowledge and adaptively aggregate it across actions,                 diverse AQA tasks and datasets.
demonstrating generalization to unseen actions under zero-
and few-shot settings. However, both approaches focus on
numerical score prediction. CrossTrainer [4] extends cross-
action learning to language-based assessment by learning                     3. Method
transferable skill attributes from expert commentary, but
focuses on proficiency estimation and actionable feedback                    We construct X-AQA-40K by integrating heterogeneous
generation across sports. A unified model that jointly ad-                   datasets into a shared question-answering format and incor-
dresses numerical scoring, categorical judgments, and tex-                   porating assessment criteria when available. We then jointly
tual feedback across diverse actions remains largely unex-                   train a single MLLM on this corpus and establish X-AQA-
plored.                                                                      Bench to evaluate performance and generalization.


                                                                         3
3.1. X-AQA-40K Dataset                                                 mic Gymnastics, using the rule editions applicable to the
                                                                       corresponding competitions. For datasets with established
Data Composition. We construct X-AQA-40K from 22
                                                                       assessment rubrics, we incorporate their scoring dimen-
existing data sources spanning four domains, competitive
                                                                       sions, rating scales, and error definitions, such as OSATS
sports, fitness exercises, rehabilitation, and general skills,
                                                                       in AIxSuture, FMS criteria in LLM-FMS [64], and skill
as illustrated in Fig. 2 (top). These sources cover diverse
                                                                       assessment guidelines in LASANA. For fitness exercises,
AQA tasks, such as diving execution scoring in MTL-AQA,
                                                                       we formulate assessment criteria from the annotated form
exercise error detection in Fitness-AQA, rehabilitation cor-
                                                                       errors and technical points in Fitness-AQA and EgoExo-
rectness assessment in REHAB24-6 [15], suturing skill as-
                                                                       Fitness. For REHAB24-6, we derive observable correctness
sessment in AIxSuture [29], and coaching feedback gen-
                                                                       criteria from the provided rehabilitation exercise descrip-
eration in QEVD. To balance training data across sources
                                                                       tions. These criteria describe general assessment standards
and tasks, we cap each dataset-specific task at 2,000 train-
                                                                       independently of each sample’s reference answer and ac-
ing samples. For Ego-Exo4D and CoT-AFA [53], which
                                                                       company the task instructions and output specifications. We
span multiple domains, the cap is applied separately to each
                                                                       follow this approach during both training and evaluation.
task within each domain. Datasets with multiple assessment
tasks contribute separate training subsets. Examples include           3.2. Multi-Domain Joint Training
execution question answering and live coaching feedback
in QEVD, technical-point assessment and overall feedback               We jointly fine-tune Qwen3.5-9B on X-AQA-40K to learn
in EgoExo-Fitness [37], form assessment and explanatory                diverse AQA tasks across all four domains. Given a training
feedback in CoT-AFA, and skill scoring and error detection             sample consisting of visual input Vi , assessment instruction
in LASANA [24]. For FineFS [34] and Rhythmic Gym-                      Qi , and reference answer Ai , we optimize the autoregres-
nastics [72], we mask visible broadcast scoreboards to pre-            sive language modeling objective:
vent direct leakage of ground-truth scores. The resulting                                           |Ai |
X-AQA-40K corpus contains 40,163 question-answer pairs                                 1     X X
                                                                        L(θ) = − P               wi       log Pθ (ai,t | Vi , Qi , ai,<t )
across 29 task-specific subsets, covering 19,614 unique me-                           i |Ai | i     t=1
dia files. Detailed task-level dataset statistics and prepro-                                                                          (1)
cessing procedures for each source dataset are provided in             where θ denotes the trainable model parameters, |Ai | is the
the supplementary material.                                            number of tokens in the reference answer, ai,t is its t-th to-
                                                                       ken, and ai,<t is the preceding answer prefix. The sample-
                                                                       specific loss weight is denoted by wi . Similar to RAS [10],
Unified Question-Answering Formulation. We convert
                                                                       we assign higher loss weights to underrepresented classes.
heterogeneous AQA annotations into a unified question-
                                                                       For categorical AQA tasks, we compute these weights from
answering format. Each training sample consists of a vi-
                                                                       label frequencies within task-specific groups, such as indi-
sual input, a task-specific assessment instruction, and a ref-
                                                                       vidual exercises or technical points. The weights are nor-
erence answer derived from the original annotations. Nu-
                                                                       malized within each group and capped at 20 to limit extreme
merical scores and categorical judgments are represented
                                                                       values, balancing classification supervision without altering
using task-specific JSON fields, while textual feedback is
                                                                       the training sample distribution. All assessment tasks are
expressed in natural language. For tasks involving multiple
                                                                       optimized using this shared objective, without task-specific
assessment aspects, a single answer can contain multiple
                                                                       prediction heads.
fields, as in MTL-AQA, which combines execution scoring
and commentary. This formulation enables a single MLLM                 3.3. X-AQA-Bench and Evaluation
to learn diverse assessment tasks through a shared interface
                                                                       Benchmark Composition. We establish X-AQA-Bench
while preserving their task-specific output semantics.
                                                                       to evaluate assessment performance on seen datasets and
                                                                       generalization to unseen datasets, as illustrated in Fig. 2
Assessment Criteria Integration. Assessing action qual-                (bottom). The ID split is constructed from the test sets of
ity requires task-specific criteria that define what constitutes       datasets represented in X-AQA-40K. To preserve assess-
good execution. To provide explicit guidance across diverse            ment diversity, we stratify samples within each task accord-
AQA tasks, we incorporate assessment criteria into the as-             ing to available action categories or assessment attributes,
sessment prompts when available, drawing from official                 such as technical points. Each stratum contains samples of
sports scoring rules, clinical assessment scales, or expert-           the same action type or questions assessing the same tech-
defined annotation guidelines. For competitive sports,                 nical point, depending on the task’s annotations. We re-
we draw on official scoring rules, including FINA diving               tain one question per recording and stratum, then select up
rules [63] for MTL-AQA, ISU figure skating rules [32] for              to 300 samples per task and output format through strati-
FineFS, and FIG rhythmic gymnastics rules [31] for Rhyth-              fied sampling, accounting for category labels within each


                                                                   4
Table 1. Comparison with general-purpose MLLMs on X-AQA-Bench. All metrics are higher-is-better (↑), and the best result among
open-source models in each column is highlighted in bold. All reported values are multiplied by 100. Subscripts indicate the half-widths
of 95% bootstrap confidence intervals.

                                                        ID                                                 OOD
 Method
                                  Score           Category               Text        Score            Category                 Text
                                 SRCC↑      macro-F1↑        κ↑     BERTScore↑      SRCC↑      macro-F1↑         κ↑       BERTScore↑
                                                               Baselines
 Chance Level (Random)              –         42.71.8     -1.83.3        –              –        48.35.3      -3.410.4          –
 Chance Level (Frequency)           –         33.40.7      0.00.0        –              –        33.32.3       0.00.0           –
                                                         Open-Source Models
 Molmo2-8B                        8.85.5      39.61.7     4.22.6     86.50.1         15.66.8     34.93.1      0.62.4          86.00.1
 VideoLLaMA3-7B                  -7.07.7      44.32.0     4.23.1     87.00.1          7.75.2     34.22.9      -0.62.6         85.60.1
 InternVL3.5-8B                  12.15.2      41.61.7     6.52.9     87.30.1         16.18.7     53.25.3      6.310.5         83.60.1
 Keye-VL-1.5-8B                  13.96.5      42.11.9     6.73.0     87.40.1         11.98.2     33.42.6      -1.72.6         84.90.1
 MiniCPM-V 4.5                   11.85.9      43.41.9     6.53.1     87.20.1         13.48.3     39.64.3       3.44.7         86.10.1
 InternVideo3-8B-Instruct        20.65.4      45.01.8     8.73.1     87.40.1         12.78.1     50.05.3      10.97.9         86.50.1
 Eagle2.5-8B                     18.84.9      45.51.8     6.83.5     87.10.1         19.97.9     39.74.2       5.24.0         85.40.1
 LLaVA-OneVision-2               16.56.0      47.21.9    10.73.4     86.90.1          3.37.8     37.33.9       1.14.2         85.80.1
 Qwen2.5-VL-7B-Instruct           5.45.2      43.61.9     6.73.1     87.10.1         20.77.8     33.22.3      -0.60.9         85.50.1
 Qwen3-VL-8B-Instruct            22.45.2      45.91.9     7.03.4     87.10.1         12.97.1     46.15.1       4.67.6         86.50.1
 Qwen3-VL-8B-Thinking            11.75.8      48.11.9    12.53.3     86.50.1          8.97.6     52.75.3       8.19.9         86.20.1
 Qwen3.5-9B, Non-Thinking        21.85.0      48.71.8    14.13.3     87.60.1          6.34.2     53.15.3      6.910.4         86.80.1
 Qwen3.5-9B, Thinking            19.38.2      50.21.9    13.63.4     86.70.1         14.48.0     49.65.3       5.29.1         86.20.1
 X-AQA                           60.73.6      59.21.8    29.33.2     89.70.1         24.48.5     55.75.2      12.69.9         87.10.1
                                                          Proprietary Models
 Claude Sonnet 5.5               32.14.9      53.71.9     21.03.4      85.50.1       31.56.8     57.25.2     15.510.2         85.40.1
 Gemini 3.8 Flash                44.64.4      52.61.8     21.33.1      86.70.1       30.17.1     56.55.3     13.210.4         86.20.1
 GPT-6.1 Sol                     46.54.9      56.41.9     24.93.4      86.20.1       19.37.8     61.25.1     22.410.2         85.90.1


stratum when applicable. The OOD split comprises four                  tions using a sample-weighted Fisher z transformation [23]:
held-out datasets: T3Set [41] for textual coaching feedback
in competitive sports, Fitness-7 [21] for exercise correct-
ness classification, KIMORE for rehabilitation scoring, and                                     P                         !
JIGSAWS [25] for surgical skill scoring. The four datasets                                          g∈G ng arctanh(ρg )
                                                                                   ρ = tanh            P                                (2)
cover all four domains and three assessment formats. All                                                   g∈G ng
samples from these datasets are included in the OOD split
and excluded from training. Overall, X-AQA-Bench con-
tains 7,101 evaluation samples across 25 data sources, com-
prising 5,366 ID and 1,735 OOD samples.                                where ρ is the aggregated SRCC for the evaluated split
                                                                       or domain, and ρg and ng denote the SRCC and num-
                                                                       ber of valid predictions for scoring group g, respectively.
                                                                       The set G includes all scoring groups with valid predic-
                                                                       tions. For categorical assessment, we report macro-F1
Evaluation Metrics. We evaluate three types of AQA                     over the reference classes and unweighted Cohen’s κ [19],
tasks using metrics tailored to their output formats. For              which accounts for chance agreement. For textual feedback,
continuous scoring, we use Spearman’s Rank Correlation                 we compute BERTScore F1 [75] against the reference re-
Coefficient (SRCC) [56] to measure the agreement between               sponses, using RoBERTa-large [39]. Categorical and tex-
predicted and reference score rankings. We form scoring                tual metrics are first computed within each data source and
groups containing samples whose scores can meaningfully                then averaged across sources, weighted by the number of
be compared, such as performances in the same sport or ap-             valid predictions. All metrics are computed on successfully
paratus event within a data source. We compute SRCC sep-               parsed predictions. We also estimate 95% confidence inter-
arately within each scoring group and aggregate the correla-           vals using 10,000 recording-level bootstrap resamples.


                                                                   5
Table 2. Comparison with dataset-specific specialists. In Fitness-            on 16 NVIDIA H20 GPUs with a global batch size of 32 and
AQA, KIE and KFE refer to knees-inward and knees-forward er-                  bfloat16 precision. We adaptively sample up to 128 frames
rors, respectively. On KIMORE, X-AQA is evaluated in a zero-                  per video clip, using higher frame rates for shorter clips and
shot setting, whereas the specialist is trained on the dataset. ↑ and
                                                                              lower rates for longer clips to preserve temporal coverage.
↓ indicate higher and lower are better, respectively.
                                                                              The maximum sequence length is 32,768 tokens. Both the
                                                                              training and data random seeds are set to 42. We use the
 MTL-AQA                                          SRCC↑          R-ℓ2 ↓
                                                                              checkpoint from the end of training for evaluation.
 RICA2 [42]                                       0.9594         0.2580
 TPT [8]                                          0.9607         0.2378       4.2. Main Results
 DAE-CoRe [73]                                    0.9589            –
 CoRe [71]                                        0.9512         0.2600
                                                                              Comparison with General-Purpose MLLMs. We com-
 TSA-Net [60]                                     0.9422            –         pare X-AQA with both open-source and proprietary
 MUSDL [57]                                       0.9273         0.4510       MLLMs on X-AQA-Bench.                 The open-source mod-
 C3D-AVG-MTL [49]                                 0.9044            –         els include Molmo2-8B [18], VideoLLaMA3-7B [74],
                                                                              InternVL3.5-8B [62], Keye-VL-1.5-8B [68], MiniCPM-V
 Qwen3.5-9B (base)                                0.6464         1.8750
 X-AQA                                            0.8862         0.6948
                                                                              4.5 [70], InternVideo3-8B-Instruct [67], Eagle2.5-8B [16],
                                                                              LLaVA-OneVision-2 [2], Qwen2.5-VL-7B-Instruct [7],
                                               F1↑
                                                                              Qwen3-VL-8B, and Qwen3.5-9B. We evaluate both in-
 Fitness-AQA                                                                  struct and thinking variants of Qwen3-VL-8B, and both
                              Back Squat             Overhead Press           non-thinking and thinking modes of Qwen3.5-9B. We also
                             KIE         KFE       Elbow         Knees        include three proprietary models: Claude Sonnet 5.5 [3],
 SimSiam [17]              0.2270       0.7868     0.4145        0.5301
                                                                              Gemini 3.8 Flash, and GPT-6.1 Sol. For categorical as-
 TemporalXform [33]        0.3414       0.8319     0.4138        0.8416       sessment, we additionally report two chance-level baselines
 MD [50]                   0.4186       0.8338     0.4552        0.8452       based on uniform random predictions (random) and the em-
                                                                              pirical class distribution in the training data (frequency), re-
 Qwen3.5-9B (base)         0.0000       0.0000     0.0741        0.6224
                                                                              spectively. During evaluation, all models use a maximum
 X-AQA                     0.2378       0.8130     0.0714        0.6742
                                                                              of 128 frames, except VideoLLaMA3-7B, which is lim-
                                                                              ited to 64 frames due to its context-length constraint. The
                                               SRCC↑
 KIMORE                                                                       results are shown in Tab. 1. X-AQA surpasses all evalu-
                               E1       E2       E3       E4       E5         ated open-source and proprietary MLLMs on all four ID
 Abedi et al. [1]             0.76      0.61     0.73     0.54     0.67       metrics, demonstrating strong performance across numer-
                                                                              ical, categorical, and textual assessment. In particular, it
 Qwen3.5-9B (base)            0.00      0.00     0.00     0.00     0.00
 X-AQA                        0.35      0.45     0.47     0.50     0.18
                                                                              achieves an SRCC of 0.607, compared with 0.465 for GPT-
                                                                              6.1 Sol, the best-performing baseline on this metric. On the
 LASANA                     Accuracy↑          Balanced Accuracy↑
                                                                              OOD split, X-AQA outperforms all evaluated open-source
                                                                              MLLMs on all four metrics and is comparable with propri-
 X3D [24]                      0.8638                   0.8535                etary MLLMs. For textual feedback, it achieves the high-
 Qwen3.5-9B (base)             0.5512                   0.5669                est BERTScore of 0.871, exceeding 0.862 for Gemini 3.8
 X-AQA                         0.7706                   0.7576                Flash. These results demonstrate the effectiveness of uni-
                                                                              fied AQA training for both represented data sources and
                                                                              generalization to unseen datasets.
4. Experiments
                                                                              Comparison with Dataset-Specific Specialists. We fur-
4.1. Implementation Details
                                                                              ther compare X-AQA with dataset-specific specialists on
We fine-tune Qwen3.5-9B using LoRA [30] with a rank                           four datasets: MTL-AQA, Fitness-AQA, KIMORE, and
of 32, a scaling factor of 64, and a dropout rate of 0.05.                    LASANA. To facilitate comparison with published special-
LoRA adapters are applied to all linear layers of the lan-                    ist results, we evaluate X-AQA on the full test sets rather
guage model and visual merger. We use the AdamW [40]                          than the sampled subsets in X-AQA-Bench, using the cor-
optimizer with a weight decay of 0.1 and gradient clipping                    responding evaluation metrics. None of the test samples
at a maximum norm of 1.0. The peak learning rates are                         are included in X-AQA-40K. Specifically, we report SRCC
1 × 10−4 and 5 × 10−5 for the language model and vi-                          and relative ℓ2 error for MTL-AQA, error-detection F1 for
sual merger adapters, respectively, following a cosine decay                  Fitness-AQA, per-exercise SRCC for KIMORE, and accu-
schedule with 3% warmup and a minimum learning rate of                        racy and balanced accuracy for LASANA. X-AQA uses the
10% of the peak value. Training is performed for one epoch                    same jointly trained model without dataset-specific fine-


                                                                          6
Table 3. Effect of multi-domain learning. Single uses four independently trained domain-specific models, with each sample evaluated
by the corresponding model. Single (one pass) trains each model for one epoch, whereas single (same steps) repeats its domain-specific
training data to match the number of optimization steps used by joint. Joint trains a single model on data from all four domains. The ∆
row reports joint − single (one pass). All reported values are multiplied by 100. Subscripts indicate the half-widths of 95% bootstrap
confidence intervals.

                                                        ID                                                   OOD
 Method
                                 Score           Category                   Text        Score           Category               Text
                                SRCC↑      macro-F1↑         κ↑        BERTScore↑      SRCC↑      macro-F1↑        κ↑      BERTScore↑
 Qwen3.5-9B (base)              21.85.0      48.71.8      14.13.3          87.60.1     6.34.2      53.15.3      6.910.4       86.80.1
 Single (one pass)              59.83.7      57.71.8      26.73.3          89.80.1     10.77.7     49.95.3      5.29.4        86.80.1
 Single (same steps)            60.93.6      60.21.8      29.93.3          89.90.1     9.37.6      45.85.1      4.57.6        86.30.1
 Joint                          60.73.6      59.21.8      29.33.2          89.70.1     24.48.5     55.75.2      12.69.9       87.10.1
 ∆                              +0.92.9      +1.51.8     +2.53.3           -0.10.1     +13.68.4    +5.86.1     +7.510.5       +0.30.1

Table 4. Effect of assessment criteria. For the base model, assessment criteria are included or omitted at inference, while for X-AQA, the
corresponding settings are applied during both training and inference. The ∆ row reports X-AQA (w/ criteria) − X-AQA (w/o criteria). All
reported values are multiplied by 100. Subscripts indicate the half-widths of 95% bootstrap confidence intervals.

                                                        ID                                                    OOD
 Method
                                  Score           Category                   Text       Score           Category               Text
                                 SRCC↑      macro-F1↑         κ↑       BERTScore↑      SRCC↑      macro-F1↑        κ↑      BERTScore↑
 Base (w/o criteria)             19.25.5      45.91.8        10.83.1       87.70.1       2.07.6    52.35.3      5.210.4       86.80.1
 Base (w/ criteria)              21.85.0      48.71.8        14.13.3       87.60.1       6.34.2    53.15.3      6.910.4       86.80.1
 X-AQA (w/o criteria)            59.53.7      57.11.8        26.73.1       89.50.1      17.78.4    47.05.0      5.27.8        87.40.1
 X-AQA (w/ criteria)             60.73.6      59.21.8        29.33.2       89.70.1      24.48.5    55.75.2      12.69.9       87.10.1
 ∆                               +1.32.7      +2.11.5        +2.62.7       +0.20.1      +6.78.2    +8.75.6     +7.510.1       -0.40.1


tuning. As shown in Tab. 2, dataset-specific specialists                   joint training with four independently trained domain-
generally achieve higher scores on their respective bench-                 specific models, each evaluated on samples from its cor-
marks, while X-AQA demonstrates competitive assessment                     responding domain. We consider two settings for domain-
performance across diverse tasks with a single model. Com-                 specific training: single (one pass), where each model trains
pared with the Qwen3.5-9B base model, X-AQA improves                       on its domain data for one epoch, and single (same steps),
SRCC from 0.6464 to 0.8862 and reduces relative error                      where domain-specific samples are repeatedly drawn to
from 1.8750 to 0.6948 on MTL-AQA. On LASANA, it in-                        match the number of optimization steps in multi-domain
creases accuracy from 0.5512 to 0.7706 and balanced ac-                    joint training. As shown in Tab. 3, multi-domain learning
curacy from 0.5669 to 0.7576. On Fitness-AQA, X-AQA                        achieves comparable ID performance while outperforming
achieves an F1 of 0.8130 for knees-forward error detection,                both single-domain settings on all four OOD metrics. In
approaching the specialist result of 0.8338. Beyond these                  particular, multi-domain learning achieves an OOD SRCC
datasets represented during training, X-AQA generalizes to                 of 0.244, compared with 0.107 for single (one pass). In-
the held-out KIMORE dataset, achieving positive SRCC                       creasing single-domain training to match multi-domain op-
across all five rehabilitation exercises and reaching 0.50 on              timization steps improves ID performance but reduces OOD
E4, compared with 0.54 reported by Abedi et al. [1], whose                 performance across all four metrics, with SRCC decreasing
model is trained on KIMORE. This comparison highlights                     to 0.093. These results suggest that AQA tasks across do-
the distinction between dataset-specific specialization and                mains share transferable assessment knowledge, enabling
cross-domain generalization, with X-AQA supporting di-                     multi-domain learning to improve generalization to unseen
verse assessment tasks and actions through a single model.                 datasets.
4.3. Ablation Study
Effect of Multi-Domain Learning. We investigate the                        Effect of Assessment Criteria. We investigate the ef-
effect of multi-domain learning by comparing multi-domain                  fect of incorporating explicit assessment criteria into model


                                                                       7
  (a) MTL-AQA (Diving)                                                             (b) Ego-Exo4D (Mikan Layup)
  Give one overall execution award from 0.0 to 10.0 in increments of               You assess proficiency in short videos of skilled activities. Proficiency
  0.5 … Enter vertically without residual twist, with the body                     levels: Novice, Early Expert, Intermediate Expert, Late Expert …
  straight … Consider splash with alignment and control …                          Activity: Basketball Drills – Mikan Layup

                                                 X-AQA: {"execution_award":                                                                X-AQA:
                                                 5.5, "comment": "… short of                                                               {"proficiency_level
                                                 vertical, and the splash is a                                                             ": "Late Expert"}
                                                 little bit too big. …"}
                      Video A                                                                           Video A
                                                                                                                                           X-AQA:
                                                 X-AQA: {"execution_award":
                                                                                                                                           {"proficiency_level
                                                 9.0, "comment": "… a little bit
                                                                                                                                           ": "Early Expert"}
                                                 of a wobble there, but he’s got
                      Video B                    it under control."}                                    Video B
  (c) ExeCheck (Side-Step Squat)                                                   (d) CoT-AFA (Parallel-Bars Leg Raise)
  Assess the form of this rehabilitation exercise: side step squat … The           You assess whether the parallel bars leg raise … was performed in
  dataset’s incorrect-form criteria are: Trunk rotation or forward trunk           accordance with the following action standard … Avoid swinging the
  lean …                                                                           legs or using momentum to lift them.

                                                      X-AQA:                                                                               X-AQA:
                                                      {"exercise_form":                                                                    {"form_assessment":
                                                      "correct"}                                                                           "standard"}
                      Video A                                                                           Video A

                                                      X-AQA:                                                                               X-AQA:
                                                      {"exercise_form":                                                                    {"form_assessment":
                                                      "incorrect"}                                                                         "non-standard"}
                      Video B                                                                           Video B
  (e) UpperLimb (Lifting Object)                                                   (f) CPR-Coach (Chest Compression)
  Assess whether the upper-limb exercise in the video is completed … Lift          Assess whether the specified error is present … Error: Single Hand.
  it steadily to the final raised position while maintaining the grip and          Only one hand presses on the chest; the other hand does not support
  control …                                                                        the pressing hand …

                                                      X-AQA:                                                                               X-AQA:
                                                      {"completion":                                                                       {"error_present":
                                                      "complete"}                                                                          "NO"}
                      Video A                                                                           Video A

                                                      X-AQA:                                                                               X-AQA:
                                                      {"completion":                                                                       {"error_present":
                                                      "incomplete"}                                                                        "YES"}
                      Video B                                                                           Video B


Figure 3. Qualitative examples of X-AQA. In each panel, X-AQA evaluates two different videos using the same prompt and produces
distinct assessments results based on the observed action execution and task-specific assessment criteria.


prompts for both the base model and X-AQA. As shown                                 cal scoring and categorical judgments on unseen datasets.
in Tab. 4, providing assessment criteria at inference im-
proves the base model’s ID and OOD performance, with                                4.4. Qualitative Results
OOD SRCC increasing from 0.020 to 0.063. For X-AQA,
incorporating assessment criteria during both training and                          Figure 3 presents several examples of qualitative results
inference yields further improvements, particularly on un-                          of X-AQA across diverse action domains and assessment
seen datasets. On the OOD split, SRCC increases from                                tasks. Given the same assessment prompt for two different
0.177 to 0.244, macro-F1 from 0.470 to 0.557, and Cohen’s                           videos, X-AQA produces different judgments based on the
κ from 0.052 to 0.126. The ID results also show consis-                             observed action execution. For instance, on MTL-AQA, X-
tent improvements across all four metrics. These results in-                        AQA assigns different execution scores to two diving per-
dicate that explicit assessment criteria help MLLMs apply                           formances and generates feedback describing their execu-
task-specific evaluation standards, particularly for numeri-                        tion characteristics in natural language. The remaining ex-
                                                                                    amples demonstrate its ability to assess proficiency levels


                                                                             8
and exercise correctness, identify execution errors, and de-          [4] Kumar Ashutosh and Kristen Grauman. Learning skill-
termine task completion according to task-specific assess-                attributes for transferable assessment in video. In Advances
ment criteria. These examples demonstrate X-AQA’s ability                 in Neural Information Processing Systems, 2025. 3
to perform diverse assessment tasks using assessment crite-           [5] Kumar Ashutosh, Tushar Nagarajan, Georgios Pavlakos,
ria within a unified question-answering framework.                        Kris Kitani, and Kristen Grauman. ExpertAF: Expert action-
                                                                          able feedback from video. In Proceedings of the IEEE/CVF
                                                                          Conference on Computer Vision and Pattern Recognition
5. Conclusion                                                             (CVPR), pages 13582–13594, 2025. 2, 3, 4
                                                                      [6] Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui
We present X-AQA, the first unified training and evalua-
                                                                          Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao,
tion framework for general-purpose AQA with MLLMs. X-
                                                                          Chunjiang Ge, Wenbin Ge, Zhifang Guo, Qidong Huang,
AQA-40K unifies supervision from 22 data sources across                   Jie Huang, Fei Huang, Binyuan Hui, Shutong Jiang, Zhao-
four domains, enabling a single model to produce numerical                hai Li, Mingsheng Li, Mei Li, Kaixin Li, Zicheng Lin, Jun-
scores, categorical judgments, and textual feedback through               yang Lin, Xuejing Liu, Jiawei Liu, Chenglong Liu, Yang Liu,
question answering. X-AQA-Bench evaluates assessment                      Dayiheng Liu, Shixuan Liu, Dunjie Lu, Ruilin Luo, Chenxu
performance and generalization to unseen datasets. X-AQA                  Lv, Rui Men, Lingchen Meng, Xuancheng Ren, Xingzhang
outperforms all evaluated open-source MLLMs across the                    Ren, Sibo Song, Yuchong Sun, Jun Tang, Jianhong Tu, Jian-
benchmark metrics and achieves competitive performance                    qiang Wan, Peng Wang, Pengfei Wang, Qiuyue Wang, Yux-
relative to proprietary models. Ablation studies show that                uan Wang, Tianbao Xie, Yiheng Xu, Haiyang Xu, Jin Xu,
multi-domain learning and explicit assessment criteria im-                Zhibo Yang, Mingkun Yang, Jianxin Yang, An Yang, Bowen
                                                                          Yu, Fei Zhang, Hang Zhang, Xi Zhang, Bo Zheng, Humen
prove generalization to unseen datasets. Our data, bench-
                                                                          Zhong, Jingren Zhou, Fan Zhou, Jing Zhou, Yuanzhi Zhu,
mark, and model provide a foundation for general-purpose
                                                                          and Ke Zhu. Qwen3-VL technical report. arXiv preprint
AQA across diverse tasks and domains.                                     arXiv:2511.21631, 2025. 2
                                                                      [7] Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin
Acknowledgement                                                           Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun
                                                                          Tang, Humen Zhong, Yuanzhi Zhu, Mingkun Yang, Zhao-
This work was supported by the Beijing Natural Science                    hai Li, Jianqiang Wan, Pengfei Wang, Wei Ding, Zheren
Foundation (Grant No. L252171), the Capital’s Funds for                   Fu, Yiheng Xu, Jiabo Ye, Xi Zhang, Tianbao Xie, Zesen
Health Improvement and Research (Grant No. 2026-2-                        Cheng, Hang Zhang, Zhibo Yang, Haiyang Xu, and Jun-
2191), and Huawei’s AI Hundred Schools Program.                           yang Lin. Qwen2.5-VL technical report. arXiv preprint
                                                                          arXiv:2502.13923, 2025. 6
LLM Usage Statement                                                   [8] Yang Bai, Desen Zhou, Songyang Zhang, Jian Wang, Errui
                                                                          Ding, Yu Guan, Yang Long, and Jingdong Wang. Action
We use OpenAI Codex for code implementation and experi-                   quality assessment with temporal parsing transformer. In
ment management, including autonomous multi-step work-                    European Conference on Computer Vision, pages 422–438,
flows under author direction. We use ChatGPT to polish                    2022. 6
the language and clarity of author-written manuscript text.           [9] Edoardo Bianchi, Jacopo Staiano, and Antonio Liotta.
ChatGPT also assists in refining author-prepared related-                 ProfVLM: A lightweight video-language model for multi-
                                                                          view proficiency estimation. Computer Vision and Image
work and citation materials, figures, and data preparation
                                                                          Understanding, 268:104749, 2026. 3
materials. The research ideas, hypotheses, scientific claims,
                                                                     [10] Shengcao Cao, Zijun Wei, Jason Kuen, Kangning Liu,
and conclusions originate from the authors. The authors re-               Lingzhi Zhang, Jiuxiang Gu, HyunJoon Jung, Liang-Yan
tain full responsibility for the implementation, experimental             Gui, and Yu-Xiong Wang. Refer to any segmentation mask
results, and all content of the paper.                                    group with vision-language prompts. In Proceedings of
                                                                          the IEEE/CVF International Conference on Computer Vision
References                                                                (ICCV), pages 21853–21863, 2025. 4
                                                                     [11] Marianna Capecci, Maria Gabriella Ceravolo, Francesco
 [1] Ali Abedi, Mobin Malmirian, and Shehroz S. Khan.                     Ferracuti, Martina Grugnetti, Sabrina Iarlori, Sauro Longhi,
     Cross-modal video to body-joints augmentation for re-                Luca Romeo, and Federica Verdini. An instrumental ap-
     habilitation exercise quality assessment. arXiv preprint             proach for monitoring physical exercises in a visual marker-
     arXiv:2306.09546, 2023. 6, 7                                         less scenario: A proof of concept. Journal of Biomechanics,
 [2] Xiang An, Yin Xie, Feilong Tang, et al. LLaVA-OneVision-             69:70–80, 2018. 2, 3, 6
     2: Towards Next-Generation Perceptual Intelligence. arXiv       [12] Marianna Capecci, Maria Gabriella Ceravolo, Francesco
     preprint arXiv:2605.25979, 2026. 6                                   Ferracuti, Sabrina Iarlori, Ville Kyrki, Andrea Monteriù,
 [3] Anthropic. Introducing Claude Sonnet 5.5. https://                   Luca Romeo, and Federica Verdini. A hidden semi-Markov
     www.anthropic.com/claude-sonnet-5-5, 2026.                           model based approach for rehabilitation exercise assessment.
     6                                                                    Journal of Biomedical Informatics, 78:1–11, 2018.


                                                                 9
[13] Marianna Capecci, Maria Gabriella Ceravolo, Francesco                      Luca Zappella, Benjamı́n Béjar, David D Yuh, Chi Chi-
     Ferracuti, Sabrina Iarlori, Andrea Monteriù, Luca Romeo,                  ung Grace Chen, René Vidal, Sanjeev Khudanpur, and Gre-
     and Federica Verdini. The KIMORE dataset: Kinematic as-                    gory D Hager. JHU-ISI gesture and skill assessment working
     sessment of movement and clinical scores for remote moni-                  set (JIGSAWS): A surgical activity dataset for human motion
     toring of physical rehabilitation. IEEE Transactions on Neu-               modeling. In MICCAI Workshop on Modeling and Monitor-
     ral Systems and Rehabilitation Engineering, 27(7):1436–                    ing of Computer Assisted Interventions (M2CAI), pages 1–
     1448, 2019. 2, 6                                                           10, 2014. 3, 5, 8
[14] Andrej Černek, Jan Sedmidubský, Petra Budı́ková, Miriama           [26] Google DeepMind. Gemini 3.8 Flash Model Card. https:
     Jánošová, Lukáš Katzer, and Michal Procházka. REHAB24-               / / deepmind . google / models / model - cards /
     6: A multi-modal dataset of physical rehabilitation exercises.             gemini-3-8-flash/, 2026. 2
     Zenodo. https : / / doi . org / 10 . 5281 / zenodo .
                                                                           [27] Kristen Grauman, Andrew Westbury, Lorenzo Torresani,
     13305826, 2024. 3, 7
                                                                                Kris Kitani, Jitendra Malik, Triantafyllos Afouras, Kumar
[15] Andrej Černek, Jan Sedmidubsky, and Petra Budikova.                       Ashutosh, Vijay Baiyya, Siddhant Bansal, Bikram Boote,
     REHAB24-6: Physical therapy dataset for analyzing pose                     Eugene Byrne, Zach Chavis, Joya Chen, Feng Cheng, Fu-
     estimation methods. In Similarity Search and Applications                  Jen Chu, Sean Crane, Avijit Dasgupta, Jing Dong, Maria
     (SISAP 2024), pages 18–33. Springer, 2025. 3, 4, 7                         Escobar, Cristhian Forigua, Abrham Gebreselasie, Sanjay
[16] Guo Chen, Zhiqi Li, Shihao Wang, et al. Eagle 2.5: Boosting                Haresh, Jing Huang, Md Mohaiminul Islam, Suyog Jain,
     Long-Context Post-Training for Frontier Vision-Language                    Rawal Khirodkar, Devansh Kukreja, Kevin J Liang, Jia-
     Models. arXiv preprint arXiv:2504.15271, 2025. 6                           Wei Liu, Sagnik Majumder, Yongsen Mao, Miguel Mar-
[17] Xinlei Chen and Kaiming He. Exploring simple siamese rep-                  tin, Effrosyni Mavroudi, Tushar Nagarajan, Francesco Ra-
     resentation learning. In Proceedings of the IEEE/CVF Con-                  gusa, Santhosh Kumar Ramakrishnan, Luigi Seminara, Ar-
     ference on Computer Vision and Pattern Recognition, pages                  jun Somayazulu, Yale Song, Shan Su, Zihui Xue, Ed-
     15750–15758, 2021. 6                                                       ward Zhang, Jinxu Zhang, Angela Castillo, Changan Chen,
[18] Christopher Clark, Jieyu Zhang, Zixian Ma, et al. Molmo2:                  Xinzhu Fu, Ryosuke Furuta, Cristina Gonzalez, Prince
     Open Weights and Data for Vision-Language Models with                      Gupta, Jiabo Hu, Yifei Huang, Yiming Huang, Weslie
     Video Understanding and Grounding.              arXiv preprint             Khoo, Anush Kumar, Robert Kuo, Sach Lakhavani, Miao
     arXiv:2601.10611, 2026. 6                                                  Liu, Mi Luo, Zhengyi Luo, Brighid Meredith, Austin
[19] Jacob Cohen. A coefficient of agreement for nominal scales.                Miller, Oluwatumininu Oguntola, Xiaqing Pan, Penny Peng,
     Educational and Psychological Measurement, 20(1):37–46,                    Shraman Pramanick, Merey Ramazanova, Fiona Ryan,
     1960. 5                                                                    Wei Shan, Kiran Somasundaram, Chenan Song, Audrey
[20] Hazel Doughty, Dima Damen, and Walterio Mayol-Cuevas.                      Southerland, Masatoshi Tateno, Huiyu Wang, Yuchen Wang,
     Who’s better? who’s best? pairwise deep ranking for skill                  Takuma Yagi, Mingfei Yan, Xitong Yang, Zecheng Yu,
     determination. In Proceedings of the IEEE/CVF Conference                   Shengxin Cindy Zha, Chen Zhao, Ziwei Zhao, Zhifan Zhu,
     on Computer Vision and Pattern Recognition (CVPR), pages                   Jeff Zhuo, Pablo Arbelaez, Gedas Bertasius, Dima Damen,
     6057–6066, 2018. 2                                                         Jakob Engel, Giovanni Maria Farinella, Antonino Furnari,
[21] Sai Prashanth Duddela, Priya Kamath, Rakshith Bhandary,                    Bernard Ghanem, Judy Hoffman, C. V. Jawahar, Richard
     S Ashlesh Pai, Pratham PN, Advith P, and Abhishek                          Newcombe, Hyun Soo Park, James M. Rehg, Yoichi Sato,
     Mashetty. A multi-view raw video dataset of seven fitness ex-              Manolis Savva, Jianbo Shi, Mike Zheng Shou, and Michael
     ercises with good/bad form labels. Mendeley Data, Version                  Wray. Ego-Exo4D: Understanding skilled human activity
     2. https://doi.org/10.17632/kgbb3yn47p.2,                                  from first- and third-person perspectives. In Proceedings of
     2026. 3, 5, 6                                                              the IEEE/CVF Conference on Computer Vision and Pattern
                                                                                Recognition (CVPR), pages 19383–19400, 2024. 3
[22] Miguel Monte e Freitas, Rui Henriques, Ricardo Rei, and
     Pedro Henrique Martins. Can vision language models judge              [28] Yiwen Gu, Mahir Patel, and Margrit Betke. ExeChecker:
     action quality? an empirical evaluation. In Proceedings of                 Where did I go wrong? In Computer Vision – ECCV 2024
     the IEEE/CVF Conference on Computer Vision and Pattern                     Workshops, pages 340–355. Springer, 2025. 3, 7
     Recognition (CVPR) Workshops, pages 8874–8883, 2026. 2                [29] Hanna Hoffmann, Isabel Funke, Philipp Peters, Danush Ku-
[23] Ronald A. Fisher. On the “probable error” of a coefficient                 mar Venkatesh, Jan Egger, Dominik Rivoir, Rainer Röhrig,
     of correlation deduced from a small sample. Metron, 1(4):                  Frank Hölzle, Sebastian Bodenstedt, Marie-Christin Wille-
     3–32, 1921. 5                                                              mer, Stefanie Speidel, and Behrus Puladi. AIxSuture: vision-
[24] Isabel Funke, Sebastian Bodenstedt, Felix von Bechtol-                     based assessment of open suturing skills. International Jour-
     sheim, Florian Oehme, Michael Maruschke, Stefanie Her-                     nal of Computer Assisted Radiology and Surgery, 19(6):
     rlich, Jürgen Weitz, Marius Distler, Sören Torge Mees,                   1045–1052, 2024. 3, 4, 9
     and Stefanie Speidel. A benchmark for video-based la-                 [30] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-
     paroscopic skill analysis and assessment. arXiv preprint                   Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen.
     arXiv:2602.09927, 2026. 3, 4, 6, 10                                        LoRA: Low-rank adaptation of large language models. In In-
[25] Yixin Gao, S Swaroop Vedula, Carol E Reiley, Narges Ah-                    ternational Conference on Learning Representations, 2022.
     midi, Balakrishnan Varadarajan, Henry C Lin, Lingling Tao,                 6


                                                                      10
[31] International Gymnastics Federation. Rules. https://                    ment using a newly created cricket batsman video dataset.
     www.gymnastics.sport/site/rules/. 4, 1, 2                               In Proceedings of the IEEE/CVF Winter Conference on Ap-
[32] International Skating Union.          Figure skating rules.             plications of Computer Vision, pages 5470–5478, 2025. 3
     https://www.isu.org/en/figure- skating/                            [44] S. Nandana, M. Thenmozhi Dharshini, Vismaya
     rules / figure - skating - rules / figure -                             Viswanathan, and Binoy B. Nair. An upper limb stroke
     skating-rule. 4, 2                                                      rehabilitation exercise video dataset. Data in Brief, 66:
[33] Simon Jenni, Givi Meishvili, and Paolo Favaro. Video repre-             112819, 2026. 3, 8
     sentation learning by recognizing temporal transformations.        [45] Sao Mai Nguyen, Maxime Devanne, Olivier Remy-Neris,
     In European Conference on Computer Vision, pages 425–                   Mathieu Lempereur, and André Thepaut. A medical low-
     442, 2020. 6                                                            back pain physical rehabilitation database for human body
[34] Yanli Ji, Lingfeng Ye, Huili Huang, Lijing Mao, Yang Zhou,              movement analysis. In International Joint Conference on
     and Lingling Gao. Localization-assisted uncertainty score               Neural Networks (IJCNN), 2024. 3, 7
     disentanglement network for action quality assessment. In          [46] OpenAI. Introducing GPT-6.1 Sol. https://openai.
     Proceedings of the 31st ACM International Conference on                 com/index/introducing- gpt- 6- 1- sol/, 2026.
     Multimedia, pages 8590–8597, 2023. 3, 4, 2                              2
[35] Jianwei Li, Jun Xue, Rui Cao, Xiaoxia Du, Siyu Mo, Ke-             [47] Sunny Panchal, Apratim Bhattacharyya, Guillaume Berger,
     hao Ran, and Zeyan Zhang. FineRehab: A multi-modality                   Antoine Mercier, Cornelius Böhm, Florian Dietrichkeit,
     and multi-task dataset for rehabilitation analysis. In Pro-             Reza Pourreza, Xuanlin Li, Pulkit Madan, Mingu Lee, Mark
     ceedings of the IEEE/CVF Conference on Computer Vision                  Todorovich, Ingo Bax, and Roland Memisevic. What to say
     and Pattern Recognition Workshops (CVPRW), pages 3184–                  and when to say it: Live fitness coaching as a testbed for
     3193, 2024. 2                                                           situated interaction. In Advances in Neural Information Pro-
[36] Yicong Li and Howard Leung. FineGrade: A rule-consistent                cessing Systems, pages 75853–75882, 2024. 3, 6
     scoring framework for fine-grained action quality assess-
                                                                        [48] Paritosh Parmar and Brendan Tran Morris. Action quality as-
     ment. In Proceedings of the IEEE/CVF Conference on
                                                                             sessment across multiple actions. In 2019 IEEE Winter Con-
     Computer Vision and Pattern Recognition (CVPR) Findings,
                                                                             ference on Applications of Computer Vision (WACV), pages
     pages 8258–8267, 2026. 2
                                                                             1468–1476, 2019. 2, 3, 1
[37] Yuan-Ming Li, Wei-Jin Huang, An-Lan Wang, Ling-An
                                                                        [49] Paritosh Parmar and Brendan Tran Morris. What and how
     Zeng, Jing-Ke Meng, and Wei-Shi Zheng. EgoExo-Fitness:
                                                                             well you performed? a multitask learning approach to action
     Towards egocentric and exocentric full-body action under-
                                                                             quality assessment. In Proceedings of the IEEE/CVF Confer-
     standing. In European Conference on Computer Vision
                                                                             ence on Computer Vision and Pattern Recognition (CVPR),
     (ECCV), pages 363–382. Springer, 2024. 3, 4, 5
                                                                             pages 304–313, 2019. 2, 3, 6, 1
[38] Bin Lin, Yang Ye, Bin Zhu, Jiaxi Cui, Munan Ning, Peng Jin,
                                                                        [50] Paritosh Parmar, Amol Gharat, and Helge Rhodin. Do-
     and Li Yuan. Video-LLaVA: Learning united visual repre-
                                                                             main knowledge-informed self-supervised representations
     sentation by alignment before projection. In Proceedings of
                                                                             for workout form assessment. In European Conference on
     the 2024 Conference on Empirical Methods in Natural Lan-
                                                                             Computer Vision (ECCV), pages 105–123. Springer, 2022.
     guage Processing, pages 5971–5984. Association for Com-
                                                                             2, 3, 6, 5
     putational Linguistics, 2024. 2
[39] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-                [51] Rohith Peddi, Shivvrat Arya, Bharath Challa, Likhitha Pal-
     dar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke                      lapothula, Akshay Vyas, Bhavya Gouripeddi, Qifan Zhang,
     Zettlemoyer, and Veselin Stoyanov. RoBERTa: A ro-                       Jikai Wang, Vasundhara Komaragiri, Eric Ragan, Nicholas
     bustly optimized BERT pretraining approach. arXiv preprint              Ruozzi, Yu Xiang, and Vibhav Gogate. CaptainCook4D: A
     arXiv:1907.11692, 2019. 5                                               dataset for understanding errors in procedural activities. In
[40] Ilya Loshchilov and Frank Hutter. Decoupled weight de-                  Advances in Neural Information Processing Systems, pages
     cay regularization. In International Conference on Learning             135626–135679, 2024. 3, 9
     Representations, 2019. 6                                           [52] Hamed Pirsiavash, Carl Vondrick, and Antonio Torralba. As-
[41] Ji Ma, Jiale Wu, Haoyu Wang, Yanze Zhang, Xiao Xie,                     sessing the quality of actions. In Computer Vision – ECCV
     Zheng Zhou, Hui Zhang, Jiachen Wang, and Yingcai Wu.                    2014, pages 556–571. Springer, 2014. 2
     T3Set: A multimodal dataset with targeted suggestions for          [53] Mengshi Qi, Yeteng Wu, Wulian Yun, Xianlin Zhang, and
     LLM-based virtual coach in table tennis training. In Pro-               Huadong Ma. Explainable action form assessment by ex-
     ceedings of the 31st ACM SIGKDD Conference on Knowl-                    ploiting multimodal chain-of-thoughts reasoning. IEEE
     edge Discovery and Data Mining V.2, pages 5686–5697,                    Transactions on Image Processing, 35:6371–6384, 2026. 3,
     2025. 3, 5                                                              4
[42] Abrar Majeedi, Viswanatha Reddy Gajjala, Satya Sai Srinath         [54] Qwen Team. Qwen3.5: Towards native multimodal agents.
     Namburi GNVV, and Yin Li. RICA2 : Rubric-informed, cal-                 Qwen blog. https://qwen.ai/blog?id=qwen3.5,
     ibrated assessment of actions. In European Conference on                2026. 2
     Computer Vision, 2024. 6                                           [55] Minwoo Seong, Gwangbin Kim, Dohyeon Yeo, Yumin
[43] Tevin Moodley and Dustin Terence van der Haar. I3D-AE-                  Kang, Heesan Yang, Joseph DelPreto, Wojciech Matusik,
     LSTM: A 2-stream autoencoder for action quality assess-                 Daniela Rus, and SeungJun Kim. MultiSenseBadminton:


                                                                   11
     Wearable sensor-based biomechanical dataset for evaluation           [68] Biao Yang, Bin Wen, Boyang Ding, et al. Kwai Keye-VL 1.5
     of badminton performance. Scientific Data, 11(1):343, 2024.               Technical Report. arXiv preprint arXiv:2509.01563, 2025. 6
     3                                                                    [69] Hao Yin, Lijun Gu, Paritosh Parmar, Lin Xu, Tianxiao Guo,
[56] Charles Spearman. The proof and measurement of associa-                   Xiujin Liu, Weiwei Fu, Yang Zhang, and Tianyou Zheng.
     tion between two things. The American Journal of Psychol-                 FLEX: A largescale multimodal, multiview dataset for learn-
     ogy, 15(1):72–101, 1904. 5                                                ing structured representations for fitness action quality as-
[57] Yansong Tang, Zanlin Ni, Jiahuan Zhou, Danyang Zhang,                     sessment. arXiv preprint arXiv:2506.03198, 2025. 3
     Jiwen Lu, Ying Wu, and Jie Zhou. Uncertainty-aware score             [70] Tianyu Yu, Zefan Wang, Chongyi Wang, et al. MiniCPM-V
     distribution learning for action quality assessment. In Pro-              4.5: Cooking Efficient MLLMs via Architecture, Data, and
     ceedings of the IEEE/CVF Conference on Computer Vision                    Training Recipe. arXiv preprint arXiv:2509.18154, 2025. 6
     and Pattern Recognition, pages 9839–9848, 2020. 6                    [71] Xumin Yu, Yongming Rao, Wenliang Zhao, Jiwen Lu, and
[58] Yansong Tang, Jinpeng Liu, Aoyang Liu, Bin Yang, Wenxun                   Jie Zhou. Group-aware contrastive regression for action
     Dai, Yongming Rao, Jiwen Lu, Jie Zhou, and Xiu Li.                        quality assessment. In Proceedings of the IEEE/CVF Inter-
     FLAG3D: A 3D fitness activity dataset with language in-                   national Conference on Computer Vision, pages 7919–7928,
     struction. In Proceedings of the IEEE/CVF Conference on                   2021. 2, 6
     Computer Vision and Pattern Recognition (CVPR), pages                [72] Ling-An Zeng, Fa-Ting Hong, Wei-Shi Zheng, Qi-Zhi Yu,
     22106–22117, 2023. 3, 5                                                   Wei Zeng, Yao-Wei Wang, and Jian-Huang Lai. Hybrid
[59] Yansong Tang, Aoyang Liu, Jinpeng Liu, Shiyi Zhang,                       dynamic-static context-aware attention network for action
     Wenxun Dai, Jie Zhou, Xiu Li, and Jiwen Lu. FLAG3D++:                     assessment in long videos. In Proceedings of the 28th ACM
     A benchmark for 3D fitness activity comprehension with lan-               International Conference on Multimedia, pages 2526–2534,
     guage instruction. IEEE Transactions on Pattern Analysis                  2020. 3, 4, 2
     and Machine Intelligence, 47(11):9731–9748, 2025. 3, 5               [73] Boyu Zhang, Jiayuan Chen, Yinfei Xu, Hui Zhang, Xu Yang,
[60] Shunli Wang, Dingkang Yang, Peng Zhai, Chixiao Chen, and                  and Xin Geng. Auto-encoding score distribution regression
     Lihua Zhang. TSA-Net: Tube self-attention network for ac-                 for action quality assessment. Neural Computing and Appli-
     tion quality assessment. In Proceedings of the 29th ACM                   cations, 36:929–942, 2024. 6
     International Conference on Multimedia, pages 4902–4910,             [74] Boqiang Zhang, Kehan Li, Zesen Cheng, et al. VideoL-
     2021. 6                                                                   LaMA 3: Frontier Multimodal Foundation Models for Image
[61] Shunli Wang, Shuaibing Wang, Dingkang Yang, Mingcheng                     and Video Understanding. arXiv preprint arXiv:2501.13106,
     Li, Haopeng Kuang, Xiao Zhao, Liuzhen Su, Peng Zhai,                      2025. 6
     and Lihua Zhang. CPR-Coach: Recognizing composite er-
                                                                          [75] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Wein-
     ror actions based on single-class training. In Proceedings of
                                                                               berger, and Yoav Artzi. BERTScore: Evaluating text gener-
     the IEEE/CVF Conference on Computer Vision and Pattern
                                                                               ation with BERT. In International Conference on Learning
     Recognition (CVPR), pages 18782–18792, 2024. 3, 9
                                                                               Representations, 2020. 5
[62] Weiyun Wang, Zhangwei Gao, Lixin Gu, et al.               In-
                                                                          [76] Kaili Zheng, Kaiwen Wang, Xun Zhu, Qingyuan Yang,
     ternVL3.5: Advancing Open-Source Multimodal Models
                                                                               Chenyi Guo, and Ji Wu. FitAQA: A benchmark of fitness ac-
     in Versatility, Reasoning, and Efficiency. arXiv preprint
                                                                               tion quality assessment for multimodal large language mod-
     arXiv:2508.18265, 2025. 6
                                                                               els. arXiv preprint arXiv:2608.08736, 2026. 2
[63] World Aquatics.        Diving rules.     https : / / www .
     worldaquatics.com/diving/rules. 4, 1
[64] Qingjun Xing, Xuyang Xing, Ping Guo, Zhenhui Tang, and
     Yanfei Shen. LLM-FMS: A fine-grained dataset for func-
     tional movement screen action quality assessment. PLOS
     ONE, 20(3):e0313707, 2025. 3, 4, 8
[65] Huangbiao Xu, Huanqi Wu, Xiao Ke, Jiaxin Cai, Junyi Wu,
     and Jinglin Xu. MoAKE: Toward unified all-in-one action
     quality assessment via mixture of action knowledge experts.
     In European Conference on Computer Vision (ECCV), 2026.
     2
[66] Jinglin Xu, Yongming Rao, Xumin Yu, Guangyi Chen, Jie
     Zhou, and Jiwen Lu. FineDiving: A fine-grained dataset for
     procedure-aware action quality assessment. In Proceedings
     of the IEEE/CVF Conference on Computer Vision and Pat-
     tern Recognition (CVPR), pages 2949–2958, 2022. 2
[67] Ziang Yan, Sheng Xia, Jiashuo Yu, Yue Wu, Tianxiang Jiang,
     Songze Li, Kanghui Tian, Yicheng Xu, Yinan He, Kai Chen,
     Limin Wang, Yu Qiao, and Yi Wang. InternVideo3: Agen-
     tify foundation models with multimodal contextual reason-
     ing. arXiv preprint arXiv:2606.12195, 2026. 6


                                                                     12
                X-AQA: Unifying Action Quality Assessment with Multimodal
                   Large Language Models and Multi-Domain Learning
                                                   Supplementary Material
A. Dataset Preprocessing                                                   QA example (continued)
                                                                           Assistant
In this section, we describe the preprocessing of each source
                                                                           {”execution award”: 8.5}
dataset, including video preparation, assessment criteria
collection, and QA construction.
                                                                          A.2. MTL-AQA
A.1. AQA-7                                                                MTL-AQA [49] contains diving videos from international
AQA-7 [48] contains videos from seven competitive events:                 competitions, annotated with seven judges’ scores and
individual 10-m platform diving, gymnastics vault, Big Air                broadcast commentary. We follow the official Split 0 and
skiing and snowboarding, synchronized 3-m springboard                     reconstruct video clips at 25 fps from the released RGB
and 10-m platform diving, and trampoline. Each video is                   frame sequences. For numerical scoring, we use the me-
annotated with a total score, with degrees of difficulty ad-              dian of the seven raw judge scores, ranging from 0.0 to
ditionally provided for individual diving and vault. We use               10.0 in increments of 0.5. We clean the commentary by
the released temporally normalized clips and official Split-              removing scores, rankings, biographical information, and
4 for six sports, excluding trampoline because no split is                irrelevant broadcast speech, excluding empty or unmatched
provided. For individual diving and vault, where the re-                  commentary. The available scoring and commentary anno-
leased scores aggregate assessments from multiple judges,                 tations are combined into a single QA sample for each clip.
we derive execution score proxies from the total score S                  Similar to AQA-7, we adopt visually observable execution
and difficulty D as S/(3D) and S − D, rounded to the                      criteria from the FINA rules for 2009–2013 and 2015–2017,
nearest 0.5 and 0.1, respectively. For Big Air and synchro-               selecting the appropriate edition according to the competi-
nized diving, we retain the original panel scores. We se-                 tion [63]. The assessment prompts specify the dive and its
lect historical scoring rules corresponding to the competi-               degree of difficulty, while the target score reflects execution
tion periods represented in AQA-7. For diving, we follow                  quality rather than the competition total. An example QA
the January 2010 FINA Diving Officials Manual [63]. For                   pair is shown below.
vault, we use visually observable execution faults from the
FIG men’s Codes of Points for 2009–2012 and 2013–2016                      System
and women’s Codes of Points for 2006–2008, 2009–2012,                       You are one execution judge at a 10m platform diving
and 2013–2016 [31]. When the competition year cannot                       competition. Give one overall execution award from 0.0 to 10.0
be determined, we retain criteria shared across the relevant               in increments of 0.5. Give a brief English commentary in one
editions. An example QA pair for 10-m platform diving is                   or a few sentences, speaking naturally as during a sports
shown below.                                                               broadcast. ... Judge execution independently of difficulty. The
                                                                           announced dive describes the intended movement; its difficulty
 System                                                                    does not earn execution credit. ...
  You are one execution judge at a 10-m platform diving                    User
 competition. Give one overall execution award from 0.0 to 10.0            <video>
 in increments of 0.5. ... Deduct 0.5-2.0 for insufficient take-off        Dive: forward 3 1/2 somersaults, pike position
 height or confidence, failure to take off from the end of the             Degree of difficulty: 3.0
 platform, or twisting visibly initiated on the platform. ...              Expected execution: Begin facing the water and rotate forward,
 Throughout flight and entry, keep the feet together and toes              away from the board or platform. Complete 3 1/2 somersaults
 pointed. Deduct 0.5-2.0 for flight-position faults. ... For a             with no twists about the body’s long axis. Show a clear pike:
 head-first entry, extend the arms beyond the head in line with            bend at the hips while keeping the knees straight, feet together
 the body and bring the hands close together. If one or both               and toes pointed. ...
 arms remain below the head, the award must not exceed 4.5. ...            Assess the execution of this dive.
 Form one overall-impression award using the quality scale and             Assistant
 execution criteria, without assigning equal phase weights. ...            {”execution award”: 8.0, ”comment”: ”It’s so graceful, and
 User                                                                      you see that he’s absolutely ripped that entry. There’s barely a
 <video>                                                                   splash, drags all the bubbles down with him.”}
 As one judge, what execution award would you give this dive?



                                                                      1
      Rhythmic Gymnastics                    FineFS                     QA example (continued)
                                                                        actual interval is observable. File length, camera cuts and
                                                                        preparation are not competition time. Boundary: 0.30 for each
                                                                        body or apparatus occurrence touching the floor outside the
                                                                        boundary. ...
                                                                        User
                                                                        <video>
                                                                        Apparatus: Ball.
                                                                        Assess this complete individual routine and return its execution
                                                                        score and additional penalty.
                                                                        Assistant
                                                                        {”execution score”: 8.3, ”penalty”: 0.00}


Figure 4. Examples of broadcast scoreboard masking in Rhythmic         A.4. FineFS
Gymnastics and FineFS. The top row shows the original video            FineFS [34] contains figure-skating competition programs
frames, while the bottom row shows the corresponding frames
                                                                       with temporally annotated elements and individual judges’
with blurred score panels.
                                                                       grades of execution (GOE). To limit video length, we use
                                                                       the annotated time intervals to select individual elements
A.3. Rhythmic Gymnastics                                               from full competition programs. We take the median of the
                                                                       raw judge grades as the scoring target, ranging from −5 to
Rhythmic Gymnastics [72] contains complete individual                  5 in increments of 0.5. This target reflects element-level
routines from FIG competitions, annotated with execution               execution quality rather than converted GOE points or pro-
scores and additional penalties for each apparatus. We                 gram component scores. We verify competition identities
retain the released apparatus-wise split and construct two             against official results and use different competitions for
scoring targets for each routine: execution score and addi-            training and testing. Some videos display broadcast score
tional penalty. We exclude difficulty scores to focus on ex-           panels in the upper-left corner during the program. We ap-
ecution quality and rule violations rather than routine com-           ply the same scoreboard masking procedure with Rhythmic
plexity. Execution scores are rounded to the nearest 0.1               Gymnastics to prevent score leakage, as shown in Fig. 4
and penalties to the nearest 0.05. We incorporate selected             (right). We incorporate element-specific assessment crite-
apparatus-specific execution and penalty criteria from the             ria, including positive features, grade limits, and deduc-
FIG Rhythmic Gymnastics Codes of Points for 2013–2016                  tions, from the ISU scoring guidelines applicable to each
and 2017–2020, together with the applicable 2018 and 2019              competition season [32]. We also provide element-specific
newsletter updates [31]. The rule version is selected ac-              descriptions of the expected movements. An example for a
cording to each routine’s competition identity. Some videos            Triple Axel is shown below.
display broadcast score panels at the bottom of the frame
near the end of the routine. We locate these panels using               System
multi-scale template matching of scoreboard headings and                 You are a figure skating judge. Assess the visible execution
apply Gaussian blur to the detected regions to prevent score            quality of the specified element and give one GOE grade on a
leakage. An example is shown in Fig. 4 (left). The execu-               scale from -5 to 5 in half-point increments. ... Strong elevation
tion scores include both artistic and technical components,             and travel distance on every jump in the element. Controlled
while model inputs contain video without audio. An exam-                take-off followed by a secure landing. ... Grades +4 and +5
ple for a ball routine is shown below.                                  require strong elevation and distance, controlled take-off and
                                                                        landing, and easy, fluent execution throughout; otherwise cap
 System                                                                 the starting grade at +3. ... Fall: subtract 5. Two-foot landing
  You are a rhythmic gymnastics judge assessing a complete              or a step-out used to recover the landing: subtract 3 to 4. ...
 individual routine with ball. Estimate two separate quantities:        Subtract the total deduction from the capped starting grade,
 execution score, which includes artistic and technical                 then clamp to [-5, +5]. ...
 execution, and penalty, which contains additional time,                User
 boundary and coordinator penalties. Start execution from 10.00         <video>
 and subtract artistic and technical deductions; do not award           Competition: 2019 World Championships; Men’s singles;
 extra execution points for harder elements. Do not subtract            Short program; season 2018/19
 penalty from execution score. ... Routine time is 75-90                Element: 3A
 seconds, measured from the first movement to final complete            Action: Triple Axel
 stillness; add 0.05 per extra or missing second only when the


                                                                   2
 QA example (continued)                                                   proficiency label. We follow the official train and validation
 Expected execution: Take off from a forward outside edge                 split, using validation takes for testing because the official
 without toe-pick assistance and land backward on the outside             test labels are not publicly available. We assign basketball,
 edge of the other foot. This Axel has 3 1/2 rotations from               soccer, and rock climbing to competitive sports, and cook-
 forward take-off to backward landing. Control the body                   ing, music, and dance to general skills. Both domains share
 position through rotation and the landing, then continue with a
                                                                          the same QA format, using the four original proficiency lev-
 stable, flowing exit. Score the execution quality of this element.
                                                                          els without additional assessment criteria. An example for
 Assistant
                                                                          soccer dribbling is shown below.
 {”goe grade”: 2.0}
                                                                           System
A.5. MultiSenseBadminton                                                   You assess proficiency in short videos of skilled activities.
MultiSenseBadminton [55] contains recordings of 25 par-                    Proficiency levels: Novice, Early Expert, Intermediate Expert,
                                                                           Late Expert ...
ticipants performing two badminton strokes, forehand clear
and backhand drive, with skill-level annotations and coach-                User
ing feedback from three coaches. To accommodate long                       <video>
recordings, we divide the front-view videos into 32-second                 Activity: Soccer Drills - Dribbling
windows, each inheriting the original participant–stroke                   Assistant
skill level and merged coaching feedback. We adopt the first               {”proficiency level”: ”Intermediate Expert”}
leave-three-out participant split from the original paper, us-
ing 22 participants for training and 3 for testing. We formu-             A.7. T3Set
late assessment criteria covering movement technique and
                                                                          T3Set [41] contains table-tennis practice rounds with
shot quality based on the aspects represented in the source
                                                                          coaching feedback from two coaches across different stroke
annotations. An example for backhand drive is shown be-
                                                                          techniques. We use the complete practice-round videos, se-
low.
                                                                          lecting the remote view when available and the right view
 System                                                                   otherwise. We consolidate each coach’s feedback into an
                                                                          English paragraph and construct a separate QA sample for
  You are a badminton coach assessing a player’s overall skill in
 the stroke specified by the user. Base the assessment on the             each coach, excluding empty feedback and annotations re-
 performance visible in the video. Assessment criteria: Evaluate          quiring further review. The assessment prompt specifies the
 movement technique: grip, posture, swing mechanics,                      stroke technique and requests actionable coaching feedback
 coordination of the torso, arm and wrist, footwork, and contact          without additional scoring criteria. We combine the exist-
 point. Evaluate shot quality: accuracy, distance, direction,             ing round-level train, validation, and test partitions for OOD
 speed, and consistency across the visible attempts. Use only             evaluation. An example for forehand topspin is shown be-
 criteria that the camera view allows you to assess; an obscured          low.
 detail is not evidence of an execution error. Classify the
 player’s skill level as Beginner, Intermediate, or Expert. Briefly        System
 explain the observed strengths and weaknesses and give                     You are a table tennis coach. Assess the player’s execution
 relevant execution advice. ...                                            from the video and give specific, actionable feedback. Address
 User                                                                      the player directly in the second person. Respond in a few
 <video>                                                                   concise English sentences within a single paragraph.
 Assess the player’s overall backhand drive skill level and                User
 provide coaching feedback.                                                <video>
 Assistant                                                                 Technique: forehand topspin (topspin). Assess the player’s
 {”skill level”: ”Beginner”, ”feedback”: ”The basic posture and            execution across this practice round and provide coaching
 grip are poor, and there is no backswing.”}                               feedback.
                                                                           Assistant
A.6. Ego-Exo4D                                                             Your center of gravity is too high, and the wrist and upper arm
                                                                           direct too much force upward. ...
Ego-Exo4D [27] contains egocentric and exocentric record-
ings of skilled activities, annotated with demonstrator pro-
ficiency levels for each take. We select the designated best
                                                                          A.8. CricketVision
exocentric view and divide each recording into 32-second                  CricketVision [43] contains cricket batting videos annotated
windows, with the final window aligned to the recording                   with execution scores for five body parts: head, shoulder,
end. All windows from the same take inherit its original                  hands, hips, and feet. We combine the temporally adjacent


                                                                      3
Buildup, Execution, and FollowThrough phases into a com-                 QA example (continued)
plete batting stroke, retaining samples with valid execution             User
scores for all five body parts. The model observes the com-              <video>
plete stroke and predicts five integer scores from 1 to 10               Activity: Rock Climbing
for the Execution phase, decoded from the original annota-               Give feedback on the execution.
tion labels. We formulate assessment criteria based on the               Assistant
body-part alignment and deviation guidelines in the origi-               The climber needs to maintain pressure on the right foot and
nal paper and its supplementary scoring table. We split the              coordinate a layback move with hand placement, hip rise, and
data by source recording, keeping all strokes from the same              shoulder throw to successfully execute the move.
recording in the same split. An example is shown below.
                                                                        A.10. CoT-AFA
 System
                                                                        CoT-AFA [53] provides action videos of martial arts and
  You assess cricket batting technique. The video shows one
                                                                        fitness exercises, which we assign to competitive sports and
 batting action. Score the Execution phase, around the instant
 immediately before bat-ball contact; use the preparation and
                                                                        fitness exercises, respectively. The dataset includes human-
 follow-through only as context. Assess these five body parts           annotated form labels, explanatory captions, and category-
 independently: 1. Head: judge how well the head aligns with            specific reference forms consisting of five action steps and
 the front foot and the reference alignment through the head.           a general instruction. We incorporate these reference forms
 Greater angular departure lowers quality. 2. Shoulder: judge           into the assessment prompts and construct two QA tasks:
 the side-on stance and alignment of the two shoulders. Greater         standard/non-standard classification based on human labels
 angular departure from the appropriate alignment lowers                and explanatory feedback generation using available cap-
 quality. 3. Hands: judge hand placement relative to the vertical       tions. Both tasks use complete video clips and follow the
 line beneath the head and eyes. Greater displacement from the          released train/test split. Examples of explanatory feedback
 appropriate position lowers quality. ... Apply the alignment           for cloud hands and standard/non-standard classification for
 appropriate to the stroke: on-drive and square-drive/cut can
                                                                        a pull-up are shown below.
 require different shoulder alignment; square-drive/cut can
 require different hand placement; cut and hook allow different
                                                                         System
 hip orientation. ...
                                                                          You assess whether the pull up (a pull-up bar exercise) in the
 User
                                                                         given video was performed in accordance with the following
 <video>
                                                                         action standard. ... Step 3: The player should begin from a
 Assess the Execution phase of this cricket batting action.
                                                                         dead hang, with arms fully extended and shoulders relaxed (but
 Assistant                                                               engaged). Avoid swinging or kipping; the movement should be
 {”head”: 6, ”shoulder”: 6, ”hands”: 5, ”hips”: 6, ”feet”: 7}            controlled. ...
                                                                         User
A.9. ExpertAF                                                            <video>
ExpertAF [5] provides four-second clips of skilled activi-               Assistant
ties from Ego-Exo4D, paired with concise, actionable feed-               {”form assessment”: ”standard”}
back generated by summarizing expert commentary. We
select the annotated four-second intervals from the desig-               System
nated best exocentric view. For training, we remove du-
                                                                          You assess whether the cloud hands (a Tai chi quan technique)
plicate entries arising from multiple body-part references               in the given video was performed in accordance with the
and retrieved expert demonstrations, while retaining all re-             following action standard. Step 1: The player typically begins
leased validation samples for testing. We adapt the original             from a neutral stance or a transitional posture within the Tai
task to single-video feedback generation, using the exocen-              Chi form. The body should be relaxed, centered, and the
tric video without pose inputs or retrieved demonstrations.              weight evenly distributed, with knees slightly bent. ... Open
The prompt requests a single actionable coaching sugges-                 with one sentence naming the action and stating whether the
tion without additional assessment criteria. An example for              execution is good or bad, then explain the judgement in a few
rock climbing is shown below.                                            sentences: what the performer does, which reference steps the
                                                                         execution does or does not follow, and how to correct any error.
 System                                                                  Respond in a single paragraph.
  You analyze videos of skilled activities and give one concise,         User
 actionable coaching suggestion in a single English sentence.            <video>
 Write the feedback in the third person.                                 Assistant
                                                                         The cloud hands action in this video is bad. The character


                                                                    4
 QA example (continued)                                                 QA example (continued)
 starts with an incorrect stance, as they are not centered and          User
 balanced. Their weight distribution is uneven, and their knees         <video>
 are not bent enough. Additionally, the hand movements are not          Exercise: Svend Press
 coordinated and circular; instead, they appear jerky and               Technical point: stand shoulder-width apart
 disjointed. To improve, the character should begin by centering
                                                                        Assistant
 themselves and distributing their weight evenly, bending their
 knees slightly. They should also practice smooth, continuous           {”technical point satisfied”: ”yes”}
 hand movements that flow together, focusing on the waist’s
 coordination with the weight shift.                                   A.13. EgoExo-Fitness
                                                                       EgoExo-Fitness [37] provides full-body exercise record-
A.11. Fitness-AQA                                                      ings annotated with technical-point judgments and overall
Fitness-AQA [50] contains videos of squats and overhead                coaching feedback. We reconstruct action clips at 30 fps
presses annotated with execution errors at different tech-             from the released frame sequences and randomly select
nical points. We construct binary QA tasks by expressing               one exocentric view per action instance. We split the data
each error category as a desired form condition, with “yes”            by participant, keeping all recordings of each participant
indicating the absence of the corresponding error. For over-           in the same split. The assessment criteria are taken di-
head presses and squats, we use complete videos and deter-             rectly from the technical-point descriptions in the released
mine error presence from the annotated temporal intervals.             interpretable-action annotations. We construct two QA
For shallow squats, we extract the annotated frames as im-             tasks: binary assessment of individual technical points and
age inputs to preserve frame-level supervision. We combine             generation of overall coaching feedback. For the latter, the
the released training and validation splits for training and           prompt provides all technical points without their reference
retain the original test split. An example for the overhead            judgments, allowing the model to assess execution and gen-
press is shown below.                                                  erate feedback from the video. Examples of both tasks for
                                                                       kneeling push-ups are shown below.
 System
  You evaluate whether an exercise execution satisfies a given          System
 technical point. Return only this JSON object and nothing else:         You evaluate whether an exercise execution satisfies a given
 {”technical point satisfied”: ”yes” or ”no”}.                          technical point. Return only this JSON object and nothing else:
 User                                                                   {”technical point satisfied”: ”yes” or ”no”}.
 <video>                                                                User
 Exercise: Overhead Press                                               <video>
 Technical point: Keep the elbows in the correct position under         Exercise: Kneeling pushing-ups
 the bar, without flaring them out.                                     Technical point: Cross your feet.
 Assistant                                                              Assistant
 {”technical point satisfied”: ”yes”}                                   {”technical point satisfied”: ”yes”}


A.12. FLAG3D                                                            System
FLAG3D [58] provides 3D-annotated fitness exercises,                     You give concise, concrete feedback on exercise technique.
while FLAG3D++ [59] introduces language-based action                    Assess the execution visible in the video against the provided
standards and repetition-level quality annotations. We use              technical points. Respond in one or two sentences in the
RGB avatar renderings and segment each exercise sequence                second person.
into individual repetitions according to the annotated tem-             User
poral boundaries. Each repetition is paired with the cor-               <video>
responding technical points from the released annotations               Exercise: Kneeling pushing-ups
to construct binary QA samples. We hold out participants                Technical points:
                                                                        Cross your feet.
P009 and P010 for testing. The validation recordings are
                                                                        Keep your back straight. ... Comment on the execution.
excluded. An example for Svend Press is shown below.
                                                                        Assistant
 System                                                                 The movements were generally in accordance with the
                                                                        instructional text, performed at a fast pace, and were executed
  You evaluate whether an exercise execution satisfies a given
                                                                        smoothly. However, the back still needs to be straighter, so
 technical point. Return only this JSON object and nothing else:
                                                                        next time try to keep the back even straighter.
 {”technical point satisfied”: ”yes” or ”no”}.


                                                                   5
A.14. QEVD                                                            QA example (continued)
                                                                      <19.7 seconds> Yes! That is awesome.
QEVD [47] provides two fitness-coaching datasets: FIT-
                                                                      What would you say now?
300K for video question answering and FIT-COACH for
                                                                      Assistant
timestamped coaching feedback. FIT-300K includes high-
                                                                      Now you stopped jumping! Consistency is key to success.
level questions about exercise identity and overall execu-
tion, and fine-grained questions about specific movements
and aspects of exercise form. We exclude questions solely            A.15. Fitness-7
about action recognition and retain one question per clip.           Fitness-7 [21] contains videos of seven resistance exercises
For FIT-COACH, we construct a QA sample at each feed-                performed by 26 participants, recorded from three camera
back timestamp, using up to eight preceding seconds of               views and annotated with good/bad form labels. We use the
video and the timestamped history of earlier coaching feed-          complete front-view videos and their original labels, retain-
back within the same exercise segment. We use FIT-300K               ing one video per execution. We hold out five participants
exclusively for training, while FIT-COACH provides train-            for testing. Each QA sample asks the model to assess over-
ing data and its benchmark subset serves as the test set. Both       all exercise form using the exercise name and video, without
tasks use the released QA and coaching annotations without           additional assessment criteria. An example for the standing
additional assessment criteria. Examples of high-level QA,           dumbbell side bend is shown below.
fine-grained QA, and coaching feedback are shown below.
                                                                      System
 System                                                                Assess the exercise form in the video.
  You analyze workout videos and briefly describe the exercise        Exercise: Standing dumbbell side bend.
 and its execution. Respond in one to three concise sentences.        Determine whether the demonstrated exercise form is good or
 User                                                                 bad.
                                                                      Return only this JSON object and nothing else:
 <video>
                                                                      {”exercise form”: ”good” or ”bad”}.
 What exercise is the user doing, and how are they performing
 it?                                                                  User

 Assistant                                                            <video>
 The user is doing a downward dog pose with their body facing         Assistant
 the front. However, they need to work on pressing their heels        {”exercise form”: ”bad”}
 down towards the floor.
                                                                     A.16. KIMORE
 System                                                              KIMORE [11–13] contains recordings of five low-back-
 You answer specific questions about visible movements in            pain rehabilitation exercises performed by 78 participants,
 workout videos. Respond in one to three concise sentences.          with clinical assessments based on the ten-item Exercise
 Begin with Yes or No.                                               Accuracy Assessment Questionnaire (EAAQ). We provide
 User                                                                the exercise-specific movement instructions and the ten
 <video>                                                             EAAQ items as assessment criteria, asking the model to
 Are the user’s knees together?                                      rate each item on a five-point scale from Never to Always.
 Assistant                                                           The released clinical annotations provide the clinical Total
 No, the user’s knees are not together.                              Score (cTS) rather than individual item ratings. We there-
                                                                     fore use cTS as the reference score and sum the ten pre-
                                                                     dicted item ratings to obtain the model’s overall score. All
 System
                                                                     recordings with available RGB videos and cTS annotations
  You are a workout coach. Give one brief, timely, and useful
                                                                     are reserved for OOD evaluation. An example for the squat
 comment based on the exercise shown so far.
                                                                     exercise is shown below.
 User
 <video>                                                              System
 Previous feedback:                                                    You are a physiotherapy examiner. Evaluate the rehabilitation
 <0.0 seconds> Moving on to jumping jacks!                            exercise in the video. The exercise is Squat. The subject holds
 <4.8 seconds> Good job!                                              the arms at ninety degrees to the trunk with the elbows
 <9.1 seconds> 5 reps!                                                extended, flexes the knees up to 60–70 degrees and returns to
 <12.3 seconds> You are not moving your hands correctly.              the starting position, keeping the body aligned in the sagittal
 <15.8 seconds> You gotta move your arms too! I wanna see             plane. Rate the performance on the ten items of the Exercise
 you moving those arms.                                               Accuracy Assessment Questionnaire (EAAQ), using the scale 1


                                                                 6
 QA example (continued)                                                exercise type. We use Camera 17 RGB videos, resized
 = Never, 2 = Rarely, 3 = Sometimes, 4 = Often, 5 = Always.            while preserving the original frame indices, and select in-
 Consider the whole exercise, all repetitions, and judge only          dividual repetitions according to their annotated temporal
 what is visible in the video. - primary objective achieved: Is        boundaries. Each repetition is formulated as a binary cor-
 the primary objective of the exercise achieved (i.e., extension       rectness assessment using the released labels. Based on
 of the upper limbs, trunk rotation with upper limbs elevated to
                                                                       the dataset’s exercise descriptions, we formulate exercise-
 90 degrees, squatting, etc.)? - repetitions constant: Is the
                                                                       specific assessment criteria based on these movement de-
 exercise repeated in a constant manner? -
 movement amplitude complete: Is the amplitude of the                  scriptions, specifying observable requirements for correct
 movement complete? ... Return only this JSON object and               execution. These criteria are included in the prompts, while
 nothing else, with one score for every item: ... The clinical         supervision is provided by the original repetition-level la-
 Total Score is the sum of the ten scores.                             bels. We hold out participants 2, 3, and 6 for testing. An
 User                                                                  example for arm abduction is shown below.
 <video>
                                                                        System
 Assistant
                                                                         You judge how well one repetition of a rehabilitation exercise
 {”cTS”: 48.333}
                                                                        was performed, as a physiotherapist would. Exercise: Arm
                                                                        abduction (sideway raising of the straightened right arm)
A.17. KERAAL                                                            Performed with: right arm A correct repetition meets every one
KERAAL [45] contains recordings of three low-back-pain                  of these criteria: 1. The arm stays straight at the elbow through
                                                                        the whole repetition. 2. The arm travels sideways in the frontal
rehabilitation exercises, annotated with correct execution
                                                                        plane, not forward across the body. 3. The arm is raised at least
and exercise-specific movement errors. We resize and let-               to shoulder level. 4. The trunk stays upright, without leaning to
terbox the RGB videos to a consistent resolution and divide             the opposite side or shrugging the shoulder. 5. The arm is
longer recordings into windows of up to 32 seconds, each                lowered back to the side under control. Return only this JSON
inheriting the recording-level label. We formulate a four-              object and nothing else: {”rehabilitation form”: ”correct” or
class classification task using the correct-execution label             ”incorrect”}.
and three exercise-specific error categories, with descrip-             User
tions adapted from the dataset paper. The four answer op-               <video>
tions are shuffled deterministically for each recording. We             Assistant
use Group 3 for training and exclude Groups 1A and 2A, as               {”rehabilitation form”: ”correct”}
their videos contain robot-rendered skeleton overlays. An
example for the hiding face exercise is shown below.
                                                                       A.19. ExeCheck
 System                                                                ExeCheck [28] contains 140 recordings of ten rehabilitation
  You classify how a low-back-pain rehabilitation exercise was         exercises performed by seven participants, each recording
 performed. Return only this JSON object and nothing else:             comprising five repetitions with a correct/incorrect execu-
 {”answer”: ”<selected option letter>”}. The value must be             tion label. We extract the RGB streams and select individual
 one of the option letters shown for the current sample.               repetitions according to the released temporal boundaries.
 User                                                                  Each repetition inherits the correctness label of its source
 <video>                                                               recording. We incorporate exercise-specific assessment cri-
 Exercise: hiding face - a breathing exercise with the upper           teria adapted from the incorrect-form descriptions in its pa-
 limbs flexed 90 degrees at the shoulder and at the elbow.             per. Following the original evaluation protocol, we use the
 Possible verdicts:                                                    first six participants for training and hold out the seventh for
 A. the elbows are not bent enough
                                                                       testing. An example for arm circle is shown below.
 B. the arms are not outspread enough
 C. correct execution
                                                                        System
 D. the arms are not raised enough
                                                                         Assess the form of this rehabilitation exercise: arm circle. The
 Assistant
                                                                        dataset’s incorrect-form criteria are: Raised shoulders or bent
 {”answer”: ”C”}                                                        arms. Judge the visible repetition against these criteria.
                                                                        Incorrect means at least one listed form error; correct means
A.18. REHAB24-6                                                         the intended form is maintained. Return only this JSON object
                                                                        and nothing else: {”exercise form”: ”correct” or ”incorrect”}.
REHAB24-6 [14, 15] contains multi-view recordings of six
                                                                        User
rehabilitation exercises, with correctness labels for individ-
ual repetitions and a general movement description for each             <video>



                                                                   7
 QA example (continued)                                                  System
 Assistant                                                                Assess whether the upper-limb exercise in the video is
 {”exercise form”: ”correct”}                                            completed. Exercise candidates and expected procedures: ...
                                                                         Extending the Elbow: Begin with the elbow supported at the
A.20. LLM-FMS                                                            table and the forearm upright. Extend the elbow smoothly until
                                                                         the forearm lies along and contacts the table. Failure to achieve
LLM-FMS [64] provides RGB keyframes of 15 Functional                     that endpoint or an early stop indicates incomplete execution.
Movement Screen (FMS) movement variants, annotated                       ... Apply the procedure for the exercise shown in the video.
with item-level judgments and overall quality scores. We                 Complete means the required movement reaches its endpoint
construct one QA sample per keyframe, requiring the model                successfully; incomplete means it visibly fails or stops short.
to assess each item and predict the overall score. The as-               Assess the recorded cycle without requiring repeated cycles or
sessment criteria, including movement-specific definitions,              exact joint angles. Do not infer unseen failure from occlusion
thresholds, and scoring rules, are taken from the supplemen-             alone. Return only one JSON object and nothing else, without
                                                                         Markdown or code fences: ”completion”: ”complete” or
tary S3 Text of the source paper. We retain the released
                                                                         ”incomplete”.
item-level judgments and align the overall scores with the
                                                                         User
provided scoring rules where they determine the score, re-
taining the original annotations otherwise. We hold out ev-              <video>
ery fifth participant for testing, keeping all movements and             Assistant
recording episodes of each participant in the same split. An             {”completion”: ”incomplete”}
example for the deep squat is shown below.
                                                                        A.22. JIGSAWS
 System
                                                                        JIGSAWS [25] contains robotic surgical training trials cov-
  You assess the quality of the Functional Movement Screen
                                                                        ering suturing, knot tying, and needle passing, annotated
 (FMS) movement ”Deep Squat (Floor)” from a single
 keyframe. Judge every item below, then give the overall score.
                                                                        with six modified-OSATS skill ratings. We divide each trial
 Trunk-calf angle – The angle between the trunk (the line from          into windows of up to 32 seconds, with each window in-
 the midpoint of the hips to the midpoint of the shoulders) and         heriting the trial-level ratings. The assessment criteria fol-
 the tibia (the line from the knee to the ankle). Parallel:             low the six dimensions and their scoring anchors at levels
 standard, 0-5 degrees Not parallel: non-standard, over 5               1, 3, and 5 from the source paper, with intermediate scores
 degrees ... Overall score: 3 = every item above is standard 2 =        used for performance between adjacent anchors. We also
 the squat is completed but at least one item is non-standard 1 =       provide task-specific procedure descriptions based on the
 the squat cannot be completed on the floor ...                         dataset documentation. An example for knot tying is shown
 User                                                                   below.
 <image>
                                                                         System
 Assistant
 {”Trunk-calf angle”: ”Parallel”, ”Hip height”: ”Higher”,                 You are a surgical skills examiner. Evaluate the robot-assisted
 ”Wrist position”: ”The Left”, ”Score”: 2}                               surgical training trial provided by the user. The video may be
                                                                         an excerpt of a longer trial; score the trial it comes from. Score
                                                                         the performance using the six named dimensions of the
A.21. UpperLimb                                                          modified OSATS global rating score. ... Respect for tissue:
UpperLimb [44] contains RGB recordings of four                           Lowest anchor (score value 1): Frequently used unnecessary
upper-limb rehabilitation exercises, annotated with com-                 force on tissue
                                                                         Middle anchor (score value 3): Careful tissue handling but
plete/incomplete execution labels. We use the videos and
                                                                         occasionally caused inadvertent damage
the completion labels to construct QA samples. Based on
                                                                         Highest anchor (score value 5): Consistent appropriate tissue
the exercise descriptions and completion definitions in the              handling ...
source paper, we formulate assessment criteria specifying
                                                                         User
the expected movement procedures and endpoints. The
                                                                         Assess the trial in the following video.
prompt provides the procedures for all four exercises, re-
                                                                         Task: Knot Tying
quiring the model to identify the demonstrated movement                  Expected procedure: Using the robotic instruments, the subject
and assess its completion. We use the official train/test split.         ties two sutures, one after the other, around a flexible tube fixed
An example of QA pair is shown below.                                    at both ends. Each completed knot should be taut and secure
                                                                         around the tube.
                                                                         <video>




                                                                    8
 QA example (continued)                                                   dimension scores to obtain the global rating score (GRS).
 Assistant                                                                We retain the released subject-level train/test split, exclud-
 {”Respect for tissue”: 2, ”Suture/needle handling”: 2, ”Time             ing the validation data. An example of suturing assessment
 and motion”: 2, ”Flow of operation”: 2, ”Overall                         is shown below.
 performance”: 2, ”Quality of final product”: 3}
                                                                           System
A.23. CaptainCook4D                                                         You are a surgical skills examiner. Evaluate the open suturing
                                                                           performance in the video. The subject performs single
CaptainCook4D [51] contains cooking recordings anno-                       interrupted sutures on an ethylene-vinyl acetate bench model
tated with step-level errors across eight categories. We se-               with a needle holder, forceps and scissors; judge only the
lect individual cooking steps according to their annotated                 performance visible in the video. Score the performance on the
temporal boundaries and provide the recipe and intended                    eight dimensions of the Objective Structured Assessment of
step as context. Each QA sample requires the model to                      Technical Skills (OSATS) global rating score. Apply each
identify execution errors and generate a brief description                 dimension to the suturing task and use a five-point Likert scale.
for each applicable category, returning an empty JSON ob-                  ... Respect for tissue:
                                                                           Anchor 1: Often used unnecessary force on tissue or caused
ject when no error is present. The assessment criteria are
                                                                           damage by inappropriate use of instruments
adapted from the dataset’s error taxonomy, with task de-
                                                                           Anchor 3: Careful handling of tissue but occasionally caused
pendencies used to distinguish valid alternative step orders               inadvertent damage
from ordering errors. When multiple errors belong to the                   Anchor 5: Consistently handled tissues appropriately with
same category, their descriptions are consolidated into a sin-             minimal damage ...
gle response. We retain the official subject-level train/test              User
split and exclude validation data. An example for the pin-                 <video>
wheels recipe is shown below.                                              Assess the suturing performance in the following video.
                                                                           Assistant
 System
                                                                           {”Respect for tissue”: 1, ”Time and motion”: 2, ”Instrument
  Assess the execution of the specified cooking step in the video.         handling”: 1, ”Suture technique”: 2, ”Flow of operation and
 The input video shows a segment of a single cooking step.                 forward planning”: 2, ”Knowledge of specific procedure”: 2,
 Assessment criteria: Use the intended step as the reference for           ”Quality of final product”: 1, ”Overall performance”: 2}
 ingredients, quantities, utensils, preparation, technique, timing
 and temperature. Compare the visible actions and outcomes
 with these requirements to identify deviations. Alternative step         A.25. CPR-Coach
 orders that satisfy the required dependencies are valid. ... Error       CPR-Coach [61] contains chest-compression training
 categories: ... Order Error: Execution of steps in a sequence            recordings from four synchronized camera views, annotated
 that violates the required dependencies. ... Return when there
                                                                          with execution errors. We reconstruct RGB videos at 25 fps
 are no errors.
                                                                          from the released frame sequences and use camera ch0 for
 User
                                                                          all recordings. We construct binary QA samples for each
 <video>                                                                  annotated error and sample an equal number of absent er-
 Recipe: Pinwheels
                                                                          ror categories, using one absent-error question for record-
 Intended step: scoop-Use a butter knife to scoop nut butter
 from the jar
                                                                          ings with correct execution. To provide balanced positive
 Assess this step and return the error descriptions by category.          and negative supervision for error detection, we construct
                                                                          binary QA samples for each annotated error and an equal
 Assistant
                                                                          number of randomly sampled absent error categories. For
 {”Order Error”: ”Step performed before placing tortilla on
 cutting board”}
                                                                          recordings with correct execution, we sample one absent-
                                                                          error category. We retain the official train/test split, includ-
                                                                          ing recordings with multiple simultaneous errors in the test
A.24. AIxSuture                                                           set. An example for hand placement is shown below.
AIxSuture [29] contains recordings of open suturing on
a bench model, assessed by three raters across eight OS-                   System
ATS skill dimensions. We divide each recording into win-                    Assess whether the specified error is present in the
dows of up to 32 seconds, with each window inheriting the                  chest-compression action. Return only this JSON object and
recording-level ratings. The assessment criteria follow the                nothing else: {”error present”: ”YES” or ”NO”}.
eight OSATS dimensions and their scoring anchors at lev-                   User
els 1, 3, and 5. For each dimension, we use the median of                  <video>
the three raters’ scores as the reference, and sum the eight               Error: Overlap Hands


                                                                      9
 QA example (continued)                                                  B. Dataset Statistics
 Description: The hands are laid flat across one another with the
 fingers extended and not interlocked during compression. Look           B.1. Task-Level Composition
 at the finger arrangement; having one hand above the other              Table 5 presents the task-level composition of X-AQA-40K
 alone does not identify this error.                                     and X-AQA-Bench. X-AQA-40K contains 40,163 train-
 Assistant                                                               ing samples drawn from 22 source datasets across four do-
 {”error present”: ”YES”}                                                mains: competitive sports, fitness exercises, rehabilitation,
                                                                         and general skills. The source counts indicate the avail-
A.26. LASANA                                                             able QA samples after preprocessing, while the X-AQA-
                                                                         40K column reports the samples selected for joint training.
LASANA [24] contains laparoscopic training recordings
                                                                         These datasets contribute 29 task-specific training subsets,
with four skill-dimension ratings and task-specific error an-
                                                                         each capped at 2,000 samples. For Ego-Exo4D and CoT-
notations. We use left-camera videos and construct two
                                                                         AFA, which each span two domains, we apply this cap sep-
QA tasks: numerical assessment of surgical skill and bi-
                                                                         arately to each task within each domain. X-AQA-Bench
nary detection of individual execution errors. The scoring
                                                                         comprises 7,101 evaluation samples, including 5,366 ID
task evaluates depth perception, efficiency, bimanual dex-
                                                                         and 1,735 OOD samples. For ID evaluation, we select up
terity, and tissue handling, using the median of the available
                                                                         to 300 samples per task and output format from the held-
raw ratings from at least two raters for each dimension. The
                                                                         out test partitions of datasets represented in X-AQA-40K.
error-detection task asks whether a specified task-specific
                                                                         For OOD evaluation, we use four datasets held out from
error occurs in the video. We adapt the scoring anchors and
                                                                         training (T3Set, Fitness-7, KIMORE, and JIGSAWS) and
error definitions from the source paper. We retain the offi-
                                                                         include all QA samples across their released partitions.
cial train/test split and exclude validation data. Examples of
skill scoring and error detection are shown below.                       B.2. Data Distributions
 System                                                                  Figure 5 presents the distributions of video durations, as-
  Assess the four skill dimensions over the complete                     sessment criteria, output formats, and reference answer
 laparoscopic training video. Assess each dimension                      lengths in X-AQA-40K and X-AQA-Bench. Video du-
 independently from 1.0 to 5.0 in increments of 0.5 using the            rations vary substantially across domains. Competitive
 task-specific anchors below. Use intermediate values for                sports and fitness exercises generally involve shorter clips,
 performance between adjacent anchors. Scoring criteria:                 whereas general skills include longer recordings with a
 Depth perception: accuracy of instrument targeting, grasping            wider duration range. Rehabilitation also exhibits consid-
 and placement. 1: Missed grasps; 3: Slow accuracy; 5: Fast              erable variation in clip lengths, reflecting different exercise
 precise transfers. ...                                                  types and recording settings. Explicit assessment criteria
 User                                                                    are included in 58.9% of X-AQA-40K samples and 61.4%
 <video>                                                                 of X-AQA-Bench samples, providing task-specific evalua-
 Task: Peg transfer                                                      tion standards across both datasets. Categorical judgments
 Assess the four skill dimensions.                                       account for the largest share of output components in X-
 Assistant                                                               AQA-40K (52.2%), followed by numerical scoring (26.8%)
 {”Depth perception”: 4.0, ”Efficiency”: 4.0, ”Bimanual                  and textual feedback (21.0%). Output components in X-
 dexterity”: 4.0, ”Tissue handling”: 4.0}                                AQA-Bench are more evenly distributed, with 32.5% nu-
                                                                         merical scoring, 39.0% categorical judgment, and 28.5%
                                                                         textual feedback. Reference answer lengths also vary con-
 System
                                                                         siderably, with short numerical or categorical responses ac-
  Determine whether the specified error occurs in the
                                                                         counting for many samples and longer textual feedback ex-
 laparoscopic training video. Return only this JSON object and
 nothing else: {”error present”: ”Yes” or ”No”}.                         tending the distribution beyond 100 tokens. These distribu-
                                                                         tions highlight the diversity of X-AQA in temporal scale,
 User
                                                                         assessment objectives, and output complexity.
 <video>
 Task: Balloon resection
 Error: balloon damaged                                                  C. Experimental Details
 Definition: The inner balloon is damaged and loses less than            C.1. Video Sampling
 half its water.
 Does this error occur?                                                  We adopt an adaptive video sampling strategy to pre-
 Assistant                                                               serve temporal coverage within a maximum budget of 128
 {”error present”: ”No”}                                                 frames. For each clip of duration T seconds, we set the sam-


                                                                    10
Table 5. Task-level dataset composition. Source counts indicate the numbers of QA samples in the training and test partitions after
preprocessing, with validation samples included in the test count for T3Set. X-AQA-Bench uses held-out test samples for ID evaluation
and all available samples from unseen datasets for OOD evaluation. S, C, and T denote score, category, and text evaluation, respectively.

                                                                                            Source         X-AQA-40K X-AQA-Bench
Dataset                    Activity                    Task                     Format
                                                                                          Train    Test      Train        ID     OOD
                                                           Competitive Sports
AQA-7                      Diving, vault, etc.         Score                      S        803      303       803        300       –
MTL-AQA                    Diving                      Score + commentary        S,T      1,059     353      1,059       339       –
Rhythmic Gymnastics        Rhythmic gymnastics         Execution + penalty        S        800      200       800        200       –
FineFS                     Figure skating              GOE grade                  S       7,469    2,096     2,000       300       –
MultiSenseBadminton        Badminton                   Skill                      C       1,663     225      1,663         6       –
Ego-Exo4D                  Basketball, soccer, etc.    Sports proficiency         C       1,980     550      1,980       272       –
T3Set                      Table tennis                Coaching feedback          T        419      281        –           –      700
CricketVision              Cricket batting             Technique scores           S       6,439    1,755     2,000        40       –
ExpertAF                   Sports skills               Coaching feedback          T       3,655    1,272     2,000        63       –
CoT-AFA                    Martial arts                Martial form               C        900      175       900        175       –
                                                       Martial feedback           T        699      175       699        175       –
                                                           Fitness Exercises
Fitness-AQA                Squats, overhead presses    Technical point            C        9,669   1,706     2,000       300       –
FLAG3D                     Fitness exercises           Technical point            C       37,476   9,417     2,000       300       –
EgoExo-Fitness             Fitness exercises           Technical point            C        5,432   2,302     2,000       272       –
                                                       Overall comment            T         636     272       636        272       –
QEVD                       Fitness coaching            Execution QA               T      254,267     –       2,000        –        –
                                                       Coaching feedback          T       4,408    1,993     2,000       300       –
CoT-AFA                    Fitness exercises           Fitness form               C        1,982    335      1,982       300       –
                                                       Fitness feedback           T         358     335       358        300       –
Fitness-7                  Resistance exercises        Good/bad form              C         278      70        –          –       348
                                                              Rehabilitation
KIMORE                     Low-back rehabilitation     EAAQ clinical score        S         –      348         –          –       348
KERAAL                     Low-back rehabilitation     Verdict classification     C        540     491        540         –        –
REHAB24-6                  Rehabilitation exercises    Correctness                C        727     345        727         23       –
ExeCheck                   Rehabilitation exercises    Correctness                C        600     100        600         20       –
LLM-FMS                    Movement screening          FMS score                  S       1,451    361       1,451       300       –
UpperLimb                  Upper-limb rehabilitation   Completion                 C        411      80        411         80       –
                                                              General Skills
JIGSAWS                    Robotic surgery             OSATS dimensions           S        281       58        –          –       339
CaptainCook4D              Cooking                     Error detection            C       2,820    1,397     2,000        96       –
AIxSuture                  Open suturing               OSATS global rating        S       2,201     460      2,000       46        –
CPR-Coach                  Chest compression           Error detection            C        648     4,118      648        300       –
Ego-Exo4D                  Cooking, music, dance       Skill proficiency          C       3,725    1,035     2,000       187       –
LASANA                     Laparoscopic training       Skill dimensions           S        906      195       906        195       –
                                                       Error detection            C       3,521     763      2,000       205       –
Total                                                                                                        40,163     5,366    1,735


pling frame rate to 16 fps for T ≤ 8, 8 fps for 8 < T ≤ 16,             clips while maintaining coverage of longer action sequences
and 4 fps for 16 < T ≤ 32. For clips longer than 32                     within a fixed frame budget.
seconds, we set the sampling rate to 128/T fps. The re-
sulting frame count is constrained to the range of 4 to 128             C.2. Evaluation Protocol
and adjusted to an even number to accommodate the two-                  Prediction Parsing. We extract predictions according to
frame temporal patching of Qwen3.5-9B’s vision encoder.                 the output schema of each task. Structured responses are
This strategy provides denser temporal sampling for short               parsed as JSON objects, allowing minor formatting vari-


                                                                   11
(a) Video duration                                                                       Table 6. Prediction parsing validity on X-AQA-Bench for the eval-
                                                                                         uated models in Tab. 1.
                                  X-AQA-40K            X-AQA-Bench

Competitive                                                                               Model                                                Valid (%)
    Sports
                                                                                                             Open-Source Models
    Fitness                                                                               Molmo2-8B                                                 96.5
  Exercises
                                                                                          VideoLLaMA3-7B                                            76.1
   Rehabil-
                                                                                          InternVL3.5-8B                                            99.7
     itation                                                                              Keye-VL-1.5-8B                                            85.2
                                                                                          MiniCPM-V 4.5                                             96.1
      General                                                                             InternVideo3-8B-Instruct                                  95.9
       Skills                                                                             Eagle2.5-8B                                               98.8
                1             3            10         30           100        300         LLaVA-OneVision-2                                         97.4
                                     Video duration (s, log scale)                        Qwen2.5-VL-7B-Instruct                                    95.6
                                                                                          Qwen3-VL-8B-Instruct                                     100.0
(b) Assessment criteria                                                                   Qwen3-VL-8B-Thinking                                      95.4
  X-AQA-40K                 w/ criteria (58.9%)          wo/ criteria (41.1%)             Qwen3.5-9B, Non-Thinking                                  99.4
                                                                                          Qwen3.5-9B, Thinking                                      92.6
X-AQA-Bench                  w/ criteria (61.4%)           wo/ criteria (38.6%)           X-AQA                                                    100.0
                    0%                           50%                        100%                                Proprietary Models
(c) Output formats                                                                        Claude Sonnet 5.5                                        100.0
                                                                                          Gemini 3.8 Flash                                         100.0
  X-AQA-40K              S (26.8%)             C (52.2%)             T (21.0%)            GPT-6.1 Sol                                              100.0
X-AQA-Bench               S (32.5%)            C (39.0%)          T (28.5%)

                    0%                           50%                        100%
                                                                                         ble 6 reports the percentage of predictions that pass these
(d) Answer length                                                                        checks on X-AQA-Bench. For 14 of the 17 models, at least
      Count (log scale)                                                                  95% of predictions pass, including 100.0% for X-AQA.
                                                                X-AQA-40K
10k                                                             X-AQA-Bench              VideoLLaMA3-7B has the lowest rate (76.1%).
 1k
100
 10                                                                                      X-AQA-Bench Metrics. We compute SRCC, macro-F1,
  1                                                                                      Cohen’s κ, and BERTScore-F1 as described in the main
      1              3            10           30              100          300
                              Length (tokens, log scale)
                                                                                         paper. For categorical and textual assessment, metrics are
                                                                                         first computed within each data source and then averaged
Figure 5. Data distributions of X-AQA-40K and X-AQA-Bench.                               across sources, weighted by the number of valid predic-
(a) Video duration distributions across four domains. Video dura-                        tions. Macro-F1 is averaged over classes present in the ref-
tions are reported for video samples only. (b) Percentages of sam-                       erence labels, and Cohen’s κ is unweighted. BERTScore-F1
ples with and without explicit assessment criteria in the prompt.                        is computed using RoBERTa-large without baseline rescal-
(c) Shares of output components corresponding to numerical scor-                         ing.
ing (S), categorical judgment (C), and textual feedback (T). MTL-
AQA samples with both a score and a comment are counted once
under S and once under T. (d) Counts of complete reference an-                           Dataset-Specific Metrics. For the specialist comparisons
swers in five-token bins. Each sample contributes one answer, to-                        in Tab. 2, we evaluate X-AQA on the full test sets using the
kenized with Qwen3.5-9B.                                                                 corresponding dataset-specific metrics. On MTL-AQA, the
                                                                                         predicted execution award is converted to the final score us-
                                                                                         ing the annotated difficulty coefficient, following ŝ = 3dê.
ations such as Markdown code fences, surrounding text,                                   We report SRCC and relative ℓ2 error (R-ℓ2 ), with the latter
and differences in field naming. Numerical predictions                                   defined as
are validated against task-specific score ranges and incre-
                                                                                                                    N                    2
ments, while categorical predictions must match the pre-                                                        1 X           ŝi − si
                                                                                                       R-ℓ2 =                                         (3)
defined labels. For multi-field outputs, all required fields                                                    N i=1       smax − smin
must be valid. Textual responses are evaluated directly,
with the comment field extracted for tasks that combine                                  where N is the number of valid predictions, and smax and
scoring and feedback. In X-AQA-Bench, only successfully                                  smin denote the maximum and minimum reference scores
parsed predictions are included in metric computation. Ta-                               in the full test set. The reported R-ℓ2 values are multiplied


                                                                                    12
by 100. On Fitness-AQA, we compute error-class F1 sepa-
rately for each technical point. On KIMORE, SRCC is com-
puted independently for each of the five rehabilitation exer-
cises. On LASANA, we report accuracy and balanced ac-
curacy, where the latter is defined as the mean recall across
classes. Both metrics are averaged equally across four rep-
resentative error-detection tasks.

D. More Qualitative Results
Figures 6 and 7 provide additional qualitative examples
complementing those in Fig. 3 in the main paper. Across
diverse datasets and assessment tasks, X-AQA produces
distinct assessments for different performances under the
same prompt. Figure 8 examines the complementary set-
ting, where the same video is evaluated using different as-
sessment criteria. X-AQA adjusts its judgments accord-
ing to the specified technical requirements, correctly distin-
guishing whether the same action satisfies different criteria.
These examples further demonstrate X-AQA’s ability to as-
sess action quality based on both observed execution and
task-specific assessment criteria.

E. Data Access and Licensing
X-AQA-40K and X-AQA-Bench are constructed from ex-
isting datasets governed by their respective licenses and ac-
cess agreements. We do not redistribute the original me-
dia or annotations. Instead, we provide detailed prepro-
cessing code and supporting materials, including assess-
ment criteria and dataset-specific processing configurations,
to enable reconstruction of the training and evaluation data.
Users must obtain the original datasets from their respec-
tive providers and comply with the applicable licensing and
access requirements.

F. Limitations
X-AQA establishes a unified framework for diverse AQA
tasks, while several challenges remain. First, X-AQA does
not explicitly ground its predictions in visual evidence.
Linking observed movements to assessment criteria and
predictions could enable more interpretable and verifiable
assessments. Second, our evaluation measures the agree-
ment between generated feedback and reference annota-
tions, rather than its effectiveness in improving action exe-
cution. Extending AQA toward interactive coaching, where
feedback guides and improves subsequent performance, is
a promising direction for future research.




                                                                 13
  (a) KIMORE (Squat)                                                             (b) MultiSenseBadminton (Backhand Drive)
   Evaluate the rehabilitation exercise in the video. The exercise is Squat.         Assess the player's overall backhand drive skill level and provide
   … Rate the performance on the ten items of the Exercise Accuracy                  coaching feedback. … Evaluate grip, posture, swing mechanics,
   Assessment Questionnaire (EAAQ), using the scale 1 = Never … 5 =                  coordination of the torso, arm and wrist, footwork, and contact
   Always.                                                                           point.




                                     Video A                                                                           Video A
       X-AQA:                                                                           X-AQA:
       {"primary_objective_achieved": 4, "repetitions_constant": 4,                     {"skill_level": "Intermediate", "feedback": "The swing does not go
       "movement_amplitude_complete": 4, "head_posture": 4,                             forward and instead goes downward, with the head and hips tilted
       "right_arm_posture": 4, "left_arm_posture": 4, "trunk_posture": 4,               back at impact and the upper body not leaning forward."}
       "pelvis_posture": 4, "right_leg_posture": 4, "left_leg_posture": 4}




                                     Video B                                                                           Video B
       X-AQA:                                                                           X-AQA:
       {"primary_objective_achieved": 3, "repetitions_constant": 3,                     {"skill_level": "Beginner", "feedback": "The contact point is too
       "movement_amplitude_complete": 3, "head_posture": 3,                             low, the backhand grip is poor, and the right foot is not used. The
       "right_arm_posture": 3, "left_arm_posture": 3, "trunk_posture": 3,               swing needs to be performed while looking sideways."}
       "pelvis_posture": 3, "right_leg_posture": 3, "left_leg_posture": 3}


  (c) CaptainCook4D (Blender Banana Pancakes)                                    (d) CoT-AFA (Kneeling Step Double Tiger Claw)
   Assess the execution of the specified cooking step in the video. …                Assess whether the kneeling step double tiger claw was performed in
   Intended step: Pour three little puddles straight from the blender                accordance with the action standard. … Bend one knee and lower the
   into the frying pan. … Return the error descriptions by category.                 body until that knee touches the ground. … Maintain stability and
                                                                                     balance.

                                                X-AQA:                                                                                   X-AQA:
                                                {"Technique Error": "Using a                                                             {"form_assessment":
                                                spoon to pour instead of                                                                 "standard"}
                   Video A
                                                pouring directly from the                               Video A
                                                blender", …}
                                                                                                                                         X-AQA:
                                                                                                                                         {"form_assessment":
                                                X-AQA: {}                                                                                "non-standard"}
                   Video B                                                                              Video B

  (e) Ego-Exo4D (Advanced Choreography)                                          (f) ExeCheck (Forward Lunge)
   You assess proficiency in short videos of skilled activities. Proficiency         Assess the form of this rehabilitation exercise: forward lunge. The
   levels: Novice, Early Expert, Intermediate Expert, Late Expert. …                 dataset’s incorrect-form criteria are: Forward trunk lean, knee beyond
   Activity: Performing the advanced choreography.                                   toes, or the trailing knee striking the floor.

                                                       X-AQA:                                                                            X-AQA:
                                                       {"proficiency_level":                                                             {"exercise_form":
                                                       "Late Expert"}                                                                    "correct"}
                      Video A                                                                           Video A
                                                       X-AQA:                                                                            X-AQA:
                                                       {"proficiency_level":                                                             {"exercise_form":
                                                       "Intermediate Expert"}                                                            "incorrect"}
                      Video B                                                                           Video B


Figure 6. Additional qualitative examples of X-AQA across different videos (Part 1). Each pair of videos is evaluated using the same
prompt, with X-AQA producing distinct assessments based on the observed action execution.




                                                                                14
  (a) Fitness-7 (Overhead Dumbbell Triceps Extension)                             (b) Fitness-7 (Bodyweight Squat)
   Assess the exercise form in the video. Exercise: Overhead dumbbell                 Assess the exercise form in the video. Exercise: Bodyweight squat.
   triceps extension. Determine whether the demonstrated exercise form                Determine whether the demonstrated exercise form is good or bad.
   is good or bad.

                                                          X-AQA:                                                                              X-AQA:
                                                          {"exercise_form":                                                                   {"exercise_form":
                                                          "good"}                                                                             "bad"}




                        Video A                                                                            Video A
                                                          X-AQA:                                                                              X-AQA:
                                                          {"exercise_form":                                                                   {"exercise_form":
                                                          "bad"}                                                                              "good"}




                        Video B                                                                            Video B

  (c) CPR-Coach (Chest Compression)                                               (d) AQA-7 (Snowboard Big Air)
   Assess whether the specified error is present in the chest-compression             Give one overall score from 0 to 50 for this attempt. … Assess take-off
   action. … Error: Squatting. The rescuer performs compressions from a               and amplitude, flight: difficulty, execution and style, and landing
   low squat with the feet supporting the body and the knees raised off the           and ride-away.
   floor.

                                                                    X-AQA:                                                              X-AQA:
                                                                    {"error_p                                                           {"overall_score": 38}
                                                                    resent":
                                                                    "YES"}
                             Video A                                                                    Video A

                                                                    X-AQA:                                                              X-AQA:
                                                                    {"error_p                                                           {"overall_score": 32}
                                                                    resent":
                                                                    "NO"}
                             Video B                                                                    Video B

  (e) Fitness-AQA (Overhead Press)                                                (f) LLM-FMS (Deep Squat (Plank))
   Evaluate whether an exercise execution satisfies a given technical point.          Assess the quality of the Functional Movement Screen movement Deep
   … Exercise: Overhead Press. Technical point: Keep the knees                        Squat (Plank) from a single keyframe. Judge trunk-calf angle, hip
   straight and fully extended throughout the lift, without bending                   height, and wrist position, then give the overall score.
   them.

                                                 X-AQA:                                                        X-AQA:
                                                 {"technical_point_satisfied":                                 {"Trunk-calf angle": "Parallel", "Hip height":
                                                 "yes"}                                                        "Lower", "Wrist position": "The Left", "Score":
                                                                                                               2}
                   Video A                                                                  Frame A
                                                 X-AQA:                                                        X-AQA:
                                                 {"technical_point_satisfied":                                 {"Trunk-calf angle": "Not parallel", "Hip height":
                                                 "no"}                                                         "Lower", "Wrist position": "The Left", "Score":
                                                                                                               1}
                   Video B                                                                  Frame B


Figure 7. Additional qualitative examples of X-AQA across different visual inputs (Part 2). Each pair of visual inputs is evaluated using
the same prompt, with X-AQA producing distinct assessments based on the observed action execution.


                                                                                 15
 (a) EgoExo-Fitness (Leg Lunge With Knee Lift)                                   (b) EgoExo-Fitness (Side Knee Raise with Ab Contraction)




              Prompt A                               Prompt B                                    Prompt A                              Prompt B
  Exercise: Leg Lunge With Knee          Exercise: Leg Lunge With Knee               Exercise: Side Knee Raise And         Exercise: Side Knee Raise And
  Lift                                   Lift                                        Abdominal Muscles Contract            Abdominal Muscles Contract
  Technical point: Place your            Technical point: Place your                 Technical point: Touch the            Technical point: Keep your left
  hands on your hips.                    hands behind your back.                     ground with your left tiptoes.        leg raised off the ground or
                                                                                                                           touch the ground only with
                                                                                                                           your left toes.
  X-AQA:                                 X-AQA:                                      X-AQA:                                X-AQA:
  {"technical_point_satisfied": "no"}    {"technical_point_satisfied": "yes"}        {"technical_point_satisfied": "no"}   {"technical_point_satisfied": "yes"}

 (c) Fitness-AQA (Back Squat)                                                    (d) Fitness-AQA (Overhead Press)




              Prompt A                               Prompt B                                    Prompt A                              Prompt B
  Exercise: Back Squat                   Exercise: Back Squat                        Exercise: Overhead Press              Exercise: Overhead Press
  Technical point: Keep the knees        Technical point: Let the knees              Technical point: Keep the knees       Technical point: Bend the
  tracking outward in line with          cave inward during the squat                straight and fully extended           knees slightly before the press,
  the toes throughout the squat,         instead of keeping them aligned             throughout the lift, without          then extend the legs to help
  without letting them cave              with the toes.                              bending them.                         drive the weight overhead.
  inward.
  X-AQA:                                 X-AQA:                                      X-AQA:                                X-AQA:
  {"technical_point_satisfied": "yes"}   {"technical_point_satisfied": "no"}         {"technical_point_satisfied": "no"}   {"technical_point_satisfied": "yes"}

 (e) REHAB24-6 (Table Push-Ups)                                                  (f) REHAB24-6 (Leg Abduction)




        Prompt A (condensed)                   Prompt B (condensed)                              Prompt A                              Prompt B
  For a correct table push-up, the       For a correct diamond table                 Performed with: left leg              Performed with: left leg
  hands are about shoulder-              push-up, the thumbs and index               A correct repetition meets every      A correct repetition meets every
  width apart. The body stays            fingers form a diamond on the               one of these criteria: The            one of these criteria: The
  straight as the elbows bend until      table. The body stays straight as           moving leg stays straight at the      moving leg stays straight at the
  the chest comes close to the           the elbows bend close to the                knee. The leg travels sideways        knee. The leg travels sideways
  table. Both arms bend and              torso and the chest lowers                  in the frontal plane, not forward     in the frontal plane, not forward
  extend at the same rate and            toward the hands. Both arms                 or backward. … The leg is             or backward. … The leg is
  straighten fully at the top.           bend and extend at the same rate            lowered back under control.           lowered back under control.
                                         and straighten fully at the top.                                                  The leg is raised to hip height,
                                         The upper back stays straight
                                         without rounding.                                                                 reaching a horizontal position at
                                                                                                                           the top of the movement.

  X-AQA:                                 X-AQA:                                      X-AQA:                                X-AQA:
  {"rehabilitation_form": "correct"}     {"rehabilitation_form": "incorrect"}        {"rehabilitation_form": "correct"}    {"rehabilitation_form": "incorrect"}


Figure 8. Additional qualitative examples of X-AQA under different assessment criteria. Each video is evaluated using two prompts with
different assessment criteria, and X-AQA produces distinct judgments based on the specified requirements.


                                                                                16
