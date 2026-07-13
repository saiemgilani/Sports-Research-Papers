<!-- source: library/conferences/New England Symposium on Statistics in Sports/2023/2023 - Leveraging PFF Data to Identify Off-the-Ball Runs in Soccer through NFL Route Running - Unknown Authors.pdf -->



# **Leveraging PFF Data to Identify Off-the-Ball Runs in Soccer through NFL Route Running** 



Alexander Schram, Amelia Probst, Rory Breslin 

## **Introduction** 

We aim to connect (American) football and soccer by spotting off-the-ball runs in soccer, akin to NFL routes. These runs, executed by players without the ball, aim to exploit gaps in defense and create passing opportunities. While NFL routes are systematically labeled, off-the-ball runs in soccer lack such categorization. Our study employs machine learning techniques trained on labeled NFL route data to identify and categorize soccer off-the-ball runs. 

## **Data** 

Our football dataset focuses on the 2021 NFL season's week 1, merging NFL's Next Gen Stats (NGS) and PFF Play-by-Play data. To align with soccer, we analyze the first 3.0 seconds after the snap and select specific football routes (xo, xl, xd, x6, 1, 2, 3, 4, 6, 7, 8, 9, h2, h3, h8, h9) that have parallels in soccer. Our soccer dataset, sourced from Sportlogiq broadcast tracking data and PFF event data for the 2022-2023 Premier League season, comprises three high-quality games: Manchester United - Arsenal, Everton - Wolverhampton Wanderers, and Arsenal - Bournemouth. To align datasets, we introduce "soccer snaps" for consecutive events involving ball possession. 

## **Method** 

We enhance each NGS frame with three features: receiver-passer distance (in yards), angle between them (in degrees), and receiver speed (in yards per second). These features cover 0.0 to 3.0 seconds after the snap, resulting in 93 features (31 distances, 31 angles, 31 speed values). A Random Forest model predicts route types after training on 2161 labeled routes. 

## **Results** 

Model performance is summarized in Table 1, with an overall accuracy of 0.73, indicating an average 73% correct prediction rate for routes. Specific route types show varying precision, recall, and F1-scores, with routes 1, 6, h2, h3, h8, and xd performing well, and 8 and xl encountering challenges. 

## **Discussion** 

To boost model performance, we plan to expand our football dataset, particularly for route types with low support. Additional features, such as passer-receiver location and defender data, are considered. Transitioning to a Convolutional Neural Network (CNN) may enhance accuracy, given CNNs' proficiency in capturing spatial relationships, aligning with our goal of analyzing player movements and trajectories. 







<!-- Start of picture text -->
75+<br>Full Time Employees<br>S<br>N<br>A<br>P<br><!-- End of picture text -->





<!-- Start of picture text -->
Q<br>B<br><!-- End of picture text -->







<!-- Start of picture text -->
E<br>N<br>D<br><!-- End of picture text -->





PFFA Acquisition LLC proprietary and confidential information 


