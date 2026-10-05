<!-- source: library/journals/Wharton Sports Analytics Journal/2025/2025 - Optimizing Lead Distance - Whitney-Epstein et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/optimizing-lead-distance/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2025 -->
<!-- authors: Jack Whitney-Epstein; Jackson Hubbard; Lila Dodson; William Deflorio; Zach Sissman -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Optimizing Lead Distance

Jack Whitney-Epstein, Jackson Hubbard, Lila Dodson, William Deﬂorio, Zach Sissman

## 1. Intro

Lead Distance

Caught Stealing

Pickoﬀ

Research Question:

If a runner on 1B intends to steal 2nd, what is the optimal* lead from ﬁrst base?

*maximizes xRuns (Expected Runs) for base state 1 - - (2024)

Outcomes

+0.2 xRuns

-0.45 xRuns

The Formula: xRuns = 0.2 x SB - 0.45 x CS - 0.45 x PK

Linear Weights Per Baseball Savant

Factors

Runner: sprint speed Pitcher: Threat

Catcher: pop time

Pitcher Threat

Net Bases Prevented 100 Innings Pitched

● Lead Distance ● Threat ● Catcher Pop Time ● Runner Speed

## 2. Approach

GLM scale

Probabilities

Stolen Base Caught Pickoﬀ xRuns

For one pitch, only lead distance can be controlled… hold everything else constant, ﬁnd optimal

Each situation: Own optimal value!

Example Pitch and Model run

Runner: Pete Crow-Armstrong

30 ft/s sprint speed

Pitcher: Paul Skenes

4.03 threat

Threat 1.803 Wheeler Pop time 1.87 Marchán

Sprint speed 28.1 OhtaCniatcher: Yasmani Grandal

2.09 s pop time lead 13.6 optimal

Lead

11.5 ft

10.6 ft

Optimal

Lead

11.2 ft

14.5 ft

Optimal

Lead

11.2 ft

14.5 ft

Optimal

## 3. Results

Expected Runs (Sample of 100 pitches)

Evaluating Players

Evaluating Teams

Takeaways

Optimizing lead distance: Just 1 more shuﬄe → +0.02 runs

Leads are typically too short

Confounding Factors?

Players’ fear of making an out on basepath

Game Situation (Situational vs linear weights)

New rule: 3 pickoﬀs

Questions

## References

https://baseballsavant.mlb.com/leaderboard/basestealing-run-value?game_type=Regular&n=q&pitch_hand=all&runner_m oved=All&target_base=All&prior_pk=All&season_end=2025&season_start=2025&sortColumn=simple_stolen_on_running _act&sortDirection=desc&split=no&team=&type=Bat&with_team_only=1&expanded=0 https://baseballsavant.mlb.com/leaderboard/pitcher-running-game?game_type=Regular&n=q&pitch_hand=all&runner_mo ved=All&target_base=All&prior_pk=All&season_end=2024&season_start=2025&sortColumn=simple_prevented_on_runni ng_attr&sortDirection=desc&split=no&team=&type=Pit&with_team_only=1&expanded=0 https://support.mlb.com/s/?_gl=1*1wh6jhq*_gcl_au*MjAzOTIzNzk0MC4xNzUyNzE4OTA5Ljk3MjI2NzE0My4xNzUzMjI0Mz Q5LjE3NTMyMjQzNTQ.*_ga*MTYyOTE1Njc5OC4xNzUyNzE4OTA5*_ga_N8YFCZLYSZ*czE3NTMzMjUwMzgkbzEwJGc wJHQxNzUzMzI1MDM4JGo2MCRsMCRoMjAyMDc2MTE4Mw.. https://baseballsavant.mlb.com/leaderboard/basestealing-run-value?game_type=Regular&n=q&pitch_hand=all&runner_m oved=All&target_base=All&prior_pk=All&season_end=2025&season_start=2025&sortColumn=simple_stolen_on_running _act&sortDirection=desc&split=no&team=&type=Bat&with_team_only=1&expanded=0 https://baseballsavant.mlb.com/leaderboard/pitcher-running-game?game_type=Regular&n=q&pitch_hand=all&runner_mo ved=All&target_base=All&prior_pk=All&season_end=2024&season_start=2025&sortColumn=simple_prevented_on_runni ng_attr&sortDirection=desc&split=no&team=&type=Pit&with_team_only=1&expanded=0 https://support.mlb.com/s/?_gl=1*1wh6jhq*_gcl_au*MjAzOTIzNzk0MC4xNzUyNzE4OTA5Ljk3MjI2NzE0My4xNzUzMjI0Mz Q5LjE3NTMyMjQzNTQ.*_ga*MTYyOTE1Njc5OC4xNzUyNzE4OTA5*_ga_N8YFCZLYSZ*czE3NTMzMjUwMzgkbzEwJGc wJHQxNzUzMzI1MDM4JGo2MCRsMCRoMjAyMDc2MTE4Mw..

Refer https://baseballsavant.mlb.com/leaderboard/basestealing-run-value?game_type=Regular&n=q&pitch_hand=all&run ner_moved=All&target_base=All&prior_pk=All&season_end=2025&season_start=2025&sortColumn=simple_stolen _on_running_act&sortDirection=desc&split=no&team=&type=Bat&with_team_only=1&expanded=0 https://baseballsavant.mlb.com/leaderboard/pitcher-running-game?game_type=Regular&n=q&pitch_hand=all&runn er_moved=All&target_base=All&prior_pk=All&season_end=2024&season_start=2025&sortColumn=simple_prevent ed_on_running_attr&sortDirection=desc&split=no&team=&type=Pit&with_team_only=1&expanded=0 https://support.mlb.com/s/?_gl=1*1wh6jhq*_gcl_au*MjAzOTIzNzk0MC4xNzUyNzE4OTA5Ljk3MjI2NzE0My4xNzUz MjI0MzQ5LjE3NTMyMjQzNTQ.*_ga*MTYyOTE1Njc5OC4xNzUyNzE4OTA5*_ga_N8YFCZLYSZ*czE3NTMzMjUw MzgkbzEwJGcwJHQxNzUzMzI1MDM4JGo2MCRsMCRoMjAyMDc2MTE4Mw..
