<!-- source: library/journals/Wharton Sports Analytics Journal/2022/2022 - Zero Running Backs or Zero Points An Analysis on the Optimal Fantasy Football Draft Strategy - Heller et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/zero-running-backs-or-zero-points-an-analysis-on-the-optimal-fantasy-football-draft-strategy/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2022 -->
<!-- authors: Andrew Heller; James Sohigian; Henry Bartz; Ethan Kawahara; Felix Wang -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Zero Running Backs or Zero Points:

An analysis on the optimal Fantasy Football draft strategy

Andrew Heller, James Sohigian, Henry Bartz, Ethan Kawahara, Felix Wang

Wharton Moneyball Academy 2022, Sports Analytics Student Research Journal

DEFINITIONS

Key terms used

Fantasy football: a game in which the participants serve as owners and general managers of virtual professional American football teams

PPR (points per reception) data for our model

● ADP = average draft position (overall) ● FPT = fantasy points total

## BACKGROUND

Millions of people every year struggle with their fantasy football drafts because they often:

● Draft what is computer recommended ● Auto draft ● Draft based on subjective bias like name recognition ● Draft teams with players that are susceptible to injuries during the season

Running backs are the most susceptible players to injury… so is it even worth to draft them early?

Zero Running Back draft strategy is:

● Load up team with the top WRs, TEs, and QBs in the early rounds of the draft ● Let others pick off the ‘top’ RBs in the first five rounds ● Starting around the 6th round, draft the leftover RBs (usually consisting of high upside players or backups that might play or can be used for trade value)

STRATEGIES EXPLAINED:

ZERO-RB

Not popularly known or used

OPTIMAL STRATEGY

Whichever draft strategy used to produce teams with the highest final season total points

’Standard’

Common process of subjectively drafting

OTHER

Other uncommon draft strategies not investigated

AUTO-DRAFT

Computer based ratings

HYPOTHESIS

The Zero-RB draft strategy will prove to be more effective than the conventional draft strategy.

• Top RBs have been proven to be injured more frequently than other top positional players

• Stacking up on WRs, TEs, and QBs usually scores an equal number of points as the top RBs

APEX Fantasy Football Insider

Blog

“Our three-year average tells us that a top 30 running back is likely to miss 0.86 more games per season than a top 30 wide receiver.”

“Considering wide receivers are scoring more points than running backs, come at a cheaper price, and are less likely to get injured, I think it’s a very good idea to take wide receivers early. This is the best way to give your fantasy football team a weekly advantage.”

Fantasy points by draft round over different position groups

RB

WR

TE

QB

DEF

STANDARDIZED FPT BY POS, GROUPED BY YEAR

## MODEL PROCESS

ADP (acting as the mean) and SD are used to generate a random draft position.

## 2. SIM

Each team’s players are sorted and ranked by

POS and Fantasy Points.

## 4. SORT

## 1. DATA

The ADP, SD, and average fantasy points tables are combined.

## 3. DRAFT

According to various “limits,” all 12 team draft 14 players in a snake draft.

## 5. LOOP

The model is repeated for every position and year.

## 1. DATA

## 2. SIMULATION

rnorm(n, mean, sd)

## 3. DRAFT

## 4. SORT

POS QB WR WR RB RB TE DEF

## 5. LOOP

12 Picks 14 Rounds 100 Simulations 12 Experiments 10 Years = 2,016,000 Picks

: Standard strategy

: Zero-RB

: Standard strategy

: Zero-RB

: Standard strategy

: Zero-RB

## CONCLUSIONS

From our data, the Zero - RB doesn’t work optimally and it is suggested that the Fantasy Football draft process is based primarily on luck

● Year to year distribution of the running backs determines which draft strategy will be the most viable

● Larger discrepancies between top RBs and lesser RBs effect the Zero-RB draft strategy effectiveness

● Random year to year variation in player productivity changes outcomes

## LIMITATIONS & FAULTS

● Excluded years 2012 and 2013 due to a lack of data for player ADPs ● Used Occam's razor for draft with assigning normal curves to players ● Elimination of positions in real life leagues like kickers ● Did not have real life data from Sleeper, ESPN, etc to ensure normality in

ADP distribution ● Trades and FAAB/Waiver Wire not accounted for ● Data was converted to a .csv and cleaned by hand so room for data errors

## References & Resources

https://apexfantasyleagues.com/more-injury-prone-wide-receivers-running-backs/ https://fantasydata.com/nfl/fantasy-footballleaders?season=2020&seasontype=1&scope=1&subscope=1&scoringsystem=2&st artweek=1&endweek=1&aggregatescope=1&range=1 https://fantasyfootballcalculator.com/adp/ppr/12-team/all
