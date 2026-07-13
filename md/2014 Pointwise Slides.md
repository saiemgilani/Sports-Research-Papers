<!-- source: 2014 Pointwise Slides.pdf -->

POINTWISE: Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data Dan Cervone, Alex D’Amour, Luke Bornn, and Kirk Goldsberry (Harvard University) 















































# Introducing Expected Possession Value 















# EPV Defined 

Expected possession value (EPV) is the **number of points** the offense is **expected** to score by the we end of the possession, given **everything** know **now** . 

- **Points:** The currency of the NBA. 

- **Expected:** On average, with “luck” removed. 

- **Everything:** Full resolution spatial information. 

- **Now:** Any moment in time. 







# Calculating EPV 

### REGRESSION? 

### MARKOV CHAINS? 







# EPV is a path average 













<!-- Start of picture text -->
+<br><!-- End of picture text -->



<!-- Start of picture text -->
…<br><!-- End of picture text -->













# What happens next? 



**Raw data** 

**Dynamics layer Microtransitions “Action” layer Macrotransitions** 

**Combined Value layer** 







# The math 









# Transition models 

Microtransitions model dynamics: forecast future player locations based on velocities, accelerations 



KALMAN FILTER 

Macrotransitions model actions: predict changes in ball behavior such as passes, shots, turnovers 





<!-- Start of picture text -->
COMPETING RISKS<br>HAZARD<br><!-- End of picture text -->

Coarsened Markov Chain: computes expected possession value given the observed macrotransition 







# Weaving our models together 



Microtransition model simulates small-scale evolution until the macrotransition model predicts and values a pass, shot, or turnover event. 









# Systematic treatment of space 











<!-- Start of picture text -->
Which court locations have the<br>SITUATIONAL EFFECTS<br>strongest effect on my chance of<br><!-- End of picture text -->



<!-- Start of picture text -->
i  = PLAYER<br>attempting a shot?<br>j  = EVENT TYPE<br><!-- End of picture text -->







# Space is sparse 



<!-- Start of picture text -->
I’m the best<br>corner 3 shooter<br>in the NBA<br><!-- End of picture text -->



<!-- Start of picture text -->
RAY ALLEN<br>Yeah? Let’s<br>see the data…<br><!-- End of picture text -->











# Dwight Howard’s neighbors 



<!-- Start of picture text -->
Brook  JaVale  Jason  Nene  Jermaine<br>Lopez  McGee  Maxiell  Hilario  O’Neal<br>Andrew  Carlos<br>Bynum  Dwight  Boozer<br>Howard<br>Jeremy  Taj<br>Tyler  Gibson<br>Al  Bismack  Andrew  Hilton  Ognjen<br>Jefferson  Biyombo  Nicholson  Armstrong  Kuzmic<br><!-- End of picture text -->

# Model checking 

Unit testing: Verify small sections of code block by block. 

Internal replication: Independent and redundant data and results checks. 

our models other models 



PREDICTED SHOT % 

Cross entropy: predicted probabilities and observed outcomes (out of sample). Lower is better. 

Calibration plot: predicted vs. observed shot make probabilities (out of sample). Should lie on y = x line. 







# Model checking 

THE EYE TEST 







## EPVmetrics: 

## A new microeconomics for the NBA 









# Best decision-makers? EPV-Added 

##### TOP 10, 2013-14 

BOTTOM 10, 2013-14 

|**NAME**|**EPVA**||**NAME**|**EPVA**|
|---|---|---|---|---|
|Jose Calderon|+3.36|JOSE<br>CALDERON|Josh Smith|-2.23|
|LeBron James|+2.77||Brandon Jennings|-1.75|
|Dirk Nowitzki|+2.54||Gerald Henderson|-1.72|
|Channing Frye|+1.90||Paul Pierce|-1.58|
|Chandler Parsons|+1.85||Ricky Rubio|-1.58|
|Kyle Lowry|+1.71||Victor Oladipo|-1.39|
|Al Horford|+1.66||Jeff Teague|-1.29|
|Kyle Korver|+1.66|JOSH|Steve Blake|-1.27|
|Kevin Durant|+1.63|SMITH|Evan Turner|-1.19|
|Wesley Matthews|+1.57|(min 500 touches)|Tayshaun Prince|-1.17|









# Selfish shooters? Shot satisfaction 

TOP 10, 2013-14 

BOTTOM 10, 2013-14 

|**Name**|**Shot Sat**||**Name**|**Shot Sat**|
|---|---|---|---|---|
|Jose Calderon|+0.29|JOSE<br>CALDERON|Kevin Garnett|-0.04|
|Andre Iguodala|+0.28||Ricky Rubio|-0.04|
|Martell Webster|+0.26||Tayshaun Prince|-0.04|
|Lance Stephenson|+0.25||Tim Duncan|-0.01|
|Kyle Korver|+0.25||Cody Zeller|-0.01|
|Spencer Hawes|+0.25||LaMarcus Aldridge|-0.01|
|LeBron James|+0.25||Marc Gasol|+0.01|
|Jodie Meeks|+0.24|KEVIN|Brian Roberts|+0.01|
|Kawhi Leonard|+0.23|GARNETT|Jerryd Bayless|+0.02|
|Darren Collison|+0.23|(min 500 touches)|Jeff Teague|+0.03|









# More EPVmetrics 

SITUATIONAL OFF BALL 

EPV-added over specific player. Pass satisfaction. 

Screens, cuts. Who gets credit? 

DEFENSE 

Lowering EPV. Most valuable option. 

TURNING POINT 







# Limitations and the way forward 

TRACKING Players aren’t (x,y) points. DETAILS SHOT CLOCK, FOULS, DEFENSIVE MATCHUPS, SCREENS, FAST BREAKS, PICK AND ROLLS, END OF GAME SITUATIONS, IN-GAME WIN PROBABILITY, MOMENTUM, TRADE VALUES, PLAYER EVOLUTION,, … MORAL Big data? Bigger questions. Better models. 







# THANK YOU 



#### ALEX FRANKS 



ANDREW MILLER BRIAN KOPP, CARL MORRIS, EDOARDO AIROLDI, NATESH PILLAI 








