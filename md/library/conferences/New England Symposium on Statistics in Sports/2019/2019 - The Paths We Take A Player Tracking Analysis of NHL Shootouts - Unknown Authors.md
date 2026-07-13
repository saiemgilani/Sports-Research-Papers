<!-- source: library/conferences/New England Symposium on Statistics in Sports/2019/2019 - The Paths We Take A Player Tracking Analysis of NHL Shootouts - Unknown Authors.pdf -->







|Nick Czuzoj-Shulman<br>  <br><br> <br>**THE PATHS WE TAKE:**<br>**A PLAYER TRACKING ANALYSIS OF NHL SHOOTOUTS**|
|---|
|Sportlogiq, Montreal, Quebec, Canada|<br>nick<br>@sportlogiq.com |@SLiQ_Nick94|
|●The data are made up of a set of<br>1,154 shootout attempts from the<br>2017-2018 and 2018-2019 NHL<br>regular seasons and were collected<br>using computer vision techniques<br>with tracking data.<br>**_In the NHL, the shootout takes place if a tie remains at the end of overtime by pitting a single shooter against the opposing goalie in a mano a mano bid to_**<br>**_seal the game. Given how important each point is in the standings, finding a competitive advantage in these scenarios could be the difference between making_**<br>**_the playoffs and ending the season early. Research on shootouts has typically measured shooting success rates based on eventing data and observable aspects_**<br>**_of the shootout attempt. We consider these along with tracking the paths and changes in shooter speed and acceleration during their attempt._**<br>●The trajectories were smoothed with spline interpolation and clustered<br>into 6 groups with functional cluster centres modelled as Bézier curves.<br>●Clustering was run on shooter paths from the blue line to the shot or deke<br>location, as this allowed for more tracks to be clustered.<br>●The grouped trajectories were analyzed along with the remaining shot<br>features to determine optimal skating paths and derive new insights based<br>on where skaters travel on their shootout attempts.<br>●The features comprise shooter and<br>goalie spatiotemporal and trajectory<br>information along with contextual<br>attributes<br>such<br>as<br>player<br>and<br>goaltender handedness, dekes, goal<br>information, and contexts such as<br>shootout rounds and scores.<br>**Dataset**<br>**Methods**<br>**Abstract**|
|**Slow**<br>**Fast**<br>**VGK     TBL**<br>**Saves    Goals**|
|8<br>2<br>1<br>0|
|**X= Saves**<br>⬤ **= Goals**<br>On the left:Player trajectories from a shootout<br>game between the Tampa Bay Lightning (0 for 3)<br>and the Vegas Golden Knights (1 for 3) in<br>February 2019.<br>On the right:10 of Jonathan Huberdeau’s shootout<br>f h l  NHL  Th|
|attempts rom te ast two  seasons. e<br>attempts that were saved are shown heading<br>toward the left, whereas goals are shown scoring<br> <br>J. Huberdeau|
|on the net on the right.|
|**Clusters**|
|1<br>2<br>3|
|Cluster 1 consists of attempts where the shooter takes a<br>wide path crossing the blue line near the left face-off dot,<br>and attacking the net from the goalie’s right-hand side.<br>Cluster 2 is similar to Cluster 1, however these paths are<br>narrower, with players staying inside the face-off dots and<br>taking more direct approaches from the goalie’s right.<br>Cluster 3 is almost a mirror of Cluster 1, with players<br>approaching wide and from the goalie’s left. There is,<br>however, a curve at the end driving in towards the net.<br>4<br>5<br>6|
|Cluster 4 has the straightest route as the shooters take a<br>slight curve, but don’t skate as wide or change the angles<br>on the goalie nearly as much as the other clusters.<br>Cluster 5’s routes attack from the goalie’s left side, but are<br>narrower than Cluster 3. These are similar to a mirror of<br>Cluster 2, but also feature a curve at the tail.<br>Cluster 6 consists of a slight but meaningful curve to the<br>goalie’s left, appearing similar to Cluster 5, but with<br>trajectories traveling more in the centre of the ice.|
|**Clusters Results**|
|The results table to the left features a<br>breakdown of each of the 6 clusters,<br>looking<br>at<br>success<br>rates,<br>shooter<br> <br>**Cluster**<br>**1**<br>**2**<br>**3**<br>**4**<br>**5**<br>**6**<br>**Total**<br>**Description**<br>Wide Left<br>Narrow Left<br>Wide Right<br>Down the Middle<br>Narrow Right<br>Right Dip<br>**Num. of Attempts**<br>173 (15.0%)<br>243 (21.1%)<br>188 (16.3%)<br>212 (18.4%)<br>219 (19.0%)<br>119 (10.3%)<br>1,154<br>**Shooting %**<br>329%<br>329%<br>309%<br>278%<br>256%<br>328%<br>302%|
|handedness, best and worst performers, as<br>well as the most frequent shooters and<br>goalies in each group.<br> <br>.<br>.<br>.<br>.<br>.<br>.<br>.<br>**Left-Hand Sh %**<br>31.7%<br>29.7%<br>30.0%<br>24.2%<br>25.0%<br>33.7%<br>28.7%<br>**Right-Hand Sh %**<br>33.6%<br>34.9%<br>34.2%<br>31.0%<br>26.9%<br>26.7%<br>32.3%<br>|
|<br>●Right-handed shooters performed better<br> <br>**Best Shooter***<br>M Cammalleri (4/5)<br>M Scheifele (4/5)<br>A Matthews (4/8)<br>P Byron (4/8)<br>T Bozak (5/8)<br>C Atkinson (3/5)<br>A Galchenyuk (2/5)<br>V Hedman (4/5)<br>M Cammalleri (4/5)<br>M Scheifele (4/5)|
|overall than left-handed (although it’s<br>worth noting this was mostly against<br>left-gloved goalies as well).<br>**Worst Shooter***<br>R Ellis (1/6)<br>J Silfverberg (0/5)<br>J Voracek (2/5)<br>M Zuccarello (2/5) <sup>D Perron (0/5)</sup><br>C Mittelstadt (2/6)<br>K Fiala (0/5)<br>J Silfverberg (0/6)<br>J Slavin (0/6)<br>J van Riemsdyk (0/6)<br>|
|●Based on the clusters, changing the<br>M Koivu (0/6)|
|<br>angles for the goalie and skating to the<br>’<br>**B Gli***<br>F Ad /6<br>B Holtby (5/5)<br>C Hllbk /<br>T Gi 8/9<br>F Andersen (8/8)<br>P Ri /<br>J Howard (6/6)<br>C Hllbk /<br>F Ad /<br>M Sbb 13/13|
|side of ones backhand appear to give<br> <br>**est oae**<br>nersen (5)<br>eeuyc (55)<br>P Rinne (5/5)<br>ress ()<br>nne (77)<br>J Howard (6/6)<br>eeuyc (55)<br>A Khudobin (5/5)<br>nersen (55)<br>uan ()|
|shooters a higher chance of scoring.<br>●At the player level, 5 of the 6 most<br> <br> <br> <br>**Worst Goalie***<br>M Smith (2/5)<br>A Raanta (1/5)<br>M Smith (2/5)<br>M Jones (2/6)<br>H Lundqvist (2/5)<br>P Rinne (4/7)<br>M Condon (3/8)|
|frequent<br>shooters<br>performed<br>above<br>averae in their resective clusters<br>**Frequent Shooter**<br>A Panarin (5/8)<br>M Zibanejad (5/10) A Matthews (4/8)<br>T Seguin (5/9)<br>K Shattenkirk (4/7)<br>F Nielsen (1/8)<br>K Turris (6/15)|
|g   p ,<br>h F Nil  1f8 i<br>**Frequent Goalie**<br>J Markstrom (6/9)<br>M Jones (8/11)<br>M Jones (6/10)<br>H Lundqvist (8/10)J Markstrom (10/12)P Rinne (4/7)<br>J Markstrom (34/47)|
|owever, rans esen was -or- n<br>his_Right Dip_attempts.<br> <br> <br> <br> <br>     <br> <br>* denotes the best and worst shooters/goalies with a minimum of 5 attempts taken/faced for that cluster|





<!-- Start of picture text -->
shootout rounds and scores.<br>Slow<br>VGK     TBL<br>1 0<br>X<br>On the left:<br>February 2019.<br>On the right:<br><!-- End of picture text -->



<!-- Start of picture text -->
on where skaters travel on their shootout attempts.<br>Saves    Goals<br>8 2<br>J. Huberdeau<br><!-- End of picture text -->




