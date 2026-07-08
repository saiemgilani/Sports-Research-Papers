# Sports Analytics Research Feed

Last verified: 2026-07-08

This directory is a seed catalog for two related feeds:

- Research paper feed: journals, proceedings, preprints, books, and article indexes.
- Opportunity feed: conference calls, paper competitions, posters, presentations, hackathons, data challenges, and Kaggle competitions.

Use `sports-analytics-sources.yml` as the canonical source list. Use `sports-analytics-feeds.opml` for feed readers that can import RSS/XML endpoints.

## Core Journals

The core journal set starts with JQAS, Journal of Sports Analytics, IJCSS, JSSM, and International Journal of Sports Science and Engineering. JQAS, JSA, and IJCSS are the highest-signal sports analytics outlets. JSSM is broader sports science and medicine, so tag/filter for quantitative methods, modeling, performance, biomechanics, tracking, and analytics. IJSSE is included from the ASA Statistics in Sports listing and the original seed list, but should stay monitor-only until its publisher URL is refreshed.

Static reference volumes, including the Oxford anthology and the statistical methods handbook, are included as references rather than feed sources.

## Core Opportunities

Highest priority recurring sources:

- MIT Sloan Sports Analytics Conference Research Paper Competition: abstracts, invited full papers, finals presentations, posters.
- MIT Sloan competitions: hackathon and related competition tracks.
- NESSIS: talks, posters, conference videos and materials; next cycle is 2027.
- CASSIS: talks, posters, and programs; alternates with NESSIS.
- CMSAC: academic sports analytics conference with talks and student posters.
- CSAS, formerly UCSAS: student-oriented symposium with posters, workshops, and data challenges.
- MLSA: ECML PKDD workshop with sports analytics papers and proceedings.
- MathSport International and MathSport Asia: mathematics, statistics, operations research, and sport.
- NFL Big Data Bowl and Kaggle Sports: annual or continuous data competitions and writeups.
- Brendan Kent's sports analytics conference video archive index: discovery source for free videos, panels, and presentations from MIT Sloan, NESSIS, CMSAC, StatsBomb, hockey analytics conferences, UCSAS, MathSport, and related events.

## Current Watch Items

- SSAC27 research paper competition: abstract deadline is 2026-10-01 at 11:59 PM Eastern; selected full papers are due 2026-12-04.
- NESSIS: 2025 event is complete; the next NESSIS is expected in 2027 and abstracts are expected to open in early 2027.
- CASSIS: verified page said abstracts were closed and registration was open.
- CSAS 2026: held 2026-04-10 to 2026-04-11 at University of Connecticut, with data challenge and poster outputs listed.
- MLSA 2026: paper deadline was 2026-06-05; workshop date is 2026-09-07.
- MathSport Asia 2026: scheduled 2026-12-08 to 2026-12-10, with accepted abstracts eligible for optional full paper proceedings submission.

## Monitoring Workflow

1. Import `sports-analytics-feeds.opml` into a feed reader for true RSS/XML sources.
2. Poll all `feed_kind: poll` URLs weekly during active seasons and monthly otherwise.
3. Use video archive indexes to discover talks and panels, then verify the downstream video URL before cataloging it.
4. Save accepted papers, poster PDFs, proceedings, video links, slides, and solution writeups into this repository with a year-prefixed filename.
5. Tag each item with sport, method, venue, format, and data type.
6. Re-check all active deadlines directly from the official page before submitting.

Suggested tags:

- `venue`: journal, conference, workshop, symposium, competition, book
- `format`: article, abstract, full-paper, poster, talk, slides, video, code, writeup
- `method`: bayesian, causal-inference, optimization, machine-learning, computer-vision, tracking-data, simulation, ranking, scheduling
- `sport`: baseball, basketball, football, soccer, hockey, golf, tennis, olympic, multi-sport
- `status`: new, triaged, downloaded, archived, submitted, accepted, rejected, stale

## Standing Searches

- `"sports analytics" "call for papers"`
- `"sports analytics" "poster" "submission"`
- `"sports analytics" "data challenge"`
- `"sports analytics" "hackathon"`
- `"sports analytics" "research paper competition"`
- `"sports statistics" "symposium" "abstract"`
- `"player tracking" "competition" "Kaggle"`
- `"Big Data Bowl" "Kaggle"`
- `"Machine Learning and Data Mining for Sports Analytics"`
- `"MathSport" "call for papers"`
- `"sports analytics conference" "video archive"`
- `"sports analytics" "YouTube" "conference"`
