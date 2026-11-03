<!-- source: 2026 - SoccerNet-FoulRet Retrieving Semantically Similar Soccer Foul Videos - Arthur et al.pdf -->
<!-- arXiv:2610.09742, 2026-10-07 · abstract from the arXiv API; PDF saved under library/ -->
<!-- arXiv roundup 2026-11-03 -->

# SoccerNet-FoulRet: Retrieving Semantically Similar Soccer Foul Videos

**Jacobus Arthur, Ahmad Sait, Batool Hani, Merey Ramazanova, Jan Held, Marc Van Droogenbroeck, Bernard Ghanem, Anthony Cioppa, Silvio Giancola**

arXiv:[2610.09742](https://arxiv.org/abs/2610.09742), submitted 2026-10-07.

## Abstract

Refereeing decisions in professional soccer remain inconsistent because referees cannot easily compare a contentious foul against similar past cases. We cast this as a retrieval problem and introduce SoccerNet-FoulRet, the first benchmark for semantic foul retrieval. Given a query foul, the task is to retrieve past fouls judged to be relevant precedents, regardless of camera angle, teams, or appearance. This differs from prior video-to-video retrieval, which matches clips by visual similarity or a shared event. Here, relevance is defined by refereeing interpretation. We build the benchmark from the SoccerNet-MVFoul dataset and evaluate retrieval ability of zero-shot video and vision-language embedders together with a task-specific fine-tuned baseline on 693 human-verified queries and category-relevance labels. Semantic foul retrieval remains challenging. The strongest zero-shot model achieves under 5% HitRate@10 on human-verified precedents, while category-supervised fine-tuning improves category relevance but transfers only modestly to precedent retrieval. We release SoccerNet-FoulRet to establish semantic foul retrieval as an open problem: https://github.com/SoccerNet/sn-foulret.
