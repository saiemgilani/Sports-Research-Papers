<!-- source: library/conferences/New England Symposium on Statistics in Sports/2025/2025 - A Comps-Based Approach for Interpreting Tree-Based Predictions with an Application to the NFL Draft - Unknown Authors.pdf -->

- A comps-based approach for interpreting tree-based predictions with an application to the NFL draft Elisabeth Millington<sup>1</sup> , Scott Powers<sup>2</sup> 

- _1Rice University, Department of Kinesiology, 2Rice University, Department of Sport Management_ <mark>Methods</mark> Random Forest Modeling • Cam Ward: 37.0 

- 1. We used a random forest model to predict average NFL QBR based on college • Dillon Gabriel: 34.6 

- quarterback statistics. 



<mark>Introduction</mark> 

<mark>Application to 2025 NFL Draft</mark> The predictions for the top four NFL prospects pre-draft were 

- Random Forests are a powerful machine learning prediction model, but like other “black box” algorithms, their results are difficult to interpret. 

- • In sports, interpretability is crucial because it builds trust for the user in the predictions, and front offices need to consider non-quantifiable information in their decision-making. 

- • We aim to use the _k_ -NN properties of random forests to add interpretability to the QBR predictions produced for quarterback prospects in the form of “player comps”. 



<!-- Start of picture text -->
•<br>Dillon Gabriel: 34.6<br>•<br>Shedeur Sanders: 33.2<br>•<br>Jaxson Dart: 24.0<br>Cam Ward Dillon Gabriel Shedeur Sanders Jaxson Dart<br>Comp Score Comp Score Comp Score Comp Score<br>Johnny Manziel 2.3% Mason Rudolph 2.0% Mason Rudolph 1.9% Teddy Bridgewater 1.9%<br>Marcus Mariota 2.3% Dwayne Haskins 1.9% Kenny Pickett 1.9% Tajh Boyd 1.6%<br>Baker Mayfield 2.2% Kenny Pickett 1.9% Philip Rivers 1.9% Russell Wilson 1.5%<br>Philip Rivers 2.1% C.J. Stroud 1.9% Ben Roethlisberger 1.8% John Beck 1.5%<br>Trevor Lawrence 2.0% Andrew Luck 1.9% Case Keenum 1.8% Drake Maye 1.4%<br>Matt Leinart 2.0% Bo Nix 1.9% Russell Wilson 1.8% Zach Terrell 1.4%<br>Russell Wilson 2.0% Trevor Lawrence 1.9% Trevone Boykin 1.8% Kevin Hogan 1.2%<br>Lamar Jackson 1.9% Philip Rivers 1.8% Kellen Moore 1.7% Blake Bortles 1.2%<br>Deshaun Watson 1.9% Aaron Rodgers 1.7% Andrew Luck 1.7% Sam Howell 1.2%<br>Case Keenum 1.9% Bryce Young 1.6% C.J. Stroud 1.7% Patrick Mahomes 1.1%<br>Dillon Gabriel Cam Ward Shedeur Sanders Jaxson Dart<br>0.08 0.08 0.08 0.08<br>0.06 0.06 0.06 0.06<br>0.04 0.04 0.04 0.04<br>0.02 0.02 0.02 0.02<br>0.00 0.00 0.00 0.00<br>0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60<br>QBR QBR QBR QBR<br>Dillon Gabriel Cam Ward Shedeur Sanders Jaxson Dart<br>0.03 0.03 0.03 0.03<br>0.02 0.02 0.02 0.02<br>0.01 0.01 0.01 0.01<br>0.00 0.00 0.00 0.00<br>0 20 40 60 0 20 40 60 0 20 40 60 0 20 40 60<br>Training Player QBR Value Training Player QBR Value Training Player QBR Value Training Player QBR Value<br>Figure 1: Top: Histogram of training players’ regressed QBR values weighted by similarity to the prospect being predicted. The vertical green line<br>annotates each prospect’s predicted QBR, which matches the mean of the weighted distribution. Bottom: Scatter plot showing individual similarity<br>scores and regressed QBR for historical prospects.<br>Weights Weights Weights Weights<br>Training Player Similarity Score Training Player Similarity Score Training Player Similarity Score Training Player Similarity Score<br><!-- End of picture text -->

• Response Variable: Average NFL QBR across seasons (0 for players who never played in the NFL) 

Random Forest as Adaptive Nearest Neighbors 

1. Building on the work of Lin & Jeon (2006) we interpret the random forest model as a 

data-adaptive weighted 𝑘-nearest neighbors ( _k_ -NN) algorithm. 

• Let ⃗𝑥 ∈ℝ<sup>#</sup> ∈ℝ the !, … ,⃗𝑥" be the training feature vectors and 𝑦!, … , 𝑦" corresponding outcomes (NFL QBR). We draw 𝐵bootstrap samples and train a decision tree on each sample 𝑏∈ 1 … 𝐵 . 

- Let 𝑛 be the number of times observation 𝑖appears in bootstrap sample 𝑏 $,& 

<mark>Data</mark> • The data used in this project consists of publicly available data from Sports Reference • Our dataset includes 2,099 quarterbacks. The data for each player-season includes team, conference,  strength of schedule, games played, passing statistics (attempts, completions, touchdowns, interceptions),  rushing statistics (attempts, yards, touchdowns), and awards (All-America designation, Heisman voting). • In addition to college statistics, we obtained each player’s NFL passing attempts and Total Quarterback Rating (QBR) (Burke, 2016). QBR is based on expected points added (EPA), and considers each quarterback’s share of their team’s EPA and accounts for home-field advantage, defensive strength, and garbage time. • We regressed each player’s QBR/season to zero to mitigate the effects of players who put up very high QBR numbers in very small samples. <mark>Software</mark> • R package treecomp. • Extracts similarity scores from random forests. • Open-source: github.com/elisabethmill/treecomp 

Let 𝒯 denote the terminal node of observation 𝑖in tree 𝑏 $,& 

- 

• Let ∣𝒯 ∣be the number of observations in that node (with repetition) $,& 2. Given a new query point ⃗𝑥', the prediction of tree 𝑏 is: 

" "!,#⋅𝕀 𝒯!,$(𝒯!,# = 1. ⃗𝑥 𝑤 𝑤 2𝑦$ ' = 4 $,',& ⋅𝑦& _where_ $,',& &(! ∣𝒯 ∣ !,$ 3. The random forest prediction is the average across trees: ¯ ¯ " ! ! - - • = 2𝑦 ⃗𝑥' 2𝑦$ ⃗𝑥' 𝑤',&<sup>⋅𝑦</sup> &<sup>_with_𝑤</sup> ',&<sup>=</sup> 𝑤$,',& -<sup>∑$(!</sup> -<sup>4</sup> $(! = 8 &(! 4. ⃗𝑥 This formulation shows that a random forest defines a custom neighborhood for ', where observations that frequently land in the same leaf across trees are assigned higher weights. Similarity Score ¯ 1. 𝑤 We interpret ',&<sup>as a similarity score between the query point ⃗𝑥</sup> '<sup>and a training</sup> ⃗𝑥 : point & ¯ - ! " • 𝑤 !,# 𝒯 = 𝒯 ',&<sup>=</sup> $,' $,& -<sup>8</sup> ∣𝒯 ∣<sup>⋅𝕀</sup> $(! !,$ 2. Higher similarity implies more frequent co-occurrence in terminal nodes 

# <mark>Results</mark> 

The random forest model achieved a test RMSE of 8.61, explaining 43.7% of the variance in regressed NFL QBR. Key predictors of NFL success: • Final-season Heisman voting • Passing stats per season (yards, TDs, completions) • Final-season strength of schedule High multicollinearity exists between some variables (e.g., yards, touchdowns, and completions per season are all pairwise correlated at ≥ 0.94). 



- References: • Burke, B. (2016). How is total QBR calculated? We explain our (improved) QB rating [September 27, 2016]. ESPN.com. https://www.espn.com/nfl/story/_/id/17653521/how-total-qbr-calculated-explain-our-improved-qb-rating 

- • Lin, Y., & Jeon, Y. (2006). Random forests and adaptive nearest neighbors. Journal of the American Statistical Association, 101 (474), 578–590. https://doi.org/10.1198/016214505000001230 

- • - Probst, P. (2024). tuneRanger: Tune random forest of the ’ranger’ package (Version 0.7). <u>https://cran.r project.org/web/packages/tuneRanger/index.html</u> 

- • - Wright, M. N. (2024). Ranger: A fast implementation of random forests (Version 0.17.0). https://cran.r <u>project.org/web/packages/ranger/index.html</u> 

- Acknowledgement: The authors thank Kevin Meers for suggestions that led to improvements in the random forest model for predicting NFL quarterback prospect success. 


