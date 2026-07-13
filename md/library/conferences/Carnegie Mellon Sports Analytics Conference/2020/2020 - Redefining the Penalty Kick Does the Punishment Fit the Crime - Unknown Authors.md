<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2020/2020 - Redefining the Penalty Kick Does the Punishment Fit the Crime - Unknown Authors.pdf -->



#### Redefining the Penalty Kick: Does the Punishment Fit the Crime? Bria Cratty & Jack de la Parra 

01 THE PROBLEM 



2 

###### Men’s World Cup 2018 Scoring Percentages 



<!-- Start of picture text -->
Penalty Kick Scoring Regular Play Scoring within the Box<br>Number of PKs 29 Shots Taken within the 18 940<br>PK Goals Scored 22 Goals Scored 111<br>Scoring Percentage 75.86% Scoring Percentage 11.81%<br>3<br><!-- End of picture text -->

###### Expected Goals for Open Play Shots Men’s World Cup 2018 



4 



### Goal: 

- Re-configure the penalty kick to make for a more fair penalty kick opportunity ○ Reshape or move the location of the kick 

5 

## 02 

### BUILDING THE MODEL 

6 



##### Model Objectives 

- No change in box shape 

- Model for how expected goals change at different penalty kick distances and angles 

   - Calibrate model to ~75% for current penalty kick distance and angle 

- Find a new location and angle with reduced expected goals 

7 

##### Generalized Additive Model 

- Beta family, logit link 

- Used shot data excluding penalty kicks 

   - 1638 observations 

- Original Model: 

   - Used distance to goal, angle to goal and distance to closest defender 

   - Not predicting correctly for PK 

- Considered adding defenders behind ball variable to the model 

   - Decide between linear or smoothed term 

8 

###### Smoothing Spline More Appropriate for Defenders Behind Ball 



● Seems to have an exponential relationship ○ Not captured linearly ● K value of 9 not needed 

9 

##### Final Model 

- Generalized Additive Model 

   - Response: Statsbomb Expected Goals 

   - ○ Predictors 

      - Distance to closest defender, k = 9 

      - Angle to goal, k = 9 

      - Distance to goal, k = 9 

      - Defenders Behind Ball, k= 3 

- Prediction for Current PK: 

   - 74% 

10 



11 



03 

### CONCLUSIONS 

12 

###### The Penalty Arc 



- Arc 18 yards from goal, 

outside marks at 50° 

- If fouled outside arc, brought 

into closest mark 

- If fouled in arc, placed on arc at horizontal location of the foul 

13 

# THANKS & QUESTIONS? 

14 


