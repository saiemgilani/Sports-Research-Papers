# Wharton Sports Analytics Journal: back catalogue, scores and data sources

The Wharton Sports Analytics Journal (WSAJ, ISSN 3070-4065) publishes student research twice a
year. This report covers its whole public back catalogue as of 2026-10-04: 95 articles from
Spring 2022 to Spring 2026. Per-article rows are in `wsaj-data-sources.csv`; scores are appended
to `paper-ranking-scores.csv` as a separate pass (`folder = library`, `file` = the markdown twin).

## Method and date

- **Collection (2026-10-04).** The `wsaj` source in `feeds/download-sources.json` read
  `all-editions/`, the nine edition pages and the Rookie Review and High School Data Science
  Competition category pages. It made one request at a time, at least 2.5 s apart. It found 95
  articles and saved 94 PDFs into `library/journals/Wharton Sports Analytics Journal/`.
- **Text (2026-10-04).** pdftotext plus a scripted reflow, the method of commit `80776ee`, wrote
  94 twins under `md/`. Every PDF has a text layer; none is a scanned image.
- **Scoring (2026-10-05).** Each paper was scored on the committed 1-10 rubric (novelty,
  practicality, reproducibility; composite out of 30) from its abstract, introduction, data and
  method sections, never from the title. The SDV verdict (full / partial / none) applies the
  `SDV_BRIEF.md` rubric to the inputs the paper needs. The work was split across six parallel
  readers using one written brief with calibration anchors taken from the existing CSV.
- **Mentions.** SportsDataverse packages and related ecosystems were found by verbatim,
  case-insensitive regex over the twins. A package counts only if the text names it. Code links
  were checked against the PDFs' hyperlink annotations.
- **Caveats.** "Predicting March Madness Cinderella Teams" was scored from its web abstract
  alone: its page links a byte-identical copy of the Fall 2023 defensive-line paper. Three
  conversions with letter-spaced or garbled text (the "In a Rush to Pass" poster, the "Surprise
  Teams" paper and the Leicester City slide deck) are low-confidence reads.

## Articles by edition

| Edition | Found | Stated on `all-editions/` | PDFs |
|---|--:|--:|--:|
| Spring 2022 | 14 | 29 | 14 |
| Fall 2022 | 11 | 11 | 11 |
| Spring 2023 | 5 | 5 | 4 (Cinderella links another paper) |
| Fall 2023 | 8 | 10 | 8 |
| Spring 2024 | 11 | 11 | 11 |
| Fall 2024 | 8 | 8 | 8 |
| Spring 2025 | 9 | 9 | 9 |
| Fall 2025 | 14 | 16 | 14 |
| Spring 2026 | 10 | 10 | 10 |
| No edition (4 Rookie Review, 1 HS competition) | 5 | - | 5 |
| **Total** | **95** | 109 | **94** |

The WordPress edition categories hold exactly the counts found (the REST API agrees), so the
gaps are in the stated numbers or in posts outside the edition categories. Two Rookie Reviews
dated 2023-09-01 probably account for Fall 2023's missing pair. Spring 2022's 29 is unexplained.
Three Spring 2022 PDFs are 28-44 MB; all three are committed (each is under GitHub's 50 MB warning threshold).

## By sport

NFL 22 · MLB 13 (+ baseball 1, softball 1) · NBA 10 (+ basketball 4, men's college 3, women's
college 1) · soccer 10 · tennis 7 · cricket 3 · F1 3 · multi-sport 3 · NHL 2 (+ hockey 1) ·
fencing 2 · one each: CFB, rugby union, volleyball, field hockey, badminton, speedcubing,
esports, Paralympics, FIRST robotics. Tennis, F1, fencing and other sports outside SDV make up
about a fifth of the catalogue.

## By data source (papers naming each family; keyword match on `data_sources`)

| Family | Papers |
|---|--:|
| Official league or federation sites and APIs (MLB Stats API, NHL, NCAA, ATP/WTA, FIA, USA Fencing, ...) | 19 |
| Sports Reference sites (Pro Football, Basketball, Baseball, Hockey Reference, FBref) | 17 |
| NFL Big Data Bowl / Next Gen Stats tracking | 14 |
| Source not stated | 11 |
| nflverse family (nflfastR, nflscrapR, nfl_data_py) | 9 |
| Kaggle datasets | 8 |
| ESPN | 7 |
| Salary and transfer sites (Transfermarkt, Capology, Spotrac, Over the Cap) | 7 |
| FanGraphs; Statcast / Baseball Savant; Jeff Sackmann tennis data | 6 each |
| NBA Stats / nba_api | 3 |
| Retrosheet / Lahman; PFF; StatsBomb; surveys or own collection | 2 each |

## SportsDataverse packages named

Two of 95 articles name an SDV package, both baseballr. No article names sportsdataverse (Python,
JS or R), cfbfastR, hoopR, wehoop, fastRhockey, softballR, recruitR, oddsapiR, sdvplotR, cfbseedR,
sportyR, sportypy or a sportsdataverse-data release.

| Article | Package | Snippet |
|---|---|---|
| A Holistic Examination of Streakiness and Consistency in Major League Baseball (Spring 2024) | baseballr | "...were scraped from Baseball Reference20, both using the baseballr21 package in R." (methods; the digits are footnote markers) |
| All-Star Based Evaluation of Draft Value Curves Across Major North American Sports Leagues (Spring 2026) | baseballr | "Petti, B., Gilani, S., Baumer, B., ... (2024). baseballr: Acquiring and analyzing baseball data (Version 1.6.0) [R package]." (reference list only) |

Thirteen articles name a related ecosystem: nflfastR 8 (two also say nflverse), nflscrapR 1,
nfl_data_py 1, StatsBomb 2, Retrosheet 1. None names nba_api or pybaseball.

## Reproducibility and code

- **SDV verdict:** full 14, partial 37, none 44. The 14 "full" papers run on NFL play-by-play and
  draft/contract tables, Statcast and the MLB Stats API, ESPN EPL results, NBA Stats shot charts,
  men's college basketball play-by-play, 247Sports recruiting rankings and NCAA softball
  scoreboards. "None" is mostly tracking frames (Big Data Bowl), tennis, F1, fencing, salaries and
  transfer fees.
- **Code:** 17 of 95 (18%) link code or a repository; 5 more say code exists without a link; 73
  give neither. The share has risen: 2 of the 30 papers from Spring 2022 through Spring 2023
  (both in Fall 2022), 8 of the 24 in Fall 2025 and Spring 2026.
- **Data access:** 69 use public data, 9 mixed, 6 proprietary, 11 unknown.

## Top works by composite

Mean composite 12.5 (median 12), against 16.2 for the existing 286-row corpus; Spring 2022 averages
10.1 and Spring 2026 15.0.

| Σ/30 | N | P | R | Article | Edition | SDV |
|--:|--:|--:|--:|---|---|---|
| 21 | 7 | 6 | 8 | Introducing Grid WAR: Rethinking WAR for Starting Pitchers | Fall 2022 | partial |
| 19 | 6 | 6 | 7 | A Unified Server Quality Metric for Tennis | Spring 2026 | none |
| 19 | 5 | 6 | 8 | College Basketball: An In-depth Study of the "Foul Up 3" Dilemma | Fall 2024 | full |
| 19 | 6 | 6 | 7 | Expected Value Curves Don't Tell the Full Story: NFL Draft Position Trade Value Curves | Fall 2024 | full |
| 19 | 6 | 7 | 6 | Kicking for Goal or Touch? An Expected Points Framework for Penalty Decisions in Rugby Union | Spring 2026 | none |
| 18 | 5 | 4 | 9 | A Holistic Examination of Streakiness and Consistency in Major League Baseball | Spring 2024 | full |
| 18 | 6 | 6 | 6 | SET: Spatial Edge Technique - A Framework to Evaluate Edge Setters | Spring 2024 | none |
| 17 | 6 | 6 | 5 | Algorithmic NBA Player Acquisition | Fall 2023 | partial |
| 17 | 4 | 5 | 8 | Integrating Dynamic Defensive Geometry and Match-State Context in ... Expected Goals | Spring 2026 | none |

The best WSAJ work, Grid WAR at 21, would rank behind 12 of the 286 earlier rows and tie with 13
others.
