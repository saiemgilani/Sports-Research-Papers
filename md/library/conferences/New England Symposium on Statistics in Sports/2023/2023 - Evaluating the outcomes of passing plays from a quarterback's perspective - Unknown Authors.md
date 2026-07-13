<!-- source: library/conferences/New England Symposium on Statistics in Sports/2023/2023 - Evaluating the outcomes of passing plays from a quarterback's perspective - Unknown Authors.pdf -->

**<mark>Evaluating the outcomes of passing plays from a QB perspective</mark>** Will Morgan | Head of AMF Data Science, StatsBomb | will.morgan@statsbomb.com Introduction Method When evaluating quarterback decision making and We utilise our own event and low-frequency tracking data that tracks player performance, it's important to consider the trade-offs as a locations from the start of the play and updates at a minimum of 2.5 times per play evolves; when pressured, judging the fine line between second. The penultimate frame prior to the pass, sack or exiting the pocket is throwing the ball, scrambling or being sacked is a key skill. used to derive features up to a maximum of 2.5 seconds post-snap. We use this time-limit to avoid leaking too much information into the model training task. We derive features from the tracking frames to quantify the pressure on the QB, Arguably the best example of this in the current NFL, is plus representations of receiver separation and location. Patrick Mahomes, who combines elite passing efficiency, low sack rates and effective scrambling when required. Contextual features were also included (yardline, down, distance, time-to-throw). However, one metric where his performance apparently dips We developed three approaches for this multi-classification modelling task: is Completion Percentage Over Expected (CPOE), with 1. eXtreme Gradient Boosting (XGBoost) models placing him towards or even below league average 2. Graph convolutional Neural Network (GNN) over recent seasons. 

|3. Convolutional Neural Network (CNN) - adapted from prior studies<sup>[1,2,3]</sup><br>We trained the models on data from the 2022 NFL and NCAA seasons.<br>GNN features<br>Input frame|
|---|
|CNN example features|
|Results<br>Key model performance metrics are outlined below. Individual class labels were<br>found to be well calibrated on test-set data from the model training stage.<br>|
|**Description**<br>**Log loss ↓**<br>**F1 score ↑**<br>**ROC-AUC↑**|
|XGBoost<br>0.997<br>0.50<br>0.67|
|GNN<br>1.014<br>0.43<br>0.66|
|Given the XGBoost model had the best performance, subsequent analysis will<br>focus on predictions from it.<br>CNN<br>1.010<br>0.51<br>0.64|







<!-- Start of picture text -->
Input frame<br><!-- End of picture text -->



<!-- Start of picture text -->
GNN features<br><!-- End of picture text -->

Does separating all of these elements across either distinct models or outcome-based metrics present issues with evaluating quarterback performance? To tackle this, we build a classification model to predict the outcome of a drop-back play. The model aims to predict whether a play results in a: ● Completion ● Incompletion ● Interception ● Scramble ● Sack 



Analysis Below we profile QB performance by deriving outcome rates over expectation for some of the model target variables for both the NFL and NCAA 2022 season. 





# ● Justin Fields outlier status 

● A number of QBs able to maintain strong positive outcomes, while avoiding negative plays 

○ Mahomes stands out in ability to run below expectations on sacks, incompletions & interceptions, while scrambling at above average rates ● 2022 & 2023 NFL draft prospects with good performances relative to expectations ● The contrast between Caleb Williams & Drake Maye in their sack & scramble rates relative to expectation 



- Ashford’s unfortunate NFL player comparison status 

- References 

1The Zoo, How many yards will an NFL player gain after receiving a handoff?, Big Data 

> Bowl, 2020 

2Ben Baldwin, Computer Vision with NFL Player Tracking Data using torch for R, Open 

> Source Football, 2021 

3Song et al., Explainable Defense Coverage Classification in NFL Games using Deep Neural 

> Networks, Sloan Analytics Conference, 2023 


