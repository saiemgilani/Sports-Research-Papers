<!-- source: library/conferences/New England Symposium on Statistics in Sports/2019/2019 - Comparing NHL Players' Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces - Unknown Authors.pdf -->

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces 

Devan Becker, Ph.D. Candidate Department of Statistical and Actuarial Sciences The University of Western Ontario, Canada 

Collaborators: Charmaine Dean and Douglas Woolford 

New England Symposium on Statistics in Sports Harvard University September 28, 2019 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

1 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces 

Introduction 

Introduction 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

2 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces 

Introduction 

# A Song of Ice Hockey and Forest Fire 



University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

3 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces 

Introduction 

# Outline 

## _•_ Describe the NMF-LGCP algorithm in general. 

- Apply it to NHL shot data. 

- Use these estimates to describe shot efficiency (with a twist). 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

4 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Image Recognition and Spatial Estimates 

Image Recognition and Spatial Estimates 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

5 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Image Recognition and Spatial Estimates 

# Idea: Convert one big matrix into two smaller matrices 

## _X ≈ WH_ 

- _X_ is a giant collection of images 

   - In this case, LGCP estimates of the shot locations. 

## _• W_ the “bases” 

- Building blocks for all images 

## _• H_ the 

- How much each image uses each building block 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

6 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Image Recognition and Spatial Estimates 

Dummy Data and Estimates 



<mark>Normalized so</mark> Devan <mark>that</mark> Becker <mark>the</mark> - dbecker7@uwo.ca <mark>total volume</mark> University <mark>is 1 so</mark> of Western <mark>that</mark> Ontario <mark>we are focused on</mark> 

7 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Image Recognition and Spatial Estimates 

# Dummy Bases and Coefficients 



University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

8 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Image Recognition and Spatial Estimates 

# Choosing the number of bases 

- Too many bases and you’re modelling the noise. 

- Too few and your residuals are too large. 

- Balance: Interpretability and accuracy. 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

9 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Image Recognition and Spatial Estimates 

# NHL Shot Location Data 

- Scraped from https://statsapi.web.nhl.com/api/v1/. . . 

   - Incomplete version available from a Kaggle data set. 

   - Always check robots.txt before scraping. 

- Only looked at players with _>_ 500 shots. 

## _•_ Removed rebounds. 

- Focused on shot choice, not opportunity. 

In all, 510,847 shots and goals from 466 players. 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

10 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Image Recognition and Spatial Estimates 

# Estimated Bases for NHL Data 



University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

11 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Image Recognition and Spatial Estimates 

# Some Select Players 



<!-- Start of picture text -->
Crease LCrease RCrease/LIce Slot<br>Alex Ovechkin (LW−R)<br>P.K. Subban (D−R)<br>Ryan Getzlaf (C−R)<br>Sidney Crosby (C−L)<br>Connor McDavid (C−L)<br>Anze Kopitar (C−L)<br>0.0 0.5 1.0 1.5 2.0 2.5<br>RIce RPoint LPoint<br>Alex Ovechkin (LW−R)<br>P.K. Subban (D−R)<br>Ryan Getzlaf (C−R)<br>Sidney Crosby (C−L)<br>Connor McDavid (C−L)<br>Anze Kopitar (C−L)<br>0.0 0.5 1.0 1.5 2.0 2.50.0 0.5 1.0 1.5 2.0 2.50.0 0.5 1.0 1.5 2.0 2.5<br>Coefficient (x100)<br><!-- End of picture text -->

Different position/handedness shoot from different places, but same position/handedness can be different too. 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

12 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Image Recognition and Spatial Estimates 

# Basis Results - Outliers 

### Principal Components of Coefficients 



<!-- Start of picture text -->
C−L C−R D−L D−R<br>0.03<br>0.02<br>0.01 Lecavalier Malkin Wisniewski<br>0.00 Richards Spooner Stoll Coburn Subban Niskanen<br>Mitchell Ott Getzlaf Daley<br>−0.01<br>Rask<br>−0.02<br>−0.03 Oduya<br>LW−L LW−R RW−L RW−R<br>0.03<br>0.02<br>0.010.00 TeravainenHoffmanSteenBeleskeyDrouin OvechkinThornton VoracekDupuisKopeckyYaku Jagr pov Pominville Pastrnak LaineHansenRead<br>−0.01 Clifford Bickell Kovalchuk Iginla<br>−0.02<br>−0.03<br>−0.02 −0.01 0.00 0.01 −0.02 −0.01 0.00 0.01 −0.02 −0.01 0.00 0.01 −0.02 −0.01 0.00 0.01<br>PCA Dimension 1<br>PCA Dimension 2<br><!-- End of picture text -->

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

13 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces 

Shot Quality 

Shot Quality 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

14 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces 

Shot Quality 

# Basketball versus Hockey 

For players who played at least half of the 2017-2018 season: 

## Basketball 

   - WORST 3-point percentage: 29.8% (Russell Westbrook) 

- Hockey 

   - BEST shooting percentage: 23.5% (Alexander Kerfoot) 

Hockey just doesn’t have enough goals per player! 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

15 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces 

Shot Quality 

# Where do Goals Come From? 



University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

16 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces 

Shot Quality 

# Perfect Players 

Instead of looking at a player’s goals, we use the goals as a player. 

- Goals are split up based on position/handedness. 

- Name of player is replaced by the position/handedness. 

- These “perfect players” are added to the algortihm. 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

17 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Shot Quality 

# Coefficients for the Perfect Players 

### Coefficients for Perfect Players 



<!-- Start of picture text -->
Crease LCrease RCrease/LIce Slot<br>RW−R<br>RW−L<br>LW−R<br>LW−L<br>D−R<br>D−L<br>C−R<br>C−L<br>0.0 0.5 1.0 1.5 2.0<br>RIce RPoint LPoint<br>RW−R<br>RW−L<br>LW−R<br>LW−L<br>D−R<br>D−L<br>C−R<br>C−L<br>0.0 0.5 1.0 1.5 2.0 0.0 0.5 1.0 1.5 2.0 0.0 0.5 1.0 1.5 2.0<br>Coefficient (x100)<br>Position/Handedness<br><!-- End of picture text -->

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

18 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Shot Quality 

# Comparing Stastny, Crosby, and Aho to the Perfect Player 



<!-- Start of picture text -->
Crease LCrease RCrease/LIce Slot<br>C−L<br>Paul Stastny<br>Sidney Crosby<br>Sebastian Aho<br>0.0 0.5 1.0 1.5<br>RIce RPoint LPoint<br>C−L<br>Paul Stastny<br>Sidney Crosby<br>Sebastian Aho<br>0.0 0.5 1.0 1.5 0.0 0.5 1.0 1.5 0.0 0.5 1.0 1.5<br>Coefficient (x100)<br>Player<br><!-- End of picture text -->

- Stastny: Follows the Perfect Player, “Could stand to shoot the puck more.” - EliteProspects.com 

- Crosby: Shoots from different place, but scores. 

- Aho: “Very good passer.” - EliteProspects.com 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

19 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces Shot Quality 

# Euclidean distance as shot quality 

Players "closest" to the perfect player have better shooting percentage Blue line is the linear trend. 



<!-- Start of picture text -->
C−L C−R D−L D−R<br>0.150 0.08<br>0.12 0.125 0.070.06 0.070.06<br>0.09 0.100 0.05 0.05<br>0.06 0.075 0.04 0.04<br>0.03 0.03<br>0.2 0.3 0.4 0.5 0.6 0.2 0.3 0.4 0.5 0.6 0.7 0.3 0.4 0.5 0.2 0.3 0.4 0.5 0.6<br>LW−L LW−R RW−L RW−R<br>0.150 0.12 0.14 0.14<br>0.12<br>0.125 0.10 0.12<br>0.10<br>0.100 0.08 0.10 0.08<br>0.075 0.06 0.08 0.06<br>0.04 0.04<br>0.2 0.4 0.6 0.3 0.4 0.5 0.6 0.3 0.4 0.5 0.3 0.4 0.5 0.6 0.7<br>Euclidean Distance from Perfect Player<br>Shooting Percentage<br><!-- End of picture text -->

Recall: estimates were normalized to **not** include the number of shots or goals. 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

20 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces 

Shot Quality 

# Conclusions 

- Bases provide good foundations for heuristic advice. 

   - “Shoot more when you’re at the point, less from the faceoff circle.” 

- Coefficients simplify the comparison of player shooting strategy. 

- Perfect players give us a measure of quality when we don’t have enough data. 

- Playing like a perfect player does not mean you’ll always score. 

University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

21 

Comparing NHL Players’ Shots and Goals by Algorithmically Decomposing Shot Intensity Surfaces 

Shot Quality 

# Acknowledgements 





University of Western Ontario 

Devan Becker - dbecker7@uwo.ca 

22 


