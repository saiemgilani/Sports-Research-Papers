<!-- source: library/preprints/arXiv/2026/2026 - StreamCoach Proactive Sports Coaching via Continuous Visual Reasoning - Liang et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.32281 -->
<!-- authors: Xiaoye Liang, Yiming Huang, Jialu Wu, Yushe Cao, Ruxiang Duan, Yi Sun, Tie Liu, Lai Jiang, Mai Xu, Shikun Feng, Yiheng Zhu -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-25; equations, tables and figures are NOT preserved - consult the PDF for those -->

# StreamCoach: Proactive Sports Coaching via Continuous Visual Reasoning

                                             StreamCoach: Proactive Sports Coaching via Continuous Visual Reasoning

                                          Xiaoye Liang1,2 * Yiming Huang2,3∗ Jialu Wu4 Yushe Cao5 Ruxiang Duan6 Yi Sun2,7 Tie Liu1
                                                                 Lai Jiang1 Mai Xu1 Shikun Feng2,8† Yiheng Zhu2,8†
                                              1
                                                Beihang University 2 Zhongguancun Academy 3 Nankai University 4 Zhejiang University
                                                             5
                                                               Tsinghua University 6 South China University of Technology
                                                                  7
                                                                    Institute of Automation, Chinese Academy of Science
                                                                     8
                                                                       Zhongguancun Institute of Artificial Intelligence
arXiv:2611.32281v1 [cs.CV] 24 Nov 2026




                                                                                        {fengshikun, zhuyiheng}@zgci.ac.cn



                                                                     Abstract                             1. Introduction
                                                                                                          In fitness and sports training, timely action quality assess-
                                         In fitness and sports training, timely action quality assess-    ment (AQA) helps learners correct technical errors dur-
                                         ment (AQA) is essential for learners to identify and cor-        ing an action or before their next attempt. For example,
                                         rect technical errors during movement execution. However,        when a player pushes the ball too far ahead during a soccer
                                         most AQA methods assess completed performances, limiting         slalom drill, immediate feedback can help them soften their
                                         their ability to provide timely feedback. Streaming methods      touch before reaching the next pole. However, many exist-
                                         alleviate this latency, but limited reasoning hinders their      ing AQA methods require the full video for assessment,
                                         use of subtle movement cues and sport-specific knowledge.        delaying corrective feedback and allowing errors to per-
                                         Moreover, their fragmented feedback focuses on one body          sist [23, 24, 30, 34, 38, 44]. Therefore, real-time coaching
                                         part at a time, overlooking movement details of other body       calls for streaming AQA methods that assess technique as the
                                         parts and transitions between action phases. To address          action unfolds and provide targeted feedback once sufficient
                                         these limitations, we propose StreamCoach, a streaming           evidence accumulates.
                                         AQA framework under the OnCueCoaching paradigm that
                                                                                                              Recent work explores assessment and task guidance in
                                         couples continuous chain-of-thought (CoT) reasoning with
                                                                                                          streaming video [11, 16, 22]. For example, Panchal et
                                         proactive, evidence-gated coaching. Technique-Aware Rea-
                                                                                                          al. [22] introduced QEVD-Fit-Coach and Stream-VLM to
                                         soning tracks body-part movements and action-phase transi-
                                                                                                          learn when to intervene and what feedback to provide during
                                         tions against sport-specific criteria, while Holistic Coaching
                                                                                                          exercise. Beyond fitness coaching, Liu et al. [16] introduced
                                         integrates accumulated evidence to deliver timely, compre-
                                                                                                          GuideMe, a multi-domain benchmark with annotations for
                                         hensive feedback on strengths and technical errors. To sup-
                                                                                                          next-step instructions, error detection, and corrective guid-
                                         port training and benchmarking, we construct EE4D-Stream
                                                                                                          ance in streaming video. Despite these advances, three lim-
                                         from 1,213 sports video sequences in Ego-Exo4D through
                                                                                                          itations remain: (1) Limited reasoning: existing methods
                                         LLM-assisted reannotation and manual review of selected
                                                                                                          [11, 16, 22] struggle to integrate fine-grained movement cues
                                         claims, pairing dense CoT annotations with evidence-gated
                                                                                                          with sport-specific knowledge and action intent. (2) Frag-
                                         speech content. Building on this dataset, we train Stream-
                                                                                                          mented feedback: they [11, 16, 22] often identify only an
                                         Coach using Temporal–Semantic Alignment Reinforcement
                                                                                                          overall issue or isolated error, without explaining what to
                                         Learning to jointly optimize feedback timing and content.
                                                                                                          retain, what to correct, and how to improve. (3) Narrow
                                         We benchmark 11 offline and streaming baselines on EE4D-
                                                                                                          data coverage: existing long-form coaching datasets, e.g.,
                                         Stream, including three proprietary models. StreamCoach
                                                                                                          QEVD-Fit-Coach [22], remain small and scenario-specific,
                                         achieves state-of-the-art results across intervention timing,
                                                                                                          restricting diversity and generalizability.
                                         action assessment, and coaching quality, surpassing both
                                         GPT-6.1 Sol and Claude Opus 5.5.                                     To address these limitations, we introduce OnCueCoach-
                                                                                                          ing, a streaming AQA paradigm that reasons over fine-
                                                                                                          grained movement cues as an action unfolds. As illustrated
                                                                                                          in Fig. 1, OnCueCoaching performs Technique-Aware Rea-
                                            * Equal contribution                                          soning at each streaming step and determines whether to
                                            † Corresponding author                                        provide Holistic Coaching. Specifically, Technique-Aware
Figure 1. Illustration of the OnCueCoaching paradigm with a soccer sample. Technique-Aware Reasoning updates the assessment as visual
evidence accumulates, while Holistic Coaching delivers feedback only when that evidence warrants intervention.


Reasoning integrates new observations of body-part motion              Semantic Alignment Reinforcement Learning to jointly op-
and phase transitions with prior evidence to infer their im-           timize feedback timing and content over complete stream-
plications for execution quality and update the assessment.            ing trajectories.
Based on this assessment, Holistic Coaching triggers feed-
back only when the accumulated evidence warrants it. The
feedback highlights strengths and pairs each identified er-          2. Related Work
ror with a specific correction. Building on this paradigm,
we introduce StreamCoach, a streaming AQA framework                  2.1. Action Quality Assessment
with chain-of-thought (CoT) reasoning. We further intro-
duce Temporal–Semantic Alignment Reinforcement Learn-                AQA evaluates how well an action is performed according
ing, which uses GRPO [29] to jointly optimize feedback               to task-specific criteria, such as body positioning, movement
timing and content over full streaming trajectories. To sup-         precision, and timing across action phases. Prior studies
port training and benchmarking, we construct EE4D-Stream             primarily formulate AQA as score prediction [23, 24, 30,
from 1,213 Ego-Exo4D video sequences spanning basket-                38, 44], exploring uncertainty-aware score distribution learn-
ball, soccer, and bouldering. Through LLM-assisted reanno-           ing [30] and exemplar-based contrastive regression [38]. To
tation and manual review of selected claims, we pair dense           capture subtle execution differences, FineDiving [34] intro-
CoT annotations with evidence-gated speech content. We               duces procedure-aware assessment, while FineParser [35]
benchmark StreamCoach against 11 offline and streaming               jointly models spatial and temporal action structure. These
baselines, including three proprietary models. StreamCoach           approaches improve sensitivity to local execution details,
achieves state-of-the-art results across eight metrics span-         although their primary output remains a score. Recent
ning intervention timing, action assessment, and coaching            work extends AQA toward descriptive and actionable feed-
quality, outperforming both GPT-6.1 Sol [20] and Claude              back [2, 3, 15, 41]. TechCoach [15] reasons about technical
Opus 5.5 [1]. Our contributions are threefold:                       points to generate coaching commentary, while ExpertAF [3]
                                                                     provides personalized corrections and visual demonstrations.
• We introduce OnCueCoaching, a streaming AQA                        Beyond post-hoc feedback, recent studies further explore
  paradigm that couples Technique-Aware Reasoning with               online coaching, aiming to provide timely guidance during
  Holistic Coaching to deliver timely, structured feedback.          execution [11, 16, 22]. For example, QEVD-Fit-Coach and
• We construct EE4D-Stream for training and benchmark-               its Stream-VLM baseline [22] study feedback timing and
  ing streaming AQA. Through LLM-assisted reannotation               content during live fitness routines. These online coach-
  of 1,213 Ego-Exo4D video sequences across three sports             ing methods often identify isolated issues without explicitly
  and manual review of selected claims, we pair dense CoT            describing supporting movement details. Instead, our CoT
  annotations with evidence-gated speech content.                    reasoning connects movement evidence across body parts
• We develop StreamCoach, a CoT-based framework im-                  and action phases and applies sport-specific criteria for co-
  plementing OnCueCoaching, and introduce Temporal–                  herent, evidence-gated feedback.
Table 1. Comparison with sports AQA and coaching datasets. △:    cesses interact. Technique-Aware Reasoning updates the
timestamps only. Inst. and Hours denote the number and total     assessment at each step, and Holistic Coaching provides
duration of unique video sequences.                              feedback only when the accumulated evidence warrants a
                                                                 response.
Dataset                  Inst. Hours FGF Rat. EGS DCoT
Offline text                                                     Technique-Aware Reasoning. Each update integrates ob-
FSBench [7]              783     76.0   ×    ×    ×      ×       servations of body-part movements and action-phase transi-
EgoExo-Fitness [14]      913      4.6   ✓    ×    ×      ×       tions with historical context and sport-specific knowledge. It
ExpertAF [3]          11,763     13.1   ✓    ✓    ×      ×       considers three aspects: (1) Observation: identifying the on-
EE4D-DescCoach [15] 4,843        10.8   ✓    ✓    ×      ×       going action and its execution details; (2) Effect: assessing
CoT-AFA [25]           3,392      3.0   ✓    ✓    ×      ×       execution quality and inferring potential effects on perfor-
Ego-Exo4D (Sports) [9] 1,214     17.3   ✓    ✓    △      ×       mance; and (3) Feedback: deriving candidate corrections for
Streaming annotations                                            identified issues when supported by evidence.
QEVD-Fit-Coach [22]       223    13.5   ✓    ×    △      ×
T3Set [18]                380     6.1   ✓    ×    ✓      ×       Holistic Coaching. Following each update, assessments
EE4D-Stream (Ours)      1,213    15.0   ✓    ✓    ✓      ✓       across body parts and action phases are consolidated into
                                                                 feedback only when sufficient evidence supports a new, use-
                                                                 ful assessment or correction. Otherwise, observation con-
2.2. Streaming Video Understanding                               tinues without a response. Depending on the evidence, a
Unlike offline video understanding, where models analyze         response may include (1) Positive Assessment: highlighting
video clips before generating [12, 19, 39], streaming video      correctly executed details; (2) Issue Identification: pinpoint-
understanding requires models to process incoming video          ing technical errors; and (3) Corrective Guidance: providing
clips and respond without accessing future frames [5, 33, 40].   actionable adjustments.
VideoLLM-online [5] introduces streaming dialogue su-            3.1.2. Formal Definition
pervision and temporally aligned generation, while later
                                                                 Let V = (v1 , v2 , . . .) denote the incoming video stream,
methods support efficient continuous processing and multi-
                                                                 where vt is the chunk observed at step t, and let Ht−1 de-
turn interaction [33, 40]. Beyond content understanding,
                                                                 note the available context from preceding observations and
proactive methods address when to respond during play-
                                                                 outputs. Given (Ht−1 , vt ), StreamCoach generates a reason-
back [26, 31, 32, 37]. MMDuet [31] interleaves video and
                                                                 ing sequence rt . Conditioned on (Ht−1 , vt , rt ), it then emits
text, while Dispider [26] separates perception, decision-
                                                                 a decision token at ∈ {⟨silent⟩, ⟨speak⟩}. If at = ⟨speak⟩,
making, and response generation to maintain continuous
                                                                 it generates coaching content ct . Otherwise, ct = ϵ, where ϵ
observation. MMDuet2 [32] further improves response tim-
                                                                 denotes the empty sequence. The complete output is
ing and quality through multi-turn reinforcement learning.
These methods focus on general video comprehension and                    zt = ⟨think⟩ ⊕ rt ⊕ ⟨/think⟩ ⊕ at ⊕ ct ,                 (1)
timely interaction. We instead assess fine-grained action ex-
ecution in its broader temporal context and provide targeted     where ⊕ denotes sequence concatenation. Treating the sur-
coaching feedback once sufficient evidence accumulates.          rounding thinking tags as fixed formatting, the conditional
                                                                 distribution factorizes as
3. Methodology                                                          πθ (zt | Ht−1 , vt ) = πθ (rt | Ht−1 , vt )
In this section, we present StreamCoach, a streaming AQA                                       · πθ (at | Ht−1 , vt , rt )         (2)
framework that continuously reasons over fine-grained body-                                    · πθ (ct | Ht−1 , vt , rt , at ),
part movements and transitions between action phases to
                                                                 where πθ is the policy parameterized by θ. At silent steps,
deliver timely, evidence-gated coaching feedback. We first
                                                                 the final factor assigns probability one to the empty sequence.
define the OnCueCoaching paradigm and describe the con-
                                                                 This factorization captures how the current assessment in-
struction of EE4D-Stream, then present the model architec-
                                                                 forms both the decision to intervene and the content of the re-
ture and two-stage training procedure.
                                                                 sulting feedback. This formulation jointly models reasoning,
3.1. OnCueCoaching Paradigm                                      intervention timing, and coaching content while conditioning
                                                                 only on past and current observations.
3.1.1. Paradigm Design
Inspired by how coaches assess athletic performance, we de-
                                                                 3.2. EE4D-Stream Dataset
fine OnCueCoaching as a continuous Observe–Think–Coach           OnCueCoaching requires continuous reasoning over unfold-
loop for streaming AQA. Fig. 1 illustrates how the two pro-      ing actions and selective speech grounded in accumulated
                                                            (a) Dataset construction pipeline                                                                                    (b) Dataset composition
    Step 1: Claim extraction                                                    Atomic claims                                 Step 2: Temporal grounding
          Expert commentary                                                    observation On the shot, the
                                                                               player keeps the shooting hand
     45.94 s “But the more I look                  Extract         Filter      on the side of the ball rather than
    at her shooting hand, maybe                                                behind it.                                Qwen
    bring it a little bit more behind               Qwen                                                                  main view              42.43–42.80 s
                                                                               effect It may cause the left hand
    the ball instead of on the side.                                           to slide a little bit.
    Maybe that's why that left hand                          drops
    slides a little bit. But overall,                                          feedback Bring the shooting
                                                           conflicts
    not bad at all. I like how she                                             hand a little more behind the ball        Qwen
    has that shooting elbow 90                     DeepSeek                    instead of keeping it on the side.         auxiliary view           41.43–42.80 s            Basketball                     Soccer                       Bouldering
    degree, guide hand is here. …”                                             assessment negative                          Re-checked: main view
                                                                                                                                                                                               g
                                                                                                                                                                                           rin
                                                                                                                                                       42.43–42.80 s
                                                                                                                                                                                      u lde                   Speak
                                                                                                                                                                                                              4394
    Step 3: Streaming annotation generation                                            1-s windows of the whole video                                                            Bo




                                                                                                                                                                                                                                          So
                                                                                                                                                                                                                                   C 39

                                                                                                                                                                                                                                            cc
                                                                                                                                                                                                                                    oT 5
                                                                                                                                                                                      14 oT




                                                                                                                                                                                                                                  1
                                                                                                                                                                                                            Neutral
                                                                                                                                                                                           3




                                                                                                                                                                                                                                   00

                                                                                                                                                                                                                                     1
                                                                                                                                                                                                       12105




                                                                                                                                                                                                                                              er
                                                                                                                                                                                        78
                                                                                                                                                                                  C




                                                                                                                                                                                                                               e 34
                                                                                                                                                                                           Ne




                                                                                                                                                                                                                                 8
                                                                                                                                                                                                                              14
      Window input                     Qwen draft per window                           GPT polish speak                 Qwen refine think whole video, reads Speak                           ga




                                                                                                                                                                                                                          itiv

                                                                                                                                                                                                                           e4
                                                                                                                                                                                                tiv
                                                                                                                                                                                                   e4




                                                                                                                                                                                                                        tiv
                                                                                                                                                                                                                      Pos
                                                                                                                                                                                          Posit                                   tral
                                                                                                                                                                                                     51




                                                                                                                                                                                                                      ga
                                                                                                                                                                                                       6
                                                                                                                                                                                          5974ive                              Neu 80




                                                                                                                                                                                                                        Ne
   41–42 s no claim          VLM caption                      draft Think                                                                                                                                                                   Speak
                                                                                              Silent                    The player is facing the hoop, holding the                                         69,309  88                       2689
                             The player stands facing the hoop, holding                                                                                                                              annotations Po
                             the ball at waist level, and raises it to chest                                         ball at waist level, and raising it to chest height.                                            sitiv




                                                                                                                                                                                 Spea
                                                                                                                                                                                                   l             1  024 e




                                                                                                                                                                               8312
                                                                                                                                                                                                ra                1
                             height.                                                      draft Think                The set is in progress. I should keep watching.                         ut
                                                                                                                                                                                           Ne 9648




                                                                                                                                                                                  k




                                                                                                                                                                                                                  Nega 90
                                                                                                                                                                                            1




                                                                                                                                                                                                                131
   42–43 s 4 claims




                                                                                                                                                                                                                      tive
                             Merge                drafts Think & Speak                    draft Think
                                                                                                                        The shooting elbow is at about 90 degrees
  negative shooting hand
                                The player keeps the shooting hand on              negative assessment                                                                                                                  CoT 6
  on the side of the ball,
                             the side of the ball rather than behind it,           positive assessment               and the guide hand is in place, … those are                                                         2773
  not behind it
                             which may cause the left hand to slide.                                                 good. However, the shooting hand is kept on the                              Basketball
   positive elbow at about                                                           The elbow, guide hand,
  90 degrees, guide hand     The shooting elbow is at about 90 degrees                                               side of the ball rather than behind it, which may
                                                                                  and release are good, but the
  in place                   and the guide hand is in place. …                                                       cause the left hand to slide, …
   negative base not big
                                                                                  shooting hand is on the side
                                                                                  and the base is too small.
                                                                                                                                                                                53,914                                            15,395
  enough to get off the         Good elbow, guide hand, and release.                                                 I should acknowledge the elbow, guide hand,                Chain-of-Thought                                    Speech Content
  ground
                                                                                  The player should move the
                             Shooting hand on the side. Base too small.                                              and release, but point out the hand position and
                                                                                  shooting hand behind the
   positive release off      The player should move the shooting hand                                                base. …
  two or three fingers,
                                                                                  ball and use a bigger base.                                                                  15.0                    145                              per-second
  giving backspin            behind the ball and use a bigger base.                                   feedback                                                                 hours                   athletes                         annotations
                                                                                    Speech content                      Chain-of-thought



Figure 2. Overview of the EE4D-Stream dataset. (a) Dataset construction pipeline, which extracts atomic claims, temporally grounds them,
and generates per-second CoT and evidence-gated speech content. (b) Dataset composition by sport and annotation type.


evidence. This demands four forms of supervision: (i) fine-                                                                  ments. We therefore convert the commentary into atomic
grained feedback (FGF) identifying strengths, errors, and                                                                    claims through the LLM-assisted pipeline shown in Fig. 2(a),
corrections, (ii) assessment rationale (Rat.) linking exe-                                                                   where each claim assesses one action phase with a single pos-
cution details to performance, (iii) evidence-gated speech                                                                   itive, negative, or neutral label and organizes its content into
(EGS) grounding utterances in observations, and (iv) dense                                                                   observation, effect, and feedback, so that feedback can target
chain-of-thought (DCoT) tracking evidence accumulation                                                                       specific execution details. Specifically, we extract atomic
per second. As shown in Tab. 1, existing sports AQA and                                                                      claims using Qwen3.8-27B [27], cross-validate them with
coaching datasets with natural-language annotations only                                                                     DeepSeek-V4-Flash [6] to remove conflicts. Effect and feed-
partially meet these requirements. To bridge this gap, we                                                                    back are recorded only when the commentary supports them.
introduce EE4D-Stream, which supports all four dimensions.                                                                   Qwen3.8-27B then localizes each claim independently in
    We construct EE4D-Stream from Ego-Exo4D [9], lever-                                                                      two camera views and reconciles inconsistent intervals using
aging synchronized ego-exo videos and time-stamped expert                                                                    evidence from both. After grounding, duplicate claims are
commentary across basketball, soccer, and bouldering. We                                                                     merged and conflicting assessments of the same execution
extract and temporally ground atomic claims from expert                                                                      detail are discarded.
commentary, then synthesize per-second CoT from these
claims to track accumulating evidence. Speech is provided                                                                    3.2.2. Streaming Annotation Generation
only when the CoT supports a positive or negative assess-                                                                   We partition each video sequence into non-overlapping one-
ment. After removing one sequence without claims and trim-                                                                  second windows and assign each claim to the window con-
ming leading and trailing windows with no athlete present,                                                                  taining its interval end. The claims in each window are
the dataset comprises 1,213 sequences spanning about 15                                                                     merged into a draft Think, and the positive and negative
hours. The dataset distribution across basketball, soccer, and                                                              ones also into a draft Speak; windows without claims use a
bouldering is shown in Fig. 2(b).                                                                                           neutral description of the athlete’s movement, generated by
                                                                                                                            Qwen3.8-27B from the window frames, as the draft Think.
3.2.1. Claim Extraction and Grounding                                                                                       GPT-6.1-Terra [21] then polishes the Speak drafts into the
Expert commentary has two characteristics: (1) individual                                                                   final speech content, and Qwen3.8-27B refines the Think
comments are colloquial and may mix assessments of dif-                                                                     drafts using the full sequence’s speech content as context.
ferent action phases with advice; (2) comments on the same                                                                  To preserve streaming causality, the prompt explicitly re-
execution detail may contain repeated or conflicting judg-                                                                  stricts each reasoning step to information available up to
                                                                   since the start of the stream. This allows the decoder to refer
                                                                   to movement details recorded in earlier reasoning even after
                                                                   the corresponding visual tokens leave the window. Using the
                                                                   visual tokens in the current window and the full text history,
                                                                   the decoder generates the reasoning sequence rt followed
                                                                   by the decision token at . If at = ⟨speak⟩, the decoder
                                                                   continues to generate coaching feedback ct . If at = ⟨silent⟩,
                                                                   decoding ends for the current step. In both cases, the decoder
                                                                   appends the keys and values of all newly generated text
                                                                   tokens to the text cache for subsequent steps.

                                                                   Stage 1: Reasoning-Augmented Coaching Cold Start.
                                                                   We initialize StreamCoach through supervised fine-tuning
                                                                   (SFT) on annotated streaming outputs. Each step con-
                                                                   tains a reasoning sequence and a binary speaking deci-
Figure 3. Overview of the reward design in Temporal–Semantic
                                                                   sion, while coaching feedback appears only when the tar-
Alignment RL, which consists of three parts: (a) feedback timing   get decision is ⟨speak⟩. To control the relative contribu-
reward, (b) feedback semantics reward, and (c) auxiliary reward.   tion of these targets despite their different token counts, we
                                                                   compute a separate mean token loss for each group. Let
                                                                   G = {think, dec, speak} and let Tt,g denote the set of tar-
the current window, allowing the CoT to draw on preceding          get token positions assigned to group g at streaming step
actions and convey coaching intent without incorporating           t. The thinking group contains the reasoning sequence and
future information. All prompts used are provided in Suppl.        its delimiters. The decision group contains the single token
Mat. 8.                                                            at ∈ {⟨silent⟩, ⟨speak⟩}. The speak group contains only
                                                                   the feedback tokens following ⟨speak⟩. Given the streaming
Manual Annotation Quality Validation. Two experi-                  input xt = (Ht−1 , vt ), we compute the teacher-forced loss
enced athletes per sport manually validate a randomly sam-         for each nonempty group as
pled 10% of takes, auditing each pipeline stage for omissions,
                                                                                       1 X
unsupported additions, semantic or polarity shifts, temporal              Lt,g = −           log πθ (yt,i | xt , yt,<i ) ,    (3)
misalignment, and future-information leakage in CoT. The                             |Tt,g |
                                                                                           i∈Tt,g
audit yields 94.8% polarity agreement, 88.3% grounding ac-
curacy within 0.5 seconds, a 6.2% unsupported-content rate,        where yt,i is the target token at position i and yt,<i denotes
and no observed future-information leakage, with further           the preceding target tokens at the same step. On silent steps,
details in the Suppl. Mat. 6.5.                                    Tt,speak is empty and we set Lt,speak = 0. We combine the
                                                                   group losses using a weighted mean,
3.3. StreamCoach                                                                                P
                                                                                                   g∈G λg Lt,g
Building on the OnCueCoaching paradigm and the EE4D-                                 LSFT,t = P                 ,             (4)
                                                                                                      g∈G λg
Stream dataset, we introduce StreamCoach, a streaming
AQA framework that integrates Technique-Aware Reasoning            and average over supervised streaming steps. Each weight
with Holistic Coaching. As the video unfolds, StreamCoach          λg scales the mean loss for its group, so a longer reasoning
accumulates fine-grained technical evidence and determines         sequence does not receive more weight solely because it
when to speak, aiming to generate actionable feedback only         contains more tokens.
when sufficient evidence is available.
                                                                   Stage 2: Temporal–Semantic Alignment Reinforcement
Model Structure StreamCoach uses a pretrained video-               Learning. After SFT, we optimize intervention timing and
language model comprising a visual encoder, a multimodal           semantic alignment with reference feedback. For each train-
projector, and a causal language decoder. At step t, the visual    ing video, we sample G causal streaming trajectories. At
encoder processes only the incoming video chunk vt , and the       each step, the policy observes only the video prefix available
projector maps its features into the decoder’s input space. To     at that step. Once a trajectory is complete, we evaluate its
reuse Ht−1 , each self-attention layer maintains separate key-     coaching events and assign a trajectory-level reward compris-
value (KV) caches for visual tokens within a sliding temporal      ing timing, semantic, and auxiliary components, as shown in
window and for all previously generated text tokens. The text      Fig. 3. For clarity, we omit the rollout index when defining
cache retains the keys and values of all text tokens generated     the reward components.
Feedback Timing.           Let E ∗ = {(t∗i , c∗i )}N
                                                   i=1 and Ê =   The format reward measures adherence to the Think and
{(t̂j , ĉj )}N̂
              j=1 denote the reference  and generated  coaching   Silent/Speak protocol, while the efficiency reward discour-
events, respectively. Each event consists of the streaming        ages unnecessarily long reasoning and excessive interven-
step at which a Speak response occurs and its feedback text.      tions. For rollout k, we compute the group-relative advan-
A reference event i and a generated event j are eligible for      tage as
matching if |t∗i − t̂j | ≤ ∆, where ∆ is the tolerance in                                    R(k) − µR
                                                                                      A(k) =              ,               (8)
streaming steps. For each eligible pair, we define its tempo-                                  σR + ϵ
ral proximity as τij = 1 − |t∗i − t̂j |/(∆ + 1). Let M denote
the one-to-one matching of eligible pairs. For a video with       where µR and σR are the mean and standard deviation of
N > 0 reference events, the timing and event rewards are          the G rewards for the same video. We update the policy
                                                                  using GRPO with KL regularization against the reference
                                                                  policy. Each rollout thus receives a single advantage re-
                  P
                 2 (i,j)∈M τij                     2|M|
    Rtime =                     ,      Revent =          . (5)    flecting both its intervention timing and the content of its
                    N + N̂                        N + N̂          coaching responses.
Both rewards penalize missed reference events and un-
matched responses. The event reward gives full credit to          4. Experiments
every match within the tolerance window, while the timing
reward gives more credit to responses closer to the reference     In this section, we evaluate StreamCoach on EE4D-Stream
step. Both are zero if the policy remains silent throughout       against representative offline and streaming video-language
the video.                                                        models under a common streaming AQA protocol. We also
                                                                  ablate CoT supervision and RL rewards in StreamCoach.

Feedback Semantics.        Using the same matching M, a
frozen LLM judge compares each matched response with              Implementation Details. For EE4D-Stream, we follow
its reference on three dimensions. The technical point score      the original Ego-Exo4D take-level assignments, retaining
measures whether the response addresses the same execution        945 training takes and merging the validation and test splits
details. The polarity score measures whether it agrees with       into a 268-take test set. We initialize StreamCoach from
the reference on which details are strengths or errors. When      Qwen3.5-4B [28] and adapt it with LoRA [10]. During SFT,
the reference includes an actionable correction, the correc-      we train for five epochs with a global batch size of 4 and a
tion score measures whether the response recommends an            learning rate of 2 × 10−4 , followed by one RL epoch with
adjustment in the same direction for the same issue. The          a per-device batch size of 1, a GRPO group size of 4, and
judge receives only the reference and generated feedback          a learning rate of 10−5 . Both stages use AdamW with a
texts. Each applicable dimension is scored from 0 to 5,           cosine learning-rate schedule and a 3% warmup ratio. We
and an unmatched reference event receives zero on every           sample videos at 2 FPS to form one-second chunks of two
applicable dimension.                                             frames each. For the temporal reward, we allow a matching
    Let Id denote the reference events to which dimension         tolerance of two steps (±2 seconds). All experiments run
d applies. The point and polarity dimensions apply to all         on a single node with four A100 GPUs. More experimental
reference events, while the correction dimension applies          details are provided in the Suppl. Mat. 7.
only to references containing an actionable adjustment. Let
D = {d : |Id | > 0} be the active dimensions for the video.       Evaluation Metrics We evaluate streaming AQA along
With equal weight for each active dimension, the semantic         three dimensions: intervention timing, action assessment,
reward is                                                         and coaching quality. For intervention timing, we report
                         1 X 1 X d                                Speak F1 on a one-second grid and T-F-Score@2 using
              Rsem =               si ,                    (6)    one-to-one event matching within ±2 seconds. For action as-
                        |D| 5|Id |
                            d∈D        i∈Id                       sessment, Pos-Recall and Neg-Recall measure the fractions
                                                                  of positive and negative reference events, respectively, cor-
where sdi is the score for reference event i on dimension d.      rectly identified by matched predictions. Unmatched events
                                                                  count as false negatives, and Macro-Recall is the unweighted
Joint Reward and Policy Optimization. We combine                  mean of the two recalls. For coaching quality, we report ME-
timing, event matching, and semantic agreement with auxil-        TEOR [4], BERTScore [42], and LLM-Score, each averaged
iary rewards for output format and efficiency:                    over all reference events with unmatched events scored as
                                                                  zero. For LLM-Score, Qwen3-32B [36] rates each matched
            R = λt Rtime + λe Revent + λs Rsem                    response from 0 to 5 on technical-point agreement, assess-
                                                           (7)
                 + λf Rformat + λr Refficiency .                  ment polarity, and correction direction.
Table 2. Streaming AQA results on EE4D-Stream. Bold and underlined values denote the best and second-best scores in each column,
respectively, among models that predict their own intervention times.

                               Intervention Timing                Action Assessment                 Coaching Content Quality
  Model / setting               F1         T-F-Score@2 Pos-Recall Neg-Recall Macro-Recall METEOR BERTScore LLM-Score

  Streaming with oracle timing
  Qwen3.5-4B (w/ GT)       N/A                N/A        0.5081       0.9747      0.7414        0.2012        0.7326        1.6924
  Qwen3.5-4B (w/o GT) N/A                     N/A        0.3739       0.9089      0.6414        0.1774        0.7166        1.2263
   Offline baselines
  Qwen3.5-4B                   0.4351        0.4403      0.4572       0.1577      0.3074        0.0821        0.5880        0.7604
  Claude-Opus-5.5              0.3511        0.6124      0.1905       0.3546      0.2725        0.0624        0.3332        0.6761
  Gemini-4-argon               0.4182        0.6237      0.0202       0.4563      0.2382        0.0549        0.3510        0.3848
  GPT-6.1-sol                  0.3856        0.6350      0.1784       0.2492      0.2138        0.0532        0.3717        0.6625
   Zero-shot streaming baselines
  VideoLLM-online-7B 0.0006                  0.0012      0.0000       0.0000      0.0000        0.0000        0.0004        0.0000
  MMDuet-7B              0.4556              0.3351      0.0802       0.4987      0.2895        0.0725        0.5445        0.3469
  Dispider-7B            0.0151              0.0285      0.0005       0.0110      0.0057        0.0008        0.0089        0.0027
  MMDuet2-3B             0.0758              0.1401      0.0360       0.0013      0.0187        0.0105        0.0540        0.0698
  Em-Garde-7B            0.1469              0.2420      0.0919       0.0282      0.0601        0.0229        0.1019        0.1210
  ThinkStream-3B         0.4472              0.4860      0.4937       0.0687      0.2812        0.0558        0.6227        0.5744
  VideoChat3-4B          0.0386              0.0490      0.0275       0.0000      0.0137        0.0020        0.0186        0.0248
   Fine-tuned streaming baselines
  VideoLLM-online-7B 0.4267                  0.4722      0.1311       0.2837      0.2074        0.0519        0.2432        0.4079
  MMDuet2-3B             0.3159              0.3868      0.2153       0.1847      0.2000        0.0461        0.1794        0.3978
  VideoChat3-4B          0.3284              0.3759      0.2113       0.1353      0.1733        0.0478        0.1760        0.3913
  StreamCoach-4B               0.5393        0.6354      0.6135       0.6530      0.6333        0.1906        0.6825        1.4939


Table 3. Ablation of CoT supervision and RL rewards in Stream-            GT). We evaluate these variants only on action assessment
Coach. Bold and underlined values mark the best and second-best           and coaching quality. Offline models, including GPT-6.1-sol,
results per metric, respectively, based on unrounded scores.              Claude-opus-5.5, Gemini-4-argon [8], and Qwen3.5, predict
                                                                          feedback timestamps and content after viewing the full video,
                              SFT               RL with CoT               while streaming models, including Dispider, Em-Garde [43],
  Metric          w/o CoT w/ CoT Timing Semantic Both                     MMDuet2, MMDuet, VideoChat3 [13], VideoLLM-online,
                                                                          and ThinkStream [17], decide when to intervene and what
  Speak F1             0.41         0.49     0.49     0.54    0.54
                                                                          to say as the video unfolds. For fair comparison, we also
  T-F-Score@2          0.56         0.66     0.69     0.62    0.64
                                                                          fine-tune MMDuet2, VideoChat3, and VideoLLM-online on
  Pos-Recall           0.32         0.28     0.35     0.58    0.61        the EE4D-Stream training set.
  Neg-Recall           0.30         0.43     0.46     0.65    0.65
  Macro-Recall         0.31         0.35     0.40     0.62    0.63
                                                                          Quantitative Results. As shown in Table 2, the baselines
  METEOR               0.09         0.11     0.13     0.19    0.19
                                                                          struggle to identify both strengths and technical errors at
  BERTScore            0.31         0.42     0.45     0.69    0.68
                                                                          the moments when experts provide feedback. MMDuet-7B,
  LLM-Score            0.66         0.82     0.92     1.39    1.49
                                                                          for example, achieves the highest Speak F1 among the base-
                                                                          lines, yet its Pos-Recall of 0.0802 is substantially lower than
                                                                          its Neg-Recall of 0.4987. Its T-F-Score@2 of 0.3351 and
4.1. Main Results                                                         LLM-Score of 0.3469 also indicate limited agreement with
Comparison Settings. We benchmark 11 baselines in                         the timing and content of expert feedback. StreamCoach
three settings on EE4D-Stream. With ground-truth speak-                   ranks first on all eight metrics among models that predict
ing times provided, Qwen3.5 generates feedback from the                   their own intervention times. Compared with MMDuet-7B,
available video prefix using either prior reference outputs,              StreamCoach improves Speak F1 by 18.4% and LLM-Score
Qwen3.5 (w/ GT) or its own prior outputs, Qwen3.5 (w/o                    by 330.6%. Against Claude Opus 5.5, the strongest propri-
Figure 4. Soccer shot case study. In the same 3–4 s window as the reference, StreamCoach identifies both the backward lean and the plant
foot positioned too far behind the ball, and provides a correction for each.


etary baseline on LLM-Score, the corresponding gains are              describes the kicking foot as unlocked, contradicting the
53.6% and 121.0%. These gains extend to action assessment,            reference assessment. It shows that StreamCoach identi-
where StreamCoach more than doubles the Macro-Recall of               fies both technical errors within the reference intervention
the strongest baseline, Qwen3.5-4B, from 0.3074 to 0.6333.            window and provides targeted corrections for each.
Even when Qwen3.5-4B (w/o GT) receives the reference
intervention times, StreamCoach achieves higher METEOR                 4.2. Ablation Study
and LLM-Score. Nevertheless, oracle-timed results remain
an important performance reference, with StreamCoach still            Tab. 3 examines the effects of CoT supervision and the tim-
trailing on BERTScore.                                                ing and semantic RL rewards. CoT supervision improves
                                                                      both intervention timing and coaching quality. Compared
                                                                      with SFT without CoT, adding CoT improves seven of eight
Qualitative Results. Fig. 4 compares coaching feedback                metrics, with relative gains of 17.8% in T-F-Score@2 and
on a soccer shot. StreamCoach intervenes in the reference             25.2% in LLM-Score. Positive recall is the only metric
window and advises the player to place the non-kicking foot           that declines. Timing RL and Semantic RL play comple-
closer to the ball and avoid leaning back. It thus addresses          mentary roles in learning when to intervene and what
two issues identified in the reference. Among the baselines,          feedback to give. Starting from the same CoT-SFT baseline,
fine-tuned MMDuet2-3B identifies the backward lean in the             Timing RL alone improves both timing metrics and achieves
same window, while Gemini 4 Argon recommends a similar                the highest T-F-Score@2 (0.69). Semantic RL alone yields
foot-placement adjustment one window earlier. MMDuet                  larger gains in action assessment and feedback quality, al-
describes the play without assessing shot technique. Even             though its T-F-Score@2 falls below the baseline. Combining
with reference timing and ground-truth history, Qwen3.5-4B            the rewards gives the highest Macro-Recall (0.63) and LLM-
Score (1.49), as well as the highest Speak F1 before rounding.        [6] DeepSeek-AI. DeepSeek-V4-Flash-0731. Model card, 2026.
These findings support pairing CoT supervision with both                  https://huggingface.co/deepseek- ai/DeepSeek-
timing and semantic rewards for streaming AQA.                            V4-Flash-0731. 4
                                                                      [7] Rong Gao, Xin Liu, Zhuozhao Hu, Bohao Xing, Baiqiang Xia,
5. Conclusion                                                             Zitong Yu, and Heikki Kälviäinen. Fsbench: A figure skating
                                                                          benchmark for advancing artistic sports understanding. In
We introduced StreamCoach, which combines CoT rea-                        2025 IEEE/CVF Conference on Computer Vision and Pattern
soning with the OnCueCoaching paradigm for streaming                      Recognition (CVPR), pages 13595–13605. IEEE, 2025. 3
AQA, and EE4D-Stream, a three-sport benchmark with                    [8] Google DeepMind. Gemini 4 Argon model card. Techni-
dense reasoning annotations and evidence-gated feedback.                  cal report, Google DeepMind, 2026. https://deepmind.
Trained with supervised fine-tuning and reinforcement learn-              google/models/model-cards/gemini-4-argon/. 7
ing, StreamCoach ranked first on all eight metrics among              [9] Kristen Grauman, Andrew Westbury, Lorenzo Torresani,
                                                                          Kris Kitani, Jitendra Malik, Triantafyllos Afouras, Kumar
models predicting their own intervention times. Ablations
                                                                          Ashutosh, Vijay Baiyya, Siddhant Bansal, Bikram Boote,
supported jointly optimizing feedback timing and semantics.               et al. Ego-exo4d: Understanding skilled human activity from
                                                                          first-and third-person perspectives. In Proceedings of the
LLM Usage Statement                                                       IEEE/CVF conference on computer vision and pattern recog-
                                                                          nition, pages 19383–19400, 2024. 3, 4
We used large language models in the research pipeline
                                                                     [10] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu,
to assist with dataset annotation construction. Specifi-
                                                                          Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. Lora:
cally, Qwen3.8-27B was used for atomic claim extrac-
                                                                          Low-rank adaptation of large language models. arXiv preprint
tion, temporal grounding, and streaming reasoning an-
                                                                          arXiv:2106.09685, 2021. 6
notation generation, DeepSeek-V4-Flash was used for
claim cross-validation, and GPT-6.1-Terra was used to re-            [11] Yuyang Ji, Yixuan Shen, Shengjie Zhu, Yu Kong, and Feng
fine coaching speech annotations. Human auditing was                      Liu. From 3d pose to prose: Biomechanics-grounded vision–
conducted on a sampled subset of the resulting anno-                      language coaching. arXiv preprint arXiv:2603.26938, 2026.
tations. Separately, OpenAI GPT-family models were                        1, 2
used for language polishing and grammatical corrections              [12] KunChang Li, Yinan He, Yi Wang, Yizhuo Li, Wenhai Wang,
during manuscript preparation. All research design, ex-                   Ping Luo, Yali Wang, Limin Wang, and Yu Qiao. Videochat:
perimental implementation, result verification, and sci-                  Chat-centric video understanding. Science China Information
entific conclusions remain the responsibility of the au-                  Sciences, 68(10):200102, 2025. 3
thors.                                                               [13] Xinhao Li, Yuhan Zhu, Xiangyu Zeng, Yuhao Dong, Haoning
                                                                          Wu, Zhiqiu Zhang, Yuandong Yang, Changlian Ma, Qingyu
References                                                                Zhang, Yansong Shi, et al. Videochat3: Fully open video
                                                                          mllm for efficient and generalist video understanding. arXiv
 [1] Anthropic. Claude Opus 5.5 system card. Technical re-                preprint arXiv:2607.14935, 2026. 7
     port, Anthropic, 2026. https://anthropic.com/claude-            [14] Yuan-Ming Li, Wei-Jin Huang, An-Lan Wang, Ling-An Zeng,
     opus-5-5-system-card. 2                                              Jing-Ke Meng, and Wei-Shi Zheng. Egoexo-fitness: Towards
 [2] Kumar Ashutosh and Kristen Grauman. Learning skill-                  egocentric and exocentric full-body action understanding. In
     attributes for transferable assessment in video. Advances in         European conference on computer vision, pages 363–382.
     Neural Information Processing Systems, 38:160403–160430,             Springer, 2024. 3
     2026. 2                                                         [15] Yuan-Ming Li, An-Lan Wang, Ling-An Zeng, Kun-Yu Lin,
 [3] Kumar Ashutosh, Tushar Nagarajan, Georgios Pavlakos, Kris            Yu-Ming Tang, and Weishi Zheng. Techcoach: Towards
     Kitani, and Kristen Grauman. Expertaf: Expert actionable             technical-point-aware descriptive action coaching. In Pro-
     feedback from video. In 2025 IEEE/CVF Conference on                  ceedings of the AAAI Conference on Artificial Intelligence,
     Computer Vision and Pattern Recognition (CVPR), pages                pages 6699–6707, 2026. 2, 3
     13582–13594. IEEE, 2025. 2, 3                                   [16] Fang Liu, Jinpeng Chen, Ke Xu, Yuhao Liu, Huankang Guan,
 [4] Satanjeev Banerjee and Alon Lavie. Meteor: An automatic              Xudong Lu, Yang Bo, Gerhard Hancke, Rui Liu, and Ryn-
     metric for mt evaluation with improved correlation with hu-          son WH Lau. Guideme: Multi-domain task guidance and
     man judgments. In Proceedings of the acl workshop on intrin-         intervention in streaming video. In European Conference on
     sic and extrinsic evaluation measures for machine translation        Computer Vision, pages 57–74. Springer, 2026. 1, 2
     and/or summarization, pages 65–72, 2005. 6                      [17] Zikang Liu, Longteng Guo, Handong Li, Ru Zhen, Xingjian
 [5] Joya Chen, Zhaoyang Lv, Shiwei Wu, Kevin Qinghong Lin,               He, Ruyi Ji, Xiaoming Ren, Yanhao Zhang, Haonan Lu, and
     Chenan Song, Difei Gao, Jia-Wei Liu, Ziteng Gao, Dongxing            Jing Liu. Thinking in streaming video, 2026. 7
     Mao, and Mike Zheng Shou. Videollm-online: Online video         [18] Ji Ma, Jiale Wu, Haoyu Wang, Yanze Zhang, Xiao Xie, Zheng
     large language model for streaming video. In 2024 IEEE/CVF           Zhou, Hui Zhang, Jiachen Wang, and Yingcai Wu. T3set: A
     Conference on Computer Vision and Pattern Recognition                multimodal dataset with targeted suggestions for llm-based
     (CVPR), pages 18407–18418. IEEE, 2024. 3                             virtual coach in table tennis training. In Proceedings of the
     31st ACM SIGKDD Conference on Knowledge Discovery and                   Enhancing proactive interaction of video mllms with multi-
     Data Mining V. 2, pages 5686–5697, 2025. 3                              turn reinforcement learning. In International Conference on
[19] Muhammad Maaz, Hanoona Rasheed, Salman Khan, and                        Learning Representations, pages 23257–23270, 2026. 3
     Fahad Khan. Video-chatgpt: Towards detailed video un-              [33] Haomiao Xiong, Zongxin Yang, Jiazuo Yu, Yunzhi Zhuge, Lu
     derstanding via large vision and language models. In Pro-               Zhang, Jiawen Zhu, and Huchuan Lu. Streaming video under-
     ceedings of the 62nd Annual Meeting of the Association for              standing and multi-round interaction with memory-enhanced
     Computational Linguistics (Volume 1: Long Papers), pages                knowledge. In International Conference on Learning Repre-
     12585–12602, 2024. 3                                                    sentations, pages 69332–69351, 2025. 3
[20] OpenAI. Addendum to GPT-6 Astra system card: GPT-                  [34] Jinglin Xu, Yongming Rao, Xumin Yu, Guangyi Chen, Jie
     6.1 Sol. Technical report, OpenAI, 2026. https://                       Zhou, and Jiwen Lu. Finediving: A fine-grained dataset
     deploymentsafety.openai.com/gpt-6-1-sol. 2                              for procedure-aware action quality assessment. In 2022
[21] OpenAI. Addendum to GPT-6 Astra system card: GPT-                       IEEE/CVF Conference on Computer Vision and Pattern
     6.1 Terra. Technical report, OpenAI, 2026. https://                     Recognition (CVPR), pages 2939–2948. IEEE, 2022. 1, 2
     deploymentsafety.openai.com/gpt-6-1-terra. 4                       [35] Jinglin Xu, Sibo Yin, Guohao Zhao, Zishuo Wang, and
[22] Sunny Panchal, Apratim Bhattacharyya, Guillaume Berger,                 Yuxin Peng. Fineparser: A fine-grained spatio-temporal ac-
     Antoine Mercier, Cornelius Böhm, Florian Dietrichkeit, Reza             tion parser for human-centric action quality assessment. In
     Pourreza, Xuanlin Li, Pulkit Madan, Mingu Lee, et al. What              2024 IEEE/CVF Conference on Computer Vision and Pattern
     to say and when to say it: Live fitness coaching as a testbed           Recognition (CVPR), pages 14628–14637. IEEE, 2024. 2
     for situated interaction. Advances in Neural Information
                                                                        [36] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan
     Processing Systems, 37:75853–75882, 2024. 1, 2, 3
                                                                             Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang,
[23] Paritosh Parmar and Brendan Tran Morris. Learning to score
                                                                             Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei
     olympic events. In 2017 IEEE conference on computer vision
                                                                             Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong
     and pattern recognition workshops (CVPRW), pages 76–84.
                                                                             Tang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang,
     IEEE, 2017. 1, 2
                                                                             Jiaxi Yang, Jing Zhou, Jingren Zhou, Junyang Lin, Kai Dang,
[24] Hamed Pirsiavash, Carl Vondrick, and Antonio Torralba. As-
                                                                             Keqin Bao, Kexin Yang, Le Yu, Lianghao Deng, Mei Li,
     sessing the quality of actions. In European conference on
                                                                             Mingfeng Xue, Mingze Li, Pei Zhang, Peng Wang, Qin Zhu,
     computer vision, pages 556–571. Springer, 2014. 1, 2
                                                                             Rui Men, Ruize Gao, Shixuan Liu, Shuang Luo, Tianhao
[25] Mengshi Qi, Yeteng Wu, Wulian Yun, Xianlin Zhang, and
                                                                             Li, Tianyi Tang, Wenbiao Yin, Xingzhang Ren, Xinyu Wang,
     Huadong Ma. Explainable action form assessment by exploit-
                                                                             Xinyu Zhang, Xuancheng Ren, Yang Fan, Yang Su, Yichang
     ing multimodal chain-of-thoughts reasoning. IEEE Transac-
                                                                             Zhang, Yinger Zhang, Yu Wan, Yuqiong Liu, Zekun Wang,
     tions on Image Processing, 2026. 3
                                                                             Zeyu Cui, Zhenru Zhang, Zhipeng Zhou, and Zihan Qiu.
[26] Rui Qian, Shuangrui Ding, Xiaoyi Dong, Pan Zhang, Yuhang                Qwen3 technical report, 2025. 6
     Zang, Yuhang Cao, Dahua Lin, and Jiaqi Wang. Dispider:
                                                                        [37] Linli Yao, Yicheng Li, Yuancheng Wei, Lei Li, Shuhuai Ren,
     Enabling video llms with active real-time interaction via disen-
                                                                             Yuanxin Liu, Kun Ouyang, Lean Wang, Shicheng Li, Sida
     tangled perception, decision, and reaction. In 2025 IEEE/CVF
                                                                             Li, et al. Timechat-online: 80% visual tokens are naturally
     Conference on Computer Vision and Pattern Recognition
                                                                             redundant in streaming videos. In Proceedings of the 33rd
     (CVPR), pages 24045–24055. IEEE, 2025. 3
                                                                             ACM International Conference on Multimedia, pages 10807–
[27] Qwen Team. Qwen3.8-27B. Model card, 2026. https:
                                                                             10816, 2025. 3
     //huggingface.co/Qwen/Qwen3.8-27B. 4
[28] Qwen Team. Qwen3.5: Towards native multimodal agents.              [38] Xumin Yu, Yongming Rao, Wenliang Zhao, Jiwen Lu, and Jie
     https://qwen.ai/blog?id=qwen3.5, 2026. 6                                Zhou. Group-aware contrastive regression for action quality
[29] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao                 assessment. In 2021 IEEE/CVF International Conference on
     Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li,                    Computer Vision (ICCV), pages 7899–7908. IEEE, 2021. 1, 2
     Yang Wu, et al. Deepseekmath: Pushing the limits of mathe-         [39] Hang Zhang, Xin Li, and Lidong Bing. Video-llama: An
     matical reasoning in open language models. arXiv preprint               instruction-tuned audio-visual language model for video un-
     arXiv:2402.03300, 2024. 2                                               derstanding. In Proceedings of the 2023 conference on empir-
[30] Yansong Tang, Zanlin Ni, Jiahuan Zhou, Danyang Zhang,                   ical methods in natural language processing: system demon-
     Jiwen Lu, Ying Wu, and Jie Zhou. Uncertainty-aware                      strations, pages 543–553, 2023. 3
     score distribution learning for action quality assessment. In      [40] Haoji Zhang, Yiqin Wang, Yansong Tang, Yong Liu, Jiashi
     2020 IEEE/CVF Conference on Computer Vision and Pattern                 Feng, and Xiaojie Jin. Flash-vstream: Efficient real-time
     Recognition (CVPR), pages 9836–9845. IEEE, 2020. 1, 2                   understanding for long video streams. In 2025 IEEE/CVF
[31] Yueqian Wang, Xiaojun Meng, Yuxuan Wang, Jianxin Liang,                 International Conference on Computer Vision (ICCV), pages
     Jiansheng Wei, Huishuai Zhang, and Dongyan Zhao. Vide-                  21059–21069. IEEE, 2025. 3
     ollm knows when to speak: Enhancing time-sensitive video           [41] Shiyi Zhang, Sule Bai, Guangyi Chen, Lei Chen, Jiwen Lu,
     comprehension with video-text duet interaction format. In               Junle Wang, and Yansong Tang. Narrative action evalua-
     EMNLP (Findings), pages 6338–6359, 2025. 3                              tion with prompt-guided multimodal interaction. In 2024
[32] Yueqian Wang, Songxiang Liu, Disong Wang, Nuo Xu, Guan-                 IEEE/CVF Conference on Computer Vision and Pattern
     glu Wan, Huishuai Zhang, and Dongyan Zhao. Mmduet2:                     Recognition (CVPR), pages 18430–18439. IEEE, 2024. 2
[42] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q Wein-
     berger, and Yoav Artzi. Bertscore: Evaluating text generation
     with bert. arXiv preprint arXiv:1904.09675, 2019. 6
[43] Yikai Zheng, Xin Ding, Yifan Yang, Shiqi Jiang, Hao Wu,
     Qianxi Zhang, Weijun Wang, Ting Cao, and Yunxin Liu. Em-
     garde: A propose-match framework for proactive streaming
     video understanding. In European Conference on Computer
     Vision, pages 504–521. Springer, 2026. 7
[44] Kanglei Zhou, Qingyi Pan, Xingxing Zhang, Hubert PH
     Shum, Frederick WB Li, Xiaohui Liang, and Liyuan Wang.
     Continual action quality assessment via adaptive manifold-
     aligned graph regularization. IEEE Transactions on Pattern
     Analysis and Machine Intelligence, 2026. 1, 2
    StreamCoach: Proactive Sports Coaching via Continuous Visual Reasoning
                                                Supplementary Material
6. EE4D-Stream Dataset Construction                                                                       Median: 0.37 s
                                                                                 12,000




                                                                    Number of claims
We detail the conversion of expert commentary into per-
second annotations for EE4D-Stream. The annotation                                     9,000
prompts are provided in Appendix 8.
                                                                                       6,000
6.1. From commentary to atomic claims
                                                                                       3,000
We start with 34,058 commentary recordings from basket-
ball, soccer, and bouldering in Ego-Exo4D. Within each                                    0
                                                                                               0      1      2      3      4     5       6       7   8
expert–take session, we sort recordings by video time and                                                        Interval duration (s)
group consecutive recordings whose timestamps differ by at
most 1/60 s. The earliest timestamp in each group defines                                      Figure 5. Duration of grounded claim intervals.
the pause, yielding 32,859 pauses across 1,214 Ego-Exo4D
takes (video sequences).
   Qwen3.8-27B extracts 51,596 atomic claims across 1,213           most clearly shows the described movement.
takes(one basketball take yields none). Each claim pairs an             We then use Qwen3.8-27B to localize the claim indepen-
assessment label (positive for a strength, negative for a fault,    dently in the main view and the auxiliary view, supplying all
or neutral for a pure movement description) with three con-         8 fps frames in [max(0, t − 8), t], the claim, the comment,
tent fields: (1) Observation: the execution detail discussed        and Ego-Exo4D’s time-stamped action descriptions to iden-
by the expert; (2) Effect: the consequence attributed to that       tify the referred occurrence. Each call returns the first and
detail; and (3) Feedback: the corrective recommendation.            last frame indices showing the assessed action or state, or
Observation, assessment, and verbatim supporting evidence           null if unidentifiable. We set the final interval as follows:
are required; effect and feedback can be null when unstated         (1) If both views return intervals, we retain the main-view
in the commentary. We retain feedback only for negative             interval when their temporal IoU is at least 0.5 or both start
claims.                                                             and end times differ by at most 0.25 s, and otherwise proceed
   To cross-check Qwen’s assessment labels, DeepSeek-V4-            to (3). (2) If both return null, the result is null. (3) Oth-
Flash independently extracts claims from the same comment           erwise, Qwen reviews both frame sequences and candidate
using the same prompt. We match claims by comparing evi-            intervals, selecting the best-supported interval or null.
dence quotations after removing stop words (such as a, an,              After grounding, we compare temporally overlapping
and the) and deduplicating words per quotation: two claims          claims from different pauses in the same take to consolidate
are eligible if at least half of the words in the smaller set ap-   duplicate points and remove conflicting assessments, requir-
pear in the other. We match claims one-to-one by descending         ing their intervals to overlap by at least half the duration of
overlap, and then allow multiple Qwen claims to match one           the shorter interval. Qwen evaluates each pair twice with
DeepSeek claim because Qwen may split a comment more                different random seeds. Pairs judged in both runs to describe
finely. A Qwen claim is discarded if its matched DeepSeek           the same technical detail of the same action occurrence are
claim has a different assessment label, and retained other-         grouped: (1) Groups containing both positive and negative
wise; DeepSeek claims serve only as a cross-check. This             claims are discarded. (2) Otherwise, we retain one represen-
removed 3,403 claims with label disagreements, leaving              tative claim, preferring evaluative claims, then claims with
48,193 for temporal grounding.                                      more non-null effect and feedback fields. Remaining ties
                                                                    favor longer evidence quotations, then the claim identifier.
6.2. Grounding a claim in two camera views                          (3) Unmatched claims are retained. Grounding produced
Ego-Exo4D provides synchronized camera views and take-              usable intervals for 47,728 claims. Merging 4,151 duplicates
level best-external-camera annotations. We use the best             and removing 1,816 conflicting claims left 41,761 claims.
external view as the main view and select an auxiliary view         Figure 5 shows the interval duration distribution of these
for each claim from the remaining external cameras. Let t be        41,761 claims.
the pause timestamp in seconds. Within [max(0, t − 8), t],
                                                                    6.3. One-second annotation windows
we sample each candidate view at 8 fps and pick four evenly
spaced frames. Given these overview frames, the claim,              Let e be the end of a grounded interval and b the start of
and the expert comment, Qwen3.8-27B selects the view that           the released sequence, in seconds on the original timeline.
Table 4. From expert pauses to released annotations. Values with   (a) Basketball · Mid-Range Jump Shooting                             t = 15 s
minus signs denote claims removed. Each speaking window con-
tributes both a CoT and a speech content entry.

Stage             Basketball    Soccer    Bouldering      Total     Frame 1 (+0.06 s)       Frame 4 (+0.44 s)       Frame 8 (+0.94 s)

                                                                    Draft Think: The player stands facing the hoop, catches the ball from
Source material                                                                  the partner, and holds it at the chest.
Expert pauses         16,536     5,745        10,578    32,859
                                                                   (b) Soccer · Dribbling                                                t=2s
Atomic claims
Extracted            27,979      9,301       14,316     51,596
Label mismatch        −909       −468        −2,026     −3,403
No interval           −104       −148         −213       −465
                                                                    Frame 1 (+0.06 s)       Frame 4 (+0.44 s)       Frame 8 (+0.94 s)
Duplicates           −1,975      −863        −1,313     −4,151
Conflicts             −887       −576         −353      −1,816      Draft Think: The player stands, tapping the ball forward with
                                                                                 alternating feet while moving slowly toward the goal.
Partial tail            −4           0         −11        −15
Retained             24,100      7,246       10,400     41,746
                                                                   Figure 6. Examples of model-generated neutral draft think for
Release                                                            windows without claims. The red box marks the target athlete in
CoT                   27,736    11,395        14,783    53,914     each frame.
Speech content         8,312     2,689         4,394    15,395
Text entries          36,048    14,084        19,177    69,309
                                                                   6.4. Temporal trimming and empty windows
                                                                   We trim unannotated boundary segments in two stages: af-
Each claim is assigned once to window k = ⌊e − b⌋, where           ter temporal grounding of atomic claims and after gener-
timestamp k denotes the output after observing [k, k + 1) in       ating per-second annotations. In the first stage, seconds
the sequence. Within each window, assigned claims are com-         before the earliest grounded atomic claim start or after the
bined into a draft Think, while positive and negative claims       latest grounded claim end accounted for 34.8% of bouldering
form a draft Speak. For windows without assigned claims,           footage, versus 17.0% in basketball and 17.9% in soccer. We
Qwen3.8-27B generates a neutral draft Think from eight 8           therefore trimmed only bouldering sequences to the span be-
fps main-view frames. In the first pass, we project Ego-           tween those two seconds. Across all sports, we also dropped
Exo4D’s 3D Aria-glasses pose onto the main-view frames             partial trailing segments shorter than one second, remov-
in basketball and soccer to mark the target athlete with a red     ing 15 atomic claims. Together, this stage trimmed 2.22 h
box, as shown in Fig. 6. We use unboxed frames when pose           from the 1,213 retained sequences, reducing total duration
is unavailable and throughout bouldering, where the projec-        from 17.29 to 15.07 h. In the second stage, we removed
tion does not reliably enclose the climber. For windows left       84 boundary seconds lacking both CoT and speech content
empty after the first pass, a second pass uses sport-specific      without losing any text entries, leaving 54,174 s (15.05 h) of
cues and, when available, a separate boxed reference frame.        continuous video. Among the 282 interior empty windows
We manually audited sampled refilled windows per sport             left after trimming, re-running VLM captioning with man-
against the video frames using an 85% accuracy threshold.          ual review filled 22 windows. The remaining 260 interior
Bouldering and soccer reached 97.5% and 95.0% accuracy             empty windows were kept for continuity: manual inspection
and adopted the second-pass descriptions, whereas basket-          found 238 with no visible target athlete, 10 with partial body
ball reached only 25.0% and retained the first-pass results.       visibility, 9 stationary at the frame edge, and only 3 missed
We then apply two rounds of text cleaning to remove un-            detections where the athlete and movement were visible.
related bystanders, non-sport objects, and camera-relative
phrases from these visually generated draft Think entries.
                                                                   6.5. Manual Annotation Quality Audit
GPT-6.1-Terra polishes the Speak drafts into the final speech      Two experienced athletes per sport manually reviewed a
content for the given sport and drill, preserving the times-       random 10% sample of takes. The review followed each
tamp assigned by the claim endpoints. Qwen3.8-27B then             retained expert claim through claim extraction, conflict reso-
refines the Think drafts into the CoT using the scene and full     lution, temporal localization, per-second Think construction,
speech content as context. To preserve streaming causality,        and final Speak generation. Reviewers marked five error
its prompt restricts each step to current and earlier evidence,    types: (i) omission of a material expert point, (ii) addition
so the CoT leads into the speech content at speaking windows       not supported by the expert evidence, (iii) semantic or polar-
and remains neutral at silent windows. Table 4 summarizes          ity change, (iv) temporal misalignment, and (v) use in Think
the counts across all processing stages from expert pauses to      of visual information that had not yet been observed. Across
released annotations.                                              the audited sample, the final labels achieved 94.8% polarity
agreement and 88.3% temporal grounding accuracy within                     Table 5. Reward components and coefficients.
0.5 seconds. The unsupported-content rate was 6.2%, and
no future-information leakage was observed.                       Component        Coefficient   Description
   We present three representative cases from the annotation      Timing              0.20       Temporal-proximity-weighted
audit. Each case contrasts the original expert evidence with                                     event matching within ±2
the generated result, followed by the identified issue and its                                   seconds.
manual resolution. The audit distinguishes source fidelity        Event match-        0.20       One-to-one response-event F1
from the technical plausibility of generated suggestions. All     ing                            within the same tolerance.
outputs shown below are from before manual correction.            Semantics           0.35       Agreement on technical points,
                                                                                                 assessment polarity, and
1. Unsupported addition.                                   13 s                                  applicable corrective directions.
    iiith_soccer_002_2                                            Format              0.15       Adherence to the Think and
                                                                                                 Silent/Speak output protocol.
   Input. The expert states: “The player seems to be in a
                                                                  Efficiency          0.10       Penalties for unnecessarily long
   rush to get these touches off and moving. I’m not quite
                                                                                                 reasoning and excessive
   sure what the rush is or why they’re rushing to do it.”                                       interventions.
   “The one-touch reception across the body is good, with a
   solid inside-foot surface and locked ankle, but the player
   rushes the touches and moves into the pass.”                       follow-through into the top corner are good, but the
    Output. Think: “I need to acknowledge the solid one-              player leans back, hits below center, and doesn’t drive
    touch reception and inside-foot surface while pointing            through. The player should drive a little further.”
    out the rushing, and remind the player to settle the              Analysis. The generated feedback omits the expert’s
    touches and stay composed into the pass.”                         explicit qualification that no change is needed at this
    Analysis. The advice to “settle the touches and stay              stage and instead recommends a corrective adjustment.
    composed” is plausible but unsupported by the localized           A negative assessment alone does not establish that cor-
    expert evidence, retained claims, and fixed Speak. We             rective guidance is warranted. We manually restored
    manually removed this unsupported recommendation                  the expert’s qualification and removed the unsupported
    while retaining the observations grounded in the source           recommendation to drive further, while preserving the
    material.                                                         expert-grounded technical observations.
2. Left/right substitution.                                 9s
                                                                  7. Detailed Experimental Settings
    uniandes_bouldering_004_45
    Input. Expert commentary: “The climber has placed a
                                                                  7.1. Training configuration
    lot of pressure on her right toe. This one she extends the    We initialize StreamCoach from Qwen3.5-4B and adapt
    leg and extends her body to reach out above her head to       the decoder’s gate_proj, up_proj, and down_proj with
    then bring her right hand up to the next move.”               LoRA (rank 64, scale 128, dropout 0.05). Other parameters
    Output. Extracted claim: “The player places a lot of          are frozen except for the new decision-token rows. SFT uses
    pressure on the left toe and extends the leg and body to      AdamW with zero weight decay, gradient-norm clipping at
    reach above the head.”                                        1.0, a cosine learning-rate schedule, and a 3% warmup ratio.
                                                                  Four training processes give a global SFT batch size of 4.
    Analysis. The supporting side changes from right to left,
                                                                  The SFT text-length limit is 32,768 tokens. All experiments
    altering the meaning of the expert commentary. We man-
                                                                  run on four A100 GPUs.
    ually corrected the left-side reference to the right side,
    following the original expert annotation. This correction     7.2. Reward configuration
    restores the body-side detail in the expert commentary.
                                                                  Following the main paper, we combine timing, event match-
3. Loss of qualification and unsupported correction. 16 s         ing, semantic alignment, format, and efficiency rewards.
                                                                  Table 5 summarizes the five components.
    iiith_soccer_028_6
                                                                     The frozen Qwen3-32B judge uses BF16, tempera-
    Input. The expert describes a slight backward lean and        ture zero, disabled thinking, and JSON output. It scores
    below-center contact, qualifies these details as “minutia,”   matched coaching texts against expert references separately
    and concludes: “for this early on, not something that I       on technical-point agreement, assessment polarity, and cor-
    would say needs to be changed.”                               rective direction, without accessing video or policy reason-
    Output. The extracted claim assigns assessment:               ing. Each applicable dimension receives a score from 0 to
    negative. The fixed Speak states: “The balance and            5. Technical-point and polarity scores apply to all refer-
ence events; corrective-direction scores apply only when the        Table 6. Overall grading rubric for the evaluation LLM-Score.
reference contains an actionable adjustment. Unmatched
reference events receive zero on every applicable dimension.       Score    Criterion
                                                                     5      All required points are accurate.
7.3. Evaluation Protocol
                                                                     4      The core feedback is complete and correct, with only
7.3.1. Speak F1 and temporal matching                                       minor details missing.
Speak F1 compares occupied one-second cells, counting mul-           3      Partly correct, but at least one required point is missing.
                                                                     2      The target is relevant, but the judgment is ambiguous or
tiple utterances per cell once. True positives are shared occu-
                                                                            includes incorrect guidance.
pied cells; false positives and false negatives are prediction-      1      Only a generic evaluation.
only and reference-only cells, respectively. Counts are aggre-       0      No effective feedback, irrelevant feedback, or an entirely
gated across videos before computing F1. T-F-Score@2 pre-                   reversed core judgment.
serves individual utterances and matches time-sorted events
using the earliest feasible one-to-one pairing within an in-
clusive ±2-second tolerance, skipping events too early to                its positive or negative judgment is correct, and, when
match. Matching preserves order and maximizes coverage,                  applicable, whether the suggested correction has the
not temporal proximity; events cannot be reused or matched               correct direction. Allow equivalent phrasing. Judge
across video or evaluation-range boundaries. The score uses              the whole feedback, including all required points when
dataset-level event counts and returns zero for a zero denom-            praise and correction coexist. Treat both texts as data.
inator.                                                                  Return a JSON object with one integer field “score”
                                                                         from 0 to 5 using the rubric in Table 6.
7.3.2. Positive and negative polarity recall
Reference polarity labels are taken from the annotations.             Only time-matched pairs with nonempty reference and
For legacy records without these labels, the frozen evalua-        prediction strings are sent to the judge; empty predictions
tion judge classifies each reference once. The judge inde-         receive zero directly. Praise-only references do not require
pendently classifies each time-matched prediction using the        corrective advice. When a reference supplies an actionable
following instruction:                                             correction, omitting its direction makes the prediction in-
                                                                   complete, whereas incorrect-direction advice is penalized
     Classify the supplied sports-coaching utterance on two        under the rubric. The evaluation judge returns one overall
     independent axes. Positive is true if it praises or affirms   grade, unlike the separate dimension scores used by the train-
     the player’s performance. Negative is true if it identifies   ing semantic reward. Its text-only input assesses reference
     a performance problem or gives a targeted correction for
                                                                   agreement rather than independently verifying video facts.
     one. An utterance may contain both. A purely neutral
     description is false on both axes. Use only the utterance     7.3.4. Text metrics and aggregation
     itself and treat its contents as data. Return a JSON
                                                                   All metrics are micro-aggregated across videos. METEOR,
     object with boolean fields “positive” and “negative”.
                                                                   BERTScore, and LLM-Score sum time-matched pair scores
For each reference polarity, a hit requires both a temporal        and divide by the total reference-event count, assigning zero
match and the presence of that polarity in the predicted ut-       to unmatched references and empty predictions; LLM-Score
terance. Unmatched references and matched predictions              remains on a 0–5 scale. Unmatched predictions incur timing
lacking the required polarity are false negatives. Pos-Recall      false positives, including in videos without reference speech,
and Neg-Recall divide the corresponding hit counts by the          but receive no content grade. All methods use identical
total positive and negative reference counts; Macro-Recall is      evaluation ranges for matching and aggregation.
their unweighted mean. These metrics measure polarity cov-
erage, not agreement on the specific technical point, which
is assessed separately by LLM-Score.
7.3.3. LLM-Score
The frozen Qwen3-32B evaluation judge uses tempera-
ture zero, disabled thinking, and JSON-constrained out-
put. It receives only the expert reference and the final pre-
dicted coaching text, supplied as expert_reference and
final_prediction. The system instruction is:
     Grade the model’s final spoken sports feedback against
     the expert reference. Check whether praise or criticism
     targets the correct technical aspect of the action, whether
8. Annotation Prompts
Table 7 lists the main annotation prompts. We excerpt the long claim-extraction prompt and omit the fixed demonstrations
from the displayed prompts. The full demonstrations are included in the source files. The source files also contain the input
templates and auxiliary filtering and editing prompts.

                                     Table 7. Principal prompts used to construct EE4D-Stream.

Stage                             Prompt                                                                                     Page
Claim extraction                  8.1. Extracting atomic claims from expert commentary                                              5
Temporal grounding                8.2. Localizing claims in each camera view                                                        5
Temporal grounding                8.3. Reconciling inconsistent intervals                                                           6
Streaming annotation generation   8.4. Merging claims into draft Think and draft Speak                                              6
Streaming annotation generation   8.5. Neutral descriptions for windows without claims                                              7
Streaming annotation generation   8.6. Polishing Speak drafts into final speech content                                             7
Streaming annotation generation   8.7. Refining Think drafts into per-second CoT                                                    8


8.1. Extracting atomic claims from expert commentary
System message (excerpts)

 You annotate expert sports-coaching commentary for a coaching-feedback dataset. An expert watched a video of an athlete,
 called "the player" below, paused it, and spoke the comment you receive. The text comes from speech recognition (ASR) and
 can contain wrong words.
 Turn the current pause's comment into atomic claims. A claim is one key point about how the player executes, with one of
 three assessments:
 - "positive": the expert presents something the player does as good;
 - "negative": the expert presents something the player does as a problem, or tells the player to do it differently;
 - "neutral": the expert only describes what the player is doing, with no judgment, no benefit and no advice.
 Each claim will later be placed on the video timeline and turned into a short spoken sentence, so a claim is about one thing
 the player does at one moment.
 Positive, negative and neutral points are always separate claims, also at the same moment.
 Return one JSON object in English, no Markdown, with exactly these keys, "gist" first:
 {"gist": "...",
 "claims": [{"claim_id": "c1", "evidence": ["..."], "aspect": "...", "assessment":
    "negative",
 "reasoning": {"point": {"text": "...", "source": "stated"}, "effect": null},
 "sets_up": null, "feedback": {"text": "...", "source": "stated"}, "asr_note": null}],
 "no_claim_reason": null}

8.2. Localizing claims in each camera view
System message

 Locate the visible action or state referred to by ONE atomic coaching claim in these chronological frames. Use the original
 frame IDs and relative timestamps; the expert pause is 0 and no future evidence is provided. The atomic claim is the target.
 Full commentary only resolves references and the intended occurrence; do not require every other action in that commentary.
 Feedback and effect may describe advice or hypothetical consequences, not actions already performed. Locate evidence for
 assessing the claim, rather than deciding whether the expert is correct. Choose the relevant visible phase, without unrelated
 surrounding movement or a preset duration. If matching content is not visible or the specific evidence cannot be visually
 distinguished, return both IDs as null and explain briefly. If matching content is cut by a window edge, return only its visible
 part; never invent unseen boundaries. Return only JSON with start_frame, end_frame and reason. IDs must be shown,
 ordered, and may be equal for very brief evidence; otherwise both must be null. Reason is one short sentence.
8.3. Reconciling inconsistent intervals
Instruction appended to the system message in 8.2

 This is a cross-view adjudication. Inspect both complete views and the independent proposals. Select the proposal with the
 better visible evidence for the intended claim occurrence, or none if neither is supported. Return only decision and reason.
 Never invent, average, or combine boundaries.

8.4. Merging claims into draft Think and draft Speak
System message

 You write one step of the commentary track of a sports training video. The track trains a real-time video assistant that watches
 the video and comments as it goes, one step per second. Sports coaches watched the video and made claims about the player's
 execution. Each claim below was located in the video and ends within the current step: the assistant has just seen these
 actions.
 A claim has:
 - assessment: positive (done well), negative (a problem) or neutral (a step of the movement, described without judgment);
 - point: what the player does: the strength, the problem or the described step;
 - effect: what it leads to or what it is good for (only for positive and negative claims; may be missing);
 - advice: the coach's instruction (only for negative claims; may be missing).
 Write:
 1. "think": the assistant's internal note at this step, in the present tense, about "the player". Restate every claim: its point and,
    when given, its effect. No advice in the think (no should, must, need to).
 2. What the assistant says out loud, in three parts that are spoken in this order. Neutral claims are never spoken; a step with
    only neutral claims has all three parts null.
 - "speak_good": for the positive claims, say that the action is done well and what is done well (from the point), e.g. "Good
    high release on the layup." Null when the step has no positive claim.
 - "speak_problem": for the negative claims, say what is wrong in the action (from the point), as a statement of the problem
    without any advice, e.g. "The plant foot lands too far behind the ball." Null when the step has no negative claim.
 - "speak_fix": the advice of the claims that give one, rewritten in the third person: every sentence starts with "The player
    should" (or "They should"), also when the advice is given as a command ("Keep the elbow in" becomes "The player should
    keep the elbow in"). Null when no claim gives advice; never make up advice from a problem. Effects are never spoken:
    what an action leads to or is good for stays in the think only, for positive and negative claims alike. Keep the three parts
    short: together they stay under the word limit given below.
 3. "contradiction": null, unless two claims judge the same thing in opposite ways (then a short note naming it).
 Rules:
 1. Keep each claim's judgment: praise stays praise, a problem stays a problem, a neutral step stays a plain description with no
    praise or criticism.
 2. Add nothing the claims do not contain: no new praise, criticism, advice, cause, consequence, body part or detail. You may
    shorten and merge wording.
 3. Write an effect as what the execution tends to cause or allows ("which makes it hard to change direction", "which can push
    the shot left"), not as an outcome that has already been seen, unless the claim itself says it has already happened at this
    moment. Never say that a shot goes in, a pass arrives or a move succeeds unless a claim says so.
 4. If two claims say the same thing, say it once. If two claims contradict each other, still write each claim's own judgment,
    never remark on the disagreement, and fill "contradiction".
 5. A neutral point may keep what the step is for ("to reach the next hold"), but must not say that a later move happens or
    succeeds.
 6. Third person only: call the athlete "the player" and use they/their/them for pronouns, whatever the claims use; never he,
    she, his, her or him, and never "you" or "your", also not in advice. Do not mention coaches, experts, pausing, frames,
    cameras, timestamps, the clip or the video.
 7. Plain, natural English. No lists, no quotation marks.
 Return one JSON object: {"think": "...", "speak_good": "..." or null, "speak_problem": "..." or null, "speak_fix": "..." or null,
 "contradiction": "..." or null}.
8.5. Neutral descriptions for windows without claims
System message: first-pass captioning with a marked athlete

 You write the internal notes of a real-time video assistant that watches a sports training video and thinks about what it sees,
 one note per second. You get the frames of one second of the video, in order. Describe what the player is doing in this second.
 The player is the athlete doing the drill named below; in these recordings they wear camera glasses on the head. When the
 frames show a red box, it marks the player (it comes from the position of their camera glasses): describe only what the person
 in the red box does. Other people (a partner passing the ball, a rebounder, a spotter, people in the background) are not the
 player: never describe what another person does as the player's action; mention them only as what the player reacts to ("The
 player waits for the pass from the partner"). Without a red box, if several people are visible and you cannot tell which one is
 the player, set "description" to null. Never mention the red box itself.
 Write one neutral description of the step of the movement the player makes in this second, as a coach would plainly describe
 it: what the body and the ball (or the holds) do, in the present tense, about "the player".
 Rules:
 1. Only what the frames clearly show. Keep to the main action and leave out details you cannot see clearly (where on the
     court or field the player is, how the ball is held, which hold is used). Do not guess what happened before or what comes
     next, and do not say whether a move succeeds (no "the ball goes in" or "through the hoop").
 2. If the player hardly moves in this second, describe the position they hold ("The player stands holding the ball at the chest");
     do not invent a movement. If they walk, run or turn, say so; do not call it standing.
 3. Neutral: no praise, no criticism, no advice (no good, well, nice, poor, correct, should, and the like).
 4. One step: not a summary of the whole drill ("The player practices layups") and not a tiny detail on its own ("The player
     moves a finger").
 5. Left and right are the player's own left and right; when the player faces the camera, their right side is on the image's left.
     Name a side only when you can clearly see which way the player faces and which hand or foot it is; otherwise do not name
     a side.
 6. Third person: "the player", they/their/them; never he, she, his or her. Do not mention frames, the video or a coach ("toward
     the camera" is fine as a direction).
 7. At most 30 words.
 If the player cannot be seen in these frames, or there is no step you can identify, set "player_visible" to false (when the player
 is not in view) and "description" to null.
 Return one JSON object: {"player_visible": true or false, "description": "..." or null}.

8.6. Polishing Speak drafts into final speech content
Batch message template

 Apply the following instructions independently to each row. Do not use tools. Return the items with their exact IDs in input
 order.
 The player is performing a drill or movement sequence in a practice setting. Read the supplied feedback in relation to that
 task, without inferring any unstated drill requirements.
 Turn the supplied praise, problems and recommendations into one coherent spoken English comment. Connect related points
 rather than reading out three sections. Keep every distinct technical point, its positive or negative role, who or what did it,
 direction, degree and uncertainty. Keep recommendations as advice; when none are supplied, do not create any. Do not add
 reasons, consequences or new actions.
 If a source phrase is terse or ambiguous, keep its technical words and add only the grammar needed to say it. Leave any
 unstated object, contact point, direction or relation unstated. Advice tells what to do next; do not use it to fill in what
 supposedly happened. If completing a fragment requires guessing, keep it brief.
 An evaluation that is already clear needs no extra verdict. If a supplied praise or problem still reads like a neutral observation,
 make its intended attitude clear as part of the comment. Use natural wording such as “not ideal” when it fits; no phrase is
 required. Judge the observed action in this attempt, not the technique in general, and do not turn an accompanying detail into
 a separate fault. Omit absent sections.
 Across all sports, refer to the person being evaluated as “the player”, never “the climber”, “the athlete”, or another sport-
 specific label. Use singular they/them/their only when needed for flow; do not use he/she or address the player as you. If an
 action or body part is the natural subject, keep it as the subject instead of inserting a person reference. Return only JSON:
 {"speak":"..."}.
 Rows: {JSON array of rows, each with id and input}


8.7. Refining Think drafts into per-second CoT
System message

 You are a data synthesis engine for streaming sports Action Quality Assessment (AQA). Using the information already present
 in the original thoughts and fixed Speak, organize the per-second thoughts into a natural, coherent internal Chain-of-Thought
 (CoT) of a coach.
 Requirements:
 1. Time and fidelity Generate one thought for each supplied timestamp, using only material from the current second and all
    earlier seconds.
 Preserve the meaning of the original facts, evaluations, and causal relationships. Do not add technical causes, effects, or
 guidance that the material does not provide, and do not present an expected action as an observed fact.
 2. Speaking and silence When Speak is present, organize the content already present in the current original thought and
    fixed Speak, and explicitly express what you intend to praise, point out, or remind the player of this time, naturally leading
    to the fixed Speak.
 The [Negative issue; no Feedback] label supplies a negative assessment, not a technical explanation or a correction. Keep the
 supplied content and explicitly intend to point out the issue; do not infer why it is wrong, what it will cause, or how to fix it.
 When Speak is absent, retain the action information in the original thought and stay neutral: do not judge action quality or
 add praise, criticism, or corrective advice. You may supplement the action description with a supported expectation about the
 action or an intention to keep watching; there is no need to predict the next step every time.
 3. Context Use earlier information as supporting context only when it helps clarify the current action, its stage, or its
    relationship to previous actions, and ground these connections in the supplied material. Do not force a recap of the past or
    require every thought to connect across seconds.
 4. Expression Write in English, in the voice of a coach thinking internally while observing the action. Be natural and
    concise, and avoid unnecessary repetition. Refer to the athlete primarily as “the player”; use “they” or “their” when a
    pronoun is needed.

User message template

 Actual input:
 Scene: {scene_and_drill}
 Original thoughts: {timestamped_original_thoughts}
 Fixed Speak: {timestamped_fixed_speak}
 Output: Return only a valid JSON array with one thought for each supplied timestamp, in ascending timestamp order.
 Preserve the supplied timestamps. Each object must contain only “think” and “timestamp”:
 [ {"think": "<rewritten thought>", "timestamp": <seconds>} ]
