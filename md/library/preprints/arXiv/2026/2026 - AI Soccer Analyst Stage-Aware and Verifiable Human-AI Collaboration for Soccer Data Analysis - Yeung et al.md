<!-- source: library/preprints/arXiv/2026/2026 - AI Soccer Analyst - Stage-Aware and Verifiable Human-AI Collaboration for Soccer Data Analysis - Yeung and Fujii.pdf -->
<!-- arXiv:2609.11224 · CC BY-NC-SA 4.0 · first submitted 2026-09-10 · retrieved 2026-10-21 -->

# AI Soccer Analyst: Stage-Aware and Verifiable Human-AI Collaboration for Soccer Data Analysis

**Calvin Yeung, Keisuke Fujii**

arXiv:[2609.11224](https://arxiv.org/abs/2609.11224) · [PDF](https://arxiv.org/pdf/2609.11224)

## Triage (N/P/R = 6/5/5, composite 16/30)

Mixed-initiative LLM analyst with six revisable stages on public Wyscout 2017; 16-participant study completed 33/48 tasks and participants rated verifiability favourably. Relevant to LLM-driven sports-data tooling (sdv-docs MCP).

## Full text (extracted from the arXiv PDF)

                                                 AI Soccer Analyst: Stage-Aware and Verifiable Human–AI
                                                          Collaboration for Soccer Data Analysis
                                                                     Calvin Yeung                                                           Keisuke Fujii
                                                                Nagoya University                                                         Nagoya University
                                                               Nagoya, Aichi, Japan                                                      Nagoya, Aichi, Japan
                                                     yeung.chikwong@g.sp.m.is.nagoya-u.ac.jp                                            fujii@i.nagoya-u.ac.jp
arXiv:2609.11224v1 [cs.HC] 10 Sep 2026

                                         Figure 1: AI Soccer Analyst supports stage-aware human–AI collaboration in soccer data analysis. Domain experts contribute
                                         context and judgment, while AI provides scalable processing and reporting through an iterative guidance-and-review loop
                                         (top). The interface exposes two key control points (bottom): confirming the analytical problem and plan before execution, and
                                         inspecting linked evidence and relevant code to support claim validation and refinement.
                                         Abstract                                                                     correction. Interaction records showed domain knowledge emerg-
                                         Sports data analysts translate domain questions into insights by             ing through clarification, planning, and refinement. These findings
                                         combining computation with sport-specific domain expertise. Large            position stage-aware human–AI collaboration as a practical ap-
                                         language models ease programming, but prompt-to-report work-                 proach for producing inspectable, revisable, and verifiable analyses
                                         flows may obscure decisions and evidence. We present AI Soccer               while retaining domain-expert involvement in consequential deci-
                                         Analyst, a mixed-initiative system with revisable stages: Data Un-           sions.
                                         derstanding, Problem Definition, Structured Planning, Execution,
                                         Evidence-Grounded Reporting, and Interaction and Refinement.                 Keywords
                                         A formative study with five analysts first informed design goals             sports analytics, soccer, human–AI collaboration, large language
                                         for automation, verifiability, human control, and accessibility. Sub-        models, analytical provenance, verifiability, mixed-initiative sys-
                                         sequently, a task-based evaluation with 16 participants combined             tems
                                         system logs, retained artifacts, ratings, and open responses; 33 of 48
                                         tasks met the operational completion criteria. Exploratory tests sup-
                                         ported favorable participant perceptions of completed-task output
                                                                                                                      1   Introduction
                                         quality, task achievement, reliability, and verifiability after Holm         Data increasingly informs decisions in professional practice, but
                                                                                                                      recorded data does not answer practical questions by itself. Ana-
                                                                                                                      lysts must translate domain questions into operational definitions,
                                                                                                                  1
                                                                                                                                      Yeung and Fujii

determine what the available data can support, implement appropri-           question was interpreted, revise definitions and plans before as-
ate computations, examine intermediate results, and communicate              sumptions propagate, and trace reported claims back to execution
evidence in a form that decision makers can use. Data analysis               evidence. Revisions are directed to the responsible part of the analy-
is therefore an iterative combination of computational work and              sis so that affected outputs can be updated consistently. The central
situated domain judgment rather than a direct transformation from            design principle is therefore to combine computational automa-
data to conclusions [22].                                                    tion with meaningful opportunities for domain experts to shape
    This challenge is particularly visible in competitive sport, where       and verify the analysis. Figure 1 illustrates two key control points:
analytical results must connect recorded performance data to con-            confirming analytical intent before execution and inspecting the
textual and tactical decisions. Coaching staff interpret and com-            connection between a report claim and its supporting evidence
municate data while remaining responsible for its practical con-             afterward.
sequences [5], and analytical work unfolds across interdependent                The formative findings informed and refined the design goals
activities rather than isolated calculations [28]. Soccer analytics          concerning efficiency, verifiability, and human analytical control. A
supports a broad range of tasks, including creating summary statis-          subsequent evaluation with 16 participants found that 33 of 48 ana-
tics, assessing player decisions, and identifying team-level tactical        lytical tasks met the operational completion criteria. In exploratory
patterns [45, 46, 49]. At the team level, comparing how teams attack         tests, all four completed-task ratings remained above the neutral
requires analysts to decide where a possession begins and ends,              midpoint after Holm correction [19]; seven of eight overall-system
identify recurring sequences of actions, account for the positions of        ratings met the unadjusted threshold, but only two remained sig-
teammates and opponents, and choose measures that support a fair             nificant after Holm correction. More importantly, the interaction
comparison between teams. These decisions also depend on what                records showed that domain knowledge was not provided only
a particular data provider records and how its schema represents             in the initial request; it emerged as participants examined plans
match events.                                                                and refined results. Operationally incomplete tasks were concen-
    Large language models (LLMs) offer a promising way to re-                trated around understanding what the dataset could support, while
duce the computational burden of this work by translating natural-           open responses emphasized the need for sustained interaction and
language questions into plans, code, and reports. However, an an-            stronger verification. Together, these findings show how a struc-
swer that sounds convincing may not show how the system in-                  tured and revisable workflow can support useful human–AI analysis
terpreted the question, whether the dataset contains the required            while identifying dataset understanding and active validation as
information, or how it translated domain concepts into calcula-              priorities for future systems.
tions. An LLM may assume that an unavailable event is recorded, or              This paper makes the following contributions:
produce a plausible tactical interpretation from an incomplete cal-
culation. Prior research similarly shows that users of LLM-assisted              (1) A formative study of soccer analysts’ current practices and
data analysis can struggle to communicate sufficient context and                     expectations that identifies requirements for efficient au-
verify generated results [9, 14]. Supporting soccer analysts therefore               tomation, domain control, verifiability, accessibility, and
requires more than converting a prompt directly into a report.                       practical communication.
    Human–AI collaboration provides a basis for dividing this work               (2) AI Soccer Analyst, an implemented workflow for collabora-
between the analyst and the system. Automated support is well                        tion between analysts and AI that externalizes key decisions
suited to repetitive data inspection, code generation, execution,                    and artifacts, requests domain input when needed, routes
and artifact management, whereas analysts are better positioned to                   revisions to the responsible stage, and connects reported
define soccer concepts, select meaningful comparisons, and judge                     claims to execution evidence.
tactical relevance [17, 20, 35]. Yet existing sports-oriented AI sys-            (3) A mixed-method evaluation across analytical tasks of differ-
tems have primarily focused on coaching, engagement, or person-                      ent complexity, providing empirical findings on perceived
alized feedback, while general analytical assistants rarely account                  usefulness, operational incompletion, the points at which
for provider-specific soccer data and domain definitions. Existing                   analysts introduce domain knowledge, and the interaction
provenance and verification approaches make analytical histories                     and verification support required for continued use.
more visible [15, 33], but they do not fully address where analyst
input should enter an LLM-generated workflow or how a revision               2 Related Work
should propagate through its dependent outputs.
    This paper presents AI Soccer Analyst, a system that supports            2.1 Sports Analytics in Practice
human–AI collaboration in soccer event-data analysis. Its input              Data analysis involves both computation and interpretation [22].
is a structured soccer dataset paired with a natural-language an-            This is especially important in sport, where the usefulness of a result
alytical question, and its output is an evidence-grounded report             depends on the setting in which it is produced. Studies of collegiate
accompanied by inspectable intermediate artifacts. Automated re-             coaching staff show that data use is closely tied to responsibility for
view checks computational consistency across these artifacts, while          performance and athlete welfare [5]. Athletes also decide how to use
responsibility for judging domain validity remains with the analyst.         performance data based on their goals, relationships with coaches,
Rather than treating the LLM as a one-step report generator, the             and well-being [4]. Research on esports coaching likewise shows
system makes key analytical decisions and their resulting artifacts          that analysis is part of wider coaching and communication practices
visible throughout the workflow. Analysts can inspect how their              [28]. Sports analytics is therefore situated work: a metric gains value
                                                                             only when people can relate it to their goals and decisions.
                                                                         2
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

   SportsHCI research also shows that feedback is more useful                           domain knowledge needed to interpret soccer-specific concepts
when it reflects expert knowledge. Some systems express coaching                        correctly. This gap calls for a soccer-specific workflow that keeps
principles directly, while others connect measured performance to                       the link between the user’s intent and the computation visible.
the practice context [7, 18, 40]. Conversational coaching agents use
a similar idea by adapting support to the user and their data [13, 21].                 2.3     Mixed-Initiative Analytical Workflows
Accuracy alone, however, does not make a system useful. Research
                                                                                        Mixed-initiative interaction is a collaborative approach in which
on automated ball–strike judgments found that stakeholders evalu-
                                                                                        the user and the AI system can each initiate actions, with control
ated the system not only by its accuracy but also by how it changed
                                                                                        shifting between them as the task evolves [20]. This distribution of
their roles and decision authority [27]. Although automated match
                                                                                        control means that the user’s responsibility also depends on where
decisions differ from analytical assistance, this finding highlights
                                                                                        automation is applied [32]. Human-centered AI therefore aims
the need for sports AI to preserve clear opportunities for expert
                                                                                        to combine automation with meaningful human control [17, 35].
review.
                                                                                        Users need to understand what the system is doing and be able to
   This need for expert review is especially important in soccer
                                                                                        correct important decisions [1]. In data analysis, the right balance
analysis, where analysts may interpret the same soccer concept
                                                                                        may change during a single task because the AI system provides
in different ways. For example, one analyst may define an “attack-
                                                                                        computational capabilities, while the analyst contributes domain
ing play” as any move toward the opponent’s goal, while another
                                                                                        expertise.
may count only moves that create a scoring chance. These inter-
                                                                                           Making the AI system’s analytical steps visible can help maintain
pretations produce different measures and may lead to different
                                                                                        this balance. AI Chains and PromptChainer allow users to inspect
conclusions. Structured datasets such as the public Wyscout dataset
                                                                                        and change intermediate outputs [42, 43]. A study of AI-assisted
provide detailed records, but the data alone cannot determine which
                                                                                        data analysis also found that visible assumptions and task steps
interpretation is appropriate [31]. Soccer research has developed
                                                                                        made the process easier to guide and check [23]. These systems
advanced methods for representing and analyzing match activity
                                                                                        provide more than a sequence of smaller tasks. They give the user
[45, 47, 48]. Yet these methods offer limited support for a key part
                                                                                        a shared view of the work and show how an early choice affects
of the analyst’s work: translating a soccer question into an analysis
                                                                                        the final result.
whose assumptions, methods, and conclusions can be clearly un-
                                                                                           However, each request for user input takes time and attention.
derstood and evaluated. Our study addresses this gap by keeping
                                                                                        Research on multi-step agents shows that confirmation is useful
expert interpretation visible throughout the analytical process.
                                                                                        when it helps users find errors early, but poorly timed checks can in-
                                                                                        terrupt the task [50]. AI Soccer Analyst therefore uses stage-aware
2.2     LLM-Assisted Data Analysis                                                      intervention: the user confirms the system’s understanding and
                                                                                        analytical plan at explicit checkpoints; outside these checkpoints,
LLMs are increasingly used as conversational interfaces for compu-
                                                                                        the system requests input only when an unresolved decision can
tational analysis, translating users’ natural-language questions into
                                                                                        materially change the analysis. Routine work otherwise contin-
analytical steps. Although this can make analysis more accessible,
                                                                                        ues automatically. Our study examines whether this stage-aware
users must still communicate their intent clearly and determine
                                                                                        approach provides control without requiring constant oversight.
whether the resulting answer is valid. One study found that partic-
ipants using generative AI for data analysis struggled to provide
sufficient context and verify the results [9]. Consequently, even                       2.4     Analytical Verifiability and Provenance
when the interaction appears smooth, the system may perform an                          An explanation may help a user understand a result, but it does
analysis that does not match the user’s intended question.                              not prove that the result is correct. Human-centered XAI therefore
   This risk begins during planning. Gu et al. separate the decision                    argues that explanations should be designed for the people and
about what an analysis should do from the later task of implement-                      practices that use them [10]. Bansal et al. found that explanations
ing that decision [14]. They found that useful planning support                         can increase acceptance without improving human–AI team per-
depends on the current state of the analyst’s work. This means that                     formance [2]. The goal should not be to maximize trust, but to help
correct code is not enough; the code must also answer the right                         users judge when the system deserves trust [29]. Asking users to
question. Domain experts therefore need a chance to shape the                           stop and reconsider AI advice can reduce overreliance, although it
analysis before it runs.                                                                requires extra effort [6].
   Recent HCI research shows that effective LLM-assisted analysis                          Generative AI makes this judgment harder because an incorrect
depends on preserving user understanding, agency, and opportuni-                        answer can still sound convincing [36]. In data analysis, users often
ties for verification [16, 24, 34, 42, 43]. Users can judge and redirect                need to reconstruct the system’s work before they can check the
an analysis more effectively when they can inspect its evolving                         result. Gu et al. found that analysts used several views of an AI-
rationale and outputs rather than only the final result [37, 39, 44].                   generated analysis to understand what the system had done [15].
Collectively, these findings suggest that user involvement should                       Verification therefore requires access to the analysis process, not
extend throughout the analytical process [1, 6, 33].                                    only an explanation of the final answer.
   Existing sports-focused AI agents tailor coaching and engage-                           Analytical provenance addresses this need by recording the his-
ment to individual users and situational contexts [13, 21, 25]. How-                    tory of an analysis [33]. In an LLM-assisted workflow, this history
ever, they offer limited support for data analysis. By contrast, general-               must show how human decisions relate to automated work. We
purpose analysis tools support data analysis but often lack the                         call this process verifiability: users should be able to follow how
                                                                                    3
                                                                                                                                      Yeung and Fujii

an analytical decision becomes reported evidence and revise the              verifiability, and trust were specified a priori as theory-driven sen-
process when the connection is wrong.                                        sitizing concepts and formed the initial deductive categories. Open-
   Prior research shows that sports analysis depends on its practical        ended survey and follow-up responses were segmented into mean-
context [4, 5, 28]. It also shows that experts need meaningful con-          ingful units, each of which could receive multiple codes. A second
trol over AI-assisted work [1, 17, 20, 23]. Other studies explain how        pass formed and consolidated inductive codes for content not cap-
users can inspect an analysis after it has been produced [15, 33].           tured by the initial categories. Accordingly, the formative findings
These concerns have rarely been brought together. Our study exam-            informed and refined the design goals rather than independently
ines whether a stage-aware soccer-analysis workflow can support              establishing them. The analysis was exploratory and conducted by
human control and verification while still providing the efficiency          a single coder. The full codebook and coding results are reported
expected from LLM assistance.                                                in Appendix B.

                                                                             3.2    Thematic Findings
3     Formative Study                                                        The analysis yielded five themes concerning where AI assistance
                                                                             may fit within soccer-analysis practice and the conditions necessary
The formative study examined current soccer-analysis practices,              for its responsible use. These themes address workflow efficiency,
workflow difficulties, and participants’ expectations and concerns           verifiability and trust, boundaries of automation, practical commu-
regarding AI assistance in soccer analysis. The thematic findings            nication, and secure and accessible use.
synthesize related deductive and inductive codes rather than corre-
sponding one-to-one with individual codes. The complete survey                  Efficiency concerns spanned the analytical workflow. The specific
and follow-up interview instruments are provided in Appendix A;              bottlenecks varied by work setting. Participants described sub-
detailed quantitative results and the qualitative codebook are pro-          stantial effort in data preparation, report production, and result
vided in Appendix B.                                                         verification. E2 described how manual data collection constrained
                                                                             both time and analytical scope: “Aggregating data such as phases
                                                                             of play and event-location coordinates took more than a day and
                                                                             a half. Because the work was slow, the team asked me to limit
3.1    Method                                                                data collection to attacking play only.” This account also identi-
The formative study employed a survey with selective semi-structured         fied broader data-access and infrastructure constraints. Although
follow-up interviews. In total, 7 eligible soccer analysts working in        these constraints provide important context, they largely fall out-
collegiate or professional contexts were contacted; 5 agreed to par-         side what an analysis-support system could address. E5 described a
ticipate and completed the survey, and 2 of those 5 also completed           highly automated workflow that still required substantial human
follow-up interviews. The interviews were conducted selectively              effort for interpretation and verification. Together, these accounts
when participants’ open-ended responses required further clarifi-            highlighted opportunities for AI assistance to reduce effort in data
cation or elaboration. The 5 survey participants were assigned the           preparation and subsequent stages of the analytical workflow once
pseudonymous identifiers E1–E5 according to the chronological                source data became available.
order of their responses; their characteristics are summarized in
Table 4 in Appendix B. The study protocol was approved by the                   Verifiability supports calibrated trust. Respondents described veri-
institutional ethics review board and conducted in accordance with           fication practices combining process inspection, source-level check-
institutional guidelines for research involving human participants.          ing, and domain validation. E2 reported that current data limita-
All participants provided written informed consent before taking             tions prevented meaningful validity checking and characterized the
part.                                                                        available checking as qualitative rather than objective. Trust was
   The protocol was guided by the initial assumption that AI assis-          associated with interpretability, alignment with soccer knowledge,
tance in soccer analysis should address efficiency, verifiability, and       and communication of uncertainty. Together, these responses sug-
appropriately calibrated trust. The pre-interview survey therefore           gest that participants considered access to the underlying data and
served two purposes. First, it examined how participants under-              analytical process necessary for judging whether an output could
stood and prioritized these anticipated requirements. Second, it             be trusted; an explanation alone was insufficient.
established a structured overview of their current practices, includ-           Automation boundaries reflected human analytical responsibility.
ing existing workflows, recurring difficulties, validation practices,        Respondents distinguished routine, time-consuming work from
and uses of manual, automated, and AI-assisted methods. For the              consequential analytical decisions that they expected to remain
2 interviewees, the follow-up questions clarified their survey re-           under human control. E5 warned that automation could undermine
sponses and probed the reasons and practical context behind them.            expertise: “The ability to think could be taken away, verification
The qualitative survey responses from all 5 participants and the             could consume time, and junior members could lose opportunities
follow-up interview data from 2 participants were analyzed together          to gain experience.” Together, these responses framed acceptable
as a single qualitative corpus.                                              automation as support for human judgment without eroding op-
   Given the small formative sample, closed-ended responses were             portunities to develop expertise.
summarized descriptively to contextualize the qualitative findings
rather than treated as inferential evidence. The qualitative analy-            Practical communication shaped expectations for analytical out-
sis used a combined deductive–inductive approach [3]. Efficiency,            puts. Respondents emphasized that outputs must fit downstream
                                                                         4
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

decision and communication needs. E1 identified manual report                           5       System Overview
creation and repeated adjustment of graph design and slide layout                       Building on the design goals presented in Section 4, AI Soccer
as a source of difficulty. E5 noted that output volume could exceed                     Analyst is a web application that enables users to create, inspect,
an audience’s ability to absorb it. Together, these accounts asso-                      and refine soccer data analyses through natural language. Its web
ciated useful reporting with prioritization, fit with existing staff                    interface supports question submission, artifact inspection, and
workflows, and opportunities for focused clarification or revision.                     feedback, while the backend preserves job and interaction state
   Security and accessibility were deployment concerns. Information                     and coordinates specialized agents for problem definition, planning,
leakage and data security were explicit concerns. Participants raised                   result review, reporting, and refinement. A locally deployed LLM
protection across data access, model use, storage, and reporting.                       supports these agents’ reasoning and generation, and an isolated
Beyond security, they wanted AI-assisted analytical outputs to                          coder worker hosts a coding agent that generates, executes, and
be understandable and usable by stakeholders without technical                          revises analysis scripts before returning the resulting artifacts to
or data-analysis expertise, such as coaches and players, without                        the backend. Together, these components automate bounded stages
continual support from a specialist analyst. E3 described the desired                   (DG1), preserve inspectable artifacts and user control (DG2), pro-
outcome as “an environment in which anyone can perform analysis                         vide accessible and actionable interaction (DG3), and support the
independently—where questions such as ‘I want that data’ or ‘What                       cross-cutting data-exposure and containment requirement. Figure 2
is happening with this data?’ can be directed to an LLM rather than                     summarizes the system components and their primary exchanges.
a data scientist or data analyst, allowing people to resolve them
independently.” Together, these responses highlight the importance                      5.1      Web Interface
of protecting information throughout the analytical workflow while                      The web interface is the user’s point of contact with the system.
making its outputs accessible to stakeholders with different levels                     Implemented as a Next.js application [38], it consists of a dashboard
of technical expertise.                                                                 and stage-specific job pages. Each stage produces a persistent, in-
                                                                                        spectable output (such as a dataset summary, problem definition,
4    Design Goals                                                                       analytical plan, execution record, or report), which we refer to as
The formative findings informed and refined three design goals that                     an artifact. These artifacts serve as inputs to subsequent stages.
connect the reported needs to the implemented architecture and                          A job represents a persistent analysis workspace that connects a
workflow. Table 1 summarizes their relationship to the design goals                     user’s request and target dataset with the progress, artifacts, and
and cross-cutting data-exposure and containment requirement.                            interaction history of the resulting analysis. The dashboard allows
                                                                                        users to create a job by selecting a target dataset and providing
   DG1: Enable efficient, data-grounded automation. Expec-                              a job name. It also lists existing jobs together with their current
tations for greater speed and less manual work extended beyond                          status and analytical stage.
computation to preparation, verification, reporting, and revision.                         After starting a job, the user moves through stage-specific pages
External data-access constraints may limit the achievable benefit,                      corresponding to the analytical workflow described in Section 6.
but the system’s primary contribution is to reduce effort within the                    A persistent stage navigator communicates progress and allows
analytical stages it supports. DG1 therefore emphasizes automation                      the user to revisit the artifacts and interactions associated with
across the supported workflow while grounding each analysis in                          each stage. Each page presents the information and interaction
the data already available.                                                             controls relevant to its current stage. While an analysis is running,
   DG2: Preserve verifiability and human analytical control                             the interface polls the backend for updated state and displays newly
across workflow stages. Trust and appropriate reliance were as-                         produced artifacts when they become available. In the final report,
sociated with transparency into the analytical process and contin-                      interactive evidence identifiers make the connection from claims to
ued human oversight of domain-specific decisions. DG2 therefore                         supporting results or code directly accessible, combining DG2’s in-
emphasizes cross-stage inspectability and revisability, traceable                       spectability with DG3’s emphasis on usable outputs. Representative
reported claims, and selective human oversight of unresolved deci-                      interface views are provided in Appendix F.
sions that could materially change the analysis.
                                                                                        5.2      Agent-Based Analysis Backend
   DG3: Support accessible and actionable use across stake-
                                                                                        The agent-based analysis backend is implemented with FastAPI
holders. Participants emphasized that analytical outputs needed to
                                                                                        [11] and has three primary responsibilities: controlling access to
be understandable, appropriately prioritized, and usable by stake-
                                                                                        system resources, managing analysis jobs, and coordinating the
holders with different levels of technical expertise. DG3 therefore
                                                                                        agents that perform the analysis. First, the backend authenticates
focuses on clear reporting, accessible interaction, and self-service
                                                                                        users, enforces account and job ownership, and controls access to
use without continual support from specialist analysts.
                                                                                        datasets and generated artifacts, providing the resource protection
   Cross-cutting requirement: Reduce unnecessary data expo-                             required across the workflow. The web interface accesses the LLM,
sure and constrain untrusted operations. Data-exposure and                              coder worker, and analysis resources only through the backend.
containment concerns apply across the design goals and workflow                         Second, the backend manages the lifecycle and state of each analysis
stages rather than to a single interaction objective. This yields a                     job. This persistent state allows an analysis to progress efficiently
cross-cutting requirement to reduce unnecessary data exposure                           across stages (DG1) while retaining the intermediate results and
and limit the effects of untrusted operations.                                          interactions needed for inspection, revision, and resumption (DG2).
                                                                                    5
                                                                                                                                                 Yeung and Fujii

                Table 1: Relationship between formative findings, design responses, and main system implications.

Formative finding                    Design response         Main system implication
Workflow-wide efficiency             DG1                     The six-stage workflow automates data profiling, plan generation, code execution, review, and
                                                             reporting from available data.
Verifiability and calibrated trust   DG2                     Persistent artifacts link the problem definition, confirmed plan, code, execution records, outputs,
                                                             and report claims.
Automation boundaries                DG2                     Confirmation gates precede consequential stages, while feedback is routed to the earliest
                                                             responsible stage for regeneration.
Practical communication and self-    DG3                     Human-readable, evidence-linked reports prioritize supported findings, while the web interface
service use                                                  supports focused follow-up without requiring code editing.
Data-security concerns               Cross-cutting data-     A local model supports data-local processing, backend mediation constrains resource access,
                                     exposure and contain-   and an isolated coder worker limits some effects of generated code across the workflow.
                                     ment requirement

Figure 2: System architecture of AI Soccer Analyst. The web interface communicates with the agent backend, which coordinates
the local LLM, isolated coder worker, and analysis artifacts. These artifacts record the problem definition, analytical plan,
execution records, generated outputs, review decisions, report, and interaction history across workflow stages.

   Finally, the backend coordinates the specialized agents that per-             are routed to the responsible stage so that affected downstream
form each stage of the analysis described in Section 6. For each                 artifacts can be regenerated.
stage, it selects the appropriate agent and provides the relevant
context, including the user’s request, target-dataset information,
outputs from previous stages, and subsequent feedback. Reasoning                 5.3     Local LLM Deployment
and generation requests are routed to the locally deployed LLM,
                                                                                 AI Soccer Analyst uses OpenAI’s gpt-oss-120b, an open-weight
while code-generation and execution tasks are delegated to the
                                                                                 mixture-of-experts model designed for reasoning, structured gen-
isolated coder worker. The returned outputs are recorded as job
                                                                                 eration, tool use, and agentic workflows [30]. We selected the 120B
artifacts and used to update the job’s current state. The backend
                                                                                 model to balance reasoning capacity with local deployability and
pauses at defined confirmation checkpoints and, outside them, only
                                                                                 used it as a fixed baseline across the planning, coding, review, and
when an unresolved decision can materially change the analysis;
                                                                                 reporting stages. Its architecture and benchmark performance are
otherwise, progression remains automatic. Refinement requests
                                                                                 documented by OpenAI [30]; we cite these results only to charac-
                                                                                 terize the model, not as evidence for the interaction and verification
                                                                            6
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

mechanisms evaluated in this work. Comparing alternative model                          requested changes to the responsible stage. Table 2 summarizes
sizes and families is outside the scope of the paper.                                   each agent’s workflow stages, responsibilities, and main artifacts.
   The model is hosted locally using vLLM [26]. Using a local de-                       Appendix D provides shortened agent prompts.
ployment rather than an external API supports data-local process-
ing. This keeps analytical data, prompts, and intermediate workflow                     6.1     Data Understanding
context within the controlled deployment environment and avoids                         The user begins by selecting the target dataset. The system automat-
transmitting them to an external model provider. Local deployment                       ically profiles its source files, record structures, fields, data types,
also allows the same model checkpoint and inference configura-                          missing values, examples, basic statistics, and possible identifier
tion to be used consistently across workflow stages and evaluation                      and time fields (DG1). The system checks what data exists and its
conditions.                                                                             structure, but the user must judge whether the data is sufficient and
                                                                                        appropriate for answering their specific analysis problem (DG2).
5.4     Isolated Coder Worker                                                           The stage ultimately produces a dataset summary stored as JSON
The coder worker isolates code generation and execution from                            for downstream automation and rendered as Markdown for user
the analysis backend because generated scripts may fail, perform                        inspection.
unintended file operations, consume excessive resources, or access                          The summary provides an overview, while task-relevant file
sensitive backend configuration. AI Soccer Analyst therefore runs                       details remain available on demand during planning and review.
the CoderAgent and its execution environment in a separate Docker                       By summarizing rather than loading all records, the workflow can
container [8]. The container limits access to backend resources,                        accommodate datasets of different sizes while limiting context use.
while time, concurrency, and output-size limits bound automated                         It is retained as an input to Structured Planning; Problem Definition
execution, reducing exposure of backend resources and containing                        focuses only on the user’s natural-language request.
some effects of generated code. The backend remains responsible
for job coordination and analysis state.                                                6.2     Problem Definition
   The CoderAgent uses Aider [12] to generate or revise scripts in                      The user provides a natural-language analytical question and any
a job-specific working directory. For each request, the backend sup-                    constraints or clarifications about the intended entities, scope, com-
plies a bounded bundle containing the confirmed analytical plan, se-                    parisons, and expected result. The AnalystAgent organizes the
lected context files, and execution metadata. Aider applies revisions                   information stated in the request and asks for clarification when an
directly to the working script, allowing focused changes across                         ambiguity must be resolved before planning (DG1). The user then
execution–review rounds without regenerating it from scratch.                           judges whether the resulting definition accurately represents the
After each run, the worker returns the execution status, logs, gen-                     intended question, scope, and soccer-domain criteria and confirms
erated code, and output files as analysis artifacts. These records                      or corrects it (DG2). The stage ultimately produces the confirmed
support subsequent review and retain the evidence required for                          problem definition.
DG2’s inspection and revision.                                                             The interface presents the definition through three fields. The
                                                                                        Task field specifies the intended analysis, relevant soccer enti-
6     Analytical Workflow                                                               ties, scope, comparisons, and expected result. The Limitations field
For the user, the workflow begins with dataset selection and ends                       records constraints or preferences provided by the user, while the
with an evidence-grounded report that they can question or refine.                      Clarifying questions field asks the user to resolve parts of the re-
Its six stages are Data Understanding, Problem Definition, Struc-                       quest that could be interpreted in multiple ways and lead to different
tured Planning, Execution, Evidence-Grounded Reporting, and In-                         analyses. For example, “top-performing teams” does not specify
teraction and Refinement. Execution Review operates as an internal                      how performance should be measured or which teams should be
substage of Execution. Figure 3 illustrates the six-stage progression,                  included. While clarifying questions or corrections remain, the
the main artifacts and user interactions across the stages, the in-                     workflow stays in this stage; user confirmation transitions it to
ternal review loop within Execution, and the routes for confirmed                       Structured Planning.
refinements to affected stages. Each stage produces a persistent,
inspectable output, referred to as an artifact. The user confirms the                   6.3     Structured Planning
problem and plan at defined checkpoints and inspects the report                         Structured Planning begins with the problem definition confirmed
and its evidence (DG2). The user otherwise provides input only                          by the user in the preceding stage. During planning, the user may
when an unresolved decision can materially change the analysis,                         add constraints or revise the proposed analytical steps. The An-
while routine workflow steps advance automatically (DG1). These                         alystAgent combines that input with the dataset summary and
artifacts support traceability and refinement (DG2) while making                        relevant dataset details to translate the requested soccer concept
the process accessible to users with different technical capabilities                   into a quantitative definition and a sequence of coding steps. It
(DG3).                                                                                  constructs the plan using available files, fields, values, and map-
   Four agents coordinate the workflow. The AnalystAgent de-                            pings and requests targeted context when essential information
fines the problem, creates the plan, and produces the report. The                       is missing. Constructing the plan from available dataset context
CoderAgent implements and executes the confirmed plan, while the                        supports data-grounded planning (DG1). The user judges whether
ReviewAgent checks the code and results. After reporting, the In-                       the quantitative definitions, comparisons, and assumptions validly
teractionRefinementAgent answers follow-up questions and routes                         represent the intended soccer concepts (DG2). The plan presents
                                                                                   7
                                                                                                                                 Yeung and Fujii

Figure 3: Illustrated six-stage analytical workflow on a soccer-field background. Solid blue arrows show forward progression,
the orange arrow shows the internal review loop at Execution, and dashed purple arrows route confirmed refinements from
Interaction and Refinement to affected stages. Green pills identify the main artifacts, while orange callouts identify user
interactions.

                              Table 2: Responsibilities of the four agents in the analytical workflow.

Agent                    Workflow stage(s)                Responsibilities                                 Main artifacts
AnalystAgent             Problem Definition, Structured   Interprets the user’s question, prepares the     Confirmed problem definition,
                         Planning, and Evidence-          analytical plan, and synthesizes the final re-   confirmed analytical plan, and
                         Grounded Reporting               port from reviewed evidence.                     evidence-grounded report.
CoderAgent               Execution (Analysis Execution)   Uses Aider [12] to generate or revise the        Execution record and outputs.
                                                          analysis script, which the isolated worker
                                                          executes to produce the planned outputs.
ReviewAgent              Execution (Execution Review)     Uses a separate review context to compare        Review result.
                                                          the confirmed plan, generated code, execu-
                                                          tion record, and outputs and then accepts
                                                          the execution, requests revision, or asks for
                                                          clarification.
Interaction-             Interaction and Refinement       Answers questions from existing artifacts,       —
RefinementAgent                                           requests clarification when needed, and
                                                          routes confirmed refinements to the earliest
                                                          responsible stage.

these choices as user-readable steps (DG3). After the user confirms          For targeted retrieval, the AnalystAgent can call get_file_summary
them, the stage ultimately produces the confirmed analytical plan.        to inspect a relevant file; Appendix E describes the available func-
                                                                          tions. Each result is added to the planning context, and the number

                                                                      8
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

of retrieval rounds is limited. The workflow remains in planning                        correctness. Changes to the analytical definition or computation
while additional information is needed or the user is revising the                      must return to the responsible upstream stage. Therefore, the work-
plan, and advances to Analysis Execution only after user confirma-                      flow transitions to Interaction and Refinement, where the user can
tion.                                                                                   ask follow-up questions or request corrections.

6.4     Execution                                                                       6.6      Interaction and Refinement
6.4.1 Analysis Execution. The user provides the confirmed ana-                          After reading the report, the user either asks a follow-up question
lytical plan and, only when an unresolved decision concerns analyt-                     or requests a change. The InteractionRefinementAgent answers
ical intent, scope, or preference, any requested clarification; the user                a follow-up question from existing artifacts or, if a refinement is
does not need to write or run code. The CoderAgent automatically                        required, routes it to the earliest responsible stage and identifies
generates and executes the analysis script in the isolated worker                       only the affected downstream artifacts (DG1). Before refinement
(DG1). The worker enforces operational limits and records logs                          begins, the user confirms that the proposed target and scope match
and outputs that support downstream traceability (DG2). Analysis                        the intended change and remains responsible for judging the do-
Execution itself does not validate these artifacts; that assessment                     main validity of the revised analysis (DG2). The stage ultimately
occurs in Execution Review. The substage ultimately produces the                        produces either an artifact-grounded answer to the question (DG3)
execution record and analytical outputs for review.                                     or an updated set of affected artifacts and their visible interaction
   Behind the interface, the CoderAgent uses Aider in the isolated                      history (DG2); it introduces no separate main artifact.
worker (Section 5.4) to generate or revise an analysis script. The exe-                    When an artifact is revised or regenerated, the new version re-
cution record retains the generated code, logs, and output summary                      places the previous version. Consequently, only the current version
for the ReviewAgent. The final user-facing report is synthesized sep-                   remains inspectable. The scope of regeneration depends on the
arately by the AnalystAgent during Evidence-Grounded Reporting.                         requested change: a wording change updates only the report, a
A completed run advances to Execution Review.                                           change to a metric definition returns to Structured Planning, and
                                                                                        a change to the teams or time period being compared returns to
6.4.2 Execution Review. The user’s confirmed plan supplies the
                                                                                        Problem Definition.
review criteria, and the user provides clarification only when a
question concerns analytical intent, scope, or preference. Using
a new context independent of the CoderAgent, the ReviewAgent                            7       User Experiment
compares the confirmed plan, generated code, execution record, and                      A task-based evaluation of AI Soccer Analyst was conducted to
outputs to assess plan adherence and computational consistency                          examine operational completion, perceived output quality, and
(DG2). The substage ultimately produces a review result recording                       the evidence participants used to judge an analysis. This was a
acceptance, revision feedback, or a clarification request.                              single-system evaluation rather than a controlled comparison with
   Most review and revision rounds occur automatically (DG1).                           a baseline. Each retained participant attempted one analytical task
Acceptance advances to Evidence-Grounded Reporting, while revi-                         at each of three levels of increasing analytical difficulty: L1 (de-
sion feedback returns the workflow to Analysis Execution. Dataset                       scriptive retrieval), L2 (comparative interpretation), and L3 (tactical
questions are resolved by retrieving the required details, whereas                      synthesis). The evaluation combined system logs and retained arti-
the user is involved when clarification concerns analytical intent,                     facts with task-level ratings, an overall-system survey, and open
scope, or preference. The configured round limit stops automated                        responses.
progression.
                                                                                        7.1      Dataset
6.5     Evidence-Grounded Reporting                                                     All analytical tasks used the public Wyscout 2017 soccer-event
Evidence-Grounded Reporting receives the reviewed outputs and                           dataset [31]. As reported in the dataset paper, the dataset contains
execution records from the preceding stage, together with the                           over 3 million events from over 1.9 thousand matches involving
cleaned code and confirmed problem definition. The AnalystAgent                         over 4 thousand players across seven competitions: the top divisions
uses these artifacts to generate a report organized around the user’s                   of England, France, Germany, Italy, and Spain, plus UEFA Euro 2016
problem (DG1). It grounds report claims in the reviewed outputs                         and the 2018 FIFA World Cup. The accompanying files provide
and execution records and connects each claim to its supporting                         match, team, player, competition, and coaching metadata.
evidence through identifiers (DG2). The cleaned code is provided as                        Event data is a chronological log of discrete match actions. For
an explanatory view of the computation, not as evidence that veri-                      example, one record may describe a pass by a particular player
fies a claim. The stage outputs the evidence-grounded report with                       and team at a given match time and pitch location, while a later
its supporting tables, figures, and claim-to-evidence associations in                   record may describe the resulting shot. Records include event and
a user-readable form (DG3). The user then checks the validity of                        subevent labels, identifiers for the match, team, and player, match
the report’s interpretations and conclusions (DG2). Appendix G.6                        period and time, event tags, and locations when available. These
provides implementation details and an example.                                         fields support filtering, aggregation, sequence analysis, and spatial
    The AnalystAgent may improve how supported results are orga-                        summaries. However, these analyses are limited to actions recorded
nized and explained, but it cannot fix incorrect calculations. A status                 in the event log. For example, the dataset cannot be used to analyze
of “Complete” means that the automated workflow has reached its                         off-the-ball player movement or changes in team formation because
terminal state; it does not indicate expert validation of analytical                    this information is not recorded.
                                                                                    9
                                                                                                                                         Yeung and Fujii

7.2    Three Levels of Analytical Tasks                                            The overall-system assessment contained eight agreement items
The tasks were divided into three levels to represent distinct stages          covering trust, the ability to judge validity, process and evidence ver-
of analytical work rather than treating every task as simply easy              ifiability, efficiency, reduced manual work, interaction usefulness,
or difficult. L1 tests whether the system can retrieve and summa-              and intended future use. In addition, four open-response questions
rize explicitly requested information. L2 introduces the additional            asked what worked well, what was difficult or inefficient, which
need to choose appropriate comparison conditions and interpret                 outputs felt untrustworthy, and what additional evidence would
differences in context. L3 tests whether the system can integrate              support verification. The complete Survey 2 instrument appears in
several event patterns into a coherent tactical account. Keeping               Appendix A.
these stages separate makes it possible to evaluate the system as                  Invitations were sent to university soccer-team analysts, master’s
analytical abstraction, verification effort, and reliance on domain            or doctoral students whose research focused on soccer, and indi-
judgment increase.                                                             viduals who belonged to both groups. In total, 23 participants were
    The levels also differ in the soccer knowledge needed to for-              recruited, of whom 16 completed the experimental procedure and
mulate and assess an answer. L1 requires relatively little domain              submitted Survey 2. The analysis included all 16 participants and
knowledge because its quantities can be obtained through direct                their 48 analytical tasks, with 16 tasks at each level. One participant
filtering and aggregation. L2 requires moderate domain knowl-                  (P013) had no operationally completed task but remained in the
edge to select meaningful comparison groups and judge whether                  cohort so that operationally incomplete tasks and overall-system
definitions are applied consistently. L3 requires the most domain              perceptions were represented. The experiment was approved by
knowledge because several results must be connected to higher-                 the institutional ethics review board, and all participants provided
level soccer concepts and assessed for tactical plausibility. Table 3          written informed consent before taking part.
summarizes these distinctions and gives one representative task
at each level. A complete L1 example, including its problem defini-            8     Results
tion, confirmed plan, report, evidence links, and cleaned code, is             This section presents five complementary views of the evaluation
provided in Appendix G.                                                        before deriving design implications. It first examines participants’
                                                                               ratings of completed analytical tasks and then identifies why other
7.3    Experiment Method                                                       tasks were operationally incomplete. It next characterizes human–
                                                                               AI collaboration across the workflow, reports overall system ratings,
Participants attempted the three tasks: L1, then L2, then L3. Before
                                                                               and uses the open responses to explain participants’ positive assess-
starting, they received the same written study instructions and a
                                                                               ments and remaining concerns. Together, these analyses distinguish
PowerPoint walkthrough covering the Wyscout dataset, the three
                                                                               the perceived value of completed results from operational barriers
task-level definitions with examples, and the system workflow for
                                                                               and show how participants contributed domain expertise during the
creating a job, confirming the problem definition and plan, and
                                                                               analytical process. Supplementary information and full statistical
inspecting the report and its evidence. Participants formulated their
                                                                               results appear in Appendix C.
own soccer-analysis question at each level rather than following
the example; the level descriptions and examples in Table 3 guided
the intended scope and complexity. Participants were instructed                8.1    Ratings for Completed Tasks
to spend approximately 45–60 minutes on each task. Jobs could                  Ratings were summarized descriptively using medians and interquar-
continue asynchronously beyond the session, but a job that had                 tile ranges. To explore whether participants perceived completed
not produced a final report at the 24-hour cutoff was stopped and              outputs favorably, we used exact one-sided Wilcoxon signed-rank
classified as incomplete. If a task failed, was cancelled, or remained         tests [41] to determine whether participant-aggregated ratings of
unresolved, participants proceeded to the next level.                          output quality, task achievement, reliability, and verifiability ex-
   After each attempted task, including an incomplete one, partici-            ceeded the neutral midpoint of 3 on the 5-point Likert scale (1–5).
pants recorded the job name and rated output quality, task achieve-            The analysis included the 33 operationally completed analytical
ment, reliability, and verifiability on 5-point Likert scales from very        tasks. These ratings therefore characterize completed tasks only
poor to very good. For analysis, a task was classified as operationally        and do not represent participants’ experiences with operationally
complete when the system completed the Evidence-Grounded Re-                   incomplete tasks. Ratings were first averaged within participant for
porting stage and generated a final report; this corresponded to               each outcome because ratings from tasks completed by the same
a final top-level job status of complete. Jobs ending as failed or             participant are not independent. This also prevented participants
cancelled, or otherwise remaining unresolved, were classified as               with more completed tasks from having greater influence on the
operationally incomplete. Operational completion indicates suc-                results. Each of the 15 participants with at least one completed task
cessful pipeline completion and report generation, but does not                therefore contributed a single value per outcome; P013 contributed
establish the semantic or statistical correctness of the analysis. By          no completed-task rating.
this definition, 33 of 48 tasks were operationally complete. All 15                All four participant-aggregated ratings met the unadjusted 𝑝 <
incomplete tasks were rated and retained in the analysis of opera-             .05 threshold: output quality (𝑝 = .0002), task achievement (𝑝 =
tionally incomplete tasks, but their ratings were excluded from the            .0001), reliability (𝑝 = .0022), and verifiability (𝑝 = .0022). All four
completed-task rating analysis. After the three task stages, partici-          remained significant after Holm correction [19] (adjusted 𝑝 = .0002–
pants completed the overall-system assessment and open-response                .0044). Figure 4 shows the distributions of participant-aggregated
questions.                                                                     ratings. Complete descriptive and participant-level test statistics,
                                                                          10
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

                                                Table 3: Analytical task levels used in the evaluation.

Level                      Goal                                Characteristics                                Example
L1—Descriptive       Re-   Retrieve and summarize ex-          Simple filtering, aggregation, and descrip-    Summarize the number of passes, shots, and duels
trieval                    plicit information from event       tive statistics with low reasoning and veri-   for each team.
                           data.                               fication demands.
L2—Comparative In-         Compare and interpret pat-          Multi-condition comparison, contextual         Compare passing patterns between Team A and the
terpretation               terns across multiple analyt-       reasoning, and moderate verification effort.   top-performing teams.
                           ical conditions.
L3—Tactical Synthesis      Produce higher-level tactical       Multi-step reasoning, analytical synthesis,    Generate a tactical analysis report describing a
                           and analytical conclusions          report generation, and integration of mul-     team’s attacking tendencies based on passing se-
                           from event data.                    tiple event patterns.                          quences, shot creation, and player involvement.

                                                                                        Figure 5: Primary causes assigned to the 15 operationally
Figure 4: Participant-aggregated ratings for the 33 completed                           incomplete analytical tasks.
analytical tasks. Points represent participants. Each box
spans the interquartile range (IQR; 25th–75th percentiles),
its central line marks the median, and its whiskers extend
to the most extreme values within 1.5 times the IQR. The
dashed line marks the neutral value of 3.

                                                                                        this reason. A further 6 tasks across 5 participants failed because
                                                                                        execution could not resolve required dataset fields, identifiers, tags,
together with task-level analyses stratified by task complexity level                   or available records. These tasks ranged from player rankings and
(L1–L3), are reported in Appendix C. These results indicated that                       temporal passing comparisons to tactical reports, showing that
participants who received a completed output generally evaluated                        schema and data-capability problems occurred across the three an-
its quality, usefulness for the task, reliability, and verifiability fa-                alytical levels. Another 3 tasks stopped because the system ran out
vorably. The consistently positive ratings suggest that participants                    of memory during the analysis, 1 failed because the required report
perceived the completed analyses as useful and verifiable, consistent                   was saved to the wrong path, and 1 was cancelled after reaching
with the intended goals of accessibility and transparency.                              the experiment’s time limit (24 hours). The distribution of causes
                                                                                        of incompletion is shown in Figure 5.
8.2     Operationally Incomplete Task Analysis                                             The concentration of operationally incomplete tasks around data
To identify where the workflow broke down, the 15 incomplete                            resolution highlighted the value of checking dataset capabilities
analytical tasks were classified by their primary cause of incomple-                    before execution. The remaining cases highlighted the need for
tion. Classification drew on each task’s final job state, execution                     resource-aware execution, support for resuming time-limited tasks,
review, and artifact status. The causes were grouped into 5 cate-                       and artifact validation before workflow advancement. Separating
gories and summarized descriptively, with each task assigned to a                       infeasible requests from resolvable schema and identifier failures
single category.                                                                        clarifies which tasks exceeded the information available in the event
   In total, 4 tasks across 2 participants were infeasible with the                     data and which failed during execution. These findings qualified
available event data because they required tracking or off-ball infor-                  DG1 by illustrating the importance of resolving provider-specific
mation. all three of P013’s tasks were operationally incomplete for                     schemas and dataset capabilities before execution.
                                                                                   11
                                                                                                                                      Yeung and Fujii

8.3    Human–AI Collaboration Patterns                                         and helpful interaction. Responses were more mixed for validity
To characterize how participants engaged with the stage-aware                  judgment and evidence verification. Evidence verifiability met the
workflow and how soccer-domain knowledge entered the analy-                    unadjusted threshold (𝑝 = .0391) but not the Holm-adjusted thresh-
sis, logs from all 48 analytical tasks were examined for system-               old (adjusted 𝑝 = .1333), whereas validity judgment did not reach
requested clarification, feedback on the proposed plan, and post-              the unadjusted threshold (𝑝 = .0873). Although validity-judgment
result refinement. A domain-knowledge contribution was defined                 ratings were directionally positive (mean = 3.56, median = 4), re-
as participant input that changed the soccer context, analytical               sponses varied considerably (SD = 1.41, IQR = 2.75–5). This result
scope, metric or comparison definition, data feasibility, or interpre-         does not show that ratings were neutral; rather, the sample provided
tation. Presentation-only changes were excluded. Categories could              insufficient evidence that they consistently exceeded neutral. This
overlap, and all comparisons were descriptive.                                 suggests that participants generally found the evidence inspectable,
   Across the interaction types, system-requested clarification oc-            but were less certain whether the analysis itself was valid. Figure 6
curred least often, in 3 of 48 tasks (6.3%): 2 requests asked partici-         shows the response distributions, and complete item-level statistics
pants to identify the exact team and 1 asked for the exact match.              appear in Appendix C.
Participants provided plan feedback in 11 tasks (22.9%). This feed-               Participants most clearly perceived practical benefits, reporting
back addressed scope, metric definitions, output requirements, and             reduced manual work and useful interaction. These responses were
data feasibility; examples included organizing results by team and             consistent with DG1’s efficiency objective and DG3’s emphasis
defining progressive passes from player movement rather than an                on accessible interaction. Less consistent agreement on validity
assumed event tag. Participants requested post-result refinement in            and evidence verification identified stronger support for judging
9 tasks (18.8%), including expanded comparisons, corrected metric              whether an analysis should be trusted as a remaining priority for
representations, presentation changes, and further interpretation.             realizing DG2.
   Participants introduced or revised explicit soccer-domain knowl-
edge in 14 of 48 tasks (29.2%). Its first point of entry was most often        8.5    Open-Response Themes
Structured Planning (7/14 tasks), followed by post-result refinement
(4/14) and clarification (3/14). Participants identified the relevant          The open responses helped explain why participants evaluated
team or match, refined the analytical scope, defined soccer measures           the system as they did. In total, 9 participants valued analytical
and comparisons, questioned dataset feasibility, and reconsidered              efficiency and accessibility because the system could search large
how results should be interpreted.                                             event datasets, automate work, and produce usable reports without
   Together, these patterns showed that participant involvement                requiring them to write code. Analytical support and new insights
extended beyond answering system questions: analysts more often                were valued by 6 participants: structured plans, suggested analyses,
shaped the plan or revised the result. Soccer-domain knowledge                 and alternative views helped them decide what to examine and how
also entered throughout the workflow rather than only through                  to interpret a result. These accounts provided qualitative support
the problem definition. Structured Planning was the main stage at              for DG1 and DG3 by showing why manual-work reduction and
which participant expertise became an executable analytical defini-            helpful interaction received high overall ratings.
tion, while post-result refinement allowed soccer judgment to be                  The improvement-oriented responses formed two broader themes.
applied after concrete results became visible. These patterns illus-           In total, 11 participants emphasized interaction continuity and re-
trate mixed-initiative use of the stage-aware workflow: participants           covery, indicating that an analysis should remain understandable
expressed domain expertise through explicit, revisable analytical              and revisable when interaction or execution breaks down. Analyti-
decisions rather than only through the initial prompt. These obser-            cal credibility and verification were emphasized by 11 participants,
vations were consistent with aspects of DG2: participants exercised            who sought sufficient evidence to judge analytical definitions, re-
domain control by revising analytical definitions during planning              sults, and interpretations before relying on them. The reported
and after reviewing the results.                                               numbers indicated how many participants mentioned each theme.
                                                                               A participant could be included in more than one theme. Together
                                                                               with the data-resolution failures reported earlier, these themes mo-
8.4    Overall System Ratings                                                  tivated the three design implications presented next. The open
Ratings were summarized descriptively using medians and interquar-             response analysis is detailed in Appendix C.
tile ranges. To explore whether participants perceived the system
favorably, we used exact one-sided Wilcoxon signed-rank tests [41]
to determine whether each of the eight overall-system ratings ex-
                                                                               8.6    Design Implications
ceeded the neutral midpoint of 3 on the 5-point Likert scale (1–5).            The evaluation findings motivated three implications for extending
The analysis used a single response per item from each of the 16               stage-aware analytical systems. These implications concern how
participants.                                                                  systems understand changing data sources, sustain human–AI col-
    Seven of the eight ratings met the unadjusted 𝑝 < .05 thresh-              laboration across analytical tasks, and support verification beyond
old (𝑝 = .0006–.0449). After Holm correction [19] across the eight             tracing how an output was produced.
items, only reduced manual work (adjusted 𝑝 = .0049) and helpful
interaction (adjusted 𝑝 = .0184) remained significant. Responses                  Maintain provider-specific schema and capability knowledge. Soc-
leaned toward agreement across all eight items, with the clearest              cer data providers differ not only in their schemas, terminology,
concentration of positive responses for manual-work reduction                  and APIs, but also in the analytical capabilities supported by their
                                                                          12
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

   Figure 6: Distributions of the eight overall-system ratings. Ratings range from 1 (strongly disagree) to 5 (strongly agree).

data. Future systems should therefore maintain validated, provider-                     recomputation, and comparison with authoritative external statis-
specific knowledge of available fields, event types, spatial and tem-                   tics when available. Conflicting evidence and unresolved assump-
poral granularity, match coverage, and data modalities such as                          tions should be highlighted so analysts can focus their verification
event, tracking, and off-ball data. This knowledge should be incor-                     effort on the results most likely to require domain judgment.
porated into dataset understanding and planning to map analytical                          Together, these implications extend the stage-aware workflow
concepts to the correct data representations and assess feasibil-                       from supporting individual analytical tasks toward retaining knowl-
ity before execution. When a request requires information that                          edge across providers, revisions, and verification activities. They
is unavailable, such as player movement between events, sprint                          were also grounded directly in the evaluation: data-resolution fail-
trajectories, or off-ball positioning, the system should explain the                    ures motivated provider-aware dataset understanding, observed
limitation, identify the missing data modality, and either request                      plan and result revisions motivated persistent human–AI collab-
an appropriate data source or propose a feasible event-data-based                       oration, and participants’ verification concerns motivated active
alternative. This would reduce schema resolution failures while                         validation.
preventing inherently unsupported analyses from proceeding to
execution.
                                                                                        9       Discussion
                                                                                        The central contribution of AI Soccer Analyst is not simply the
                                                                                        generation of an analytical answer. It is the organization of anal-
   Extend refinement into persistent human–AI collaboration. The
                                                                                        ysis as a process in which system actions remain inspectable and
current system routes refinement to the responsible analytical stage
                                                                                        human expertise can change the analysis at the stage where it is
and regenerates its dependent artifacts. Future systems could ad-
                                                                                        needed. The evaluation provides two complementary perspectives
ditionally preserve alternative analysis branches, allow analysts
                                                                                        on this contribution: process artifacts supported inspection and
to compare the effects of different definitions or plans, and reuse
                                                                                        verification, while clarification, planning feedback, and refinement
analyst-approved domain definitions across subsequent tasks. This
                                                                                        allowed participants to introduce domain knowledge as the analysis
would transform individual revisions into persistent knowledge,
                                                                                        developed.
reduce repeated corrections, and allow the system to adapt to an
analyst’s established practices.
                                                                                        9.1      Revisability as Process-Level Transparency
                                                                                        AI Soccer Analyst shifts the focus of transparency from explaining
   Move from traceability to active verification. The current system                    a final answer to exposing the process that produced it. A plausible
links claims to plans, code, data, and result artifacts, allowing ana-                  explanation alone does not reveal how a question was interpreted,
lysts to trace how an output was produced. Future systems should                        which data were selected, or how an analytical definition was im-
also actively evaluate whether those outputs are credible using                         plemented. Externalizing the problem definition, plan, execution
domain-specific validation rules, anomaly detection, independent                        record, and claim–evidence links makes these decisions available
                                                                                   13
                                                                                                                                        Yeung and Fujii

for inspection and allows a correction to be routed to the respon-             and more diverse samples, including professional and academy an-
sible stage. The Holm-adjusted completed-task verifiability rating             alysts, coaches, and technical staff, while examining successful and
and the descriptively favorable overall evidence-verifiability ratings         unsuccessful experiences together.
suggest that participants found this process-level visibility useful.              The implementation and evaluation focused on structured JSON
However, neither the overall evidence-verifiability nor validity-              event data with a Wyscout 2017 configuration, providing a consis-
judgment item was significant after Holm correction, showing that              tent setting in which to examine the stage-aware workflow. Data
supporting validity assessment remains an open challenge.                      providers nevertheless differ in their schemas, terminology, cov-
   Revisability gives this visibility an operational role. An analyst          erage, and interfaces, and these resources can change between
can respond to a questionable assumption by changing the relevant              versions. Event logs can support only concepts represented directly
definition or plan and regenerating the affected artifacts, rather than        or derivable from their recorded fields, while sample-based profiling
accepting or rejecting the entire report. Process evidence therefore           may not expose rare structures. Future work can evaluate transfer
supports informed judgment: it shows what should be examined and               across providers, schema versions, competitions, data types, and
where an intervention can be made. This perspective also reframes              sports. It can also examine whether incorporating official provider
trust as the ability to assess and respond to an output, rather than           documentation or maintained data dictionaries into dataset un-
confidence in the output alone.                                                derstanding and planning improves task feasibility and reduces
                                                                               data-resolution failures.
                                                                                   LLM-generated plans and code provide flexibility in translating
9.2    Human–AI Collaboration as Expertise                                     natural-language questions into executable analyses, but their out-
       Integration                                                             puts remain sensitive to model assumptions and can carry shared
The staged workflow divides analytical work according to the                   blind spots across coding and review agents. Claim–evidence links
strengths of the system and the analyst. The system performs repet-            make the resulting process easier to inspect, but traceability alone
itive data inspection, code generation, execution, artifact collection,        does not establish computational or soccer-analytical correctness.
and structured checks. The analyst contributes soccer-specific def-            Future work can combine model-based review with deterministic
initions, selects meaningful comparisons, and judges whether a                 checks, independent models, or expert assessment. Studies with
result supports a credible tactical interpretation. This division does         known analytical errors can then measure whether the system iden-
not restrict domain knowledge to the initial request. The interaction          tifies the error, whether users recognize the warning and revise the
records show that participants introduced it during problem clari-             appropriate stage, and whether the final report corrects the original
fication, plan revision, and post-result refinement, with planning             problem.
and refinement serving as its principal entry points.
    The task-level patterns further suggest that the required balance          11    Conclusion
changes with analytical demand. L3 tasks had lower completion and              Soccer data analysis requires analysts to translate domain ques-
required more execution rounds than the other levels, consistent               tions into definitions and computations whose assumptions and
with the additional coordination needed to connect several event               supporting evidence can be examined, yet prompt-to-report LLM
patterns into a tactical account. Because task content and fixed               tools can obscure these decisions and make problems difficult to
order also differed across levels, this pattern should not be treated          identify and revise. This paper presented AI Soccer Analyst, which
as a controlled effect of difficulty. It nevertheless indicates that           organizes LLM-assisted analysis into the inspectable stages of Data
support for complex analysis should strengthen opportunities to                Understanding, Problem Definition, Structured Planning, Execu-
revise definitions, plans, and interpretations rather than relying on          tion, Evidence-Grounded Reporting, and Interaction and Refine-
greater automation alone.
                                                                               ment while preserving opportunities for analysts to contribute
    Together, these findings position stage-aware collaboration as
                                                                               domain knowledge. In the evaluation, 33 of 48 analytical tasks met
a means of making analytical work both revisable and open to                   the operational completion criteria. Exploratory tests supported
domain judgment. Its value lies not only in reducing manual effort,            favorable participant perceptions of completed-task output quality,
but also in providing explicit points at which analysts can shape,             task achievement, reliability, and verifiability after Holm correction.
inspect, and verify an analysis as it develops.                                Interaction records showed that participants contributed domain
                                                                               knowledge when clarifying questions, reviewing plans, and refining
10    Limitations and Future Work                                              results. Together, these findings illustrate how participants used
                                                                               stage-aware human–AI collaboration and suggest that they per-
The formative and task-based studies provide focused evidence from
                                                                               ceived it as supporting access to complex analytical work while
5 and 16 participants, respectively. Their experience as university-
                                                                               retaining opportunities for involvement in consequential decisions.
team analysts or soccer-focused researchers was well aligned with
                                                                               The approach offers a design direction for analytical systems that
the analytical workflow, but it captures only part of the range of
                                                                               combine automation with sustained human judgment and produce
roles and organizational settings in which soccer analysis is con-
                                                                               analyses that are easier to inspect, revise, and verify.
ducted. In addition, the task ratings describe the 33 completed tasks
and include ratings from only the 15 participants with at least one
completed task; they omit ratings for the 15 operationally incom-              Acknowledgments
plete tasks and therefore do not represent P013’s task-level experi-           This work was financially supported by JST FOREST Program (JP-
ence. Future evaluations can extend this evidence through larger               MJFR26153613) and JSPS KAKENHI (26H02478). The study was
                                                                          14
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

approved by the General Affairs Committee of the Graduate School                                [16] Jiajing Guo, Vikram Mohanty, Jorge Henrique Piazentin Ono, Hongtao Hao,
of Informatics, Nagoya University (approval no. I26-18(I26-09-01)).                                  Liang Gou, and Liu Ren. 2024. Investigating Interaction Modes and User Agency
                                                                                                     in Human–LLM Collaboration for Domain-Specific Data Analysis. In Extended
Generative AI tools were used to assist with manuscript writing,                                     Abstracts of the 2024 CHI Conference on Human Factors in Computing Systems.
editing, and figure preparation. The authors reviewed all AI-assisted                                Association for Computing Machinery, New York, NY, USA, Article 203, 9 pages.
                                                                                                     doi:10.1145/3613905.3651042
content and take full responsibility for the work.                                              [17] Jeffrey Heer. 2019. Agency Plus Automation: Designing Artificial Intelligence
                                                                                                     into Interactive Systems. Proceedings of the National Academy of Sciences 116, 6
                                                                                                     (2019), 1844–1850. doi:10.1073/pnas.1807184115
                                                                                                [18] Toshihiro Hirano, Hitoshi Yoshihara, Yichen Peng, Chen-Chieh Liao, Erwin Wu,
References                                                                                           and Hideki Koike. 2026. SoleCoach: Sole Pressure and IMU-Based MLLMs for
 [1] Saleema Amershi, Dan Weld, Mihaela Vorvoreanu, Adam Fourney, Besmira                            Skill Coaching. In Proceedings of the 2026 CHI Conference on Human Factors in
     Nushi, Penny Collisson, Jina Suh, Shamsi Iqbal, Paul N. Bennett, Kori Inkpen,                   Computing Systems. Association for Computing Machinery, New York, NY, USA,
     Jaime Teevan, Ruth Kikin-Gil, and Eric Horvitz. 2019. Guidelines for Human–                     Article 1429, 17 pages. doi:10.1145/3772318.3791181
     AI Interaction. In Proceedings of the 2019 CHI Conference on Human Factors in              [19] Sture Holm. 1979. A Simple Sequentially Rejective Multiple Test Procedure.
     Computing Systems. Association for Computing Machinery, New York, NY, USA,                      Scandinavian Journal of Statistics 6, 2 (1979), 65–70. https://www.jstor.org/
     Article 3, 13 pages. doi:10.1145/3290605.3300233                                                stable/4615733
 [2] Gagan Bansal, Tongshuang Wu, Joyce Zhou, Raymond Fok, Besmira Nushi, Ece                   [20] Eric Horvitz. 1999. Principles of Mixed-Initiative User Interfaces. In Proceedings
     Kamar, Marco Tulio Ribeiro, and Daniel S. Weld. 2021. Does the Whole Exceed Its                 of the SIGCHI Conference on Human Factors in Computing Systems. Association for
     Parts? The Effect of AI Explanations on Complementary Team Performance. In                      Computing Machinery, New York, NY, USA, 159–166. doi:10.1145/302979.303030
     Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems.              [21] Matthew Jörke, Shardul Sapkota, Lyndsea Warkenthien, Niklas Vainio, Paul
     Association for Computing Machinery, New York, NY, USA, Article 81, 16 pages.                   Schmiedmayer, Emma Brunskill, and James A. Landay. 2025. GPTCoach: Towards
     doi:10.1145/3411764.3445717                                                                     LLM-Based Physical Activity Coaching. In Proceedings of the 2025 CHI Conference
 [3] Virginia Braun and Victoria Clarke. 2006. Using Thematic Analysis in Psy-                       on Human Factors in Computing Systems. Association for Computing Machinery,
     chology. Qualitative Research in Psychology 3, 2 (2006), 77–101. doi:10.1191/                   New York, NY, USA, Article 993, 46 pages. doi:10.1145/3706598.3713819
     1478088706qp063oa                                                                          [22] Sean Kandel, Andreas Paepcke, Joseph M. Hellerstein, and Jeffrey Heer. 2012.
 [4] Mollie Brewer, Kevin Childs, Spencer Thomas, Celeste Wilkins, Zachary R. Smith,                 Enterprise Data Analysis and Visualization: An Interview Study. IEEE Transac-
     Kristy Elizabeth Boyer, Jennifer A. Nichols, Kevin R. B. Butler, Garrett F. Beatty,             tions on Visualization and Computer Graphics 18, 12 (2012), 2917–2926. doi:10.
     and Daniel P. Ferris. 2026. Improve my Performance, Protect my State of Mind:                   1109/TVCG.2012.219
     How Student-Athletes Engage with their Sports Data. In Proceedings of the                  [23] Majeed Kazemitabaar, Jack Williams, Ian Drosos, Tovi Grossman, Austin Z.
     2026 CHI Conference on Human Factors in Computing Systems. Association for                      Henley, Carina Negreanu, and Advait Sarkar. 2024. Improving Steering and
     Computing Machinery, New York, NY, USA, Article 1428. doi:10.1145/3772318.                      Verification in AI-Assisted Data Analysis with Interactive Task Decomposition.
     3791745                                                                                         In Proceedings of the 37th Annual ACM Symposium on User Interface Software
 [5] Mollie Brewer, Kevin Childs, Celeste Wilkins, Spencer Thomas, Kristy Elizabeth                  and Technology. Association for Computing Machinery, New York, NY, USA,
     Boyer, Jennifer A. Nichols, Kevin R. B. Butler, Garrett F. Beatty, and Daniel P.                19 pages. doi:10.1145/3654777.3676345
     Ferris. 2025. Coach, Data Analyst, and Protector: Exploring Data Practices of              [24] Jaehoon Kim, Dayoung Jeong, Beejin Son, Hansung Kim, Bogoan Kim, and
     Collegiate Coaching Staff. In Proceedings of the 2025 CHI Conference on Human                   Kyungsik Han. 2026. LAPS: Automating Hypothesis-Driven Statistical Analysis
     Factors in Computing Systems. Association for Computing Machinery, New York,                    of Public Survey Using Large Language Models. In Proceedings of the 2026 CHI
     NY, USA, 1–13. doi:10.1145/3706598.3714026                                                      Conference on Human Factors in Computing Systems. Association for Computing
 [6] Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos. 2021. To Trust                       Machinery, New York, NY, USA, 19 pages. doi:10.1145/3772318.3791665
     or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in                  [25] Kyusik Kim, Hyungwoo Song, Jeongwoo Ryu, Changhoon Oh, and Bongwon
     AI-Assisted Decision-Making. Proceedings of the ACM on Human-Computer                           Suh. 2025. BleacherBot: AI Agent as a Sports Co-Viewing Partner. In Proceedings
     Interaction 5, CSCW1, Article 188 (2021), 21 pages. doi:10.1145/3449287                         of the 2025 CHI Conference on Human Factors in Computing Systems. Association
 [7] Taizhou Chen, Kai Chen, Xingyu Liu, Pingchuan Ke, and Zhida Sun. 2026. Bad-                     for Computing Machinery, New York, NY, USA, Article 988, 31 pages. doi:10.
     minSense: Enabling Fine-Grained Badminton Strokes Evaluation on Single Smart-                   1145/3706598.3714178
     watch. In Proceedings of the 2026 CHI Conference on Human Factors in Computing             [26] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng,
     Systems. Association for Computing Machinery, New York, NY, USA, Article                        Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. 2023. Efficient
     1424, 20 pages. doi:10.1145/3772318.3790998                                                     Memory Management for Large Language Model Serving with PagedAttention.
 [8] Docker, Inc. 2026. What Is Docker? https://docs.docker.com/get-started/docker-                  In Proceedings of the 29th Symposium on Operating Systems Principles. 611–626.
     overview/                                                                                       doi:10.1145/3600006.3613165
 [9] Ian Drosos, Advait Sarkar, Xiaotong Xu, Carina Negreanu, Sean Rintel, and Lev              [27] Dokyung Lee, Jaeseong Ju, Hyungwoo Song, and Hyunwoo Park. 2026. From
     Tankelevitch. 2024. "It’s Like a Rubber Duck That Talks Back": Understand-                      Ballpark to Society: Understanding Stakeholders’ Adaptation to Automated
     ing Generative AI-Assisted Data Analysis Workflows through a Participatory                      Judgment via ABS in Baseball. In Proceedings of the 2026 CHI Conference on
     Prompting Study. In Proceedings of the 3rd Annual Meeting of the Symposium on                   Human Factors in Computing Systems. Association for Computing Machinery,
     Human-Computer Interaction for Work. Association for Computing Machinery,                       New York, NY, USA, Article 1426. doi:10.1145/3772318.3791249
     New York, NY, USA, Article 16, 21 pages. doi:10.1145/3663384.3663389                       [28] Hanbyeol Lee, Erica Kleinman, Namsub Kim, Sangbeom Park, Casper Harteveld,
[10] Upol Ehsan and Mark O. Riedl. 2020. Human-Centered Explainable AI: Towards                      and Byungjoo Lee. 2025. Crafting Champions: An Observation Study of Esports
     a Reflective Sociotechnical Approach. In HCI International 2020—Late Breaking                   Coaching Processes. In Proceedings of the 2025 CHI Conference on Human Factors
     Papers: Multimodality and Intelligence. Springer International Publishing, Cham,                in Computing Systems. Association for Computing Machinery, New York, NY,
     449–466. doi:10.1007/978-3-030-60117-1_33                                                       USA, Article 991, 20 pages. doi:10.1145/3706598.3713141
[11] FastAPI. 2026. FastAPI Documentation. https://fastapi.tiangolo.com/                        [29] John D. Lee and Katrina A. See. 2004. Trust in Automation: Designing for
[12] Paul Gauthier. 2024. Aider: AI Pair Programming in Your Terminal. https:                        Appropriate Reliance. Human Factors 46, 1 (2004), 50–80. doi:10.1518/hfes.46.1.
     //github.com/Aider-AI/aider                                                                     50.30392
[13] Andreas Göldi, Roman Rietsche, and Lyle H. Ungar. 2025. Efficient Management               [30] OpenAI. 2025.         gpt-oss-120b & gpt-oss-20b Model Card.                  (2025).
     of LLM-Based Coaching Agents’ Reasoning While Maintaining Interaction Qual-                     arXiv:2508.10925 [cs.CL] doi:10.48550/arXiv.2508.10925
     ity and Speed. In Proceedings of the 2025 CHI Conference on Human Factors in               [31] Luca Pappalardo, Paolo Cintia, Paolo Ferragina, Emanuele Massucco, Dino Pe-
     Computing Systems. Association for Computing Machinery, New York, NY, USA,                      dreschi, and Fosca Giannotti. 2019. A Public Data Set of Spatio-Temporal Match
     Article 992, 18 pages. doi:10.1145/3706598.3713606                                              Events in Soccer Competitions. Scientific Data 6, 1 (2019), 236. doi:10.1038/s41597-
[14] Ken Gu, Madeleine Grunde-McLaughlin, Andrew McNutt, Jeffrey Heer, and Tim                       019-0247-7
     Althoff. 2024. How Do Data Analysts Respond to AI Assistance? A Wizard-of-Oz               [32] Raja Parasuraman, Thomas B. Sheridan, and Christopher D. Wickens. 2000.
     Study. In Proceedings of the 2024 CHI Conference on Human Factors in Computing                  A Model for Types and Levels of Human Interaction with Automation. IEEE
     Systems. Association for Computing Machinery, New York, NY, USA, 22 pages.                      Transactions on Systems, Man, and Cybernetics—Part A: Systems and Humans 30,
     doi:10.1145/3613904.3641891                                                                     3 (2000), 286–297. doi:10.1109/3468.844354
[15] Ken Gu, Ruoxi Shang, Tim Althoff, Chenglong Wang, and Steven Mark Drucker.                 [33] Eric D. Ragan, Alex Endert, Jibonananda Sanyal, and Jian Chen. 2016. Char-
     2024. How Do Analysts Understand and Verify AI-Assisted Data Analyses?. In                      acterizing Provenance in Visualization and Data Analysis: An Organizational
     Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems.                   Framework of Provenance Types and Purposes. IEEE Transactions on Visualiza-
     Association for Computing Machinery, New York, NY, USA, Article 748, 22 pages.                  tion and Computer Graphics 22, 1 (2016), 31–40. doi:10.1109/TVCG.2015.2467551
     doi:10.1145/3613904.3642497
                                                                                           15
                                                                                               Yeung and Fujii

[34] Jasmine Y. Shih, Vishal Mohanty, Yannis Katsis, and Hariharan Subramonyam.
     2024. Leveraging Large Language Models to Enhance Domain Expert Inclusion
     in Data Science Workflows. In Extended Abstracts of the 2024 CHI Conference on
     Human Factors in Computing Systems. Association for Computing Machinery,
     New York, NY, USA, 11 pages. doi:10.1145/3613905.3651115
[35] Ben Shneiderman. 2020. Human-Centered Artificial Intelligence: Reliable, Safe &
     Trustworthy. International Journal of Human–Computer Interaction 36, 6 (2020),
     495–504. doi:10.1080/10447318.2020.1741118
[36] Lev Tankelevitch, Viktor Kewenig, Auste Simkute, Ava Elizabeth Scott, Advait
     Sarkar, Abigail Sellen, and Sean Rintel. 2024. The Metacognitive Demands and
     Opportunities of Generative AI. In Proceedings of the 2024 CHI Conference on
     Human Factors in Computing Systems. Association for Computing Machinery,
     New York, NY, USA. doi:10.1145/3613904.3642902
[37] Priyan Vaithilingam, Elena L. Glassman, Jeevana Priya Inala, and Chenglong
     Wang. 2024. DynaVis: Dynamically Synthesized UI Widgets for Visualization
     Editing. In Proceedings of the 2024 CHI Conference on Human Factors in Computing
     Systems. Association for Computing Machinery, New York, NY, USA, Article 985,
     17 pages. doi:10.1145/3613904.3642639
[38] Vercel. 2026. Next.js Documentation. https://nextjs.org/docs
[39] Chenglong Wang, John Thompson, and Bongshin Lee. 2024. Data Formulator:
     AI-Powered Concept-Driven Visualization Authoring. IEEE Transactions on
     Visualization and Computer Graphics 30, 1 (2024), 1128–1138. doi:10.1109/TVCG.
     2023.3326585
[40] Jian-Jia Weng, Calvin Ku, Jo Chien Wang, Chih-Jen Cheng, Tica Lin, Yu-An
     Su, Tsung-Hsun Tsai, You-Yi Lin, Lun-Wei Ku, Hung-Kuo Chu, and Min-Chun
     Hu. 2025. Bridging Coaching Knowledge and AI Feedback to Enhance Motor
     Learning in Basketball Shooting Mechanics Through a Knowledge-Based SOP
     Framework. In Proceedings of the 2025 CHI Conference on Human Factors in
     Computing Systems. Association for Computing Machinery, New York, NY, USA.
     doi:10.1145/3706598.3713324
[41] Frank Wilcoxon. 1945. Individual Comparisons by Ranking Methods. Biometrics
     Bulletin 1, 6 (1945), 80–83. doi:10.2307/3001968
[42] Tongshuang Wu, Ellen Jiang, Aaron Donsbach, Jeff Gray, Alejandra Molina,
     Michael Terry, and Carrie J. Cai. 2022. PromptChainer: Chaining Large Language
     Model Prompts through Visual Programming. In Extended Abstracts of the 2022
     CHI Conference on Human Factors in Computing Systems. Association for Com-
     puting Machinery, New York, NY, USA, 10 pages. doi:10.1145/3491101.3519729
[43] Tongshuang Wu, Michael Terry, and Carrie J. Cai. 2022. AI Chains: Transparent
     and Controllable Human–AI Interaction by Chaining Large Language Model
     Prompts. In Proceedings of the 2022 CHI Conference on Human Factors in Com-
     puting Systems. Association for Computing Machinery, New York, NY, USA,
     22 pages. doi:10.1145/3491102.3517582
[44] Liwenhan Xie, Chengbo Zheng, Haijun Xia, Huamin Qu, and Zhu-Tian Chen.
     2024. WaitGPT: Monitoring and Steering Conversational LLM Agent in Data
     Analysis with On-the-Fly Code Visualization. In Proceedings of the 37th Annual
     ACM Symposium on User Interface Software and Technology. Association for
     Computing Machinery, New York, NY, USA, 14 pages. doi:10.1145/3654777.
     3676374
[45] Calvin Yeung, Rory Bunker, and Keisuke Fujii. 2024. Unveiling Multi-Agent
     Strategies: A Data-Driven Approach for Extracting and Evaluating Team Tactics
     from Football Event and Freeze-Frame Data. Journal of Robotics and Mechatronics
     36, 3 (2024), 603–617. doi:10.20965/jrm.2024.p0603
[46] Calvin Yeung and Keisuke Fujii. 2024. A Strategic Framework for Optimal
     Decisions in Football 1-vs-1 Shot-Taking Situations: An Integrated Approach
     of Machine Learning, Theory-Based Modeling, and Game Theory. Complex &
     Intelligent Systems 10 (2024), 5989–6008. doi:10.1007/s40747-024-01466-4
[47] Calvin Yeung, Kenjiro Ide, Taiga Someya, and Keisuke Fujii. 2025. OpenSTARLab:
     open approach for spatio-temporal agent data analysis in soccer. Complex &
     Intelligent Systems 11, Article 342 (2025). doi:10.1007/s40747-025-01965-y
[48] Calvin Yeung, Tony Sit, and Keisuke Fujii. 2025. Transformer-Based Neural
     Marked Spatio Temporal Point Process Model for Analyzing Football Match
     Events. Applied Intelligence 55, Article 335 (2025). doi:10.1007/s10489-024-05996-
     9
[49] Calvin C. K. Yeung, Rory Bunker, and Keisuke Fujii. 2023. A Framework of
     Interpretable Match Results Prediction in Football with FIFA Ratings and Team
     Formation. PLOS ONE 18, 4 (2023), e0284318. doi:10.1371/journal.pone.0284318
[50] Jieyu Zhou, Aryan Roy, Sneh Gupta, Daniel Weitekamp, and Christopher J.
     MacLellan. 2026. When Should Users Check? Modeling Confirmation Frequency
     in Multi-Step Agentic AI Tasks. In Proceedings of the 2026 CHI Conference on
     Human Factors in Computing Systems. Association for Computing Machinery,
     New York, NY, USA, Article 1649, 20 pages. doi:10.1145/3772318.3790655

                                                                                          16
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

A     Administered Surveys and Follow-Up Interview Protocol
This appendix presents the study instruments in three parts. Survey 1 (S1) examines participants’ soccer-analysis backgrounds, current
workflows, and expectations for AI-supported analysis. The formative follow-up interview clarifies and extends participants’ Survey 1
responses, with particular attention to verification practices and appropriate boundaries for automation. Survey 2 (S2) evaluates the system
after tasks at three levels of analytical complexity: L1 (descriptive retrieval), L2 (comparative interpretation), and L3 (tactical synthesis).
It concludes with an overall assessment of the user experience. Stable identifiers S1-Q1–S1-Q14 and S2-Q1–S2-Q13 correspond to the
numbered survey items. An asterisk marks a required response.

A.1      Survey 1: Formative Evaluation

 Purpose and administration                                                                                                                           Survey 1
   The participant-facing introduction explains that the survey is part of a formative study of an AI-supported soccer-analysis system. Its
purpose is to collect expert input for future design and development, including desired analytical functions and forms of support. Responses
are used only for research, are not published in personally identifiable form, and may inform system design and subsequent research.

 Participant identification and background                                                                                                      Required items

S1-Q1*      Email address
Response format: Free text. Participants are instructed to use the address listed on their consent form; it is collected for research communication and to match
the response to the consent record.

S1-Q2*      How many years of experience do you have in soccer analysis?
Response format: Select one: less than 1 year; 1–3 years; 4–6 years; 7–10 years; 10 years or more.

 Current analysis workflow                                                                                                                      Required items

S1-Q3*      How do you currently conduct soccer analysis?
Response format: Select all that apply.
    • Analysis conducted mainly through manual work.
    • Manual analysis with some automated steps.
    • Analysis combining manual work and AI assistance.
    • Analysis conducted mainly through automation or AI assistance.
S1-Q4*      Which aspects of your current analysis workflow are the most difficult?
Response format: Select all that apply: data preparation; discovering useful insights; validation and validity checking; report preparation; sharing and
communicating results; time required; other.

S1-Q5*      Current-workflow challenges
Response format: Rate each statement.
Scale anchors: 1 = strongly disagree; 5 = strongly agree.

     Statement                                                                                                                          1   2    3   4   5
     Verification of analytical results requires substantial manual work.                                                               ◦   ◦    ◦   ◦   ◦
     Existing analysis tools provide insufficient support for inspecting or verifying the process and evidence leading to a result.     ◦   ◦    ◦   ◦   ◦
     The current analysis workflow is time-consuming.                                                                                   ◦   ◦    ◦   ◦   ◦
     Repeated manual operations reduce workflow efficiency.                                                                             ◦   ◦    ◦   ◦   ◦

 Expectations for AI-supported analysis                                                                                                         Required item

S1-Q6*      Expectations for the system
Response format: Rate each statement.
Scale anchors: 1 = strongly disagree; 5 = strongly agree.

     Statement                                                                                                                          1   2    3   4   5
     Making intermediate reasoning processes visible would increase trust in AI-generated analyses.                                     ◦   ◦    ◦   ◦   ◦
     Transparency and verifiability are important in AI-supported analysis.                                                             ◦   ◦    ◦   ◦   ◦
     An LLM-based system is expected to reduce the burden of manual work.                                                               ◦   ◦    ◦   ◦   ◦
     An AI-supported workflow is expected to increase the speed of analysis.                                                            ◦   ◦    ◦   ◦   ◦
                                                                                   17
                                                                                                                                     Yeung and Fujii

Semi-structured written responses                                                                                                Applicable items
  The form explains that these items are open-ended and may be followed by one or two brief questions when clarification is needed.
Follow-ups are intended to clarify the response while minimizing participant burden.
S1-Q7*    Please describe your current analysis workflow.
Response format: Open text.
S1-Q8*    What are the main challenges in your current workflow?
Response format: Open text.
S1-Q9*    Which analysis tasks require the most manual work?
Response format: Open text.
S1-Q10*     At which stage of the analysis process are corrections or rework most likely to occur, and why?
Response format: Open text.
S1-Q11*     How do you currently check or validate the validity of analytical results?
Response format: Open text.
S1-Q12*     What do you expect from an LLM-based analysis-support system?
Response format: Open text.
S1-Q13*     What elements would be necessary to increase your trust in an AI-supported analysis system?
Response format: Open text.
S1-Q14*     What concerns would you have when using such a system?
Response format: Open text.

A.2     Formative Follow-Up Interview
The follow-up interview is a separate, semi-structured protocol rather than a numbered component of either survey form. Interview questions
are selected in response to the participant’s Survey 1 answers. They are not administered as a fixed checklist: each category has a specific
diagnostic purpose, and the interviewer asks only the interview questions needed to understand the participant’s account.
Rating rationale.
Purpose: explain unusually high or low ratings and distinguish the participant’s interpretation of a scale item from its intended construct.
Interview questions: Ask why the participant selected the response and request a concrete example from a recent analysis task.

Workflow reconstruction.
Purpose: connect general descriptions to the steps and tools used in actual practice. Interview question: Ask how the participant usually
performs that step.

Verification and rework.
Purpose: identify the evidence analysts inspect and the failures that initiate revision. Interview questions: Ask what information the participant
inspects when checking a result and what commonly causes an analysis to be revised.

Automation boundaries.
Purpose: locate decisions that can be automated and decisions where domain input has high analytical leverage. Interview question: Ask when
an automated action would be acceptable without confirmation and when the system should stop and ask.

Domain conflict and responsibility.
Purpose: understand how analysts resolve disagreement between generated evidence and soccer knowledge. Interview question: Ask how the
participant would decide what to do if a system result conflicted with their soccer knowledge.

Coverage check.
Purpose: surface practices or concerns not anticipated by the survey. Interview question: Ask whether the questionnaire omitted anything
important about workflow, trust, verification, or the use of AI.
  Short probes such as asking why, requesting an example, or asking how a step is usually performed are used to clarify vague answers,
apparent contradictions, or distinctive practices.

A.3     Survey 2: User Evaluation
Purpose and administration                                                                                                               Survey 2
   The participant-facing introduction explains that Survey 2 evaluates the AI-supported soccer-analysis system after use. Participants
assess both their experience and the generated analytical results. The survey contains three task-level sections, completed after L1, L2, and
                                                                        18
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

L3 respectively, followed by one overall-system evaluation section. Responses are used only for research, are not published in personally
identifiable form, and may inform system evaluation and future development.
 Participant identification and background                                                                                                      Required items

S2-Q1*      Email address
Response format: Free text. Participants are instructed to use the address listed on their consent form; it is collected for research communication and to match
the response to the consent record.
S2-Q2*      How many years of experience do you have in soccer analysis?
Response format: Select one: less than 1 year; 1–3 years; 4–6 years; 7–10 years; 10 years or more.

 Part 1: L1 descriptive-retrieval task evaluation                                                                                               Required items

S2-Q3*      Enter the name of the L1 job executed in the system.
Response format: Free text.
S2-Q4*      Rate the system for the L1 task.
Response format: One rating per criterion.
Scale anchors: 1 = very poor; 5 = very good.

          Criterion                                                                                                                1   2    3    4   5
          Output quality                                                                                                           ◦   ◦    ◦    ◦   ◦
          Task achievement                                                                                                         ◦   ◦    ◦    ◦   ◦
          Reliability                                                                                                              ◦   ◦    ◦    ◦   ◦
          Verifiability                                                                                                            ◦   ◦    ◦    ◦   ◦

 Part 2: L2 comparative-interpretation task evaluation                                                                                          Required items

S2-Q5*      Enter the name of the L2 job executed in the system.
Response format: Free text.
S2-Q6*      Rate the system for the L2 task.
Response format: One rating per criterion.
Scale anchors: 1 = very poor; 5 = very good.

          Criterion                                                                                                                1   2    3    4   5
          Output quality                                                                                                           ◦   ◦    ◦    ◦   ◦
          Task achievement                                                                                                         ◦   ◦    ◦    ◦   ◦
          Reliability                                                                                                              ◦   ◦    ◦    ◦   ◦
          Verifiability                                                                                                            ◦   ◦    ◦    ◦   ◦

 Part 3: L3 tactical-synthesis task evaluation                                                                                                  Required items

S2-Q7*      Enter the name of the L3 job executed in the system.
Response format: Free text.
S2-Q8*      Rate the system for the L3 task.
Response format: One rating per criterion.
Scale anchors: 1 = very poor; 5 = very good.

          Criterion                                                                                                                1   2    3    4   5
          Output quality                                                                                                           ◦   ◦    ◦    ◦   ◦
          Task achievement                                                                                                         ◦   ◦    ◦    ◦   ◦
          Reliability                                                                                                              ◦   ◦    ◦    ◦   ◦
          Verifiability                                                                                                            ◦   ◦    ◦    ◦   ◦

 Part 4: Overall system evaluation                                                                                                              Required item

S2-Q9*      Overall system evaluation
Response format: Rate each statement.
Scale anchors: 1 = strongly disagree; 5 = strongly agree.

                                                                                   19
                                                                                                                              Yeung and Fujii

   Statement                                                                                                         1   2     3   4    5
   I could trust the analytical results generated by the system.                                                     ◦   ◦     ◦   ◦    ◦
   I could judge whether the system output was valid or problematic.                                                 ◦   ◦     ◦   ◦    ◦
   The system made it easy to inspect and verify the process leading to an analytical result.                        ◦   ◦     ◦   ◦    ◦
   The system made it easy to inspect and verify the evidence supporting an analytical result.                       ◦   ◦     ◦   ◦    ◦
   The system helped me progress through analysis tasks efficiently.                                                 ◦   ◦     ◦   ◦    ◦
   The system reduced unnecessary manual work.                                                                       ◦   ◦     ◦   ◦    ◦
   Dialogue with the system, including questions, corrections, and feedback, helped me progress with the analysis.   ◦   ◦     ◦   ◦    ◦
   I would like to use this system in future soccer-analysis work.                                                   ◦   ◦     ◦   ◦    ◦

Overall written feedback                                                                                                     Optional items

S2-Q10     What aspects of the system were good?
Response format: Open text.
S2-Q11     While using the system, what was difficult, hard to understand, or inefficient?
Response format: Open text.
S2-Q12     Did any output feel untrustworthy? If so, please explain.
Response format: Open text.
S2-Q13     What information or explanation would you need to verify the results more effectively?
Response format: Open text.

                                                                           20
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

B Supplementary Formative Study Results
B.1 Study Data and Participants
This appendix provides supporting descriptive results and coding details for the formative study reported in Section 3. The semi-structured
protocol combined the pre-interview survey reproduced in Appendix A with follow-up questions. Administrative fields and personally
identifying information were excluded.
   Participants were recruited through email invitations. Eligibility required at least 1 year of soccer-analysis experience in a professional
context or multiple years of experience in a collegiate context. In total, 7 eligible individuals were contacted, 5 agreed to participate and
completed the survey, and 2 of those 5 also completed a follow-up interview. Follow-up interviews were conducted selectively rather than
with every participant. The 2 participants were contacted because their open-ended responses raised points that required further clarification
or elaboration; the remaining survey responses were sufficiently detailed for the formative analysis. Participants received compensation of
approximately US$20. The survey took approximately 30 minutes to complete. The follow-up interviews were conducted by email, took
approximately 15 minutes, and focused primarily on the open-ended survey questions. Follow-up responses were incorporated as extensions
to the corresponding open-ended survey answers, producing the qualitative dataset used for coding.
   The study included 5 survey participants, and all percentages use 𝑛 = 5. Qualitative responses could receive multiple codes; consequently,
theme percentages do not sum to 100%. Participants are identified using the anonymized labels E1–E5; these labels distinguish participants
only and do not indicate rank or level of expertise.

B.2     Participant and Workflow Context
   Soccer-analysis experience. Table 4 summarizes the participants’ experience. All participants had at least 1 year of experience, and 4 had 4
or more years of experience. The responses therefore reflect sustained practical exposure to soccer analysis rather than first impressions
from novice users.

                                   Table 4: Participant roles, work contexts, and soccer-analysis experience.

      Participant     Role and work context                                                                                    Experience
      E1              Professional soccer analyst                                                                              4–6 years
      E2              Professional soccer analyst                                                                              1–3 years
      E3              Professional soccer analyst                                                                              4–6 years
      E4              Collegiate soccer analyst                                                                                7–10 years
      E5              Professional soccer analyst                                                                              7–10 years

   Current workflow. S1-Q3 allowed multiple selections; accordingly, the percentages in Table 5 do not sum to 100%. The overlapping
selections indicate that participants combined workflow modes rather than working exclusively manually or automatically. Participants who
selected mainly automated or AI-assisted analysis still described substantial human work in interpretation, checking, and communication,
suggesting that existing automation shifted effort rather than removing it.

                                                  Table 5: Current soccer-analysis workflow modes.

           Workflow mode                                                                                          Count    Percentage
           Mainly automation or AI assistance                                                                          4         80%
           Manual analysis with some automated steps                                                                   2         40%
           Manual work combined with AI assistance                                                                     2         40%
           Mainly manual work                                                                                          0          0%

   Workflow difficulties. The workflow-difficulty item (S1-Q4) permitted multiple selections; the reported difficulties are shown in Table 6. No
predefined difficulty dominated the sample; instead, the selections span data preparation, insight discovery, validation, communication, and
time cost. This distribution suggests that workflow burden is distributed across analytical stages rather than confined to a single bottleneck.
Report preparation received no selections, whereas E1 identified manual report creation and repeated adjustment of graph and slide layouts
as difficult. This contrast illustrates the additional context contributed by the follow-up questions.
   Current-workflow ratings. Ratings range from 1 (strongly disagree) to 5 (strongly agree). The interquartile range (IQR) is the 25th–75th
percentile interval. Table 7 reports the response distributions and descriptive statistics. Time cost received the highest median rating, while
ratings of manual verification burden and process opacity varied across participants. These results identify efficiency as the clearest shared
concern while indicating that verification needs depend on participants’ existing workflows.
                                                                                   21
                                                                                                                                      Yeung and Fujii

                                           Table 6: Difficulties in the current analytical workflow.

              Difficulty                                                                                       Count     Percentage
              Data preparation                                                                                      2           40%
              Discovering useful insights                                                                           2           40%
              Validation and validity checking                                                                      2           40%
              Sharing and communicating results                                                                     2           40%
              Time required                                                                                         2           40%
              Real-time data acquisition (other)                                                                    1           20%
              Report preparation                                                                                    0            0%

                                             Table 7: Ratings of the current analytical workflow.

S1-Q5 item                                                                                                Distribution (1/2/3/4/5)    Median    IQR
Verification requires substantial manual work                                                                    1/0/2/2/0               3      3–4
Existing tools insufficiently expose process and evidence                                                        0/2/1/0/2               3      2–5
Current workflow is time-consuming                                                                               1/1/0/3/0               4      2–4
Repeated manual operations reduce efficiency                                                                     1/1/2/0/1               3      2–3

   Expectations for AI-supported analysis. Table 8 summarizes participants’ initial expectations concerning trust, verifiability, workload, and
speed. Every rating was 4 or 5, with the strongest consensus concerning transparency and verifiability, reduced manual work, and greater
speed. The ratings therefore indicate agreement with the initial assumptions guiding the formative study: AI assistance should improve
efficiency while supporting verifiability and appropriately calibrated trust.

                                               Table 8: Expectations for AI-supported analysis.

S1-Q6 item                                                                                                Distribution (1/2/3/4/5)    Median    IQR
Visible intermediate reasoning would increase trust                                                              0/0/0/2/3               5      4–5
Transparency and verifiability are important                                                                     0/0/0/1/4               5      5–5
An LLM system could reduce manual work                                                                           0/0/0/1/4               5      5–5
AI support could increase analysis speed                                                                         0/0/0/1/4               5      5–5

B.3     Qualitative Coding and Codebook
Written responses to S1-Q7–S1-Q14, including their incorporated follow-up clarifications, were segmented into meaningful units. A response
could receive more than one code. The first pass applied three deductive categories:
• Trust and calibrated reliance: conditions affecting whether an AI-supported result can be relied upon appropriately.
• Verifiability and evidence: practices or needs for inspecting assumptions, data, process, and outputs.
• Efficiency and workload: time, repeated manual operations, bottlenecks, and desired workload reductions.
  A second pass compared uncaptured units across participants and formed inductive codes. Similar codes were merged, their boundaries
were clarified, and prevalence was counted once per participant per code. This was an exploratory single-coder analysis; no intercoder-
agreement claim is made. Table 9 presents the final codebook and participant prevalence. Its operational definitions state the observable
content used to apply each code consistently.

                                                                      22
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

                                   Table 9: Final deductive–inductive codebook and participant prevalence.

Type              Code                                                     Operational definition                                          Participants Prevalence
Deductive         Trust and calibrated reliance                       Interpretability, literacy, contextual fit, or uncertainty affect-             4        80%
                                                                      ing appropriate reliance
Deductive         Verifiability and evidence                          Inspection of assumptions, primary data, distributions, video,                 4        80%
                                                                      alternative sources, or process records
Deductive         Efficiency and workload                             Time-consuming acquisition, aggregation, reporting, check-                     4        80%
                                                                      ing, or repeated manual work
Inductive         Data access, timeliness, and infrastructure         Real-time availability, APIs, provider constraints, cloud readi-               4        80%
                                                                      ness, storage, and pipeline access
Inductive         Human interpretation and domain alignment           Need to connect outputs with soccer knowledge, tactical judg-                  4        80%
                                                                      ment, video, and local team criteria
Inductive         Communication and actionable outputs                Reporting, prioritization, staff-facing presentation, self-                    4        80%
                                                                      service access, and information overload
Inductive         Organizational adoption and capability distribution Literacy, staff engagement, individual dependency, continuity,                 3        60%
                                                                      and uneven technical capability
Inductive         Automation boundaries and skill preservation        Work suitable for automation versus work requiring judg-                       2        40%
                                                                      ment, plus risks of deskilling
Inductive         Data security and information governance            Risk of sensitive information leakage or insecure use of AI-                   2        40%
                                                                      supported tools

                                                                                   23
                                                                                                                                    Yeung and Fujii

C Supplementary User Evaluation Results
C.1 Study Data and Participants
This appendix reports the detailed cohort definition, descriptive results, inferential tests, system-behavior summaries, and qualitative
codebook for the task-based evaluation described in Section 7.
   Participants were recruited through email invitations sent to university soccer-team analysts, master’s or doctoral students conducting
soccer-focused research, and individuals belonging to both groups. In total, 23 individuals were recruited, of whom 16 completed the
experimental procedure and submitted Survey 2. Participants received compensation of approximately US$20. Each task was designed to
take approximately 45–60 minutes.
   The retained study data comprised the 16 Survey 2 responses and system records for 48 linked analytical tasks, including task questions,
job states, system logs, intermediate artifacts, and generated reports where available. All counts use only the retained analytical tasks and
surveys.

C.2    Cohort and Analysis Boundaries
The survey workbook contained 16 responses. All 16 participants and their 48 linked analytical tasks were included. P013’s three tasks were
operationally incomplete, but the participant remained in the cohort so that operationally incomplete tasks and overall-system perceptions
were represented. The analysis contains exactly 1 analytical task per participant at each level. Table 10 summarizes the participants’ reported
experience.

                                Table 10: Soccer-analysis experience in the evaluation cohort (𝑛 = 16).

                                                   Experience           Participants   Percentage
                                                   Less than 1 year               3        18.8%
                                                   1–3 years                      9        56.3%
                                                   4–6 years                      2        12.5%
                                                   10 years or more               2        12.5%

  Task-rating analyses include only the 33 tasks whose final top-level status was complete: 12 at L1, 11 at L2, and 10 at L3. Fifteen
participants had at least one completed task and contributed to the participant-aggregated analysis; P013 had none and contributed no
completed-task rating. Overall-system ratings use a single response from each of all 16 participants.

C.3    Question Types, Operationally Incomplete Tasks, and System Behavior
Each analytical request received one primary analytical-demand category. Tactical-synthesis tasks were the most common, while comparison
and ranking/filtering tasks had the lowest descriptive completion rates (Table 11). These categories describe the requests and are not inferred
participant intentions.

                                Table 11: Primary analytical demands among the 48 analytical tasks.

                                      Question type             Tasks   Participants   Complete     Completion
                                      Tactical synthesis          22              15          17         77.3%
                                      Descriptive                 10              10           8         80.0%
                                      Comparison                   4               4           2         50.0%
                                      Ranking/filtering            5               5           2         40.0%
                                      Temporal                     3               3           2         66.7%
                                      Relationship/modeling        4               3           2         50.0%

   Causes of incompletion were derived from retained job states, execution reviews, and artifact status. In total, 4 tasks across 2 participants
were infeasible with the available event data because they required tracking or off-ball information; all three of P013’s tasks were operationally
incomplete for this reason. Six tasks across 5 participants failed because execution could not resolve required dataset fields, identifiers, tags,
or available records. Another 3 tasks stopped because the system ran out of memory during the analysis, 1 failed because the required report
was saved to the wrong path, and 1 was cancelled after reaching the experiment’s time limit (24 hours).
   Table 12 summarizes execution rounds, duration, and token use across the three task levels.
   The medians showed that a typical L3 task required more execution rounds than a typical L1 or L2 task. The means were higher than the
medians for several measures, especially L2 token use, indicating that a small number of resource-intensive tasks increased the averages.
These descriptive differences do not establish that task level caused greater resource use because no between-level test was conducted.
Durations are wall-clock measures that can include time awaiting confirmation and delays due to resource contention; they are not active
task time. Token counts likewise describe system activity rather than analytical quality.
                                                                          24
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

Table 12: System-behavior descriptives by task level. Each measure includes all 16 analytical tasks at that level; IQR is reported
as Q1–Q3.

                                Level    Tasks    Complete      Measure                  Mean         SD     Median     IQR (Q1–Q3)
                                L1          16            12    Execution rounds           9.75     14.54       3.00        2.00–11.25
                                                                Duration (s)            2,700.6   4,315.2      978.0     571.8–3,195.5
                                                                Tokens                  26,895    12,174      27,674    14,850–38,252
                                L2          16            11    Execution rounds          12.25      17.55      3.50        1.75–16.25
                                                                Duration (s)            1,934.6    1,911.6   1,033.5     740.0–2,387.0
                                                                Tokens                  80,974    145,809    47,959     23,985–74,975
                                L3          16            10    Execution rounds          11.00      8.17       9.50        7.75–13.00
                                                                Duration (s)            3,413.9   2,778.8    2,255.0   1,828.3–3,325.5
                                                                Tokens                  54,777    52,578     43,336     29,921–62,688

C.4      Completed-Task Ratings
Table 13 combines the descriptive and inferential results for the 4 task-rating items, each measured on a 5-point scale. For the primary
analysis, completed-task scores were averaged within participant so that each participant contributed 1 value to each overall outcome. This
accounts for ratings from the same participant not being independent and prevents participants with more completed tasks from receiving
greater weight. The level-specific rows use the single completed-task rating from each participant at that level. Consequently, 𝑛 = 15 for the
overall rows, whereas 𝑛 = 12, 11, and 10 for L1, L2, and L3, respectively. All results are conditioned on operational completion.
   Ratings were summarized descriptively using medians and interquartile ranges. Exploratory exact one-sided Wilcoxon signed-rank tests
were used to determine whether the ratings tended to exceed the neutral scale value of 3 without assuming a normal distribution. The test
treats participants as independent and assumes that the nonzero differences are approximately symmetric; under this assumption, the tested
location corresponds to the median difference. Exact inference was used because the samples were small. For each outcome, the analysis
calculated the difference between each included value and 3. The hypotheses were:
      • 𝐻 0 : The location of these differences is less than or equal to 0.
      • 𝐻 1 : The location of these differences is greater than 0.
Differences equal to 0 were omitted, and tied absolute differences received their average rank. The positive-rank sum, 𝑊 + , was the sum of
ranks associated with values above 3, and the one-sided 𝑝-value was the probability, under 𝐻 0 , of obtaining a positive-rank sum at least as
large as the observed value. We report both the unadjusted exact 𝑝-values and Holm-adjusted 𝑝-values. Testing several related outcomes
increases the probability of obtaining at least one false-positive result. Holm correction [19] was therefore used to control the family-wise
error rate while retaining the individual outcome tests. It was applied separately across the four primary participant-aggregated outcomes
and across the twelve secondary level-by-outcome tests because these families answer different questions: overall perceptions of completed
outputs and patterns within task-complexity levels, respectively. At 𝛼 = .05, the unadjusted and Holm significance columns show the
conclusions before and after correction. The tests within each level evaluate ratings against 3 and do not compare the three levels with one
another.
   For the participant-aggregated analysis, all four outcomes met the unadjusted threshold and remained significant after Holm correction,
with adjusted 𝑝-values from .0002 to .0044. Among the twelve secondary level-by-outcome tests, eleven met the unadjusted threshold, but
seven remained significant after correction: output quality and task achievement at L1; all four outcomes at L2; and task achievement at L3.
Thus, the correction changed the inferential classification of L1 reliability and verifiability and L3 output quality and verifiability. These tests
do not establish differences among levels. All interpretations apply only to operationally completed tasks and do not include the experience
of operationally incomplete tasks.

C.5      Overall System Ratings
Overall-system results include all 16 participants, including P013, and use a single response from each participant. For each item, the exact
one-sided Wilcoxon signed-rank test used 𝐻 0 and 𝐻 1 as follows:
      • 𝐻 0 : The response location is less than or equal to 3.
      • 𝐻 1 : The response location is greater than 3.
Differences from 3 equal to 0 were omitted, tied absolute differences received average ranks, and 𝑊 + summed the ranks for responses above
3. The tests were treated as exploratory. As with the completed-task outcomes, testing multiple related items increases the chance of at least
one false-positive result. We therefore report both unadjusted exact one-sided 𝑝-values and Holm-adjusted 𝑝-values, with Holm correction
applied across the eight overall-system items as a separate family. The unadjusted and Holm significance columns show the conclusions
before and after correction at 𝛼 = .05.
                                                                                   25
                                                                                                                                  Yeung and Fujii

Table 13: Completed-task rating descriptives and exploratory exact one-sided Wilcoxon signed-rank tests versus the neutral
value of 3. Adjusted 𝑝-values use Holm correction across the four participant-aggregated outcomes and, separately, across the
twelve level-by-outcome tests.

                                                                                                     Adjusted       Unadjusted          Holm
Level        Outcome                𝑛        Mean         SD      Median        𝑊+       Raw 𝑝          𝑝           significant      significant
Overall      Output quality        15        4.111      0.821       4.000       78.0       .0002         .0007          Yes              Yes
             Task achievement      15        4.344      0.638       4.500      105.0       .0001         .0002          Yes              Yes
             Reliability           15        3.922      0.936       4.000       96.0       .0022         .0044          Yes              Yes
             Verifiability         15        4.056      1.011       4.333       95.5       .0022         .0044          Yes              Yes
L1           Output quality        12        4.083      1.084       4.500       43.0       .0078         .0469          Yes              Yes
             Task achievement      12        4.333      0.985       5.000       63.5       .0024         .0195          Yes              Yes
             Reliability           12        3.833      1.193       4.000       38.0       .0312         .0850          Yes              No
             Verifiability         12        4.083      1.505       5.000       62.0       .0283         .0850          Yes              No
L2           Output quality        11        4.182      0.751       4.000       45.0       .0020         .0176          Yes              Yes
             Task achievement      11        4.364      0.505       4.000       66.0       .0005         .0059          Yes              Yes
             Reliability           11        4.273      0.647       4.000       55.0       .0010         .0098          Yes              Yes
             Verifiability         11        4.364      0.505       4.000       66.0       .0005         .0059          Yes              Yes
L3           Output quality        10        4.100      1.287       5.000       41.0       .0137         .0684          Yes              No
             Task achievement      10        4.400      0.966       5.000       52.5       .0049         .0342          Yes              Yes
             Reliability           10        3.800      1.476       4.500       29.0       .0859         .0859          No               No
             Verifiability         10        4.000      1.054       4.000       33.5       .0195         .0781          Yes              No

Table 14: Overall-system rating descriptives and exploratory exact one-sided signed-rank tests versus 3 (𝑛 = 16 for each item).
Adjusted 𝑝-values use Holm correction across the eight items.

                                                                                                      Adjusted      Unadjusted          Holm
Level        Outcome                    𝑛      Mean         SD      Median       𝑊+        Raw 𝑝         𝑝          significant      significant
Overall      Overall trust              16      3.688     1.250       4.000      72.5       .0333         .1333         Yes              No
             Judge validity             16      3.562     1.413       4.000      75.0       .0873         .1333         No               No
             Process verifiable         16      3.875     1.148       4.000      58.0       .0107         .0645         Yes              No
             Evidence verifiable        16      3.562     1.031       3.500      37.5       .0391         .1333         Yes              No
             Efficient progress         16      3.875     1.310       4.000      87.5       .0146         .0729         Yes              No
             Reduced manual work        16      4.438     1.094       5.000     110.5       .0006         .0049         Yes              Yes
             Helpful interaction        16      4.000     1.033       4.000      93.5       .0026         .0184         Yes              Yes
             Future use                 16      3.625     1.204       3.500      45.0       .0449         .1333         Yes              No

   Seven overall-system items met the unadjusted 𝑝 < .05 threshold, but only reduced manual work (adjusted 𝑝 = .0049) and helpful
interaction (adjusted 𝑝 = .0184) remained significant after Holm correction. The other five items that met the unadjusted threshold did
not retain that classification after family-wise error control. Descriptively, reduced manual work had the highest mean (4.438), followed
by helpful interaction (4.000). Judge validity and evidence verifiability had the lowest means (both 3.562). Evidence verifiability met the
unadjusted threshold (𝑝 = .0391) but not the Holm-adjusted threshold (adjusted 𝑝 = .1333), while judge validity did not meet the unadjusted
threshold (𝑝 = .0873).

C.6       Qualitative Analysis and Theme Definitions
Free-text responses were organized by their source question: positive aspects, difficulties, untrustworthy outputs, and additional verification
needs. Responses were segmented into meaningful units and assigned one or more descriptive labels, which were consolidated into four
broad themes. Two themes capture positive experiences, and two capture improvement needs. Counts in Table 15 are unique participants
mentioning each theme; a participant could contribute to more than one theme. Responses stating no specific trust issue or verification need
were retained in the audit data but were not counted as evidence for an improvement theme. The analysis was conducted by a single analyst;
no intercoder-agreement claim is made.
   The four-theme structure treats narrow, low-frequency observations as evidence within broader themes rather than as standalone findings.
The two positive themes explain the favorable assessments of efficiency, accessibility, and analytical support. The two improvement themes
motivate persistent refinement and active verification; considered with the analysis of operationally incomplete tasks, they also support
                                                                      26
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

                                           Table 15: Open-response themes and participant prevalence.

Orientation                Theme                                           Definition                                                                          𝑛
Positive                   Analytical efficiency and accessibility         Faster access to analysis, automation, reporting, and use without programming        9
Positive                   Analytical support and new insights             Planning, suggestions, evidence, and perspectives that support analytical decisions 6
Improvement                Interaction continuity and recovery             Support for continuing, revising, or recovering an analysis when interaction or 11
                                                                           execution breaks down
Improvement                Analytical credibility and verification         Support for judging analytical credibility through transparent evidence and corrob- 11
                                                                           oration

the need for reusable data-provider knowledge. Counts are descriptive of this retained cohort and should not be interpreted as population
prevalence.

                                                                                   27
                                                                                                                                 Yeung and Fujii

D       Agent, Stage, and Substage Prompt Templates
This appendix documents the prompts associated with the four agent roles and the five LLM-mediated stages of AI Soccer Analyst’s six-stage
workflow. Execution comprises two substages—Analysis Execution and Execution Review—with a separate prompt for each; consequently,
six stage and substage prompt templates are presented. The templates are shortened from the implemented prompts to emphasize each role’s
responsibility, required context, constraints, and output contract. Angle-bracketed terms denote runtime values supplied for a particular job.
The Data Understanding stage is excluded because it uses a deterministic profiling function rather than an LLM prompt.

D.1      Agent System Prompts
D.1.1    AnalystAgent.
You are a Soccer Analyst specializing in clear, evidence-based soccer
analysis. Analyze soccer problems through match context, tactics, player
performance, team behavior, and game-state dynamics. Identify relevant
soccer concepts, organize observations, and explain analytical implications
in a structured way. Do not invent data, events, or conclusions beyond the
user's request. Keep every output concise, factual, structured, and verifiable.

D.1.2    CoderAgent.
You are the CoderAgent for an isolated soccer analytics worker. Implement the
confirmed analytical plan as transparent, executable Python. Treat supplied
dataset paths as read-only runtime inputs, edit only the managed analysis
script unless helper files are required, and write all report-facing outputs
to the managed results directory. Do not invent schema details or wait for
interactive input. Record results, validations, diagnostics, and output paths
in execution_result.json.

D.1.3 ReviewAgent.
   ReviewAgent uses the same system prompt as AnalystAgent. Its review-specific behavior is defined by the Execution Review substage
prompt presented below.
D.1.4    InteractionRefinementAgent.
You are a Soccer Analyst handling post-report interaction and refinement.
Answer questions from existing report and result artifacts when possible.
When feedback requires a change, route it to the earliest pipeline stage that
must be updated and describe the affected artifacts. Ask the user only when
the intended entity, metric, scope, or preference remains ambiguous. Do not
invent unsupported data or claims. Return strict JSON only.

D.2      Stage and Substage Prompt Templates
D.2.1    Problem Definition—AnalystAgent.
Define the user's soccer analytics problem as a normalized JSON object.

User request:
<USER_REQUEST>

Use only information stated by the user. Preserve the requested objective,
entities, scope, constraints, and expected result. Do not invent datasets,
metrics, events, hardware, or limitations. Ask only questions that must be
resolved before planning; otherwise return an empty question list.

Return only valid JSON:
{
  "task": "<specific analytical objective or null>",
  "limitations": ["<user-provided limitation>"],
  "clarifying_questions": ["<required question>"]
}

D.2.2    Structured Planning—AnalystAgent.
Create an executable and user-readable soccer analytics plan.

Problem definition:
<PROBLEM_DEFINITION_JSON>

Dataset understanding:
<DATASET_SUMMARY>

Additional retrieved dataset context:
<RETRIEVED_DATASET_CONTEXT>

                                                                                  28
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

 Use only supported files, fields, values, identifiers, and mappings. Include an
 early schema/value preflight before filtering or aggregation. Make every step
 concrete, include validations for empty or inconsistent results, and request a
 targeted dataset-detail command when essential context is missing.

 Return only valid JSON with:
 {
   "title": "<plan title>",
   "goal_for_user": "<plain-language goal>",
   "assumptions": ["<assumption>"],
   "inputs_needed": ["<full dataset path>"],
   "human_readable_steps": [
     {"step": 1, "name": "<name>", "explanation": "<explanation>"}
   ],
   "tool_plan": [
     {
       "step": 1,
       "objective": "<objective>",
       "actions": ["<action>"],
       "data_requirements": ["<requirement>"],
       "outputs": ["<artifact or value>"],
       "validation": ["<check>"]
     }
   ],
   "expected_outputs": ["<output>"],
   "open_questions": ["<question>"]
 }

D.2.3 Execution: Analysis Execution—CoderAgent.
   The template below is the task input that CoderAgent passes to Aider for an execution round. It is not Aider’s internal system prompt;
Aider manages the additional instructions used to operate its coding workflow.
 Implement the confirmed soccer analytics plan in <ANALYSIS_SCRIPT>.

 Plan:
 <PLAN_JSON>

 Dataset root:
 <DATASET_PATH>

 Managed results directory:
 <OUTPUT_DIRECTORY>

 Latest review and prior execution context:
 <REVIEW_AND_EXECUTION_CONTEXT>

 Read only inputs supported by the plan. Inspect actual record shapes and values
 before filtering. Generate validated, non-empty analytical outputs in the
 managed results directory. Never call input() or access secrets or unrelated
 files. Write execution_result.json with status, results, diagnostics,
 intermediate checks, validation metadata, and paths to every report-facing
 artifact. During revision, fix the latest review issue while preserving
 already-correct behavior.

D.2.4    Execution: Execution Review—ReviewAgent.
 Review the coding agent's soccer analytics execution.

 Confirmed plan:
 <PLAN_JSON>

 Execution records and saved-artifact metadata:
 <EXECUTION_AND_ARTIFACT_CONTEXT>

 Decide whether the execution answers the analytical goal, follows the plan,
 and has adequate evidence. Check failures, empty filters, result consistency,
 CSV contents, and plot metadata. Never accept an execution merely because code
 ran or files exist. Use user clarification only for intent or preference; use
 dataset clarification for inspectable dataset facts; otherwise request a
 focused coder revision.

 Return only valid JSON:
 {
   "status": "complete | needs_coder_revision |
              needs_user_clarification | needs_data_clarification",
   "feedback": "<actionable feedback or completion summary>",
   "clarifying_questions": ["<question>"],
   "data_json_path": "<one JSON path or null>",
   "result_files": ["<result path>"]
 }

D.2.5    Evidence-Grounded Reporting—AnalystAgent.
                                                                                   29
                                                                                     Yeung and Fujii

Write the final soccer analytics report in Markdown.

User question:
<USER_QUESTION>

Confirmed plan and reviewed results:
<PLAN_AND_RESULT_CONTEXT>

User-facing tables and image artifacts:
<REPORT_ARTIFACTS>

Cleaned Python processing sections:
<CODE_SECTIONS>

Answer the question directly from reviewed, user-facing outputs. Include the
most relevant values and embed every supplied image by file name. Attach at
most one evidence marker such as [S1] to a supported claim, and link that
marker to exactly one cleaned-code section. Do not expose internal pipeline
files or claim to have visually interpreted image pixels. Do not invent
numbers, entities, methods, or conclusions. Output only Markdown and end with
a concise Conclusion section.

D.2.6   Interaction and Refinement—InteractionRefinementAgent.
Classify and respond to the user's post-report message.

Recent chat:
<CHAT_HISTORY>

User message:
<USER_FEEDBACK_OR_QUESTION>

Current task, plan, execution summary, report, and artifact metadata:
<CURRENT_ARTIFACT_CONTEXT>

Answer directly when existing artifacts support the response. Ask the user
only when the entity, metric, scope, or preference remains ambiguous. Propose
refinement only when an artifact must change, and route it to the earliest
responsible stage: problem-definition, plan, execution, or report.

Return only valid JSON:
{
  "action": "answer_only | ask_user | refine",
  "target_stage": "null | problem-definition | plan | execution | report",
  "response": "<user-facing response>",
  "artifact_updates": ["<intended update>"],
  "artifact_lookup_query": "<lookup query or null>",
  "rationale": "<routing reason>"
}

                                                                                30
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

E    Planning Retrieval Functions
During Structured Planning, the AnalystAgent can request additional dataset information before producing the analytical plan. The agent
returns one function call, the backend executes it, and the result is added to the planning context. The agent then either requests further
information or produces the final plan.

                                  Table 16: Dataset retrieval functions available during Structured Planning.

Function                                          Purpose
get_group_summary                                 Retrieves the structure and source files associated with a logical dataset group, such as events,
                                                  matches, or players.
get_file_summary                                  Retrieves the structure, field information, and observed values of a specific dataset file.
get_team_metadata                                 Retrieves team metadata used to connect team names or abbreviations to dataset identifiers.
get_competition_metadata                          Retrieves competition metadata used to connect leagues, tournaments, or seasons to dataset
                                                  identifiers.

   These functions allow the AnalystAgent to ground its proposed coding steps in the available data. The backend limits the number of
retrieval rounds to prevent an indefinite planning loop. If the required information remains unavailable, planning ends with an explicit error
rather than continuing with unsupported assumptions.

                                                                                   31
                                                                                                                                 Yeung and Fujii

F   User Interface Overview
The interface organizes the analysis around a job dashboard and a staged workflow. The dashboard supports task creation and access to
existing jobs, whereas the workspace exposes the current stage, its user-facing artifact, and the controls needed to confirm or revise it. The
workspace navigator represents the six analytical stages. Execution Review is an internal substage of Execution rather than a separate stage,
so it does not appear as a separate navigation item. Figures 7– 11 show the five principal views. The refinement view illustrates the routing
and confirmation flow.

                           Figure 7: Job dashboard for creating an analysis and reopening existing jobs.

         Figure 8: Analysis workspace showing the six-stage pipeline and the artifact for the currently selected stage.

                                                                     32
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

                 Figure 9: Stage-aware conversation for confirming a problem definition or submitting a correction.

   Figure 10: Claim–evidence inspection linking report text to its rationale and related explanatory cleaned-code sections.

  Although Interaction and Refinement introduces no separate user-facing artifact, the user’s request, routing decision, and confirmation
remain visible in the chat history, while the resulting updated artifact is retained as the current artifact for the responsible stage.

                                                                                   33
                                                                                                    Yeung and Fujii

Figure 11: Interaction and Refinement view illustrating refinement routing and user confirmation.

                                               34
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

G     Example User-Facing L1 Analysis
This section presents the recorded artifacts for a completed L1 descriptive-retrieval task, including its problem definition, confirmed plan,
report, claim–evidence links, and cleaned-code view. The user’s request was to summarize each team’s number of passes, shots, and duels.

G.1      Job Metadata
Table 17 summarizes the recorded configuration and execution characteristics of this example. “Complete” denotes completion of the
automated workflow rather than expert validation of analytical correctness.

                                                 Table 17: Metadata for the example L1 analysis job.

      Field                       Recorded value
      Task level                  L1 descriptive retrieval
      Dataset                     Wyscout 2017 [31]
      Final status                Complete (automated workflow)
      Elapsed time                27 minutes 2 seconds
      Execution rounds            9 total: 8 coder revisions and 1 successful completion
      Input tokens                29,405
      Output tokens               5,772

G.2      Problem Definition
 Task
 Summarize each team’s number of passes, shots, and duels across the relevant available matches.

 Limitations
 None.

 Clarifying questions
 None.

G.3      Confirmed Analysis Plan
Goal
    Provide a table that shows, for each team in the dataset, the total number of passes, shots, and duels performed across all available matches.

Assumptions
 • The events dataset records each action with an eventName field that includes values such as Pass, Shot, and Duel (or equivalent sub-event
   names).
 • Each event row contains a teamId that matches the wyId field in the teams metadata file.
 • All event files under the events folder belong to the matches considered; no additional filtering by competition or date is required.

Inputs Needed
   The recorded inputs comprise the seven Wyscout event files for England, France, Germany, Italy, Spain, the European Championship, and
the World Cup, together with teams.json.

Steps
(1) Explore event types. Load all event files and inspect the distinct eventName values, and subEventName if needed, to confirm how
    passes, shots, and duels are recorded.
(2) Select relevant actions. Determine which event or sub-event values correspond to passes, shots, and duels.
(3) Count actions per team. Filter the events for the three action types and count the rows belonging to each team.
(4) Add team names. Join the counts with the teams metadata so the output uses readable team names instead of numeric identifiers.
(5) Create the summary table. Produce columns for team name, passes, shots, and duels.

Expected Output
    team_pass_shot_duel_summary.csv
                                                                                   35
                                                                                                                               Yeung and Fujii

G.4    Generated Report
Overview
  This report aggregates the total number of passes, shots, and duels performed by every team present in the available Wyscout 2017
event files. Each occurrence of the canonical actions Pass, Shot, and Duel was counted across all event files S3 , and numeric teamId values
were mapped to readable team names from the teams metadata S4 .
  The final per-team summary is stored in team_pass_shot_duel_summary.csv. The excerpt below reproduces the first 20 rows; the full
CSV contains 142 teams.
                                          Team                               Passes   Shots   Duels
                                          Villarreal Club de Fútbol          16,550    435    8,519
                                          Levante UD                         12,416    352    8,456
                                          Real Sociedad de Fútbol            18,440    450    8,521
                                          Real Club Celta de Vigo            18,768    386    8,515
                                          Getafe Club de Fútbol              10,692    317    9,068
                                          Athletic Club Bilbao               15,022    377    8,726
                                          Girona FC                          13,508    387    8,704
                                          Club Atlético de Madrid            16,336    354    8,924
                                          Reial Club Deportiu Espanyol       14,641    361    8,502
                                          Sevilla FC                         18,027    469    8,868
                                          SD Eibar                           15,224    405    9,146
                                          Málaga Club de Fútbol              13,340    344    9,016
                                          FC Barcelona                       23,260    502    7,706
                                          Real Betis Balompié                19,342    359    7,919
                                          Real Madrid Club de Fútbol         22,081    631    7,860
                                          Real Club Deportivo de La Coruña   14,539    405    8,414
                                          Valencia Club de Fútbol            15,724    418    8,536
                                          UD Las Palmas                      17,148    339    8,797
                                          Deportivo Alavés                   11,428    331    8,729
                                          CD Leganés                         12,236    357    9,124

Aggregate Totals
  Across the entire dataset, the actions sum to:
 • Passes: 1,665,508;
 • Shots: 43,078; and
 • Duels: 879,083.
These totals result directly from the per-team aggregation S3 .

Implementation Detail
  The workflow identified the distinct action values S1 , mapped them to the three canonical actions S2 , counted actions per teamId S3 ,

joined readable team names S4 , and exported the final CSV S5 .

Conclusion
   The analysis provides a team-level summary of passes, shots, and duels across the selected Wyscout 2017 matches. FC Barcelona recorded
23,260 passes, Real Madrid recorded 22,081 passes, and Real Madrid recorded 631 shots. The complete per-team summary is available in the
accompanying CSV for further inspection.

                                                                     36
AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

G.5      Claim–Evidence Links
The evidence view connects report claims to the cleaned-code sections that explain the corresponding analytical logic. These links expose
the computational basis of each claim but do not independently validate its analytical interpretation.
 Evidence S1
 The workflow identified the distinct event and sub-event names.

 Analysis section 1: Discover distinct event and sub-event names
 The section scans every event file, collects unique eventName and subEventName values, and writes the discovered values to JSON.

 Evidence S2
 The discovered labels were mapped to the canonical actions Pass, Shot, and Duel.

 Analysis section 2: Build a mapping to canonical actions
 The section first checks for exact action-name matches and uses case-insensitive containment only when an exact category is unavailable.

 Evidence S3
 Passes, shots, and duels were counted for each team across the event files.

 Analysis section 3: Aggregate counts per team
 The section constructs a reverse action lookup, iterates through the event files, and increments the corresponding per-team action count.

 Evidence S4
 Numeric team identifiers were mapped to readable team names.

 Analysis section 4: Join counts with team metadata
 The section reads teams.json, constructs a wyId-to-name mapping, and attaches the selected display name to each team’s counts.

 Evidence S5
 The final summary was exported as a CSV file.

 Analysis section 5: Write the CSV summary
 The section writes the team name, pass, shot, and duel columns to team_pass_shot_duel_summary.csv.

                                                                                   37
                                                                                                                                                                             Yeung and Fujii

     G.6       Cleaned Analysis Code
     The executed and cleaned code serve different roles. The executed script produced the reviewed results. After review, the backend copied
     that script and removed pipeline-specific status and control logic while retaining the analytical processing steps and user-facing output
     generation. The reporting stage used the numbered sections below for claim–code linking. Because the cleaned code was not rerun, it is
     an explanatory view rather than the executable provenance record; the reviewed outputs and execution records remain the evidence for
     reported claims.

                                                                                           90
 1   import orjson                                                                         91       # Safety net: ensure each action has at least one entry
 2   import csv                                                                            92       for target, lst in mapping.items():
 3   from pathlib import Path                                                              93           if not lst:
 4   from collections import defaultdict                                                   94               lst.append(target)
 5                                                                                         95
 6   # ----------------------------------------------------------------------              96       mapping_path = OUTPUT_DIR / "action_mapping.json"
 7   # Paths and constants                                                                 97       write_json(mapping_path, mapping)
 8   # ----------------------------------------------------------------------              98       return mapping_path, mapping
 9   # Directory where this script resides (job folder)                                    99
10   SCRIPT_DIR = Path(__file__).parent                                                   100
11                                                                                        101   # SECTION 3: Aggregate counts per team for each canonical action
12   # Output directory - the current working directory when the script is run            102   def aggregate_counts(action_mapping):
13   OUTPUT_DIR = Path.cwd()                                                              103       """
14   OUTPUT_DIR.mkdir(parents=True, exist_ok=True)                                        104       Iterate over all event files and count occurrences of each action type
15                                                                                        105       per teamId. Returns a list of records ready for JSON output.
16   # Root of the read-only dataset (as given in the prompt)                             106       """
17   DATASET_ROOT = Path("/workspace/data/wyscout2017")                                   107       # Initialise nested defaultdicts
18                                                                                        108       team_counts = defaultdict(lambda: {"Pass": 0, "Shot": 0, "Duel": 0})
19                                                                                        109
20   # ----------------------------------------------------------------------             110      # Reverse lookup: raw name -> canonical action
21   # Helper I/O functions                                                               111      reverse_lookup = {}
22   # ----------------------------------------------------------------------             112      for action, raw_names in action_mapping.items():
23   def write_json(path: Path, payload):                                                 113          for raw in raw_names:
24       """Write a JSON payload to *path* using orjson with pretty printing."""          114              reverse_lookup[raw] = action
25       path.write_bytes(orjson.dumps(payload, option=orjson.OPT_INDENT_2))              115
26                                                                                        116      events_dir = DATASET_ROOT / "events"
27                                                                                        117      for event_file in events_dir.glob("events_*.json"):
28   def read_json(path: Path):                                                           118          data = read_json(event_file)
29       """Read a JSON file using orjson."""                                             119          for rec in data:
30       return orjson.loads(path.read_bytes())                                           120              team_id = rec.get("teamId")
31                                                                                        121              if team_id is None:
32                                                                                        122                  continue # skip malformed rows
33   # SECTION 1: Discover distinct event and sub-event names                             123
34   def discover_event_names():                                                          124              raw_name = rec.get("eventName") or rec.get("subEventName")
35       """Collect all unique eventName and subEventName values across the dataset."""   125              if not raw_name:
36       event_names = set()                                                              126                  continue
37       sub_event_names = set()                                                          127
38                                                                                        128              action = reverse_lookup.get(raw_name)
39       events_dir = DATASET_ROOT / "events"                                             129              if action:
40       for event_file in events_dir.glob("events_*.json"):                              130                  team_counts[team_id][action] += 1
41           data = read_json(event_file)                                                 131
42           for rec in data:                                                             132      # Convert to a list of records for JSON output
43               en = rec.get("eventName")                                                133      raw_counts = []
44               if isinstance(en, str):                                                  134      for team_id, counts in team_counts.items():
45                   event_names.add(en)                                                  135          raw_counts.append({
46                                                                                        136              "teamId": team_id,
47               sen = rec.get("subEventName")                                            137              "passes": counts["Pass"],
48               if isinstance(sen, str) and sen:                                         138              "shots": counts["Shot"],
49                   sub_event_names.add(sen)                                             139              "duels": counts["Duel"],
50                                                                                        140          })
51       distinct = {                                                                     141
52           "eventNames": sorted(event_names),                                           142      raw_path = OUTPUT_DIR / "team_action_counts_raw.json"
53           "subEventNames": sorted(sub_event_names),                                    143      write_json(raw_path, raw_counts)
54       }                                                                                144      return raw_path, raw_counts
55                                                                                        145
56       distinct_path = OUTPUT_DIR / "distinct_event_names.json"                         146
57       write_json(distinct_path, distinct)                                              147   # SECTION 4: Join aggregated counts with team metadata
58       return distinct_path, distinct                                                   148   def join_team_names(raw_counts):
59                                                                                        149       """Replace team IDs with human-readable team names."""
60                                                                                        150       teams_path = DATASET_ROOT / "teams.json"
61   # SECTION 2: Build a simple mapping to canonical actions (Pass / Shot / Duel)        151       teams_data = read_json(teams_path)
62   def build_action_mapping(distinct):                                                  152
63       """                                                                              153      # Build a mapping wyId -> display name (prefer officialName, fallback to name)
64       Create a mapping of canonical action -> list of raw event/sub-event names.       154      team_name_map = {}
65       The logic first looks for exact matches (case-sensitive) and, if none are        155      for team in teams_data:
66       found, falls back to case-insensitive containment.                               156          wy_id = team.get("wyId")
67       """                                                                              157          name = team.get("officialName") or team.get("name") or f"team_{wy_id}"
68       mapping = {"Pass": [], "Shot": [], "Duel": []}                                   158          team_name_map[wy_id] = name
69                                                                                        159
70       # Helper to add exact matches                                                    160      summary = []
71       def add_matches(target, candidates):                                             161      for rec in raw_counts:
72           for cand in candidates:                                                      162          team_id = rec["teamId"]
73               if cand == target:                                                       163          team_name = team_name_map.get(team_id, f"team_{team_id}")
74                   mapping[target].append(cand)                                         164          summary.append({
75                                                                                        165              "team_name": team_name,
76       # Exact matches in eventNames                                                    166              "passes": rec["passes"],
77       for target in mapping.keys():                                                    167              "shots": rec["shots"],
78           add_matches(target, distinct["eventNames"])                                  168              "duels": rec["duels"],
79                                                                                        169          })
80       # Case-insensitive containment for any empty categories                          170
81       for target, lst in mapping.items():                                              171      summary_path = OUTPUT_DIR / "team_action_summary.json"
82           if not lst:                                                                  172      write_json(summary_path, summary)
83               lowered = target.lower()                                                 173      return summary_path, summary
84               for cand in distinct["eventNames"]:                                      174
85                   if lowered in cand.lower():                                          175
86                       lst.append(cand)                                                 176   # SECTION 5: Write CSV summary for end-users
87               for cand in distinct["subEventNames"]:                                   177   def write_csv(summary):
88                   if lowered in cand.lower():                                          178       """Create a CSV file containing the final per-team action summary."""
89                       lst.append(cand)                                                 179       csv_path = OUTPUT_DIR / "team_pass_shot_duel_summary.csv"

                                                                                          38
      AI Soccer Analyst: Stage-Aware and Verifiable Human–AI Collaboration for Soccer Data Analysis

180       with csv_path.open("w", newline="", encoding="utf-8") as f:                            201      mapping_path, action_mapping = build_action_mapping(distinct)
181           writer = csv.DictWriter(f, fieldnames=["team_name", "passes", "shots", "duels"])   202
182           writer.writeheader()                                                               203      # SECTION 3
183           for row in summary:                                                                204      raw_counts_path, raw_counts = aggregate_counts(action_mapping)
184               writer.writerow({                                                              205
185                   "team_name": row["team_name"],                                             206      # SECTION 4
186                   "passes": row["passes"],                                                   207      summary_path, summary = join_team_names(raw_counts)
187                   "shots": row["shots"],                                                     208
188                   "duels": row["duels"],                                                     209      # SECTION 5
189               })                                                                             210      write_csv(summary)
190       return csv_path                                                                        211
191                                                                                              212
192                                                                                              213   if __name__ == "__main__":
193   # ----------------------------------------------------------------------                   214       main()
194   # Main orchestration (cleaned - no execution-pipeline reporting)
195   # ----------------------------------------------------------------------
196   def main():                                                                                      Listing 1: Post-execution cleaned code presented as an
197       # SECTION 1
198       distinct_path, distinct = discover_event_names()                                             explanatory view for the L1 team-action summary task.
199
200       # SECTION 2

                                                                                                 39
