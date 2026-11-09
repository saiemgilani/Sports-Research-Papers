# Semantic Action Graph: A Shared Representation for Agent Grounding and Human Interpretation of Sports Highlights

- arXiv: https://arxiv.org/abs/2609.20768
- Authors: Tica Lin, Deepak Chandran, Gauri Jagatap, Chen Chen, Andrea Fanelli, David Gunawan, Josh Kimball

---

                                                                 Accepted for publication at IEEE VIS 2026 Workshop on GenAI, Agents, and the Future of VIS.



                                        Semantic Action Graph: A Shared Representation for Agent Grounding and
                                                       Human Interpretation of Sports Highlights
                                                           Tica Lin        *, Deepak Chandran        , Gauri Jagatap , Chen Chen                      †, Andrea Fanelli       ,
                                                                                            David Gunawan , and Josh Kimball
                                                                                                           Dolby Laboratories
arXiv:2609.20768v2 [cs.HC] 4 Oct 2026




                                               Figure 1: We design the semantic action graph as a shared representation for sports highlights, expressing a match as performer,
                                               action, recipient, moment, and state nodes joined by semantic edges. SportSAGE instantiates it with a highlight agent (bottom) to
                                               compute statistics, compose narratives, and return clips as node sequences with frame boundaries read from the graph. The same
                                               structure drives the interface (top) for filtering (a) and navigating (b) the graph. Viewers can specify preferred narrative focus (c) and
                                               view the resulting personalized highlights (d).

                                        A BSTRACT                                                                           The schema demonstrates three key properties: 1) connected event
                                        Generative agents are increasingly used to select and narrate video                 sequences, 2) a shared, closed vocabulary, and 3) frame-addressable
                                        highlights, but they typically operate over unstructured or frame-                  moments, making it suitable to serve two consumers at once: an
                                        level representations. Their output is consequently difficult for                   agentic pipeline that composes narrated highlights, and a visual
                                        a viewer to verify and steer toward individual preferences. We                      interface through which viewers query and inspect the same structure.
                                        present the semantic action graph, a lightweight domain schema that                 We instantiate it in SportSAGE, a design probe pairing a four-module
                                        represents a sports match as performer, action, recipient, moment,                  highlight pipeline with a graph interface, and report feedback from
                                        and state nodes connected by role, temporal, and outcome edges.                     12 soccer fans. Participants were satisfied with the quality of the
                                                                                                                            generated highlights and narratives, and used the graph interface to
                                            * T. Lin, D. Chandran, G. Jagatap, A. Fanelli, D. Gunawan, and J. Kimball       search, navigate, and interpret the match highlights. These results
                                        are with Dolby Laboratories. E-mail: tica.lin@dolby.com                             provide early evidence that one small, human-readable schema can
                                            † C. Chen is now with XPENG.                                                    ground agent generation and support human interpretation at the
                                                                                                                            same time.

                                                                                                                            Keywords: Graph-Based Video Representation, Highlight Genera-
                                                                                                                            tion, Agentic Systems, Human-AI Interaction, Sports Visualization.



                                                                                                                        1
                        Accepted for publication at IEEE VIS 2026 Workshop on GenAI, Agents, and the Future of VIS.


1 I NTRODUCTION                                                                  as commentator speech and crowd noise [25], modeled viewer
Sports highlights are central to how fans engage with a game beyond              arousal [12], and multimodal excitement features [20]. More re-
the live match, condensing key moments into a reel with narrative                cently, perception models have been trained to perform action spot-
that explains their significance. Yet fans differ in what they want              ting over large annotated datasets [7, 11] to identify key moments
to see and how they want it framed—a single manually edited reel                 in a match. Apostolidis et al. [3] survey the wider summarization
can’t serve everyone. As a result, current highlights often miss the             literature. However, the highlight these approaches return is a ranked
moments individual fans care about, offer little narrative context,              set of moments rather than a composed sequence, limiting viewer
and provide no effective way to find a specific play.                            interpretability and control.
   Recent systems use large language and vision-language models                      Language models have recently been applied to the same task.
to automatically generate highlights and narratives. One line of                 Structured representations such as scene graphs improve video un-
work selects or ranks the moments worth showing, by scoring frame                derstanding [13, 30] and reduce hallucination [31], though in these
importance [17], combining domain metrics with contextual reason-                systems the structure remains internal to the model. Our work ex-
ing [15], or assisting an editor with language-based retrieval [29].             tends this line by defining an action-centric schema consumed by
Another line of work generates language to accompany footage al-                 both the generative pipeline and the viewer.
ready chosen, such as live commentary [2] or answers to questions
about a play [16, 24]. These two halves are usually developed in                 2.2    Interfaces for casual game exploration
isolation, and systems that produce both together are limited [4].              Visualization research makes video navigable by pairing it with
   Because the generated prose isn’t linked to the underlying events,           structured metadata. Matejka et al. [19] presented Video Lens, which
fans can’t verify its accuracy or customize results meaningfully.               indexes baseball footage by attributes such as pitch type and player
If the narrative mentions a defense-splitting pass, nothing in the              so fans can filter moments and play them back. Pavel et al. [21, 22]
interface confirms it happened, who made it, or when. A fan wanting             structure lecture and film video through aligned transcripts, and
an earlier starting point or the passes leading to shots rather than            Deng et al. [8] reduce the effort needed to annotate racket sports
the shots themselves, has no way to specify this, since the system              events for such structured event indices.
doesn’t expose those events. Existing pipelines work over frame                    Sports visualization has produced interfaces for both analysts and
embeddings and text tokens, which enable generation but aren’t                  fans. SoccerStories [23] supported visual analysis of soccer phases,
units a person can inspect or reference.                                        and Stein et al. [28] combined movement data with video. Closer to
   We attribute both limitations to the lack of a shared intermediate           casual viewing, Lin et al. [18] augmented sports video with embed-
representation. Visualization tools have produced structured video              ded visualizations, and Lee et al. [16] answered tactical questions
indices that support browsing [8, 19], but generative models don’t              with narratives and embedded visualization. These systems show
consume them. Agentic pipelines that build explicit structures keep             that structured metadata makes video navigable and supports fans
them internal, discarding them before output reaches the viewer [13,            engage with game context interactively. The structures they expose,
30]. A representation that simultaneously grounds the AI pipeline               however, are built for human retrieval alone. Our work explores a
and supports human interpretation remains absent.                               shared structure for both generative pipeline and human interfaces.
   To bridge the gap, we present the semantic action graph, a
lightweight schema that represents a sports match as performer,                  3     F ORMATIVE S TUDY
action, recipient, moment, and state nodes connected by role, tem-               To understand how fans experience current highlights, we conducted
poral, and outcome relations. Designed for both agent and human                  30-minute semi-structured interviews with six soccer fans (ages 18-
consumers, the graph captures connected event sequences using                    55; 1 female, 5 male), including one casual viewer (F2), two regular
a closed vocabulary and frame-addressable moments. An agentic                    fans (F1, F5), three die-hard fans (F3, F4, F6). Interviews covered
pipeline can use it to compute match statistics, compose narratives,             viewing habits, highlight consumption, difficulties in finding specific
and retrieve clips, while a visual interface renders the identical struc-        content, and desired features. Recordings were transcribed and
ture for viewers to filter, inspect, and navigate. We demonstrate                analyzed using reflexive thematic analysis [6], with two researchers
the schema through SportSAGE, a design probe for soccer high-                    iteratively refining themes to consensus. Several gaps in current
lights that pairs a four-module agentic pipeline with a graph-based              highlights impede fans’ engagement, which we categorized below.
interface. Grounded in three design goals derived from a formative                  Content Gap. Participants reported that highlights omit surround-
study with six fans, SportSAGE takes structured match event data                 ing events and the build-up to key moments. Four of six preferred
from an official league feed [9] and produces personalized narrated              seeing the actions leading to a goal over the finish alone: F3 wanted
highlights that viewers can verify and navigate.                                 a clip to play “from when the action starts, the attack phase or
   We collected feedback from 12 soccer fans using SportSAGE                     previous defense phase, not just the actual moment of the goal.”
on a professional match. Participants valued receiving customized                   Narrative Gap. Participants also wanted to understand why
highlights with varying narrative focuses of the same match, and                 a moment mattered, not just what happened. There is often an
used the graph layer to inspect generated clips and check the narra-             issue with missing broader context and storytelling components:
tives against the video. These results serve as early evidence that             “Sometimes the highlight is just the moment of a goal, but I didn’t
the schema can ground agentic highlight creation and guide human                 know there was a red card before that” (F1).
interaction with its output.                                                        Personalization Gap. Current highlights use a one-size-fits-all
   This work contributes the following: (1) the semantic action                  approach that ignores individual preferences. Most fans we inter-
graph, a domain schema that serve both an agentic pipeline and                   viewed have clear preferences in highlight narrative types: “There
a viewer-facing interface; (2) SportSAGE, a design probe demon-                  is no ability to walk in onto a particular player. I’d love to be able
strating the schema in soccer highlight generation; and (3) user                 to be more personalized” (F4); “Everyone’s different. People care
feedback on narrative personalization and the value of a graph layer             about the big moments but I kind of want to see the build-up” (F5).
for interpreting and interacting with generated video content.
                                                                                    Discovery Gap. Locating a specific moment was reported as
2 R ELATED W ORK                                                                 difficult, particularly for less prominent events: “if it’s a small
                                                                                 moment, I usually have a hard time, like a penalty or a smaller
2.1 Sports highlight generation                                                  moment that’s not normally captured” (F1).
Automatically extracting highlights from sports video has been stud-                These gaps translate into three requirements on the underlying
ied for over two decades, through proxies for excitement such                    representation, which we use as design goals below. G1: Play



                                                                            2
                       Accepted for publication at IEEE VIS 2026 Workshop on GenAI, Agents, and the Future of VIS.




Figure 2: (a) Semantic Action Graph schema. Five node types record who acted, what occurred, who was affected, when it occurred, and what
game state resulted; five edge types carry role, sequence, and outcome. (b) A goal sequence expressed in the schema. The then edge chains
the action sequence, including two passes, the tackle, and the shot that produced the score.

should be represented as connected sequences rather than isolated            the schema. This property makes the boundary of the system’s capa-
moments, so that build-up and consequence are available to both the          bility explicit while allowing structured extension, such as adding
system and the viewer. G2: The units the system reasons over should          new action types (e.g., different foul types) or descriptors for players
form a vocabulary viewers can also use to express preferences. G3:           (e.g., appearance, speed).
Individual moments should be addressable, so that a viewer can                  Frame-addressable moments (G3). Each Moment node carries
reach a specific event directly rather than by scrubbing.                    a frame index of the event from the source feed, providing clear clip
                                                                             boundary when composing a highlight. A highlight generation agent
4     S EMANTIC ACTION G RAPH                                                can directly reference the moment nodes from the desired action
4.1    Schema                                                                sequence for accurate timestamps, avoiding incorrect generated time
                                                                             codes. For the viewer, the same property lets the viewer navigate the
A match is represented as a graph over five node types, as shown             video through meaningful structure,(Fig. 1b), linking generated units
in Fig. 2a. The      Performer nodes record who carried out an               to the footage to verify the narrative or localize specific moment
action and the     Recipient nodes who was affected by it, both              effectively.
drawn from the match roster. The Action nodes record what                       Overall, the semantic action graph schema builds upon the com-
occurred, drawn from a sport-specific catalog (e.g., for soccer -            mon metadata that professional event feed carries (e.g., IPTC [14])
Tackle, Foul, ShotOnTarget, Save, Score, YellowCard, and others).            and adds two structural relations that metadata alone does not ex-
The Moment nodes carry temporal context in the form of game                  press. First, the then and produce relations make explicit the tempo-
clock, video time, and frame index. The State nodes carry the                ral and causal relationships between distinct action records, i.e., one
game state an action produced, such as the score.                            action follows from another, and that an action changes the game
   Five edge types connect these nodes with semantic relationships.          state. Second, the sport-specific vocabulary is fixed in advance and
Three encode the roles within a single event: perform ( → )                  can be retargeted — participants, actions, sequence, and outcome are
links a performer to an action, affect ( → ) links an action to              shared across most sports, while event granularity and narrative style
its recipient, and happen ( → ) links a moment to the action                 are not, so a long build-up chain in soccer and a single last-minute
occurring at it. The remaining two carry structure across events:            shot in basketball are both expressible. Our contribution is not a new
produce ( → ) links an action to the state it results in, and then           data model but a minimal relational layer that connects atomic event
( → ) chains actions that are consecutive within a possession.               records to narrative structure.
Fig. 2b shows a goal expressed in the schema, in which a pass, a                Additionally, the schema is intentionally small. It does not repre-
second pass, a tackle, and a shot are linked by then edges, ending in        sent spatial position, formation, or tactical intent, which matter for
a produce edge to the resulting score.                                       analysis but are not required to cover much of the descriptive content
                                                                             of sports commentary. The schema therefore serves as a base for
4.2    Design Properties                                                     agentic highlight generation from metadata that professional feeds
The schema demonstrates three key properties informed by the de-             already provide, and it can be extended when spatial data such as
sign goals in Sec. 3.                                                        player location, speed, or formation are available.
   Connected event sequences (G1). With explicit edge definition
in the graph, i.e. then edges connecting discrete actions, a highlight       5     S PORT SAGE: A H IGHLIGHT G ENERATION P IPELINE
can be defined as a traversal of the graph rather than as a fixed            We built SportSAGE as a design probe to explore how a seman-
time window around a detected event. For example, a highlight                tic action graph can support both agentic highlight generation and
generation pipeline can add build-ups to the goal event by chaining          viewer-facing interpretation.
back to a possession boundary rather than determining how many
seconds before a goal as a parameter. The same edge structure also
                                                                             5.1    Graph Construction and Agentic Pipeline
gives the viewer a compact representation of what a clip contains
and in what order, which aligns with how a human viewer describes            We constructed the semantic action graph for a selected soccer match
the event sequences.                                                         (i.e., 2024-2025 Pokal Cup Finale match between VfB Stuttgart
   A shared, closed vocabulary (G2). In our schema, action nodes             and Arminia Bielefeld [1]) from official league match event data.
come from a fixed catalog of types, and performer and recipient              The raw event logs contain timestamped, frame-aligned records of
nodes from the match roster. Because the entities and events are de-         actions, performers, and recipients at roughly 2-5 second granularity.
fined in advance, the pipeline’s generation freedom lies in phrasing         Such format is routinely produced for professional soccer [5]. We
rather than in facts. The same catalog is also presented to the viewer       mapped the record onto the closed action catalog, including 13
as the filter panel (Fig. 1a), so the system and the user shared same        actions covering possess, pass, tackle, foul types, shot types, kick
descriptive units. This closure also bounds what a viewer can ask for.       types, and others. A 96-minute match yields 1,330 action nodes.
A request outside the catalog, such as one about crowd celebrations,             The SportSAGE highlight pipeline is composed of four modules
has no corresponding node and cannot be satisfied without extending          that operate on these records, as shown in Fig. 3.



                                                                         3
                       Accepted for publication at IEEE VIS 2026 Workshop on GenAI, Agents, and the Future of VIS.




Figure 3: SportSAGE Agentic Pipeline. All four modules operate on semantic action graph data; none reads video. 1. Game Analyzer computes
match statistics. 2. Narrative Creator generates narratives tailored to user preferences. 3. Highlight Generator assembles 10 candidate
clips bounded by Moment frame indices. 4. Ranking Agent selects the top 5 and provides feedback to (3). Modules 2-4 are LLM agents.

   1) Game Analyzer is a deterministic component. It takes the                   AI highlight and narrative quality. Participants were satisfied
graph as a CSV conforming to the schema, and computes match                   with the highlight sets produced by the agentic pipeline. On a 7-point
statistics and per-player activity profiles, removing arithmetic from         scale (1 = poor, 7 = excellent), they rated overall highlight quality
the language model [26].                                                      positively for both the default set (M = 5.25) and the set matched
   2) Narrative Creator takes the computed statistics with a cho-             to their chosen narrative focus (M = 5.25). Perceived quality was
sen narrative preference (action-focused, tactical analysis, player-          therefore unchanged by personalization. The difference appeared
centric, casual-viewing), and generates a highlight narrative using           in preference, where participants favored the customized narrative
templates built around common soccer archetypes, such as Momen-               over the default (M = 5.92). This is consistent with the narrative and
tum Shifts, Tactical Masterclass, and Individual Brilliance.                  personalization needs found in the formative study. They praised
   3) Highlight Generator assembles ten candidate clips, each                 clip coverage and accuracy (“it showed enough of the buildup to be
a set of nodes whose frame indices give the clip boundaries.                  engaging, the pivotal moment and some of the celebration” (P4))
   4) Ranking Agent returns a top-five set and, through an optional           and valued the accompanying narrative for letting them “follow the
iteration-limited reflection step [27], feeds corrective feedback back.       progression of events easily” (P7). Distinct narrative focus mattered
   The three generative modules use Claude 3.5 Sonnet. Each re-               for both die-hard and casual fan: “This [tactical] type of description
ceives the Game Analyzer’s summaries and a pool of candidate                  is more favorable for me when I want to search and watch highlights
clips identified by their constituent records, without accessing the          or game re-cap” (P8) and “It makes it easy to watch for a casual
original video. The schema thus serves as the sole interface between          viewer like me who isn’t too invested in soccer” (P2).
the agent and the match. Statistics are computed deterministically,              Graph layer usefulness. Participants interpreted the semantic
and clip boundaries derived from Moment frame indices rather than             action graph correctly and used it to check narratives against the
generated timecodes, ensuring the highlight output is factual.                video and to recover game context. They rated the interface useful
                                                                              (M = 5.96) and completed the three tasks reliably, including filtering
5.2 Interface
                                                                              shot events (12/12), locating a specific player action (11/12), and
The interface (Fig. 1) exposes the same schema through four com-              interpreting video events from the graph (11/12). In particular,
ponents. A search panel filters by action type, player, and period,           participants valued the customizable nature and the granularity of the
using the catalog of Sec. 4. A node-link view renders the events in           graph, which support fans “breaking down highlights to understand
the current filter result or generated clip along a timeline, encoding        the plays better” (P2).
team membership in node borders and player identity in thumbnails;               These preliminary insights suggest that AI highlights grounded in
selecting a node moves the video to that frame. A personalization             the semantic action graph yield satisfying quality and have the poten-
panel offers four narrative focuses (Action, Tactical, Casual, Player)        tial to address the content, narrative, personalization, and discovery
and team/player preferences. A highlight list presents each gen-              gaps found in our formative study.
erated clip, and selecting a clip updates the node-link view to its
constituent events. The frontend uses React with Cytoscape.js [10].
                                                                              7   C ONCLUSION & F UTURE W ORK
6 U SER F EEDBACK
We collected feedback from 12 soccer fans (2 female, 10 male;                 We introduced the semantic action graph, a lightweight schema
ages 18-54; 6 casual, 3 regular, 3 die-hard) in a 40-minute online            that represents matches as categorized, temporally ordered event
session on SportSAGE highlights and the graph utility. Participants           sequences shared by both the agentic pipeline and the viewer-facing
first viewed both a default highlight set of the soccer match (five           interface, making generative output in a narrative-rich domain more
clips) and a customized highlight set with their preferred narrative          steerable and navigable. SportSAGE applies this schema to soccer
focus (Tactical, Casual, or Player). They provided feedback on                highlight generation, enabling personalized narratives that viewers
their preference and perceived quality of the highlights. They then           can verify and navigate through the graph interface.
used the SportSAGE interface to examine the AI highlight clips with              As a design probe, SportSAGE was evaluated on a single match
semantic action graph and perform reasoning tasks on the interface,           with one model and no unstructured baseline, so we cannot yet at-
including locating specific game moments from graph, and linking              tribute participants’ satisfaction to the shared representation itself.
the highlight events to its semantic structure.                               Future work should compare against an unstructured baseline, ex-
    We summarized user feedback into two aspects: 1) AI highlight             tend the schema with spatial and tactical attributes, and explore
and narrative quality, and 2) graph layer usefulness.                         constructing the graph directly from video rather than official feeds.



                                                                          4
                          Accepted for publication at IEEE VIS 2026 Workshop on GenAI, Agents, and the Future of VIS.


ACKNOWLEDGMENTS                                                                       [18] T. Lin, C. Zhu-Tian, Y. Yang, D. Chiappalupi, J. Beyer, and H. Pfister.
                                                                                           The quest for omnioculars: Embedded visualization for augmenting
We acknowledge the Deutsche Fußball Liga (DFL) for granting                                basketball game viewing experiences. IEEE transactions on visualiza-
access to official match data and video footage used in this research.                     tion and computer graphics, 29(1):962–972, 2022. 2
We also thank the interviewees in our formative study for sharing                     [19] J. Matejka, T. Grossman, and G. Fitzmaurice. Video lens: Rapid play-
their experiences.                                                                         back and exploration of large video collections and associated meta-
                                                                                           data. In Proc. ACM Symp. on User Interface Software and Technology
                                                                                           (UIST), pp. 541–550. ACM, 2014. doi: 10.1145/2642918.2647366 2
R EFERENCES                                                                           [20] M. Merler, K.-N. C. Mac, D. Joshi, Q.-B. Nguyen, S. Hammer, J. Kent
 [1] 2024-25 German Cup, Final. ESPN German Cup Final, 2025. [Online;                      et al. Automatic curation of sports highlights using multimodal excite-
     accessed 13-November-2025]. 3                                                         ment features. IEEE Trans. Multimedia, 21(5):1147–1160, 2019. doi:
 [2] P. Andrews, O. E. Nordberg, S. Zubicueta Portales, N. Borch,                          10.1109/TMM.2018.2876046 2
     F. Guribye, and K. Fujita. AiCommentator: A multimodal conver-                   [21] A. Pavel, D. B. Goldman, B. Hartmann, and M. Agrawala. SceneSkim:
     sational agent for embedded visualization in football viewing. In Proc.               Searching and browsing movies using synchronized captions, scripts
     Int. Conf. on Intelligent User Interfaces (IUI), pp. 14–34, 2024. doi: 10             and plot summaries. In Proc. ACM Symp. on User Interface Soft-
     .1145/3640543.3645148 2                                                               ware and Technology (UIST), pp. 181–190. ACM, 2015. doi: 10.1145/
 [3] E. Apostolidis, E. Adamantidou, A. I. Metsai, V. Mezaris, and I. Patras.              2807442.2807502 2
     Video summarization using deep neural networks: A survey. Proc.                  [22] A. Pavel, C. Reed, B. Hartmann, and M. Agrawala. Video digests: A
     IEEE, 109(11):1838–1863, 2021. doi: 10.1109/JPROC.2021.3117472                        browsable, skimmable format for informational lecture videos. In Proc.
     2                                                                                     ACM Symp. on User Interface Software and Technology (UIST), pp.
 [4] A. Barua, K. Benharrak, M. Chen, M. Huh, and A. Pavel. Lotus:                         573–582. ACM, 2014. doi: 10.1145/2642918.2647400 2
     Creating short videos from long videos with abstractive and extractive           [23] C. Perin, R. Vuillemot, and J.-D. Fekete. SoccerStories: A kick-off for
     summarization. In Proc. Int. Conf. on Intelligent User Interfaces (IUI),              visual soccer analysis. IEEE Trans. Vis. Comput. Graph., 19(12):2506–
     pp. 967–981, 2025. 2                                                                  2515, 2013. doi: 10.1109/TVCG.2013.192 2
 [5] M. Bassek, R. Rein, H. Weber, and D. Memmert. An integrated                      [24] J. Rao, Z. Li, H. Wu, Y. Zhang, Y. Wang, and W. Xie. Multi-agent
     dataset of spatiotemporal and event data in elite soccer. Scientific Data,            system for comprehensive soccer understanding. In Proc. ACM Int.
     12(1):195, 2025. doi: 10.1038/s41597-025-04505-y 3                                    Conf. on Multimedia, pp. 3654–3663, 2025. doi: 10.1145/3746027.
 [6] V. Braun and V. Clarke. Using thematic analysis in psychology. Qual-                  3755144 2
     itative Research in Psychology, 3(2):77–101, 2006. doi: 10.1191/                 [25] Y. Rui, A. Gupta, and A. Acero. Automatically extracting highlights
     1478088706qp063oa 2                                                                   for TV baseball programs. In Proc. ACM Int. Conf. on Multimedia, pp.
 [7] A. Deliège, A. Cioppa, S. Giancola, M. J. Seikavandi, J. V. Dueholm,                  105–115. ACM, 2000. doi: 10.1145/354384.354443 2
     K. Nasrollahi et al. SoccerNet-v2: A dataset and benchmarks for                  [26] T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, E. Hambro
     holistic understanding of broadcast soccer videos. In Proc. IEEE/CVF                  et al. Toolformer: Language models can teach themselves to use tools.
     CVPR Workshops, pp. 4503–4514, 2021. doi: 10.1109/CVPRW53098.                         In Advances in Neural Information Processing Systems, vol. 36, pp.
     2021.00508 2                                                                          68539–68551, 2023. 4
 [8] D. Deng, J. Wu, J. Wang, Y. Wu, X. Xie, Z. Zhou et al. EventAn-                  [27] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao. Reflex-
     chor: Reducing human interactions in event annotation of racket sports                ion: Language agents with verbal reinforcement learning. In Advances
     videos. In Proc. CHI Conf. on Human Factors in Computing Systems,                     in Neural Information Processing Systems, vol. 36, pp. 8634–8652,
     pp. 1–13, 2021. doi: 10.1145/3411764.3445431 2                                        2023. 4
 [9] Deutsche Fußball Liga (DFL). Official match data. https://                       [28] M. Stein, H. Janetzko, A. Lamprecht, T. Breitkreutz, P. Zimmermann,
     www.dfl.de/en/topics/match-data/official-match-data/,                                 B. Goldlücke et al. Bring it to the pitch: Combining video and move-
     2024. Accessed: 2025-11-13. 2                                                         ment data to enhance team sport analysis. IEEE Trans. Vis. Comput.
[10] M. Franz, C. T. Lopes, G. Huck, Y. Dong, O. Sumer, and G. D. Bader.                   Graph., 24(1):13–22, 2018. doi: 10.1109/TVCG.2017.2745181 2
     Cytoscape.js: A graph theory library for visualisation and analysis.             [29] B. Wang, Y. Li, Z. Lv, H. Xia, Y. Xu, and R. Sodhi. LAVE: LLM-
     Bioinformatics, 32(2):309–311, 2016. doi: 10.1093/bioinformatics/                     powered agent assistance and language augmentation for video editing.
     btv557 4                                                                              In Proc. Int. Conf. on Intelligent User Interfaces (IUI), pp. 699–714,
[11] S. Giancola, M. Amine, T. Dghaily, and B. Ghanem. SoccerNet: A                        2024. doi: 10.1145/3640543.3645147 2
     scalable dataset for action spotting in soccer videos. In Proc. IEEE/CVF         [30] J. Yang, W. Peng, X. Li, Z. Guo, L. Chen, B. Li et al. Panoptic video
     CVPR Workshops, pp. 1792–1810, 2018. doi: 10.1109/CVPRW.2018.                         scene graph generation. In Proc. IEEE/CVF CVPR, 2023. doi: 10.
     00223 2                                                                               1109/CVPR52729.2023.00634 2
[12] A. Hanjalic. Adaptive extraction of highlights from a sport video based          [31] S. Yin, C. Fu, S. Zhao, T. Xu, H. Wang, D. Sui et al. Woodpecker: Hal-
     on excitement modeling. IEEE Trans. Multimedia, 7(6):1114–1122,                       lucination correction for multimodal large language models. Science
     2005. doi: 10.1109/TMM.2005.858397 2                                                  China Information Sciences, 67(12), 2024. doi: 10.1007/s11432-024
[13] Z. Huang, Y. Ji, X. Wang, N. Mehta, T. Xiao, D. Lee et al. Building a                 -4251-x 2
     mind palace: Structuring environment-grounded semantic graphs for
     effective long video analysis with LLMs. In Proc. IEEE/CVF CVPR,
     2025. doi: 10.48550/arXiv.2501.04336 2
[14] International Press Telecommunications Council. IPTC sport schema.
     https://sportschema.org/, 2024. Version 1.1, approved October
     2024. Licensed CC-BY 4.0. 3
[15] J. Kang, S. Kwon, J. Lee, and B.-H. Kim. DIAMOND: An LLM-
     driven agent for context-aware baseball highlight summarization. arXiv
     preprint arXiv:2506.02351, 2025. doi: 10.48550/arXiv.2506.02351 2
[16] C. Lee, T. Lin, H. Pfister, and Z. Chen. Sportify: Question answering
     with embedded visualizations and personified narratives for sports
     video. IEEE Trans. Vis. Comput. Graph., 31(1):12–22, 2025. doi: 10.
     1109/TVCG.2024.3456332 2
[17] M. Lee, D. Gong, and M. Cho. Video summarization with large
     language models. In Proc. IEEE/CVF CVPR, pp. 18981–18991, 2025.
     2



                                                                                  5
