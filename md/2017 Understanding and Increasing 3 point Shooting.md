<!-- source: 2017 Understanding and Increasing 3 point Shooting.pdf -->



# **A   data-­‐driven   method   for   understanding   and   increasing 3-­‐point   shooting   percentage** 

#### Rachel   Marty   and   Simon   Lucey 

University   of   California,   San   Diego   and   Carnegie   Mellon   University 

Emails: <u>ramarty@ucsd.edu,   slucey@cs.cmu.edu</u> 

### Abstract 

Although   3-­‐point   shooting   is   an   essential   aspect   of   winning   games,   shooting   percentages   have remained   stagnant   for   decades.   Here,   we   analyze   6   shooter   factors   from   over   1.1   million   3-­‐point   shots captured   by   the   Noah   shooting   system   to   quantitatively   define   high   percentage   shooting   and   shooter improvement.   We   find   significant   associations   between   all   of   these   6   shooter   factors   and   shooting   percentage. Furthermore,   we   use   the   interaction   of   these   factors   to   define   the   region   in   the   hoop   where   shots   are guaranteed   to   score.   Of   the   6   factors,   4   are   directly   actionable   using   new   technologies   for   instant   feedback. We   use   machine   learning   to   predict   shooting   percentage   within   1.5%   using   only   these   4   factors   as   input. Finally,   we   grouped   players   by   their   proficiency   at   these   4   factors   and   show   case   studies   about   the   dissimilar training   approaches   that   will   lead   to   optimal   improvement   for   two   of   these   groups. 

## **1.   Introduction** 

In   the   2015-­‐2016   season,   NBA   teams   averaged   24.1   3-­‐point   attempts   per   game,   with   the Golden   State   Warriors   topping   the   league   with   an   unprecedented   31   attempts   per   game   [1,2].   In   the last   15   years,   the   number   of   3-­‐point   attempts   across   the   league   has   rapidly   increased;   however,   the average   3-­‐point   shooting   percentage   has   remained   constant   over   the   past   20   years   [1].   With   the increased   importance   of   the   3-­‐point   shot   to   winning   games,   why   have   players   been   unable   to increase   their   yield? 

In   the   past,   a   number   of   theoretical   papers   have   been   written   which   propose   ways   of increasing   yield   from   basketball   shots   [3,4,5],   and   some   methods   have   been   proposed   for   collecting and   analyzing   multi-­‐factor   3-­‐point   shot   data   [6,7]. 

In   this   paper   we   move   from   theoretical   ideas   all   the   way   to   actionable   training   methods based   upon   proven   techniques   using   instant   verbal   feedback.   The   foundation   for   this   paper   is   the measurement   of   1.1   million   3-­‐point   shots   from   over   160   players,   gathering   information   on   6   ball dynamics   factors   in   addition   to   player   identification,   shot   location   and   make-­‐miss.      We   use   these factors   to   quantitatively   define   the   zone   in   the   hoop   plane   where   shots   score,   and   then   select   the   4 trainable   factors   which   accurately   predict   shooting   percentage.   Finally,   we   cluster   players   based   on the   4   factors   allowing   each   individual   player   to   take   the   most   efficient   path   to   improve   their   3-­‐point shooting   percentage   using   instant   verbal   feedback   training   techniques. 





2017   Research   Papers   Competition Presented   by: 

1 



## **2.   Data   collection   and   attribute descriptions** 

#### **2.1   Data   collection** 

A   Noah   shooting   system   was   placed   approximately   13 feet   above   the   basketball   hoop   to   gather   real   time   data   on each   shot   (Figure   1).   This   sensor   system   collected   the   shot data   of   4   NBA   teams,   1   WNBA   team,   4   college   teams   and   4 high   school   teams   allowing   us   to   collect   data   on   about   1.1 million   3-­‐point   shots   in   2016. 

#### **2.2   Shot   attribute   descriptions** 

For   each   shot   taken,   the   sensor   system   collects   data about   how   and   where   the   basketball   shot   enters   the   plane   of the   hoop.   We   analyze   three   attributes   of   shot   entry:   Left-­‐ Right,   Depth   and   Angle.   Since   3-­‐point   shots   are   taken   from   all positions   around   the   3-­‐point   curve,   these   shot   entry attributes   are   measured   from   the   perspective   of   the   shooter; the   point   on   the   hoop   closest   to   the   shooter   is   always   defined as   the   front   of   the   hoop.   In   the   figures,   the   front   of   the   hoop   is shown   with   a   green   dot. 



<!-- Start of picture text -->
Sensor<br><!-- End of picture text -->



<!-- Start of picture text -->
Sensor<br><!-- End of picture text -->

Figure   1:   Schematic   of   Noahlytics   sensor system   used   to   capture   shot   data. 



<!-- Start of picture text -->
Figure   1:   Schematic   of   Noahlytics   sensor<br>system   used   to   capture   shot   data.<br><!-- End of picture text -->

Left-­‐Right   is   the   left   to   right   deviation   of   the   shot   at   the   hoop.   First   an   imaginary   line   is drawn   from   the   shooter   through   the   center   of   the   hoop,   defining   a   perfectly   straight   shot.   Then   the flight   of   the   shot   is   recorded   as   the   parabola   drawn   through   the   center   of   the   ball   during   the   flight of   the   shot.   Next   the   sensor   measures   the   point   where   the   ball   flight   parabola   crosses   the   plane   of the   hoop.   The   Left-­‐Right   attribute   is   the   distance   between   the   straight   shot   line   and   the   point where   the   ball   actually   crosses   the   hoop   plane   (Figure   2A).   Since   the   hoop   has   a   9”   radius,   a   shot which   lands   exactly   on   the   leftmost   part   of   the   hoop   from   the   perspective   of   the   shooter   has   a   Left-­‐ Right   value   of   -­‐9”,   a   straight   shot   has   a   Left-­‐Right   value   of   0”   and   a   shot   which   lands   on   the rightmost   part   of   the   hoop   has   a   Left-­‐Right   value   of   +9”. 

Figure   2:   Visualizations   of   shot   attributes   at   the   plane   of   the   hoop   -­‐   A)   Left-­‐Right   attribute,   B)   Depth attribute   and   C)   Angle   attribute. 



<!-- Start of picture text -->
Figure   2:   Visualizations   of   shot   attributes   at   the   plane   of   the   hoop   -­‐   A)   Left-­‐Right   attribute,   B)   Depth<br>attribute   and   C)   Angle   attribute.<br><!-- End of picture text -->



<!-- Start of picture text -->
Straight<br>shot<br>Crossing<br>point<br>Left-right<br>attribute<br>(inches)<br><!-- End of picture text -->



<!-- Start of picture text -->
Depth<br>attribute<br>(inches)<br><!-- End of picture text -->





2017   Research   Papers   Competition Presented   by: 



2 



Depth   is   the   entry   depth   of   the   shot   into   the   hoop.   First   the   front   of   the   hoop   is   defined   as the   point   on   the   hoop   closest   to   the   shooter.   Then   the   tangent   to   the   hoop   is   drawn   through   the front   of   the   hoop   point.   Next   the   sensor   measures   the   point   where   the   ball   flight   parabola   actually crosses   the   plane   of   the   hoop.   The   Depth   attribute   is   the   distance   between   the   front   of   the   hoop tangent   line   and   the   point   where   the   ball   crosses   the   hoop   plane   (Figure   2B).   Since   the   hoop   has   a diameter   of   18”,   a   straight   shot   which   lands   directly   on   the   front   of   the   hoop   from   the   perspective   of the   shooter   has   a   Depth   value   of   0”   and   a   straight   shot   which   lands   directly   on   the   back   of   the   hoop has   a   Depth   value   of   18”. 

Angle   is   the   entry   angle   of   the   shot   into   the   hoop.   First   the   flight   of   the   shot   is   recorded   as the   parabola   drawn   through   the   center   of   the   ball   during   the   flight   of   the   shot.   Then   a   line   is   drawn as   a   tangent   to   the   ball   flight   parabola   as   it   crosses   the   hoop   plane.   The   Angle   attribute   is   the   angle between   the   hoop   plane   and   the   tangent   to   the   ball   flight   parabola   at   the   hoop   plane   (Figure   2C). For   example,   a   relatively   flat   shot   can   have   an   Angle   value   of   36°   and   a   relatively   high   arcing   shot ° can   have   an   Angle   value   of   55 . 

In   this   paper,   we   use   these   three   attributes   of   shot   entry   to   describe   6   distinct   factors   of shooters. 

## **3.   Six   shooter   factors   of   high   percentage   shooting** 

#### **3.1   Left-­‐Right   value   and   Left-­‐Right   consistency** 

The   Left-­‐Right   value   of   the   1.1   million   3-­‐point   shots   captured   follows   a   symmetric distribution   around   the   center   of   the   hoop   (Figure   3A).   Shots   that   are   more   precise   to   the   center   of the   hoop   have   a   higher   probability   of   scoring   regardless   of   any   other   factor.   Shooters   who   have   a systematic   Left-­‐Right   value   error   can   easily   see   this   problem   with   their   eyes   and   correct   their future   shots   accordingly,   thus   it   is   not   surprising   that   even   though   individuals   may   have   a   left   or right   tendency,   the   overall   population   had   a   median   Left-­‐Right   value   of   0”. 

Next   we   measured   the   Left-­‐Right   consistency   of   individual   shooters.   We   defined   consistency as   the   average   absolute   deviation   from   the   median.   We   decided   to   use   absolute   deviation   rather than   the   traditional   squared   to   minimize   the   impact   of   outliers.   Shooters   with   consistent   Left-­‐Right aim   tend   to   make   a   higher   percentage   of   shots   than   shooters   with   inconsistent   Left-­‐Right   aim (Spearman   rho   =   -­‐0.88,   Figure   3A). 



<!-- Start of picture text -->
A B Shooting<br>120K 90 Percentage<br>Spearman rho = -0.88 100%<br>80<br>100K 90%<br>70 80%<br>80K<br>60 70%<br>60K 50 60%<br>50%<br>40<br>40K<br>40%<br>30<br>20K 30%<br>20<br>20%<br>0 −10 -9 -8 -7 -6 −5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 10 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 10%<br>Left-Right (Inches) Left-Right Consistency Player with  0%<br>> 200 shots<br>Number of Shots Taken Shooting Percentage<br><!-- End of picture text -->

Figure   3:   A)   We   show   the   distribution   of   the   Left-­‐Right   values   for   all   3-­‐point   shots   measured.   The   color   of each   bar   corresponds   to   the   make   percentage   at   each   Left-­‐Right   value.   B)   We   show   the   correlation   between Left-­‐Right   consistency   and   3-­‐point   shooting   percentage   for   individual   shooters. 



<!-- Start of picture text -->
Figure   3:   A)   We   show   the   distribution   of   the   Left-­‐Right   values   for   all   3-­‐point   shots   measured.   The   color   of<br>each   bar   corresponds   to   the   make   percentage   at   each   Left-­‐Right   value.   B)   We   show   the   correlation   between<br>Left-­‐Right   consistency   and   3-­‐point   shooting   percentage   for   individual   shooters.<br><!-- End of picture text -->





2017   Research   Papers   Competition Presented   by: 

3 



#### **3.2   Depth   value   and   Depth   consistency** 

Similar   to   the   Left-­‐Right   value,   the   Depth   value   of   the   1.1   million   3-­‐point   shot   population   is evenly   distributed   around   the   center   of   the   basket   at   9”   (Figure   4A).   However,   unlike   Left-­‐Right,   the highest   shooting   percentage   Depth   value   is   not   the   center   of   the   basket.   A   higher   percentage   of shots   are   made   when   they   enter   the   hoop   at   11”   behind   the   front   of   the   rim,   2”   deeper   than   the center.   (See   Highest   Percentage   arrow   in   Figure   4A.)   The   whole   population   across   skill   levels   from high   school   through   the   NBA   are   consistently   practicing   suboptimal   Depth   values.   This   striking information   will   be   discussed   more   later   in   the   paper. 

We   then   measured   Depth   consistency   for   individual   shooters.   As   with   Left-­‐Right consistency,   we   defined   consistency   as   the   average   absolute   deviation   from   the   median.   Regardless of   Depth   median   and   other   factors,   we   found   a   very   strong   correlation   between   a   player’s   Depth consistency   and   the   player’s   shooting   percentage   (Spearman   rho   =   -­‐0.89, Figure   4B). 



<!-- Start of picture text -->
Shooting<br>Highest Percentage<br>A 90K B 90 Spearman rho = -0.89 100%Percentage<br>80K 80 90%<br>70K 70 80%<br>60K 60 70%<br>50K 50 60%<br>40K 40 50%<br>30K 40%<br>30<br>20K 30%<br>20<br>10K 20%<br>0 10<br>0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 10%<br>Depth (Inches) Depth Consistency  Player with  0%<br>> 200 shots<br>Number of Shots Taken Shooting Percentage<br><!-- End of picture text -->

Figure   4:   A)   We   show   the   distribution   of   Depth   values   for   all   3-­‐point   shots   measured.   The   color   of   each   bar corresponds   to   the   make   percentage   at   each   Depth   value   with   the   highest   shooting   percentage   at   11”   Depth value.   B)   We   show   the   correlation   between   Depth   consistency   and   shooting   percentage   for   individual   shooters. 



<!-- Start of picture text -->
Figure   4:   A)   We   show   the   distribution   of   Depth   values   for   all   3-­‐point   shots   measured.   The   color   of   each   bar<br>corresponds   to   the   make   percentage   at   each   Depth   value   with   the   highest   shooting   percentage   at   11”   Depth<br>value.   B)   We   show   the   correlation   between   Depth   consistency   and   shooting   percentage   for   individual   shooters.<br><!-- End of picture text -->

#### **3.3   Angle   value   and   Angle   consistency-­‐** 

The   mode   of   the   Angle   values   in   the   1.1   million   3-­‐point   shot   population   is   45°  with   a   slightly asymmetrical   distribution   (Figure   5A).   While   the   shooting   percentage   of   shots   in   the   mid-­‐40s   is higher   than   the   surrounding   Angles,   the   decrease   in   shooting   percentage   is   not   the   precipitous   drop we   observed   in   the   Left-­‐Right   value   and   the   Depth   value. 

However,   when   individual   players   are   scored   based   on   the   consistency   of   Angle,   a   clear correlation   emerges   between   the   Angle   consistency   and   shooting   percentage   (Spearman   rho=-­‐0.63, Figure   5B).   Angle   consistency   is   an   important   factor   as   will   be   discussed   in   more   detail   later   in   this paper. 







4 





<!-- Start of picture text -->
A 140K B 90 Shooting<br>Spearman rho = -0.63 Percentage<br>80 100%<br>120K<br>70 90%<br>100K<br>80%<br>60<br>80K 70%<br>50<br>60%<br>60K<br>40 50%<br>40K 30 40%<br>20K 20 30%<br>20%<br>0 10<br>36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 0.5 1.0 1.5 2.0 2.5 3.0 3.5 10%<br>Angle (Degrees) Angle Consistency Player with > 200 shots 0%<br>Number of Shots Taken Shooting Percentage<br><!-- End of picture text -->

Figure   5:   A)   We   show   the   distribution   of   Angle   values   for   all   3-­‐point   shots   measured.   The   color   of   each   bar corresponds   to   the   make   percentage   at   each   Angle   value.   B)   We   show   the   correlation   between   Angle   consistency and   shooting   percentage   for   individual   shooters. 



<!-- Start of picture text -->
Figure   5:   A)   We   show   the   distribution   of   Angle   values   for   all   3-­‐point   shots   measured.   The   color   of   each   bar<br>corresponds   to   the   make   percentage   at   each   Angle   value.   B)   We   show   the   correlation   between   Angle   consistency<br>and   shooting   percentage   for   individual   shooters.<br><!-- End of picture text -->

## **4.   Relationships   among   shooter   factors** 

#### **4.1   Angle   consistency   is   correlated   with   Depth   consistency** 

We   observe   a   high   correlation   (Spearman   rho   =   -­‐0.63)   between   Angle   consistency   and   the Depth   consistency   for   individual   shooters   (Figure   6).   Shooters   with   high   shooting   percentages   tend to   have   good   Angle   consistency   and   good Depth   consistency. 5.5 PercentageShootingShooting 



<!-- Start of picture text -->
5.5 PercentageShootingShooting<br>5.0 100%<br>90%<br>4.5<br>80%<br>4.0 70%<br>3.5 60%<br>50%<br>3.0<br>40%<br>2.5<br>30%<br>Spearman rho = -0.63<br>2.0 20%<br>0.5 1.0 1.5 2.0 2.5 3.0 3.5<br>Angle Consistency Player with  10%<br>> 200 shots 0%<br>Depth Consistency<br><!-- End of picture text -->

#### **4.2   Angle   median   is   a   key   determinant of   Depth   median   and   Depth consistency** 

The   data   from   the   1.1   million   shot population   revealed   a   surprising   but explainable   influence   which   Angle   median had   on   both   Depth   median   and   Depth consistency.      Figures   7A   and   7B   show   the same   data   but   with   the   y-­‐axis   expanded   in   7B. 

Figure   6:   We   show   a   high   correlation   between   Depth consistency   and   Angle   consistency   for   individual   players. 



<!-- Start of picture text -->
Figure   6:   We   show   a   high   correlation   between   Depth<br>consistency   and   Angle   consistency   for   individual   players.<br><!-- End of picture text -->

Depth   median   -­‐   For   the   population,   a shot   goes   deepest   in   the   basket   when   shot   at   an 

Angle   value   of   42°.   The   Depth   median   value   at   36°  is   about   8”   and   increases   smoothly   to   about   10” at   42°  and   then   decreases   smoothly   to   about   5”   at   55°.   Further,   the   incremental   change   in   Depth value   for   each   change   in   Angle   value   is   very   small   around   42°,   but   the   incremental   change   in   Depth value   increases   faster   the   further   you   move   away   from   42°. 

Depth   consistency   -­‐   For   the   population,   Depth   is   most   consistent   at   42°.   Depth   consistency is   poor   at   36°  and   improves   smoothly   to   a   tight   Depth   consistency   at   42°  and   then   deteriorates smoothly   to   a   poor   Depth   consistency   at   55°.   Remarkably,   these   trends   in   Depth   consistency   hold 





2017   Research   Papers   Competition Presented   by: 

5 



true   across   all   quartiles   of   the   data   as   you   can   see   in   the   full   range   of   shots   shown   in   Figure   7A.   The 2<sup>nd</sup> and   3<sup>rd</sup> quartile   ranges   can   be   inspected   more   closely   in   Figure   7B. 



Figure   7:   A)   A   boxplot   showing   the   distribution   of   Depth   values   for   each   Angle   value   across   all   measured   shots.   The box   denotes   the   middle   two   quartiles   of   the   distribution   and   the   wings   represent   the   5<sup>th</sup> and   95<sup>th</sup> percentiles.   B)   Same data   with   expanded   Y-­‐axis   to   allow   closer   inspection   of   the   Depth   median   and   Depth   consistency   across   Angle   values. 



<!-- Start of picture text -->
Figure   7:   A)   A   boxplot   showing   the   distribution   of   Depth   values   for   each   Angle   value   across   all   measured   shots.   The<br>box   denotes   the   middle   two   quartiles   of   the   distribution   and   the   wings   represent   the   5 th    and   95 th    percentiles.   B)   Same<br>data   with   expanded   Y-­‐axis   to   allow   closer   inspection   of   the   Depth   median   and   Depth   consistency   across   Angle   values.<br><!-- End of picture text -->

Figures   7A   and   7B   are   not   typical   of   normal   distributions   associated   with   human performance,   so   how   can   these   unusual   patterns   be   explained?   The   laws   of   physics   hold   the answer.      Projectile   physics   calculates,   for   example,   that   players   shooting   a   3-­‐point   shot   with constant   release   velocity   will   maximize   their   shot   depth   at   a   42°  Angle.   If   they   shoot   the   ball   higher than   42°,   Depth   will   decrease.   If   they   shoot   the   ball   flatter   than   42°,   Depth   will   also   decrease.   And the   further   the   Angle   deviates   from   42°,   the   shorter   the   Depth.   This   principle   of   physics   is described   further   in   the   Appendix. 

Although   a   42°   Angle   value   optimizes   Depth   consistency,   it   is   not   the   optimal   Angle   to maximize   shooting   percentage.   This   will   be   made   clear   in   the   next   section   which   defines   the   GMZ. 

## **5.   Defining   the   Guaranteed   Make   Zone   (GMZ)   as   a   function   of shooter   factors** 

We   next   explored   how   shooter   factors   interact   to   explain   high   percentage   shooting.   We found   that   the   family   of   shots   for   each   Angle   value   has   a   different   scoring   percentage   at   each   Depth value.   For   example,   a   shot   with   a   high   Angle   (high   arc)   will   be   less   likely   to   hit   the   front   rim   than   a low   Angle   shot   (flat   arc),   so   Angle   value   influences   whether   a   particular   Depth   value   will   score.   As an   illustrative   example,   we   selected   all   shots   with   an   Angle   value   of   45°,   the   most   common   in   the population,   and   then   produced   the   distribution   of   shooting   percentages   for   each   Depth   value   at   the 45°  Angle   (Figure   8A).   As   a   starting   point,   we   only   considered   straight   shots   with   a   Left-­‐Right   value of   -­‐2”   to   +2”.   Straight   shots   with   an   Angle   of   45°  which   cross   the   hoop   plane   at   a   Depth   value   of   7” to   14”   are   guaranteed   to   score   either   by   swishing   or   by   hitting   the   back   of   the   rim   and   deflecting down.   These   depths   are   shown   in   the   yellow   band.   The   shooting   percentages   in   the   yellow   zone   do not   quite   reach   100%   due   to   situations   such   as   shots   colliding   with   other   shots   during   practice sessions   or   sensors   which   had   not   been   upgraded   to   the   latest   version   at   the   time   the   shot   was taken.   For   our   data   analysis,   we   will   consider   all   depths   with   greater   than   90%   shooting percentage   to   be   defined   as   the   Guaranteed   Make   Zone   (GMZ).   Depths   outside   the   GMZ   have   a   low 



2017   Research   Papers   Competition Presented   by: 



6 



or   near   zero   chance   of   scoring   because   they   will   hit   the   rim   and   bounce   up   or   sideways.      For purposes   of   this   analysis,   the   percentage   of   shots   in   the   GMZ   to   total   shots   for   a   player   are   a   close approximation   to   their   shooting   percentage.   The   GMZ   for   the   45°  Angle   family   in   Figure   8A   is reflected   in   Figure   8B   as   shown   by   the   bracket. 

Each   Angle   family   has   a   slightly   different   distribution   of   make   percentages   for   each   Depth value.   By   creating   a   figure   similar   to   Figure   8A   for   all   Angles   from   35   degrees   to   55   degrees,   we created   a   GMZ   map   for   straight   shots   across   all   angles   and   depths   (Figure   8B).   Note   that   the   GMZ   is narrower   at   35°,   gets   wider   near   45°,   and   then   narrows   again   at   55°. 



Figure   8:   A)   We   show   the   make   percentage   at   each   Depth   value   for   straight   shots   with   an   Angle   value   of   45°.   B)   We show   the   Guaranteed   Make   Zone   (GMZ)   for   straight   shots   across   all   Angle   values. 

But   not   all   shots   are   straight, and   the   Left-­‐Right   value   also   impacts the   size   and   shape   of   the   GMZ.   To demonstrate   this   phenomenon,   we   split the   hoop   into   three   sections   according to   the   Left-­‐Right   value   (Figure   9A).   The yellow   band   represents   straight   shots within   2”   of   the   centerline   of   the   hoop. The   green   bands   represent   shots   that are   nearly   straight,   between   2”   and   4” from   the   centerline   of   the   hoop.   Finally, the   blue   bands   represent   shots   that enter   the   plane   of   the   hoop   between   4” and   5”   inches   from   the   centerline   of   the hoop.   As   the   Left-­‐Right   value   deviates from   straight,   the   GMZ   dramatically shrinks   (Figure   9B-­‐D).   Few   shooters consistently   shoot   only   in   the   yellow zone,   making   it   even   more   important that   shooters   consistently   shoot   the correct   Depth   value   for   their   shots   in order   to   increase   shooting   percentage. 





Figure   9:   A)   We   show   three   left-­‐right   regions   in   the   hoop   –   0   to   +/-­‐2, +/-­‐2   to   +/-­‐4   and   +/-­‐4   to   +/-­‐5.   B)   The   GMZ   for   –   0   to   +/-­‐2.   C)   The GMZ   for   +/-­‐2   to   +/-­‐4.   D) The   GMZ   for   +/-­‐4   to   +/-­‐5. 



<!-- Start of picture text -->
Figure   9:   A)   We   show   three   left-­‐right   regions   in   the   hoop   –   0   to   +/-­‐2,<br>+/-­‐2   to   +/-­‐4   and   +/-­‐4   to   +/-­‐5.   B)   The   GMZ   for   –   0   to   +/-­‐2.   C)   The<br>GMZ   for   +/-­‐2   to   +/-­‐4.   D) The   GMZ   for   +/-­‐4   to   +/-­‐5.<br>2017   Research   Papers   Competition<br><!-- End of picture text -->

2017   Research   Papers   Competition 

Presented   by: 



7 



## **6.   Overlaying   the   GMZ   on   factor   figures   to   draw   insights   on actionable   ways   to   increase   3-­‐point   shooting   percentage** 

A   key   objective   of   this   paper   is   to   improve   3-­‐point   shooting   percentage   by   identifying actionable   training   approaches.   Each   of   the   four   insights   described   below   can   be   implemented using   instant   verbal   feedback   training   techniques,   and   the   results   of   that   training   can   be   verified   by measuring   improvement   of   the   factors   in   game   situations. 

When   the   GMZ   from   Figures   9B   and   9D   overlay   the   Angle-­‐Depth   chart   from   Figure   7B,   it   is apparent   there   are   many   reasons   players   miss   shots.   The   actionable   factors   for   improving   3-­‐point percentage   are   Left-­‐Right   consistency,   Angle   median,   Angle   consistency   and   Depth   median. Although   Depth   consistency   would   appear   to   be   an   important   factor   to   increasing   shooting percentage,   it   is   not   directly   actionable   because   it   is   influenced   by   too   many   other   factors   including Angle   median   and   Angle   consistency.   Thus,   Depth   consistency,   like   shooting   percentage,   is considered   an   outcome   and   is   not   included   in   actionable   factors   for   predicting   or   improving shooting   percentage. 

#### **6.1   Left-­‐Right   consistency   is   key   to   widening   the   GMZ   to   increase   shooting percentage** 

Figure   3A   shows   that   of   the   1.1   million   shots,   only   35%   fall   within   the   -­‐2”   to   +2”   Left-­‐Right band   encompassed   in   the   yellow   GMZ   of   Figure   10A.   27%   of   the   shots   fall   5”   or   more   away   from the   centerline   creating   a   GMZ   with   few   or   zero   made   shot   opportunities   as   shown   by   the   blue   GMZ in   Figure   10B.   The   first   key   to   increasing   shooting   percentage   is   to   shoot   straight   so   a   player   is operating   in   the   yellow   GMZ   of   Figure   10A   rather   than   the   blue   GMZ   of   Figure   10B. 



Figure   10:   We   show   the   distribution   of   Depth   values   per   entry   Angle   A)   overlaid   with   the   yellow   GMZ   of   straight shots   and   B)   overlaid   with   the   blue   GMZ   of   +/-­‐   4   to   +/-­‐   5   Left-­‐Right   shots. 



<!-- Start of picture text -->
Figure   10:   We   show   the   distribution   of   Depth   values   per   entry   Angle   A)   overlaid   with   the   yellow   GMZ   of   straight<br>shots   and   B)   overlaid   with   the   blue   GMZ   of   +/-­‐   4   to   +/-­‐   5   Left-­‐Right   shots.<br><!-- End of picture text -->



2017   Research   Papers   Competition Presented   by: 



8 



#### **6.2   Angle   median   is   necessary   to   have   the   right   balance   of   Depth   consistency   and   size of   the   GMZ   to   increase   shooting   percentage** 

Of   the   162   shooters   shown   in   Figure   5A,   69%   had   an   Angle   median   between   43°  and   47°. Having   an   Angle   median   in   this   range   is   important   because   of   Angle   median’s   influence   on   Depth consistency   as   described   in   section   4.2   and   the   Appendix   as   well   as   Angle   median’s   influence   on   the size   of   the   GMZ   as   described   in   section   5.   A   42°  Angle   median   will   have   the   tightest   depth   control, but   a   narrower   GMZ.   A   47°   Angle   median   will   have   less   depth   control,   but   a   wider   GMZ.   Players with   Angle   median   in   the   range   between   43°  and   47°  are   most   able   to   fit   their   shots   into   the   GMZ and   thus   have   a   similar   shooting   percentage   all   other   factors   held   equal.   A   45°  Angle   median   is   the best   place   to   practice,   especially   for   less   proficient   shooters. 

#### **6.3   Angle   consistency   is   necessary   to   tighten   Depth   consistency   so   more   shots   can   be in   the   GMZ   and   increase   shooting   percentage** 

As   shown   in   Figure   6,   Angle   consistency   is   the   second   factor   necessary   to   tighten   Depth consistency.   Players   who   can   minimize   their   angle   variance   while   maintaining   constant   power   will shoot   their   shots   at   a   more   consistent   depth. 

#### **6.4   Depth   median   is   necessary   to   center   an   athlete’s   shots   in   the   GMZ   to   increase shooting   percentage** 

Figures   10A   and   10B   show   that   an   ideal   Depth   median   is   about   11.0”   because   that   will center   the   range   of   shot   depths   over   the   GMZ   to   maximize   shooting   percentage.   But   Figure   4A shows   that   the   population   of   1.1   million   shots   have   a   Depth   median   of   9.3”   which   is   1.7”   short   of   the ideal. 

Players   shoot   a   Depth   median   below   the   ideal   of   11”   partly   because   laws   of   physics   will cause   the   human   error   in   Angle   to   shorten   the   median   Depth   (see   Appendix).   The   laws   of   physics cannot   be   changed   with   improved   shooting   mechanics   or   improved   muscle   memory;   we   observe that   shot   Depth   median   is   a   consistent   problem   across   all   skill   levels   from   the   NBA   to   high   school. The   Depth   median   problem   can   be   minimized   by   shooting   an   Angle   median   in   the   mid-­‐40’s   (see 6.2)   with   great   Angle   consistency   (see   6.3)   and   aiming   for   11”   instead   of   simply   a   swish. 

## **7.   The   four   actionable shooter   factors   can   predict shooting   percentage** 

Next,   we   sought   to   determine   the capacity   of   the   four   actionable   shooter   factors to   predict   player   shooting   percentage.   Since we   previously   showed   Depth   consistency   is not   actionable   because   it   is   a   function   of   other factors   such   as   Angle   consistency   and   Angle median,   we   exclude   Depth   consistency   as   a factor.   Furthermore,   we   also   exclude   Left-­‐ 





<!-- Start of picture text -->
80<br>Spearman rho = 0.89<br>70<br>60<br>50<br>40<br>30<br>30 40 50 60 70 80<br>Actual Shooting Percentage<br>Predicted Shooting Percentage<br><!-- End of picture text -->



<!-- Start of picture text -->
Figure 11: A) We show the correlation between the actual<br>shooting percentage and the predicted shooting percentage<br>for the players in our test set.<br>2017   Research   Papers   Competition<br><!-- End of picture text -->

Figure 11: A) We show the correlation between the actual shooting percentage and the predicted shooting percentage for the players in our test set. 2017   Research   Papers   Competition Presented   by: 



9 



Right   median   because   shooters   can   generally   self-­‐correct   for   this   attribute.   Thus,   our   remaining factors   are   Angle   median,   Depth   median,   Angle   consistency   and   Left-­‐Right   consistency.   We   split   the 162   players   with   more   than   200   recorded   shots   into   a   training   and   a   testing   group.   We   used   cross validation   to   train   and   optimize   the   parameters   of   a   gradient   boosting   regressor.   Our   resulting model   had   100   estimators   and   a   learning   rate   of   0.1.   Our   predictions   on   our   test   set   received   a Spearman   correlation   of   0.89   between   the   actual   shooting   percentage   of   the   players   and   the predicted   shooting   percentage;   this   resulted   in   an   error   of   1.5%   (Figure   11). 

## **8.   Player   case   studies** 

#### **8.1   Cluster   players   on   improvement   potential** 

All   four   of   these actionable   shooter   factors can   be   improved   in   order to   increase   shooting percentage.   However, each   player   has   a   unique baseline   of   these   factors, so   improvement   of   a specific   factor   holds different   potential   for   each player.   To   quantify improvement   potential   for each   factor,   we   separated players   into   two categories   –   ‘Proficient’ and   ‘Not   Proficient’   –   for each   of   the   four   actionable factors.   We   grouped   the players   according   to   these factor   states   (Figure   12). There   are   15   groups.   The group   at   the   top   is   where all   actionable   factors   are ‘Not   Proficient’,   and   the group   at   the   bottom   is 



<!-- Start of picture text -->
Proficient<br>Not Proficient<br>Shooting<br>Percentage<br>0%<br>10%<br>20%<br>30%<br>40%<br>50%<br>60%<br>70%<br>80%<br>90%<br>100%<br>Median Median Angle<br>Angle  Depth Left-Right<br>Consistency Consistency<br> Proficiency in Actionable Factors<br>Individual Players Clustered According to<br><!-- End of picture text -->

Figure   12:   A   heat   map   showing   players   clustered   by   their   proficiency   at   the   four factors.   The   green   and   yellow   bar   represents   the   shooting   percentage   of   the individual   player. 



<!-- Start of picture text -->
Figure   12:   A   heat   map   showing   players   clustered   by   their   proficiency   at   the   four<br>factors.   The   green   and   yellow   bar   represents   the   shooting   percentage   of   the<br>individual   player.<br><!-- End of picture text -->

where   all   actionable   factors   are   ‘Proficient’.   Note   the   median   shooting   percentage   in   the   cluster with   all   ‘Not   Proficient’   is   39%   and   the   median   shooting   percentage   in   the   cluster   with   all ‘Proficient’   is   68%.   Next,   we   take   a   closer   look   at   two   case   studies   to   understand   the   improvement potential   of   players   with   specific   factor   expressions. 

#### **8.2   Player   case   studies** 

Player   X   is   a   47%   three-­‐point   shooter   during   practice.   She   is   ‘Proficient’   in   Angle   median and   Depth   median   and   ‘Not   Proficient’   in   Left-­‐Right   consistency   and   Angle   consistency.   Her   shot distribution   is   centered   on   her   GMZ,   yet   her   GMZ   is   severely   narrowed   by   her   Left-­‐Right inconsistency   (Figure   13A). By   focusing   on   her   Left-­‐Right   consistency,   she   will   expand   her   GMZ   and 





2017   Research   Papers   Competition Presented   by: 

10 



make   many   more   shots   regardless   of   her   Angle   and   Depth   inconsistency   (Figure   13B).   Through improvement   in   Left-­‐Right   consistency   alone,   she   can   expect   to   reach   a   3-­‐point   shooting   percentage of   56%   during   practice   once   she   reaches   a   level   of   ‘proficiency’,   an   overall   improvement   of   9%. Other   players   clustered   in   the   same   category   as   her   should   also   focus   on   Left-­‐Right   consistency   to optimize   their   path   to   improved   shooting   percentage. 



Figure   13:   A)   We   show   the   current   shot   distribution   and   current   GMZ   of   Player   X.   B)   We   show   improved,   wider   GMZ   of Player   X   if   Left-­‐Right   consistency   is   improved   to   ‘proficient’   resulting   in   more   shots   in   the   GMZ   and   a   higher   shooting percentage. 



<!-- Start of picture text -->
Figure   13:   A)   We   show   the   current   shot   distribution   and   current   GMZ   of   Player   X.   B)   We   show   improved,   wider   GMZ   of<br>Player   X   if   Left-­‐Right   consistency   is   improved   to   ‘proficient’   resulting   in   more   shots   in   the   GMZ   and   a   higher   shooting<br>percentage.<br><!-- End of picture text -->

Player   Y   is   a   64%   3-­‐point   shooter   during   practice.   He   is   proficient   in   all   categories   except for   median   Depth.   While   one   can   always   expect   to   increase   one’s   shooting   percentage   with improved   Angle   consistency   and   Left-­‐Right   consistency,   Player   Y   has   straightforward   improvement potential   if   he   focuses   first   on   improving   his   Depth   median.   He   is   currently   shooting   with   a   Depth median   of   8.5   inches   (Figure   14A).   If   he   increases   his   Depth   median   by   2   inches   to   10.5   inches,   he can   expect   to   become   a   70%   three-­‐point   shooter   in   practice   –   an   overall   improvement   of   6%.   Due   to few   examples   of   players   shooting   the   optimal   depth,   this   percentage   increase   was   determined   by sampling   Player   Y’s   shot   population   to   simulate   the   deeper   Depth   median.   This   increase   in   Depth median   will   create   a   much   better   overlap   between   his   shot   distribution   and   GMZ   (Figure   14B). 



Figure   14:   A)   We   show   the   current   shot   distribution   of   Player   Y   where   Depth   median   is   not   centered   in   the   GMZ.   B) We   show   the   potential   shot   distribution   of   Player   Y   if   his   median   Depth   is   improved   by   centering   in   the   GMZ. 



<!-- Start of picture text -->
Figure   14:   A)   We   show   the   current   shot   distribution   of   Player   Y   where   Depth   median   is   not   centered   in   the   GMZ.   B)<br>We   show   the   potential   shot   distribution   of   Player   Y   if   his   median   Depth   is   improved   by   centering   in   the   GMZ.<br><!-- End of picture text -->





2017   Research   Papers   Competition Presented   by: 

11 



#### **8.3   Practice   performance   translates   to   game   performance   for   individual   players** 

The   Noah   shooting   system   collects   shot   data   (6   ball   dynamics   factors   in   addition   to   player identification,   shot   location   and   make-­‐miss) for   both   practices   and   games.      Currently,   the   game data   is   limited,   but   the   initial   data   shows   strong   correlation   between   practice   performance   and game   performance   for   seven   individual   shooters   with   sufficient   game   data   available.      A   few examples:   a   strong   correlation   exists   between   practice   3-­‐point   shooting   percentage   and   game   catch and   shoot   3-­‐point   shooting   percentage   (Spearman   rho=-­‐0.82,   p-­‐value   =   0.02);   a   good   correlation occurs   between   practice   Left-­‐Right   consistency   and   game   catch   and   shoot   3-­‐point   shooting percentage   (Spearman   rho=-­‐0.78,   p-­‐value   =   0.03);   and   a   good   correlation   occurs   between   practice Depth   consistency   and   game   catch   and   shoot   3-­‐point   shooting   percentage   (Spearman   rho=-­‐0.78,   p-­‐ value   =   0.03).   As   we   collect   more   game   3-­‐point   data   on   the   four   actionable   player   factors   (Angle median,   Angle   consistency,   Depth   median   and   Left-­‐Right   consistency),   we   expect   to   see   a   wide range   of   additional   correlations   which   will   instruct   practice   methodologies   to   maximize   3-­‐point shooting   performance   for   individuals   with   specific   factor   expressions. 

## **9.   Conclusions** 

Increasing   3-­‐point   shooting   percentage   is   fundamental   to   winning   games,   but   the   NBA   3-­‐ point   shooting   percentage   has   been   stuck   at   35%   over   the   past   20   years.   Over   those   20   years,   the fundamental   3-­‐point   training   method   has   not   changed;   players   take   a   lot   of   3-­‐point   shots   with   good shot   mechanics   and   count   the   number   of   makes   and   misses.   In   this   paper,   we   explored   3   shot attributes   and   6   shooter   factors   which   give   much   greater   understanding   into   why   shots   are   made   or missed.   This   understanding   is   supported   by   shot   data   from   1.1   million   3-­‐point   shots.   With   the availability   of   real-­‐time,   verbal   feedback   on   Left-­‐Right,   Angle   and   Depth,   individual   athletes   are   now able   to   focus   their   workouts   on   the   specific   aspects   that   limit   their   game   3-­‐point   shooting percentage. 

Using   advanced   computer   vision   and   machine-­‐learning   techniques,   there   is   an   exponential increase   in   our   ability   to   collect   and   analyze   3-­‐point   shot   data   using   the   6   shooter   factors.   This newly   available   data   will   provide   opportunity   for   many   high   potential   analytics   research   efforts including: 

- What   training   methodologies   are   most   efficient   in   improving   shooting   percentage   for   each cluster   of   shooter   factors?   What   is   the   shooting   percentage   improvement   pace   for   specific clusters   using   specific   training   methodologies? 

- Most   players   have   different   expressions   of   the   6   shooter   factors   for   a   “catch   and   shoot” compared   to   a   “dribble   left   and   shoot”   or   a   “dribble   step   back   and   shoot”.   What   are   the most   efficient   training   methods   for   players   to   increase   shooting   percentage   across   all   shot types? 

In   the   coming   years,   there   is   a   large   opportunity   to   complete   meaningful   longitudinal studies   since 2500   middle   school   and   high   school   athletes   are   already   training   regularly   with instant   verbal   feedback   on   Left-­‐Right,   Angle   and   Depth. 



2017   Research   Papers   Competition Presented   by: 



12 



## **10.   Acknowledgements** 

Tom   Edwards,   Deputy   Director   at   NASA   Ames   Research   Center,   for   his   work   in   modeling   the physics   of   the   basketball   shot. 

John   Carter,   CEO   of   Noah   Basketball,   and   Logan   Buchanan,   Developer   at   Forty   AU,   for   providing   the Noah   shot   factor   data   used   in   the   analysis. 

Daniel   O’Neel,   Data   Engineer   at   Wealthfront,   and   Santiago   Carmona,   Bioinformatics   Post-­‐doc   at   the University   of   Lausanne,   for   providing   statistical   feedback. 

## **References** 

[1]   http://www.basketball-­‐reference.com/leagues/NBA_stats.html 

[2]   https://www.teamrankings.com/nba/stat/three-­‐pointers-­‐attempted-­‐per-­‐game?date=2016-­‐06-­‐ <u>20</u> 

[3]   Silverberg,   L.,   Tran,   C.,   &   Adcock,   K.   (2003).   Numerical   analysis   of   the   basketball   shot.   Journal   of Dynamic   Systems,   Measurement,   and   Control,   125(4),   531-­‐540. 

[4]   Okubo,   H.,   &   Hubbard,   M.   (2006)   Dynamics   of   the   basketball   shot   with   application   to   the   free throw.   Journal   of   Sports   Sciences,   24,   1303-­‐1314 

[5]   Tran,   Chau   M.   and   Silverberg,   Larry   M.   (2008)   Optimal   release   conditions   for   the   free   throw   in men's   basketball.   Journal   of   Sports   Sciences,   26:11,   1147-­‐1155 

[6]   Marty,   Alan   W.,   McGhee,   Ridge,   &   Edwards,   Thomas,   A.   (2003)   Trajectory   detection   and feedback   system.   US   Patent   7,094,164   August   22,   2006. 

[7]   Marty,   Alan   W.,   Carter,   John   (2008)   Stereoscopic   Image   Capture   with   Performance   Outcome Prediction   in   Sporting   Environments   US   Patent   9,390,501   July   12,   2016 



2017   Research   Papers   Competition Presented   by: 



13 



## **Appendix Physics   behind   Angle   and   Depth interaction** 



<!-- Start of picture text -->
15<br>10<br>5<br>0<br>33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52<br>Angle (degrees)<br>Depth (inches)<br><!-- End of picture text -->

As   mentioned   in   Section   4.2, Figures   7A   and   7B   are   not   typical   of normal   distributions   associated   with human   performance.   In   these   figures, laws   of   physics   dominate   shooting   skill   in determining   Depth   consistency   results. Projectile   physics   calculates,   for   example, that   players   shooting   a   3-­‐point   shot   from an   8   foot   release   height   with   constant release   velocity   will   maximize   their   shot depth   at   a   42°  Angle   (Figure   13).   If   they release   the   ball   either   steeper   or shallower   than   42°,   Depth   will   decrease,   a counterintuitive   outcome   for   most   observers without   a   physics   background. 

Figure   13:   3-­‐point   shots   with   consistent   release   velocity maximize   their   depth   at   an   Angle   of   42°.°. 



<!-- Start of picture text -->
Figure   13:   3-­‐point   shots   with   consistent   release   velocity<br>maximize   their   depth   at   an   Angle   of   42°.°.<br><!-- End of picture text -->

##### To   demonstrate   this   concept,   we   consider   three   fictional   3-­‐point   shooters: 

Flat   shooter   #1   shoots   11   shots   with   constant   release   velocity   in   one   degree   Angle   increments   from 33°  to   43°  with   a   median   Angle   of   38°.      At  38°  the  Depth  is  8.8”.     At   33°  the   Depth   is   0.5”,   and   at   43° the   Depth   is   11.0”.   The   Depth   range   is   10.5”. 

High   shooter   #2   shoots   11   shots   with   constant   release   velocity   in   one   degree   Angle   increments from   42°  to   52°  with   a   median   Angle   of   47°.      At  47°  the  Depth  is  8.2”.     At   42°  the   Depth   is   11.1”,   and at   52°   the   Depth   is   -­‐1.1”.   The   Depth   range   is   12.2”. 

Medium   Angle   shooter   #3   shoots   11   shots   with   constant   release   velocity   in   one   degree   Angle increments   from   37°  to   47°  with   a   median   Angle   of   42°.      At  42°  the  Depth  is  11.1”.     At   37°  the   Depth is   7.6”,   and   at   47°   the   Depth   is   8.2”.   The   Depth   range   is   3.5”. 

In   this   simplified   example,   the   Depth   range   (associated   with   Depth   consistency)   for   the   42°   medium angle   shooter   is   far   better   than   the   Depth   range   for   either   the   flat   shooter   or   the   high   shooter. 





2017   Research   Papers   Competition Presented   by: 

14 


