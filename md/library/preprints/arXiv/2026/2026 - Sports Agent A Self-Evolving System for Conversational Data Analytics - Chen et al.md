<!-- source: library/preprints/arXiv/2026/2026 - Sports Agent A Self-Evolving System for Conversational Data Analytics - Chen et al.pdf -->
<!-- item: https://arxiv.org/abs/2611.33700 -->
<!-- authors: Chao Chen, Fuqi Lin, Ze Chen, Ziyan Liu, Chen Li, Haishu Jiang, Bo Xu, Zihan Jiang, Yue Wu, Zheng Wang, Kun Wang, Zhihang Fu, Jieping Ye -->
<!-- machine conversion from the stored PDF via pdftotext, 2026-11-26; equations, tables and figures are NOT preserved - consult the PDF for those -->

# Sports Agent: A Self-Evolving System for Conversational Data Analytics

                                                                                                                                            2026-11-26


                                                   Sports Agent: A Self-Evolving System for Conversational
                                                                        Data Analytics
                                                   Chao Chen* , Fuqi Lin* , Ze Chen* , Ziyan Liu* , Chen Li* , Haishu Jiang,
                                                         Bo Xu, Zihan Jiang, Yue Wu, Zheng Wang, Kun Wang,
                                                                         Zhihang Fu† , Jieping Ye†
                                                                              Alibaba Token Hub, Alibaba Group
                                                                 {ercong.cc, zhihang.fzh, yejieping}@alibaba-inc.com
arXiv:2611.33700v1 [cs.CL] 25 Nov 2026




                                                                                           Abstract
                                                       Conversational sports analytics requires agents to interpret user queries, coordi-
                                                       nate heterogeneous resources, and deliver accurate, evidence-based responses
                                                       with low latency. In production, changes in query distributions, data resources,
                                                       and model behavior can degrade the performance of static agent configura-
                                                       tions, while manual maintenance is often slow and costly. These challenges
                                                       motivate controlled, evidence-driven evolution to sustain reliable performance
                                                       in changing environments.
                                                       We present Sports Agent, a self-evolving framework for reliable conversational
                                                       sports analytics. It integrates an Agentic SQL Model for structured-data rea-
                                                       soning, a Sports Agent Harness for planning and tool orchestration, and a
                                                       unified Feedback Engine connecting online execution with offline evolution.
                                                       The engine assesses responses and execution trajectories, verifies factual claims,
                                                       diagnoses failures, and produces actionable evolution signals. Model evolution
                                                       combines SQL-to-Question Scaling to broaden coverage with Graph-Guided
                                                       Scaling to generate data targeting diagnosed errors. The synthesized questions
                                                       then undergo trajectory distillation and quality filtering for iterative super-
                                                       vised fine-tuning, followed by a separate Post-RL stage. Harness evolution
                                                       converts recurrent production issues into bounded prompt and skill updates,
                                                       validated through independent audits, execution replay, and regression testing.
                                                       Performance-tolerance checks prevent unacceptable performance degradation
                                                       during harness simplification.
                                                       Model evolution yields a Qwen3.6-35B-A3B-based Agentic SQL Model that
                                                       outperforms Qwen3.8-Max on question answering and analysis tasks over
                                                       sports data and achieves approximately three times the inference efficiency.
                                                       Across 30 successive harness-evolution rounds, the aggregate performance
                                                       score increases by 10.8 points. In a live sports analytics product, the evolved
                                                       version improves the factual correctness score by 10.5 points and the response
                                                       richness by 158.1%, while reducing average latency by 41.3% relative to the
                                                       non-evolved version.




                                         * Equal contribution.   † Corresponding author.

                                         We would like to thank the Qwen Team at Alibaba Token Hub (ATH), Alibaba Group, for providing the computational
                                         resources and foundation models (Qwen) used in this research.


                                                                                               1
Contents

1   Introduction                                                                                                    4
    1.1   Conversational Sports Data Analytics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           4
    1.2   Progressive Degradation of Static Agent Systems . . . . . . . . . . . . . . . . . . . . . . . .            4

    1.3   Research Problem and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           5
    1.4   Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      6


2   Sports Agent: Dual-Loop Evolution                                                                                6
    2.1   Problem Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        7

    2.2   Architecture Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        7

3   Model Self-Evolution Loop                                                                                        9

    3.1   Agentic SQL Task . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       9
    3.2   Model Evolution Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        10
          3.2.1   SQL-to-Question Scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       10

          3.2.2   Graph-Guided Scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        11
          3.2.3   Agentic Trajectory Distillation and Training . . . . . . . . . . . . . . . . . . . . . . .        12
    3.3   Post-RL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   13
    3.4   Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     14

          3.4.1   Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      14
          3.4.2   Model Performance Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          15
          3.4.3   Model Efficiency Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         15

          3.4.4   Ablation Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      15

4   Harness Self-Evolution Loop                                                                                     16

    4.1   Turning Accumulated Evidence into Coordinated Repairs . . . . . . . . . . . . . . . . . .                 17
    4.2   Intent Aggregation and Edit Synthesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         18
          4.2.1   Persistent Intent Aggregation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       18

          4.2.2   Bounded Edit Synthesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        19
    4.3   Dual-Audit Candidate Refinement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           20
    4.4   Post-Selection Consolidation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      20
          4.4.1   Evidence-Based Consolidation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          20

          4.4.2   Non-Inferiority Guard . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       21
    4.5   Case Study: From Repair Intents to Layer-Specific Updates . . . . . . . . . . . . . . . . . .             21
          4.5.1   Case A: A Cross-Task Evidence-Boundary Contract . . . . . . . . . . . . . . . . . .               21

          4.5.2   Case B: Task-Specific Career-Statistics Coverage . . . . . . . . . . . . . . . . . . . .          23



                                                          2
          4.5.3   Layer Responsibilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   24


5 A Unified Feedback Engine for Self-Evolution                                                                   24
    5.1   From Runtime Evidence to Evolution Signals . . . . . . . . . . . . . . . . . . . . . . . . . .         25
    5.2   Generating Feedback for Self-Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       27

          5.2.1   Evidence-Based Quality Assessment . . . . . . . . . . . . . . . . . . . . . . . . . . .        27
          5.2.2   From Evaluation Findings to Component Diagnosis . . . . . . . . . . . . . . . . . .            28
    5.3   Case Studies: From Observed Failures to Evolution Feedback . . . . . . . . . . . . . . . .             29

          5.3.1   SQL Tool Diagnosis for Model Self-Evolution . . . . . . . . . . . . . . . . . . . . . .        29
          5.3.2   Skill Refinement for Harness Self-Evolution . . . . . . . . . . . . . . . . . . . . . .        29


6   Production Deployment and Evaluation                                                                         30
    6.1   Production System Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       30
    6.2   Overall Performance: Baseline vs. Evolved System . . . . . . . . . . . . . . . . . . . . . . .         31

    6.3   Continuous Evolution in Production . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       31
    6.4   Production Workload Profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    32
          6.4.1   Query Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   32
          6.4.2   Tool and Complexity Profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    33

    6.5   User Engagement and Retention Comparison . . . . . . . . . . . . . . . . . . . . . . . . . .           34


7   Related Work                                                                                                 34
    7.1   Harness Self-Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   35
    7.2   Model Self-Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   36

    7.3   Agent Evaluation and Diagnosis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       36

8   Discussion: Broader Lessons for Self-Evolving Agents                                                         37


9   Summary and Outlook                                                                                          38


Appendix                                                                                                         46


A Experimental Setup for the Agentic SQL Model                                                                   46
    A.1 Benchmarks and Evaluation Settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         46

    A.2 Post-RL Training Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     47
    A.3 Tool-Use Efficiency on General Agentic SQL . . . . . . . . . . . . . . . . . . . . . . . . . .           48


B Privacy and Data Protection                                                                                    48




                                                         3
1     Introduction
1.1    Conversational Sports Data Analytics

Sports Agent targets factual retrieval and analytical reasoning over heterogeneous sports data. Unlike
LLM-based chatbots that rely primarily on parametric knowledge (Singh et al., 2025), a production-grade
sports agent must select appropriate data sources and specialized tools, retrieve evidence from the
external environment, and ground its responses in the retrieved evidence.
Conversational sports analytics draws on diverse and evolving data sources, including structured
databases, knowledge bases and real-time web search (Xia et al., 2024; Zheman, 2026). Structured
databases support precise queries over schedules, player profiles, game records, and statistics; knowledge
bases and FAQs provide rules, terminology, and historical context; web search delivers the latest news,
injury reports, and roster updates (Hui et al., 2026; Qin et al., 2025). Differences in data structure, update
frequency, and access mechanisms require the system to select appropriate sources and tools for each
request. Simple factual questions may require a single lookup, while statistical analysis demands a precise
understanding of metric definitions and aggregation logic. Questions involving real-time information or
multiple aspects of a topic often require coordinated tool use and evidence synthesis across sources. A
sports agent must therefore support an end-to-end workflow encompassing intent understanding, tool
selection, evidence verification, and response generation based on the retrieved evidence. Conversational
sports analytics is also highly interactive. Users expect accurate, timely, and verifiable responses with low
latency (Martinez et al., 2025). Although multi-step planning, iterative tool invocation, and cross-source
evidence verification can enhance factual reliability, they introduce additional retrieval and inference
overhead. Maintaining factual accuracy while minimizing response latency under evolving data and
database schemas therefore remains a central challenge for production-grade sports agents.
Conversational sports analytics integrates information from multiple sources to support a broad range
of applications, including professional sports analysis, live-event engagement, and sports information
services (Xu et al., 2026b). StatMuse translates natural-language questions into structured sports-statistics
queries, returning textual answers alongside the underlying results (StatMuse). Wimbledon Match Chat
integrates live match data with generative AI to support in-match statistical queries and performance
analysis (IBM, 2025; Baughman et al., 2025). AthleteGPT, deployed at the Paris 2024 Olympic Games, used
retrieval-augmented generation to provide approximately 11,000 athletes with guidance on venues, rules,
and event information (Intel Corporation, 2024). Collectively, these applications illustrate the growing
role of conversational sports analytics as an interface to official databases, live-event data, and domain
knowledge. However, integrating these resources does not, by itself, ensure sustained performance as
data sources, tool interfaces, and model capabilities evolve. Maintaining reliable operation under such
changes remains an open challenge.

1.2    Progressive Degradation of Static Agent Systems

Most existing agent systems follow an “offline development–deployment–manual maintenance” paradigm
(Zhai et al., 2025). During development, the foundation model, prompts, skills, tool descriptions, and
routing policies are configured for a target task distribution and operating environment, with system
performance validated through offline evaluation. The effectiveness of this approach depends on the de-
ployment conditions remaining broadly consistent with those used during development and evaluation.
In sports applications, however, evolving user requirements, data resources, and model capabilities can
progressively widen the gap between static system configurations and operational demands (Gao et al.,
2025; Liu et al., 2026a).
We evaluate the proposed framework in a live sports analytics product, whose deployment context
and system configuration are described in Section 6.1. The initial agent system used a largely static
configuration, maintained through manual diagnosis and periodic refinement. Production observations


                                                      4
indicate that this approach is susceptible to performance degradation as the agent environment evolves.
Three factors are particularly salient.
Query Distribution Shift. User interests shift substantially across the competition calendar. During
the regular season and playoffs, queries primarily concern game results, player and team statistics, and
standings; during the offseason, attention shifts toward trades, the draft, and roster changes. In the
observed deployment, the share of database-oriented queries fell from approximately 63% during the
playoffs to 43% in the offseason. This shift can reduce the effectiveness of planning and tool-routing
policies tuned to the previous query distribution.

Data Source and Schema Drift. The data environment continually evolves as new sources and metrics
are introduced, schemas are revised, and field definitions change. Agents must adapt how they access
and interpret data accordingly. During a six-month production period, three data sources were added
and more than 100 fields were modified. Without timely adaptation, agents relying on fixed schema
descriptions, example queries, and predefined access paths may reference invalid fields, use outdated
query logic, or misinterpret retrieved results.

Model Capability Misalignment. Parametric knowledge is updated more slowly than sports facts and
can diverge from current player status, game statistics, and standings. Upgrading or replacing a model
component can also change instruction following, planning, and tool-use behavior, affecting existing
prompts and skills. Conversely, stronger models may render some harness components redundant.
Model changes therefore require a reassessment of the surrounding harness configuration.

As illustrated in Figure 1, these changes can progressively undermine planning, data access, and execution.
In the observed production system, weekly factual accuracy declined from 88% to 75% over eight weeks.
Manual diagnosis and ad hoc patches offer limited responsiveness and coverage, while accumulating
prompts, rules, and skills can overfit individual cases and increase harness complexity. These limitations
motivate continuous evolution guided by runtime evidence and the Feedback Engine.




Figure 1: Progressive degradation of a static sports agent. The upper panels illustrate query shifts, data
drift, and model-capability misalignment; the lower panel shows declining weekly factual accuracy.


1.3   Research Problem and Scope

These challenges motivate the research topic of this report: How can runtime evidence guide the
continuous evolution of both the model and the agent harness to maintain reliable performance in an
evolving environment?
We investigate three complementary aspects of this problem:


                                                    5
Model Self-Evolution. How can runtime failures and capability gaps inform the construction of high-
quality training data, and how can iterative data refinement and post-training improve model generaliza-
tion and efficiency?

Harness Self-Evolution. How can runtime evidence guide the diagnosis and targeted refinement of
prompts and skills to improve task planning, tool use, and response style as task distributions evolve?

Unified Feedback Engine. How can the analysis of responses and execution trajectories support root-
cause diagnosis and generate actionable feedback to guide both model and harness evolution?

1.4    Contributions

The main contributions of this report are as follows.
A Dual-Loop Self-Evolution Framework. We introduce Sports Agent, which integrates the Sports Agent
Harness, Agentic SQL Model, and Feedback Engine into a unified system. By connecting online task
execution, runtime evidence collection, evaluation and diagnosis, and capability updates, the system
establishes self-evolution loops for reliable conversational sports analytics.
Data-Scaling-Driven Model Self-Evolution. We develop a data evolution pipeline encompassing
question synthesis, trajectory distillation, error attribution, and targeted data generation. Combined
with model fine-tuning and reinforcement learning, this pipeline continuously improves the accuracy,
execution efficiency, and generalization of the Agentic SQL Model for sports data analysis.

Harness Evolution with Dual Audit and Complexity Control. We enable controlled updates to prompts,
skills, and response strategies by translating recurrent production issues into bounded edits. Each edit
undergoes an independent static audit and paired execution replay, followed by joint replay for final
selection. Non-inferiority checks guide harness simplification, while inactive components are deactivated
rather than deleted.
A Unified Feedback Engine for Both Evolution Loops. The engine represents answers, evidence, and
execution trajectories as verifiable objects. Through evidence verification, step-level error attribution, and
expert feedback, it identifies update targets and translates diagnostic findings into actionable signals for
both model and harness evolution. It also provides unified regression evaluation and release control for
candidate versions.
Production Validation. We deploy and evaluate Sports Agent in a live sports analytics product. Relative
to the baseline version, the evolved system improves the factual correctness score by 10.5 points and
increases average response length, a proxy for response richness, by 158.1%, while reducing average
end-to-end latency by 41.3%. Across 30 successive harness-evolution rounds, the aggregate performance
score increases by 10.8 points. These results demonstrate improvements in response quality and execution
efficiency in the evaluated production setting.

Beyond sports analytics, Sports Agent offers practical lessons for building self-evolving agents: accumu-
late evidence from multiple related failures before making persistent updates, identify shared root causes
to generate training examples beyond the original cases, and use executable checks to validate generated
training data. These principles can guide self-evolution in coding agents, enterprise assistants, and other
agent systems. Section 8 discusses the design principles for self-evolving agents and the cross-domain
transferability of our approach.

2     Sports Agent: Dual-Loop Evolution

To address the challenges in Section 1, Sports Agent establishes two coordinated evolution loops for
the Agentic SQL Model and the Sports Agent Harness. A unified Feedback Engine translates runtime
evidence into diagnostic findings and update signals, providing evaluation and release control for


                                                      6
candidate versions. This section formulates the evolution problem in a changing environment and
presents the system architecture, covering online execution and offline evolution workflows.

2.1   Problem Formulation

Let Et denote the operating environment at time t, including the user-query distribution, data resources,
and tool space Tt . The distribution shift, data and schema drift, and model changes discussed in Section 1
can be summarized as Et ̸= Et+1 . Consequently, an agent configuration that is effective in the current
environment may become progressively less suitable as operating conditions change.
Given a user query qt , the current Agentic SQL Model Mt and Sports Agent Harness Ht jointly execute
the online task:


                                    (yt , τt ) = Execute (qt ; Mt , Ht , Et ) ,                         (1)

where yt is the final answer and τt is the execution trajectory, including task planning, model inference,
tool calls, tool results, and response generation. The system organizes the input query, final answer, and
execution trajectory as runtime evidence,


                                               et = (qt , yt , τt ) ,                                   (2)

Only task-relevant information from this representation is used for response quality assessment, failure
attribution, and targeted capability updates. The use of this information follows the data privacy
safeguards described in Appendix B.
Sports Agent optimizes two components: the Agentic SQL Model Mt , which supports sports-domain
semantic understanding, complex SQL reasoning, and structured-data querying; and the Sports Agent
Harness Ht , which governs planning, tool orchestration, prompts, skills, and response generation. The
Feedback Engine converts runtime evidence into targeted evolution signals and guides validation and
release decisions for candidate updates:


                                    ( gtH , gtM ) = FeedbackEngine(et ),
                                                            
                                          Ht+1 = U H Ht ; gtH ,                                         (3)
                                                             
                                         Mt+1 = U M Mt ; gtM .

Here, gtH and gtM denote harness- and model-oriented evolution signals, respectively. The system aims
to improve answer correctness and completeness while reducing end-to-end latency. Each candidate
update undergoes independent evaluation and regression testing to identify potential trade-offs and
guard against regressions in existing capabilities.

2.2   Architecture Overview

The three sources of degradation identified in Section 1 require complementary forms of adaptation.
Query shifts call for changes to planning, tool routing, prompts, and skills; data and schema changes
require updated access strategies and model capabilities; and model upgrades may alter tool-use behavior
or invalidate existing harness components. These challenges cannot be addressed through isolated model
updates or incremental prompt engineering alone. Accordingly, Sports Agent comprises three tightly
connected modules: Harness Self-Evolution, a Unified Feedback Engine, and Model Self-Evolution. As
shown in Figure 2, the architecture organizes the harness and model evolution loops around the shared
Feedback Engine. The harness loop adapts planning and tool orchestration to changes in tasks, tools,
and model behavior, while the model loop addresses persistent capability gaps through targeted data


                                                         7
construction and post-training. Positioned between the two loops, the Feedback Engine analyzes runtime
evidence, diagnoses failures, routes target-specific evolution signals, and validates candidate updates.




Figure 2: Sports Agent dual-loop evolution architecture. Feedback Engine converts runtime evidence
into diagnostic findings and evolution signals that drive updates to the harness and model.


Model Self-Evolution. This loop updates the specialized Agentic SQL Model; the parameters of the
orchestration model responsible for task planning and tool selection are not updated in this work.
Structured databases provide the factual foundation for sports analytics, including schedules, game
records, player statistics, and standings. The Agentic SQL Model provides the core capability for accessing
and analyzing these data, making its accuracy and efficiency essential to overall system performance.
Model-oriented diagnostic signals are compiled into targeted data-construction tasks. Question synthesis,
trajectory distillation, and quality filtering then produce Mt+1 through in-loop supervised fine-tuning,
improving sports semantics, complex SQL reasoning, cross-task generalization, and execution efficiency.
A final reinforcement-learning stage outside the loop (Post-RL) produces Mfinal .

Harness Self-Evolution. This loop optimizes prompts and skills that guide the orchestration model’s
task planning, tool-use policies, safety policies and response style. The Feedback Engine aggregates
recurring failures into evidence-supported repair intents, guiding bounded edits to global rules, skill
content, and activation conditions. Candidate edits undergo independent review, execution replay, and
regression testing before a validated Ht+1 is released.

Unified Feedback Engine. Positioned between the two loops, the Feedback Engine performs the
structured conversion from runtime evidence to system updates. It jointly assesses answers, supporting
evidence, and execution trajectories; diagnoses root causes; routes evolution signals to the relevant
component; and protects each update through regression validation and release gating.
The architecture connects online execution with offline evolution. During online execution, the orchestra-
tion model follows the harness configuration to plan tasks and coordinate tools, invoking the Agentic
SQL Model when structured-data queries or analysis are required. Evidence retrieved from databases,
web search, and knowledge bases is integrated into the final response. Relevant information derived
from agent trajectories supports subsequent evaluation, failure diagnosis, and system evolution.


                                 qt −→ Ht −→ Mt −→ Tt −→ τt −→ yt .                                     (4)

Offline, the Feedback Engine assesses relevant execution evidence, diagnoses failures, routes model- and
harness-oriented signals to their respective loops, and validates candidate versions:


                                                    8
                                                 
                et −→ Feedback Engine −→ gtH , gtM −→ ( Ht+1 , Mt+1 ) −→ Validate .                       (5)

By closing the loop among online execution, automated assessment, and offline updates, Sports Agent
continually recalibrates its capability boundary and maintains a more effective balance among answer
quality, execution efficiency, and system complexity.

3     Model Self-Evolution Loop

Model improvement requires not only more training data but also a training distribution that reflects
observed failures and evolving task requirements. As discussed in Section 1, schema drift can render
learned field references, metric definitions, and query logic outdated, while recurrent failures reveal
capability gaps that data-volume expansion alone may not adequately address. We therefore organize
task execution, failure diagnosis, data generation, and parameter updates into an iterative loop guided
by execution feedback, with each training round targeting diagnosed capability gaps.
The model-evolution loop combines Feedback Engine diagnosis, targeted Data Scaling, and in-loop
supervised fine-tuning (SFT). The Feedback Engine assesses runtime evidence and identifies model-side
deficiencies (Section 5), which guide SQL-to-Question Scaling and Graph-Guided Scaling. Questions
generated by both methods undergo a shared trajectory-distillation and quality-filtering pipeline to
produce training data for SFT. The updated model is then evaluated to inform the next evolution round.
After iterative evolution concludes, a separate reinforcement-learning (RL) stage, termed Post-RL, further
optimizes task performance.
Section 3.1 formulates the Agentic SQL task and its execution trajectory. Section 3.2 describes the evolution
pipeline, the two Data Scaling methods, and in-loop SFT. Section 3.3 presents Post-RL, and Section 3.4
evaluates model quality, execution efficiency, and the contribution of data evolution.

3.1    Agentic SQL Task

Conversational sports data analytics draws on heterogeneous resources, but many user questions require
precise computation over official databases. Answering them requires identifying the relevant entities,
interpreting metric definitions, resolving temporal scope and implicit constraints, and verifying results
against database evidence rather than relying on parametric knowledge. Conventional Text-to-SQL maps
a natural-language question to a single SQL statement for a given schema and is typically evaluated
through exact match or execution accuracy (Li et al., 2023; Qin et al., 2025). In contrast, the Agentic
SQL Model treats SQL as an intermediate action within a multi-step workflow: it explores the schema,
constructs and executes queries, and refines them in response to execution feedback. Evaluation therefore
considers both the execution trajectory and the final task outcome (Huo et al., 2026).
Given a user question, database resources, and an Agentic SQL tool space, the model solves a task
through multi-step tool interaction. Let q and M denote the question and agentic model. The execution
trajectory is
                                  τ = [( a1 , o1 ), ( a2 , o2 ), · · · , ( aK , oK )] .            (6)

In the notation of Section 2.1, τ is the sub-trajectory that a single Agentic SQL call contributes to the
system trajectory τt at run time. Here, K is the number of interaction steps and ( ak , ok ) is the k-th
tool-action–observation pair. The action ak may retrieve schema information, inspect tables or fields,
execute SQL queries, or verify query results, while the observation ok captures the corresponding schema
metadata, execution results, or error messages. The model selects the next action from the question and
trajectory prefix:
                                           ak ∼ π M ( ak | q, τ<k ) ,                                  (7)



                                                     9
where π M is the action policy induced by M and τ<k is the trajectory before step k. Once sufficient
evidence has been collected or a termination condition is met, the system generates the final answer from
the execution trajectory:
                                          y = Synthesize (q, τ ) .                                      (8)
Once invoked, the model autonomously explores the database schema, plans and executes queries, and
uses execution feedback to correct syntax, field references, and query conditions. Relevant execution
evidence, including query results and trajectory-level signals, supports subsequent evaluation, failure
attribution, and data evolution.
The Agentic SQL Model is trained to improve query correctness and cross-database generalization while
reducing interaction turns and end-to-end latency. To balance capability and inference cost, we use
Qwen3.6-35B-A3B, a mixture-of-experts model with few active parameters, as the base model.

3.2     Model Evolution Training

Model evolution requires both broader data coverage and targeted learning from observed failures. We
formalize this process below.
Let D0 be the seed dataset curated from historical queries, and let Σ, K, and L denote the database
schema, sports-domain knowledge, and task-control variables, respectively. The first SQL-to-Question
scaling round generates ∆D0 under predefined controls and combines it with a filtered subset of D0 :


                                              D1 = D0sub ∪ ∆D0 .                                        (9)
Here, D0 is the seed training set, ∆D0 is the generated increment in the first evolution round, and
D1 is the expanded dataset. For each subsequent round t ≥ 1, the Feedback Engine analyzes the
agent execution trajectory, SQL results, judge outputs, and relevant schemas for the current model Mt ,
producing diagnostic findings Ft . Each finding records the root cause, sports concept, semantic intent,
related schema, and error pattern of a failed case. Ft is diagnostic metadata rather than a training sample
or a complete synthesis specification.
The data increment for round t is the union of SQL-to-Question and Graph-Guided Scaling:
                                                                Graph
                                          ∆Dt = ∆DtSQL ∪ ∆Dt            .                              (10)
The combined increment updates the training set and current model:
                             Dt+1 = Dtsub ∪ ∆Dt ,       Mt+1 = SFT( Mt , Dt+1 ).                       (11)
The updated Mt+1 is evaluated by the Feedback Engine in the next round, coupling changes in the data
distribution to changes in model capability.

3.2.1   SQL-to-Question Scaling

We propose a reverse SQL-to-Question synthesis method that uses executable SQL as an intermediate
semantic representation. The pipeline first constructs the query logic and then expresses it as a natural-
language question. This allows query structure, task difficulty, and domain semantics to be explicitly
constrained at the SQL level, while execution verifies answerability. Compared with generating questions
directly from a schema, this approach checks constraints before question generation, helping preserve
constraint completeness and semantic consistency.
For sample i, we define the control vector
                                                                     
                                     zi = ztask
                                           i    , z diff theme tables
                                                    i   , z i , z i     .                              (12)

The components ztask
                   i   and ztables
                             i       jointly constrain SQL structure. The former specifies one of 14 task
categories, including retrieval, filtering, aggregation, ranking, comparison, and trend analysis, together


                                                      10
                                             one evolution round
   M0                      ⋯        Mt                                              Mt+1                   ⋯                MT              Post-RL               Mfinal


                                                                            Data Scaling

                                         SQL-to-Question Scaling                                 Graph-Guided Scaling
                                    Schema          Controls           Ft                                        Ft
                                                                                      Attribution Graph               Subgraph Sampling
    Model Diagnosis                                                                    Concept    Intent
                                    Generated SQL                 Executable                                                                         Supervised
                                                                                                                                                  Fine-Tuning (SFT)
        Mt   Current Model
                                                                                            Root
                                                                                                                 sample
                                                                                                                             Root
                                                                                                                                                      Mt         Dt+1
                               Ft                                                                                                          Dt+1
    Feedback Engine                                                                    Schema Pattern
                                                                                                               Subgraph-Guided Synthesis                   SFT
                                    “How many games per team                          “Which players scored the most points
              Diagnostic            in the 2024-25 season?”                           in the 2024-25 playoffs?”
        Ft    Findings                                                                                                                            Mt+1     Updated Model


                                                          Trajectory Distillation + Quality Filtering

                                                                Dt+1           Training Dataset




Figure 3: Model self-evolution loop. The Feedback Engine produces diagnostic findings Ft for SQL-to-
Question and Graph-Guided Scaling; the resulting data update drives SFT in each round.


with the corresponding SQL operators; the latter specifies whether the query involves a single table
or multiple tables. The component ztheme  i      selects a domain theme, such as players, teams, schedules,
                                             diff
standings, or injuries. The component zi specifies one of four difficulty levels, L1-L4, ranging from
direct factual retrieval to multi-table joins, compound constraints, and multi-stage computation. Together,
these controls guide query synthesis across structural, semantic, and difficulty dimensions.

During initial data construction, F0 = ∅, and synthesis is guided solely by the predefined controls. In
subsequent rounds, the Feedback Engine analyzes execution failures and produces diagnostic findings
Ft (Section 5). These findings, including those concerning errors in join conditions, aggregation granu-
larity, temporal filtering, and window ordering are translated into targeted constraints that guide SQL
generation in round t:


                                                               ξ i ∼ p θs ( ξ | Σi , zi , Ft ) ,                                                                           (13)
where ξ i denotes a candidate SQL statement, pθs the SQL-generation distribution, and Σi the correspond-
ing database schema. The scaling pipeline translates diagnostic findings into generation constraints,
while the Feedback Engine provides the findings rather than generating training examples directly.
Each candidate SQL statement is checked for syntactic validity, schema consistency, and valid multi-table
references, then deduplicated based on its normalized form. Retained statements are converted into
natural-language questions:
                                         q i ∼ p θ q ( q | ξ i , Σ i ).                              (14)
The conversion must preserve all filtering, aggregation, ordering, and cardinality constraints without
exposing table names, field names, or SQL terminology. The resulting questions are expressed naturally
while remaining semantically verifiable against the underlying SQL.

3.2.2        Graph-Guided Scaling

Predefined task categories and difficulty levels do not fully capture the diversity of failures observed
in production. Graph-Guided Scaling organizes diagnostic findings in Ft into a global error-attribution
graph and samples local subgraphs that preserve relevant capability dependencies. These subgraphs
guide question synthesis by linking each target root cause to its semantic, schema, and execution context.



                                                                                 11
Error Attribution Graph Construction. The global graph organizes individual failures into a reusable
network of capability dependencies. For each failure, the Feedback Engine jointly examines the input
query, execution trajectory, SQL results, judge decision, and relevant schema. The resulting diagnostic
findings are aggregated into a heterogeneous graph:
                                             Gt = Aggregate (Ft ) .                                     (15)
The graph contains five node types: Root Cause, Sports Concept, Semantic Intent, Schema, and Error
Pattern. Edges encode supporting-case links, semantic relations, and schema dependencies. Similar root
causes are merged, while supporting cases, attribution confidence, and schema associations are retained
and updated across rounds. This structure consolidates scattered failures into a reusable representation
of recurring capability gaps.

Subgraph Sampling. Sampling operates on complete local capability-dependency structures rather
than arbitrary node sets. Root causes are prioritized by supporting-case counts. For each selected root
cause r, the system constructs candidate subgraphs that retain the associated concepts, semantic intents,
schemas, error patterns, and dependencies, then samples subgraphs for the current synthesis round:
                                                sub
                                               Gr,k ∼ p ( g | r, Gt ) .                                 (16)
The k-th candidate centered on root cause r is represented by
                                       n                                     o
                                 sub         concept intent          pattern
                                Gr,k = r, ck        , ik    , Σ k , ek         .                        (17)
Candidate nodes are ranked by direct graph connections, shared failure cases, and shared tables. While
keeping the target root cause fixed, the sampler varies domain concepts, semantic intents, and table
combinations, producing structurally and semantically diverse subgraphs that target the same capability
gap.

Subgraph-Guided Question Synthesis. Each sampled subgraph specifies structured constraints for
question synthesis, including the target root cause, sports concept, semantic intent, relevant schema,
and error pattern. Guided by these constraints, the generator varies entities, query conditions, difficulty
levels, and linguistic forms to target a specific capability gap while maintaining semantic and structural
diversity.

To reduce memorization and the risk of evaluation leakage, synthesis avoids reusing the original failed
case, SQL statement, or entity combination. Instead, it recombines abstract diagnostic information across
scenarios. Candidate questions are checked for answerability under the relevant schema, field consistency,
constraint completeness, near duplication, and test-set overlap. A teacher model then generates complete
execution trajectories for distillation, and a shared quality gate filters the resulting samples to form the
final data increment.

3.2.3   Agentic Trajectory Distillation and Training

The two scaling strategies described above determine which questions should be included in the current
evolution round. We next apply a shared trajectory-distillation and training pipeline to convert these
questions into Agentic SQL supervision. For each synthesized question qi , Qwen3.8-Max (Qwen Team,
2026b) serves as the teacher model and interacts with the structured database environment. The teacher
explores the schema, constructs and executes SQL, repairs execution errors, and generates an answer
grounded in the returned results. The resulting training sample is


                                                 di = (qi , τi , yi ) ,                                 (18)

where τi records the complete sequence of tool calls, database observations, and intermediate corrections,
and yi is the final evidence-grounded answer. Distilling the execution trajectory, rather than only the final
answer, provides supervision for schema exploration, query planning, tool use, and error recovery.


                                                          12
A shared quality gate filters the distilled trajectories at both the outcome and execution levels. A
retained sample must contain a complete question-tool call–tool result–answer chain, conform to the
tool protocol, execute valid SQL, and support its final answer with database evidence. We discard
trajectories containing syntax or field errors, timeouts, missing tool results, repeated SQL execution,
abnormal interaction lengths, or incomplete answers. Questions are also normalized and deduplicated,
and samples overlapping with the evaluation set are removed. The retained trajectories constitute the
data increment ∆Dt defined above.
SFT then incrementally updates Mt using the mixed training set Dt+1 , following the model-update
process formulated above (Chen et al., 2023; Zeng et al., 2024). The loss is applied only to assistant-
generated tokens:


                                                   ∑      ∑ log p Mt x j | x< j ,
                                                                                 
                                      LSFT = −                                                                    (19)
                                                  d∈Dt+1 j∈A(d)

where A(d) denotes assistant-token positions, including tool calls and final responses. Tool observations
are excluded from the loss because they provide execution context rather than prediction targets (Song
et al., 2024). This objective teaches the model to preserve the interaction protocol while improving the
query and recovery behaviors targeted in the current evolution round.

3.3   Post-RL

Post-RL is performed after the iterative model-evolution loop. Starting from MT , RL directly opti-
mizes final Agentic SQL task outcomes (Ma et al., 2026; Feng et al., 2026) and produces Mfinal . We use
GSPO (Zheng et al., 2025): a group of trajectories is sampled for each prompt, rewards are normalized
within the group to obtain advantages, and a clipped objective is optimized using sequence-level im-
portance ratios. The complete objective and sampling configuration are provided in Appendix A.2; this
section focuses on reward design.

Reward Design. Agentic SQL tasks vary in their degree of verifiability. Some admit a unique executable
reference, whereas others must be evaluated by whether the execution trajectory fulfills the underlying
query intent. No single evaluation oracle is suitable for both settings: an LLM-based judge introduces
unnecessary uncertainty for directly verifiable tasks, while execution-based verification alone cannot
adequately assess valid open-ended analyses. We therefore choose the strongest available oracle for each
task type and align the reward structure with the task structure. Rewards remain sparse terminal scalars
at the trajectory level; training only forwards and normalizes them within each group, without a learned
reward model or step-level shaping. Table 1 summarizes the design.

                          Table 1: Reward design for the two Agentic SQL task types.

   Task Type                Verification Oracle                   Reward Form                       Granularity

   Execution-verifiable     Database executor: result             Stage-weighted execution          Stage
                            equivalence                           equivalence
   Open-ended               LLM judge: three-dimensional          Fraction of successful repeated   Trajectory
   analysis                 assessment                            judgments



Execution-Verifiable Tasks. Correctness can be determined objectively by the database executor, so the
reward is anchored in result equivalence between predicted and reference queries. To reflect composite
tasks, the reward is defined over stages:
                              Cexec
                   Rexec = ∑ ws · 1 [exec(ŷs ) ≡ exec(y∗s )] ,           ws ≥ 0, ∑C
                                                                                   s=1 ws = 1.                    (20)
                               s =1


                                                           13
ŷs and y∗s are the predicted and reference queries for stage s, ws is the stage weight, C is the number of
stages defined by the task, and Cexec is the number of executable stages. A single-stage task reduces to a
binary execution-equivalence test. Multi-stage rewards accumulate in order with weights reflecting stage
importance, distinguishing partial progress while reserving the maximum reward for complete solutions.
Appendix A.2 gives the instantiated weights and normalization rules.

Open-Ended Analysis Tasks. These tasks have no unique reference SQL. Correctness is a trajectory-
level property: a single execution result cannot determine whether all constraints were covered, the
queries were valid, or the exploration converged. An LLM judge therefore evaluates intent coverage,
query validity, and trajectory efficiency. To reduce single-call variance, the reward is the success fraction
over repeated independent judgments:

                                                   1 k
                                                   k i∑
                                        Rjudge =         1[resolvedi ].                                  (21)
                                                      =1

The judgment is based on semantic equivalence and does not penalize immaterial boundary-expression
differences such as > versus ≥. Missing required constraints, adding or removing filters that alter
the result, substituting an approximate metric, or answering only part of the question causes a failure.
Appendix A.2 specifies the number of judgments and judge configuration.

Format Gate. Outcome rewards alone may assign a positive reward to a trajectory whose interaction
format has degraded. Before training, the raw reward is multiplied by a binary gate, Rfinal = Rraw · Gformat .
The gate checks whether the text preceding the first tool call in each round follows the required format.
It is a necessary condition rather than a bonus and is applied only when Rraw > 0, so it can reject a
malformed positive trajectory but cannot turn a zero reward into a positive one.

3.4     Experiments

3.4.1   Experimental Setup

Table 2: Performance comparison on Sports Agentic SQL task. Best and second-best results are shown in
bold and underlined, respectively.

                Model                                         Sports-Normal    Sports-Hard
                Qwen3.8-Max (Qwen Team, 2026b)                     94.5%           72.3%
                GLM-5.2 (Zeng et al., 2026)                        92.5%           60.0%
                DeepSeek-V4-Pro (Xu et al., 2026a)                 89.6%           76.0%
                Qwen3.6-35B-A3B (Qwen Team, 2026a)                 83.5%           45.7%
                Qwen3.6-35B-A3B-Evolve                             96.7%           70.7%
                Qwen3.6-35B-A3B-Evolve + RL                        97.8%           74.0%


We evaluate the model on two task families. Sports Agentic SQL assesses domain-specific capability over
sports databases used in the evaluated application, with Sports-Normal and Sports-Hard subsets covering
routine queries and more complex sports analytical tasks. General Agentic SQL assesses generalization
to external databases and domains using LiveSQLBench (Team, 2024) and BIRD-Interact (Huo et al., 2026).
Appendix A describes the datasets and evaluation settings.
To reflect production latency constraints, we disable explicit thinking mode for all evaluated models and
retain this configuration on the general benchmarks. For Sports Agentic SQL, we report task correctness,
end-to-end latency, and average tool-call rounds. Each test sample is evaluated three times, and the
reported results are averaged across the three runs. For General Agentic SQL, we report task reward and
average tool-call rounds.


                                                      14
3.4.2    Model Performance Evaluation

As shown in Table 2, Qwen3.6-35B-A3B-Evolve outperforms the base model by 13.2% on Sports-Normal
and 25.0% on Sports-Hard, with a larger gain on the more challenging subset. Post-RL yields additional
gains of 1.1 and 3.3 percentage points, respectively.

Table 3: Performance on General Agentic SQL. Best and second-best results are shown in bold and
underlined, respectively.

                                              LiveSQLBench                           BIRD-Interact
 Model                         Reward (Lite) Reward (Full) Reward (Large) Reward (Lite) Reward (Full)
 Qwen3.8-Max                       46.7%         34.3%             32.3%          23.0%         21.9%
 Kimi-K3 (Team et al., 2026)       47.8%         33.8%             32.7%          26.8%         21.9%
 GLM-5.2                           44.8%         30.3%             26.3%          19.7%         15.7%
 Qwen3.6-35B-A3B                   41.5%         29.3%             24.8%          15.2%         13.9%
 Qwen3.6-35B-A3B-Evolve            46.3%         32.8%             32.3%          28.4%         23.4%
 Qwen3.6-35B-A3B-Evolve + RL       47.4%         37.2%             31.9%          54.0%         41.0%


As shown in Table 3, Qwen3.6-35B-A3B-Evolve outperforms the base model across all five General
Agentic SQL metrics, with gains of 4.8, 3.5, and 7.5 percentage points on LiveSQLBench Lite, Full, and
Large, respectively, and 13.2 and 9.5 percentage points on BIRD-Interact Lite and Full. Post-RL further
improves four of the five metrics, with particularly large gains on BIRD-Interact, although performance
on LiveSQLBench Large declines slightly.

3.4.3    Model Efficiency Evaluation

Figure 4 compares end-to-end latency and average tool-call rounds on Sports Agentic SQL. Relative
to Qwen3.6-35B-A3B, the evolved model reduces latency by 52.3% on Sports-Normal and 58.6% on
Sports-Hard, and tool-call rounds by 29.6% and 52.6%, respectively. These results show that accuracy
gains are accompanied by lower latency and fewer tool interactions. Table 11 reports tool-use efficiency
on General Agentic SQL.




                                                           Figure 5: Ablation of data-evolution strategies
Figure 4: Efficiency on Sports Agentic SQL in terms
                                                           on Sports-Normal and Sports-Hard.
of latency and interaction turns.


3.4.4    Ablation Study

Effect of Data Evolution. To demonstrate the effectiveness of data evolution, we hold the base model,
training configuration, and evaluation protocol fixed, and compare models trained on the curated seed
dataset and the evolved dataset. As shown in Figure 5, Data Evolution improves accuracy from 89.4%
to 96.7% on Sports-Normal and from 59.0% to 70.7% on Sports-Hard, yielding gains of 7.3 and 11.7
percentage points, respectively. The larger improvement on Sports-Hard is consistent with the evolved


                                                      15
dataset’s broader coverage of multi-table joins, compound constraints, and long-tail SQL structures
that are less prevalent in the curated seed dataset. These results suggest that data evolution improves
performance on both routine queries and more complex Agentic SQL tasks.




Figure 6: Multidimensional comparison of the curated seed dataset and the evolved dataset. Bar heights
are normalized to the seed dataset, with original values reported above each bar.


Statistics of the Evolved Data. Figure 6 compares the curated seed dataset with the evolved dataset
across several dimensions. The evolved dataset contains approximately 3.5 times as many multi-table
combinations, while its multi-table coverage and mean SQL length are nearly twice as high and its mean
question length is approximately three times greater. These results show that data evolution expands
the coverage of cross-table relationships, compound constraints, and compositional queries beyond the
patterns represented in the seed dataset.

Figure 7 further examines SQL-structure coverage. The evolved dataset substantially increases the
prevalence of joins, subqueries, common table expressions, window functions, and other complex
operators. Several long-tail structures occur four to nine times as frequently as in the seed dataset, while
common aggregation and ordering operations also receive broader coverage. Data evolution therefore
reduces the initial dataset’s bias toward simple and frequent tasks and adapts the training distribution
to evolving schemas and diagnosed capability gaps. Together with the observed improvements in
accuracy, generalization, and execution efficiency, these findings demonstrate that failure diagnosis can
be translated into targeted training data, enabling the model to continually refine its training distribution
rather than relying on a one-time data-construction process.

4   Harness Self-Evolution Loop

Improving Sports Agent requires the harness to adapt as tasks, data, and model capabilities evolve. As
discussed in Section 1, these changes can disrupt skill activation, invalidate tool contracts and domain
guidance, or make existing components redundant as models internalize their functionality. Addressing
these failures requires targeted edits to policies, content, activation conditions, and component structure.
Reliable harness evolution therefore links runtime evidence, failure attribution, bounded edits, and
version validation in an iterative loop, ensuring that persistent changes are supported by evidence and
verified before release.

We develop a harness-evolution framework in which the Feedback Engine serves as the diagnostic entry
point, typed repair intents as the unit of evolution, and independent auditing and execution replay as
the validation mechanisms. The Feedback Engine assesses relevant execution evidence and diagnoses
harness-side capability gaps (Section 5), translating them into structured repair intents. Related intents
accumulate across evolution events and trigger bounded edits only after receiving sufficient support.


                                                     16
Figure 7: SQL-structure coverage of the curated seed dataset and the evolved dataset. The evolved
dataset provides broader coverage of both common operators and long-tail complex structures.


Each candidate edit undergoes an independent audit and execution verification, after which validated
edits are jointly replayed for final selection. Finally, evidence-based consolidation and a non-inferiority
guard control configuration growth and produce the next harness version.

Section 4.1 presents the overall process and unit of evolution. Section 4.2 describes persistent intent aggre-
gation and bounded edit synthesis. Section 4.3 introduces independent auditing, execution verification,
and final selection. Section 4.4 explains evidence-based consolidation and non-inferiority gating.

4.1   Turning Accumulated Evidence into Coordinated Repairs

The Sports Agent harness determines how the agent plans tasks, invokes tools, organizes context, and
produces responses (Guo et al., 2026). It consists of behavioral policies, solution procedures, tool contracts,
reusable capability content (skills), and the activation relationships among them. This section instantiates
the harness update operator U H from Section 2 as an offline evolution loop driven by Feedback Engine
outputs.

Three difficulties separate observed degradation from a reliable repair. First, evidence for a persistent
change is often sparse (Liu et al., 2026b); an individual failure may result from transient execution
variance or a data anomaly, so directly editing the harness risks overfitting. Second, root causes are
heterogeneous (Cemri et al., 2025). A missing global policy, incorrect capability content, failed capability
activation, and an unclear component boundary require different targets and edit operations. Third,
individually useful edits may conflict when combined, and an append-only update strategy steadily
increases redundancy and complexity. Figure 8 presents the resulting loop.
One evolution round is represented as
                                       ready
               ( Ht , Ωt ) → It → Ct           → {∆t,j } → Vt → Htwin → Htcons → ( Ht+1 , Ωt+1 ) .              (22)
               |                {z                     }|     {z    }|          {z            }
                    (i) Intent-Guided Edit Synthesis     (ii) Dual Audit   (iii) Post-Selection Consolidation

Ht is the current harness, Ωt is cross-event evolution memory, and It contains repair intents emitted by
                                                                                                        ready
the Feedback Engine—the concrete form of the harness evolution signal g H introduced in Section 2. Ct
contains intent groups that meet the evidence threshold; ∆t,j is a local edit candidate; Vt is the validated
edit set; Htwin is the version selected after joint replay; and Htcons is the consolidated candidate. Repairs
are decomposed by root-cause mechanism and target component rather than attached to individual
failures. Each edit is audited and verified independently so that gains are attributable and failures remain


                                                          17
                                                                               one evolution round
                H0                        ···               Ht                                                    Ht+1                ···                     HT


                     Intent-Guided                                            Dual-Audit                                               Post-Selection
                     Edit Synthesis                                      Candidate Refinement                                          Consolidation

                                                                        Each edit · same baseline Ht                            Refine the selected harness
                Feedback Engine Diagnosis
                Execution evidence
                → typed intents                                                                                                               Consolidate
                                                                  Independent                     Runtime                                     harness
          Cross-day / cross-batch intents                            Audit                       → AutoEval              Verified
                                                                                                                          edits          Merge redundant
        Day 1    Day 2     Day 3       Group                     Evidence    Scope           Gain    Regression
                                                                                                                                         content
                                                       Δ1                                                                Select
                                                                                                                                         Retire harmful entries

                                                                                                                                             Historical evidence
                                                       Δ2                                                                Harness             guides cleanup


                 Sufficient support
                  → editing candidates                                            Either fails
                                                                                                                                    Replay + guard
                                                                                                                                    Check for performance loss
                Pending intents                                   re-audit
                Keep accumulating evidence                                           Revise the edit
                                                                                                                                                  H t+1
           Policy · content · activation · structure                         Both audits must pass
                                                                                                                              Keep selected version if cleanup fails




Figure 8: Harness self-evolution. Repair intents accumulate across events and produce bounded edit
candidates after reaching a support threshold. Each candidate undergoes independent audit and runtime
verification. Validated edits are jointly replayed to produce Htwin , followed by evidence-based consolida-
tion and a non-inferiority guard for Ht+1 .


isolated. Final selection and consolidation operate on the complete harness to control interactions among
edits.

Evolution Granularity. The unit of evolution is an evolution event; t indexes events. Each event comprises
relevant execution evidence from a predefined observation window, typically organized as a daily batch,
together with the corresponding Feedback Engine assessments. An event can produce at most one update
Ht → Ht+1 . A deterministic split partitions the event sample set into training and held-out subsets:


                                                            Qt = Qtr   te
                                                                  t ∪ Qt ,                       Qtr   te
                                                                                                  t ∩ Qt = ∅.                                                          (23)
Qtr                                                                 te
  t is used for attribution, intent generation, and edit drafting. Qt remains isolated from these steps
and is used only for candidate gains, regression checks, final selection, and non-inferiority gating. An
event may contain multiple epochs, each repeating attribution, editing, and validation from the previous
epoch’s output. Cross-event state—including pending intents, component usage and impact statistics,
and retired entries—is stored in Ωt . This allows infrequent problems to accumulate evidence over
multiple events.

4.2       Intent Aggregation and Edit Synthesis

4.2.1      Persistent Intent Aggregation

A typed repair intent describes the attributed layer of a failure, the proposed edit action, its target,
supporting cases, and rationale.

Layer Attribution. To handle prompts and skills within a common framework, attribution identifies
the harness layer responsible for a failure using the actual system prompt, activated capabilities, and
execution trajectory. A Prompt Gap is a missing cross-task behavioral rule that is absent from the


                                                                                       18
current system prompt and must apply globally. Skill Content denotes a missing or incomplete reusable
capability, including errors in domain knowledge, retrieval procedures, or statistical conventions within
an activated skill. Skill Activation indicates that the required capability exists but was not retrieved for
the request. Skill Harm indicates that an activated capability actively misdirected the solution.
Cases in which an existing rule was not followed, no usable data exist after a reasonable execution, or an
evaluator contradicts the evidence are classified as non-harness defects. They do not produce harness
edits, although they remain in the evolution memory for analysis. Consistent with Section 5, failures to
follow an available rule are better addressed through model training or execution constraints. A case
may carry both prompt- and skill-level attributions; the corresponding intents enter separate aggregation
paths rather than being treated as mutually exclusive.

Aggregation. The system combines intents from different minibatches with pending intents retained in
Ωt . Aggregation is stratified by attribution layer. Skill intents are grouped primarily by edit type and
target component; creation intents, whose target does not yet exist, are grouped by question type. Prompt
intents are clustered by the semantics of the proposed global rule and must be supported by multiple
question types, preventing a specialized deficiency from being promoted into a global policy. Supporting
cases, failed dimensions, proposals, and root-cause statistics are merged into single-layer intent groups
C jintent .

Support is the number of distinct event:case_id values in a group, denoted by supp(C jintent ). This allows
evidence to accumulate across events while preventing duplicate cases from being counted multiple
times. Groups meeting threshold λsupp become ready:
                                        n                                   o
                                ready
                               Ct     = C jintent | supp(C jintent ) ≥ λsupp .                          (24)

Groups with insufficient evidence remain pending; groups whose targets are obsolete or whose waiting
time exceeds a limit are expired. The threshold establishes an explicit boundary between a one-off failure
and a persistent system change.
Before synthesis, ready groups are prioritized by support, failure severity, and diagnostic confidence,
subject to a per-round proposal budget. Preserve clauses extracted from successful cases are attached as
behavioral constraints. This design gives infrequent issues time to accumulate evidence while limiting
the scope of each update round.

4.2.2   Bounded Edit Synthesis

Each ready intent group produces an edit candidate ∆t,j . Prior work has used LLM feedback to revise
textual configurations (Yuksekgonul et al., 2025; Agrawal et al., 2026); our candidates are instead bound
to an attribution layer, preserve constraints, and an edit budget. Each candidate consists of explicitly
scoped actions and is associated with the baseline Ht , target intent, protection constraints, and allowed
edit magnitude. Table 4 defines the edit space.
Each ready group maps to an edit type according to its attribution. Prompt gaps yield Policy candidates
over the system prompt. The three skill-side attributions yield Content, Activation, or Structure candi-
dates. For example, incomplete rules within a correctly retrieved skill require a Content edit, whereas
an existing skill that was not retrieved requires an Activation edit. Structure edits may also be initiated
during consolidation from cross-event evidence of overlap or persistent harm (Section 4.4).
Different attribution layers impose different constraints. A Policy edit must express a durable, cross-task
behavioral principle and cannot introduce entity-specific values, numerical answers, or task templates.
Content and Activation edits are scoped to one task family and cannot move general behavior into a
specialized skill. These boundaries prevent duplicate repairs across prompts and skills and protect global
rules from specialized knowledge. Candidate isolation also reduces experimental confounding.


                                                    19
                                        Table 4: Harness edit space.

 Type         Layer     Attribution                    Primary Target                Typical Operation

 Policy       Prompt    Prompt gap                     Global behavior and tool      Add, rewrite, or narrow a
                                                       contracts                     rule

 Content      Skill     Missing or incomplete capa-    Specialized    knowledge,     Create, extend, or correct
                        bility                         procedures, and examples      content

 Activation   Skill     Capability not activated       Descriptions, triggers, and   Revise retrieval and routing
                                                       task mappings                 conditions

 Structure    Skill     Harmful capability or cross-   Component boundaries, in-     Merge, split, retire, or re-
                        event overlap                  dices, and dependencies       build an index



An edit candidate is only a proposal. During verification, ∆t,j is applied to the fixed baseline Ht in an
isolated environment, producing H
                                e t,j . Sharing the same baseline makes gains from different edits directly
comparable.

4.3     Dual-Audit Candidate Refinement

Each edit candidate undergoes two checks: an independent static audit followed by dynamic execution
verification.

Independent Audit. Following LLM-as-a-Judge practice (Zheng et al., 2023; Gu et al., 2026; Liu et al.,
2023; Kim et al., 2024), an independent model checks whether the proposed edit is supported by evidence,
remains within its attributed scope, and preserves structural, interface, dependency, and protection
constraints. The audit is designed to reject hard-coded examples, unsupported rule expansion, and
internal inconsistency.

Execution Verification. After an edit passes audit, the runtime executes both Ht and H
                                                                                     e t,j . The Feedback
Engine compares paired gains on target cases, regressions on non-target tasks, protected behavior, and
actual capability activation. Only candidates passing both checks enter
                            n                                                     o
                       Vt = ∆t,j Audit(∆t,j ) = pass ∧ Verify( Ht , H
                                                                    e t,j ) = pass .                  (25)

Bounded Revision. If either check fails, the edit may be revised using the returned feedback and
resubmitted under a new revision identifier. Revision terminates after a fixed number of attempts or
when the execution budget is exhausted. Failure reasons and unresolved intents are retained in evolution
memory for future events.

Final Selection. Validated edits are jointly applied to Ht to form a candidate version, which is compared
with the baseline through full replay on Qte
                                           t . score( H ) is the mean Feedback Engine score on the held-out
set. Because metric differences must be interpreted relative to evaluator noise (Miller, 2024), a candidate
is accepted as Htwin only when its gain exceeds the noise threshold. Differences within the threshold are
treated as ties, in which case the round falls back to Ht . Final selection confirms that locally validated
improvements remain beneficial when combined in the complete harness.

4.4     Post-Selection Consolidation

4.4.1   Evidence-Based Consolidation

After editing and final selection, the system controls the duplication and accumulation introduced
by long-term evolution. Consolidation searches the selected version for highly overlapping entries,


                                                       20
components with similar function, and entries with persistent evidence of harm. Components that have
not been used for an extended period are marked dormant rather than immediately removed, protecting
rare but valid capabilities.

Consolidation candidates are identified from Ωt . A merge requires both content similarity and sufficient
related-failure evidence; retirement requires sustained evidence of harm. If no candidate meets these
criteria, consolidation terminates without additional generation or evaluation.
For eligible candidates, a consolidation plan is generated and applied to a copy of Htwin . Guardrails limit
edit magnitude and check that existing constraints and activation information are preserved, producing
Htcons . Following ACE (Zhang et al., 2026b), consolidation does not search for a new optimum; it removes
clear redundancy and persistent harm while preserving behavior as closely as possible.

4.4.2   Non-Inferiority Guard

Because multiple consolidation operations are applied together, their combined effect cannot be inferred
from the evidence for each individual operation. Merging or retiring components may also damage
infrequent but useful behavior. The system therefore replays Htcons on the same held-out set used for final
selection and compares it with Htwin :
                                  score Htcons ≥ score Htwin − ϵNI ,
                                                             
                                                                                                       (26)
where ϵNI ≥ 0 is the maximum acceptable performance loss. By default, it equals the evaluation-noise
threshold used in final selection. Comparing against Htwin , rather than the original Ht , separates the
effect of editing from the effect of consolidation.
Final selection and consolidation use the same noise scale in opposite directions. New or modified
behavior must improve by more than the noise threshold; consolidation primarily reduces redundancy
and is accepted when it is not meaningfully worse. Requiring a significant score gain from consolidation
would reject nearly every cleanup and force the harness to grow monotonically. The non-inferiority
criterion instead treats a smaller configuration as an improvement when its performance is statistically
indistinguishable, while ϵNI bounds the price paid for simplification.

The next version is                
                                    H cons ,   if the non-inferiority guard passes,
                                      t
                          Ht+1 =                                                                        (27)
                                    H win ,    otherwise.
                                      t
Pending intents, failure reasons, and component usage and impact statistics are written back to produce
Ω t +1 .
Algorithm 1 summarizes one complete round. In summary, the Harness Self-Evolution Loop uses
accumulated evidence to decide whether a change is warranted, root-cause attribution to determine
where the change belongs, independent validation and full replay to decide whether it should be retained,
and consolidation under a non-inferiority guard to control long-term complexity. Diagnostic signals from
the Feedback Engine are thereby converted into coordinated and verifiable harness updates.

4.5     Case Study: From Repair Intents to Layer-Specific Updates

We examine two offline evolution events to illustrate how failure evidence leads to edits at different
harness layers. Case A repairs a cross-task evidence-boundary gap through a prompt-level Policy
edit; Case B extends career-statistics retrieval through a skill-level Content edit. Figure 9 connects
representative questions and repair intents to the resulting edits and held-out performance score gains.

4.5.1   Case A: A Cross-Task Evidence-Boundary Contract

Failure Evidence and Repair Intents. The baseline system prompt allowed the agent to answer without
retrieval when it believed it already knew the answer. Three representative failures exposed the resulting


                                                       21
Algorithm 1 One round of harness self-evolution
Require: Current harness Ht , memory Ωt , event split (Qtr               te                                       tr
                                                                    t , Qt ), and repair intents It derived from Qt
Ensure: Next harness Ht+1 and updated memory Ωt+1
 1: Aggregate It with pending intents in Ωt by attribution layer and target (or by task type for creation
    intents)
      ready
 2: Ct      ← {C jintent | supp(C jintent ) ≥ λsupp }; retain other groups as pending or expired
 3: Rank ready groups by support, severity, and confidence; truncate to the proposal budget and attach
    preserve clauses
 4: Vt ← ∅
                         ready
 5: for all C jintent ∈ Ct     do
 6:      Select an edit type from the attribution and synthesize bounded edit ∆t,j
 7:      repeat
 8:         Apply ∆t,j to isolated baseline Ht to obtain H     e t,j
 9:         if Audit(∆t,j ) = pass and Verify( Ht , Ht,j ) = pass then
                                                        e
10:             Vt ← Vt ∪ {∆t,j }; break
11:         end if
12:         Revise ∆t,j from audit or verification feedback
13:     until the revision or execution budget is exhausted
14: end for
15: Jointly replay a version constructed from Vt and select Htwin ; set Htwin = Ht if no gain is established
16: if Ωt contains entries meeting merge or retirement criteria then
17:     Apply consolidation to a copy of Htwin to obtain Htcons
18:     if score( Htcons ) ≥ score( Htwin ) − ϵNI then
19:         Ht+1 ← Htcons
20:     else
21:         Ht+1 ← Htwin
22:     end if
23: else
24:     Ht+1 ← Htwin
25: end if
26: Write pending intents, failure reasons, and usage statistics to Ωt+1



evidence-boundary gap. A comparison of Yang Hansen and Yao Ming added Yao’s statistics beyond
the retrieved evidence. A response about James Harden’s 2026 China visit first stated that no public
information was available, then asserted that he had not traveled with the team. A response about
defensive matchups involving Luka Dončić and DeMar DeRozan named specific defenders without tool
support.

These failures motivated related repair intents: ground factual assertions in current tool evidence, disclose
missing information without adding unverified details, and keep conclusions within the retrieval scope.
Diagnosis grouped the cross-task patterns around one global evidence-boundary contract. Because the
same root cause appeared across question types, the selected target was the system prompt rather than
individual skills.

Bounded Policy Edit. The candidate replaced the permissive retrieval instruction with a coordinated
contract: retrieve before answering factual questions, support verifiable assertions with current tool
results, and state uncertainty when the requested information is not covered. For partially covered
questions, the response should answer the supported portion and disclose the remaining gap. Gap
disclosures were explicitly treated as part of the answer, keeping the evidence requirement consistent
with existing concision rules.


                                                        22
   A Prompt: evidence-boundary contract                                        B Skill: career-statistics coverage

          Bad cases and repair intents                                                 Bad cases and repair intents
   How do Yang Hansen and Yao Ming differ?                                     Curry's career three-point volume and efficiency?
   Failure Adds Yao's statistics beyond the tool evidence.                     Failure Reports regular-season statistics only.
   Intent Ground every factual assertion in retrieved evidence.                Intent Retrieve regular-season and playoff statistics.
   Any news on Harden's 2026 China visit?                                      What is Towns's playoff field-goal percentage?
   Failure Says 'no news,' then claims he did not travel.                      Failure States a value not sufficiently supported.
   Intent Disclose gaps without adding unverified details.                     Intent Retrieve the missing metric or disclose the gap.
   Who usually guards Doncic and DeRozan?                                      How many career points does Curry have?
   Failure Names specific defenders without tool support.                      Failure Career-total retrieval needs refinement.
   Intent Keep conclusions within the retrieved evidence.                      Intent Prefer a career-statistics tool or parameter.



          Group cross-task patterns into one Policy edit                               Merge same-skill intents into one Content edit


          Bounded edit                                                                 Bounded edit
      /system | Working method and evidence boundary                               player-career-basic-stats / SKILL.md
    - Tool use is optional.                                                       Default to regular season if unspecified.
    - Answer directly when you already know.                                      State the statistical scope.
    + Retrieve first for factual questions.                                     + For overall-career requests:
    + Ground each fact in current tool results.                                 + Retrieve regular season and playoffs.
    + If uncovered, say it cannot be confirmed.                                 + If one is missing, disclose that gap.
    + Answer covered parts; disclose other gaps.                                + If the requested metric is absent:
    + Limit claims to this retrieval's scope.                                   + Retrieve again or say it is unconfirmed.
    + Gap disclosures are part of the answer.                                     Keep list limits and source priorities.



          Performance score                                                            Performance score

                                                       +5.79 points                                                                 +9.29 points
  0                        5                      10                           0                          5                    10


                         Prompt edits constrain evidence use.         Skill edits define task-specific retrieval coverage.


Figure 9: From concrete failures to layer-specific repairs. Related repair intents lead to a bounded Policy
or Content edit. In the diff panels, red denotes removed text, green added text, and gray retained context.
Performance score bars show mean gains on the respective held-out evaluation sets. The cases come from
separate experiments; their gains are not a controlled comparison or estimates of an individual rule’s
contribution.


The edit was confined to the relevant system-prompt section and introduced no player-specific facts or
answer templates. Independent audit and validation checked its scope and consistency. For the second
(player-visit) example, the revised policy requires the agent to disclose that the retrieved evidence does
not establish whether the player traveled with the team, rather than infer that he did not. This preserves
the distinction between missing evidence and evidence supporting a negative conclusion.

Held-Out Performance. On the held-out evaluation set, the mean Performance score increased from
65.31 to 71.10, a gain of 5.79 points relative to the historical baseline. The revised prompt was accepted.
This result reflects the overall contract update rather than the isolated contribution of any one clause.

4.5.2     Case B: Task-Specific Career-Statistics Coverage

Failure Evidence and Repair Intents. The skill-only experiment started with a prompt that already
contained Case A’s evidence contract. A question about Stephen Curry’s career three-point volume and
efficiency activated player-career-basic-stats, but the agent retrieved only regular-season statistics.
The returned values were grounded in tool results; the gap was that the evaluation convention for this
overall-career request also required playoff coverage, which the answer neither supplied nor identified
as missing.
The resulting intent called for retrieving both season types and disclosing any missing portion. Two


                                                                         23
related cases supported a broader repair of the same skill: a question about Karl-Anthony Towns’s playoff
field-goal percentage called for retrieving the requested metric or stating that it could not be confirmed,
while a historical question about Curry’s career points called for a more appropriate career-statistics
retrieval route. These intents accumulated across events and were grouped by their shared target skill.
The deficiency concerned task-specific retrieval knowledge, so it was attributed to Skill Content rather
than to the global evidence policy.

Bounded Content Edit. The candidate added two requirements: retrieve both regular-season and
playoff statistics for an explicit overall-career request, and retrieve again or disclose the gap when the
initial result lacks the requested metric. The existing default to regular-season statistics for unspecified
requests, tool-covered list boundaries, and preferred data sources were preserved. Only the target skill
changed; the system prompt remained fixed. The overall-career convention was specific to this task
family and did not redefine the scope of all sports-statistics questions.
Replay of the Curry question showed the corresponding execution change. The baseline query selected
regular-season data only; the revised query selected both regular-season and playoff data and grouped
the results by season type. The answer then reported the two categories separately. This trajectory shows
how a content edit expanded retrieval and answer coverage while preserving the original supported
statistics.

Held-Out Performance. On the relevant held-out evaluation subset, the skill update improved the
mean performance score by 9.29 points and was accepted. This aggregate result covers the target skill’s
update; the query trajectory provides the direct evidence for the season-coverage change.

4.5.3    Layer Responsibilities

The cases share a path from failure evidence through repair intents to bounded edits and validation,
but address different responsibilities. The prompt constrains which factual assertions may appear in an
answer; the skill specifies which data and statistical scope a task requires. Case B occurred with Case
A’s contract already present, showing that grounded assertions alone do not guarantee complete task
coverage. Placing specialized retrieval rules in the prompt would blur this boundary, while repeating
global evidence rules in individual skills would duplicate policy and make its application depend on
skill activation. Effective repair therefore requires routing each diagnosed gap to the layer with the
appropriate editing authority.

5       A Unified Feedback Engine for Self-Evolution

Agent tasks typically involve reasoning, tool use, and information synthesis. Assessing answer correctness
alone is generally insufficient to explain how a failure arose or identify the component that requires
improvement (Zhang et al., 2025b). Actionable feedback for self-evolution therefore requires execution
evidence to be examined in relation to task requirements, so that an observed failure can be linked to a
specific recommendation for improvement.
The Feedback Engine comprises two modules: Assessment and Diagnosis. Assessment evaluates task
performance under a common specification (Zheng et al., 2023). For confirmed factual errors, Diagnosis
investigates the execution evidence to identify the mechanisms and components involved. The resulting
feedback specifies the optimization targets, update unit, diagnostic conclusion, and recommended
improvement.
Section 5.1 formalizes the process from runtime evidence to evolution feedback. Section 5.2 presents the
methods used by Assessment and Diagnosis, and Section 5.3 examines two production cases that inform
recommendations for model training and harness refinement.



                                                    24
5.1   From Runtime Evidence to Evolution Signals

Following Section 2, the Feedback Engine operates on the runtime-evidence representation et = (qt , yt , τt ),
which comprises the input query, final answer, and task-level execution trace. Assessment and Diagnosis
use only the fields relevant to their respective functions. The trace captures observable execution
information, including planning decisions, applicable instructions, tool calls and results, and model
responses. An evaluation specification S defines each metric’s scope, applicability conditions, and
evidence requirements; the associated rubrics describe observable performance at different quality
levels (Liu et al., 2023). All tasks in an evaluation batch use the same specification. Assessment returns


                                    At = Assess(et ; S) = { At,m : m ∈ S}.                                  (28)

The set At contains the assessment results. For each metric m, At,m records the evaluation status, rationale,
evidence references, and score, where available. These results identify unmet quality requirements, but
explaining their causes requires further investigation.
For a confirmed factual error, let ϕi denote the affected claim and ri the factual reference, comprising
verified facts, their scope, and their sources. After establishing this reference, the request is resubmitted in
new sessions to test whether the error recurs and to obtain additional execution evidence. The reference
                                                        ( j)
remains fixed throughout the investigation. Let τt denote the trace available from run j. Diagnosis
produces

                                                                           
                                      diag                             ( j)
                                     Dt,i,j = Diagnose qt , ϕi , ri , τt      .                             (29)

             diag
The result Dt,i,j records the relevant components, error mechanism, expected behavior, and unresolved
                                                                                   diag
questions for claim i in run j. The corresponding results are collected in Dt . Fact verification and
controlled reproduction supplement the initial runtime evidence with reference facts and replay observa-
tions. Only cases requiring further analysis proceed to root-cause diagnosis, as similar factual errors may
arise from different failure mechanisms. The resulting structured case records can be aggregated into
recurring capability gaps and used to guide targeted training-data construction.
Assessment and Diagnosis jointly produce actionable recommendations for system improvement. We
represent each feedback item as follows:


                                             γ = ⟨Z opt , u, d, rec⟩.                                       (30)

The set Z opt specifies the optimization targets, and u identifies the component to be modified, such as a
Prompt or Skill. The diagnostic conclusion d records the error mechanism, supporting evidence, scope,
and remaining uncertainty. The recommendation rec states the capability, rule, or behavior to improve.
For feedback directed at the model, the update unit need not be specified at the level of an internal model
component.
The stage at which an error appears does not, by itself, determine the component to update. An error
in query construction may reflect failure to follow an available rule or a gap in the task guidance. The
former may motivate model training or execution constraints, whereas the latter may require a Skill
revision; both changes may also be warranted. The recommendation must therefore remain grounded in
the diagnostic report, with evidence references and conclusion status retained in d.
For Sports Agent, the optimization targets are the Harness and the Agentic SQL Model. Let Γt denote the
set of evidence-supported feedback items for which an improvement direction can be determined, and
let Z opt (γ) denote the target set of item γ. Using H and M for the harness and model, respectively, we
define the target-specific evolution signals as


                                                        25
                                            gtH = {γ ∈ Γt : H ∈ Z opt (γ)},
                                                                                                                       (31)
                                           gtM = {γ ∈ Γt : M ∈ Z opt (γ)}.

A feedback item may belong to both sets, and either set may be empty. When a diagnosis supports
distinct recommendations for different components, the recommendations can be represented as separate
items sharing the same diagnostic evidence. Conversely, findings that do not yet justify a specific update
remain in the investigation record. The resulting feedback is used by the model and harness update
procedures described in Sections 3 and 4, respectively.
Table 5 illustrates the feedback representation using the leaderboard eligibility case discussed in Sec-
tion 5.3.2.

                 Table 5: Fields and example values of structured improvement feedback.

Feedback field                  Example: leaderboard eligibility

Optimization targets Z opt      {H}: Harness

Update unit u                   Leaderboard Skill

Diagnosis d                     The SQL eligibility criterion used field-goal attempts (FGA) rather than field goals
                                made (FGM). Supplementary inspection of the same request established that the
                                loaded Skill and table documentation omitted the leaderboard’s eligibility
                                requirement

Recommendation rec              Specify the standard eligibility criterion and its source in the leaderboard Skill, retain
                                user-defined conditions, and validate the distinction between makes and attempts and
                                the eligibility boundaries


Producing evidence-based recommendations therefore requires dispersed records to be integrated and
interpreted in relation to the observed execution failure. Figure 10 summarizes how Assessment and
Diagnosis connect evidence analysis to recommendations for improvement.


                 Feedback Engine
                  Assessment                                       Diagnosis
                              Metrics & Rubrics
                                                                         Reference          Reproduced
                  Answer-Only                                              Facts              Traces
   Production
  Interactions                            Rubric
                    ?
                                          Scoring       Factual
                                                        Failures                                            Improvement
   ?                                                                                                        Requirements
                                                                               Trace Inspection
 Query Answer     Trajectory-Based
                             Map          Reduce                                                               Model
                                                                     Hypothesis          Verification
                                          Merge                                                             Self-Evolution
       Trace                                 &
                                                                           Diagnostic Findings
                                       Rubric Scoring
                                                                                                              Harness
                        Local Checks                                                                        Self-Evolution




Figure 10: Assessment applies a shared evaluation specification through direct rubric-based scoring or
trace-based Map–Reduce (Dean & Ghemawat, 2004), with Map performing local verification and Reduce
aggregating evidence and assigning scores. For confirmed factual errors, Diagnosis uses factual references
and reproduced traces to investigate hypotheses and produce findings that inform recommendations for
the model and harness.




                                                           26
5.2     Generating Feedback for Self-Evolution

Section 5.1 defines how evaluation and diagnostic findings are represented as improvement feedback.
Selecting an appropriate update, however, requires both a judgment of task performance and an ex-
planation of the observed failure. Assessment identifies unmet task requirements, while Diagnosis
investigates the mechanisms underlying confirmed factual errors. Their findings jointly support the
choice of optimization target, update unit, and recommended change.

5.2.1   Evidence-Based Quality Assessment

Evaluation metrics require different forms of evidence. Answer relevance can be assessed directly from
the question and response, whereas factual-claim verification and behavioral evaluation require evidence
from the execution trace (Zhuge et al., 2025). Combining evidence retrieval, claim–evidence verification,
and scoring in a single model call can reduce judgment reliability, particularly when the call must process
a long trace and handle several subtasks simultaneously. Assessment therefore selects an execution
path according to the metric specification and separates local verification from final scoring when trace
evidence is required. Table 6 summarizes these paths.
For claim checking, Assessment extracts factual claims Φt = {ϕi } from (qt , yt ) (Min et al., 2023; Ru
et al., 2024) and distinguishes core from secondary claims. Each evidence unit zℓ corresponds to an
identifiable trace record containing its source type, text, and reference. Context checking instead examines
metric-relevant information and behavior without extracting claims. Successful execution under the
selected mode is represented by

                                    
                                    Map(q , y , z , Φ ; m),      claim checking,
                             (ℓ)              t   t   ℓ    t
                           Ot,m =
                                  Map(qt , yt , zℓ ; m),         context checking,                               (32)
                                                   
                                             (ℓ)
                           Ot,m = Collect [Ot,m ]ℓ .

         (ℓ)
Each Ot,m is a validated list of local observations linked to their sources and may contain zero or more
items recording support, contradiction, qualification, or context. The Collect operation aggregates these
lists in evidence-unit order and removes duplicates to obtain Ot,m . Map verifies evidence relationships
under metric m without assigning scores. Tool outputs and instruction snapshots can substantiate claims
within the recorded evidence; the agent’s own statements are retained only as context.

                 Table 6: Evaluation targets, evidence requirements, and execution paths.

Evaluation target            Required evidence                        Execution path

Response quality             Question and answer                      Direct rubric-based scoring

Claim–evidence               Claims in the answer and relevant        Local verification followed by scoring in
relationships                trace evidence                           Reduce

Behavior in context          Information available and actions        Criterion-specific observations followed by
                             taken during execution                   scoring in Reduce


Once the local observations have been collected, the claim-checking path proceeds to Reduce. The
complete claim list is used to consolidate verification states, which in turn constrain rubric-based scoring:


                                      st,m = BuildStates(Φt , Ot,m ),
                                                                       ctx
                                                                                                                  (33)
                                      At,m = Scorem (qt , yt , st,m , Ot,m ).

The sequence st,m records each claim’s content, importance, verification status, and evidence references,


                                                          27
including claims without relevant observations. Contextual observations that are not associated with
                                   ctx . Given these records, Score produces a rubric-based evaluation
a specific claim are retained in Ot,m                              m
subject to the claim-state constraints: the model forms an initial assessment within the permitted score
range, and structurally valid outputs undergo programmatic checks and any necessary corrections to the
score, status, and rationale. Context checking evaluates the collected observations directly against the
rubric, without constructing claim states or applying these constraints. Both paths retain rationales and
evidence references without rereading the full trace. Support within a recorded trace remains distinct
from independent factual verification.

5.2.2   From Evaluation Findings to Component Diagnosis

The same factual error may have different causes, and reproduction alone does not identify the com-
ponents or behaviors responsible. Diagnosis therefore organizes evidence collection and verification
around explicit hypotheses, using the findings to refine explanations and inform recommendations (Zhu
et al., 2025). Once the factual reference ri has been established, the request is repeated in new sessions.
        ( j)
With yt denoting the answer from run j, the recurrence condition and claim–request pairs eligible for
investigation are

                                         h                                       i
                                                   ( j)                  ( j)
                                  Rij = 1 Related(yt , ϕi ) ∧ Conflicts(yt , ri ) ,
                                                                                                               (34)
                               diag                           ( j)
                             It       = {(i, j) : Rij = 1, τt        is available}.

The condition Rij = 1 holds when the new answer contains a claim semantically related to ϕi that still
                                                                                                               diag
conflicts with ri ; identical wording or the same erroneous value is not required. Each pair in It
links a claim to a particular run. Because session conditions may differ from those of the original run,
reproduction is not a deterministic replay. Diagnosis examines the observed inputs, actions, and outputs
and traces upstream within the limits of the available evidence, distinguishing missing or unloaded
capabilities, inadequate task guidance, and failure to follow an available rule.

The verification method depends on the hypothesized mechanism. Instruction checks first establish
whether the relevant rule entered the request context before the action under investigation, then compare
the rule with subsequent behavior. Answer consistency checks compare the affected claims with the
original tool outputs. SQL-related hypotheses can be examined through read-only local comparisons
under the preparation, registration, and verification requirements in Table 7.

                      Table 7: Requirements for read-only local SQL comparisons.

Comparison        Requirement
stage

Preparation       Inspect the original tool output before registering a hypothesis, and inspect the relevant table
                  documentation before executing a query

Registration      Register the predicted values, entities and statistical scope to be held fixed, proposed query
                  modification, and output columns for both computations

Verification      Execute both computations in a single read-only query, compare the registered output columns
                  with the predictions, and record warnings and unexplained discrepancies


The tools enforce these prerequisites so that each comparison is grounded in the original output and
documented data semantics. Predictions for the baseline and modified queries are registered before
execution. Verification then checks whether the baseline reproduces the original erroneous value and
whether the modified query yields the predicted target.

A comparison is accepted as verification evidence only if it passes the applicable checks without warnings.


                                                         28
Otherwise, unexplained discrepancies require revision of the hypothesis or further upstream investigation.
Even a successful comparison provides only local support for the proposed error mechanism; the
programmatic checks do not establish that the query modification isolates a single factor affecting the
result.
Throughout an investigation, the system records the evidence examined, open hypotheses, verification
conclusions, and unexplained discrepancies, and identifies outstanding tasks. Before delivery, it checks
that the conclusions and tests have been recorded and linked to runtime evidence. Insufficient support
requires further investigation or an explicit statement of what remains unresolved. The labels confirmed,
hypothesis, and inconclusive describe evidential support rather than calibrated probabilities.
The distinction between missing guidance and noncompliance also determines the type of recommenda-
tion. If an applicable rule was present in the execution context but was not followed, training or execution
constraints may improve adherence. If the guidance omitted a necessary rule, the appropriate target may
instead be a Prompt or Skill. Defects in implementation, configuration, or knowledge and data depen-
dencies may indicate other changes. Accordingly, the diagnosis d, update unit u, and recommendation
rec must be supported by the same body of evidence.

5.3     Case Studies: From Observed Failures to Evolution Feedback

We present two representative cases with different improvement targets. Assessment first verified factual
accuracy using multiple online sources, after which Diagnosis analyzed confirmed errors across repeated
executions. The figures summarize the case comparisons and distinguish automated findings from
supplementary evidence supporting the recommendations.

5.3.1   SQL Tool Diagnosis for Model Self-Evolution

In a representative evaluation case, the system reported that Kobe Bryant had 920 career regular-season
wins. External verification established the correct count as 836 games in which he appeared and his team
won, while repeated controlled executions continued to return 920.
Trace inspection showed that the query applied the player, regular-season, and win filters but omitted the
appearance condition specified in the pre-query guidance: positive minutes played or a positive value in
at least one core statistic. In the archived comparison, applying this condition reduced the count from 920
to 836; the 84 excluded records fully explained the discrepancy (Figure 11). The final answer matched the
original query result.

The evidence supports a diagnosis of failure to follow an available rule. We therefore recommend con-
structing SQL training examples for the Agentic SQL Model that reinforce application of the appearance
rule, with validation across players and appearance conditions.

5.3.2   Skill Refinement for Harness Self-Evolution

The standard eligibility criterion for the career regular-season field-goal percentage leaderboard is at
least 2,000 field goals made (FGM). The question specified neither statistical scope nor eligibility criteria,
but the response applied a threshold of 2,000 field-goal attempts (FGA), ranking Daniel Gafford first at
approximately 70.2%.

The query correctly computed career FGM divided by FGA; Gafford’s 1,660 makes in 2,364 attempts
yielded 70.22%. The archived comparison retained the statistical scope and ratio calculation but changed
eligibility to FGM≥2000, excluding Gafford and placing DeAndre Jordan first at 67.34% (Figure 12). The
set of eligible players changed; Gafford’s percentage did not.
Diagnosis confirmed the error in the SQL eligibility field. The recommendation to revise the Skill is
additionally supported by inspection of the same request: the guidance loaded before query generation


                                                     29
specified the statistical scope and ratio calculation but omitted the leaderboard’s eligibility requirement.
The proposed revision is to document the standard criterion and its source, preserve user-defined
conditions, and validate the distinction between makes and attempts and the eligibility boundaries.

Across these cases, the Feedback Engine combines quality assessment, component diagnosis, and task-
rule evidence to produce specific recommendations for improvement. The resulting feedback can inform
model learning objectives and the development of reusable Skill specifications.

           An Available Rule Left Unused
           Kobe Bryant · Career Regular-Season Wins


                                                   Local Contrast
                 Loaded Rule
                                                   Original query                                        84 excluded
             Minutes > 0
             OR any core stat > 0                                                                                      920
             Generated Query                       Apply full appearance rule

             Appearance filter                                                                                         836
             omitted




             Diagnosis                                                     Model Training · Proposed

             Available rule not executed                                   Rule following



Figure 11: Archived comparison for Kobe Bryant’s career regular-season wins and the proposed model-
training recommendation.


           Qualification Changes the Leader
           Career Regular Season · Individual Ratios Unchanged


             Generated Query                                               Factual Reference

             FGA ≥ 2000                                                    FGM ≥ 2000

             Leader                                                        Leader

             Daniel Gafford                        70.22%                  DeAndre Jordan                       67.34%
             Gafford eligible · 2364 FGA                                   Gafford excluded · 1660 FGM


                                                            SQL Finding · FGA vs FGM


             Diagnosis           Supplementary inspection                  Harness / Skill · Proposed

             Qualification rule missing                                    Define qualification



Figure 12: Comparison of eligibility criteria for the career field-goal percentage leaderboard and the
proposed Skill refinement.


6     Production Deployment and Evaluation

6.1    Production System Overview

The evaluated system is a conversational sports analytics product powered by specialized models and an
agent system. Its first production version was launched in June 2026, serving users in mainland China.
The product integrates structured databases, knowledge bases, and real-time web sources, enabling users


                                                                      30
to retrieve and analyze sports information without manually navigating disparate data platforms. It
supports knowledge retrieval, statistical analysis, real-time information access, player and team profiling,
pre-game analysis, and contextual multi-turn follow-up. Users can explore historical records, compare
player and team performance, aggregate statistics, track schedules, results, standings, injuries, and
transactions, and discuss potential game outcomes using available evidence. A unified conversational
interface allows users to refine questions, adjust analytical constraints, and continue exploring related
topics across multiple turns.
To address the limitations of static configurations in a changing production environment, we upgraded
the baseline system between June and September 2026 by integrating the Sports Agent framework. The
evolved system combines an improved Agentic SQL Model with an updated Sports Agent Harness,
supported by the Feedback Engine for runtime assessment, failure diagnosis, and update validation.
The upgrade targeted three objectives: improving factual correctness, enhancing response richness and
informativeness, and reducing end-to-end latency. The following subsections evaluate these objectives
through comparisons between the baseline and evolved systems, continuous-evolution experiments,
production traffic analysis, and user engagement and retention statistics.

To protect user privacy, all workload and engagement statistics reported in this section are derived from
aggregated, de-identified product data. The underlying analyses exclude raw user content and persistent
user identifiers. Additional details on data scope and privacy safeguards are provided in Appendix B.

6.2   Overall Performance: Baseline vs. Evolved System

We compare the baseline and evolved systems on a shared evaluation set. The baseline uses a largely
static agent configuration, whereas the evolved system integrates an evolved Agentic SQL Model and
Sports Agent Harness, supported by the Feedback Engine for runtime assessment, error attribution,
and version validation. The evaluation set contains 500 questions: 400 internally curated evaluation
samples and 100 questions generated by an AI agent based on daily trending topics to represent emerging
information needs. It covers factual retrieval, statistical analysis, real-time information, and composite
queries. Response quality is assessed using a multidimensional evaluation framework covering factual
correctness and content richness.

We report three user-facing metrics. Factual Correctness Score is an LLM-as-a-Judge assessment of the
correctness of core factual claims, normalized to a 0-100 scale. Answer Richness uses average response
length as an observable proxy for informational breadth and completeness of the response. Average
Latency measures the end-to-end time from request receipt to response completion. As shown in Figure 13,
the evolved system achieves substantial improvements in response quality and execution efficiency. The
factual correctness score rises from 75.8 to 86.3, a gain of 10.5 points, while average response length
increases from 240.8 to 621.5 characters, suggesting more informative answers. Meanwhile, average
end-to-end latency falls from 26.4 to 15.5 seconds, a reduction of 41.3%. These results indicate that
coordinated model and harness evolution can improve factual correctness and response richness while
reducing latency, rather than trading response efficiency for answer quality.

6.3   Continuous Evolution in Production

To assess sustained improvement in a deployed setting, we evaluated 30 successive harness versions
produced through iterative evolution. Each update builds on the preceding version and uses relevant
execution evidence and Feedback Engine diagnostics to identify capability gaps and refine the prompt
configuration and associated skills. All versions, V1-V30, are evaluated on the same fixed test set under a
consistent evaluation protocol.
The aggregate Performance Score combines general response quality and application-specific criteria,
weighted at 30% and 70%, respectively. General criteria include readability, self-consistency, and relevance;


                                                     31
         Figure 13: Overall performance comparison between the baseline and evolved systems.


application-specific criteria comprise expressiveness, factual correctness, and faithfulness to retrieved
evidence. This fixed-set evaluation tracks improvements driven by newly observed failures while
monitoring regressions in established capabilities.

As shown in Figure 14, the Performance Score increases from 78.2 at V1 to 89.0 at V30, a gain of 10.8 points,
and peaks at 89.5 at V19. Despite fluctuations across individual versions, the fitted trend is positive,
indicating overall improvement across evolution rounds. The final version remains within 0.5 points
of the peak score. However, local declines highlight the non-monotonic nature of harness evolution:
updates targeting one failure category may adversely affect other tasks. Fixed-set regression evaluation
and release gating are therefore essential at each round.




Figure 14: Performance over 30 self-improvement iterations. The aggregate score increases from 78.2 at
V1 to 89.0 at V30 and reaches its maximum of 89.5 at V19.


6.4     Production Workload Profile

6.4.1   Query Distribution

The query distribution varies across seasonal phases in topic composition, concentration, and tool
requirements. Player information consistently accounts for 27.0%–31.4% of queries, while transaction-
related queries rise sharply from 3.4% during the playoffs to 32.1% in the offseason. Together, these


                                                     32
two categories represent 59.1% of offseason queries, reflecting a more concentrated distribution. As the
regular season begins, the combined share of game prediction, schedule, and game-analysis queries
increases from 8.0% to 20.4%, redirecting attention toward ongoing competition and statistical analysis.
These shifts also reshape tool requirements. In-season queries rely more heavily on structured databases,
whereas offseason queries require greater use of news search and knowledge retrieval. Adapting to
production query shifts therefore requires corresponding adjustments to task planning, source selection,
and tool orchestration.




         Figure 15: Query-topic distribution across the playoffs, offseason, and regular season.


6.4.2   Tool and Complexity Profile

Tool use is shaped jointly by the season phase and the deployed system version. During the offseason,
input queries center on trades, drafts, and roster changes: Web Search and Profile RAG achieve coverage
rates of 57.0% and 36.5%, respectively, while Database Query drops to 17.0%, reflecting the dominance
of current news and unstructured knowledge. During the regular season, queries shift back toward
schedules, box scores, and team performance. Consequently, Database Query coverage rises to 40.6%,
nearly matching Web Search at 41.3%.
The regular-season observation period coincided with the deployment of the evolved system, which
improved context management, intermediate-evidence reuse, and task-termination policies, thereby
reducing redundant retrieval during follow-up reasoning. During the playoffs and offseason, 73.3% and
89.1% of requests required at least two tool calls, respectively. After the deployment of the evolved system,
this proportion fell to 33.6%, with single-call requests rising to 46.1% and three-or-more-call requests
dropping to 12.9%. Combined with the gains in answer quality, these results indicate that fewer tool calls
reflect better context utilization and more compact execution paths rather than reduced capability. In
short, the evolved agent system preserves multi-source evidence acquisition while substantially lowering
the interaction cost per task.




                                                     33
Figure 16: Tool usage and execution complexity across season phases. The left panel reports the coverage
of database tool, web search, and profile RAG; the right panel shows the number of tool calls per request.


6.5    User Engagement and Retention Comparison

We compare user engagement, retention, and conversation depth over two 30-day observation periods,
one in July 2026 for the baseline system and the other in October 2026 for the evolved system. We report
five engagement-oriented metrics. Interactions per User measures the average number of user questions
submitted per unique user. Users with at Least Three Sessions captures the proportion of users who
initiate three or more distinct sessions during the observation window. Users Active on at Least Three
Days measures repeated usage across different calendar days. D7 Retention is the proportion of eligible
users who return exactly seven days after their first observed active date. Finally, Sessions with at
Least Three Turns measures the proportion of reconstructed sessions containing three or more user
questions, reflecting conversation depth and sustained follow-up behavior. Note that the absolute values
are withheld to protect user privacy and commercially sensitive usage data.
As shown in Figure 17, with the baseline system normalized to 1.0 for each metric, the evolved system
shows improvements across all five engagement dimensions. Interactions per user reach 1.36× the
baseline. The relative indices for users with at least three sessions and users active on at least three days
increase to 2.26× and 2.27×, respectively. D7 retention reaches 2.39× the baseline, while the share of
sessions with at least three turns increases to 1.50×. These results indicate greater conversation depth
and repeated usage during the evolved system’s observation window. Higher multi-session usage,
cross-day activity, D7 retention, and multi-turn session rates suggest stronger overall user engagement.
However, because the two evaluation windows cover different calendar periods and competition phases,
the observed differences cannot be attributed solely to the version upgrade.

7     Related Work

Sports Agent connects three research directions: harness evolution, model evolution, and agent diagnosis.
This section reviews related work in these areas and discusses how the principles derived from our
production deployment can inform the design of self-evolving agents in other domains, together with
their applicability and limitations.




                                                     34
Figure 17: Relative user engagement, retention, and conversation depth for the evolved system, with the
baseline normalized to 1.0 for each metric.


7.1   Harness Self-Evolution

From Prompt Optimization to Harness Evolution. Early adaptation methods focused on prompt
optimization. Promptbreeder (Fernando et al., 2024) jointly evolves task prompts and their mutation
prompts, while DSPy (Khattab et al., 2024) compiles declarative LM modules against program-level
metrics. GEPA (Agrawal et al., 2026) uses execution trajectories, including reasoning, tool calls, and
outputs, to guide prompt updates. These methods establish prompts and modular inference programs
as explicit optimization targets. Harness-oriented methods broaden the editable space to persistent
context and executable structures. ACE (Zhang et al., 2026b) maintains evolving strategy playbooks,
while AFlow (Zhang et al., 2025a) searches executable workflows composed of LLM-invoking nodes.
Automated Design of Agentic Systems (Hu et al., 2025) generates and archives agent programs through
a meta-agent, and STOP (Zelikman et al., 2024) recursively improves its own scaffolding under an explicit
utility function. More directly, Self-Harness (Zhang et al., 2026a) groups verifier-grounded failures, pro-
poses localized harness revisions, and selects candidates through regression gates. HarnessEvolve (Jiang
et al., 2026) uses validated reference trajectories to guide failure diagnosis, then screens updates through
quality and performance gates. Together, these approaches extend adaptation from individual prompts
to workflow structures and execution logic, with recent methods explicitly coupling failure diagnosis to
validated harness updates (Lin et al., 2026).

Lifelong Learning of LLM Agents. Lifelong agent learning aims to retain and reuse execution ex-
perience across tasks. Reflexion (Shinn et al., 2023) stores verbal feedback in episodic memory, while
Voyager (Wang et al., 2024) accumulates executable skills through environment interaction. ACE (Zhang
et al., 2026b) maintains evolving strategy playbooks, and broader frameworks organize historical interac-
tions into reusable memories and skills (Cai et al., 2025). Living-Harness (Du et al., 2026) further converts
trajectories and evaluator feedback into bounded updates of memory and control rules. These methods
turn feedback into persistent capabilities, but retained artifacts may become outdated or redundant. More
evolution rounds do not guarantee gains, making validation essential (Liu et al., 2026b). Sports Agent
aggregates related failures across dates and batches into typed evolution intents, proposing updates only
when evidence is sufficient. Validation then selects effective candidates, enabling controlled adaptation
while limiting incident-level overfitting.




                                                     35
7.2   Model Self-Evolution

From Self-Training to Autonomous Post-Training. Model self-evolution improves successive check-
points through generated supervision and iterative feedback. Bootstrapped methods such as STaR and
ReSTEM generate, filter, and learn from model outputs (Zelikman et al., 2022; Singh et al., 2023), while
self-play and model-generated judgments support alternative training objectives (Chen et al., 2024; Yuan
et al., 2024). More recent work explores automation of the learning procedure itself: model-development
benchmarks evaluate end-to-end experimentation (Chan et al., 2025; Nathani et al., 2025), and research
agents select data, training methods, and hyperparameters (Yano et al., 2025; Rank et al., 2026). This
progression extends evolution from generating supervision to designing the training process. How-
ever, automated training may amplify model bias, exploit evaluation weaknesses, or introduce data
contamination, making independent verification and data provenance essential.

Data and Trajectory Evolution. Recent work increasingly couples training-data generation with envi-
ronment interaction and learner feedback. Environment-grounded task discovery and execution-verified
self-play create supervision from agent interactions and executable problems (Zhai et al., 2025; Zhao et al.,
2025), while capability-adaptive generators produce tool-use tasks near the solver’s current competence
boundary (Acikgoz et al., 2026). Trajectory-based methods construct and filter teacher demonstrations
or repair failed rollouts for subsequent training (Wu et al., 2025; Yuan et al., 2025). Failure-driven cur-
ricula further use diagnostic feedback to generate targeted tasks during reinforcement learning (Wang
et al., 2026b). These approaches automate supervision, but generated tasks still require verification, and
targeted expansion must avoid overly narrow coverage.
Sports Agent combines executable task synthesis with structured diagnosis of observed failures. SQL-
to-Question Scaling converts verified, schema- and difficulty-controlled SQL into natural-language
questions. Graph-Guided Scaling uses an attribution graph to target diagnosed capability gaps while
varying entities, constraints, and table combinations. Together, these pathways use agent diagnosis to
guide data generation and executable checks to validate the results.

7.3   Agent Evaluation and Diagnosis

From Outcome Scoring to Process-Aware Evaluation. LLM-based evaluators provide a scalable al-
ternative to human review. G-Eval (Liu et al., 2023) evaluates generated text using explicit criteria and
structured reasoning, while MT-Bench and Chatbot Arena (Zheng et al., 2023) examine the reliability and
bias of LLM judges. For factuality, FActScore (Min et al., 2023) decomposes responses into atomic claims
and verifies them against external knowledge. Agent evaluation increasingly extends from final answers
to intermediate processes. AgentBoard (Ma et al., 2024) measures task progress in addition to final
success. Agent-as-a-Judge (Zhuge et al., 2025) and AgentDiagnose (Ou et al., 2025) evaluate intermediate
decisions and capabilities such as planning, observation reading, exploration, and self-verification. These
methods show that outcome scores alone are insufficient for diagnosing tool-using agents; evaluation
must retain the local evidence and trajectory segments that support each judgment.

Root-Cause Attribution in Agent Systems. A detected error does not directly identify the component
that should be updated. An unsupported answer may result from missing model knowledge, an
incomplete Prompt, failed Skill activation, or incorrect tool use. Failure detection and repair localization
are therefore distinct problems. Recent work highlights the difficulty of reliable attribution. MAST (Cemri
et al., 2025) provides a taxonomy of failures in multi-agent systems, while TRAIL (Deshpande et al., 2025)
evaluates failure-category prediction and span-level localization over agent traces. Automated attribution
methods also attempt to identify both the responsible agent and the decisive failure step (Zhang et al.,
2025b). These studies show that failure classification is easier than precise localization, particularly
for long trajectories. Reliable diagnosis therefore requires trace decomposition and evidence-backed
hypothesis testing rather than a single judgment over the complete execution.


                                                     36
                 Table 8: Positioning Sports Agent with respect to related research directions.

Direction            Optimization Object         Key Open Question              Key Mechanisms of Our
                                                                                Approach
Harness              Prompts, skills, context,   Which failures justify updates, Evidence accumulation guides
evolution            tools, and workflows        and how can rule                updates; Validated consolidation
                                                 accumulation be controlled?     controls redundancy.
Model                Training data, model        How can generated              Verified SQL anchors scalable
self-evolution       weights, and training       supervision address            question synthesis;
                     strategies                  deployment gaps while          Attribution-guided synthesis
                                                 preserving validity and        broadens coverage beyond
                                                 coverage?                      observed failures.
Agent evaluation     Quality metrics and         How can observed errors be     Evidence-grounded assessment
and diagnosis        failure attribution         translated into targeted,      checks correctness; failure
                                                 validated updates?             attribution guides targeted
                                                                                updates.



Sports Agent separates quality assessment from root-cause diagnosis. For confirmed errors, the Feedback
Engine replays tasks and inspects context, Prompts, Skills, and tool interactions to test competing
explanations. Diagnoses specify causes, evidence, update targets, and actions, guiding model training,
harness updates, regression testing, and release decisions. Diagnosis thus connects runtime evidence to
controlled system evolution.

8    Discussion: Broader Lessons for Self-Evolving Agents

Positioning Sports Agent. Related research has expanded the scope of agent evolution from prompts to
executable workflows, model training, and failure diagnosis. Recent methods already connect diagnosis
with validated Harness revisions (Zhang et al., 2026a; Jiang et al., 2026) and coordinate Harness adaptation
with model updates (Chen et al., 2026b;a; Mao et al., 2026). Sports Agent builds on these advances by
addressing three linked production questions: which failures justify persistent changes, which capabilities
should be learned rather than patched, and how diagnostic findings become validated updates. Table 8
summarizes this positioning.
The contribution is a controlled workflow linking runtime evidence to persistent system updates, rather
than a standalone optimization algorithm. Evidence support justifies proposals, diagnosis identifies
update targets, validation governs acceptance, and consolidation limits complexity.

Design Principles. Drawing on our system design and production experience, we summarize five
principles for controlled agent evolution beyond the sports domain:

      1. Attribute before updating. Evidence-grounded diagnosis should guide model training, Harness
         revision, or both. Ambiguous attribution requires further verification rather than immediate
         modification.
      2. Avoid updates based on isolated failures. Individual failures may reflect ambiguous requests
         or stochastic generation. Persistent updates should therefore rely on sufficient evidence from
         related cases accumulated over time, rather than isolated incidents.
      3. Generalize mechanisms, not individual failures. Directly synthesizing variants of failed exam-
         ples can cause local overfitting and evaluation leakage. Instead, identify the underlying capability
         gaps and use them to generate diverse training examples that extend beyond the original cases.
      4. Ground supervision in verifiable representations. SQL-to-Question synthesis illustrates a
         broader principle: use executable or machine-checkable representations to validate generated
         tasks and training signals, while retaining semantic checks on questions, trajectories, and answers.


                                                         37
     5. Simplify the Harness as capabilities improve. As the agent improves, review existing rules
        and skills and remove those that are no longer needed. Validate each simplification through
        regression testing and retain the option to restore the previous version.

Cross-Domain Transferability. The proposed principles can extend to agents whose execution traces
are observable, the components requiring updates can be identified, and outcomes can be independently
assessed. Transfer requires adapting the diagnostic categories, evidence sources, verification methods,
and release criteria to the target domain. For coding agents, test results and execution traces can support
failure diagnosis, while repository state identifies the code or configuration to update. Enterprise
assistants require checks that distinguish retrieval failures, outdated knowledge, and unsupported
answers. Multimodal agents additionally need evidence alignment across text, images, and video,
including temporal consistency. These adaptations connect the shared evolution process to each domain’s
failure mechanisms and quality requirements.

9   Summary and Outlook

This work investigated how a production sports agent can sustain reliable conversational data analytics
under continuous changes in user demand, data resources, and model behavior. We presented Sports
Agent, a dual-loop self-evolution framework that connects online execution with offline system improve-
ment through a shared Feedback Engine. The framework organizes runtime queries, responses and
execution trajectories into structured evidence; diagnoses whether an observed failure originates from
the model or the harness; and converts the diagnosis into actionable evolution signals. The model loop
expands training coverage through SQL-to-Question scaling and graph-guided synthesis, then uses
generated trajectories for supervised fine-tuning. A separate Post-RL stage further refines the resulting
model. In parallel, the harness loop applies evidence-supported updates to prompts, skills, tool policies,
and response logic, while dual audits, regression replay, and non-inferiority guards control update risk
and system complexity. Experiments demonstrate that the proposed approach improves both capability
and execution efficiency. On the Sports Agentic SQL generation task, the evolved model improves
accuracy from 83.5% to 97.8% on the Sports-Normal test set and from 45.7% to 74.0% on the Sports-Hard
test set, while substantially reducing latency and tool-call rounds. The gains extend to general Agentic
SQL benchmarks, supporting the transferability of the learned query and tool-use capabilities beyond the
evaluated sports databases. In the deployed product, the evolved system increases the factual correctness
score from 75.8 to 86.3 and average response length by 158.1%, while reducing average end-to-end latency
by 41.3%. Across 30 successive harness-evolution rounds, the aggregate Performance Score rises from
78.2 to 89.0. Together, these results show that higher answer quality does not necessarily require longer
execution paths: targeted model training and more effective orchestration can improve reliability and
efficiency simultaneously.
The results demonstrate that runtime evidence can improve model capabilities and agent orchestration.
However, model and harness updates remain largely separate, harness evolution primarily targets
prompts and skills, and the current workflow connects evidence-based evaluation, diagnosis, and service
updates while still requiring substantial human involvement in code review and production deployment.
These limitations motivate three directions for future work.
Model–Harness Co-Evolution. Building on recent co-evolution frameworks (Chen et al., 2026a; Mao et al.,
2026; Chen et al., 2026b), future work will investigate alternating optimization: execution feedback guides
harness revisions, and quality-filtered trajectories generated under the revised harness support model
training. Joint credit assignment will help determine whether failures require model updates, harness
revisions, or both. Shared quality and efficiency objectives will coordinate these updates, reducing
component mismatch and redundant modifications.
Agent Design and Workflow Evolution. Future work will extend harness evolution beyond prompts


                                                    38
and skills to executable workflows and orchestration code. Modularizing workflow stages and atomic
operations will enable search over agent structures and implementations (Zhang et al., 2025a; Wang et al.,
2026a). Execution evidence can guide changes to workflow topology, control logic, and individual code
blocks. Constrained generation, sandboxed execution, static analysis, and regression testing will support
reliable structural updates.
Full-Lifecycle Agent Self-Evolution. While evidence-based evaluation, failure diagnosis, and service
updates are already automated, code review, deployment, and release verification remain manual. Future
work will close this loop, linking failure discovery to candidate implementation, automated review,
deployment, and post-release validation, with every change tied to a versioned artifact and traceable
evidence of its effects.




                                                   39
References
Emre Can Acikgoz, Cheng Qian, Jonas Hübotter, Heng Ji, Dilek Hakkani-Tür, and Gokhan Tur. Tool-R0:
 Self-evolving LLM agents for tool-learning from zero data. In Findings of the Association for Computational
 Linguistics: EMNLP 2026, pp. 29989–30017. Association for Computational Linguistics, 2026. doi: 10.1
 8653/2026.findings-emnlp.1407. URL https://aclanthology.org/2026.findings-emnlp.1407/.

Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav
  Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, et al. Gepa: Reflective prompt evolution can
  outperform reinforcement learning. In International Conference on Learning Representations, volume 2026,
  pp. 8479–8565, 2026.

Aaron Baughman, Gozde Akay, Eduardo Morales, Rahul Agarwal, and Preetika Srivastava. Match chat:
 Real time generative ai and generative computing for tennis. arXiv preprint arXiv:2509.12592, 2025.

Yuxuan Cai, Yipeng Hao, Jie Zhou, Hang Yan, Zhikai Lei, Rui Zhen, Zhenhua Han, Yutao Yang, Junsong Li,
  Qianjun Pan, et al. Building self-evolving agents via experience-driven lifelong learning: A framework
  and benchmark. arXiv preprint arXiv:2508.19005, 2025. URL https://arxiv.org/abs/2508.19005.

Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A. Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt
 Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, et al. Why do multi-agent LLM
 systems fail? In Advances in Neural Information Processing Systems, volume 38, 2025. URL https:
 //openreview.net/forum?id=fAjbYBmonr.

Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace,
  Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, and Aleksander Madry. MLE-bench: Evaluat-
  ing machine learning agents on machine learning engineering. In The Thirteenth International Conference
  on Learning Representations, 2025. URL https://arxiv.org/abs/2410.07095.

Baian Chen, Chang Shu, Ehsan Shareghi, Nigel Collier, Karthik Narasimhan, and Shunyu Yao. Fireact:
  Toward language agent fine-tuning. arXiv preprint arXiv:2310.05915, 2023.

Guhong Chen, Yingcheng Shi, Yongbin Li, Binhua Li, Xander Xu, Hu Wei, Shiwen Ni, Min Yang, and
 Jieping Ye. Evotrainer: Co-evolving llm policies and training harnesses for autonomous agentic
 reinforcement learning. arXiv preprint arXiv:2606.03108, 2026a.

Zhengyu Chen, Teng Xiao, Huaisheng Zhu, Yige Yuan, Luan Zhang, and Jingang Wang. Co-harness:
  Co-evolving harnesses and model weights for LLM agents. arXiv preprint arXiv:2607.22688, 2026b. URL
  https://arxiv.org/abs/2607.22688.

Zixiang Chen, Yihe Deng, Huizhuo Yuan, Kaixuan Ji, and Quanquan Gu. Self-play fine-tuning converts
  weak language models to strong language models. In Proceedings of the 41st International Conference on
  Machine Learning, volume 235, pp. 6621–6642, 2024. URL https://proceedings.mlr.press/v235/c
  hen24j.html.

Jeffrey Dean and Sanjay Ghemawat. MapReduce: Simplified data processing on large clusters. In 6th
  Symposium on Operating Systems Design and Implementation (OSDI 04). USENIX Association, 2004. URL
   https://www.usenix.org/conference/osdi-04/mapreduce-simplified-data-processing-large
  -clusters.

Darshan Deshpande, Varun Gangal, Hersh Mehta, Jitin Krishnan, Anand Kannappan, and Rebecca Qian.
 TRAIL: Trace reasoning and agentic issue localization, 2025. URL https://arxiv.org/abs/2505.086
 38.

Yuetian Du, Yucheng Wang, He Xu, Jiexu Xu, Shanwen Tan, Bing Zhao, Boyu Yang, Zhijie Xu, Ming
  Kong, Hu Wei, Jie Liu, and Qiang Zhu. Living-harness is an interactive-agent evolver. arXiv preprint
  arXiv:2607.26598, 2026. URL https://arxiv.org/abs/2607.26598.


                                                    40
Jiazhan Feng, Shijue Huang, Xingwei Qu, Ge Zhang, Yujia Qin, Baoquan Zhong, Chengquan Jiang, Jinxin
   Chi, and Wanjun Zhong. Retool: Reinforcement learning for strategic tool use in llms. In International
   Conference on Learning Representations, volume 2026, pp. 37909–37926, 2026.

Chrisantha Fernando, Dylan Sunil Banarse, Henryk Michalewski, Simon Osindero, and Tim Rocktäschel.
  Promptbreeder: Self-referential self-improvement via prompt evolution. In Proceedings of the 41st
  International Conference on Machine Learning, volume 235 of Proceedings of Machine Learning Research, pp.
 13481–13544. PMLR, 2024. URL https://proceedings.mlr.press/v235/fernando24a.html.

Huan-ang Gao et al. A survey of self-evolving agents: What, when, how, and where to evolve on the
 path to artificial super intelligence. arXiv preprint arXiv:2507.21046, 2025.

Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen,
   Shengjie Ma, Honghao Liu, et al. A survey on llm-as-a-judge. The Innovation, 7(6), 2026.

Jianyuan Guo, Zhiwei Hao, Chengcheng Wang, Cheng Fan, Tingzhang Luo, Hongguang Li, Ying Gao,
   Hefei Mei, Jiankun Peng, Rongjian Xu, et al. From question answering to task completion: A survey on
   agent system and harness design. arXiv preprint arXiv:2606.20683, 2026.

Shengran Hu, Cong Lu, and Jeff Clune. Automated design of agentic systems. In International Conference
  on Learning Representations, 2025. URL https://proceedings.iclr.cc/paper_files/paper/2025/h
  ash/36b7acf6f6010652b3f2a433774a66fe-Abstract-Conference.html.

Yulong Hui, Chao Chen, Zhihang Fu, Yihao Liu, Jieping Ye, and Huanchen Zhang. Interact-rag: Reason
  and interact with the corpus, beyond black-box retrieval. In International Conference on Learning
  Representations, volume 2026, pp. 112154–112174, 2026.

Nan Huo, Xiaohan Xu, Jinyang Li, Per Jacobsson, Shipei Lin, Bowen Qin, Binyuan Hui, Xiaolong Li,
 Ge Qu, Shuzheng Si, et al. Bird-interact: Re-imagining text-to-sql evaluation via lens of dynamic
 interactions. In International Conference on Learning Representations, volume 2026, pp. 44285–44333, 2026.

IBM. The all england lawn tennis club and IBM launch new AI features for real-time wimbledon fan
  engagement. IBM Newsroom, June 2025. URL https://newsroom.ibm.com/2025-06-17-the-all-e
  ngland-lawn-tennis-club-and-ibm-launch-new-ai-features-for-real-time-wimbledon-fan
  -engagement. Accessed: Oct. 21, 2026.

Intel Corporation. From athletes to GenAI developers: Intel tackles real-world challenges with AI systems.
  Intel Newsroom, July 2024. URL https://download.intel.com/newsroom/archive/2025/en-us-2
  024-07-18-from-athletes-to-genai-developers-intel-tackles-realworld-challenges-wit
  h-ai-systems.pdf. Accessed: Oct. 21, 2026.

Wen Jiang, Mingmin Chu, Yimeng Tian, Qianxin Zhang, Haofei Yang, Rui Yang, Yang Liu, Tao Lv, and
 Fangming Li. HarnessEvolve: Learning from reference trajectories for reliable agent self-evolution.
 arXiv preprint arXiv:2609.00829, 2026. URL https://arxiv.org/abs/2609.00829.

Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vard-
 hamanan, Saiful Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei
 Zaharia, and Christopher Potts. DSPy: Compiling declarative language model calls into self-
 improving pipelines. In International Conference on Learning Representations, 2024. URL https:
 //proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181
 e0-Paper-Conference.pdf.

Seungone Kim, Jay Shin, Joel Jang, Shayne Longpre, Hwaran Lee, Sangdoo Yun, Ryan Shin, Sungdong
  Kim, James Thorne, Minjoon Seo, et al. Prometheus: Inducing fine-grained evaluation capability in
  language models. In International Conference on Learning Representations, volume 2024, pp. 29927–29962,
  2024.


                                                    41
Jinyang Li, Binyuan Hui, Ge Qu, Jiaxi Yang, Binhua Li, Bowen Li, Bailin Wang, Bowen Qin, Ruiying Geng,
   Nan Huo, et al. Can llm already serve as a database interface? a big bench for large-scale database
   grounded text-to-sqls. Advances in Neural Information Processing Systems, 36:42330–42357, 2023.

Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou, Xuanjing Huang, Hang Yan, Zhenhua
   Han, and Tao Gui. Agentic harness engineering: Observability-driven automatic evolution of coding-
   agent harnesses. arXiv preprint arXiv:2604.25850, 2026. URL https://arxiv.org/abs/2604.25850.

Shuaiqi Liu, Zhengkai Lin, Yuxiang Zhang, Yuanyi Ren, Yue Wu, Yongbin Li, Zheng Wang, Zhihang
  Fu, and Jieping Ye. The path to recursive self-improving agents: Foundation, framework, and future
  directions. 2026a.

Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Ruochen Xu, and Chenguang Zhu. G-Eval: NLG
  evaluation using GPT-4 with better human alignment. In Proceedings of the 2023 Conference on Empirical
  Methods in Natural Language Processing, pp. 2511–2522. Association for Computational Linguistics, 2023.
  doi: 10.18653/v1/2023.emnlp-main.153. URL https://aclanthology.org/2023.emnlp-main.153/.

Yuxuan Liu, Zhaochen Su, Yuhao Zhang, Jiahe Guo, Zhongwei Xie, Huihao Jing, Lingyun Xie, Qing
  Zong, Yauwai Yim, Zhixiong Zhang, et al. Rethinking self-evolving agent skills: Feedback dynamics
  over multiple rounds. arXiv preprint arXiv:2608.02636, 2026b.

Chang Ma, Junlei Zhang, Zhihao Zhu, Cheng Yang, Yujiu Yang, Yaohui Jin, Zhenzhong Lan, Lingpeng
 Kong, and Junxian He. Agentboard: An analytical evaluation board of multi-turn LLM agents. In
 Advances in Neural Information Processing Systems, volume 37, 2024. URL https://proceedings.neur
 ips.cc/paper_files/paper/2024/hash/877b40688e330a0e2a3fc24084208dfa-Abstract-Dataset
 s_and_Benchmarks_Track.html.

Peixian Ma, Xialie Zhuang, Chengjin Xu, Xuhui Jiang, Ran Chen, and Jian Guo. Sql-r1: Training natural
  language to sql reasoning model by reinforcement learning. Advances in Neural Information Processing
  Systems, 38:174505–174537, 2026.

Qinghua Mao, Wanying Qu, Dadi Guo, Leitao Yuan, Qingyu Liu, Yu Li, Guanxu Chen, Yanwei Fu, Xi Lin,
  Xia Hu, et al. Safeevolve: Harness-policy co-evolution from agent experience for safety alignment.
  arXiv preprint arXiv:2609.02786, 2026.

S. Martinez, N. Ahuja, F. Bardoliya, S. R. Chowdhury, C. Bryan, and V. Gupta. SPORTSQL: An interactive
   system for real-time sports reasoning and visualization. In Proceedings of The 14th International Joint
   Conference on Natural Language Processing and The 4th Conference of the Asia-Pacific Chapter of the Association
   for Computational Linguistics: System Demonstrations, pp. 94–101, December 2025.

Evan Miller. Adding error bars to evals: A statistical approach to language model evaluations. arXiv
  preprint arXiv:2411.00640, 2024.

Sewon Min, Kalpesh Krishna, Xinxi Lyu, Mike Lewis, Wen-tau Yih, Pang Wei Koh, Mohit Iyyer, Luke
  Zettlemoyer, and Hannaneh Hajishirzi. FActScore: Fine-grained atomic evaluation of factual precision
  in long-form text generation. In Proceedings of the 2023 Conference on Empirical Methods in Natural
  Language Processing, pp. 12076–12100. Association for Computational Linguistics, 2023. doi: 10.18653/v
  1/2023.emnlp-main.741. URL https://aclanthology.org/2023.emnlp-main.741/.

Deepak Nathani, Lovish Madaan, Nicholas Roberts, Nikolay Bashlykov, Ajay Menon, Vincent Moens,
 Mikhail Plekhanov, Amar Budhiraja, Despoina Magka, Vladislav Vorotilov, et al. MLGym: A new
 framework and benchmark for advancing AI research agents. In Conference on Language Modeling, 2025.
 URL https://arxiv.org/abs/2502.14499.




                                                       42
Tianyue Ou, Wanyao Guo, Apurva Gandhi, Graham Neubig, and Xiang Yue. Agentdiagnose: An open
  toolkit for diagnosing LLM agent trajectories. In Proceedings of the 2025 Conference on Empirical Methods
  in Natural Language Processing: System Demonstrations, pp. 207–215, 2025. doi: 10.18653/v1/2025.emnlp
  -demos.15. URL https://aclanthology.org/2025.emnlp-demos.15/.

Yang Qin, Chao Chen, Zhihang Fu, Ze Chen, Dezhong Peng, Peng Hu, and Jieping Ye. Route: Robust
  multitask tuning and collaboration for text-to-sql. In International Conference on Learning Representations,
  volume 2025, pp. 12425–12448, 2025.

Qwen Team. Qwen3.6-35B-A3B: Agentic coding power, now open to all, April 2026a. URL https:
 //qwen.ai/blog?id=qwen3.6-35b-a3b.

Qwen Team. Qwen3.8-Max: A new bar for coding and cowork, August 2026b. URL https://qwen.ai/
 blog?id=qwen3.8.

Ben Rank, Hardik Bhatnagar, Ameya Prabhu, Shira Eisenberg, Karina Nguyen, Matthias Bethge, and
  Maksym Andriushchenko. PostTrainBench: Can LLM agents automate LLM post-training? arXiv
  preprint arXiv:2603.08640, 2026. URL https://arxiv.org/abs/2603.08640.

Dongyu Ru, Lin Qiu, Xiangkun Hu, Tianhang Zhang, Peng Shi, Shuaichen Chang, Cheng Jiayang,
 Cunxiang Wang, Shichao Sun, Huanyu Li, Zizhao Zhang, Binjie Wang, Jiarong Jiang, Tong He, Zhiguo
 Wang, Pengfei Liu, Yue Zhang, and Zheng Zhang. RAGChecker: A fine-grained framework for
 diagnosing retrieval-augmented generation. In Advances in Neural Information Processing Systems,
 volume 37, 2024. doi: 10.52202/079017-0692. URL https://proceedings.neurips.cc/paper_files
 /paper/2024/hash/27245589131d17368cccdfa990cbf16e-Abstract.html.

Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion:
 Language agents with verbal reinforcement learning. In Advances in Neural Information Processing
 Systems, volume 36, 2023. doi: 10.52202/075280-0377. URL https://proceedings.neurips.cc/paper
 _files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html.

Aaditya Singh et al. Openai GPT-5 system card. arXiv preprint arXiv:2601.03267, 2025.

Avi Singh, John D. Co-Reyes, Rishabh Agarwal, Ankesh Anand, Piyush Patil, Xavier Garcia, Peter J.
  Liu, James Harrison, Jaehoon Lee, Kelvin Xu, et al. Beyond human data: Scaling self-training for
 problem-solving with language models. arXiv preprint arXiv:2312.06585, 2023. URL https://arxiv.or
  g/abs/2312.06585.

Yifan Song, Weimin Xiong, Xiutian Zhao, Dawei Zhu, Wenhao Wu, Ke Wang, Cheng Li, Wei Peng, and
  Sujian Li. Agentbank: Towards generalized llm agents via fine-tuning on 50000+ interaction trajectories.
  In Findings of the Association for Computational Linguistics: EMNLP 2024, pp. 2124–2141, 2024.

StatMuse. Asking questions. StatMuse MCP and API Documentation. URL https://developer.statmu
  se.com/docs/asking-questions/. Accessed: Oct. 21, 2026.

BIRD Team. Livesqlbench: A dynamic and contamination-free benchmark for evaluating llms on real-
  world text-to-sql tasks. https://github.com/bird-bench/livesqlbench, 2024. Accessed: 2025-05-22.

Kimi Team, Tongtong Bai, Yifan Bai, Yiping Bao, Jianfeng Cai, Xinyuan Cai, Peizhou Cao, Yuxuan Cao,
  Ziwei Chai, Y Charles, et al. Kimi k3: Open frontier intelligence. arXiv preprint arXiv:2607.24653, 2026.

Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima
 Anandkumar. Voyager: An open-ended embodied agent with large language models. Transactions on
 Machine Learning Research, 2024. URL https://openreview.net/forum?id=ehfRiF0R3a.




                                                     43
Ruhan Wang, Yucheng Shi, Zongxia Li, Zhongzhi Li, Yue Yu, Junyao Yang, Kishan Panaganti, Haitao Mi,
  Dongruo Zhou, et al. Harness handbook: Making evolving agent harnesses readable, navigable, and
  editable. arXiv preprint arXiv:2607.13285, 2026a.

Ziyi Wang, Yuxuan Lu, Yimeng Zhang, Qun Liu, Chen Luo, Jiri Gesi, Hanqing Lu, Yisi Sang, Manling
  Li, Jing Huang, and Dakuo Wang. SENTINEL: Failure-driven reinforcement learning for training
  tool-using language model agents. arXiv preprint arXiv:2606.12908, 2026b. URL https://arxiv.org/
  abs/2606.12908.

Jialong Wu, Baixuan Li, Runnan Fang, Wenbiao Yin, Liwen Zhang, Zhenglin Wang, Zhengwei Tao,
   Ding-Chu Zhang, Zekun Xi, Robert Tang, Yong Jiang, Pengjun Xie, Fei Huang, and Jingren Zhou.
   WebDancer: Towards autonomous information seeking agency. In Advances in Neural Information
   Processing Systems, volume 38, 2025. URL https://openreview.net/forum?id=quJdphBcdP.

Haotian Xia, Zhengbang Yang, Yun Zhao, Yuqing Wang, Jingxi Li, Rhys Tracy, Zhuangdi Zhu, Yuan-fang
 Wang, Hanjie Chen, and Weining Shen. Language and multimodal models in sports: A survey of
 datasets and applications. arXiv preprint arXiv:2406.12252, 2024.

Anyi Xu, Bangcai Lin, Bing Xue, Bingxuan Wang, Bingzheng Xu, Bochao Wu, Bowei Zhang, Chaofan
 Lin, Chen Dong, Chenchen Ling, et al. Deepseek-v4: Towards highly efficient million-token context
 intelligence. arXiv preprint arXiv:2606.19348, 2026a.

Yichen Xu, Jianzhe Ma, Chuhan Wang, Zhonghao Cao, Liangyu Chen, Wenxuan Wang, and Qin Jin. A
  survey of large models in sports. In Findings of the Association for Computational Linguistics: ACL 2026,
  pp. 37154–37189, 2026b.

Taro Yano, Yoichi Ishibashi, and Masafumi Oyamada. LaMDAgent: An autonomous framework for
  post-training pipeline optimization via LLM agents. In Proceedings of the 2025 Conference on Empirical
  Methods in Natural Language Processing, pp. 30078–30095, 2025. doi: 10.18653/v1/2025.emnlp-main.1529.
  URL https://aclanthology.org/2025.emnlp-main.1529/.

Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan,
  Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale.
  Advances in Neural Information Processing Systems, 38:113222–113244, 2026.

Siyu Yuan, Zehui Chen, Zhiheng Xi, Junjie Ye, Zhengyin Du, and Jiecao Chen. Agent-R: Training
  language model agents to reflect via iterative self-training. arXiv preprint arXiv:2501.11425, 2025. URL
  https://arxiv.org/abs/2501.11425.

Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Xian Li, Sainbayar Sukhbaatar, Jing Xu, and
 Jason Weston. Self-rewarding language models. arXiv preprint arXiv:2401.10020, 2024. URL https:
 //arxiv.org/abs/2401.10020.

Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Pan Lu, Zhi Huang, Carlos Guestrin, and
 James Zou. Optimizing generative ai by backpropagating language model feedback. Nature, 639(8055):
 609–616, 2025.

Eric Zelikman, Yuhuai Wu, Jesse Mu, and Noah D. Goodman. STaR: Bootstrapping reasoning with
  reasoning. In Advances in Neural Information Processing Systems, volume 35, 2022. doi: 10.52202/06843
  1-1126. URL https://proceedings.neurips.cc/paper_files/paper/2022/hash/639a9a172c044fb
  b64175b5fad42e9a5-Abstract-Conference.html.

Eric Zelikman, Eliana Lorch, Lester Mackey, and Adam Kalai. Self-taught optimizer (STOP): Recursively
  self-improving code generation. In Conference on Language Modeling, 2024. URL https://openreview
  .net/forum?id=46Zgqo4QIU.


                                                    44
Aohan Zeng, Mingdao Liu, Rui Lu, Bowen Wang, Xiao Liu, Yuxiao Dong, and Jie Tang. Agenttuning:
 Enabling generalized agent abilities for llms. In Findings of the Association for Computational Linguistics:
 ACL 2024, pp. 3053–3077, 2024.

Aohan Zeng, Xin Lv, Zhenyu Hou, Zhengxiao Du, Qinkai Zheng, Bin Chen, Da Yin, Chendi Ge,
 Chenghua Huang, Chengxing Xie, et al. Glm-5: from vibe coding to agentic engineering. arXiv
 preprint arXiv:2602.15763, 2026.

Yunpeng Zhai, Shuchang Tao, Cheng Chen, Anni Zou, Ziqian Chen, Qingxu Fu, Shinji Mai, Li Yu, Jiaji
  Deng, Zouying Cao, et al. Agentevolver: Towards efficient self-evolving agent system. arXiv preprint
  arXiv:2511.10395, 2025.

Hangfan Zhang, Shao Zhang, Kangcong Li, Chen Zhang, Yang Chen, Yiqun Zhang, Lei Bai, and Shuyue
 Hu. Self-Harness: Harnesses that improve themselves. arXiv preprint arXiv:2606.09498, 2026a. URL
 https://arxiv.org/abs/2606.09498.

Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xionghui Chen, Jiaqi Chen, Mingchen Zhuge, Xin
   Cheng, Sirui Hong, Jinlin Wang, et al. Aflow: Automating agentic workflow generation. In International
   Conference on Learning Representations, volume 2025, pp. 34040–34077, 2025a.

Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru,
  Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, et al. Agentic context engineering: Evolving contexts
  for self-improving language models. In International Conference on Learning Representations, volume
  2026, pp. 86069–86100, 2026b.

Shaokun Zhang, Ming Yin, Jieyu Zhang, Jiale Liu, Zhiguang Han, Jingyang Zhang, Beibin Li, Chi Wang,
  Huazheng Wang, Yiran Chen, and Qingyun Wu. Which agent causes task failures and when? On
  automated failure attribution of LLM multi-agent systems. In Proceedings of the 42nd International
  Conference on Machine Learning, volume 267 of Proceedings of Machine Learning Research, pp. 76583–76599.
  PMLR, 2025b. URL https://proceedings.mlr.press/v267/zhang25cq.html.

Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Yang Yue, Matthieu Lin, Shenzhi Wang,
 Qingyun Wu, Zilong Zheng, and Gao Huang. Absolute Zero: Reinforced self-play reasoning with zero
 data. In Advances in Neural Information Processing Systems, volume 38, 2025. URL https://openreview
 .net/forum?id=neZSGqhxDa.

Rami Zheman. From generation to specification: Fast natural language sports q&a across llms. 2026.

Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu,
  Rui Men, An Yang, Jingren Zhou, and Junyang Lin. Group sequence policy optimization. arXiv preprint
  arXiv:2507.18071, 2025.

Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
  Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. Judging
  LLM-as-a-judge with MT-Bench and chatbot arena. In Advances in Neural Information Processing Systems,
  volume 36, 2023. URL https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1
  287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html.

Kunlun Zhu, Zijia Liu, Bingxuan Li, Muxin Tian, Yingxuan Yang, Jiaxun Zhang, Pengrui Han, Qipeng
 Xie, Fuyang Cui, Weijia Zhang, Xiaoteng Ma, Xiaodong Yu, Gowtham Ramesh, Jialian Wu, Zicheng
 Liu, Pan Lu, James Zou, and Jiaxuan You. Where llm agents fail and how they can learn from failures,
 2025. URL https://arxiv.org/abs/2509.25370v1.

Mingchen Zhuge, Changsheng Zhao, Dylan R. Ashley, Wenyi Wang, Dmitrii Khizbullin, Yunyang Xiong,
 Zechun Liu, Ernie Chang, Raghuraman Krishnamoorthi, Yuandong Tian, et al. Agent-as-a-judge:
 Evaluate agents with agents. In Proceedings of the 42nd International Conference on Machine Learning,
 volume 267, pp. 80569–80611, 2025. URL https://proceedings.mlr.press/v267/zhuge25a.html.


                                                     45
Appendix

A     Experimental Setup for the Agentic SQL Model

A.1    Benchmarks and Evaluation Settings

Sports Agentic SQL. We construct a domain-specific benchmark for production sports question answer-
ing and analysis, comprising Sports-Normal and Sports-Hard. Sports-Normal contains 200 questions
derived from real-world requirements, covering player and team information, schedules and results,
basic statistics, and conditional filtering. It evaluates routine query capabilities and execution efficiency.
Sports-Hard contains 100 challenging query tasks involving multi-table joins, compound constraints,
cross-season comparisons, multi-stage aggregation, and complex game-context analysis. All questions
are manually reviewed for domain relevance and answerability using the available databases. Together,
the two subsets assess performance on routine queries and complex, long-tail analytical tasks.

LiveSQLBench. LiveSQLBench evaluates agentic text-to-SQL on real databases, covering both SELECT
and management/CRUD tasks. We evaluate all three released splits with the official LiveSQLBench-
Agent ADK harness.0 The agent receives only the query and a 30-tool-call budget; it retrieves schema and
external knowledge through tools, can execute SELECT/WITH/EXPLAIN queries to inspect intermediate
results, and submits exactly once. We report the official reward: 1 if the submitted SQL passes all test
cases and 0 otherwise (i.e., the task success rate).

BIRD-Interact. BIRD-Interact evaluates interactive text-to-SQL under ambiguity, where the agent must
clarify with a user simulator and explore the database. We evaluate both splits in a-Interact mode with the
official BIRD-Interact-ADK harness.1 The agent has nine actions with bird-coin costs and a stress-mode
interaction budget; Qwen3.8-Flash is used as the user simulator. We report the normalized reward (NR),
denoted Reward in Table 3; in a-Interact, NR is 1.0 when both sub-tasks pass, 0.7 when only the first
sub-task passes, and 0 otherwise.
For both public benchmarks, our evaluation follows the official ADK implementations: the agent scaffold,
prompts, and budget are identical to the official code, and the only difference is the evaluated model
endpoint (and the BIRD-Interact user simulator). All runs use temperature 0.0 and a single run per task.
Tool-use efficiency is measured by the mean number of tool-call rounds per task.

                       Table 9: Evaluation data used in Agentic SQL experiments.

                                     Benchmark                     Size
                                     Sports Agentic SQL
                                     Sports-Normal                 200
                                     Sports-Hard                   100
                                     General Agentic SQL
                                     LiveSQLBench-Base-Lite        270
                                     LiveSQLBench-Base-Full        600
                                     LiveSQLBench-Large            480
                                     BIRD-Interact-Lite            300
                                     BIRD-Interact-Full            600


    0 https://github.com/bird-bench/livesqlbench/tree/main/LiveSQLBench-Agent
    1 https://github.com/bird-bench/BIRD-Interact/tree/main/BIRD-Interact-ADK




                                                     46
A.2    Post-RL Training Details

Table 10 summarizes the instantiated rewards. The complete definitions and implementation details
follow.

                        Table 10: Instantiated reward values for the two task types.

 Task Type                 Scoring Rule                                                                   Raw Reward

 Execution-verifiable      Predicted and reference queries have equivalent results; staged tasks          0, 0.7, 1
                           accumulate stage rewards
 Open-ended analysis       Repeated LLM-judge decisions                                                   0, 1/3, 2/3, 1



Objective. Post-RL adopts GSPO (Zheng et al., 2025). For each prompt, the system samples a group
of trajectories and normalizes rewards within the group to obtain advantage Ai . The sequence-level
importance ratio, computed only over model-generated tokens and excluding tool observations, is

                                                  πθ (τi | x ) 1/|τi |
                                                                
                                    si ( θ ) =                         .                        (35)
                                                 πθold (τi | x )
Training maximizes
                                    "                                                       #
                                   1 G
                                   G i∑
                        J (θ ) = E       min (si (θ ) Ai , clip (si (θ ), 1 − ϵ, 1 + ϵ) Ai ) ,                        (36)
                                      =1

where G is the group size, |τi | is the number of model-generated tokens in the trajectory, and ϵ is the
clipping coefficient.

Execution-Verifiable Tasks. Single- and multi-stage tasks use a common stage-weighted execution-
equivalence reward:
                                                               
                      C                                        1,
                                                               
                                                                    C = 1,
                           exec
                 Rexec = ∑ ws · 1 [exec(ŷs ) ≡ exec(y∗s )] ,           ws =       0.7,   C = 2, s = 1,               (37)
                           s =1
                                                                               
                                                                               
                                                                                   0.3,   C = 2, s = 2.
                                                                               

Rexec is the execution-equivalence reward, s is the stage index, ws is its weight, C ∈ {1, 2} is the number
of stages defined by the task, and Cexec ∈ {1, . . . , C } is the number of executable stages. ŷs and y∗s are the
predicted and reference queries. The maximum reward is
                                                 
                                                 1,
                                                 
                                                            C = 1,
                                    max Rexec =        0.7,      C = 2, Cexec = 1,                                    (38)
                                                   
                                                   
                                                       1,        C = 2, Cexec = 2.
                                                   

A single-stage task receives binary execution-equivalence credit. For a two-stage task, the first successful
stage contributes 0.7 and the second contributes 0.3. If the task has no executable second stage, the
maximum is 0.7. Stages are evaluated in order, and a later stage contributes only after the preceding stage
succeeds.
Before comparison, queries are normalized by removing comments and selected non-semantic operators
such as DISTINCT and ROUND. Results are compared as sets unless the task explicitly requires ordering.
Empty results receive zero. Each trajectory may submit only once; SQL errors, missing submissions,
empty or inequivalent results, and failed execution all receive zero without partial credit. Retries within a
stage are not penalized. When the interaction budget is exhausted, the server permits one final submission
and terminates in the next round, preventing repeated free submissions.



                                                            47
Open-Ended Analysis Tasks. These tasks have no unique reference SQL and are scored by an LLM
judge. Each trajectory is judged independently k = 3 times, and its reward is the resolved fraction:

                                                   1 k
                                                   k i∑
                                        Rjudge =         1[resolvedi ].                                 (39)
                                                      =1

We use Qwen3.7-Max as the judge and provide the input query together with the temporally ordered
SQL–observation pairs. The judge assigns structured 0–5 ratings for intent coverage, query validity,
and trajectory efficiency and returns a resolved decision. Missing key constraints, adding or removing
filters that change the result, substituting an approximate metric, answering only part of the question, or
entering a loop yields false. Boundary-expression differences such as > versus ≥ do not. The continuous
resolved_rate is used directly; repeated evaluations at the same temperature reduce service and parsing
variance rather than forming a majority vote. A trajectory is sent to the judge only after at least one tool
call and a valid completion action. Judge failures or unparseable outputs receive zero, and the judge
evaluates the query trajectory rather than the final natural-language response.

Sampling Strategy. Rollout uses dynamic sampling (Yu et al., 2026): prompt groups with near-zero
reward variance—all correct or all incorrect—are discarded and resampled, ensuring that every group
used for gradient updates has non-zero advantage. The procedure is implemented during rollout
assembly without changing the main training loop.

A.3    Tool-Use Efficiency on General Agentic SQL

For General Agentic SQL, efficiency is reported as the mean number of tool-call rounds; latency is not
used.

                      Table 11: Average tool-call rounds on General Agentic SQL.

                                                    Average Tool-Call Rounds
                          Model                 LiveSQLBench         BIRD-Interact
                          Qwen3.6-35B-A3B              15.8               20.8
                          Qwen3.8-Max                  14.4               17.6
                          Ours                          9.4               11.3


Our model averages 9.4 tool-call rounds on LiveSQLBench and 11.3 on BIRD-Interact, reductions of
34.7% and 35.8% relative to Qwen3.8-Max. The evolved model therefore solves tasks on both general
benchmarks with substantially fewer interactions.

B     Privacy and Data Protection

The analyses presented in this report use only de-identified, task-level records required for system
evaluation, including input queries, model responses, and task-relevant agent execution trajectories.
These records are processed without user labels, persistent identifiers, or account-level metadata. No
direct user identifiers - such as names, phone numbers, email addresses, IP addresses, or account
identifiers, or profile and preference attributes are collected in this study. Workload and engagement
statistics are reported only in aggregate, and no attempt is made to identify, profile, or link records to
individual users. Access to the analysis data is strictly limited to system evaluation and improvement.




                                                      48
