<!-- source: library/journals/Wharton Sports Analytics Journal/2025/2025 - Poise or Panic Breaking Down QB Pressure - Hafiz et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/poise-or-panic-breaking-down-qb-pressure/ -->
<!-- authors: Jahan Hafiz; Avi Mandhana; Derek Park; Sohan Saleem -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Poise or Panic? Breaking Down QB Pressure

Jahan Hafiz, Avi Mandhana, Derek Park, Sohan Saleem

Take a look at these two plays

Tom Brady

Zach Wilson

199th Overall Pick

2nd Overall Pick

How do we quantify QB performance against pressure?

Importance

● QBs perform differently under pressure

● QB performance under pressure defines outcomes of games

Pressure Score Formula

● Multivariable regression model

● Bin into clean, medium, and high pressure situations

Using bins to separate levels of pressure

Pressure Score 0 (0, 15] (15, ∞)

Pressure Level Clean Pocket Medium Pressure High Pressure

Standardized Passer Rating

0.02484 = R-Squared

Discrete outcomes result in model being less interpretable

We can’t see everything using hits, hurries, beats.

Past Work

- Ibrahim (2021)

- Offensive Line & QB Voronoi data to estimate protection levels

- Binning system

- Modeled duration in which space remained unchanged

- STRAIN - Nguyen, Yurko, Matthews (2023)

- Based on strain rate in material science

- Developed to rank pass rushers

- Our goal: combine these ideas to quantify QB performance under pressure

Voronoi Diagrams

Using Voronoi diagrams to measure rate of change in pocket area

Voronoi Overview

- Partitions based on players

- QB Region can be used to measure “pocket” space

Example Play - Cowboys vs. Buccaneers (Week 1, 2021)

Example Play - Cowboys vs. Buccaneers (Week 1, 2021)

PRSS - Pocket Reduction Speed Score

Maximum Negative Change in Pocket Area

Early Attempts

● Plotting the raw data looks a bit messy

● Lower PRSS does seem to be associated with more yards gained though

Early Attempts

● Averaging data by QB is a bit messy but might show some trend

○ Averaging reduces granularity of how specific lower and higher PRSS values will affect avg_yards_gain ed

Binned Avg. PRSS (Voronoi) vs. Avg Yards Gained

Avg_yards_gained = 4.97 - 0.0647 × (avg_PRSS)

Model fit: R² = 0.507, P = 0.00134.

● Binning increases interpretability of how PRSS affects passing

● Higher scores associated with fewer yards gained on a pass play

Avg. PRSS for Offensive Team

● Binned into increments of 10

● Calculated average yards gained within the bins

● Allows us to see which qb is outperforming / underperforming their o-line at specific PRSS levels.

PRSS Applications

● Using PRSS can determine which quarterbacks fare better under pressure

● Joe Burrow, Jalen Hurts, were high above the regression line and went on to be stars

● Using similar data can be used to judge college prospects

Analyzing College Prospects using PRSS

● Handling pressure is the hardest aspect for college athletes to transition to the NFL

Next Steps for PRSS

● Apply PRSS to Full-Season Data

● Apply to Draft Preparation and Free Agency

● Explore Correlation with More Advanced QB Stats

Thank You!

## Methods

● Gather freeze frames of all players per play

● Generate Voronoi diagrams for each freeze frame until the pass using deldir package in R

● Calculate QB pocket area change and QB pocket area rate of change (PRSS)

● Gather conclusions for QB performance and PRSS
