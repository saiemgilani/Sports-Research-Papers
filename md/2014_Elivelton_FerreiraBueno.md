<!-- source: 2014_Elivelton_FerreiraBueno.pdf -->

# UNIVERSITE<sup>´</sup> DE MONTREAL<sup>´</sup> 

MATHEMATICAL MODELING AND OPTIMIZATION APPROACHES FOR SCHEDULING THE REGULAR-SEASON GAMES OF THE NATIONAL HOCKEY LEAGUE 

# ELIVELTON FERREIRA BUENO 

DEPARTEMENT<sup>´</sup> DE MATHEMATIQUES<sup>´</sup> ET DE GENIE<sup>´</sup> INDUSTRIEL ´ECOLE POLYTECHNIQUE DE MONTR´EAL 

THESE<sup>`</sup> PRESENT<sup>´</sup> EE<sup>´</sup> EN VUE DE L’OBTENTION DU DIPLOME<sup>ˆ</sup> DE PHILOSOPHIÆ DOCTOR (MATHEMATIQUES<sup>´</sup> DE L’INGENIEUR)<sup>´</sup> AOUT<sup>ˆ</sup> 2014 

- © Elivelton Ferreira Bueno, 2014. 

# UNIVERSITE<sup>´</sup> DE MONTREAL<sup>´</sup> 

# ´ECOLE POLYTECHNIQUE DE MONTREAL<sup>´</sup> 

Cette th`ese intitul´ee : 

MATHEMATICAL MODELING AND OPTIMIZATION APPROACHES FOR SCHEDULING THE REGULAR-SEASON GAMES OF THE NATIONAL HOCKEY LEAGUE 

pr´esent´ee par : BUENO Elivelton Ferreira 

en vue de l’obtention du diplˆome de : Philosophiæ Doctor 

a ´et´e dˆument accept´ee par le jury d’examen constitu´e de : 

- M. ROUSSEAU Louis-Martin, Ph.D., pr´esident 

- M. GENDREAU Michel, Ph.D., membre et directeur de recherche 

- M. FERLAND Jacques, Ph.D., membre et codirecteur de recherche 

Mme LAHRICHI Nadia, Ph.D., membre 

- M. TRICK Michael A., Ph.D., membre 

iii 

# **DEDICATION** 

_To Carmelucia Ferreira Bueno_ 

iv 

# **ACKNOWLEDGMENTS** 

I would like to express my deep gratitude to Professor Michel Gendreau and Professor Jacques Ferland, my research supervisors, for their guidance, encouragement and support through all the ups and downs of this journey. My grateful thanks are also extended to my other committee members, Professor Louis-Martin Rousseau, Professor Nadia Lahrichi, and Professor Michael Trick, who were more than generous with their expertise and precious time. 

I owe thanks to Professor Marco Antonio Figueiredo Menezes, from the Pontifical Catholic University of Goi´as, who introduced me to Operations Research; and also to Professor Nelson Maculan, from the Federal University of Rio de Janeiro, who encouraged me to dive deeper into this striking field. 

Many friends have helped me stay sane through these years of study in Montreal. Among them, I would like to offer my special thanks to Dariusz Trzaniec and to the families of Emilia Rei and Jos´e Tom´e, who embraced me as their own. 

I am also grateful to Leizer de Lima Pinto, who has been as a supportive brother to me, and to the lovely Pr´ıscila Valc´acio, who was waiting for me when I did research and wrote. 

Finally, I would like to thank the Brazilian National Council for the Improvement of Higher Education (CAPES) for their financial support during three years of this research study. 

v 

# **RESUM**<sup>**´**</sup> **E**<sup>**´**</sup> 

La Ligue nationale de hockey (LNH) est une association sportive professionnelle de hockey sur glace regroupant des ´equipes du Canada et des Etats-Unis.<sup>´</sup> Chaque ann´ee, la LNH dois compter sur un calendrier de haute qualit´e concernant des questions ´economiques et d’´equit´e pour les 1230 matchs de sa saison r´eguli`ere. Dans cette th`ese, nous proposons le premier mod`ele de programmation lin´eaire en nombres entiers (PLNE) pour le probl`eme de la planification de ces matchs. Bas´e sur la litt´erature scientifique en planification des horaires sportifs, et aussi sur un raisonnement pratique, nous identifions et soulignons des exigences essentielles et des pr´ef´erences qui doivent ˆetre satisfaites par des calendriers de haute qualit´e pour la LNH. La construction de tels calendriers, tout comme la planification des horaires sportifs en g´en´eral, s’av`ere une tˆache tr`es difficile qui doit prendre en compte des int´erˆets concurrents et, dans plusieurs cas, subjectifs. En particulier, les exp´erimentations num´eriques que nous d´ecrivons dans cette ´etude fournissent des ´evidences solides sugg´erant qu’une approche bas´ee sur la PLNE est actuellement incapable de r´esoudre des instances de taille r´ealiste pour le probl`eme. Pour surmonter cet inconv´enient, nous proposons ensuite un algorithme de recherche adaptative `a voisinage large (ALNS) qui int`egre `a la fois des nouvelles strat´egies et des heuristiques sp´ecialis´ees provenant de la litt´erature scientifique. Afin de tester cette approche, nous g´en´erons plusieurs instances du probl`eme. Toutes les instances sont bas´ees sur les calendriers officiels de la LNH et, en particulier, utilisent les dates de matchs `a domicile de chaque ´equipe comme des dates de disponibilit´e de son ar´ena. Dans les situations les plus difficiles, la disponibilit´e des ar´enas est rare ou est `a son minimum. Dans tous les cas, en ce qui concerne les indicateurs de qualit´e soulev´es, l’algorithme ALNS a ´et´e capable de g´en´erer des calendriers clairement meilleur que leur correspondants adopt´es par la LNH. Les r´esultats obtenus sugg`erent que notre approche pourrait certainement permettre aux gestionnaires de la LNH de trouver des calendriers de meilleur qualit´e par rapport `a une vari´et´e de nouvelles pr´ef´erences. 

vi 

# **ABSTRACT** 

The National Hockey League (NHL) is a major professional ice hockey league composed of 30 teams located throughout the United States and Canada. Every year, the NHL must rely on a high-quality schedule regarding both economic and fairness issues for the 1230 games of its regular season. In this thesis, we propose the first integer linear programming (IP) model for the problem of scheduling those games. Based both on the pertinent sports scheduling literature and on practical reasoning, we identify and point out essential requirements and preferences that should be satisfied by good NHL schedules. Finding such schedules, as many other sports scheduling problems, is a very difficult task that involves several stakeholders with many conflicting, and often subjective, interests. In fact, computational experiments that we describe in this study, provide compelling evidence that an IP approach is currently unable to solve instances of realistic size for the problem. To overcome such drawback, we propose then an Adaptive Large Neighborhood Search (ALNS) algorithm that integrates both novel strategies and specialized heuristics from the scientific literature. To test the approach, we generate instances based on past NHL schedules and on a given number of arenaavailable dates that are suitable for the home games of each team. In the most challenging instances, availability of arenas is scarce or at its minimum. In all cases, regarding the identified concerns, the ALNS algorithm was able to generate much better schedules than those implemented by the NHL. Results obtained suggest that our approach could certainly identify unnecessary weakness in NHL schedules, makes the NHL managers aware of better schedules with respect to different requirements, and even lead them to consider other desired features they might not have previously taken into account. 

vii 

# **TABLE OF CONTENTS** 

|DEDIC|ATION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>iii|
|---|---|---|
|ACKN|OWLEDGMENTS<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>iv|
|R<sup>´</sup>ESUM|<sup>´</sup>E . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>v|
|ABSTR|ACT<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>vi|
|TABLE|OF CONTENTS<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . vii|
|LIST O|F TABLES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>ix|
|LIST O|F FIGURES<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>x|
|LIST O|F APPENDICES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>xi|
|CHAP|TER 1<br>INTRODUCTION<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>1|
|CHAP|TER 2<br>LITERATURE REVIEW<br>. . . . . . . . . . . . . . . . . . . .|. . . . .<br>6|
|2.1|Basic terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>7|
||2.1.1<br>Round-robin tournaments<br>. . . . . . . . . . . . . . . . . . . .|. . . . .<br>7|
|2.2|Literature on the NHL scheduling problem . . . . . . . . . . . . . . .|. . . . .<br>10|
|2.3|Literature on time-constrained sports scheduling problems<br>. . . . . .|. . . . .<br>13|
||2.3.1<br>Finding home-away patterns . . . . . . . . . . . . . . . . . . .|. . . . .<br>15|
||2.3.2<br>Optimizing breaks<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>16|
||2.3.3<br>The Traveling Tournament Problem . . . . . . . . . . . . . . .|. . . . .<br>18|
||2.3.4<br>Typical constraints in sports scheduling . . . . . . . . . . . . .|. . . . .<br>21|
|2.4|Literature on time-relaxed sports scheduling problems . . . . . . . . .|. . . . .<br>24|
||2.4.1<br>The NBA scheduling problem . . . . . . . . . . . . . . . . . .|. . . . .<br>25|
|CHAP|TER 3<br>THE NHL SCHEDULING PROBLEM . . . . . . . . . . . . .|. . . . .<br>31|
|3.1|The structure of the NHL<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>31|
|3.2|The structure of the NHL regular season . . . . . . . . . . . . . . . .|. . . . .<br>32|
||3.2.1<br>The availability of dates, teams, and arenas<br>. . . . . . . . . .|. . . . .<br>33|
|3.3|The scheduling problem of the NHL regular season<br>. . . . . . . . . .|. . . . .<br>34|
||3.3.1<br>The NHL scheduling problem in the literature . . . . . . . . .|. . . . .<br>36|



viii 

|CHAPT|ER 4|MATHEMATICAL MODELING<br>. . . . . . . . . . . . . . . .|. . . . .<br>39|
|---|---|---|---|
|4.1|Basic|formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>39|
||4.1.1|Data of the problem<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>39|
||4.1.2|Parameters of the model . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>39|
||4.1.3|Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>40|
||4.1.4|Constraints<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>41|
|4.2|Formu|lation for minimizing total travel distance . . . . . . . . . . . .|. . . . .<br>46|
|4.3|Comp|utational experiments<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>48|
||4.3.1|Models and parameters . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>49|
||4.3.2|Problem instances . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>50|
||4.3.3|Results for the _partial-league_ instances . . . . . . . . . . . . .|. . . . .<br>53|
||4.3.4|Results for the _2012_ instances . . . . . . . . . . . . . . . . . .|. . . . .<br>54|
||4.3.5|Results for the _entire-league_ instances . . . . . . . . . . . . . .|. . . . .<br>55|
|CHAPT|ER 5|AN ADAPTIVE LARGE NEIGHBORHOOD SEARCH . . . .|. . . . .<br>60|
|5.1|Model|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>60|
|5.2|Algori|thm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>60|
||5.2.1|Controlling the master level of the algorithm . . . . . . . . . .|. . . . .<br>62|
||5.2.2|Constructing an initial solution . . . . . . . . . . . . . . . . .|. . . . .<br>64|
||5.2.3|Partially destroying a solution . . . . . . . . . . . . . . . . . .|. . . . .<br>70|
||5.2.4|Repairing a partial solution<br>. . . . . . . . . . . . . . . . . . .|. . . . .<br>75|
|5.3|Comp|utational Experiments . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>79|
||5.3.1|Constructing initial solutions<br>. . . . . . . . . . . . . . . . . .|. . . . .<br>80|
||5.3.2|Choosing the size of the current solution to destroy . . . . . .|. . . . .<br>83|
||5.3.3|Setting the ALNS parameters . . . . . . . . . . . . . . . . . .|. . . . .<br>84|
||5.3.4|Solving other instances . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>93|
|CHAP|ER6|CONCLUSION|100|
|||. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .|
|REFER|ENCE|S . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 102|
|APPEN|DICES|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 109|



ix 

# **LIST OF TABLES** 

|Table 2.1|Length of home stands in ofcial NHL schedules . . . . . . . . . . . . .|12|
|---|---|---|
|Table 2.2|Length of road trips in ofcial NHL schedules<br>. . . . . . . . . . . . . .|13|
|Table 3.1|The current NHL structure<br>. . . . . . . . . . . . . . . . . . . . . . . .|32|
|Table 3.2|Constraint violations in ofcial NHL schedules . . . . . . . . . . . . . .|37|
|Table 3.3|Constraints of the NHL scheduling problem in the literature . . . . . .|38|
|Table 4.1|Models for the computational experiments with CPLEX<sup>® </sup>. . . . . . . .|49|
|Table 4.2|Instances for the computational experiments . . . . . . . . . . . . . . .|51|
|Table 4.3|Results for the partial-league instances without minimization of total<br>travel distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|56|
|Table 4.4|Results for the partial-league instances with minimization of total travel<br>distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|57|
|Table 4.5|Results for the 2012 instances with and without minimization of total<br>travel distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|58|
|Table 4.6|Results for the 2012-13 season schedule of the Eastern Conference . . .|58|
|Table 4.7|Results for the entire-league instances without minimization of total<br>travel distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|59|
|Table 5.1|Statistics on initial schedules . . . . . . . . . . . . . . . . . . . . . . . .|80|
|Table 5.2|Results on diferent number of games being removed per LNS iteration|84|
|Table 5.3|Best-found solutions on diferent parameters settings for the ALNS<br>. .|92|
|Table 5.4|Best-found solutions for instances with extra arena-available dates . . .|94|
|Table 5.5|Typical results for instances without extra dates . . . . . . . . . . . . .|95|
|Table 5.6|Best-found schedules for instances without extra arena-available dates .|97|



x 

# **LIST OF FIGURES** 

|Figure 5.1|Constraint violations in initial schedules<br>. . . . . . . . . . . . . .|. . .<br>81|
|---|---|---|
|Figure 5.2|Selection probabilities for the destroy operators<br>. . . . . . . . . .|. . .<br>88|
|Figure 5.3|Best-found solutions on diferent confgurations of operators<br>. . .|. . .<br>98|
|Figure 5.4|Selection probabilities for the chosen operators . . . . . . . . . . .|. . .<br>99|



xi 

# **APPENDIX** 

|Appendix A|PSEUDOCODE OF THE ALNS ALGORITHM . . . . . .|. . . . . . . 109|
|---|---|---|
|Appendix B|FLEURENT’S HEURISTICS . . . . . . . . . . . . . . . .|. . . . . . . 111|
|Appendix C|DESTROY OPERATORS . . . . . . . . . . . . . . . . . .|. . . . . . . 116|
|Appendix D|REPAIR OPERATORS<br>. . . . . . . . . . . . . . . . . . .|. . . . . . . 120|



1 

# **CHAPTER 1** 

# **INTRODUCTION** 

The National Hockey League (NHL), one of the four leading professional sports leagues in North America, includes 30 teams located throughout the vast territories of the United States and Canada. Every team plays 82 games, 41 at its own home arena and 41 away (at arenas of its opponents), over slightly more than six months of the NHL regular season, which usually starts in early October each year. By that time, a schedule for all the 1230 games must already have been determined. As for any major sports league, the NHL must rely on high-quality schedules in order to make games more attractive so as to increase revenues from sources that include broadcasting rights and game attendance. 

Obviously, good schedules should also take into account some fairness issues, such as reduction of fatigue for players and minimization of travel distance for teams. Because of many conflicting, and often subjective, interests from several stakeholders, including players’ association, fans, teams’ owners, media, and officials’ association, finding a good schedule for the games of the NHL is a very difficult task. 

In fact, sports scheduling problems in general are very challenging and many optimization techniques have been used to deal with them. The recent annotated bibliography by Kendall _et al_ . (2010) references over 160 papers on sports scheduling, most of them having been published in the past decade alone. Also, Knust (2014) maintains an up to date collection of (currently more than 250 references) on different topics of sports scheduling and classifies them according to different models, methods, and sports disciplines. Practical papers have addressed many sports disciplines, such as soccer, baseball, golf, cricket, basketball, and ice hockey. Overall, those works point out that both artificial and real-world instances of sports scheduling problems are often surprisingly hard to be solved, even for leagues involving only a few teams. 

This thesis focuses on the task of scheduling the games of the NHL regular season. We refer to that task as the _NHL scheduling problem_ (the same term used in Costa, 1995). Although the literature on practical studies of sports scheduling has widely dealt with cases where, as for the NHL, a specific venue is associated to each team in the league, they have often been limited to round-robin tournaments, which is not the general structure of the NHL regular season. In fact, rather than every team playing all others a fixed number of times, an NHL team usually plays more often against opponents located in its own geographical area. And even though the exact number of games, and the places, that teams play one another are 

2 

determined beforehand, there is no predefined structure on the course of the games. Indeed, during each week different teams may play different numbers of games, usually any number in the range from two to five, and for any day, the number of games that the teams will individually have played will in general be also different from each other. Therefore, the round structure, so widely considered in other studies, is not suitable for the NHL scheduling problem. In addition, unlike most cases in the sports scheduling literature, where the ideal pattern for any team is usually to alternate between home and away games, it is allowed (and even preferred) that an NHL team visits several opponents on the road without a return to home. Such long “road trips” would thus lead to a reduction on the overall travelling distances for the teams. Nevertheless, because the home locations of the NHL teams are unevenly scattered throughout a vast region, some teams have to travel much further than others in order to complete their individual schedules. This unfavorable situation for the most geographically isolated teams could be somewhat aggravated or relieved, depending on how games are scheduled for those teams. In practice, travel distance is then one of the issues to be addressed in the NHL scheduling problem. In general, the requirements found in practical studies of sports scheduling are related to economics and fairness. For example, Bartsch _et al_ . (2006) highlight the main issues dealt in several cases, including how well-distributed the most attractive games are over the season, availability of arenas, and number of rest days between two consecutive games. Nurmi _et al_ . (2010) propose a framework for highlyconstrained sports scheduling problems where they enumerate 36 types of constraints found in various sports leagues. Those constraints, however, cover only part of the requirements for a good NHL schedule. 

Despite the recent growing scientific interest in sports scheduling, only a few researchers have addressed the NHL scheduling problem. The first systematic study leading to a successful approach was carried out in the late 1980s by Fleurent (1987), which was then (partially) reported in the paper by Ferland and Fleurent (1991). They developed a support system made up of various specialized heuristic procedures to help an expert to schedule the games in an interactive manner. They also present the first mathematical model for the problem. Unfortunately, that model considers only certain aspects of their own description of the problem. And even though only binary variables were used, it turns out to be a non-linear model. A few years later, Costa (1995) proposed a hybrid approach that combines Tabu Search and a genetic algorithm in order to solve combinatorial optimization problems in general, and then, he used the NHL scheduling problem to illustrate the effectiveness of his approach. In both studies, the descriptions of the problem enumerate several issues regarding each team, such as availability of arenas, number of games over a few consecutive days, duration and number of away games in a row, number of days between games involving the same pair of oppo- 

3 

nents, and daily travel distances. On the whole, their strategy consists in allowing violations of only some constraints and penalizing them in the objective function of a minimization problem. However, comparing one study to the other, the constraints are not considered in the same manner. In fact, there is no general agreement on a precise statement of the problem, which is typical in practical cases of sports scheduling, since many complex goals are often involved. In particular, Ferland and Fleurent (1991) give exceptional attention to the availability of arenas, as some teams may hardly be able to provide the minimum number of arena-available dates for its home games, and their approach never schedule a team to play home on a day that has not been provided to the scheduler by that team. On the other hand, Costa (1995) allows violations for the constraints on the availability of arenas, and for example, regarding the 1993-94 regular season, when the NHL was formed by only 24 teams but every team already had to play 41 games at home, his best result shows that, even though at least 56 arena dates (thus 15 “extra” dates) had been provided by each team, more than a hundred games were surprisingly scheduled on days when the arena of the home team was not available. Finally, in a more recent work, Craig _et al_ . (2009) describe and analyze a system that uses a multi-objective evolutionary algorithm to schedule the games of the NHL regular season. The system is reported to produce a set of schedules that offer a range of trade-offs across the following three objectives: minimizing the total distance that all the teams must travel; avoiding the unfair situation where only one of the opponents in a game must travel a long distance over a short period of time in order to play that game; and minimizing streaks of either more than three home games or more than three away games for a team. Their assumption that, in general, streaks longer than three should be avoided is not completely consistent with the previous studies. Indeed, at least for long distance visits, both Ferland and Fleurent (1991) and Costa (1995) engage in creating road trips made up of as many as seven consecutive away games. In our view, however, the main limitation in the study by Craig _et al_ . (2009) is that they overlook essential constraints of the problem, specially the availability of arenas. In particular, a team might be scheduled to play home on any day of the regular season, and the only constraint they explicitly mention is that in a feasible schedule a team cannot be assigned to play more than once a day. 

This thesis revisits the NHL scheduling problem, describing some basic requirements for good NHL schedules, and present two approaches that we are proposing to construct such schedules. One approach is based on an integer linear programming (IP) formulation that we are introducing for the NHL scheduling problem and uses a commercial state-of-the-art solver to exactly solve instances of moderate size of the problem. The other approach is an adaptive large neighborhood search (ALNS) to approximately solve instances of practical size. 

4 

In particular, this thesis reinforce the importance of crucial issues that have been highlighted in the seminal work by Fleurent (1987), as for example the scarce availability of arena dates to hold the home games of the teams. Some computational experiments on a C++ implementation that uses the solver CPLEX<sup>®</sup> are reported on several variants of the proposed IP formulation. Such variants arise from different constraints being relaxed and their violations penalized in the objective function. Because, in general, those variants can enable the solver to deal only with moderate size of instances of the problem, other computational experiments are described on the ALNS as an alternative approach to solve instances of realistic size. For this approach, another model is described, in which most of the constraints are allowed to be violated during the solution process and a penalty value is introduced into an objective function that evaluates the “cost” of a schedule as a weighted summation of the constraint violations. The ALNS tries then to generate schedules that minimize the value of the objective function. Unlike the approaches by Ferland and Fleurent (1991) and by Costa (1995), where most of the requirements are treated as “hard” constraints (which must not be violated), our strategy is then more flexible, allowing easier exploration of a wide variety of schedules during the solution process. In addition, by penalizing violations of constraints in the objective function, we can mimic different degrees of preferences with the use of different penalty weights. 

This thesis also describe the creation of several instances based on official NHL schedules. The reported results are very promising as, in particular, the ALNS is able to solve to optimality all instances that have only six extra arena dates per team. It accounts that even by only rescheduling the games to the same arena dates utilized in official NHL schedules, in general, our solutions violate much fewer constraints of the model. But the results also reinforce the importance of having (even just a few) extra arena dates per team. The final remarks on this study mention our confidence that the ALNS approach is able to identify unnecessary weakness in the NHL schedules, makes the NHL managers aware that the schedules could be improved with respect to different requirements, and even lead them to consider other desired features that they might not have previously taken into account. 

The remainder of this thesis is organized as follows. In Chapter 2, we present some basic terminology, and a short review of the literature about the NHL scheduling problem and also about more general sports scheduling problems. We describe the NHL scheduling problem in Chapter 3, specifying the constraints that we consider in this study. An IP formulation is then proposed for each of those constraints in Chapter 4, and computational results are reported on different models that are based on the proposed formulations. The generation of the instances we have used in the experiments are also described in Chapter 4. In Chapter 5, we propose an ALNS algorithm, which also includes a review of the heuristics introduced 

5 

by Fleurent (1987), and outline the results obtained with the ALNS for instances of realistic sizes. Finally, in Chapter 6, we draw some concluding remarks and suggest future directions for this study. 

6 

# **CHAPTER 2** 

# **LITERATURE REVIEW** 

The NHL scheduling problem considered in this thesis belongs to the broader field of _sports scheduling_ , which can be traced back over more than four decades. In general, problems in sports scheduling are very challenging and they have attracted the interest of a number of researchers from different fields, especially graph theory, combinatorial optimization, and applied mathematics. 

The annotated bibliography by Kendall _et al_ . (2010) references over 160 papers on sports scheduling, most of them having been published in the past decade alone. For pertinent surveys, we refer the reader to Easton _et al_ . (2004), which review the main issues that have been considered in the literature prior to 2004; to Drexl and Knust (2007), which survey graph-based models and introduce resource-based models; and to Rasmussen and Trick (2008), which propose an unified terminology and review the literature on round-robin tournaments. 

Apart from that, Knust (2014) maintains an up to date collection of references (currently with more than 250 papers) on different topics of sports scheduling and classifies them according to different models, methods, and sports disciplines. The reported approaches include integer programming (more than 60 papers), constraint programming (25), heuristics (16), and metaheuristics (30). Practical papers have addressed several sports disciplines, such as soccer (more than 30 papers), baseball (12), basketball (12), golf (6), cricket (6), and ice hockey (6). Overall, those works point out that both artificial and real-world instances of sports scheduling problems are often surprisingly hard to be solved, even for leagues involving only a few teams. 

In this chapter, we provide some basic terminology used in sports scheduling, and as a way to highlight common issues and challenges arising in several practical applications, we discuss a few problems that have been widely addressed in the related literature. We also outline typical approaches reported on other studies and point out their relevance (or lack thereof) to the scheduling of the NHL regular-season games. Although the NHL scheduling problem is only described later on, in Chapter 3, we confront here all the past known studies concerning this particular application. 

On the whole, we focus on sports scheduling for league tournaments in which every team (or club) is assumed to have an associated venue where games between two opposing teams take place. Such is, of course, the case of the NHL scheduling problem, where every team is 

7 

considered to own a specific arena and each game is played at the arena of one of the two opposing teams in the game. In particular, studies in other contexts, as that of the so-called Balanced Tournament Design Problem (Lamken, 1990), in which all the teams share the facilities holding the games are out of the scope of this thesis. 

# **2.1 Basic terminology** 

For any particular game, the team that owns the venue where that game takes place is said to be the _home team_ , while its opponent is called the _away team_ . A game is said to be a _home game_ with regard to the team that owns the venue where that game is to be held, but it is called an _away game_ with respect to the other team. A _road trip_ (or simply _trip_ ) for a team is a sequence of consecutive away games which that team plays without returning home in-between. The team corresponding to a certain road trip is referred to as the _traveling team_ . Similarly, a sequence of consecutive home games (with no away game in-between) for a team is called a _home stand_ . 

Sports scheduling problems are usually classified into two large groups: temporally constrained and temporally relaxed problems (Kendall _et al_ ., 2010). Here, we refer to them as _time-constrained_ and _time-relaxed_ problems, respectively (as in, e.g., Knust, 2010). This classification is based on the distribution of the games among the available time slots, the so-called _rounds_ , of the tournament. By definition, no team plays more than a single game during each round. In the time-constrained problems the number of rounds is at its minimum with respect to the existence of a feasible distribution of the games, which defines a _compact schedule_ . Each team plays then exactly one game in each round of a compact schedule for a league with an even number of teams. On the other hand, in time-relaxed problems more rounds than that minimum threshold is available, and a schedule is said to be _relaxed_ for such cases. If a team is not scheduled to play during a certain round then the team is said to have a _bye_ on that round. 

As noted by Easton _et al_ . (2004), nearly all the literature on the design of sport schedules deals with models for round-robin tournaments, to which we draw considerable attention in this chapter. There are of course other structures, as for example the Swiss tournament, _ladder_ , knockout and double elimination (Rokosz, 2000), but they are out of the scope of this thesis. 

# **2.1.1 Round-robin tournaments** 

A competition where the teams confront one another a fixed number of times is called a _round-robin tournament_ (RRT). In most tournaments, especially for major professional sports 

8 

leagues, each team plays two times against every other team (as noted by, e.g., Rasmussen and Trick, 2008). This is particularly referred to as a _double round-robin tournament_ , but _single_ , _triple_ , and _quadruple_ round-robin tournaments, where respectively one, three, and four games are played by each pair of teams, also occur in several leagues around the world. 

As an example, all national soccer championships in Europe uses an RRT during their regular season (stage). In particular, among the 25 European soccer competitions for which Goossens and Spieksma (2011) overview schedule formats, a total of 19, 4, and 2 competitions follows a double, a triple, and a quadruple RRT, respectively. 

Scheduling an RRT consists in determining the round and the venue in which every game will be played. In its most common form, where the problem is time constrained, the basic sports scheduling problem for a league can be stated as follows. Given a league consisting of an even number _n ≥_ 2 of teams identified by the integers in the set _T_ = _{_ 1 _,_ 2 _, . . . , n}_ , and a tournament where each team must play _ℓ ≥_ 1 times against every other team, assign all the _n_ ( _n −_ 1) _ℓ/_ 2 games of the tournament to its ( _n −_ 1) _ℓ_ rounds by determining, for each _k ∈{_ 1 _,_ 2 _, . . . ,_ ( _n −_ 1) _ℓ}_ and for each _i ∈ T_ , which opponent _j ∈ T \ {i}_ plays against team _i_ in the _k_ th round, and also determining whether _i_ plays at home (so that _j_ plays away at _i_ ’s venue) or _i_ plays away at _j_ ’s venue (so that _j_ plays at home) in that round. In cases where the league consists of an odd number _n_<sup>_′_</sup> of teams, a “dummy team” _n_<sup>_′_</sup> + 1 is introduced (as to have _n_<sup>_′_</sup> + 1 = _n_ in the preceding statement), and an actual team is considered to have a “bye” whenever it is assigned to play against _n_<sup>_′_</sup> + 1. 

While an RRT has the advantage of ensuring that all teams individually play the same number of games, the number of teams in the league determines the length of the respective season (in number of rounds). This might be seen as a drawback if the league consists of either only a few or relatively many teams. 

In a recent study, Larson and Johansson (2014) analyze the expansion of an RRT in which adding a single game for each pair of teams as to preserve an RRT format would cause a too high increase (50%) in the total number of games in the schedule. In particular, they report that the 14 team owners in the Elitserien (the top Swedish handball league) considered its traditional 26-game double RRT to be too short, but a possible 39-game triple RRT was deemed too long. Elitserien decided then to expand its season by splitting the league into two divisions of seven teams each, and by adopting a schedule where an intra-divisional single RRT is played before starting a double RRT between all teams in the league. The first half of that double RRT is, in turn, identical to the second half, except for the location of each game, which alternates between the homes of the two corresponding teams. In the literature, this is known as a _mirrored tournament_ , a structure used, for instance, by several soccer leagues in South America. A mirrored double RRT is usually addressed as two consecutive 

9 

tournaments, each one being a single RRT. 

This asymmetric format, in which pairs of teams play different numbers of games between them if they are either from the same division or from two distinct divisions, occurs in many sports leagues, especially in North America. Indeed, in all the leading major professional sports leagues in the United States and Canada, which include the Major League Baseball (MLB), the National Football League (NFL), the National Basketball Association (NBA), and also the National Hockey League (NHL), the number of games for each pair of teams is determined, among other factors (like the standings from the previous season), by their respective conference and divisional alignment. Despite several motivations in favor of an asymmetric format, including the benefit of minimizing travel distances for teams and promote local rivalries (DePalma, 2004; Havard, 2014), the resulting “unbalanced schedules” might rise concerns about the fairness of the competition (Lenten, 2013). 

In the case of the NHL, changes in the number of games that teams play against each other was extensively investigated by Fleurent and Ferland (1993) in response to expansions of the NHL in the early 90s. They used IP to generate possible season structures for different numbers of teams and numbers of games per team. Obviously, the focus of that study is then part of the data provided for the NHL problem of this thesis. 

Nowadays, because the number of teams is currently not the same for all divisions of the NHL, the teams are especially susceptible to unfair schedules. To be more precise about the structure of the league, the NHL teams are split into four divisions of either seven or eight teams: two seven-team divisions form one conference, and two eight-team divisions form another conference. As for the structure of the season, it is characterized as follows. The teams in one conference play a double RRT against the teams in the other conference. The teams in one division, which is inside a particular conference, play a triple RRT against the teams in the other division inside the same conference. By contrast, the teams inside any given division does not play an RRT: each team plays either four or five games against the other teams in its own division. Apart from that, there is no particular sequence of rounds associated to either intradivision or interdivisional games, and thus the NHL regular season structure is different from the Elitserien structure that we mentioned earlier (Larson and Johansson, 2014). Even the classical notion of “rounds” would be inaccurate in the context of the NHL scheduling problem, as at any time before the end of the tournament the teams will normally have played different numbers of games. 

Despite the recent growing scientific interest in sports scheduling, very few researches have been carried out on the NHL scheduling problem. Generally speaking, this problem consists in creating schedules for the regular-season games of the NHL, which are subject to several constraints involving unavailability of some arenas on most days, limitation on the 

10 

number of games a team can play over a few days, requirement of at least a certain number of days between two games involving the same opposing teams, and minimization of traveling distances, to mention but a few. While the NHL scheduling problem will be extensively described only in Chapter 3, we address now the literature on this particular application in sports scheduling. 

# **2.2 Literature on the NHL scheduling problem** 

The first systematic study leading to a successful approach to scheduling the NHL games was carried out in the late 1980s by Fleurent (1987), which is partially reported in the paper by Ferland and Fleurent (1991). Their work was motivated by the disappointing experience of Fraser (1982), who had developed a rather inflexible generator of road trips that is reported to be unable to produce feasible schedules for all the NHL games. 

In his study, Fraser (1982) had in fact concluded that _“due to the unpredictability of some constraints and the human relationships involved in others, its impractical to expect that a computer program will ever produce a final schedule which would require no tuning or adjustment”_ (as cited in Costa, 1995). To overcome this drawback, Ferland and Fleurent (1991) highlight the importance of considering an approach which would allow an expert to include in the scheduling process his own experience and all relevant requirements he might have. They develop then a support system made up of various specialized heuristic procedures to help a person to schedule the games in an interactive manner. 

Their heuristics (which will be described in more detail in Chapter 5) can be outlined as follows, where a “free game” is a game that has not yet been scheduled at a specific time of the scheduling process. 

- _Forced-trip heuristic_ Schedule free games by first identifying long periods of days with no arena-available dates for a team, and then, by assigning the respective team to visit, in a single road trip, at most seven of its distant opponents exclusively during the corresponding period of arena unavailability. 

- _Forced-home heuristic_ Schedule, for each road trip lasting more than one week, two home games for the respective traveling team: one game on its last (latest) arenaavailable date before the trip, and the other, on its first arena date after the trip. 

- _Free-trip heuristic_ Schedule all currently free games opposing teams based far from each other by first identifying, for each team, at most three of its distant opponents to be visited in a single trip, and then, by scheduling every one of those long-distance trips on a period that does not violate the hard constraints of the problem and that contains the minimum possible number of arena-available dates of the visiting team. 

11 

- _Weekend-game heuristic_ Schedule as many free games as feasibly possible respectively on Saturdays, on Fridays, and on Sundays, by trying not to schedule a team to play away on a weekend containing some of its own arena-available dates, and by never putting a team to play an away game within a period when it has already been scheduled to visit distant opponents. 

- _Weekday-game heuristic_ Schedule as many free games as feasibly possible on weekdays from Monday through Thursday, by trying not to schedule a team to play away on its own arena-available dates, and by never assigning days from periods of long-distance visits for the teams involved in the game being scheduled. 

- _Exchange heuristic_ Schedule as many free games as feasibly possible by allowing some of the previously scheduled short-distance visits to be rescheduled on alternative days. 

In addition, Ferland and Fleurent (1991) propose the first mathematical model for the NHL scheduling problem. Unfortunately, that model does not consider all aspects of their own description of the problem. For example, different requirements over road-trip games for a team are not taken into account. And even though only binary variables are used, it turns out to be a non-linear model that involves, for example, products of multiple variables. 

A few years later, Costa (1995) proposed a hybrid approach that combines Tabu Search and a genetic algorithm in order to solve combinatorial optimization problems in general, and then, he used the NHL scheduling problem to illustrate the effectiveness of his approach. 

In both of those research studies, the descriptions of the problem enumerate several issues regarding each team, such as availability of arenas, number of games over a few consecutive days, duration and number of away games in a row, number of days between games involving the same pair of opposing teams, and travel distances. On the whole, their strategy consists in allowing violations of some constraints but penalizing them in the objective function of a minimization problem. 

However, comparing one study to the other, the constraints are not considered in the same manner. In fact, there is no general agreement on a precise statement of the problem, which is typical in practical cases of sports scheduling, since many complex goals are often involved in the process. 

In particular, Ferland and Fleurent (1991) give exceptional attention to the availability of arenas, as some teams may hardly be able to provide the minimum number of arena-available dates for its home games, and their approach never schedules a team to play at home on a day that has not been provided to the scheduler by that team. On the other hand, Costa (1995) allows violations for the constraints on the availability of arenas. 

As an example, regarding the 1993-94 regular season, when the NHL was formed by only 24 teams but every team already had to play 41 games at home, the best result by Costa 

12 

(1995) shows that, even though at least 56 arena dates (thus 15 “extra” dates) had been provided by each team, more than a hundred games were surprisingly scheduled on days when the arena of the home team was supposed not to be available. 

Finally, in a more recent work, Craig _et al_ . (2009) describe and analyze a system that uses a multi-objective evolutionary algorithm to schedule the games of the NHL regular season. The system is reported to produce a set of schedules that offer a range of trade-offs across the following three objectives: minimizing the total distance that all the teams must travel; avoiding the unfair situation where only one of the rivals in a game must travel a long distance over a short period of time in order to play that game; and minimizing streaks of either more than three home games or more than three away games for a team. In addition, as in Costa (1995), they allow a team to be scheduled to play more than one game on the same day during the solution process, but eventually discard any schedule where such infeasible setting happens. 

The assumption, in Craig _et al_ . (2009), that streaks longer than three should be avoided is not completely consistent with the previous studies. Indeed, at least for long distance visits for a team, both Ferland and Fleurent (1991) and Costa (1995) engage in creating road trips made up of as many as seven consecutive away games, which in turn seems more in line with actual NHL schedules. Evidence for this is in tables 2.1 and 2.2. 

In our view, however, the main limitation in the study by Craig _et al_ . (2009) is that they overlook essential constraints of the problem, specially the availability of arenas. A team might, for instance, be scheduled to play home on any day of the regular-season period, and the only constraint they explicitly mention is that in a feasible schedule a team cannot be 

Table 2.1 _Length of home stands in official NHL schedules_ Frequency of home stands by their individual number of games (# _g_ ) in the official schedules of past seasons 

|#_g_|2009|-10|2010|-11|2011|-12|2012|-13|2013|-14|
|---|---|---|---|---|---|---|---|---|---|---|
|1|214|(42.04%)|221|(45.29%)|216|(42.19%)|139|(40.29%)|236|(40.48%)|
|2|149|(29.27%)|147|(30.12%)|145|(28.32%)|104|(30.14%)|182|(31.22%)|
|3|75|(14.73%)|64|(13.11%)|88|(17.19%)|62|(17.97%)|86|(14.75%)|
|4|40|(7.86%)|27|(5.53%)|37|(7.23%)|22|(6.38%)|38|(6.52%)|
|5|21|(4.13%)|14|(2.87%)|14|(2.73%)|12|(3.48%)|31|(5.32%)|
|6|6|(1.18%)|10|(2.05%)|8|(1.56%)|3|(0.87%)|7|(1.20%)|
|7|4|(0.79%)|3|(0.61%)|2|(0.39%)|3|(0.87%)|2|(0.34%)|
|8|||1|(0.20%)|2|(0.39%)|||||
|9|||||||||1|(0.17%)|
|10|||1|(0.20%)|||||||



13 

assigned to play more than once a day. 

In chapters 3 and 5 of this thesis we explore in more details the research studies by Ferland and Fleurent (1991) and by Costa (1995), including our remarks on their models for the NHL scheduling problem and also on the solution approaches they proposed to solve it. 

To provide a more general context for the NHL problem of our study, we review in the remaining of this chapter a number of scientific publications in sports scheduling. 

# **2.3 Literature on time-constrained sports scheduling problems** 

By far, most of the studies on sports scheduling either deals with leagues that play some time-constrained RRT as their regular-season schedules, or addresses a number of fundamental questions regarding such well-structured tournaments. Although the whole structure of the NHL regular season does not induce a compact schedule, the literature on both practical and theoretical aspects do provide us with insights into solving the NHL scheduling problem. 

In line with the most fundamental aspects, Easton _et al_ . (2004) highlight the direct analogy between latin squares and single RRT (and thus mirrored double RRT). A latin square of order _n_ is an _n×n_ array filled with the elements from the set _S_ = _{_ 1 _,_ 2 _, . . . , n}_ , such that each element appears exactly once in each row and exactly once in each column. Reductions of part of the extensive studies on latin squares to single RRT scheduling are presented in Easton (2003), providing some important results with regard to, e.g., the scheduling of tournaments with fixed games, which is one of the most common constraints found in practical applications (Easton _et al_ ., 2004). Specifically, Easton (2003) uses the NP-completeness results on partially completed latin squares in Easton and Gary Parker (2001) to show that a single RRT with 

Table 2.2 _Length of road trips in official NHL schedules_ Frequency of road trips by their individual number of games (# _g_ ) in the official schedules of past seasons 

|#_g_|2009|-10|2010|-11|2011|-12|2012|-13|2013|-14|
|---|---|---|---|---|---|---|---|---|---|---|
|1|253|(47.83%)|262|(50.38%)|255|(47.93%)|165|(46.35%)|295|(48.60%)|
|2|132|(24.95%)|133|(25.58%)|130|(24.44%)|96|(26.97%)|131|(21.58%)|
|3|77|(14.56%)|73|(14.04%)|77|(14.47%)|50|(14.04%)|93|(15.32%)|
|4|35|(6.62%)|29|(5.58%)|45|(8.46%)|24|(6.74%)|59|(9.72%)|
|5|18|(3.40%)|18|(3.46%)|15|(2.82%)|13|(3.65%)|20|(3.29%)|
|6|11|(2.08%)|4|(0.77%)|7|(1.32%)|6|(1.69%)|6|(0.99%)|
|7|2|(0.38%)|1|(0.19%)|2|(0.38%)|1|(0.28%)|2|(0.33%)|
|8|1|(0.19%)|||||||1|(0.16%)|
|9|||||1|(0.19%)|1|(0.28%)|||



14 

fixed games can be scheduled in polynomial time only for a very few special cases, as the problem is NP-complete even _i_ ) if on average each team has two games scheduled; or _ii_ ) if all but three rounds are completely scheduled and every team has at most three unscheduled games. 

A latin square of order _n_ , with _n_ even, is closely related to 1-factorization of a complete graph _Kn_ , which is, in turn, equivalent to an edge coloring of _Kn_ and also to a decomposition of _Kn_ into perfect matchings. Therefore, another analogy (probably more popular) occurs between an RRT and an edge coloring of _Kn_ with _n −_ 1 colors (Easton _et al_ ., 2004). To be more precise, an _oriented coloring_ of the graph _Kn_ , which is defined by a 1-factorization of _Kn_ together with an orientation, completely defines a schedule for the single RRT: each node _k_ in the graph correspond to a team _k ∈{_ 1 _,_ 2 _, . . . , n}_ in the league and an arc ( _i, j_ ) represents the game to be played by team _i_ against team _j_ , at the venue of team _j_ , on the specific round represented by each 1-factor (and thus by each color). Several research studies focus on graph-based models, including de Werra (1980, 1981, 1982, 1985, 1988), Knust and von Thaden (2006), Schreuder (1980, 1992) and Van Weert and Schreuder (1998). 

Although Combinatorics has efficient methods for some special situations (Easton, 2003; Hamiez and Hao, 2004), scheduling an RRT normally becomes a very hard combinatorial problem when additional constraints, such as arena availability or travel distances, are considered. Furthermore, researches in general have provided compelling evidence that developing appropriate models in sports scheduling is as much of an issue as the choice of solution methodologies to be employed (Trick, 2005; Kendall _et al_ ., 2010) . 

In particular, traditional approaches often decompose the problem into at least the following two phases: 

( _i_ ) determining the opponent of every team in each round; and 

( _ii_ ) determining which team in every match plays at home (so that its opponent is the one to play away) in each round. 

Such phases have been sequentially solved both in the order we present them as well as in the reverse order. Indeed, Knust (2014) lists 12 references (e.g., Trick, 2001; Elf _et al_ ., 2003; Miyashiro and Matsui, 2005; Post and Woeginger, 2006; Brouwer _et al_ ., 2008; Cheung, 2008) that uses a _first-schedule-then-break (FSTB) approach_ , which first deals with phase ( _i_ ), and then, with phase ( _ii_ ); and 20 references (e.g., Schreuder, 1992; Nemhauser and Trick, 1998; Henz, 2001; Miyashiro _et al_ ., 2003; Rasmussen and Trick, 2007; Briskorn, 2008a; Knust and L¨ucking, 2009; Larson and Johansson, 2014) that uses a _first-break-then-schedule (FBTS) approach_ , which proceed from phase ( _ii_ ) to phase ( _i_ ), instead. In those terms, a “break” refers to the occurrence of a round when a team shifts to a an away game after having played at home in the previous round, or the team shifts to a home game after an away game. 

15 

Decomposition approaches like that have benefited from fundamental progress in the design of models and algorithms for some specially-created sports scheduling problems. In general, triggered by real-world applications, such rather theoretical problems gave rise to most of the current literature on sports scheduling, which normally does not take into account many of the complex issues that appear in practice. In particular, the problems are often easy to state, either by some mathematical formulation (specifying a few types of constraints and, more often than not, an objective function) or by no more than a descriptive definition. This allows researchers to focus not only on the development of appropriate models but also in the improvement of solution methodologies which, in turn, may provide inspiration for dealing with practical problems, including others than those in sports scheduling. 

Throughout the following subsections, we present an informal description of some of the most investigated problems in the sports scheduling literature, and we also point out a number of contributions to each of them. In particular, the examples we mention here include both studies that focus “only” on constructing a feasible schedule and studies that try to find the best schedule with regard to a certain evaluation function. 

# **2.3.1 Finding home-away patterns** 

A _home-away pattern_ (HAP) is a sequence of home games, away games, and byes related to a particular team and according to which the team plays during the tournament. Such a pattern is often represented by a vector with an entry for each round containing either an H, an A, or a B to indicate that the team has, in the corresponding round, a home game, an away game, or a bye, respectively. Regarding the construction of a schedule for _n_ teams, an _HAP set_ is a set of exactly _n_ home-away patterns, each one associated with a particular team. 

Obviously, creating an HAP set in order to have a corresponding RRT schedule requires to satisfy certain constraints (enforcing, for example, a proper pairing of the patterns). An HAP set for which an RRT schedule exists is said to be _feasible_ . And the task of determining whether a given HAP set is feasible is known as the _HAP Set Feasibility Problem_ (Briskorn, 2008a). Researches have been conducted to establish necessary and sufficient conditions for the feasibility of a given HAP set to different types of tournaments (de Werra, 1980, 1988; Schreuder, 1992; Van Weert and Schreuder, 1998; Easton _et al_ ., 2001; Miyashiro _et al_ ., 2003; Lim _et al_ ., 2006; Briskorn, 2008b). However, sufficient conditions for general HAP set feasibility remain unknown. 

16 

# **2.3.2 Optimizing breaks** 

The number of consecutive games played away (at home likewise) by any given team is strongly related to fairness among all the teams in a tournament (de Werra, 1981) and also to attractiveness of the games (Bartsch _et al_ ., 2006; Drexl and Knust, 2007). Therefore, the lengths of both sequences of Hs and sequences of As in an HAP is especially relevant in virtually any sports scheduling problem. When a team plays either two consecutive games at home or two consecutive games away, that team is said to have a _break_ in the last of the corresponding two rounds. Ideally, the course of games played by any given team would be alternated between home and away games as regularly as possible. 

Minimizing breaks is the first objective in sports scheduling (Kendall _et al_ ., 2010). Lower bounds on the number of breaks have been stated, notably by de Werra (1981), for different kinds of tournaments. In particular, while it is possible to construct an RRT without any break for an odd number of teams, an RRT for _n_ teams has at least _n −_ 2 breaks if _n_ is even. Theoretical results and efficient (polynomial) methods on generating an RRT schedule with minimum number of breaks are well known when no additional constraints are considered (de Werra, 1981, 1988; Schreuder, 1992; Van Weert and Schreuder, 1998). 

However, no efficient method is currently known when a cost is associated to each assignment of a game to a round and the goal is to find a schedule having that minimum number of breaks while minimizing the sum of the costs of the assignments (Briskorn, 2008b). For this special case, Briskorn and Drexl (2007) develop and apply, at first, a branch-and-price approach (with slightly disappointing results), and then, a heuristic variant of the same approach that is reported to provide good solutions for random instances (yet limited to no more than 10 teams). 

In virtually all practical applications, schedules with the minimum number of breaks we just mentioned (i.e., _n −_ 2 for _n_ teams) normally does not satisfy many kinds of requests. Examples of such requests are presented by Nemhauser and Trick (1998) for the basketball competition of the Atlantic Cost Conference (ACC), which includes restrictions on the place where certain teams can play on a given round and restrictions on the order in which specific opponents are visited by a team. Inspired by the works of Russell and Leung (1994) and of Schreuder (1992), they solved the scheduling problem of the ACC through a combination of IP and complete enumeration. In fact, Nemhauser and Trick (1998) used a rather typical decomposition approach that at first generates feasible home-away (and _bye_ ) patterns by enumeration; after, uses IP to find pattern sets for “placeholder teams”; next, uses also IP to find timetables for placeholders; and then, assigns actual teams to placeholders by complete enumeration. For each one of these four phases, a certain part of the constraints of the problem was taken into consideration. Shortly later, a similar decomposition approach 

17 

was used by Henz (2001) with the crucial difference that all the phases were then solved only through CP. Comparing to the results from Nemhauser and Trick (1998) for the ACC 1997-98 season, in which around 24 hours were needed to create all the feasible schedules, this change in the approach led Henz (2001) to obtain the same schedules in less than one minute. Almost all this drastic reduction in solution time was achieved in the last phase alone, when assigning teams to placeholders. In order to solve the same problem, as well as other variants of it with break minimization, Rasmussen and Trick (2007) proposed an algorithm that iterates between those four phases where, for a certain iteration, only a limited number of the patterns are generated and Benders cuts arising from infeasibilities identified in other phases are used to generate new patterns. The algorithm was applied to problems on both mirrored and non-mirrored schedules, with and without place constraints, and is reported to excel in performance compared to previous approaches. Later on, Rasmussen (2008) also succeed in scheduling soccer games for a triple RRT of the Danish Football Association through the same logic-based Benders approach. 

Among other sports-scheduling applications involving minimization of breaks, we mention the construction of a double RRT schedule for the “Serie A” of the Italian Major Football League by Della Croce and Oliveri (2006). They report to be able to generate several schedules by adapting the decomposition approach of Nemhauser and Trick (1998), which, in the first phase, generates an HAP set that satisfies several constraints (some of them related to cable television requirements); in the second phase, produces a corresponding RRT schedule with placeholder teams; and, in the third phase, assigns actual teams to the placeholders in that schedule. Also, Van Hentenryck and Vergados (2005) propose a simulated annealing algorithm that is reported to find optimal solutions very quickly for large instances (e.g., 28 teams). 

Related to this context, many studies involve finding a schedule that minimizes the number of breaks for the special situation in which, on every round, the opponent for each team is already known. Namely, given an _opponent schedule_ , which is a timetable with the rows individually associated to the teams, and the columns to the rounds, such that every entry specifies the opponent of the respective team on the corresponding round, the _Break Minimization Problem_ (which we refer to as BMP) consists in finding an associated feasible HAP set that results in a schedule with the minimum number of breaks. Some authors (e.g., Trick, 2011) uses the acronym CBMP to refer to a more general constrained problem where the minimization of breaks is not necessarily subject to a certain opponent schedule, but to any kind of constraint instead. 

The BMP has been widely addressed in sports scheduling papers. Whether embedded in more general models or in practical applications, it normally appears in the two-phase 

18 

decomposition approach we mentioned earlier (p. 14), in which all the games (matching of teams) are assigned in one phase ( _i_ ), while the place for each game is only determined in the other phase ( _ii_ ). 

An extensive study about the BMP (and also about some of its variations, which include new constraints) is conducted by R´egin (2001) through the use of a CP approach that involves global constraints with which efficient filtering algorithms are associated. He was able to solve instances of up to 20 teams. Based on the discoveries of that study, Trick (2001) presents an IP model for the BMP that is reported to be at least competitive with R´egin’s CP model. He was able to solve instances of up to 22 teams. Elf _et al_ . (2003) transform the BMP into a maximum cut problem in an undirected graph and then apply a branchand-cut algorithm to both randomly-generated instances and the real-world instance of the Bundesliga 1999-2000 (the first national German soccer league). They were able to solve instances of up to 26 teams. Miyashiro and Matsui (2006) and Suzuka _et al_ . (2007) formulate the problem as a maximum restricted cut and a maximum 2-satisfiability problems, and apply the approximation algorithm by Goemans and Williamson (1995), which is based on a positive semidefinite programming relaxation. They were able to solve instances of up to 40 teams. 

Despite the advantages of having a schedule with minimum number of breaks, longer sequences of consecutive away games would imply fewer road trips for a team and thus reduced traveling distances in total. Therefore, in some contexts, normally where venues are located far from each other (as in the NHL problem), it is preferable to have a large number of breaks, so as to minimize traveling distances. Russell and Leung (1994) are the first to consider the problem of finding a HAP set that maximizes the number of breaks for a given opponent schedule. But breaks minimization and breaks maximization were first treated together by Miyashiro and Matsui (2005). In particular, these two problems are shown to be equivalent for a single RRT if the opponent schedule is known beforehand: an optimal solution for one problem can be directly constructed from an optimal solution for the other one. 

Urrutia and Ribeiro (2006) and Rasmussen and Trick (2007) deal with maximization of breaks in special cases of the Traveling Tournament Problem, which we describe in the following subsection. 

# **2.3.3 The Traveling Tournament Problem** 

The duration of a tournament might be too short for teams to play according to the highly-alternating HAP of a schedule with only a few breaks. This is especially the case when, as in the NHL, there are venues located very far from each other. Due to obvious 

19 

economic issues and possibly to players’ fatigue (Smith _et al_ ., 2000), only trying to alternate home games and away games as much as possible may not be suitable for some sports leagues around the world (Oberhofer _et al_ ., 2010). In fact, in order to reduce traveling distances (and times), a team should have as many consecutive away games as possible, considering it goes directly from one opponent’s venue to that of the next one without returning home before the corresponding breaks. 

Inspired by a real-world sports scheduling problem that requires minimization of traveling distances, namely the scheduling of the Major League Baseball (MLB) regular season, Easton _et al_ . (2001) introduces the _Traveling Tournament Problem_ (TTP). Given the distances between each pair of venues, a lower bound _l_ and an upper bound _u_ on the number of consecutive home and consecutive away games, the TTP consists in scheduling a double RRT for _n_ teams that minimizes the total distance traveled during the tournament by all teams, subject to the constraint that every team must play between _l_ and _u_ consecutive away games and between _l_ and _u_ consecutive home games. Typical values for _l_ and _u_ are 1 and 3, respectively. As noted by Trick (2011), most of the studies on the TTP also include the so-called _no-repeater constraint_ , which imposes that if a team _i_ plays at home against a team _j_ in one round then _j_ must not play at home against _i_ in the next round. Obviously, as in the NHL problem of this thesis, every team on a TTP is assumed to have its own venue at its home city, where it begins and ends the travels over all the tournament. In addition, every time a team plays two consecutive away games, it travels directly from the venue of its first opponent to that of the second one. 

Since it was first announced, in 2001, some variants of the TTP have been proposed in order to capture further requirements in sports scheduling applications, and also, to stimulate researchers on the development of new approaches. Among such variants, we mention the _Timetable Constrained Distance Minimization Problem_ (TCDMP), introduced by Rasmussen and Trick (2006), and the _TTP with Predefined Venues_ (TTPPV), proposed by Melo _et al_ . (2007). The TCDMP can be defined as follows: given an opponent schedule (timetable) for a double RRT, the distances between each pair of venues, and a lower bound and an upper bound on the number of consecutive away games and consecutive home games, find a corresponding feasible HAP set which minimizes the total distance traveled during the tournament by all teams. Therefore, the TCDMP is a generalization of the BMP, which we defined earlier (p. 17), where distances are now considered in the objective function, instead of breaks (Rasmussen and Trick, 2009). As for the TTPPV, it can be defined as follows: given the venue where each game of a single RRT will take place and the distances between any pair of venues, find a schedule in which the total distance traveled by all teams is minimized and no team plays more than three consecutive away games or more than three consecutive 

20 

home games. 

The TTP and its variants are among the most studied problems in the sports scheduling literature. Indeed, the classification of pertinent literature by Knust (2014) currently list almost 50 papers that deals with the TTP. Numerous benchmark instances and best-found results are presented on the TTP website `http://mat.gsia.cmu.edu/TOURN/` . In particular, the “NL instances” introduced by (Easton _et al_ ., 2001) were inspired in the National League (one of the two leagues constituting the MLB), and today, are probably the best-know class of TTP instances. Although the TTP is very simple to state and typical instances are made up from quite little data, it has proved to be very difficult to solve. Even for a very small number of teams, TTP instances have challenged many researchers in combinatorial optimization. In fact, in its original form, only instances with as few as 10 teams have been solved to optimality. Curiously, for example, the classic NL8 instance (with 8 teams) was only solved to provable optimality for the first time by Irnich (2010), almost 10 years after it was announced. 

Several state-of-the-art algorithms have been systematically applied in order to determine either improved lower bounds or better objective function values for benchmark instances of the TTP. The first algorithms, which combine CP and IP approaches, were proposed by Easton _et al_ . (2001, 2003) and Easton (2003). They were able to find an optimal solution for the NL8 without the non-repeater constraint by means of a parallel implementation of a branchand-price algorithm in which an IP approach solves the master problem and a CP approach solves the pricing problem. Later on, Irnich (2010) revisited that CP-based branch-andprice, reformulated its pricing problem as a shortest-path problem over an extended network, and implemented new branching techniques, which led him to obtain several improved lower bounds and some optimal solutions for previously unsolved TTP instances, including the NL8 (with the non-repeater constraint). Around the same time, Uthus _et al_ . (2009) presented a remarkable work in which a parallelized DFS* (a variant of a depth-first branch-and-bound search that keeps all heuristic estimates in memory) is able to find past known optimal solutions much faster than previous approaches and to greatly improve the lower bounds of larger TTP instances. More recently, those same authors (Uthus _et al_ ., 2012) also proposed a new approach based on iterative-deepening A* (a greedy best-first-search guided by a heuristic strategy) that is able to find past known optimal solutions even faster than their DFS* and that turns out to be the first approach to find optimal solutions to all 10-team instances (including the NL10) of the four TTP classes to which it was applied. 

21 

# **2.3.4 Typical constraints in sports scheduling** 

Although each sports scheduling problem has its own set of constraints and objectives, the literature often come up with common requirements found in different studies. In 2010, on the occasion of the International MultiConference of Engineers and Computer Scientists, a dozen of authors (Nurmi _et al_ ., 2010) proposed a framework for sports scheduling problems as an attempt to establish a common ground for the development of benchmark instances which would allow researchers to evaluate and compare their solution approaches. In particular, Nurmi _et al_ . (2010) outline 36 typical constraints inspired from both theoretical and realworld problems. For the sake of clarity, the statements for those constraints are reproduced bellow. 

- Structural requirements: 

   - C01. There are at most _R_ rounds available for the tournament. 

   - C02. A maximum of _m_ games can be assigned to round _r_ . 

   - C03. Each team plays at least _m_ 1 and at most _m_ 2 games at home. 

   - C22. Two teams play against each other at home and in turn away in 3RR or more. 

- Home-away requirements: 

   - C04. Team _t_ cannot play at home in round _r_ . 

   - C05. Team _t_ cannot play away in round _r_ . 

   - C06. Team _t_ cannot play at all in round _r_ . 

   - C07. There should be at least _m_ 1 and at most _m_ 2 home games for teams _t_ 1 _, t_ 2 _, . . ._ on the same day. 

   - C08. Team _t_ cannot play at home on two consecutive calendar days. 

   - C09. Team _t_ wants to play at least _m_ 1 and at most _m_ 2 away tours on two consecutive calendar days. 

   - C23. Team _t_ wishes to play at least _m_ 1 and at most _m_ 2 home games on _weekday_ 1, _m_ 3 _− m_ 4 on _weekday_ 2 and so on. 

- Special-game requirements: 

   - C10. Game _h_ -team against _a_ -team must be preassigned to round _r_ . 

   - C11. Game _h_ -team against _a_ -team must not be assigned to round _r_ . 

   - C24. Game _h_ -team against _a_ -team cannot be played before round _r_ . 

   - C25. Game _h_ -team against _a_ -team cannot be played after round _r_ . 

   - C34. Game _h_ -team against _a_ -team can only be carried out in a subset of rounds _r_ 1 _, r_ 2 _, r_ 3 _, . . ._ . 

- Break requirements: 

22 

   - C12. A break cannot occur in round _r_ . 

   - C13. Teams cannot have more than _k_ consecutive home games. 

   - C14. Teams cannot have more than _k_ consecutive away games. 

   - C15. The total number of breaks must not be larger than _k_ . 

   - C16. The total number of breaks per team must not be larger than _k_ . 

   - C17. Every team must have an even number of breaks. 

   - C18. Every team must have exactly _k_ number of breaks. 

   - C35. A break of type A/H for team _t_ 1 must occur between rounds _r_ 1 and _r_ 2. 

- Tournament-quality requirements: 

   - C19. There must be at least _k_ rounds between two games with the same opponents. 

   - C20. There must be at most _k_ rounds between two games with the same opponents. 

   - C21. There must be at least _k_ rounds between two games involving team _t_ 1 and any team from the subset _t_ 2 _, t_ 3 _, . . ._ . 

   - C26. The difference between the number of played home and away games for each team must not be larger than _k_ in any stage of the tournament (a _k_ -balanced schedule). 

   - C27. The difference in the number of played games between the teams must not be larger than _k_ in any stage of the tournament (in a relaxed schedule). 

   - C36. The carry-over effects value must not be larger than _c_ . 

- Strength-group requirements: 

   - C28. Teams should not play more than _k_ consecutive games against opponents in the same strength group. 

   - C29. Teams should not play more than _k_ consecutive games against opponents in the strength group _s_ . 

   - C30. At most _m_ teams in strength group _s_ should have a home game in round _r_ . 

   - C31. There should be at most _m_ games between the teams in strength group _s_ between rounds _r_ 1 and _r_ 2. 

   - C32. Team _t_ should play at least _m_ 1 and at most _m_ 2 home games against opponents in strength group _s_ between rounds _r_ 1and _r_ 2. 

   - C33. Team _t_ should play at least _m_ 1 and at most _m_ 2 games against opponents in strength group _s_ between rounds _r_ 1 and _r_ 2. 

In general, a benchmark instance for a highly-constrained sports scheduling problem can then be characterized by standard information, which includes the number of teams, the type of RRT, and among the constraints from the list above, the sets of both hard and soft constraints taken into account, with their respective parameters. Obviously, these 36 constraints 

23 

do not cover all the constraints that might appear in many real-world sports scheduling problems. In particular, they are not inclusive enough to allow a complete specification of an instance for the NHL scheduling problem, as we will point out in the next chapter. 

In their survey on round-robin scheduling, Rasmussen and Trick (2008) characterize the following eight common types of constraints, for which we identify some possible relations to the constraints in Nurmi _et al_ . (2010). 

- _Place constraints_ Constraints enforcing certain teams to play at home or away on specific rounds. They arise, for example, from unavailability of venues, and in general, can be specified by C04. 

- _Top-team and bottom-team constraints_ Constraints imposing that teams from a similar strength group must have their games somewhat evenly distributed through all the rounds, or that certain teams should not play consecutive games against opponents from a similar strength group. They can usually be specified by the statements from C28 to C33. 

- _Break constraints_ Constraints ensuring that no breaks occur on certain rounds. They can be stated by C12. 

- _Game constraints_ Constraints fixing or forbidding certain games on particular rounds. They can be specified by C10 or C11. 

- _Complementary constraints_ Constraints imposing that certain teams must not be assigned to home games that would be simultaneously played on any particular round. They arise, for example, when two teams share the same venue as home. Although Nurmi _et al_ . (2010) does not directly specify any particular constraint for this case, such constraints could be stated by C31 with a “strength group” _s_ being the set of corresponding teams, _m_ = 1, and _r_ 1 and _r_ 2 being the first and the last rounds, respectively. 

- _Geographical constraints_ Constraints enforcing the games to be, on any round, somewhat evenly distributed throughout all regions of the tournament. They could also be stated by C31 with a “strength group” _s_ being the set of teams with venues in a specific region, _m_ being a reasonable number of games, and _r_ 1 and _r_ 2 being the first and the last rounds, respectively. 

- _Pattern constraints_ Constraints over the HAP of each team ensuring, for example, that the number of consecutive games at home (or away) stays within a certain range, or yet that all teams have the same number of breaks in their HAPs. Such constraints can usually be specified by the statement from C12 to C18, and by C35. 

24 

- _Separation constraints_ Constraints imposing lower and upper bounds on the number of rounds between consecutive games involving the same pair of teams. Obviously, they arise from an attempt to evenly spread such games through the whole period of the tournament, and in general, can be specified by the statements from C19 to C21. 

# **2.4 Literature on time-relaxed sports scheduling problems** 

Nearly all the scientific literature on sports scheduling has focused on the study of compact schedules. This predominance of researches on time-constrained problems may be due to both the rather neat structure of a compact schedule and their high popularity among major professional sports around the world. 

In non-commercial leagues, however, time-relaxed schedule is the most widely adopted structure (Knust, 2010). The regular seasons of both the NHL and the National Basketball Association (NBA) are two rare examples of major tournaments in which the number of days “available” for potential assignments of games is much larger than the number of games to be played by a team. In particular, teams may play different numbers of games during a certain week, and the number of weekly games are often unevenly spread throughout the season. 

Scheduling for non-commercial leagues normally requires special attention not only to the limited access to sports facilities for the home games of each team, but also to the sporadic availability of sportsmen. In fact, in such contexts, a team is usually able to provide only a relatively small number of potential dates for its home games, while many other dates may not be available for away games, either. 

In a recent work, Knust (2010) deals with non-commercial sports league scheduling. A time-relaxed schedule is to be found for a double RRT with several hard constraints, including unavailability of teams to play away on certain dates, and also soft constraints, including minimization of breaks. In particular, the tournament is assumed to be made up of two half series, one after the other, and every team must play once at home in one series and once away in the other series against each other team. Either half series refers thus to a single RRT. In addition, regarding each team, the number of home games must not differ by more than one from the number of away games. This restriction over a single RRT defines a _balanced homeaway assignment_ for the matches (Knust and von Thaden, 2006). The paper presents two formulations for the problem, one as an IP model and the other as a multi-mode resourceconstrained project scheduling problem, and a two-phase heuristic algorithm is proposed. In the first phase of the algorithm, a balanced home-away assignment for the matches is determined with an implementation of connected neighborhood structures introduced with theoretical results by Knust and von Thaden (2006). In the second phase, an adapted genetic 

25 

algorithm for resource-constrained project scheduling problems is used, and then, matches are reassigned to different days as an attempt to evenly distribute the games over the whole season. The heuristic is reported to be very efficient for a number of benchmark instances and was then used to schedule two seasons of regional table-tennis leagues in Germany. Knust (2010) mentions trying to solve, with a similar two-phase approach, time-constrained problems subject to a hard constraint enforcing the number of breaks to be at their minimum, but feasible solutions were only found for a few instances. This might indicate that the approach is not well suited for the special structure of time-constrained problems, even so the minimum-break requirement seems too restrictive. 

For other studies on scheduling non-commercial leagues, we refer to Sch¨onberger _et al_ . (2000) and to Sch¨onberger _et al_ . (2004), where similar tournaments (also for a table-tennis league in Germany) are scheduled by Genetic Algorithms and by CP approaches. 

Another example of real-world tournament that gives rise to a time-relaxed schedule is the 1992 World Cup of Cricket. Addressed by Armstrong and Willis (1993), the problem consists in scheduling a single RRT for 9 teams, such that every team plays its corresponding 8 games in a period of 26 days, and for which 19 venues scattered over a large geographical area (in Australia and New Zealand) are available. Among the many constraints taken into account, some are related to long traveling distances and others to several requirements from TV broadcasting. The paper presents an IP formulation, but due to both its large number of constraints (which turned out to be impractical for that time) and the need for having a more flexible approach, heuristic procedures are proposed to solve the problem. Implemented in a spreadsheet package (Lotus 1-2-3), such heuristic procedures allow a user to sequentially assign games to days in an interactive manner. 

It seems that no other sport scheduling in the literature share so many identical issues with the NHL scheduling of this thesis as that of the NBA regular season. Therefore, we devote the following subsection specifically to studies on the scheduling of games for the NBA. 

# **2.4.1 The NBA scheduling problem** 

Like the NHL, the NBA currently consists of 30 teams, each one playing 82 games (41 at home and 41 away) according to a relaxed schedule for its regular season. The NBA features two 15-team conferences of three 5-team divisions each. Also, the teams are scattered throughout a vast geographical area in North America, 29 of them in the United States and one in Canada. 

To our knowledge, the problem of scheduling the NBA regular season has been studied at least on two occasions: in 1980 in a paper by Bean and Birge, and in 2009 in a Ph.D. thesis 

26 

by Bao. Generally speaking, the approach by Bean and Birge (1980) is quite practical and had, in fact, been applied to actual instances of at least four NBA regular seasons. It has probably served as an important baseline for the approach that Fleurent (1987) proposed later on for the NHL scheduling problem. The study by Bao (2009), on the other hand, follows an approach that is more in line with the researches on time-constrained problems that we mentioned earlier. He points out several types of constraints for the NBA scheduling problem, and for each type, he proposes both IP and CP formulations, which are implemented into a commercial solver and individually tested on randomly-generated instances. The remaining of this subsection is our review on these two studies. 

Bean and Birge (1980) develop schedules for some seasons in the 1980’s, when the NBA consisted of only 22 teams but each team had already to play 82 games in a period of around 170 days. The NBA scheduling problem of that time was to assign 902 games to dates of the regular season, such that a number of constraints were satisfied and the total traveling distance was minimized. In their paper, they mention that a typical arena used by an NBA team was usually available only on about 30% of the days of the season, and that this turned out to be the most difficult constraint they had to deal with. 

To provide some insight about the size and complexity of the problem, Bean and Birge (1980) present a mathematical formulation of a modified problem in which the season would consist of exactly 82 days and the teams would play every day of this fictional season. Of course, a solution for the problem would now be a compact schedule. In their model, the constraints are linear equalities and the objective function is also linear, all of them expressed in terms of four-index variables _xijkl ∈{_ 0 _,_ 1 _}_ for any triple of teams _i_ , _j_ , _k_ , and every day _l_ . One such variable, _xijkl_ , is set to value 1 only if team _i_ is assigned to travel from the city of team _j_ to the city of team _k_ to play a game on day _l_ . Clearly, the model has then _O_ ( _n_<sup>4</sup> ) variables. The objective function, whose value is to be minimized, is the sum of the daily traveling distances of all the teams, and the constraints impose the following structural requirements: _i_ ) for each pair of teams, a specific number of games must be played during the season; _ii_ ) if a visiting team is in a city to play, the respective home team must also be there; _iii_ ) all teams start the season at their own city and half of them go to visit the others in the first day; and _iv_ ) if a team leaves one city then it must have played in that city on the preceding day. Regarding the seasons in the 1980’s, the model entails almost 42 thousand constraints and more than 800 thousand variables. For the current seasons, where 30 teams play 82 games per team, it would have almost 78 thousand constraints and more than 2 million variables. Bean and Birge (1980) claim thus that finding a solution even for such simplified unrealistic formulation would be extremely difficult at the time. 

They propose then a two-phase heuristic approach for the NBA scheduling problem. In 

27 

the first phase, road trips with up to five away games for each team are created, and in the second phase, those trips are combined into a feasible schedule for the entire league. To be more precise, the approach can be outlined as follows. 

- _Phase I: Generating road trips_ This phase is similar to a classic savings heuristic originally proposed for routing problems by Clarke and Wright (1964). In particular, the following saving measure is used, for each team _k_ , to select the opponents, _i_ and _j_ , to be visited during a same road trip for _k_ : 



where dist( _·, ·_ ) is the distance between the cities of the respective pair of teams. The feasible road trips of each team _k_ are generated by first creating every road trip, _r_ = ( _k, l, k_ ), made up of a single away game against team _l_ , and then, by repeating the following steps, where a feasible road trip is always limited to at most five games. _Step 1)_ Calculate the saving, _sk_ ( _i, j_ ), for each pair of teams, _i_ and _j_ . _Step 2)_ Create a list with all ( _i, j_ )-pairs sorted in a non-increasing order of their savings. _Step 3)_ Make a single pass through that ordered list and for each pair at hand, ( _i, j_ ), merge the road trip that contains one of the corresponding teams, _i_ , with the road trip that contains the other team, _j_ , into a new feasible road trip if no more than five games are involved and if one team is at the end of one trip and the other team is at the begin of other trip, i.e., if the forms of those two trips are either ( _k, . . . , i, k_ ) and ( _k, j, . . . , k_ ), or ( _k, . . . , j, k_ ) and ( _k, i, . . . , k_ ). 

- _Phase II: Scheduling road trips_ In this phase, the heuristic firstly sorts all road trips by their total traveling distances, and subsequently, try to schedule them, from the longest to the shortest ones, into periods in which the corresponding traveling team has the least arena-available dates. When the road trip at hand cannot be feasibly scheduled, it is divided into two or more partial road trips, which in turn are to be scheduled with the same “sort-and-schedule” strategy, but only after all the current road trips have been considered. This iterative process continues until only road trips made up of a single game remain unscheduled. The games in such road trips are then individually scheduled to a feasible day that minimizes the increase in overall traveling distance. 

This two-phase heuristic was adapted later on by Fleurent (1987) for the NHL scheduling problem. This shall become evident to the reader in Chapter 5, especially when we describe the“forced-trip heuristic”and the“free-trip heuristic”, which generates road trips with games to be played far from the city of the corresponding traveling team. 

Bean and Birge (1980) report that their heuristic alone was able to find feasible schedules 

28 

for the NBA games. But since optimality was not guaranteed, they mention to have eventually used “switching algorithms” in an attempt to further reduce the overall traveling distance. Such algorithms would find the best feasible dates for each game, while considering fixed the rest of the schedule. They are, however, reported to lead to only few improvements over the initial feasible schedule. In spite of its rather vague description, it appears that this strategy was similar to the “exchange heuristics” used later on by Fleurent (1987) (which is described in Ferland and Fleurent, 1991, as well). 

More recently, Bao (2009) has also tackled the NBA scheduling problem in a chapter of his Ph.D. thesis. He claims that a schedule for the NBA regular season must satisfy numerous constraints, and then, he presents several of them. In particular, each constraint is formulated both by means of Integer Programming and by means of Constraint Programming. Computational results obtained with IBM ILOG CPLEX<sup>®</sup> 11.2 and with IBM ILOG CP Optimizer<sup>®</sup> 2.1 (for the IP and the CP models, respectively) are compared between them with regard to running time, as well as number of branch nodes (from the IP solver) and number of failed branches (from the CP solver). 

The experiments have been individually conducted for each type of constraints added to a basic formulation that only considers the structural requirements of the problem. The instances submitted to the solvers have been generated for even numbers of teams varying from 6 to 30. In each instance, the number of days provided by Bao (2009) is equal to the double of the corresponding number of games that every team has to play. The following is our informal description of those experiments, which, to provide an idea of how challenging the problem turned out to be under each type of constraint, also includes some of the main reported results. Bao (2009) limits each experiment to 30 minutes and uses a personal computer running Windows<sup>®</sup> XP with 2.2GHz Duo Core CPU and 1GB of RAM. 

- _Structure_ A single RRT is to be scheduled, such that only the essential constraints for such a tournament are taken into account, i.e., every team plays each of the others exactly once and no team plays more than one game per day. Feasible solutions for all the instances with up to 30 teams are found both by IP (in as long as 2.56 seconds) and by CP (in no more than 0.76 second). 

- _Interconference games_ A double RRT is to the scheduled for the interconference games, which are evenly divided into two conferences, such that every team plays once at home against each opponent. In the NBA, the structure of the interconference games is indeed a double RRT. While IP finds feasible solutions for the instances with up to 30 teams (in no more than 22 seconds), CP solves only instances with up to 22 teams (in less than 4 minutes), failing to solve the instances with 26 or more teams (in 30 minutes). 

29 

- _Intradivision games_ A quadruple RRT is to be scheduled, such that every team plays twice at home against each opponent. In the NBA, the structure of the intradivision games is indeed a quadruple RRT for each division (which currently involves five teams). Only instances with up to 10 teams were submitted to the solvers, and both IP and CP easily find feasible solutions (in no more than 0.17 second). 

- _Consecutive games_ A single RRT is to be scheduled, such that: no team plays at home on two consecutive days; no team plays more than two games on three consecutive days; and no team plays more than five games on eight consecutive days. Feasible solutions for all instances with up to 30 teams were found both by IP (in less than 3 seconds) and by CP (in as long as 2.3 minutes). 

- _Consecutive byes_ A single RRT is to be scheduled, such that: any team plays at least two games per week and at least one game during every five days. Feasible solutions for all instances with up to 30 teams were found both by IP (in as long as 4 minutes) and by CP (in less than 20 seconds). 

- _TV schedules_ A single RRT is to be scheduled for instances in which about 20% of the games are considered as being “attractive games”, such that: no more than a given number of attractive games are played on a same day; at least a certain number of attractive games are played on each of the days in a given special set of days; and every team plays at least two games per week. Feasible solutions for all instances with up to 30 teams were found both by IP (in no more than 0.41 second) and by CP (in no more than 0.91 second). 

- _HAP sets_ A single RRT is to be scheduled according to a given (feasible) HAP set. While IP finds feasible solutions for instances with up to 30 teams (in no more than 8.5 minutes), CP solves only instances with up to 14 teams (in less than 0.03 second) and fails to solve the instances with 18 or more teams (in 30 minutes). 

- _Arena availability_ A single RRT is to be scheduled for instances in which the arena of any team is available only on about 33% of the days. While IP finds feasible solutions for instances with up to 30 teams (in less than 2.3 seconds), CP solves only instances with up to 14 teams (in as long as 27 seconds), failing to solve the instances with 18 or more teams (in 30 minutes). 

- _Forbidden assignments_ A single RRT is to be scheduled for instances where, for each day, certain particular games should not be assigned. In the NBA, this occurs when, for example, a team requests not to have certain games on a particular day. Feasible solutions for all instances with up to 30 teams were found both by IP (in no more than 0.63 second) and by CP (in no more than 1.08 seconds). 

30 

   - _Complementary home games_ A single RRT for up to 30 teams is to be scheduled, such that exactly two given teams never play at home on a same day. In the NBA, this constraint occurs because two teams (the LA Lakers and the LA Clippers) share the same arena for their home games. Feasible solutions for all instances with up to 30 teams were found both by IP (in no more than 0.03 second) and by CP (in as long as 1.17 seconds). 

   - _Assignment-value maximization_ A single RRT is to be scheduled for instances where a fixed value (between 0 and _n_<sup>2</sup> for a problem with _n_ teams) is given for each potential game-day assignment, and the sum of the values for the actual assignments in a feasible solution is to be maximized. While IP finds optimal solutions for instances with up to 30 teams (in less than 2 seconds), CP fails to solve even the instances with only 6 teams (in 30 minutes). This contrasting result is somehow expected, since the solvers are dealing with an optimization problem in this particular experiment. 

   - _Back-to-back games_ A single RRT is to be scheduled, such that every team plays a same given small number of back-to-back games. Only instances with up to 10 teams were submitted to the solvers, and both IP (in no more than 34 seconds) and CP (in as long as 14 minutes) find feasible solutions. 

   - _Weekend games_ A single RRT is to be scheduled, such that every team plays a same given small number of games on weekends (Fridays, Saturdays, and Sundays). Only instances with up to 24 teams are solved by IP (in as long as 29.6 minutes); and although solutions are found for instances with 20, 24, and 28 teams (in just 0.38 second), CP fails to solve (in 30 minutes) almost 40% of the instances with up to 30 teams. 

   - _Bounded traveling distances_ A single RRT is to be scheduled, such that the total traveling distance for each team remains within a particular given range. Both IP and CP fail to find feasible solutions, even for those with only as few as 6 teams. 

- It is important to notice that all these experiments have been undertaken one at a time, 

- which might be suitable on providing insights into the development of decomposition approaches as those we mentioned earlier for minimizing breaks. In particular, Bao (2009) does not test models integrating into a same formulation the different types of constraints. 

31 

# **CHAPTER 3** 

# **THE NHL SCHEDULING PROBLEM** 

The NHL scheduling problem consists in assigning a playable day to each game of the NHL regular season by not imposing more than one single daily game for any team. The game-day assignments should obviously satisfy several other constraints that are imposed either by the NHL, or individually, by the teams. Although the requirements, the goals, and even the structure of the NHL may change from one season to another, we will try to establish the most essential components of a good NHL schedule in the present days. In particular, all the factors taken into account in the pertinent literature that are relevant nowadays are being considered in this thesis. 

In this chapter, we present the structure of the NHL and the structure of its regular season. The requirements and goals for an NHL schedule are described, and then, compared with those in the literature on the same problem. 

# **3.1 The structure of the NHL** 

The NHL is currently formed by 30 franchised member clubs, which we refer to as _teams_ , that are located throughout the vast territories of the United States and Canada. The teams are distributed into two _conferences_ which, over the past years before 2013, has individually aggregated three _divisions_ of five teams each. Since the 2013-14 season, however, the NHL teams are split into four divisions of either seven or eight teams: two eight-team divisions form the Eastern Conference, and two seven-team divisions form the Western Conference. This structure is shown in Table 3.1. 

Because the NHL operates as a franchise system, the term “division” refers to a group of teams arranged not by their competitive level but by other factors, which may include their geographical locations, their rivalries, and their time zones. In particular, the teams within any specific division usually have their individual venues (for which we adopt the standard term _arenas_ ), located in the same geographical region. But overall, the distances between the home arenas of two NHL teams range from only a few miles to as much as 2700 miles (about 4500 km). Furthermore, comparing to the case of the Eastern Conference, the arenas in the Western Conference are, for the most part, located much farther from each other. This fact normally results in longer travel times for the Western teams, which could be somewhat aggravated or relieved, depending on the schedule of games assigned to them. 

32 

Table 3.1 _The current NHL structure_ The NHL teams disposed by their respective division and conference. 

|_Western Conference_|_Central _|_Division_|_Pacifc_|_Division_|
|---|---|---|---|---|
||CHI|Chicago Blackhawks|ANA|Anaheim Ducks|
||COL|Colorado Avalanche|ARZ|Arizona Coyotes|
||DAL|Dallas Stars|CGY|Calgary Flames|
||MIN|Minnesota Wild|EDM|Edmonton Oilers|
||NSH|Nashville Predators|LAK|Los Angeles Kings|
||STL|Saint-Louis Blues|SJS|San Jose Sharks|
||WPG|Winnipeg Jets|VAN|Vancouver Canucks|
|_Eastern Conference_|_Atlanti_|_c Division_|_Metrop_|_olitan Division_|
||BOS|Boston Bruins|CAR|Carolina Hurricanes|
||BUF|Bufalo Sabres|CBJ|Columbus Blue Jackets|
||DET|Detroit Red Wings|NJD|New Jersey Devils|
||FLA|Florida Panthers|NYI|New York Islanders|
||MTL|Montreal Canadiens|NYR|New York Rangers|
||OTT|Ottawa Senators|PHI|Philadelphia Flyers|
||TBL|Tampa Bay Lightning|PIT|Pittsburgh Penguins|
||TOR|Toronto Maple Leafs|WSH|Washington Capitals|



In general, changes in the NHL structure occur (when they do) on a very small scale from one year to the next. In the early 2013, however, a new NHL structure with the 30 teams distributed into only four divisions was proposed, which is now being implemented for at least three NHL regular seasons, starting at the 2013-14 season (Rosen, 2013). A method for changing sports leagues structures, which falls outside the scope of this thesis, is proposed by Macdonald and Pulleyblank (2014), specially for the case of the NHL, as an attempt to enable the construction of better schedules with regard to the total travel distance for the whole league. 

# **3.2 The structure of the NHL regular season** 

The NHL regular season usually starts in the first week of October each year and runs until mid-April. During that period, a total of 1230 games are played. Each game is a match between a _home team_ , which is the owner of the arena where the game is held, and an _away team_ (or likewise referred to as _visiting team_ ). Exactly 82 regular season games are played by every NHL team, 41 at _home_ and the other 41 games on the road (or equivalently, _away_ ). 

33 

All those games will have been completely specified by the time a schedule is designed. 

For each NHL regular season between 2008 and 2013, for example, every team played 24 _intradivisional games_ (against the other four teams in its own division), 40 _interdivisional games_ in its own conference (against the 10 teams from the other divisions), and 18 _extra-conferencial_ games (against the 15 teams from the other conference). Specifically, the intradivisional games for any team consisted of six games against each of the other four teams in its own division, where three of them were held at home, and the three others, away. With respect to the interdivisional games, a team played four times, two at home and two away, against every single extra-divisional rival in its own conference. Finally, the remaining 18 games for any team consisted of one game against each of the 15 teams in the other conference and three wild-card games versus three of those teams. 

At the present, however, every team plays two games against each team outside its conference, and three games against each team inside its conference but outside its division. In addition, every team plays either four or five games against the other teams in its own division. 

As mentioned earlier, the aggregation of teams into the two conferences and their different divisions is substantially related to the geographical distribution of the arenas of those teams. In particular, because teams within the same division are often located in the same region, the NHL regular season structure indicates that teams based within the same region usually play between themselves more often than those located farther from each other. Hence, most of the games give rise to trips over relatively short distances. The total distance that a team must travel, however, strongly depends on the whole schedule for the regular season. 

# **3.2.1 The availability of dates, teams, and arenas** 

Even though the NHL regular season runs from early October to mid-April, there are some dates during that period of around 190 days on which no game scheduling is allowed. Indeed, several constraints are imposed either by the NHL or by any of its member clubs to the dates suitable for having a game. Firstly, the NHL managers usually specify a few dates that must be excluded from the playable dates. Such restriction often arises from some holidays or special events like the Winter Olympic Games and the NHL All-Star Game. These events alone typically shut out from consideration between seven and fourteen days at the midway point of the regular season. Secondly, it may happen that a team is not available to play at some specific date because of an exceptional event to which the club is locally committed, for example. So the individual availability of the teams may also be an important concern when designing an NHL schedule. Finally, the factor to which the pertinent scientific literature, specially Ferland and Fleurent (1991), gives the most attention is the availability of arenas. 

34 

Although every team has its corresponding arena where home games take place, the building housing an arena may also be used for a variety of other entertainments. In fact, an arena might be assumed to be unavailable for a certain day if any major event is occurring in the same city or region where a club is based on, which could inhibit interest of fans or causes public safety concerns, for example. 

The availability of arena differs from one team to the other and some clubs may hardly be able to provide the minimum number of feasible dates for home games required by the NHL managers. Costa (1995) mentions the case of the 1993-94 regular season, when the number of home games per team changed to 41 and the NHL managers asked each club to provide at least 56 (thus 15 extra) arena dates for the scheduling of those games. He reports that such dates may not be enough to yield a reasonable schedule. According to Ferland and Fleurent (1991), this is the main reason why an NHL schedule design usually follows through several months of mutual discussions and arrangement of dates. 

# **3.3 The scheduling problem of the NHL regular season** 

Here, we describe the NHL scheduling problem in a rather informal manner. A mathematical model with integer variables will be proposed in Chapter 4. 

Because several games are played almost every day of the NHL regular season, the standard meaning of “bye” in the sports scheduling literature (Kendall _et al_ ., 2010) will be used for the NHL scheduling problem. So a team is said to have a _bye_ on a certain day if that team is not scheduled to play on that day. 

Moreover, we define a _road trip_ (or simply _trip_ ) for an NHL team as a sequence of all its away games scheduled to a period with no home games for that team and during which it has no more than two byes (off days) between two consecutive games. Whenever a road trip has more than one game, the corresponding travelling team plays then at least one game for each three consecutive days within that road trip period. 

We denote by _a_ @ _h_ a game where a team _a_ plays against a team _h_ in the arena of _h_ , and by [ _a_ @ _h_ : _d_ ] the scheduling of the game _a_ @ _h_ on a day _d_ , or equivalently, the _assignment_ of a day _d_ to the game _a_ @ _h_ . An NHL schedule can then be seen as a set of game-day assignments for the corresponding season. 

We enumerate and define below the constraints for the NHL scheduling problem that have been taken into account in this study. For each constraint, we also specify how the corresponding violations are being counted for our evaluations of NHL schedules. 

In addition to the (hard) constraint that a team can never be scheduled to play more than one game a day, which we refer to as C0, and also to the (hard) constraint that the 

35 

games must be scheduled exclusively on playable dates provided by the NHL, we consider the following nine constraints, and respective violation counting, for the NHL scheduling problem: 

- C1 _Arena availability for home games_ A team should play at home only when its arena is available. Here, we count one violation for each game _a_ @ _h_ scheduled to a day _d_ that is not an arena date provided by the home team, _h_ . 

- C2 _Number of games over three days_ A team should not play more than two games during any three consecutive days. Here, we count one violation for each sequence of three consecutive days, from a day _d_ to day _d_ + 2, during which a team _t_ is scheduled to play three games. 

- C3 _Number of games over five days_ A team should not play more than three games during any five consecutive days. Here, we count one violation for each sequence of five consecutive days, from a day _d_ to day _d_ + 4, during which a team _t_ is scheduled to play more than three games. 

- C4 _Daily travel distance_ A team should not travel more than 900 miles to play games on two consecutive days if those games are to be held in the arenas of two teams from different divisions. Here, we count one violation for each time a team _t_ is scheduled to play on two consecutive days, _d_ and _d_ + 1, and the respective games are to be held in two arenas (possibly including the arena of _t_ ) that are both more than 900 miles away from each other and belong to teams from different divisions. 

- C5 _Number of games in a week_ A team should play at least two games in each week, from Sunday to Saturday. Here, we count one violation for each team _t_ and each week _w_ where _t_ is not scheduled to play at least two games within the period from Sunday to Saturday. Weeks that involve Christmas and NHL All-Star game, or Olympic Games, are not counted. 

- C6 _Number of days between revisits_ Games should be at least 14 and 30 days apart when related to the same intradivisional and interdivisional matches, respectively. Here, we count one violation for each pair of days _d_ 1 and _d_ 2 assigned to a match _a_ @ _h_ (same ordered _away-home_ pair of teams), such that the condition _d_ 2 _− d_ 1 _< δ_ holds for _δ_ = 14 if _a_ and _h_ belong to the same division, or for _δ_ = 30 if _a_ and _h_ belong to different divisions. 

- C7 _Number of games in a trip_ A team should play no more than seven games during a trip. Here, we count one violation for each team _t_ and a corresponding trip _r_ ( _t_ ) during which _t_ is scheduled to play more than seven games. 

36 

- C8 _Duration of a trip_ A trip should last no more than 14 days. Here, we count one violation for each team _t_ and a corresponding multi-game trip _r_ ( _t_ ) during which _t_ is scheduled to play a first away game on day _d_<sup>_r_</sup> 1<sup>and a last away game on day</sup><sup>_dr_</sup> 2<sup>,and the condition</sup> _d_<sup>_r_</sup> 2<sup>_−dr_</sup> 1<sup>_≥_14holds.</sup> 

- C9 _Number of days between two trips_ Two consecutive trips for a team should be separated by at least three days between them if that team travels more than 900 miles both from the last game in the first trip to home, and from home to the first game in the second trip; otherwise, the two trips should be separated by at least two days. Here, we count one violation for each team _t_ and two corresponding consecutive trips, _r_ 1( _t_ ) and _r_ 2( _t_ ), where the last game in _r_ 1( _t_ ) is scheduled to be played on day _d_<sup>_r_</sup> 1<sup>inthearenaofteam</sup> _h_ 1, and the first game in _r_ 2( _t_ ) is scheduled to be played on day _d_<sup>_r_</sup> 2<sup>inthearenaofteam</sup> _h_ 2, such that _d_<sup>_r_</sup> 2<sup>_−dr_</sup> 1<sup>_≤_3holdsifthedistancebetween</sup><sup>_h_1and</sup><sup>_h_2isfartherthan900</sup> miles, or _d_<sup>_r_</sup> 2<sup>_−dr_</sup> 1<sup>_≤_2holds,otherwise.</sup> 

The number of constraint violations in the last five official NHL schedules are shown in Table 3.2. Overall, these numbers seem to indicate that at least some of the constraints listed above (especially C4, C5, and C6) might not be as relevant today as they had been in the past. On the other hand, these constraints are highly related to two common concerns in the sports scheduling literature, namely traveling distances and flow of the games (in an ideal situation, the games would be evenly spread throughout the whole season). 

In accordance with Ferland and Fleurent (1991), we refer to a game to be scheduled (while not scheduled to any day), as a _free_ game. A schedule where an NHL playable day has been assigned to every free game is referred to as a _complete schedule_ . The basic problem of this thesis can then be stated as follows. Given the free games for an NHL regular season, the corresponding set _D_ of playable dates provided by the NHL, and the set _Dt ⊆ D_ of arena dates for each NHL team _t_ , the NHL scheduling problem in this thesis consists in scheduling every free game _a_ @ _h_ to a playable date _d ∈ D_ , as to build a complete schedule having the minimum number of violations (if any) of the constraints from C1 to C9. 

# **3.3.1 The NHL scheduling problem in the literature** 

The constraints we enumerated in the preceding subsection are essentially the same as those that have been considered in the academic literature on the NHL scheduling problem. In particular, only the constraints C7, C8 and C9 are not taken into account in the mathematical model introduced by Fleurent (1987). That model deals with all the constraints from C0 to C6 as _hard_ constraints, which cannot be violated, except for C3, which is treated as a _soft_ constraint and for which violations are allowed but penalized in the objective function. The general description of the NHL scheduling problem in Fleurent (1987), however, does 

37 

include the constraint C7 and also a constraint enforcing a team to be scheduled to play at home on its first arena date after a trip of more than seven days. Those two constraints are, in fact, characterized as hard constraints in that description of the problem. Apart from the violations of C3, the objective function of the mathematical model referred above incorporates, in a weighted sum, both the number of games to be played on weekdays (from Monday to Thursday) and the total distance to be travelled by all teams of the league. In this thesis, among the specified constraints, we denote the set of hard constraints considered in the model by Fleurent (1987) as 



With regard to the work by Costa (1995), the constraints from C0 to C3 are treated as soft constraints, and the ones from C4 to C8 are considered hard constraints, except for C5, which is not mentioned by the author. In particular, during the solution process, violations for the constraint C0 are actually allowed only for the cases where either two away games or two home games are scheduled on the same day for a team. However, at the end of Costa’s evolutionary approach, which holds a _population_ of schedules in each iteration, any final solution violating C0 is rejected. 

As noticed in the preceding chapter, Craig _et al_ . (2009) do not mention other constraints than C0. However, they penalize any road trip made up of more than three games, and both C7 and C8 could then be interpreted as soft constraints in their work. 

Table 3.2 _Constraint violations in official NHL schedules_ For each constraint ( _ctr_ ), number of violations in the actual NHL schedules of the last seasons. 

|_ctr_|2009-10|2010-11|2011-12|2012-13|2013-14|
|---|---|---|---|---|---|
|C1|0|0|0|0|0|
|C2|0|0|0|0|0|
|C3|3|3|0|0|0|
|C4|12|14|9|10|10|
|C5|6|16|19|3|8|
|C6|87|66|75|88|33|
|C7|1|0|1|1|1|
|C8|1|0|1|2|0|
|C9|0|0|0|0|0|
|Total|110|99|105|104|52|



38 

On the whole, Table 3.3 summarises the constraints that had (and that had not) been considered in the literature. Although none of those references has explicitly defined the constraint C9, it has been motivated by our attempt to mimic a more realistic representation of consecutive road trips in NHL schedules. In fact, our definition of _trip_ introduced in the preceding subsection is based on the approach for generating road trips that was used in Ferland and Fleurent (1991). Specifically, that approach does not allow a team to have byes made up of three or more consecutive days in the course of a single road trip. With regard to Costa (1995), this requirement was relaxed by one day, as he tries to avoid byes of four or more consecutive days during a road trip. 

Table 3.3 _Constraints of the NHL scheduling problem in the literature_ Comparison of the constraints ( _ctr_ ) in this thesis (C0 _,_ C1 _, . . . ,_ C9) with those that are, or that are not ( _×_ ), taken into account in Craig _et al_ . (2009) (CWB-2009), in Costa (1995) (C-1995), in Ferland and Fleurent (1991) (FF-1991), and in Fleurent (1987) (F-1987). Some of the constraints have been treated as _hard_ constraints, and others as _soft_ constraints. In particular, with regard to the ( _soft*_ ) constraint C0 in C-1995, only violations where either two away games or two home games are scheduled to the same day for a team are allowed during the solution process; but as well as in CWB-2009, any final solution that violates C0 is rejected. 

|_ctr_|F-1987|FF-1991|C-1995|CWB-2009|
|---|---|---|---|---|
|C0|_hard_|_hard_|_soft*_|_soft*_|
|C1|_hard_|_hard_|_soft_|_×_|
|C2|_hard_|_hard_|_soft_|_×_|
|C3|_soft_|_soft_|_soft_|_×_|
|C4|_hard_|_hard_|_hard_|_×_|
|C5|_hard_|_hard_|_×_|_×_|
|C6|_hard_|_hard_|_hard_|_×_|
|C7|_×_|_×_|_hard_|_soft_|
|C8|_×_|_×_|_hard_|_soft_|
|C9|_×_|_×_|_×_|_×_|



The surprisingly high number of violations for the constraints C4 and C6 in the most recent NHL schedules (see Table 3.2) does not support, nowadays, the assumption that these constraints should be considered as hard constraints with the same parameter values (900 miles in the description of C4, and 14 and 30 days in the description of C6) that were used by Ferland and Fleurent (1991) and by Costa (1995) in the 1990s. 

In the next chapter, we first formulate the NHL scheduling problem as an integer linear programming and then, we present some computational results obtained from a commercial state-of-the-art solver on different configurations of hard and soft constraints. 

39 

# **CHAPTER 4** 

# **MATHEMATICAL MODELING** 

In this chapter, we propose the first integer linear programming model for the NHL scheduling problem which takes into account all its constraints considered in the literature, in addition to the minimization of total travel distance for the league. Some computational results obtained from a commercial state-of-the-art solver on several variants of the model are also reported. 

Section 4.1 specifies the data of the problem, the parameters for the model, and the mathematical formulations that cover all the constraints enumerated in the previous chapter. The formulation for minimizing total travel distance will be presented in Section 4.2. 

# **4.1 Basic formulation** 

In this section, we present a formulation for each constraint of the problem, which leads to a feasibility model with _O_ ( _n_<sup>2</sup> _m_ ) variables for _n_ teams and _m_ days. 

# **4.1.1 Data of the problem** 

The data of the problem are the following: 

- _n_ : number of teams in the league; 

- _m_ : number of calendar days in the regular season period; 

- _T_ = _{_ 1 _,_ 2 _, . . . , n}_ : set of teams in the league; 

- _D_ = _{_ 1 _,_ 2 _, . . . , m}_ : set of calendar days in the regular season period; 

- — _Dt_ = _{d_<sup>_t_</sup> 1<sup>_, dt_</sup> 2<sup>_, . . . , dt_</sup> _mt_<sup>_}_:setofarena-availabledaysforeachteam</sup><sup>_t ∈T_;</sup> 

- _Ga,h_ : number of games (visits) for each match _a@ h_ , where _a, h ∈ T_ ; and 

- _dist_ ( _t_<sup>_′_</sup> _, t_<sup>_′′_</sup> ): distance between the arenas of teams _t_<sup>_′_</sup> and _t_<sup>_′′_</sup> , for all _t_<sup>_′_</sup> _, t_<sup>_′′_</sup> _∈ T_ . 

# **4.1.2 Parameters of the model** 

Based on the description of the constraints of the problem in the preceding chapter, the following are the parameters for the model: 

- _δa,h_<sup>_V V_:minimumnumberofdaysbetween(re)visitsforthematch</sup><sup>_a@ h_,where</sup><sup>_a, h ∈T_;</sup> 

- _ξ_<sup>_DD_</sup> : maximum daily travel distance for a team; 

40 

- _ξ_<sup>_AB_</sup> : maximum number of consecutive “away byes” (during a same trip); 

- _ξ_<sup>_AG_</sup> : maximum number of away games in any road trip for a team; 

- _ξ_<sup>_AD_</sup> : maximum duration, in number of days, of any road trip for a team; 

- _ξ_<sup>_WG_</sup> : minimum number of games per week for a team; 

- _δ_ far<sup>_RR_:minimumnumberofdaysbetweentwoconsecutiveroadtripsforateamthathas</sup> to travel long distances (more than _ξ_<sup>_DD_</sup> ) both back home from the last game in the first trip and from home to the first game in the second trip; 

- _δ_ near<sup>_RR_:minimumnumberofdaysbetweentworoadtripsforateam;thathastotravel</sup> short distances (no more than _ξ_<sup>_DD_</sup> ) both back home from the last game in the first trip and from home to the first game in the second trip. 

In particular, _ξ_<sup>_DD_</sup> , on the maximum daily distance, can be seen as a threshold beyond which a distance is considered “too far” for a team to travel in order to play back-to-back games. 

# **4.1.3 Variables** 

For any two teams _a, h ∈ T_ and any day _d ∈ D_ , let _x_<sup>_A_</sup> _a,d,h_<sup>beabinaryvariabledefinedas</sup> 



In addition, for any team _t ∈ T_ and any day _d ∈ D_ , let _x_<sup>_H_</sup> _t,d_<sup>,</sup><sup>_xB_</sup> _t,d_<sup>,and</sup><sup>_xL_</sup> _t,d_<sup>bebinary</sup> variables as 







In the descriptions that follow, we might refer to _x_<sup>_A_</sup> _a,d,h_<sup>,</sup><sup>_xH_</sup> _t,d_<sup>,</sup><sup>_xB_</sup> _t,d_<sup>,and</sup><sup>_xL_</sup> _t,d_<sup>as</sup><sup>_away_,</sup><sup>_home_,</sup> _bye_ , and _long-bye_ variables, respectively. 

41 

# **4.1.4 Constraints** 

We now present the formulation of each constraint of the problem with a short informal description for each of them to (hopefully) make the model easier to understand. 

**Restricting a team to play at most one game per day** On any day _d ∈ D_ , exactly one of the following cases must happen for any team _t ∈ T_ : 

1) _t_ plays an away game (at the arena of a single opponent); 

2) _t_ plays a home game; 

- 3) _t_ does not play any game. 

In our model, this is represented by the following constraints: 



**Linking host and visiting team** If a team _t ∈ T_ plays home on a day _d ∈ D_ then some other team _a ∈ T_ must be visiting _t_ on day _d_ . This is represented by the following constraints: 



**Fixing non-meaningful “self-visit” variables** For any team _t ∈ T_ and any day _d ∈ D_ , the variable _x_<sup>_A_</sup> _t,d,t_<sup>issetto0.</sup> 



**Linking variables** _x_<sup>_B_</sup> _t,d_<sup>**and**</sup><sup>_xL_</sup> _t,d_ For any team _t ∈ T_ and any day _d ∈ D_ , such that _d <_ = _m − ξ_<sup>_AB_</sup> , the variable _x_<sup>_L_</sup> _t,d_<sup>shouldbesetto1ifandonlyif</sup><sup>_t_doesnotplayfromday</sup><sup>_d_</sup> to day _d_ + _ξ_<sup>_AB_</sup> , which can be written as the logical connective 



The idea is that _x_<sup>_L_</sup> _t,d_<sup>= 1indicatesthat day</sup><sup>_d_isnot within a road trip period for team</sup><sup>_t_and,</sup> in particular, if _t_ plays away on the previous day, _d −_ 1, then it must return home before playing the next game (even when this is also an away game). In terms of linear inequalities, 

42 

we add then the following constraints to the model: 



**Setting the number of games for each pair of teams** For each two teams _a ∈ T_ and _h ∈ T_ , exactly a given number _Ga,h_ of games must be scheduled for the match a _@_ h: 



**Constraint C** 1 ( _arena availability for home games_ ) Every home variable for a non arenaavailable day of a team is fixed to value 0: 



**Constraint C** 2 ( _maximum number of games over three days_ ) Every sequence of three days for a team is forced to have at least one bye: 



**Constraint C** 3 ( _maximum number of games over five days_ ) Every sequence of five days for a team is forced to have at least two byes: 



43 

**Constraint C** 4 ( _maximum daily travel distance_ ) For any two consecutive days, at least one of every two variables corresponding to two distant arenas is forced to take value 0: 



**Constraint C** 5 ( _minimum number of games in a week_ ) Regarding every week of the season, say _w_ , at least _ξ_<sup>_WG_</sup> bye variables corresponding to the days, _d_<sup>1</sup> _w_<sup>_, d_2</sup> _w_<sup>_, . . . , d_7</sup> _w_<sup>_,_ofthatweekare</sup> forced to take value 0: 



**Constraint C** 6 ( _minimum number of days between revisits_ ) Regarding every match _a@ h_ , for each interval of 1 + _δa,h_<sup>_V V_days,no more than one away variable is allowed to take value 1:</sup> 



**Constraint C** 7 ( _maximum number of games in a trip_ ) The idea behind the formulation of this constraint is the following. Consider at first the definition of road trip from the previous chapter (p. 34), which allows no more than two byes between two consecutive games during the same trip (i.e., _ξ_<sup>_AB_</sup> = 2), and consider also that a trip must have no more than seven games (i.e., _ξ_<sup>_AG_</sup> = 7). In this case, any trip that violates constraint C7 has at least eight games. And any trip with eight games lasts between eight days (when there is one game for each day) and 22 days (when there is one game for each three, _ξ_<sup>_AB_</sup> + 1, consecutive days). Therefore, to prevent trips from having eight or more games, every sequence of _ℓ_ days, with _ℓ ∈{_ 8 _,_ 9 _, . . . ,_ 22 _}_ , must have at least _ℓ −_ 7 byes or at least one“trip breaker”(a home game or a bye lasting more than two days), which can be expressed by the following linear inequalities: 



For the general case, given the parameters _ξ_<sup>_AG_</sup> and _ξ_<sup>_AB_</sup> , every sequence of _ℓ_ days for a team, with _ℓ ∈{_ 1 + _ξ_<sup>_AG_</sup> _, . . . ,_ 1 + _ξ_<sup>_AG_</sup> _·_ ( _ξ_<sup>_AB_</sup> + 1) _}_ , must have at least _ℓ − ξ_<sup>_AG_</sup> byes or at least 

44 

one “trip breaker” (a home game or a bye longer than _ξ_<sup>_AB_</sup> days): 



**Constraint C** 8 ( _maximum number of days in a trip_ ) The idea on the formulation of this constraint is similar to the previous one, on C7, as we look at the shortest sequences of days that would potentially violates the constraint C8. At first, we describe the formulation for the particular case from the previous chapter (p. 34), where a trip should last no more than 14 days ( _ξ_<sup>_AD_</sup> = 14) and away byes should last no more than two days ( _ξ_<sup>_AB_</sup> = 2). Regarding any given team, we impose here that if a team _t_ has an away game on day _d_ (i.e., _x_<sup>_H_</sup> _t,d_<sup>+</sup><sup>_xB_</sup> _t,d_<sup>= 0)</sup> and another away game on day _d_ + 14 (i.e., _x_<sup>_H_</sup> _t,d_ +14<sup>+</sup><sup>_xB_</sup> _t,d_ +14<sup>=0)thenatleastone “trip</sup> breaker” (a home game or a bye lasting more than two days) must exist between those two away games. Similar restriction is imposed on days _d_ and _d_ + 15, and also on days _d_ and _d_ + 16. We point out that, because two games in the same trip are never separated by more than two days, such restrictions on periods of 15, 16, and 17 days are enough to cover any trip that would potentially last more than 14 days (and then violates C8). Hence, if a team has two away games separated by _ℓ −_ 2 days, with _ℓ ∈{_ 15 _,_ 16 _,_ 17 _}_ , the following linear inequalities must hold: 



For the general case, given the parameters _ξ_<sup>_AD_</sup> and _ξ_<sup>_AB_</sup> , if a team has away games on days _d_ and _d_ + _ℓ −_ 1, with _ℓ ∈{ξ_<sup>_AD_</sup> +1 _, . . . , ξ_<sup>_AD_</sup> + _ξ_<sup>_AB_</sup> +1 _}_ , then at least one“trip breaker”(a non-zero home variable or a non-zero long-bye variable) must exist between those two away games: 



**Constraint C** 9 ( _minimum number of days between two trips_ ) The basic idea on the formulation of this constraint is to look at each short period of days that would potentially violate constraint C9 for a team and specify some inequalities preventing such violations from 

45 

actually happening. In particular, given a traveling team _t_ and the set _Ft_ of all its opponents located far from its own home arena, we look at each period of less than _δ_ far<sup>_RR_days,sayfrom</sup> day _d_ to day _d_ + _q_ , with _q ∈{_ 1 _, . . . , δ_ far<sup>_RR−_1</sup><sup>_}_,andwhenever</sup><sup>_t_hasnoawaygamesbutone</sup> “trip breaker” (a home game or a long bye) during those _q_ days, we impose that _t_ is not scheduled to play away on both day _d −_ 1 and day _d_ + _q_ + 1 against its opponents in _Ft_ . Obviously, the idea is similar when considering only the opponents located close to the arena of the traveling team under consideration. 

As an example, considerer the description of C9 in the previous chapter (p. 36), where we have _δ_ far<sup>_RR_=3and</sup><sup>_δ_</sup> near<sup>_RR_=2.Becauseawaybyeslastnomorethantwodays(</sup><sup>_ξAB_=2),the</sup> formulation of C9 comes down to only the following two cases. 

— Preventing a team of having away games on days _d_ and _d_ + 2 when it has a home game on day _d_ + 1: 



for each _t ∈ T_ and each _d ∈ D_ with _d < m −_ 2 _._ 

— Preventing a team of having away games on days _d_ and _d_ + 3 when it has, in total, at least one home game on days _d_ + 1 and _d_ + 2: 



for each _t ∈ T_ and each _d ∈ D_ with _d < m −_ 3 _,_ where _Ft_ = _{h ∈ T_ : _dist_ ( _h, t_ ) _>_ 900 _}._ 

For the general case, regarding a traveling team _t ∈ T_ , any two away games _t_ @ _h_<sup>_′_</sup> and _t_ @ _h_<sup>_′′_</sup> that are respectively the last game and the first game of two consecutive road trips for _t_ must be scheduled at least _δ_ far<sup>_RR_daysapartfromeachotherifboththedistancesbetween</sup><sup>_h′_</sup> and _t_ , and between _t_ and _h_<sup>_′′_</sup> , are _far_ (more than _ξ_<sup>_DD_</sup> miles), or at least _δ_ near<sup>_RR_daysapartfrom</sup> each other, otherwise. In particular, if the arenas of both _h_<sup>_′_</sup> and _h_<sup>_′′_</sup> are _far_ from the arena of _t_ , we impose then the following constraints: 



46 

Similarly, if the arena of either _h_<sup>_′_</sup> or _h_<sup>_′′_</sup> is _close_ to the arena of _t_ , we impose then the following constraints: 



and 





# **4.2 Formulation for minimizing total travel distance** 

In this section, we present a formulation that involves the minimization of total travel distance, which, compared to the basic formulation from the preceding section, results in a much higher number of variables and constraints. In particular, the resulting model has _O_ ( _n_<sup>3</sup> _m_ ) variables for _n_ teams and _m_ days, which is in line with other sports scheduling formulations in the literature (Trick, 2005; Ribeiro, 2012). 

The formulation introduced in the preceding section is essentially based on the _place_ that every team must be on each day of the season. In order to solve the NHL scheduling problem with minimization of total travel distance, we add then to the basic formulation new variables that, regarding every team, account for the sequence of _moves_ from one place to another. 

In fact, the new variables can be described, for each _ℓ ∈{_ 1 _,_ 2 _, . . . , ξ_<sup>_AB_</sup> + 1 _}_ , as follows: 



for any teams _t, h_<sup>_′_</sup> _, h_<sup>_′′_</sup> _∈ T_ , and any day _d ∈ D_ such that _d ≤ m − ℓ_ . In particular, indices _h_<sup>_′_</sup> and _h_<sup>_′′_</sup> can both refer to team _t_ itself. 

Generally speaking, for any _ℓ ∈{_ 1 _,_ 2 _, . . . , ξ_<sup>_AB_</sup> _}_ , having _yt,d,h_<sup>_ℓ′_</sup> _,h_<sup>_′′_= 1indicatesthat</sup><sup>_t_plays</sup> at the arena of _h_<sup>_′_</sup> on day _d_ and then plays at the arena of _h_<sup>_′′_</sup> on day _d_ + _ℓ_ . However, in 

47 

addition to that case, if _ℓ_ = _ξ_<sup>_AB_</sup> + 1 then having _yt,d,h_<sup>_ℓ′_</sup> _,h_<sup>_′′_= 1mightalsoindicatethateither</sup> _t_ plays at the arena of _h_<sup>_′_</sup> on day _d_ and then has a forced home bye on day _d_ + _ℓ_ (team _t_ must return home due a long-bye period), or _t_ has a forced home bye on day _d_ and then plays at _h_<sup>_′′_</sup> on day _d_ + _ℓ_ (team _t_ leaves home after a long-bye period). 

These new variables are linked to those in the basic formulation by mean of the following constraints, which are logically grouped for easy understanding. 

— two consecutive away games: 



— home game and then away game: 



— away game and then home game: 



— away game and then long-bye period (forced home bye): 



— long-bye period (forced home bye) and then away game: 



48 

— first game (away) within the first _ξ_<sup>_AB_</sup> + 1 days of the season: 



— last game (away) within the last _ξ_<sup>_AB_</sup> + 1 days of the season: 



Hence, in particular, the trip that a team travels from home for an away game in the first _ξ_<sup>_AB_</sup> +1 days of the season is taken into account in (4.28), and the trip that a team travels for an away game in the last _ξ_<sup>_AB_</sup> + 1 days of the season to home is taken into account in (4.29). 

Finally, with the _y_ variables, minimizing the total travel distance comes down to the following straightforward linear objective function: 



# **4.3 Computational experiments** 

In this section, we report several results from an implementation of the preceding mathematical model in a commercial state-of-the-art solver, namely the IBM ILOG CPLEX<sup>®</sup> 12.6. 

In fact, all the models resulting from the relaxation of any of the constraints described in the preceding section have been implemented in C++ and use the Concert Technology C++ API of CPLEX<sup>®</sup> . Here, by “relaxation” we mean either the omission of constraints or the addition of artificial variables to the constraints and corresponding penalty in the objective function. It was run under Linux on a 3.07GHz Intel(R) Xeon(R) X5675 processor (only one processor was used) with 94.5G of RAM. For each experiment, the maximum time which CPLEX<sup>®</sup> was allowed to run had been set (through the parameter `IloCplex::TiLim` ) to 48 hours, and the number of threads had also been limit to a single one (through the parameter `IloCplex::Threads` ). Test were performed on different values for the MIP emphasis parameter ( `MIPEmphasis` ), but because it had no noticeable impact in the quality of the overall results, we limit this reporting to those obtained with this parameter set as _balanced_ , which orients the search for a solution toward both optimality and integer feasibility. 

49 

# **4.3.1 Models and parameters** 

The results reported in this chapter are limited to four models and two settings of parameters. Furthermore, every combination model-and-parameters was tested both with and without minimization of total travel distance. We use the term _MinDist_ to denote the presence of minimization of distance in the model at hand. Each model refers to only a particular subset of constraints being relaxed, but always penalized in the objective function. And each setting of parameters fix different values for the revisit-gap parameters in the models. 

To be more precise, the models we refer to are characterized by the following description, which is summarized in Table 4.1. 

- **Model I** This model relaxes only the constraint C5 on the minimum number of games to be played by a team during every week of the season. 

- **Model II** In addition to C5, this model relaxes the constraints C7, C8, C9 on the maximum number of games per trip, on the maximum duration for a trip, and on the minimum number of days between two consecutive trips for a team. 

- **Model III** In addition to the previous relaxations, on C5, C7, C8, and C9, this model relaxes the constraints C4 and C6, on the daily travel distance and on the minimum number of days between two games involving the same pair of teams in the same place (the revisit gap). 

- **Model IV** This model relaxes all the nine constraints, from C1 to C9 in our descriptions of the problem. 

Table 4.1 _Models for the computational experiments with CPLEX_<sup>®</sup> Characterization of the models with regard to each constraint of the problem. 

|Constraint|Model I|Model II|Model III|Model IV|
|---|---|---|---|---|
|C1 : `arenaAvailability`|_hard_|_hard_|_hard_|_soft_|
|C2 : `max2GamesOver3Days`|_hard_|_hard_|_hard_|_soft_|
|C3 : `max3GamesOver5Days`|_hard_|_hard_|_hard_|_soft_|
|C4 : `maxDistancePerDay`|_hard_|_hard_|_soft_|_soft_|
|C5 : `minNGamesPerWeek`|_soft_|_soft_|_soft_|_soft_|
|C6 : `minNDaysBetweenRevisits`|_hard_|_hard_|_soft_|_soft_|
|C7 : `maxNGamesPerTrip`|_hard_|_soft_|_soft_|_soft_|
|C8 : `maxNDaysPerTrip`|_hard_|_soft_|_soft_|_soft_|
|C9 : `minNDaysBetweenTrips`|_hard_|_soft_|_soft_|_soft_|



In all these models, the objective function is to be minimized, as it is defined by a weighted 

50 

summation of variables representing the violation of the relaxed constraints, in addition to the total distance (when _MinDist_ is considered in the model). For the computational experiments, we have set the weight (penalty parameter) _wi_ for the violation of a constraint C _i_ to the following values: _w_ 1 = 10 000, _w_ 2 = 1 000, _w_ 3 = 100, _w_ 5 = 1, and _wi_ = 10 for each constraint C _i_ with _i ∈{_ 4 _,_ 6 _,_ 7 _,_ 8 _,_ 9 _}_ . 

As for the parameters, we report results for two settings, _LGap_ and _SGap_ , which differ only on the values for the revisit gaps. Indeed, both settings use the following values: _ξ_<sup>_DD_</sup> = 900, _ξ_<sup>_AB_</sup> = 2, _ξ_<sup>_AG_</sup> = 7, _ξ_<sup>_AD_</sup> = 14, _ξ_<sup>_WG_</sup> = 2, _δ_ far<sup>_RR_= 3,and</sup><sup>_δ_</sup> near<sup>_RR_= 2;andtheydifferontherevisit</sup> gaps ( _δa,h_<sup>_V V_)asfollows:</sup> 

- **Long revisit gaps** ( _LGap_ ) The minimum number of days between two games (revisits) for each match is set to 13 and to 29 for intra-division and for interdivisional revisits, respectively, as in Fleurent (1987). 

- **Short revisit gaps** ( _SGap_ ) The minimum number of days between two games (revisits) for each match is set to only 5 and to only 11 for intra-division and for interdivisional revisits, respectively. 

# **4.3.2 Problem instances** 

The data for the NHL scheduling problem are made up by specifying _1)_ the arrangement of the League (comprising the distance between each pair of arenas), _2)_ the structure of the regular season (with all the games that must be scheduled), and _3)_ the arena dates for each team. As we have already stated, changes in the structures of both the League and its regular season usually occur (when they do) on a very small scale from one year to the next. On the other hand, the availability of arenas is expected to be quite irregular over different seasons. To our knowledge, no such data are openly available, even for the past years. We have decided, therefore, to create our own test problems, which we categorize into the three following classes. 

- **Entire-league instances** Instances in this class were generated by keeping all home dates in an actual NHL schedule and adding to it some _extra arena-available dates_ . Such dates were randomly chosen from the corresponding regular-season period. We denote these `-` 

- instances by `NHL` _α βγ_ , where _α_ refers to the starting year of the concerning season; _β_ is the number of extra arena dates per team; and _γ_ is a letter to identify different instances for the same year ( _α_ ) and number of extra dates ( _β_ ). For example, `NHL13-4a` stands for a particular instance identified by `a` and having 4 additional home dates per team with regard to the NHL schedule of the 2013-14 regular season. Given any official NHL schedule, the only two parameters in our instance generator for this class are the 

51 

Table 4.2 _Instances for the computational experiments_ Information about some of the problem instances used in this thesis: numbers of conferences ( _#confs_ ), divisions ( _#divs_ ), teams ( _#teams_ ), games in a complete schedule ( _#games_ ), games per team ( _#tgames_ ), home games per team ( _#hgames_ ), and extra arena-available dates per team ( _#edays_ ). 

|Instance|_#confs_<br>|_#divs_|_#teams_|_#games_|_#tgames_|_#hgames_|_#edays_|
|---|---|---|---|---|---|---|---|
|**Entire-league **|**instances**|||||||
|`NHL09-00a`|2|6|30|1230|82|41|0|
|`NHL10-00a`|2|6|30|1230|82|41|0|
|`NHL11-00a`|2|6|30|1230|82|41|0|
|`NHL13-00a`|2|4|30|1230|82|41|0|
|`NHL09-04a`|2|6|30|1230|82|41|4|
|`NHL10-04a`|2|6|30|1230|82|41|4|
|`NHL11-04a`|2|6|30|1230|82|41|4|
|`NHL13-04a`|2|4|30|1230|82|41|4|
|`NHL09-08a`|2|6|30|1230|82|41|8|
|`NHL10-08a`|2|6|30|1230|82|41|8|
|`NHL11-08a`|2|6|30|1230|82|41|8|
|`NHL13-08a`|2|4|30|1230|82|41|8|
|**Partial-league **|**instances**|||||||
|`NHL11-1208-76`|1|2|8|304|76|38|3|
|`NHL13-1208-76`|1|2|8|304|76|38|3|
|`NHL11-1208-74`|1|2|8|296|74|37|4|
|`NHL13-1208-74`|1|2|8|296|74|37|4|
|`NHL11-1208-72`|1|2|8|288|72|36|5|
|`NHL11-1210-74`|1|2|10|370|74|37|4|
|`NHL13-1212-76`|1|2|12|456|76|38|3|
|`NHL11-1312-78`|1|3|12|468|78|39|2|
|`NHL11-1312-72`|1|3|12|432|72|36|5|
|`NHL13-1216-74`|1|2|16|592|74|37|4|
|`NHL13-2416-78`|2|4|16|624|78|39|2|
|`NHL13-2416-74`|2|4|16|592|74|37|4|
|`NHL11-2624-74`|2|6|24|888|74|37|4|
|**The 2012 inst**|**ances**|||||||
|`NHL12-1315a`|1|3|15|360|48|24|0|
|`NHL12-1315b`|1|3|15|360|48|24|0|



number and the“type”of extra dates per team. The _type_ parameter indicates the dates within the regular-season period that are the candidates to become extra dates for the instance being generated. In fact, this parameter specifies which of the following two 

52 

strategies is applied: _(1)_ the extra dates are chosen, for any team _t_ , only among those days when _t_ had not been scheduled to play (neither home nor away) in the actual NHL schedule; or _(2)_ the extra dates are selected among any non-home dates (even those when _t_ had been scheduled to play away) in the actual NHL schedule. This is based upon the rationale that finding a solution for the instances in which all the new dates, regarding the actual NHL schedule, are indeed extra dates may be easier than scheduling games for instances in which some NHL away dates had also been selected as “extra”dates. Evidences for such premise is to be gathered throughout the experiments reported in this thesis. We refer to those two types of dates as _true-extra_ dates and _pseudo-extra_ dates, respectively. 

- **Partial-league instances** Instances in this class are formed by only some randomly chosen subset of the teams from the League. The home dates in the corresponding actual NHL schedule for the chosen teams are taken as arena-available dates in these instances. But the numbers of games to be scheduled are changed. They are proportionally increased for each pair of teams until every team would have to play in this “partial league” almost the same number of games it plays in the actual schedule. Obviously, even with such small artificial leagues, the idea is to mimic the unavailability of arena dates from the real situation, where a limited number of dates are reported to be available for the home games of many teams. 

- **The 2012 instances** There are only two instances in this class, named `NHL12-1315a` (for the Eastern Conference schedule) and `NHL12-1315b` (for the Western Conference schedule), each one made up from the 15 teams (and their home dates) on the NHL 2012-13 season for a particular conference. The actual schedule for that season, during which only 720 games were played, is in fact formed by two independent schedules, one for each conference. In particular, no game was played between a team from the Eastern Conference and another from the Western Conference during that shortened season due to a labour dispute that started in 2012 and lasted for a few months. 

- Table 4.2 outline some information about the instances of these three classes that we use 

- for the computational experiments reported in this chapter. 

We must remark that some instances also provide a few pre-scheduled games if the corresponding actual NHL schedule includes some special games that are not supposed to be rescheduled. Examples of such games are Premi`ere games (which are played in Europe), Winter Classic games (which are usually fixed in the middle of the season), Stadium Series games, and Heritage Classic games. Furthermore, only days that in the corresponding actual schedule have at least one scheduled game are considered as “playable days” in our instances. In particular, our implementations does not schedule games to special days that involves, for 

53 

example, Christmas holidays, All Star game week, and Olympic break. In addition, for a team that, in the beginning of the season, plays a Premi`ere game, no game is scheduled in a period of at least four days after the last of those games (in Europe). 

The results are grouped by class of instances throughout the following subsections. We start reporting on the partial-league instances, which are expected to be somewhat less difficult to solve than the entire-league instances. 

# **4.3.3 Results for the** **_partial-league_ instances** 

Results for the partial-league instances are presented in tables 4.3 and 4.4 respectively for the cases with and without minimization of total travel distance. These tables show the running times and output solution status from CPLEX<sup>®</sup> on the four models (different relaxed constraints) with the two revisit-gap configurations we mentioned earlier. For a model in which a particular constraint has been relaxed, the reference to the constraint, C _i_ , is enclosed between brackets, [C _i_ ], on the top of the tables. The results are separated into two groups: one for each configuration of the revisit-gap parameters, which are either long ( _LGap_ ) or short ( _SGap_ ). The solution status ( _Sol_ ) indicates whether ( _feas_ ) or not (–) a feasible solution, not necessarily the optimal ( **opt** ), has been found within the time limit of 48 hours. 

An inspection of the solution statuses in Table 4.3 indicates that, for large revisit gaps, 73% of the instances have been solved either to proved optimality (42%) or at least to feasibility (31%). That proportion is much larger for short revisit gaps (96%), where almost all instances were solved to optimality. Even though the short revisit gaps were intended to facilitate the search for feasible solutions with regard to the C6 constraints, the results on short revisit gaps are quite remarkable, particularly for instances with 16 and 24 teams, which have no more than four extra arena dates per team. 

As for the experiments involving the minimization of total travel distance ( _MinDist_ ), although slightly more instances are solved to feasibility for the small than for the large revisitgap configuration, the results in Table 4.4 show that the solver is somewhat disappointing in this case. In fact, by a deeper inspection of the feasible solutions from this part of the experiments and by comparing them with the corresponding feasible solutions referred in Table 4.3, we noticed that even though the total distances have indeed decreased for most of the cases, in general it happened to the price of higher number of constraint violations. Exception to this disappointing effect did occur with Model I, where only the C5 constraints are allowed to be violated. Indeed, the total distance on every feasible solution in Table 4.4 for Model I with parameters _SGap_ + _MinDist_ happens to be between 4 and 16% lower than the distance on the corresponding (optimal) solutions without minimization of distance from Table 4.3. And this, at the price of no more than three additional violations of C5 in the 

54 

same comparison. 

Now, comparing the overall results in these two tables indicates that the models involving _MinDist_ are indeed much more difficult to be solved than their corresponding configurations without considering the total distance. In fact, solutions (not necessarily optimal) were found only for 38% of the instances when the models incorporate _MinDist_ , as opposed to more than 84% for the other case. This is somewhat in agreement with what we expected, because, in particular, the models with _MinDist_ involves a huge number of additional constraints and variables. 

In both tables, the results also suggest that shorter values for the revisit-gap parameters make the problems easier for CPLEX<sup>®</sup> to solve them. In practice, when sequentially scheduling the games, once a game for a particular match is scheduled, imposing larger revisit gaps reduces the range of remaining feasible days for other games of the same match. In a MIP solver, however, it could be expected that such reduction in the number of possible assignments would speed up the search for a solution, which does not seem to occur in the case of CPLEX<sup>®</sup> for any of our experiments in this chapter. 

We also notice that, when we compare the results on the different models, these experiments support the general idea that solving such problems becomes less difficult when more (hard) constraints are present in the model, as in general it reduces the solution space of the problem. 

# **4.3.4 Results for the** **_2012_ instances** 

The 2012 instances are especially interesting for the application of our models in this chapter, as they are entirely based in the official NHL schedule while having numbers of games and teams that, considering the results in the preceding subsection, can probably be dealt with by our C++ CPLEX<sup>®</sup> implementations. Here, we also test the models I to IV, each one with the two configurations of revisit gaps, _LGap_ and _SGap_ , with and without minimization of total distance ( _MinDist_ ). The corresponding running times and output solution status from CPLEX<sup>®</sup> are outlined in Table 4.5. 

A first look at the results in this table reveals that the Western Conference instance, `NHL12-1315b` , seems surprisingly more difficult to solve than the other one, `NHL12-1315a` , which was solved to proved optimality on all models without _MinDist_ , and at least to feasibility when total distance is to be minimized. In particular, regarding the models I and II, a feasible (optimal) solution was only found for the short revisit-gap configuration on Model II during 48 hours of search. 

To further explore these results, we now focus in the instance `NHL12-1315a` for the particular case of Model III. Table 4.6 shows the constraint violations for the corresponding found 

55 

solutions, in addition to the increase in the total travel distance regarding the actual NHL schedule. Here, we notice that no constraint is violated by the optimal solutions obtained both for the easier case of small revisit gap and for the more realistic long revisit gap. But when minimization of total distance had been incorporated in those cases, some violations did occur in the best-found solutions. As for the value of the total distance, the particular case of the large revisit gap configuration also resulted in a worse solution than in the corresponding case without _MinDist_ . This might suggest that, in general, the bigger models involving _MinDist_ would need much more than 48 hours to possibly obtain reasonable solutions with respect to the total travel distance. 

# **4.3.5 Results for the** **_entire-league_ instances** 

Different from some rather promising results obtained for the previous classes of instances, CPLEX<sup>®</sup> failed to solve (in 48 hours) almost all the instances of this more realistic class. In fact, as shown in Table 4.7, CPLEX<sup>®</sup> was only able to solve five instances of the entireleague class through the most constrained models, I and II, for the “easier” short revisit-gap configuration without minimization of distance. 

Curiously, all but one of the instances solved have no extra arena dates, which seems to suggest that, as expected, the search has been favored by the smaller search space of these cases. 

56 

Table 4.3 _Results for the partial-league instances without minimization of total travel distance_ Running times and output solution status from CPLEX<sup>®</sup> on four different models. For a model in which a particular constraint has been relaxed, the reference to the constraint, C _i_ , is enclosed between brackets, [C _i_ ], on the top of the table. The results are separated into two groups: one for each configuration of the revisit-gap parameters, which are either long ( _LGap_ ) or short ( _SGap_ ). The solution status ( _Sol_ ) indicates whether ( _feas_ ) or not (–) a feasible solution, not necessarily the optimal ( **opt** ), has been found within the time limit of 48 hours. 

||Model|I|Model I|I|Model I|II|M|odel I|V|
|---|---|---|---|---|---|---|---|---|---|
||C1<br>C2<br>C4<br>[C5]<br>C7<br>C8|C3<br>C6<br>C9|C1<br>C2<br>C4<br>[C5]<br>[C7]<br>[C8]|C3<br>C6<br>[C9]|C1<br>C2<br>[C4]<br>[C5]<br>[C7]<br>[C8]|C3<br>[C6]<br>[C9]|[C1]<br>[C4]<br>[C7]|[C2]<br>[C5]<br>[C8]|[C3]<br>[C6]<br>[C9]|
|**Param.** _LGap_||||||||||
|Instance|Time|_Sol_|Time|_Sol_|Time|_Sol_|Time||_Sol_|
|`NHL11-1208-76`|–|–|–|–|–|_feas_||–|_feas_|
|`NHL13-1208-76`|–|–|–|–|–|_feas_||–|_feas_|
|`NHL11-1208-74`|18h41m14s|**opt**|11m5s|**opt**|46h42m25s|**opt**||–|_feas_|
|`NHL13-1208-74`|15h6m0s|**opt**|–|_feas_|–|_feas_||–|_feas_|
|`NHL11-1208-72`|–|–|–|–|–|_feas_||–|_feas_|
|`NHL11-1210-74`|30m16s|**opt**|19m54s|**opt**|4h45m14s|**opt**||–|_feas_|
|`NHL13-1212-76`|15h13m55s|**opt**|1h22m46s|**opt**|–|_feas_|6h5|8m9s|**opt**|
|`NHL11-1312-78`|45h41m40s|**opt**|14h48m50s|**opt**|–|_feas_||–|–|
|`NHL11-1312-72`|46h6m36s|**opt**|1h51m32s|**opt**|44h21m34s|**opt**|18h52|m23s|**opt**|
|`NHL13-1216-74`|2h5m58s|**opt**|4h26m53s|**opt**|9h26m46s|**opt**|47h55|m22s|**opt**|
|`NHL13-2416-78`|–|–|–|–|–|_feas_||–|–|
|`NHL13-2416-74`|–|–|–|_feas_|–|_feas_||–|–|
|`NHL11-2624-74`|11h49m29s|**opt**|41h8m32s|**opt**|–|–||–|–|
|**Param.** _SGap_||||||||||
|Instance|Time|_Sol_|Time|_Sol_|Time|_Sol_|Time||_Sol_|
|`NHL11-1208-76`|1m50s|**opt**|2m13s|**opt**|8m22s|**opt**|13|m46s|**opt**|
|`NHL13-1208-76`|3m17s|**opt**|5m44s|**opt**|40m45s|**opt**|1h35|m13s|**opt**|
|`NHL11-1208-74`|1m5s|**opt**|2m58s|**opt**|7m25s|**opt**|33|m52s|**opt**|
|`NHL13-1208-74`|1m20s|**opt**|5m46s|**opt**|13m24s|**opt**|54|m25s|**opt**|
|`NHL11-1208-72`|1m42s|**opt**|4m44s|**opt**|1h2m55s|**opt**|3h4|7m9s|**opt**|
|`NHL11-1210-74`|7m20s|**opt**|8m15s|**opt**|14m22s|**opt**|2h3|m23s|**opt**|
|`NHL13-1212-76`|18m45s|**opt**|45m58s|**opt**|2h28m56s|**opt**|31h39|m27s|**opt**|
|`NHL11-1312-78`|16m3s|**opt**|41m0s|**opt**|2h16m24s|**opt**|3h27|m45s|**opt**|
|`NHL11-1312-72`|18m0s|**opt**|57m40s|**opt**|1h40m0s|**opt**|4h17|m50s|**opt**|
|`NHL13-1216-74`|38m32s|**opt**|1h16m44s|**opt**|4h45m52s|**opt**||–|_feas_|
|`NHL13-2416-78`|–|–|4h23m27s|**opt**|–|_feas_||–|_feas_|
|`NHL13-2416-74`|2h40m32s|**opt**|5h39m17s|**opt**|16h29m31s|**opt**||–|_feas_|
|`NHL11-2624-74`|12h54m23s|**opt**|40h40m18s|**opt**|40h53m7s|**opt**||–|–|



57 

Table 4.4 _Results for the partial-league instances with minimization of total travel distance_ Running times and output solution status from CPLEX<sup>®</sup> on four different models. For a model in which a particular constraint has been relaxed, the reference to the constraint, C _i_ , is enclosed between brackets, [C _i_ ], on the top of the table. The results are separated into two configurations of the revisit-gap parameters: long ( _LGap_ ) and short ( _SGap_ ). The solution status ( _Sol_ ) indicates whether ( _feas_ ) or not (–) a feasible solution, not necessarily the optimal ( **opt** ), has been found within the time limit of 48 hours. 

||Mod|el I|Mo|del II|Mo|del III|Mo|del IV|
|---|---|---|---|---|---|---|---|---|
||C1<br>C<br>C4<br>[C<br>C7<br>C|2<br>C3<br>5]<br>C6<br>8<br>C9|C1<br>C4<br><br>[C7]<br>|C2<br>C3<br>[C5]<br>C6<br>[C8]<br>[C9]|C1<br>[C4]<br><br>[C7]<br>|C2<br>C3<br>[C5]<br>[C6]<br>[C8]<br>[C9]|[C1]<br>[C4]<br>[C7]|[C2]<br>[C3]<br>[C5]<br>[C6]<br>[C8]<br>[C9]|
|**Param.** _LGap_+|_MinDist_||||||||
|Instance|Time|_Sol_|Time|_Sol_|Time|_Sol_|Time|_Sol_|
|`NHL11-1208-76`|–|–|–|–|–|_feas_|–|_feas_|
|`NHL13-1208-76`|–|–|–|–|–|_feas_|–|_feas_|
|`NHL11-1208-74`|–|–|–|–|–|_feas_|–|_feas_|
|`NHL13-1208-74`|–|–|–|–|–|_feas_|–|_feas_|
|`NHL11-1208-72`|–|–|–|–|–|_feas_|–|_feas_|
|`NHL11-1210-74`|–|–|–|_feas_|–|_feas_|–|–|
|`NHL13-1212-76`|–|–|–|–|–|–|–|–|
|`NHL11-1312-78`|–|–|–|–|–|_feas_|–|–|
|`NHL11-1312-72`|–|–|–|–|–|_feas_|–|–|
|`NHL13-1216-74`|–|–|–|–|–|–|–|–|
|`NHL13-2416-78`|–|–|–|–|–|–|–|–|
|`NHL13-2416-74`|–|–|–|–|–|–|–|–|
|`NHL11-2624-74`|–|–|–|–|–|–|–|–|
|**Param.** _SGap_+|_MinDist_||||||||
|Instance|Time|_Sol_|Time|_Sol_|Time|_Sol_|Time|_Sol_|
|`NHL11-1208-76`|–|_feas_|–|_feas_|–|_feas_|–|_feas_|
|`NHL13-1208-76`|–|_feas_|–|_feas_|–|_feas_|–|_feas_|
|`NHL11-1208-74`|–|_feas_|–|_feas_|–|_feas_|–|_feas_|
|`NHL13-1208-74`|–|–|–|_feas_|–|_feas_|–|_feas_|
|`NHL11-1208-72`|–|–|–|_feas_|–|_feas_|–|_feas_|
|`NHL11-1210-74`|–|_feas_|–|_feas_|–|_feas_|–|_feas_|
|`NHL13-1212-76`|–|–|–|–|–|–|–|–|
|`NHL11-1312-78`|–|_feas_|–|–|–|–|–|–|
|`NHL11-1312-72`|–|_feas_|–|_feas_|–|_feas_|–|–|
|`NHL13-1216-74`|–|–|–|–|–|–|–|–|
|`NHL13-2416-78`|–|–|–|–|–|–|–|–|
|`NHL13-2416-74`|–|–|–|–|–|–|–|–|
|`NHL11-2624-74`|–|–|–|–|–|–|–|–|



58 

Table 4.5 _Results for the 2012 instances with and without minimization of total travel distance_ Running times and output solution status from CPLEX<sup>®</sup> on four different models. In each case, two configurations of the revisit-gap parameters, _LGap_ and _SGap_ , has been tested with ( _MinDist_ ) and without minimization of distance. The solution status ( _Sol_ ) indicates whether ( _feas_ ) or not (–) a feasible solution, not necessarily the optimal ( **opt** ), has been found within the time limit of 48 hours. 

||M|odel|I|M|odel|II|Mo|del|III|M|odel|IV|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||C1<br>C4<br>C7|C2<br>[C5]<br>C8|C3<br>C6<br>C9|C1<br>C4<br>[C7]|C2<br>[C5]<br>[C8]|C3<br>C6<br>[C9]|C1<br>[C4]<br>[C7]|C2<br>[C5]<br>[C8]|C3<br>[C6]<br>[C9]|[C1]<br>[C4]<br>[C7]|[C2]<br>[C5]<br>[C8]|[C3]<br>[C6]<br>[C9]|
|**Instance** `NHL12-`|`1315a`||||||||||||
|Parameters|Time||_Sol_|Time||_Sol_|Time||_Sol_|Time||_Sol_|
|_LGap_|4h17|m36s|**opt**|2h13|m11s|**opt**|4h24m|18s|**opt**|2h39|m58s|**opt**|
|_SGap_|15|m56s|**opt**|9|m4s|**opt**|55m|20s|**opt**|41|m10s|**opt**|
|_LGap_+_MinDist_||–|_feas_||–|_feas_||–|_feas_||–|_feas_|
|_SGap_+_MinDist_||–|_feas_||–|_feas_||–|_feas_||–|_feas_|
|**Instance** `NHL12-`|`1315b`||||||||||||
|Parameters|Time||_Sol_|Time||_Sol_|Time||_Sol_|Time||_Sol_|
|_LGap_||–|–||–|–||–|_feas_||–|_feas_|
|_SGap_||–|–|8h59|m43s|**opt**||–|_feas_||–|_feas_|
|_LGap_+_MinDist_||–|–||–|–||–|_feas_||–|_feas_|
|_SGap_+_MinDist_||–|–||–|–||–|_feas_||–|_feas_|



Table 4.6 _Results for the 2012-13 season schedule of the Eastern Conference_ Constraint violations and travel distance on the results from Table 4.5 on Model III for the instance `NHL12-1315a` . The column ∆ _Dist_ refers to the difference between the total travel distance for the corresponding solution and the travel distance for the actual NHL 2012-13 schedule of the Eastern Conference, which is 268034 miles. 

|**Model III**|||||Numb|er of|violati|ons||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|Parameters|_Sol_|C1|C2|C3|[C4]|[C5]|[C6]|[C7]|[C8]|[C9]|∆_Dist_|
|_LGap_|**opt**|0|0|0|0|0|0|0|0|0|+40492|
|_SGap_|**opt**|0|0|0|0|0|0|0|0|0|+33661|
|_LGap_+_MinDist_|_feas_|0|0|0|18|0|9|0|0|2|+50244|
|_SGap_+_MinDist_|_feas_|0|0|0|2|0|0|0|0|0|+33344|



59 

Table 4.7 _Results for the entire-league instances without minimization of total travel distance_ Running times and output solution status from CPLEX<sup>®</sup> on four models (different constraint relaxations) with one revisit-gap configuration (short). For a model in which a particular constraint has been relaxed, the reference to the constraint, C _i_ , is enclosed between brackets, [C _i_ ], on the top of the table. The solution status ( _Sol_ ) indicates whether ( _feas_ ) or not (–) a feasible solution, not necessarily the optimal ( **opt** ), has been found within the time limit of 48 hours. 

||Mode<br><br>|l I<br>|M<br>|odel<br>|II<br>|Mo<br>|del III<br><br>|Mo<br><br>|del I<br>|V<br>|
|---|---|---|---|---|---|---|---|---|---|---|
||C1<br>C2<br>C4<br>[C5]<br>C7<br>C8|C3<br><br>C6<br>C9|C1<br>C4<br>[C7]|C2<br>[C5]<br>[C8]|C3<br>C6<br>[C9]|C1<br>[C4]<br><br>[C7]<br>|C2<br>C3<br>[C5]<br>[C6]<br>[C8]<br>[C9]|[C1]<br><br>[C4]<br><br>[C7]<br>|[C2]<br>[C5]<br>[C8]|[C3]<br>[C6]<br>[C9]|
|Instance|Time|_Sol_|Time||_Sol_|Time|_Sol_|Time|_Sol_||
|`NHL09-00a`|11h31m|**opt**|36h25|m|**opt**|–|–|–|–||
|`NHL10-00a`|33h49m|**opt**|33h26|m|**opt**|–|–|–|–||
|`NHL11-00a`|15h40m|**opt**|36h5|m|**opt**|–|–|–|–||
|`NHL13-00a`|10h47m|**opt**||–|–|–|–|–|–||
|`NHL09-04a`|–|–||–|–|–|–|–|–||
|`NHL10-04a`|39h26m|**opt**||–|–|–|–|–|–||
|`NHL11-04a`|–|–||–|–|–|–|–|–||
|`NHL13-04a`|–|–||–|–|–|–|–|–||
|`NHL09-08a`|–|–||–|–|–|–|–|–||
|`NHL10-08a`|–|–||–|–|–|–|–|–||
|`NHL11-08a`|–|–||–|–|–|–|–|–||
|`NHL13-08a`|–|–||–|–|–|–|–|–||



60 

# **CHAPTER 5** 

# **AN ADAPTIVE LARGE NEIGHBORHOOD SEARCH** 

The results outlined in the preceding chapter support the general idea in the sports scheduling literature that a problem like the scheduling of the NHL games might require more specialized optimization approaches (Schaerf, 1999; Trick, 2011). Therefore, in this chapter, we propose an algorithm that integrates both classic and novel optimization techniques into an Adaptive Large Neighborhood Search (ALNS), which is well-suited for tightly-constrained problems and has provided outstanding results for transportation and other scheduling problems (Pisinger and Ropke, 2010; Kovacs _et al_ ., 2012). 

In the following sections, we describe our ALNS algorithm for the NHL scheduling problem, which includes a review of the heuristics introduced by Fleurent (1987) and computational experiments on setting the parameters of the algorithm, and present some results for several instances we have introduced in the preceding chapter. 

# **5.1 Model** 

Here, we consider a model where the constraints enumerated in Chapter 3 for the NHL scheduling problem are all soft constraints. In addition to the essential constraints that, for example, does not allow more than one game for a team on one day, this model consists basically of an objective function defined by a weighted sum of the number of violations for the nine constraints, C1, C2, . . . , C9. Indeed, in this chapter, the _objective function value_ , or simply _cost_ , with regard to a solution (schedule) _S_ for the NHL scheduling problem is given by 



where _fi_ ( _S_ ) is the number of violations of the constraint C _i_ in the schedule _S_ , and _wi_ is the corresponding non-negative weight (or penalty). 

# **5.2 Algorithm** 

The Adaptive Large Neighborhood Search (ALNS) algorithm that we propose in this thesis for the NHL scheduling problem follows the framework introduced by Ropke and Pisinger (2006), which is an extension of the Large Neighborhood Search (LNS) given by Shaw 

61 

(1998). The ALNS is also essentially based on the _ruin and recreate_ paradigm presented by Schrimpf _et al_ . (2000). 

Generally speaking, that framework is made up of repeated attempts to improve a certain solution, referred to as the _current solution_ , which must initially be either provided or generated from scratch. Each of those attempts defines an iteration of the ALNS during which part of the current solution is modified and the resulting new solution is evaluated to be either rejected or accepted to become the “current” solution for the next iteration. 

Indeed, during each ALNS iteration, two kinds of algorithms are systematically applied to the current solution: first, one that relax part of the solution, and then, another algorithm that re-optimizes the problem over the relaxed part in attempt to obtain a better whole solution. These partial-relaxation and re-optimization algorithms are well known in the ALNS literature as _destroy operator_ and _repair operator_ , respectively. 

In general, an ALNS provides a number of operators, each one implementing a different strategy, either for destroying or for repairing a solution. As suggested by Ropke and Pisinger (2006), the approach might become more robust on the whole when alternating between different destroy and repair operators, as one operator may be more effective than another on different instances of the problem. 

One destroy and one repair operators are selected at the beginning of each iteration in a random weighted manner according to their individual performance as the search progresses. The idea is to make the most promising operators more likely to be chosen (and applied) through the iterations of the ALNS. 

In our ALNS, all the destroy and repair operators are heuristics. Every destroy operator set games _free_ by canceling some game-day assignments in the current solution, or equivalently, “removes” certain games from the current schedule. In the same way, every repair operator assigns a day to each free game, or equivalently, “inserts” the free games back into the current schedule—hopefully on different (and better) days than before. This might explain why, from an application point of view, the literature often refers to the destroy and repair operators as _removal_ and _insertion_ operators, respectively. 

We now present the design decisions on the solution acceptance criteria, and on the selection of operators and the adjustment of their weights, which control the master level of the ALNS. In the next subsections, we then address a multi-heuristic approach to construct an initial solution for the problem, and describe the operators that we propose either for partially destroying an NHL schedule or for repairing it to a complete schedule. 

62 

# **5.2.1 Controlling the master level of the algorithm** 

Basically, our ALNS algorithm consists of the construction of an initial solution ( _Sinit_ ) and a loop that, while not all constraints of the problem are satisfied, tries to improve the current solution ( _Scurr_ ) through a fixed number of iterations. 

Here, we first present the solution acceptance criteria for each iteration of the algorithm; and then, we describe the strategies for the adaptive layer of the search, which controls the choice of the operators according to their individual performance in past iterations. An outline, with a pseudo-code, of the master level of the algorithm is presented in Appendix A.1. 

# **Solution acceptance criteria** 

We have chosen to use the acceptance criteria from Simulated Annealing, which has been widely used in the ALNS literature. Therefore, during each iteration of our ALNS, after a destroy and a repair operators have been applied, the new solution is accepted whenever its cost is not worse (not higher) than the cost of the current solution; and otherwise, the new solution is accepted with a certain probability. The worse the new solution is, the less likely it is to be accepted. In addition, this probability is proportional to a control parameter known as the _temperature_ , which is slightly decreased as the ALNS advances. 

To be more precise, we initially set an initial temperature _T_ 0 to a high value, and then, for each iteration _k_ of the ALNS, the temperature is lowered according to a _cooling schedule_ defined by _Tk_ +1 = _c Tk_ , where _c_ , such that 0 _< c <_ 1, is known as the _cooling factor_ . If _Scurr_ , with cost _f_ ( _Scurr_ ), is the current solution, and _Stemp_ , with cost _f_ ( _Stemp_ ), is the temporary solution generated by the corresponding pair of destroy and repair operators, then _Stemp_ is accepted whenever the condition _f_ ( _Stemp_ ) _≤ f_ ( _Scurr_ ) holds; otherwise, the temporary solution is accepted with probability _e_<sup>_−_(</sup><sup>_f_(</sup><sup>_Stemp_)</sup><sup>_−f_(</sup><sup>_Scurr_))</sup><sup>_/Tk_</sup> , which depends on the current temperature, _Tk_ , and on the corresponding increase in the cost, _f_ ( _Stemp_ ) _− f_ ( _Scurr_ ). 

Using the strategy of Ropke and Pisinger (2006), instead of providing the initial temperature as a parameter to the ALNS, a more meaningful parameter, the _start temperature control parameter_ (which we denote by _τ_ ), is used to calculate the temperature according to an evaluation of the initial solution at hand. 

Indeed, we first evaluate the initial solution, _Sinit_ , with a slightly modified cost function, _f_<sup>ˆ</sup> , that is also a weighted sum of the constraint violations, but without the terms corresponding to the first two constraints (the “most costly” ones). And then, the initial temperature is set to a value such that, at the beginning of the algorithm, a temporary solution causing a cost increase of exactly _τ_ % of _f_<sup>ˆ</sup> ( _Sinit_ ) would be accepted with probability 0.5. 

In addition, because we have chosen to run the ALNS for a fixed and relatively large 

63 

number of iterations, we also compute the cooling factor, instead of following the strategy by Ropke and Pisinger (2006), which provides the cooling factor as another parameter to the algorithm. In fact, we set the cooling factor, _c_ , which controls the constant rate of decrease in the temperature parameter to a value such that a temporary solution one unit worse than the current solution would have only 1% of chance of being accepted at the last ALNS iteration. The cooling factor depends thus on the initial temperature and on the (typically large) maximum number of ALNS iterations, and its value is usually very close to 1.0. This results in only a slight decrease in the temperature from one iteration to the next. 

# **Operator selection** 

As previously mentioned, during each iteration of the ALNS, two operators are selected: one for destroying part of the current solution and another for repairing it. The selection of operators is implemented by first assigning to each operator a weight that represents its past performance on the problem instance being solved. Then that weight is used to associate a probability of selection with each individual operator. In fact, the probability of an operator being chosen is proportional to its weight, as the ALNS uses a _roulette wheel selection_ . 

To be more precise, if _ωi_ is the weight of a destroy operator _i_ , its probability of being selected is _ωi/_<sup>�</sup> _o∈I_<sup>_−ωo_,where</sup><sup>_I−_isthesetofdestroyoperatorsprovidedtotheALNS.The</sup> strategy for selecting a repair operator is identical to that of a destroy operator. 

# **Weight adjustment** 

During the search, if all the operators (either for destroying or for repairing) had the same weight, then every operator would have, at any time, the same probability of being selected. The ALNS, however, has an adaptive layer that automatically adjusts the weights associated to operators in order for those weights to mimic the performance of the operators in earlier iterations. 

In our implementation, as suggested by Ropke and Pisinger (2006), the weights are indeed systematically recalculated at the end of every certain number of iterations. The whole search is split into blocks of consecutive iterations called _segments_ . All the segments have the same number of iterations, which defines the _segment size_ , a parameter that is provided to the ALNS. 

According to the performance of the operators during a segment, a _score_ is assigned to each of them. At the end of a segment, the weight of every operator (and thus its selection probability) is then computed as a weighted sum of its score during the segment and its overall score since the beginning of the search. 

64 

To be more precise, let _s_ be an ALNS segment, and let _o_ be an operator that is selected at least once through the iterations of the segment _s_ . In order to compute the weight of the operator _o_ for the next segment, a score _πo_ is set to zero at the beginning of the segment _s_ and might then be increased by a certain amount each time the operator _o_ is applied through _s_ . The increment amount depends on the quality of the (temporary) solution obtained after the corresponding destroy and repair operators have been applied. 

We have chosen to use three _score adjustment parameters_ , _σbes_ , _σbet_ , and _σacc_ , to specify the amounts by which the score may be increased. Indeed, at any iteration when _o_ is applied during the segment _s_ , the score _πo_ increases by _σbes_ if the cost of the resulting solution is the best (lowest) found since the beginning of the search; otherwise, _πo_ increases either by _σbet_ if the resulting solution cost is better than the cost of the current solution, or by _σacc_ if the resulting solution is accepted by the ALNS but its cost is worse than the cost of the current solution. The score is not changed if the resulting solution is not accepted. 

When the end of the segment _s_ is reached, and the operator _o_ had been applied _θo_ times and gained a total of _πo_ as score during that segment, the weight of _o_ for the next segment is computed as _ωo_ (1 _− ρ_ ) + _ρ_ ( _πo/θo_ ) _,_ where _ρ_ , such that 0 _≤ ρ ≤_ 1, is the _reaction factor_ controling the degree of change on the current weight, _ωo_ , in response to the “smoothened” score obtained by the operator _o_ . 

# **5.2.2 Constructing an initial solution** 

In order to provide a complete NHL schedule at the beginning of the ALNS algorithm, we propose a construction approach that implements the heuristics introduced by Fleurent (1987). They were originally intended to be used in an interactive manner by an expert scheduler that would call any of the corresponding procedures whenever needed during the scheduling process. But Fleurent (1987) also proposes an implementation that calls the heuristic procedures in a specific order, without any interaction with the user. Since the game-day assignments in Fleurent’s heuristics need to satisfy most of the constraints of the problem, that approach alone may not be able to fully schedule the free games (at least not for the hardest instances, with none or too few extra arena dates per team). We are therefore proposing to construct an initial NHL schedule by first applying those heuristics as suggested by Fleurent (1987), and then, if there still are free (missing) games, by scheduling them with a basic greedy approach that evaluates the incremental cost associated with every possible day for each game being scheduled. This might then yield a reasonable NHL schedule from which to start our search for an improved solution. 

Fleurent’s heuristics will be individually described in the next subsections (and outlined in Appendix B.1). Before that, we outline the whole construction approach by the steps 

65 

informally stated below, where the heuristics we mention refer to those introduced by Fleurent (1987) and, to stay in line with their original conception, a “feasibly-possible scheduling” is a game-day assignment that satisfies all the constraints in the set C _F_ , except perhaps C5 on the minimum number of games per week, where C _F_ = _{_ C0 _,_ C1 _,_ C2 _,_ C4 _,_ C5 _,_ C6 _}._ 

- **_Step 1._** _Schedule forced trips._ Apply the _forced-trip heuristic_ to schedule as many free games as feasibly possible by first identifying long periods of days with no arena dates for a team, and then, by assigning the respective team to visit, in a single trip, at most seven of its distant opponents exclusively during the corresponding period of arena unavailability. 

- **_Step 2._** _Schedule forced home games._ Apply the _forced-home heuristic_ to schedule, for each trip lasting more than one week, two home games for the respective traveling team: one game on its last (latest) arena date before the trip, and the other, on its first arena date after the trip. 

- **_Step 3._** _Schedule free trips._ Apply the _free-trip heuristic_ to schedule all current free games opposing teams based far from each other by first identifying, for each team, at most three of its distant opponents to be visited in a single trip, and then, by scheduling every one of those long-distance trips on a period that does not violate the constraints in C _F_ and that contains the minimum possible number of arena dates of the visiting team. 

- **_Step 4._** _Schedule forced home games._ Apply the _forced-home heuristic_ to have, for each trip lasting more than seven days, a home game scheduled on the last and on the first arena day of the traveling team before and after that trip, respectively. 

- **_Step 5._** _Schedule weekend games._ Apply the _weekend-game heuristic_ to schedule as many free games as feasibly possible respectively on Saturdays, on Fridays, and on Sundays, by trying not to schedule a team to play away on a weekend containing some of its own arena dates, and by never putting a team to play an away game within a period when it has already been scheduled to visit distant opponents. 

- **_Step 6._** _Schedule weekday games._ Apply the _weekday-game heuristic_ to schedule as many free games as feasibly possible on weekdays from Monday through Thursday, by trying not to schedule a team to play away on its own arena dates, and by never assigning days from periods of long-distance visits for the teams involved in the game being scheduled. 

- **_Step 7._** _Exchange games._ Apply the _single exchange heuristic_ , and then the _double exchange heuristic_ , to schedule as many free games as feasibly possible by allowing some of the previously scheduled short-distance visits to be rescheduled on alternative days. 

66 

- **_Step 8._** _Schedule the remaining free games._ Select at random every remaining free game and schedule it in a greedy manner on a day that, besides not violating the constraint C0 (no more than one game a day for a team), produces the lowest incremental cost. 

We now describe each of the heuristics initially proposed by Fleurent (1987). To anticipate, they have been adapted as some of the operators for our ALNS, which is described later in this chapter. For a more precise description of each of them, which outlines the steps they perform, see Appendix B.1. 

# **Forced-trip heuristic** 

The forced-trip heuristic tries to generate as many trips as feasibly possible, each one made up exclusively of games taking place during a long period of consecutive days with no arena dates for the respective traveling team. The overall idea is straightforward. In order to preserve dates for eventual subsequent allocations of home games by other heuristics, no team is scheduled to play away on days when its own arena is available. Furthermore, in the course of any trip being generated, the visiting team only plays against several distant opponents, which in turn, should ideally be located in the same geographical area. This aims to reduce the total distance traveled by the teams during the entire regular season. 

The strategy on preserving home dates is directly related to _forced trips_ , which are trips taking place entirely during a period when the arena of the traveling team is not available (Ferland and Fleurent, 1991). Because the schedule is intended to be feasible with regard to the constraints in C _F_ (including the arena availability constraint), when applying the forcedtrip heuristic, the only games scheduled for a team between two of its consecutive arena dates are then games to be played away. Moreover, the corresponding opponents on those games must be located farther than a given threshold distance (900 miles) from the arena of the traveling team and, as we have anticipated, they should be based in the same geographical area. 

In an attempt to satisfy this goal, the following saving measure is used when selecting the teams to be visited during a forced trip: 



where _a_ is the traveling team, _h_ 1 and _h_ 2 are two potential consecutive away opponents, and _dist_ ( _·, ·_ ) is the distance between the corresponding pair of teams. 

A large value for this measure, which was used by Clarke and Wright (1964) in a classical algorithm for vehicle routing problems, suggests that indeed the two corresponding opponents are located close to each other when compared to their distances to the arena of the traveling 

67 

# team. 

Basically, the heuristic starts building a new trip whenever it finds a team that can visit two distant opponents on a single two-game trip scheduled between two of its consecutive arena dates (which would rather be widely separated from each other) without violating the constraints in C _F_ . Then, it attempts to extend the trip for no more than seven games scheduled only to the current period of arena unavailability for the traveling team. Indeed, the heuristic tries to schedule that same team to directly visit other distant opponents both before and after the (so far two-game) trip. Each away game appended to the trip is selected as to maximize the saving measure defined above, and the constraints in C _F_ must be satisfied all the time. 

# **Forced-home heuristic** 

The forced-home heuristic tries to schedule home games to the begin and to the end of every long-lasting trip for a team. Indeed, the goal is to schedule, for each trip lasting more than seven days, the respective traveling team to play home at its first arena date just before the trip and at its first arena date after the trip. Every game-day assignment must satisfy the constraints in C _F_ . The heuristic seeks, as a priority, to schedule games for which the arena of the visiting team is not available at the day being assigned; and in case of tie, the game corresponding to the visit of the nearest opponent is chosen to be scheduled. 

# **Free-trip heuristic** 

The free-trip heuristic, as the forced-trip heuristic, generates for each team, trips that are made up exclusively of games to be played against distant opponents. In this case, however, trips are individually generated by first determining a short promising sequence of away games, and only then, by trying to assign suitable days to the respective games. In other words, once an appropriate new trip is identified, the heuristic is “free” to choose any promising period when it must take place, with the condition that the constraints in C _F_ are not violated. 

The overall goals when generating every free trip are twofold: _(1)_ to schedule a team to visit distant opponent located nearby in a same area so as to reduce the total travel distance; and _(2)_ to preserve as many arena dates of the traveling team as possible, even though such dates are now allowed to be taken, if necessary. 

At first, a team _a_ having the highest number of distant (more than 900 miles) away games remaining to be scheduled is chosen as the traveling team. Because it may be too hard to find a suitable period of days for a trip with many games, the free trips are made up of only 

68 

two or only three games. The first two distant opponents, _h_ 1 and _h_ 2, to be visited by _a_ in the free trip, _r_ ( _a_ ), being generated are chosen as to maximize _sa_ ( _h_ 1 _, h_ 2), the saving defined earlier. A third opponent, _h_ 3, is then appended to _r_ ( _a_ ) if the value _sa_ ( _h_ 3 _, h_<sup>_′_</sup> ) is maximized with _h_<sup>_′_</sup> = _h_ 1 or with _h_<sup>_′_</sup> = _h_ 2, among all distant opponents that _a_ must still be scheduled to visit. Finally, the heuristic tries to schedule the free trip _r_ ( _a_ ) to a period having the least number of arena dates for the traveling team, _a_ . 

# **Weekend-game heuristic** 

The weekend-game heuristic tries to schedule as many of the short-distance visits as possible exclusively to weekend days as this is assumed to be a promising factor to increase spectator attendance at home games. Every game-day assignment satisfies the constraints in C _F_ and no game is scheduled to a period when either of the respective teams has already been assigned to visit distant opponents. 

The heuristic is based on a specific set of“target days”, which is successively characterized (in this order) by all Saturdays, all Sundays, and all Fridays of the regular season period. For each of those sets, the heuristic seeks, whenever possible, to select a target day and a free game that yield a feasible game-day assignment where two non-distant teams oppose each other without involving any long-distance trip period for either of them. 

The actual assignments are, furthermore, based only on the arena availability of the visiting team during the respective weekend. Indeed, at any time, a game is scheduled exclusively on a target day when the arena of the visiting team, with regard to the corresponding three weekend days, is either _(i)_ completely unavailable, _(ii)_ available only on one day which is not the target day, _(iii)_ available only on the target day itself, or _(iv)_ available only on the other two (non-target) days. These four required conditions define the “levels of preference” that are successively taken into account when selecting game-day pairs for the assignments; on each of those levels, the goal is to carry out as many feasible assignments satisfying the corresponding condition as possible. 

# **Weekday-game heuristic** 

The weekday-game heuristic tries to schedule the remaining free games to weekdays from Monday through Thursday. As for the preceding heuristic, the game-day assignments satisfy the constraints in C _F_ and no game is scheduled to a period when either of the respective teams has already been assigned to visit distant opponents. 

In order to avoid wasting arena dates by scheduling a team to play away when its own arena is available, the heuristic adopts a strategy that is based on the Vogel Approximation 

69 

Method (Reinfeld and Vogel, 1958), which is a well-known simple procedure for obtaining a feasible solution to the classical transportation problem. 

Indeed, a game-day assignment cost is initially calculated for each pair of free game and corresponding feasible day (when, in particular, the arena of the home team is available). This cost is directly proportional to the number of teams for which the respective arena is available at the same day. Furthermore, a large penalty is added to the cost whenever that day is also available for the visiting team. Subsequently, the two less costly potential assignments for each game are taken and the difference between their costs is computed. This difference between the two lowest cost for every free game can be seen as a measure of the current “regret” for failing to schedule the game on its less costly feasible day. Finally, the heuristic selects a game with the largest regret and assigns to it the corresponding feasible day having the smallest cost. After each assignment, the costs and the regrets are updated for all the free games involving either of the just-scheduled teams and for which that same day is also implicated in one of their respective (two) less costly potential assignments. 

# **Exchange heuristics** 

Two exchange heuristics are presented in Fleurent (1987). Both heuristics try to schedule the free games by allowing some of the previously scheduled games to be rescheduled on alternative days. 

Whenever possible, free games are scheduled on days that violate no constraints in C _F_ . However, for each iteration when no feasible day is available, the approach considers only the days that have already been assigned to other games involving either of the two teams in the current free game. One of those days is then selected if by just removing some of its previously scheduled game, it becomes feasible for the current game scheduling (in particular, the home and the away teams would still have only a single game to play on the chosen day). Every time this happens, the heuristic replaces the corresponding scheduled game on the selected day by the free game at hand and immediately tries to reschedule the removed game on another feasible day. This defines a new _recursive level_ of the approach. If no feasible day is found for the removed game, the heuristic backtracks to the preceding level, reschedules that game on its last cancelled day, and tries to schedule the original free game on another day. For practical reasons, a parameter might be provided to specify the maximum number of levels that the heuristic can go through when attempting to schedule a free game. 

In fact, it may also happen that the most promising day for a certain game scheduling by exchanges is a day when both the home and the away teams in the current free game have already been scheduled to play against other opponents. From this fact arises the difference between the two proposed exchange heuristics: while one allows two games to be 

70 

simultaneously cancelled from a same day, the other does not. Indeed, if no feasible day is already available, the called _single exchange heuristic_ tries to find a day from which removing only one game would turn that day into a feasible candidate for the current free game to take place. On the other hand, whenever that same strategy fails, the called _double exchange heuristic_ seeks to carry out the scheduling of the game by removing from a certain day exactly two games involving the teams in the current free game if it then yield a feasible assignment. Both heuristics backtrack when either no promising day is found or a given maximum recursive level is reached. 

We now propose a number of destroy operators to be provided to the ALNS for the NHL scheduling problem. 

# **5.2.3 Partially destroying a solution** 

In this subsection, we propose 15 operators to partially destroy the schedules through the iterations of the ALNS for the NHL scheduling problem. Each of these operators is a heuristic that cancels a given number of game-day assignments in the current schedule. What makes the heuristics different from each other are the criteria for choosing the games to be removed from the schedule. In particular, when selecting its target games, a removal operator may use a specific level of greediness (or randomness); and some operators may, for example, adopt a more systematic approach of destruction than others. 

Here, we divide the destroy operators into five groups, as follows: 

1. random-based removal 

   - 01<sup>**_–_**</sup> _Random-based removal_ 

2. structure-based removals 

   - 02<sup>**_–_**</sup> _Divisional removal_ 

   - 03<sup>**_–_**</sup> _Intradivisional removal_ 

   - 04<sup>**_–_**</sup> _Interdivisional removal_ 

   - 05<sup>**_–_**</sup> _Conferential removal_ 

   - 06<sup>**_–_**</sup> _Intraconferential removal_ 

   - 07<sup>**_–_**</sup> _Interconferential removal_ 

3. neighboring-based removals 

   - 08<sup>**_–_**</sup> _Day-neighboring removal_ 

   - 09<sup>**_–_**</sup> _Place-neighboring removal_ 

4. critical removals 

71 

10<sup>**_–_**</sup> _Arena-critical removal_ 

- 11<sup>**_–_**</sup> _Sequential greedy removal_ 

12<sup>**_–_**</sup> _Cost-critical removal_ 

5. trip-based removals 

   - 13<sup>**_–_**</sup> _Short-trip removal_ 

   - 14<sup>**_–_**</sup> _Close-trips greedy removal_ 

   - 15<sup>**_–_**</sup> _Scattered-trip removal_ 

In general, the amount that an operator is allowed to destroy in a solution has substantial impact on the quality of the solutions produced by an ALNS algorithm (Pisinger and Ropke, 2007). In particular, for most of the operators we propose here, the number of game-day assignments satisfying the selection criteria of the operator being applied to the schedule at hand might be too high for all them to be removed and eventually reinserted (by some repair operator) in an effective manner. We introduce then the following strategy, which comparing to the seminal work by Ropke and Pisinger (2006), can be seen as an intensification mechanism that is being integrated into the ALNS framework. Except for the operators 10<sup>**_–_**</sup> , 11<sup>**_–_**</sup> , 12<sup>**_–_**</sup> , and 13<sup>**_–_**</sup> , all the destroy operators will first choose a certain number of game-day assignments in the current schedule and try to evaluate the advantage of cancelling each of them, prior to proceeding with a rather few game removals. 

The choice of the target assignments, which are the candidates to be eventually cancelled by the corresponding operator, is based on the specific strategy of each heuristic. On the other hand, when actually removing games from a schedule, the same greedy-based strategy is used by all those operators. This strategy consists in given a higher priority to targetassignment cancellations that individually leads to the best (maximum) reduction on the objective function value; and, in case of tie, the arena dates of the respective home and away teams are also taken into account. 

To be more precise, the cancellation of a game-day assignment will rely on a function that combines, in a weighted manner, both the incremental cost of the cancellation and the effectiveness of that assignment for the corresponding home and away teams regarding their arena availabilities. Let that function be denoted by _f_ **–** and let its value for removing an assignment [ _a_ @ _h_ : _d_ ] from a schedule _S_ be defined as 



where _f_ **–**<sup>∆(</sup><sup>_a, h, d_)isthecorresponding</sup><sup>_removalincrementalcost_,namely,</sup><sup>_f_(</sup><sup>_S \ {_[</sup><sup>_a_@</sup><sup>_h_:</sup><sup>_d_]</sup><sup>_}_)</sup><sup>_−_</sup> _f_ ( _S_ ); and _A_<sup>¯</sup> _a,h,d_ , which we refer to as the _arena-utility value_ for having the day _d_ assigned 

72 

to the game _a_ @ _h_ , is a constant given by 



The strategy is then to remove from a schedule a given number of target games having the lowest values of the function _f_ **–** . Obviously, this is an attempt to cancel assignments causing to most violations of constraints, while trying to release arena dates for teams that have been scheduled to play away in the current schedule when their own arena is available. 

In the remainder of this subsection, we describe every one of the destroy operators enumerated above. Suppose that any of those operators is a procedure to which at least the following three parameters are given: _S_ , a complete schedule (from the current ALNS iteration); _n_ ˆ, the maximum number of game-day assignments to be selected from _S_ as candidates for the cancellations; and _n_ ˜, the number of assignments to be actually cancelled in the schedule _S_ . Consider also that any complete schedule is made up of exactly _n_ game-day assignments, and the condition 0 _< n_ ˜ _< n_ ˆ _≤ n_ holds (otherwise, if _n_ ˜ _≥ n_ ˆ then all the corresponding target assignments could be cancelled with no need for evaluating them beforehand). 

In addition to the descriptions that follows, Appendix C.1 outlines the steps performed by each destroy operator. 

# **Random-based removal** 

At first, we propose a destroy operator in which the target games are chosen at random among all games in the current schedule. Indeed, the _Random-based removal_ (01<sup>**_–_**</sup> ) is a heuristic that starts by choosing at random _n_ ˆ target assignments in the current schedule, ˜ evaluates by _f_ **–** the extended incremental cost of each of them, and then cancels _n_ target assignments having the lowest values of _f_ **–** . 

# **Structure-based removals** 

We now propose six destroy operators in which the target games for each operator are chosen at random among a specific subset of games that is determined only by the structure of the NHL. In particular, such subset does not depend on the game-day assignments in the current schedule. As for the preceding operator, once _n_ ˆ target games have been chosen, ˜ those games are evaluated by _f_ **–** , and the _n_ target games in _S_ yielding the lowest extended incremental cost are removed. 

73 

The first three of these operators choose their _n_ ˆ target games by taking into account the NHL divisions of the home and away teams in each game. Namely, the _Divisional removal_ (02<sup>**_–_**</sup> ) removes only games individually involving at least one team from a division that is randomly chosen beforehand; the _Intradivisional removal_ (03<sup>**_–_**</sup> ) removes only games individually involving both home and away teams from a division that is also randomly chosen in advance; and the _Interdivisional removal_ (04<sup>**_–_**</sup> ) removes only games individually involving teams from two divisions that are also chosen at random when the operator begins. 

The other three structure-based destroy operators choose their _n_ ˆ target games by taking into account the NHL conferences of the home and away teams on each game. Indeed, the _Conferential removal_ (05<sup>**_–_**</sup> ) removes only games individually involving at least one team from a conference that is chosen beforehand; the _Intraconferential removal_ (06<sup>**_–_**</sup> ) removes only games individually involving both home and away teams from a conference that is also randomly chosen in advance; and the _Interconferential removal_ (07<sup>**_–_**</sup> ) removes only games individually involving teams from different conferences. 

# **Neighboring-based removals** 

We now propose two destroy operators in which the target games are chosen either by a neighboring area where they are scheduled to take place or by a neighboring day when they are planned to occur. 

At first, both operators randomly choose a time-window defined by a certain number of consecutive days in the schedule. The _n_ ˆ target game-day assignments are then selected from within that time-window only. However, while the target of the _Day-neighboring removal_ (08<sup>**_–_**</sup> ) is made up by all the games assigned to that period of days, the target assignments in the _Place-neighboring removal_ (09<sup>**_–_**</sup> ) are, in addition, restricted to games to be played within a geographic region that is also chosen at random each time the operator is applied. Finally, ˜ both operators cancel the _n_ target games in _S_ with the lowest values of _f_ **–** . 

# **Critical removals** 

We now propose three destroy operators where the target games are chosen by some more careful evaluation which can involve incremental costs, arena-utility values, and conflicting games for promising reassignments. Here, given a constraint C _i_ , with _i ∈{_ 0 _,_ 2 _,_ 3 _,_ 4 _,_ 6 _,_ 7 _,_ 8 _,_ 9 _}_ , we say that two games in a certain schedule are _Ci-conflicting_ games if together they are involved in some violation for C _i_ . 

One of these operators removes a given number of games from the schedule in a sequentially greedy fashion. Indeed, at each iteration, the _Sequential greedy removal_ (11<sup>**_–_**</sup> ) selects 

74 

and removes from the schedule the current worst game-day assignment regarding the incremental cost of its cancellation (the lower, the worst) and, in case of tie, also regarding its arena-utility value (the lower, the worst). 

The other two critical destroy operators, _Arena-critical removal_ (10<sup>**_–_**</sup> ) and _Cost-critical removal_ (12<sup>**_–_**</sup> ), can also be seen as iterative procedures. In this case, however, each iteration is made up of three basic steps. In the first step, a poorly assigned game (regarding the specific evaluation adopted by each operator) is selected and removed from the schedule. Then, in the second and third steps, a promising day for the just-removed game is chosen, and some other assignments may also be cancelled as an attempt to turn that day into a better candidate for a possible eventual reassignment to the game removed in the first step. 

Indeed, the operator 10<sup>**_–_**</sup> cancels, during the first and second steps, two assignments having the worst arena-utility value, such that the visiting team of the game removed in the second step is the host team of the game removed in the first one. In addition, the second game is removed from a promising day for the first-removed game, a day that, in particular, satisfies the constraint on the minimum gap for revisits (C6). On the other hand, the operator 12<sup>**_–_**</sup> cancels, in the first step, the worst current assignment regarding the incremental cost and (in case of tie) also regarding the arena-utility value. Then, in the second step, this operator identifies a day that does not violate the constraint on the minimum gap for revisits (C6) and that has the lowest number of conflicting games for the game removed in the first step. Finally, in the third step, both operators use an anticipation strategy that removes up to two C _i_ -conflicting games (if any) for the current potential reassignment (which is entirely hypothetical, as these are operators for removals only), regarding every constraint C _i_ , with _i_ = 0 _,_ 1 _,_ 2 _,_ 3 _,_ 4, in this order. 

# **Trip-based removals** 

Finally, we propose three destroy operators where the choice of the target games is based on the trips induced by the current schedule. 

The first of these operators, the _short-trip removal_ (13<sup>**_–_**</sup> ), can be seen as an iterative procedure where each iteration is made up of three basic steps. In the first step, a trip having the least number of games is chosen and all its games are removed from the schedule. Regarding each of those games, the operator identifies, in the second step, a promising day (out from the former trip period) for a potential reassignment that satisfies the constraint on the minimum span for revisits (C6) and that has the lowest corresponding number of conflicting games. In case of tie, the choice of that day is also given by the minimum incremental cost on the objective function. Then, in the third step, the same anticipation strategy used by the preceding (critical) operator is applied in order to remove up to two 

75 

conflicting games (if any) for each potential reassignment. 

The other two trip-based removals explicitly create a set of ˆ _n_ target game-day assignments before removing ˜ _n_ of them in a greedy fashion with regard to their respective incremental cost and (in case of tie) arena-utility values. At the beginning, however, both operators identify a period of days from which the target games are chosen. Such period of days is somehow related to poorly-defined trips. Indeed, the _close-trips removal_ (14<sup>**_–_**</sup> ) initially selects the two consecutive trips (for the same team) having the lowest number of days between them. On the other hand, the _scattered-trip removal_ (15<sup>**_–_**</sup> ) selects, at the beginning, a long-lasting trip (defined by a given threshold) that has relatively few games. In the case of the operator 14<sup>**_–_**</sup> , the target games are selected by the minimum arena-utility value among all the games scheduled during the period of the two corresponding chosen trips and also during the days between them. In the operator 15<sup>**_–_**</sup> , the target games are also chosen by the minimum arenautility value, but they are selected among all the games scheduled during the period of the “scattered” trip chosen at the start. Finally, both operators cancel the _n_ ˜ target games having the lowest values of _f_ **–** . 

We now propose some repair operators to be provided to the ALNS for the NHL scheduling problem. 

# **5.2.4 Repairing a partial solution** 

In this subsection, we propose five operators to repair the partial schedules through the iterations of the ALNS for the NHL scheduling problem. Every operator is a heuristic that, at each ALNS iteration, is able to insert the free games into the current partial schedule. 

Here, we say that a day _d_ is a _free day_ for a game _a_ @ _h_ if neither team _a_ nor team _h_ is currently scheduled to play on day _d_ of the schedule at hand. 

We divide the repair operators into four groups, as follows: 

1. greedy-based insertions 

   - 01<sup>**_+_**</sup> _Single-evaluation greedy insertion_ 

   - 02<sup>**_+_**</sup> _Updated-evaluation greedy insertion_ 

2. regret-based insertions 

   - 03<sup>**_+_**</sup> _Max-regret insertion_ 

3. exchange-based insertion 

   - 04<sup>**_+_**</sup> _Single-exchange insertion_ 

4. Fleurent’s approach-based insertion 

   - 05<sup>**_+_**</sup> _Fleurent’s approach-based insertion_ 

76 

Except for the operators 03<sup>**_+_**</sup> and 05<sup>**_+_**</sup> , the assignment of days to free games will rely on a function that combines, in a weighted manner, both the insertion incremental cost and the effectiveness of the assignment for the respective home and away teams with regard to their arena availabilities. Let that function be denoted by _f_ **+** and let its value for the potential scheduling of a game _a_ @ _h_ on a day _d_ of a schedule _S_ be defined as 



where _f_ **+**<sup>∆(</sup><sup>_a, h, d_) is the corresponding</sup><sup>_insertionincrementalcost_, namely,</sup><sup>_f_(</sup><sup>_S ∪{_[</sup><sup>_a_@</sup><sup>_h_:</sup><sup>_d_]</sup><sup>_}_)</sup><sup>_−_</sup> _f_ ( _S_ ); and _A_<sup>¯</sup> _a,h,d_ is the _arena-utility value_ for having the day _d_ assigned to the game _a_ @ _h_ , as defined in Subsection 5.2.3.The strategy is then to schedule free games on free days leading to the lowest values of the function _f_ **+** . Obviously, this is an attempt to favor the assignments leading to the least violations of constraints, while trying to save arena dates for teams that are being scheduled to play away when their own arena is available. 

In addition to the descriptions that follows, Appendix D.1 outlines the steps performed by each repair operator. 

# **Greedy-based insertion** 

The first repair operator that we propose is a heuristic where free games are successively chosen at random and scheduled in a greedy manner to free days. The operator, which we refer to as _Single-evaluation greedy insertion_ (01<sup>**_+_**</sup> ), can be seen as a two-phase approach that first tries to schedule as many games as possible exclusively to days when the arena of the respective home team is available, and then schedules the possible remaining free games to other days on the current schedule. In both phases, days are assigned to games in the following way. At the beginning, the extended incremental cost determined by _f_ **+** is evaluated for each pair of free game and corresponding free day on the current partial schedule. Then, free games are sequentially scheduled to their respective best free days regarding those costs. So, every time that a game is chosen, the heuristic immediately seeks to find (and to assign) a corresponding free day with the lowest cost that was determined at the beginning. 

The second repair operator is also a greedy-based heuristic. In this case, however, free games are successively chosen in decreasing order of the number of free games to be played at home for each team. Moreover, every time a free game is chosen, the heuristic seeks to assign to it the corresponding best free day on the current (updated) schedule. This operator, which we refer to as _Updated-evaluation greedy insertion_ (02<sup>**_+_**</sup> ), can also be seen as a twophase approach that first tries to schedule as many games as possible exclusively to days when the arena of the respective home team is available, and then schedules the possible 

77 

remaining free games to other days in the current schedule. In both phases, free games are successively scheduled to their respective best free days, which leads to the lowest extended incremental cost at the moment of the assignment. 

# **Regret-based insertion** 

Our third repair operator, which we refer to as _Max-regret insertion_ (03<sup>**_+_**</sup> ), is a regretbased heuristic where the first goal consists in avoiding assignments that “waste” arena dates for the respective away teams. As for the previous repair operators, the insertions rely on a specific evaluation to determine the cost of each possible game-day assignment. However, the main factor in this evaluation, which also involves the corresponding incremental cost, refers to a large penalty if a team was scheduled to visit an opponent on a day when its own arena is available. Generally speaking, the idea is to schedule the free games in decreasing order of the “regret” for failing to assign the first less costly day to a game and eventually having to assign its second less costly day instead. Although this is essentially identical to the weekday games heuristic described on Subsection 5.2.2, the possible assignments are evaluated in a rather refined manner by taking the change in the objective function value into account and by also considering the number of games that are free for the corresponding day at the time of the evaluation. 

To be more precise, the cost, in operator 03<sup>**_+_**</sup> , of scheduling a free game _a_ @ _h_ on a corresponding arena-feasible date _d_ that is free in a partial schedule _S_ is defined as follows: 



where _M_ 1 and _M_ 2 are large constants, such that _M_ 1 _≫ M_ 2; _Aa,d_ is equal to 1 if the day _d_ is also provided by the away team _a_ , and equal to 0 otherwise; _f_ **+**<sup>∆(</sup><sup>_a, h, d_)istheincremental</sup> cost of assigning _d_ to _a_ @ _h_ , namely, _f_ ( _S ∪{_ [ _a_ @ _h_ : _d_ ] _}_ ) _− f_ ( _S_ ); and _|G_<sup>˜</sup> ( _d_ ) _|_ , which can be seen as a “competitiveness” factor for _d_ , is the current number of free games that are arena-feasible (it would satisfy C1) for the day _d_ . 

# **Exchange-based insertion** 

We now propose a repair operator that sequentially chooses the free games in decreasing order of the number of corresponding visits to be scheduled and try to schedule them by single exchanges. Although essentially similar to the single-exchange heuristic addressed in Subsection 5.2.2, we consider three fundamental modifications when selecting a promising day for the free game at hand. The first modification consists in preventing exchanges with games that were already scheduled before the heuristic started. This aims to stay in line with 

78 

the idea that, during each iteration of the ALNS framework, the corresponding non-destroyed part of the solution remains fixed. The second modification refers to the range of the days that are evaluated for the free games when no feasible day is available. Now, a candidate is a day that would allow a feasible assignment by first removing a single game currently scheduled on any day (possibly other than the candidate itself). Thus, the difference here is that a conflicting assignment with regard to any constraint is now taken into account for a possible exchange (rescheduling), instead of being restrict to an assignment that would only violate C0. The third modification refers to the selection of a day. Whenever a tie occurs (where for each candidate day there is only one conflicting game in the schedule), the arenautility values of both the intended assignment and the corresponding conflicting game in the schedule are taken into account. 

Indeed, the _Single-exchange insertion_ (04<sup>**_+_**</sup> ) selects all free games, one at a time, in decreasing order of their quantity for the same away-home pair of teams. For each selected free game ˜ _a_ @ _h_<sup>˜</sup> , the heuristic proceed as follows. If feasible days are available, ˜ _a_ @ _h_<sup>˜</sup> is scheduled on a feasible day _d_<sup>ˆ</sup> leading to the highest arena-utility value, _A_<sup>¯</sup> _a,_ ˜ _h,_ ˜ ˆ _d_ . Otherwise, the heuristic only considers as candidates those days on which scheduling _a_ ˜@ _h_<sup>˜</sup> would result in a single conflicting game somewhere in the current schedule. Among such candidates, _a_ ˜@ _h_<sup>˜</sup> is then scheduled on a day _d_<sup>ˆ</sup> that maximizes the respective arena-utility difference, _A_<sup>¯</sup> _a,_ ˜ _h,_ ˜ ˆ _d − A_<sup>¯</sup> _a′,h′,d′_ , where _a_<sup>_′_</sup> @ _h_<sup>_′_</sup> , currently scheduled on a day _d_<sup>_′_</sup> (which is not necessarily equal to _d_<sup>ˆ</sup> ), is the conflicting game for the assignment of _d_<sup>ˆ</sup> to ˜ _a_ @ _h_<sup>˜</sup> . The heuristic then reschedules, in a recursive manner, the game _a_<sup>_′_</sup> @ _h_<sup>_′_</sup> on another day. Whenever it fails to find a candidate under those conditions, or whenever the maximum recursive level is reached, the free game at hand is scheduled on the corresponding free day leading to the lowest extended incremental cost, determined by _f_ **+** , with respect to the current (partial) schedule. 

# **Fleurent’s approach-based insertion** 

Finally, we propose a repair operator that tries to schedule the free games by applying a slightly modified version of the approach by Fleurent (1987). Indeed, the _Fleurent’s approach-based insertion_ (05<sup>**_+_**</sup> ) is an adaptation of five (out of seven) heuristics addressed in Subsection 5.2.2 on the generation of an initial solution. Although the heuristics are applied in the order suggested by Fleurent (1987), no game exchange is performed by this operator, neither is a forced-home scheduling. 

The first modification in the original heuristics refers to the generation of forced trips, but they are still composed of long-distance visits only. In fact, the forced-trip heuristic is split into two phases: at the beginning, it tries to create as many new two-game trips as possible, and only then, it attempts to extend any long-distance trip in the current schedule. 

79 

The free-trip heuristic is applied with no modifications. But both the weekend-game and the weekday-game heuristics are changed. They are now applied to all free games, instead of only those referring to short-distance visits, and also, a game may be scheduled within a period for some long-distance trip. In addition, when applying the weekday-game heuristic, which is based on evaluations of “regrets”, the cost of assigning a feasible day for a free game now relies only on the free games that are feasible for that day at the time of the evaluation. Finally, because all the assignments are required to be feasible on the Fleurent’s heuristics, it may occur that some free games can not be inserted by them into the current schedule. In this case, the same greedy approach as that of the “Max-regret insertion ( 03<sup>**_+_**</sup> )” is applied in order to complete the schedule. 

The next section reports the computational experiments on our implementation of the ALNS algorithm. 

# **5.3 Computational Experiments** 

We now describe the experiments conducted when calibrating the ALNS from the preceding section and report some results on several instances of the NHL scheduling problem. The calibration is based on the quality of the solutions that the approach is able to produce. All the solutions are evaluated exclusively by their respective costs, but in some cases, the corresponding number of constraint violations are also reported. For that matter, the weights in the objective function (5.1) were set as follows: _w_ 1 = 10 000, _w_ 2 = 1 000, _w_ 3 = 10, _w_ 4 = 10, and _wi_ = 1 for each constraint C _i_ with _i ∈{_ 5 _,_ 6 _, . . . ,_ 9 _}_ . Therefore, regarding the actual NHL schedules referred in Table 3.2, the costs for the last five seasons, starting with the 2009-10 season, are 245, 252, 186, 194, and 142, respectively. Obviously, our goal is to design schedules that attain the minimum total cost, which is zero as objective function value, by satisfying all the constraints of the problem. 

For all the experiments, the ALNS algorithm was implemented in the object-oriented language COMET™ and run under Linux on a 2.2 GHz Dual AMD Opteron Processor 275 (where only one processor was used) with 8 GB of RAM. By taking advantage of the constraint-based architecture of COMET™ for local search, we were able to quickly evaluate the impact, for each constraint, on the number of violations resulting from every game removal (or insertion). We have implemented such rather high-level abstraction through the definition of invariants and differentiable objects for the NHL scheduling problem, following the notions described in Van Hentenryck and Michel (2009). 

The subsections that follows describe the experiments that we have conducted in order to set the main parameters of the ALNS and report some results obtained for several instances 

80 

of the problem. In particular, close attention is paid to the choice of a configuration formed by the most promising operators among those proposed in the last section. 

In the preceding chapter (p. 50), we have described our generation of instances for the NHL scheduling problem. In particular, some of those outlined in Table 4.2 will now be used for the calibration phase of the ALNS, and then, results on others will be reported at the end of this chapter. 

At first, we evaluate the schedules generated by our implementation of the procedures proposed in Fleurent (1987). 

# **5.3.1 Constructing initial solutions** 

As mentioned earlier, an initial solution must be provided before starting the ALNS iterations. In order to do so in the case of the NHL scheduling problem, we implemented the heuristic procedures first proposed by Fleurent (1987), which are described in Subsection 5.2.2. 

Table 5.1 _Statistics on initial schedules_ Evaluations on the schedules constructed from scratch by our implementation of Fleurent’s heuristics (described in Subsection 5.2.2) for instances of the 2009-10 and 2010-11 regular seasons (’09 and ’10, respectively). The multi-heuristic approach was applied 16 times for each one of 21 instances per season: one instance with no extra dates, 10 instances with 4 extra dates per team, and 10 instances with 8 extra dates per team. The table shows the minimum ( _min_ ), the arithmetic mean ( _avg_ ), and the maximum ( _max_ ) costs ( _f_ ( _·_ )) and violations (# _viols_ ) for each season (Season) and each number of extra arena dates ( _NExtraDays_ ). 

||Season|_NExtraDays_|_min_|_avg_|_max_|
|---|---|---|---|---|---|
|||0|293 273|348 126_._06|398 654|
||’09|4|89 338|116 250_._95|154 185|
|_f_(_·_)||8|42 772|72 165_._87|109 986|
|||0|267 398|313 694_._07|357 462|
||’10|4|88 255|108 063_._46|144 410|
|||8|38 544|58 483_._27|82 367|
|||0|386|434_._13|494|
||’09|4|369|471_._18|564|
|#_viols_||8|270|349_._71|474|
|||0|348|403_._47|454|
||’10|4|379|446_._86|581|
|||8|226|296_._17|395|



81 

|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|0<br>30<br>60<br>90<br>120<br>150<br>180<br>210<br>240<br>_iols_|Instances with 8 extra dates per team|schedules constructed from scratch<br>|procedure was applied 16 times to|10 instances with 4 extra dates per<br>nstraint C_i_, _i ∈{_1_,_2_, . . . ,_9_}_, and for<br>on the sample solutions summarized<br>ated by the “diamond” shape<br>.|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C1|C2|C3|C4|C5|C6|C7|C8|C9|#_v_|(c)|in the<br>|). The|es, (b) <br>ach co<br>tions <br> illustr|
||||||||||150<br>180<br>210<br>240|ates per team|raint violations <br>|Fleurent (1987|th no extra dat<br>s indicate, for e<br>constraint viola<br>HL schedule is|
||||||||||90<br>120<br>|4 extra d|of const<br>|osed by|ance wi<br>boxplot<br>mber of <br>actual N|
||||||||||60|with|ber <br>|rop|inst<br>he <br> nu<br>ng|
||||||||||0<br>30|ances|Num<br>|rst p|) one <br>am. T<br>n the <br>pondi|
|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|_viols_|Inst|_les_ <br>|es f|(a<br>r te<br>on i<br>rres|
|C1|C2|C3|C4|C5|C6|C7|C8|C9|#|(b)|_schedu_<br>|ocedur|eason:<br>tes pe<br>spersi<br> the co|
||||||||||180<br>210<br>240|dates|_s in initial _<br>|heuristic pr|es of every s<br>h 8 extra da<br> degree of di<br>iolations in|
||||||||||0<br>90<br>120<br>150<br>|with no extra|_aint violation_<br>|ation of the|cted instanc<br>nstances wit<br>nd ’10), the <br> number of v|
||||||||||6|ces|_str_<br>|nt|ele<br>0 i<br>9 a<br>he|
||||||||||30|tan|_on_<br>|me|1 s<br>) 1<br>’0<br> T|
||||||||||0|Ins|_C_<br>|ple|e 2<br> (c<br>n (<br>.1.|
|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|’09<br>’10|_viols_|(a)|5.1 <br>|im|f th<br>and <br>easo<br>ble 5|
|C1|C2|C3|C4|C5|C6|C7|C8|C9|#||Figure<br>|by our|each o<br>team, <br>each s<br>on Ta|



82 

For any instance created as explained in the preceding subsection, our implementation was able to build from scratch a complete schedule by assigning for each team no more than one game per day, but usually resulting in a large number of constraint violations. The whole construction approach can be seen as a two-stage process where violations for the constraints in C _F_ are not allowed during the first stage, except perhaps for C5 (on the minimum number of games per week), and during the second stage, the games that might remain free are sequentially scheduled by now allowing violations for any constraint, except C0. Thus, the first stage of the process is the same as proposed in Fleurent (1987). In both cases, the heuristic procedures are called exactly in the order they are presented in Subsection 5.2.2 (p. 64), which is in accordance with both Fleurent (1987) and Ferland and Fleurent (1991) for the case of the _batch-mode_ (when all games are scheduled without any interaction with the user). Indeed, initially, all free games that individually oppose two distant teams are scheduled at first through the generation of forced trips, which preserves all the arena dates for the respective visiting team, and then, through the generation of free trips, which might sacrifice some of those dates. Subsequently, other free games are scheduled, first to dates that fall on a weekend, and then, to other dates, but never involving any long-distance trip period for the teams in the respective game. And finally, exchange heuristics are used to schedule games that might still remain free. As suggested by Fleurent (1987), the maximum recursive level for the single and for the double exchange heuristics were set to 12 and 3, respectively. 

Typical ranges of costs and total number of constraint violations observed for initial solutions are shown in Table 5.1. In addition, Fig. 5.1 illustrates, with a boxplot for each constraint, the degree of dispersion in the number of violations in the sample solutions that had been summarized in Table 5.1. These results, which evaluate initial schedules for the 2009-10 and 2010-11 seasons, refer to 16 runs of the whole construction process for each instance. A total of 21 instances per season, including the one with no extra dates and those with 4 and with 8 extra dates per team, were used in this experiment. In particular, over a sample of 16 runs for each instance with no extra dates, the number of constraint violations and the cost for individual schedules generated were, in all cases, higher than 340 and 250 000, respectively. 

When compared to the evaluations for the actual NHL schedules from Table 3.2, these results might be very disappointing. Even for our “easiest” instances, which are made up of 8 extra dates per team, all the generated solutions is by far worse than the actual corresponding schedules. In fact, a high number of the most costly constraints (as C1, C2, and C3) is being violated in these cases. 

These results illustrate thus the typical (rather poor) quality of the initial schedule provided to our ALNS. We now evaluate the best-found schedule when varying the number of 

83 

games that a destroy operator removes from the current schedule at each iteration of the algorithm. 

# **5.3.2 Choosing the size of the current solution to destroy** 

Our ALNS algorithm comprises 20 operators, each one having a specific overall goal: 15 of them to partially destroy a complete schedule and the remaining five operators to repair a partial schedule. During each iteration of the algorithm, a destroy operator removes a certain number of games from the current schedule and a repair operator must insert all them back into the schedule. The number of games that a destroy operator is allowed to remove must be provided beforehand and, intuitively, may have a substantial impact on the quality of the solutions produced by the algorithm (as investigated by Pisinger and Ropke, 2007, on variants of the vehicle routing problem, for example). 

In this section, we report the experiments we performed on different number of games being removed by the destroy operators. The algorithm was run with all the available operators being uniformly applied through a fixed number of iterations. In other words, at any iteration, every destroy operator had the same selection probability among the destroy operators (01<sup>**_–_**</sup> , 02<sup>**_–_**</sup> , . . . , 15<sup>**_–_**</sup> ), and every repair operator had the same selection probability among the repair operators (01<sup>**_+_**</sup> , 02<sup>**_+_**</sup> , . . . , 05<sup>**_+_**</sup> ). Hence, the adaptive layer was not used and the approach can be seen as a Large Neighborhood Search (LNS) algorithm, in this case. 

Table 5.2 shows some statistics on the best-found solutions generated by the LNS for 11 instances of the 2010-11 regular season. The algorithm was run 10 times for the hardest instance, with no extra dates, and 5 times for every one of the 10 instances with 8 extra dates per team. For each run, an initial solution was generated from scratch. The table lists the minimum ( _min_ ), the arithmetic mean ( _avg_ ), and the maximum ( _max_ ) costs of the bestfound solutions for each number of games ( _#games_ ) that was individually removed by the 15 destroy operators through 150 000 LNS iterations with all the available operators being uniformly applied. The last 3 rows of the table refer to a random selection, before each LNS iteration, of an integer value in the interval shown in the first column. On the whole, these experiments comprise several quantities of removed games ranging from 10 to 40. 

Unlike the case of the initial solutions from the preceding subsection (see Table 5.1), the evaluations on most of the experimental outcomes in Table 5.2 are somewhat comparable to those of the actual NHL schedule. In particular, when the destroy operators are set to remove 20 games, the costs of the corresponding sample solutions, even for the instance with no extra dates, are lower than the cost (252) of the actual schedule. 

Based on these results, the number of games to be removed by any destroy operator was fixed to 20 for all the other experiments we report in this chapter. 

84 

Table 5.2 _Results on different number of games being removed per LNS iteration_ Evaluations on the best-found solutions generated by our LNS for 11 instances of the 2010-11 regular season. The algorithm was run 10 times for the hardest instance, with no extra dates, and 5 times for every one of the 10 instances with 8 extra dates per team. The table shows the minimum ( _min_ ), the arithmetic mean ( _avg_ ), and the maximum ( _max_ ) costs of the best-found solutions for each number of games ( _#games_ ) removed by any one of the 15 destroy operators through 150 000 LNS iterations with all the available operators being uniformly applied. The last 3 rows of the table refer to a random selection, before each LNS iteration, of an integer value in the interval shown in the column. 

||N|o extra da|tes|8 e|xtra da|tes|
|---|---|---|---|---|---|---|
|_#games_|_min_|_avg_|_max_|_min_|_avg_|_max_|
|10|1 470|7 522_._80|21 525|0|0_._38|3|
|15|269|694_._80|1 285|0|0_._28|2|
|18|161|234_._00|273|0|0_._36|2|
|20|130|**165****_._75**|214|0|**0****_._26**|2|
|25|133|204_._00|264|0|0_._50|2|
|30|121|186_._60|283|0|0_._84|4|
|40|191|330_._25|424|0|2_._66|7|
|16-24|211|238_._00|260|0|0_._44|2|
|18-26|199|236_._80|299|0|0_._44|2|
|20-28|162|229_._00|321|0|0_._34|3|



The implementation of the ALNS admits several different choices of algorithm control parameters. In the following subsections, we highlight the main computational experiments performed when calibrating the algorithm. 

# **5.3.3 Setting the ALNS parameters** 

The parameters to be provided to the master level of our ALNS algorithm (see Appendix A.1) are the maximum number of iterations, _Kalns_<sup>_max_;thesegmentsize,</sup><sup>_Kseg_;thestart</sup> temperature control parameter, _τ_ ; the score adjustment parameters, _σbes_ , _σbet_ , and _σacc_ ; the reaction factor, _ρ_ ; the set of destroy operators, _I_<sup>_−_</sup> , and the set of repair operators, _J_<sup>+</sup> , with their respective initial weights, _ωo ∀o ∈ I_<sup>_−_</sup> _∪ J_<sup>+</sup> . There are evidences, both from preliminary results and from the literature, that the values for most of those parameters are generalizable to different instances and, in some cases, even to different problems. Indeed, Ropke and Pisinger (2006), for example, obtained remarkable results for several variants of vehicle routing problems with the same post-tuning values of parameters. 

85 

The overall strategy we use here to set the ALNS parameters is the same as that of Ropke and Pisinger (2006). Initially, we have identified an initial setting, and then, one parameter at time was modified while keeping the others fixed, and the modification leading to solutions with the best average cost was chosen for the subsequent parameter adjustments. 

The computational experiments reported in the course of this subsection were individually carried out by applying the ALNS eight times to each tuning instance. The cost, and occasionally the number of constraint violations, for the corresponding best-found schedules will be summarized by their minimum ( _min_ ), arithmetic mean ( _mean_ ), and maximum ( _max_ ) values. In most cases, those values will be graphically depicted as _boxplots_ , which also includes the lower quartile, the median, and the upper quartile. The setting of parameters will always be based on the average costs of the best-found schedules. So, for each experiment, the setting corresponding to the smallest average cost will be chosen. 

# **Tuning instances and initial solutions** 

The results in Table 5.1 show that our implementation of the approach by Fleurent (1987) constructs initial solutions that have a rather wide range of values. However, preliminary results that we have obtained while implementing the ALNS (including those from the preceding experiment) showed no relation between the quality of the initial solution and the quality of the best-found solution (even considering just as few as 10 000 iterations). Also during the developing phase, our tests provided compelling evidence that different runs of the ALNS for the same instance and starting at the same initial solution will mostly produce (best-found) schedules with slightly distinct values. We have then decided to select only nine instances for all the experiments in this section. They were, however, carefully chosen as to represent different levels of difficulties. In fact, our choice consists of one instance with no extra dates, four instances with four extra dates per team, and four instances with eight extra dates per team. To be more precise, the tuning instances that we selected are the following: `NHL10-0a` , and for each _γ ∈{_ `a` _,_ `b` _,_ `f` _,_ `g` _}_ , `NHL10-4` _γ_ and `NHL10-8` _γ_ , all them referring to the 2010-11 regular season. In addition, the same initial solution associated with every instance was provided to the experiments. The initial solutions were chosen among those evaluated in Subsection 5.3.1 as to have their respective costs close to the corresponding _mean_ value in Table 5.1. Obviously, this choice of solutions is intended to represent a typical initial schedule generated by our implementation. The overall idea is to keep the different tuning steps under the same circumstances regarding both the tuning instances and the initial solutions. 

86 

# **Solution acceptance and stopping criteria** 

As mentioned in Subsection 5.2.1, our ALNS algorithm iterates until either a schedule _Scurr_ with no violation of constraints is generated or a given maximum number of iterations, _Kalns_<sup>_max_,</sup> is attained. Because of the strategic nature of the NHL scheduling problem, computational time is not a major issue. So, after a number of _ad hoc_ experiments performed during the development phase, we have chosen to set _Kalns_<sup>_max_to150 000iterations,whichallowedusto</sup> obtain all results we report in the remainder of this chapter in no more than 195 minutes (3.25 hours) for each run of the algorithm. 

The acceptance criteria we use are those from Simulated Annealing. Therefore, the new (temporary) solution, _Stemp_ , obtained during an iteration _k_ of the ALNS is accepted whenever its cost, _f_ ( _Stemp_ ), is not worse than the cost, _f_ ( _Scurr_ ), of the current solution, _Scurr_ ; and otherwise, the new solution is accepted with a probability that is exponentially proportional to the quotient of the corresponding increase in the cost, _f_ ( _Stemp_ ) _− f_ ( _Scurr_ ), and the current value of the temperature parameter, _Tk_ . As in Ropke and Pisinger (2006), we systematically decrease the temperature at every single iteration of the ALNS. Indeed, the temperature is slightly decreased by using the cooling schedule _Tk_ +1 = _c Tk_ with a constant cooling factor, _c_ , that is close to 1.0. However, instead of following the strategy by Ropke and Pisinger (2006), which provides the cooling factor as a parameter, we set it to a value such that, at the last ALNS iteration, a temporary solution one unit worse than the current solution would have only 1% of chance of being accepted. So we set the constant _c_ to ( _T_ 0 ( _−_ ln(0 _._ 01)))<sup>(</sup><sup>_−_1</sup><sup>_/K_</sup> _alns_<sup>_max_)</sup> , where _T_ 0 is the initial temperature. This, in turn, is computed as ( _τ/_ 100)( _f_<sup>ˆ</sup> ( _Sinit_ ) _/_ ( _−_ ln(0 _._ 5))), where _τ_ is the start temperature control parameter provided to the ALNS and _f_<sup>ˆ</sup> ( _Sinit_ ) is the weighted sum<sup>�9</sup> _i_ =3<sup>_wifi_(</sup><sup>_Sinit_)ofthenumberofviolations,</sup> _fi_ ( _Sinit_ ), of every constraint C _i_ , for _i ∈{_ 3 _,_ 4 _, . . . ,_ 9 _}_ , in the initial solution, _Sinit_ . For all the experiments, we have chosen to set _τ_ = 5 _._ 0. Therefore, if _Stemp_ is the new (temporary) solution at the beginning of the ALNS and _Stemp_ induces a cost increasing _f_ ( _Stemp_ ) _− f_ ( _Sinit_ ) that is equal to 5% of the “modified cost” _f_<sup>ˆ</sup> ( _Sinit_ ) then _Stemp_ is accepted (to become the new _Scurr_ ) with probability 0.5. The cooling factor in our experiments have always been into the range from 0.999954 to 0.999958, which as expected, results in a slower decrease of the temperature through the ALNS iterations than in the case reported by Ropke and Pisinger (2006), where the cooling rate was set to 0.999750 and the algorithm was run for no more than 25 000 iterations. 

We now evaluate the effectiveness of the 20 operators that we proposed in the subsections 5.2.3 and 5.2.4. 

87 

# **Screening the proposed operators** 

As mentioned earlier, Pisinger and Ropke (2007) state that, when developing an ALNS, the choice between a number of possible operators is not a matter of “either-or” but rather “both-and”. Indeed, Ropke and Pisinger (2006) claim that the more (reasonable) operators are provided to their ALNS, the better it performs. However, the literature that follows the same ALNS framework usually reports to apply much fewer operators that we are proposing in this thesis. Our main goal now is, thus, to systematically examine the performance of our ALNS over different configurations for the 20 operators that we have described earlier. In particular, we try to identify a subset of those operators that will, hopefully, outperforms the 20-operator configuration. We also compare the adaptive version of the approach (ALNS) with its static version (LNS), where each operator has a fixed selection probability through the iterations of the search. 

For the experiments on the ALNS, we have set the parameters for the adaptive layer as ( _Kseg, σbes, σbet, σacc, ρ_ ) = (200 _,_ 7 _,_ 3 _,_ 1 _,_ 0 _._ 1), which was based on preliminary results. The values for the score adjustment parameters are then in line with Pisinger and Ropke (2010) as the condition _σbes ≥ σbet ≥ σacc ≥_ 0 holds. This is based upon the rationale that _σbes_ , _σbet_ , and _σacc_ are respectively associated to conditions that are arranged in decreasing order of preference with regard to the quality of the new solution. For example, if it is the case that the solution generated during an ALNS iteration is a (so far) best solution, then the increase _σbes_ in the scores of the corresponding destroy and repair operators are higher than it would be for any other case. 

Ideally, the design of an ALNS algorithm involves both operators that succeed in providing either diversification or intensification through the search. As it is the case in Ropke and Pisinger (2006), the literature on ALNS often proposes operators that individually tends to be very imprecise heuristics, even so, they are able to produce outstanding results when appropriately integrated into an ALNS framework. 

Here, we screen our operators in a subtractive manner where, starting from a configuration with all the 20 operators being provided, some apparently less effective operators are excluded through successive computational experiments. Because the number of destroy operators proposed in this thesis is relatively high, we first try to identify (and exclude) more than one operator at time, so as to speed up the process. In fact, by keeping track of the adapted selection probability of each operator through the ALNS iterations, and then by excluding the three lowest-scored operators at once, we were able to reduce the number of destroy operators from 15 to only six operators and yet obtain solutions with better average cost for the tuning instances. 

To be more precise, the first phase of this screening process was based on the range 

88 



<!-- Start of picture text -->
01 – 01 – 01 –<br>02 – 02 – 02 –<br>03 – 03 – 03 –<br>04 – 04 – 04 –<br>05 – 05 – 05 –<br>06 – 06 – 06 –<br>07 – 07 – 07 –<br>08 – 08 – 08 –<br>09 – 09 – 09 –<br>10 – 10 – 10 –<br>11 – 11 – 11 –<br>12 – 12 – 12 –<br>13 – 13 – 13 –<br>14 – 14 – 14 –<br>15 – 15 – 15 –<br>(%) 0 5 10 15 20 25 (%) 0 5 10 15 20 25 (%) 0 5 10 15 20 25<br>(a) All 15 destroy operators (b) Only 12 destroy operators (c) Only 9 destroy operators<br><!-- End of picture text -->

Figure 5.2 _Selection probabilities for each destroy operator through the ALNS iterations_ Statistics on the values of the adapted selection probabilities which was tracked at the end of every 10 000 ALNS iterations. All the 5 repair operators are available, and three configurations of destroy operators are individually investigated. In the case (a), all 15 destroy operators are available. In the case (b), only 12 destroy operators are available (operators 03<sup>**_–_**</sup> , 09<sup>**_–_**</sup> , and 12<sup>**_–_**</sup> had been excluded). And in the case (c), only 9 destroy operators are available (operators 04<sup>**_–_**</sup> , 13<sup>**_–_**</sup> , and 15<sup>**_–_**</sup> had also been excluded). For each case, the ALNS was applied 8 times to 9 instances of the 2010-11 regular season: one instance with no extra dates, 4 instances with 4 extra dates per team and other 4 instances with 8 extra dates per team. Thus, the boxplots indicate, for each operator, the degree of dispersion in the selection probabilities tracked at every 10 000 iterations over 72 runs (8 runs _×_ 9 instances) of 150 000 iterations of the ALNS algorithm. 

of selection probabilities that are illustrated in the three charts (a, b, and c) of Fig. 5.2 (p. 88). This figure summarizes, in a boxplot for each destroy operator, the range of values of the adapted selection probabilities tracked at the end of every 10 000 ALNS iterations. At the first iteration, in all cases, the same selection probability had been assigned to all the destroy operators available for the respective experiment. The ALNS was run eight times on each tuning instance for at most 150 000 iterations, and during the search, the available operators were individually selected according to their respective earned scores. To be more precise, the Fig. 5.2a refers to the experiment where the initial weight parameters for the operators were set as _ωo_ = 1 _∀o ∈ I_<sup>_−_</sup> _∪ J_<sup>+</sup> , and thus, any destroy operator and any repair operator started with 6 _._ 67% and 20% of chance of being selected, respectively. As can be seen from Fig. 5.2a, all selection probabilities turned out to be under 25% for the destroy operators. On the other hand, these results seem to indicate that some destroy operators did not substantially contribute to the generation of good solutions through the search. So, based in Fig. 5.2a, we decided to exclude the operators 03<sup>**_–_**</sup> , 09<sup>**_–_**</sup> , and 12<sup>**_–_**</sup> , which are the three destroy operators with the worst average selection probabilities: 2 _._ 99%, 4 _._ 26%, and 

89 

1 _._ 18%, respectively (far below their initial chance of being selected, 6 _._ 67%). Fig. 5.2b refers to the experiment with only 12 destroy operators and initial weight parameters set as _ωo_ = 0 _∀o ∈ I_<sup>˜</sup> 3<sup>_−_</sup> = _{_ 03<sup>**_–_**</sup> _,_ 09<sup>**_–_**</sup> _,_ 12<sup>**_–_**</sup> _}_ , and _ωo_ = 1 _∀o ∈ J_<sup>+</sup> _∪ I_ 12<sup>_−_,with</sup><sup>_I_</sup> 12<sup>_−_=</sup><sup>_I−\I_˜</sup> 3<sup>_−_.Asinthe</sup> preceding case, we inspected the probabilities in Fig. 5.2b and then excluded still the new three worst average-scored operators, which are the operators 04<sup>**_–_**</sup> , 13<sup>**_–_**</sup> , and 15<sup>**_–_**</sup> (with average selection probabilities of 6 _._ 08%, 4 _._ 55%, and 6 _._ 25%, respectively). Next, we proceeded with the experiment involving only nine destroy operators and the initial weight parameters set as _ωo_ = 0 _∀o ∈ I_<sup>˜</sup> 6<sup>_−_=</sup><sup>_I_˜</sup> 3<sup>_−∪{_04</sup><sup>**_–_**</sup><sup>_,_13</sup><sup>**_–_**</sup><sup>_,_15</sup><sup>**_–_**</sup><sup>_}_,and</sup><sup>_ωo_=1</sup><sup>_∀o∈J_+</sup><sup>_∪I_</sup> 9<sup>_−_,with</sup><sup>_I_</sup> 9<sup>_−_=</sup><sup>_I−\I_˜</sup> 6<sup>_−_.</sup> For this case, the boxplots on the selection probabilities are given in Fig. 5.2c. One more time, we excluded the three worst average-scored destroy operators, 10<sup>**_–_**</sup> , 11<sup>**_–_**</sup> , and 14<sup>**_–_**</sup> (with average selection probabilities of 7 _._ 56%, 9 _._ 34%, and 8 _._ 64%, respectively). The experiments on the remaining six destroy operators resulted in a rather more uniform dispersion of the adapted selection probabilities, which does not provide a reasonable evidence for identifying any particularly underperforming operator. 

Our criterion on excluding those nine destroy operators, and thus reducing their number from 15 to only six operators, was completely based on the adapted selection probabilities that were sampled through the ALNS iterations. So it is certainly plausible that we now evaluate the quality of the solutions generated by the experiments in each of the preceding cases. We summarize the cost of the best-found solutions for the experiments on 15, 12, 9, and 6 available destroy operators on the top of Fig. 5.3 with the labels _I_<sup>_−_</sup> , _I_ 12<sup>_−_,</sup><sup>_I_</sup> 9<sup>_−_,and</sup> _I_ 6<sup>_−_,respectively.TheresultsinFig.5.3(p.98)arearranged,fromthetoptothebottom,</sup> in the order that the experiments were conducted and they are divided into two charts (a and b) each one referring to a particular number of extra dates (0 and 4, respectively) in the tuning instances. The instances with 8 extra dates per team (for which no results are reported in Fig. 5.3) were generally solved to optimality by all the configurations we are describing here. On the whole, the configuration with the 15 destroy operators ( _I_<sup>_−_</sup> ) were only fully outperformed (with regard to the average cost) by the configuration with six destroy operators ( _I_ 6<sup>_−_).Inparticular,thetoppartofFig.5.3showsthattheaveragecostofthe</sup> solutions produced by the configuration with 12 operators ( _I_ 12<sup>_−_) are the worst among the four</sup> preceding experiments. In addition, while the 6-operator configuration ( _I_ 6<sup>_−_)resultedinthe</sup> lowest average cost on every number of extra dates, the ALNS is apparently more robust for the hardest instance, with no extra dates (Fig. 5.3a), when all the 15 destroy operators are provided to the algorithm. 

At this point of our search for a good configuration of the operators, the best averagecost solutions had then been produced by the configuration with six destroy operators, _I_ 6<sup>_−_=</sup> _{_ 01<sup>**_–_**</sup> _,_ 02<sup>**_–_**</sup> _,_ 05<sup>**_–_**</sup> _,_ 06<sup>**_–_**</sup> _,_ 07<sup>**_–_**</sup> _,_ 08<sup>**_–_**</sup> _}_ , and all the five repair operators, _J_<sup>+</sup> = _{_ 01<sup>**_+_**</sup> _,_ 02<sup>**_+_**</sup> _,_ 03<sup>**_+_**</sup> _,_ 04<sup>**_+_**</sup> _,_ 05<sup>**_+_**</sup> _}_ . 

90 

We aim now to evaluate yet another number of configurations in a subtractive manner that exclude one operator at time and choose the configuration resulting in the best average cost, until no improvement is obtained with this process. 

The boxplots labeled by _I_ 6<sup>_−\{o−}_, with every</sup><sup>_o−∈I_</sup> 6<sup>_−_, in Fig. 5.3 illustrate the dispersion</sup> in the cost of the best-found solutions when the destroy operator _o_<sup>_−_</sup> is not provided to the ALNS but only the other five operators in _I_ 6<sup>_−_.Thecorrespondingresultsshowthatthe</sup> experiment where the operator 07<sup>**_–_**</sup> was not available was the one to provide solutions with the lowest average cost to the tuning instances. In fact, the configuration with _I_ 5<sup>_−_=</sup><sup>_I_</sup> 6<sup>_−\{_07</sup><sup>**_–_**</sup><sup>_}_</sup> provided the (so far) best solutions, compared to the previous experiments. In addition, these results provide compelling evidence that among the operators in _I_ 6<sup>_−_,thepresenceofthe</sup> operators 01<sup>**_–_**</sup> , 02<sup>**_–_**</sup> , and 06<sup>**_–_**</sup> was particularly important in producing better overall solutions. In the same way, the boxplots labeled by _I_ 5<sup>_−\{o−}_, with every</sup><sup>_o−∈I_</sup> 5<sup>_−_, in Fig. 5.3 summarize</sup> the quality of the best-found solutions when the destroy operator _o_<sup>_−_</sup> was not provided to the ALNS. In this case, despite the rather good overall results on excluding the operator 08<sup>**_–_**</sup> , no average cost in this experiment turned out to be better than the one from our preceding choice, with _I_ 5<sup>_−_=</sup><sup>_{_01</sup><sup>**_–_**</sup><sup>_,_02</sup><sup>**_–_**</sup><sup>_,_05</sup><sup>**_–_**</sup><sup>_,_06</sup><sup>**_–_**</sup><sup>_,_08</sup><sup>**_–_**</sup><sup>_}_.Contrarytowhatmighthavebeenexpected,</sup> this “best” configuration of destroy operators does not include any of the critical removals (10<sup>**_–_**</sup> ,11<sup>**_–_**</sup> ,12<sup>**_–_**</sup> ). In fact, it is rather surprising that a configuration made up of operators among the most naive ones that we have proposed turned out to be the configuration to provide the best average results. Apparently, this could be attributed both to the greedy-based strategy that evaluates the target assignments before cancelling only the “worst” of them and to the relatedness of the target assignments defined by the selection criterion of the other operators (except the random-based removal 01<sup>**_–_**</sup> ). 

We then evaluated, in the same subtractive manner, the repair operators. As for the destroy operators, they remained unchanged: only the five operators in _I_ 5<sup>_−_wereprovided,</sup> all them with the same initial weight. The results indicated by a label _J_<sup>+</sup> _\ {o_<sup>+</sup> _}_ , with every _o_<sup>+</sup> _∈ J_<sup>+</sup> , in Fig. 5.3 summarize the costs of the best-found solutions when the repair operator _o_<sup>+</sup> was not provided to the ALNS but only the other four operators in _J_<sup>+</sup> . As can be seen, a better average cost were obtained by the exclusion of the repair operator 01<sup>**_+_**</sup> . The subsequent experiments, indicated by _J_ 4<sup>+</sup><sup>_\ {o_+</sup><sup>_}_,withevery</sup><sup>_o_+</sup><sup>_∈J_</sup> 4<sup>+,showthatno</sup> further single exclusion of repair operators resulted in a more effective configuration than the preceding choice, with _J_ 4<sup>+=</sup><sup>_{_02</sup><sup>**_+_**</sup><sup>_,_03</sup><sup>**_+_**</sup><sup>_,_04</sup><sup>**_+_**</sup><sup>_,_05</sup><sup>**_+_**</sup><sup>_}_.</sup> 

Therefore, based on the strategy we have adopted, our choice of operators for all the experiments that follows is given by _I_ 5<sup>_−_</sup> = _{_ 01<sup>**_–_**</sup> _,_ 02<sup>**_–_**</sup> _,_ 05<sup>**_–_**</sup> _,_ 06<sup>**_–_**</sup> _,_ 08<sup>**_–_**</sup> _}_ as the set of destroy operators and _J_ 4<sup>+</sup> = _{_ 02<sup>**_+_**</sup> _,_ 03<sup>**_+_**</sup> _,_ 04<sup>**_+_**</sup> _,_ 05<sup>**_+_**</sup> _}_ as the set of repair operators provided to the algorithm. 

91 

The three experiments reported at the bottom of Fig. 5.3 refer to the evaluation for nonadaptive versions of the algorithm (LNS), where the selection probabilities were individually fixed through the search, and only the preceding choice of operators, _I_ 5<sup>_−∪J_</sup> 4<sup>+, were provided.</sup> Indeed, for the results labeled by _uniform_ , the same weight had been assigned to all the operators in _I_ 5<sup>_−∪J_</sup> 4<sup>+,sothat,foreachiteration,thechanceofeverydestroyoperatorand</sup> every repair operator to be selected was 20% and 25%, respectively. For the other two cases, the setting of selection probabilities was based on statistics for the adapted probabilities from the previous best configuration (labeled by _J_ 4<sup>+inFig.5.3).Infact,intheexperiments</sup> indicated by _avg10K_ and by _avgklast_ , the selection probabilities were set as the average of the corresponding adapted probability that had been tracked respectively at all 10 000-iteration blocks and at the last iteration alone. These adapted probabilities are illustrated in Fig. 5.4 both for _all_ 10 000-iteration blocks (labeled by _A_ ) and for the _last_ ALNS iteration alone (labeled by _L_ ). We observe from Fig. 5.4 that a quite small dispersion had occurred on the adapted selection probabilities of most operators in the (so far) best configuration. It could then be speculated that the average upon those probabilities for each operator would be the ideal choice for the respective selection probabilities through all the iterations of the algorithm. However, inspection of Fig. 5.3 indicates that neither _avg10K_ nor _avgklast_ was able to fully outperform the configuration used in _J_ 4<sup>+.Consequently, regarding the average cost of</sup> the best-found solutions, these results reinforce the overall superiority of the adaptive version (ALNS) over the static version (LNS) of our algorithm for the NHL scheduling problem. 

In all the next experiments, we have then decided to apply the adaptive version of the algorithm (ALNS) with only the operators in _I_ 5<sup>_−∪J_</sup> 4<sup>+beingprovided,whereinthecourse</sup> of the first iterations (first segment), every destroy operator and every repair operator are selected with 20% and 25% of chance, respectively. 

# **Adjustment of selection probabilities** 

As described earlier, the selection probabilities for the operators in our ALNS are adjusted though the search according to the following five parameters: the segment size, _Kseg_ , that defines the number of ALNS iterations during which scores are added up for each operator; the score adjustment parameters, _σbes_ , _σbet_ , and _σacc_ , that stipulate, at the end of each iteration, the different degrees of “rewards” for the performance of the operators according to the type of new-found solution ( _best_ , _better_ , _accepted_ , respectively); and the reaction factor, _ρ_ , that specifies, at the begin of a new segment, how sensitive the updating of any operator weight must be to the corresponding score gathered during the preceding segment. We now report the experiments that we have conducted on evaluating different settings for those parameters. 

Ou strategy can be divided into two parts as follows. At first, we kept the same reaction 

92 

Table 5.3 _Best-found solutions on different parameters settings for the ALNS_ Statistics on the cost of the best-found solution over 150 000 ALNS iterations for three cases of score adjustment parameters, _σ_ = ( _σbes, σbet, σacc, σrej_ ), three cases of reaction factor, _ρ_ , and three cases of segment size, _Kseg_ . Only 5 destroy operators (01<sup>**_–_**</sup> , 02<sup>**_–_**</sup> , 05<sup>**_–_**</sup> , 06<sup>**_–_**</sup> , and 08<sup>**_–_**</sup> ) and 4 repair operators (02<sup>**_+_**</sup> , 03<sup>**_+_**</sup> , 04<sup>**_+_**</sup> , and 05<sup>**_+_**</sup> ) were provided. The ALNS was applied 8 times to 9 instances of the 2010-11 season, which are investigated by number of extra dates: one instance with no extra dates; 4 instances with 4 extra dates per team; and other 4 instances with 8 extra dates per team. The table shows, for each number of extra dates, the minimum ( _min_ ), the arithmetic mean ( _avg_ ), and the maximum ( _max_ ) best-found values over 72 runs (8 runs _×_ 9 instances) of the ALNS with the corresponding setting of parameters. For each instance, the same initial solution was provided. 

|||||||In|stances|||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|ALNS para|meter|s|no|extra da|tes|4 e|xtra da|tes|8 e|xtra d|ates|
|(_σbes, σbet, σacc_)|_ρ_|_Kseg_|_min_|_avg_|_max_|_min_|_avg_|_max_|_min_|_avg_|_max_|
|33913|01|100|66|116_._70|184|0|1_._20|4|0|0_._10|1|
|(_,_ _,_)|_._|200|59|104_._30|146|0|1_._50|6|0|0_._05|1|
|(33139)|01|100|79|96_._00|120|0|1_._30|3|0|0_._05|1|
|_,_ _,_|_._|200|65|91_._50|122|0|0_._95|3|0|0_._00|0|
|||100|79|99_._80|132|0|0_._95|3|0|0_._10|1|
||0_._1|200|49|89_._50|118|0|0_._90|2|0|0_._00|0|
|||400|55|93_._10|144|0|0_._90|3|0|0_._05|1|
|||100|57|94_._50|149|0|1_._30|3|0|0_._00|0|
|(7_,_3_,_1)|0_._3|200|44|93_._60|136|0|0_._95|4|0|0_._05|1|
|||400|64|93_._10|129|0|0_._75|2|0|0_._00|0|
|||100|63|99_._30|139|0|1_._25|3|0|0_._05|1|
||0_._5|200|54|93_._60|134|0|1_._15|4|0|0_._00|0|
|||400|61|102_._90|147|0|1_._15|3|0|0_._05|1|



factor as before, _ρ_ = 0 _._ 1, while evaluating all combinations of two cases for the segment size, _Kseg_<sup>_(1)_=100and</sup><sup>_K_</sup> _seg_<sup>_(2)_=200,andthreecasesforthevectorofscoreadjustmentparameters,</sup> _σ_<sup>_(1)_</sup> = (33 _,_ 9 _,_ 13), _σ_<sup>_(2)_</sup> = (33 _,_ 13 _,_ 9), and _σ_<sup>_(3)_</sup> = (7 _,_ 3 _,_ 1). Next, we kept the best among those options for score adjustment parameters, while evaluating all combinations of three cases for the reaction factor, _ρ_<sup>_(1)_</sup> = 0 _._ 1, _ρ_<sup>_(2)_</sup> = 0 _._ 3, and _ρ_<sup>_(3)_</sup> = 0 _._ 5, and also three cases for the segment size, _Kseg_<sup>_(1)_= 100,</sup><sup>_K_</sup> _seg_<sup>_(2)_= 200,and</sup><sup>_K_</sup> _seg_<sup>_(3)_= 400.</sup> 

The settings _σ_<sup>_(1)_</sup> , _ρ_<sup>_(1)_</sup> , and _Kseg_<sup>_(1)_arethosefromRopkeandPisinger(2006),whichin</sup> particular, somewhat unexpectedly, attribute a higher score increment (13) to “worse” new- 

93 

accepted solutions than (9) to new solutions that are “better” with regard to the current solution. Because the setting _σ_<sup>_(1)_</sup> is not fully consistent with the condition _σbes ≥ σbet ≥ σacc ≥_ 0 suggested in Pisinger and Ropke (2010) we are then including the setting _σ_<sup>_(2)_</sup> into our evalutions. Comparing to our implementation, there is however, one particularity to the adjustments of scores in Ropke and Pisinger (2006): both _σbet_<sup>_(1)_and</sup><sup>_σ_</sup> _acc_<sup>_(1)_areonlyused</sup> for cases where the new solution has not been accepted before. As mentioned earlier, the settings _σ_<sup>_(3)_</sup> and _Kseg_<sup>_(2)_, which we have used for previous experiments in this thesis, were based</sup> in preliminary results obtained during the implementation of our approach. In addition, _ρ_<sup>_(2)_</sup> and _ρ_<sup>_(3)_</sup> , as well as _Kseg_<sup>_(1)_and</sup><sup>_K_</sup> _seg_<sup>_(3)_,werethoughtasbeingreasonablechoicestoevaluatethe</sup> impact of a relatively small, medium, and large values for those parameters in the quality of the best-found solutions. 

Table 5.3 summarizes the results on those experiments, which are divided by number of extra dates in the respective tuning instances. On the whole, the results does not seem to indicate any particular overall outstanding setting among those we are evaluating. In fact, Table 5.3 seems to suggest that our ALNS for the NHL scheduling problem is not very sensitive to the choice of adjustment parameters. Comparing the results on _σ_<sup>_(1)_</sup> and _σ_<sup>_(2)_</sup> , however, provides some evidence that, contrary to the case in Ropke and Pisinger (2006), attributing decreasing rewards respectively to _best_ , _better_ , and _accepted_ new solutions is quite more effective in our approach for the NHL scheduling problem. 

Table 5.3 also shows that, regarding the hardest instance (with no extra dates), our initial setting ( _σ_<sup>_(3)_</sup> , _ρ_<sup>_(1)_</sup> , and _Kseg_<sup>_(2)_)resultedinthelowestaveragecost(89</sup><sup>_._5)andthesecondlowest</sup> overall cost (49) for the best-found solutions. In addition, that setting solved to optimality all tuning instances with 8 extra dates per team. 

Therefore, we decided to keep the parameters on the adjustment of selection probabilities as 



for the results on other instances, which are reported in the following subsection. 

# **5.3.4 Solving other instances** 

We now report the results obtained by applying the ALNS algorithm to the _entire-league_ instances described in Subsection 4.3.2 (p. 50). The parameters on the master level of the algorithm were set as follows: ( _σbes, σbet, σacc_ ) = (7 _,_ 3 _,_ 1) for the adjustment of operator scores; _ρ_ = 0 _._ 1 for the reaction factor; _Kseg_ = 200 for the segment size; and _Kalns_<sup>_max_= 150 000forthe</sup> maximum number of ALNS iterations. Only five destroy operators (01<sup>**_–_**</sup> , 02<sup>**_–_**</sup> , 05<sup>**_–_**</sup> , 06<sup>**_–_**</sup> , and 08<sup>**_–_**</sup> ) and four repair operators (02<sup>**_+_**</sup> , 03<sup>**_+_**</sup> , 04<sup>**_+_**</sup> , and 05<sup>**_+_**</sup> ) were provided, and an initial schedule 

94 

Table 5.4 _Best-found solutions for instances with extra arena-available dates_ Statistics on the cost of the best-found solution over 150 000 ALNS iterations when the initial solution is built from scratch. The results refer to 10 instances ( `a` _,_ `b` _, . . . ,_ `j` ) on two and on four extra arena-available dates per team for the 2010-11 season. The table shows, for each instance, the minimum ( _min_ ), the arithmetic mean ( _avg_ ), and the maximum ( _max_ ) best-found costs over 8 runs of the ALNS algorithm. Instances with either 6 or 8 extra arena dates per team were all solved to optimality (with no constraint violations). 

|||2 e|xtra da|tes|4 e|xtra d|ates|
|---|---|---|---|---|---|---|---|
|_α_|_γ_|_min_|_avg_|_max_|_min_|_avg_|_max_|
|2 010|`a`|1|1_._25|3|0|0_._38|1|
||`b`|1|1_._75|2|0|0_._38|1|
||`c`|1|2_._75|4|0|0_._38|1|
||`d`|0|1_._50|3|0|0_._25|1|
||`e`|1|2_._00|3|0|0_._13|1|
||`f`|0|2_._88|4|0|0_._63|1|
||`g`|1|3_._00|5|0|1_._00|2|
||`h`|0|1_._38|4|0|0_._63|2|
||`i`|0|2_._63|6|0|0_._63|1|
||`j`|2|3_._00|4|0|0_._25|1|
||_all_|0|2_._21|6|0|0_._46|2|



was generated from scratch for each run of the algorithm. 

As mentioned in Chapter 3, the arena availability is by far the most critical factor in the construction of schedules for the NHL regular season. It is then logical to assume that, in particular, the less extra dates an instance has, the more difficult it is to find a high-quality schedule for it. This would suggest that even our “easiest” instances (with 8 extra dates per team) are substantially more difficult to solve than those addressed either by Fleurent (1987) or by Costa (1995), where the instances are reported to have at least 15 extra arena dates per team. On the other hand, because no further information about the instances addressed in those works is available, we believe that any attempt to rigorously compare those instances with ours would be rather misleading. In fact, it may happen that the difficulty of our instances are somewhat attenuated by the fact of having been generated from an alreadyknown fairly good solution: the corresponding actual NHL schedule. 

Tables 5.4 and 5.5 present some statistics on the cost of the best-found solution in our computational experiments for the 2010-11 season, which turns out to fairly represent the typical solutions our ALNS have provided on the entire-league instances. 

95 

Table 5.5 _Typical results for instances without extra dates_ Statistics on the constraint violations and on the costs of the best-found solution over 150 000 ALNS iterations when the initial solution is built from scratch. The results refer to the instance `NHL10-00a` of the 201011 regular season with no extra arena-available dates. The table shows the minimum ( _min_ ), the arithmetic mean ( _avg_ ), and the maximum ( _max_ ) number of constraint violations ( _ctr_ ) and costs ( _f_ ( _·_ )) on the best-found solutions over 8 runs of the ALNS algorithm. Constraint violations and cost are also show for the corresponding actual NHL schedule ( _NHL’_ ). 

|_α_|_ctr_|_min_|_avg_|_max_|_NHL’_|
|---|---|---|---|---|---|
|2 010|C1|0|0_._00|0|0|
||C2|0|0_._00|0|0|
||C3|0|0_._13|1|3|
||C4|4|7_._38|10|14|
||C5|0|0_._13|1|16|
||C6|6|10_._00|19|66|
||C7|0|0_._00|0|0|
||C8|0|0_._00|0|0|
||C9|0|0_._25|1|0|
||_#viols_|10|17_._88|27|99|
||_f_(_·_)|46|85_._38|120|252|



The results are divided into two parts as follows: Table 5.4 refers to the instances with extra arena dates, and Table 5.5 refers to the instances where only the 41 home dates in the corresponding actual NHL schedule were provided. In particular, Table 5.5 also presents the number of violations for each constraint of the problem, regarding both the solutions provided by the ALNS algorithm and the respective actual NHL schedules. 

On the whole, the results reinforce the importance of having extra arena dates in order for our ALNS to find, within the considered number of iterations, NHL schedules that violate no constraints of the problem. Indeed, all the instances with either 6 or 8 extra arena dates per team (which it is not shown in the tables) were solved to optimality (with no constraint violations). Moreover, the statistics on this sample of eight schedules per instance for the 2010-11 season show that the numbers of violations are on average only 2.21 and 0.46 for the cases where each team provided 2 and 4 extra arena dates, respectively. 

It is important to notice that the violations reported in Table 5.4 can only refer to the “cheapest”constraints, to which we have set a one-unit penalty weight (or cost) per violation. 

When only the minimum number of arena dates (41) is provided by each team, table 5.5 shows, however, that the number of violations in the schedules generated by the ALNS 

96 

algorithm ranges from 10 to 27, with cost varying between 46 and 120. Although these violations and costs are worse (higher) than those for the other instances (Table 5.4), they are significantly better (lower) than the violations (99) and the cost (252) for the actual 2010-11 NHL schedule. Interestingly, the algorithm was thus able to reschedule the games on the same arena dates that had actually been used by every team and yet violates much fewer constraints of the problem. 

As shown by Table 5.6, similar comparative remarks could be drawn about the results for the instances of other seasons. In particular, however, some schedules have presented slightly more violations than those for the 2010-11 season. For example, we have noticed that slightly worse schedules were generated for the 2009-10 season. But that was not completely unexpected, and it could be attributed to the fact that fewer playable dates were available for this particular season, as the XXI Winter Olympic Games had shut out nearly two weeks from the regular-season schedule in January of 2010. 

On the whole, our results seem to be significantly better than those reported in Costa (1995). In particular, with regard to the 1993-94 season, when the NHL was formed by only 24 teams but every team already had to play 41 home games, Costa’s best result refer to a schedule that, even though at least 15 extra dates had been provided by each team, exactly 105 games were scheduled on days when the arena of the respective home team was not available. In addition, that schedule causes two violations for the constraints C2 and C3, and it also presents 33 occurrences of a team having byes made up of more than three consecutive days in the course of a single road trip. With respect to our best schedules, even for the instances with no extra arena dates, none of those requirements were violated. 

97 

Table 5.6 _Best-found schedules for instances without extra arena-available dates_ Constraint violations on the best-found solutions by the ALNS for the entire-league instances without extra arena-available dates, and violations on the corresponding official NHL schedules. 

|||||Nu|mber|of v|iolati|ons|||
|---|---|---|---|---|---|---|---|---|---|---|
|Season|By|C1|C2|C3|C4|C5|C6|C7|C8|C9|
|’09|ALNS|0|0|0|10|3|12|0|0|0|
||NHL|0|0|3|12|6|87|1|1|0|
|’10|ALNS|0|0|0|4|0|6|0|0|0|
||NHL|0|0|3|14|16|66|0|0|0|
|’11|ALNS|0|0|0|5|4|8|0|0|0|
||NHL|0|0|0|9|19|75|1|1|0|
|’12|ALNS|0|0|0|9|1|21|0|0|0|
||NHL|0|0|0|10|3|88|1|1|0|
|’13|ALNS|0|0|0|0|3|8|0|0|0|
||NHL|0|0|0|10|8|33|1|1|0|



98 

|_I−_<br> **_–_**_,_12**_–_**_}_<br> **_–_**_,_15**_–_**_}_<br> **_–_**_,_14**_–_**_}_<br> _\ {_01**_–_**_}_<br> _\ {_02**_–_**_}_<br> _\ {_05**_–_**_}_<br> _\ {_06**_–_**_}_<br> _\ {_07**_–_**_}_<br> _\ {_08**_–_**_}_<br> _\ {_01**_–_**_}_<br> _\ {_02**_–_**_}_<br> _\ {_05**_–_**_}_<br> _\ {_06**_–_**_}_<br> _\ {_08**_–_**_}_<br>_\ {_01**_+_**_}_<br>_\ {_02**_+_**_}_<br>_\ {_03**_+_**_}_<br>_\ {_04**_+_**_}_<br>_\ {_05**_+_**_}_<br>_\ {_02**_+_**_}_<br>_\ {_03**_+_**_}_<br>_\ {_04**_+_**_}_<br>_\ {_05**_+_**_}_<br>_uniform_<br>_avg10K_<br>_avgklast_<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>_f_(_·_)<br>ces with 4 extra dates per team<br> on the costs of the best-found solutions over<br>rder they appear, from the top to the bottom,<br>dates. At the beginning (label_I−_), all the 20<br> (as indicated by the respective set-theoretic<br> **_–_**_,_08**_–_**_}_ and _J_+<br>4 = _{_02**_+_**_,_03**_+_**_,_04**_+_**_,_05**_+_**_}_. All<br>ee experiments (in the bottom of each chart).<br>0-11 season: one instance with no extra dates<br>ach confguration of operators, the degree of<br>ces) of 150 000 iterations for the (A)LNS.|
|---|
|_\ {_03**_–_**_,_09<br>_\ {_04**_–_**_,_13<br><br> _\ {_10**_–_**_,_11<br>_I−_<br>6 <br>_I−_<br>6 <br>_I−_<br>6 <br>_I−_<br>6 <br>_I−_<br>5 =_I−_<br>6 <br>_I−_<br>6 <br>_I−_<br>5 <br>_I−_<br>5 <br>_I−_<br>5 <br>_I−_<br>5 <br>_I−_<br>5 <br>_J_+<br>4 =_J_+ <br>_J_+ <br>_J_+ <br>_J_+ <br>_J_+ <br>_J_+<br>4  <br>_J_+<br>4  <br>_J_+<br>4  <br>_J_+<br>4  <br>_I−_<br>5 _∪J_+<br>4<br>b) Instan<br>atistics <br>in the o<br>4 extra<br>xcluded<br>_,_05**_–_**_,_06<br>last thr<br>the 201<br>te, for e<br> instan|
|_I−_<br>_I−_<br>12<br>_I−_<br>9 <br>_o ∈_<br>(<br> St<br>ed<br>th<br>y e<br>2**_–_**<br>the<br>of<br>ica<br>_×_ 5|
|5<br>65<br>85<br>105<br>125<br>145<br>165<br>185<br>205<br>with no extra dates<br>_I−_<br>12 =<br>_I−_<br>9 =<br>_I−_<br>6 =<br>_ωo ∀_<br> _diferent confgurations of operators_ <br>mputational experiments were conduct<br>xtra dates and for the (b) instances wi<br> but operators have been successivel<br>rs remained, which are _I−_<br>5 = _{_01**_–_**_,_0<br>of the algorithm (ALNS), except for<br>was applied 8 times to fve instances<br>tes per team. Thus, the boxplots ind<br>found solutions over 40 runs (8 runs|
|_I−_<br>_I−_<br>12 =_I−\ {_03**_–_**_,_09**_–_**_,_12**_–_**_}_<br>_I−_<br>9 =_I−_<br>12_\ {_04**_–_**_,_13**_–_**_,_15**_–_**_}_<br>_I−_<br>6 =_I−_<br>9 _\ {_10**_–_**_,_11**_–_**_,_14**_–_**_}_<br>_I−_<br>6 _\ {_01**_–_**_}_<br>_I−_<br>6 _\ {_02**_–_**_}_<br>_I−_<br>6 _\ {_05**_–_**_}_<br>_I−_<br>6 _\ {_06**_–_**_}_<br>_I−_<br>5 =_I−_<br>6 _\ {_07**_–_**_}_<br>_I−_<br>6 _\ {_08**_–_**_}_<br>_I−_<br>5 _\ {_01**_–_**_}_<br>_I−_<br>5 _\ {_02**_–_**_}_<br>_I−_<br>5 _\ {_05**_–_**_}_<br>_I−_<br>5 _\ {_06**_–_**_}_<br>_I−_<br>5 _\ {_08**_–_**_}_<br>_J_+<br>4 =_J_+_\ {_01**_+_**_}_<br>_J_+_\ {_02**_+_**_}_<br>_J_+_\ {_03**_+_**_}_<br>_J_+_\ {_04**_+_**_}_<br>_J_+_\ {_05**_+_**_}_<br>_J_+<br>4 _\ {_02**_+_**_}_<br>_J_+<br>4 _\ {_03**_+_**_}_<br>_J_+<br>4 _\ {_04**_+_**_}_<br>_J_+<br>4 _\ {_05**_+_**_}_<br>_uniform_<br>_avg10K_<br>_avgklast_<br>4<br>_ωo ∀o ∈I−_<br>5 _∪J_+<br>4<br>_f_(_·_)<br>(a) Instance <br>Figure 5.3 _Best-found solutions on_<br>150 000 (A)LNS iterations. The co<br>both for the (a) instance with no e<br>operators, _I−∪J_+, were provided,<br>diference) until only nine operato<br>results refer to the adaptive version<br>For each experiment, the algorithm<br>and four instances with 4 extra da<br>dispersion in the costs of the best-|



99 



<!-- Start of picture text -->
with ×<br>35 Thus,<br>runs<br>team adapted iteration<br>provided.<br>(8<br>30 per the<br>instance team.<br>of ALNS were runs<br>25 )<br>dates + one per<br>72<br>last 05<br>20 extra values (a)<br>8 the and dates over<br>the ,<br>15 at +<br>with on 04 extra<br>+ , 8 tracked<br>10 03<br>A L A L A L A L A L A L A L A L A L + , investigated:<br>01  – 02  – 05  – 06  – 08  – + 02 + 03 + 04 + 05 (%) (c)Instances Statistics particular, (02 with<br>in<br>probabilities<br>35 and, individually instances<br>iterations ) operators 4<br>team A<br>( are<br>30 per selection<br>ALNS repair other<br>25 dates 4 which the<br>(c)<br>the in<br>iterations<br>and<br>20 extra ) and<br>4  – season,<br>08<br>15 through ALNS<br>with<br>team,<br>and dispersion<br>10  – , 2010-11 per of<br>A L A L A L A L A L A L A L A L A L 10 000 06<br> –  –  –  –  – + + + + (%) Instances operators  – , the<br>01 02 05 06 08 02 03 04 05 (b) every 05  – , of dates degree<br>chosen of 02 the<br>, extra<br>50  –<br>end 4<br>45 the (01 instances<br>9<br>for the<br>40 dates at to with operator,<br>35<br>30 extra operators times each algorithm.<br>25 no tracked 8 instances for<br>20 probabilities 4<br>with destroy ALNS<br>15 5 applied (b)<br>the<br>10<br>indicate,<br>of<br>5 Instance Selection Only was<br>A L A L A L A L A L A L A L A L A L probabilities dates,<br>01  – 02  – 05  – 06  – 08  – + 02 + 03 + 04 + 05 (%) (a) 5.4 ).( L ALNS<br>boxplots<br>extra<br>instances)<br>Figure selection alone The no the 9<br><!-- End of picture text -->

100 

# **CHAPTER 6** 

# **CONCLUSION** 

In this thesis, we have revisited the NHL scheduling problem, which consists in scheduling the regular-season games of the National Hockey League. Some basic requirements for a good NHL schedule were identified, and then, we proposed the first integer linear programming (IP) model for exactly solving the problem and also an adaptive large neighborhood search (ALNS) for solving instances of practical size. In particular, we have reported some computational results for instances of moderate size that were obtained from a commercial state-of-the-art solver with several variants of the IP model, where different constraints have been relaxed and their violations penalized in the objective function. Promising results for instances of realistic size that were generated by the ALNS have also been reported. Indeed, the ALNS was able to find schedules that satisfy all essential requirements even for the most challenging instances of the problem where, in particular, the availability of arena is scarce or at its minimum. Such results reinforce the original idea that high-quality solutions for tightly-constrained problems can be achieved by a combination of rather naive (and often individually ineffective) heuristics into an ALNS framework. 

As we have mentioned in the literature review, the focus of studies on sports scheduling has often been the minimization of travel distances. In such cases, distances are somewhat used as measure of travelling costs and players fatigue. This can be controversial as most travels are done by air, and then, in particular, fatigue would be more due to poor quality of the travel experience than long distance itself. Moreover, some particular game scheduling may result in a slightly longer travelling distance for the teams involved but, for example, have the advantage of the game being scheduled during a weekend, which could increase spectator attendance or broadcasting revenue, and thus fairly compensate some possible “extra” travel cost. And also, because the home locations of the NHL teams are so unevenly distributed throughout a vast region, care should be taken as not only try to minimize the overall travel distance at the expense of aggravating the particular situation of the most geographically isolated teams. Therefore, although we recognize that travels are indeed one of the concerns in the NHL scheduling problem, in the case of the ALNS, we have considered them only implicitly by the use of the saving measure in the generation of both forced and free trips. 

Our ALNS algorithm for the NHL scheduling problem is well suited for the cases where some games have been scheduled beforehand. In fact, all the results that we have reported in this thesis take into account that, in particular, the NHL regular season currently includes 

101 

a few games played in Europe, and also other special games, at predetermined dates that cannot be changed. 

We are confident that by involving the expert scheduler into a detailed formulation of the problem and into the implementation of other specialized heuristics in the ALNS framework would enable computers to assist the designing of much better schedules than the NHL might have conceived as being possible. In fact, the reported results suggest that our approach could enable the NHL managers to identify unnecessary weakness in their schedules, and could certainly assist them in finding high-quality schedules with respect to a variety of new preferences. 

Starting in the 2013-14 season, the NHL adopted a new structure, which distributes the 30 teams into only two eight-team divisions and two seven-team divisions. Furthermore, the teams are now playing under a new regular-season structure, yet a team still plays 41 home games. It would be useful to investigate the impact of such changes in the quality of the schedules that our approach is able to produce with regard to the essential requirements we have considered in this thesis and possibly other preferences and measures on fairness issues for the teams. 

102 

# **REFERENCES** 

– ARMSTRONG, J. and WILLIS, R. J. (1993). Scheduling the Cricket World Cup a case study. _The Journal of the Operational Research Society_ , <u>44,</u> 1067–1072. 

BAO, R. (2009). _Time Relaxed Round Robin Tournament and the NBA Scheduling Problem_ . Ph.D. thesis, Mechanical Engineering, Cleveland State University. Cleveland, United States. BARTSCH, T., DREXL, A. and KROGER,<sup>¨</sup> S. (2006). Scheduling the professional soccer leagues of Austria and Germany. _Computer & Operations Research_ , <u>33,</u> 1907–1937. 

BEAN, J. C. and BIRGE, J. R. (1980). Reducing Travelling Costs and Player Fatigue in the National Basketball Association. _Interfaces_ , <u>10,</u> 98–102. 

BRISKORN, D. (2008a). Feasibility of home-away-pattern sets for round robin tournaments. _Operations Research Letters_ , <u>36,</u> 283–284. 

BRISKORN, D. (2008b). _Sports Leagues Scheduling: Models, Combinatorial Properties, and Optimization Algorithms_ . Lecture Notes in Economics and Mathematical Systems, 603. Springer-Verlag Berlin Heidelberg, Berlin, Heidelberg. 

BRISKORN, D. and DREXL, A. (2007). A branch-and-price algorithm for scheduling sport leagues. _Journal of the Operations Research Society_ , <u>60,</u> 89–93. 

BROUWER, A. E., POST, G. F. and WOEGINGER, G. J. (2008). Tight bounds for break minimization in tournament scheduling. _Journal of Combinatorial Theory, Series A_ , <u>115,</u> 1065–1068. 

CHEUNG, K. K. H. (2008). Solving mirrored traveling tournament problem benchmark instances with eight teams. _Discrete Optimization_ , <u>5,</u> 138–143. 

CLARKE, G. and WRIGHT, J. W. (1964). Scheduling of vehicles from a central depot to a number of delivery points. _Operations Research_ , <u>12,</u> 568–581. 

COSTA, D. (1995). An evolutionary tabu search algorithm and the NHL scheduling problem. _INFOR_ , <u>33,</u> 161–178. 

CRAIG, S., WHILE, L. and BARONE, L. (2009). Scheduling for the National Hockey League Using a Multi-objective Evolutionary Algorithm. In A. Nicholson and X. Li, editors, _AI 2009: Advances in Artificial Intelligence_ , Springer Berlin Heidelberg, vol. 5866 of _Lecture Notes in Computer Science_ , book section 39. Pages 381–390. 

DE WERRA, D. (1980). Geography, games and graphs. _Discrete Applied Mathematics_ , <u>2,</u> 327–337. 

103 

DE WERRA, D. (1981). Scheduling in Sports. In P. Hansen, editor, _North-Holland Mathematics Studies_ , North-Holland, vol. 59. Pages 381–395. 

DE WERRA, D. (1982). Minimizing irregularities in sports schedules using graph theory. _Discrete Applied Mathematics_ , <u>4,</u> 217–226. 

DE WERRA, D. (1985). On the multiplication of divisions: the use of graphs for sports scheduling. _Networks_ , <u>15,</u> 125–136. 

DE WERRA, D. (1988). Some models of graphs for scheduling sports competitions. _Discrete Applied Mathematics_ , <u>21,</u> 47–65. 

DELLA CROCE, F. and OLIVERI, D. (2006). Scheduling the Italian Football League: an ILP-based approach. _Computers & Operations Research_ , <u>33,</u> 1963–1974. 

DEPALMA, T. J. (2004). _Betting market efficiency in the National Hockey League: An analysis of expansion seasons_ . Ph.D. thesis, Faculty of Economics, University of Delaware. Delaware, United States. 

DREXL, A. and KNUST, S. (2007). Sports league scheduling: graph- and resource-based models. _Omega_ , <u>35,</u> 465–471. 

EASTON, K., NEMHAUSER, G. and TRICK, M. (2001). The Traveling Tournament Problem Description and Benchmarks. In T. Walsh, editor, _Principles and Practice of Constraint Programming — CP 2001_ , Springer Berlin Heidelberg, vol. 2239 of _Lecture Notes in Computer Science_ , book section 43. Pages 580–584. 

EASTON, K., NEMHAUSER, G. and TRICK, M. (2003). Solving the traveling tournament problem: a combined integer programming and constraint programming approach. In E. Burke and P. De Causmaecker, editors, _Practice and Theory of Automated Timetabling IV (PATAT 2002)_ . Spring-Verlag, vol. 2740. Pages 100–109. 

EASTON, K., NEMHAUSER, G. and TRICK, M. (2004). Sport Scheduling. In J. Y.-T. Leung, editor, _Handbook of Scheduling: Algorithms, Models, and Performance Analysis_ , CRC Press, book section 52. Pages 1139–1157. 

EASTON, K. K. (2003). _Using integer programming and constraint programming to solve sports scheduling problems_ . Ph.D. thesis, Georgia Institute of Technology, Georgia, United States. 

EASTON, T. and GARY PARKER, R. (2001). On completing latin squares. _Discrete Applied Mathematics_ , <u>113,</u> 167–181. 

ELF, M., JUNGER,<sup>¨</sup> M. and RINALDI, G. (2003). Minimizing breaks by maximizing cuts. _Operations Research Letters_ , <u>31,</u> 343–349. 

104 

FERLAND, J. A. and FLEURENT, C. (1991). Computer aided scheduling for a sport league. _INFOR_ , <u>29,</u> 14–25. 

FLEURENT, C. (1987). _M´ethodes heuristiques pour la conception de calendriers sportifs_ . Master’s thesis, D´epartement d’informatique et de recherche op´erationnelle, Universit´e de Montr´eal. Montreal, Quebec. 

FLEURENT, C. and FERLAND, J. A. (1993). Allocating games for the NHL using Integer Programming. _Operations Research_ , <u>41,</u> 649–654. 

FRASER, W. (1982). _The role of computer simulation in building the National Hockey League Schedule_ . Technical report, IBM Canada Limited. 

GOEMANS, M. X. and WILLIAMSON, D. P. (1995). Improved Approximation Algorithms for Maximum Cut and Satisfiability Problems Using Semidefinite Programming. _J. ACM_ , <u>42,</u> 1115–1145. 

GOOSSENS, D. and SPIEKSMA, F. (2011). Soccer schedules in Europe: an overview. _Journal of Scheduling_ , <u>15,</u> 651–651. 

HAMIEZ, J.-P. and HAO, J.-K. (2004). A linear-time algorithm to solve the Sports League Scheduling Problem (prob026 of CSPLib). _Discrete Applied Mathematics_ , <u>143,</u> 252–265. 

HAVARD, C. T. (2014). Glory Out of Reflected Failure: The examination of how rivalry affects sport fans. _Sport Management Review_ , <u>17,</u> 243–253. 

HENZ, M. (2001). Scheduling a Major College Basketball Conference–Revisited. _Operations Research_ , <u>49,</u> 163–168. 

IRNICH, S. (2010). A new branch-and-price algorithm for the traveling tournament problem. _European Journal of Operational Research_ , <u>204,</u> 218–228. 

KENDALL, G., KNUST, S., RIBEIRO, C. C. and URRUTIA, S. (2010). Scheduling in sports: An annotated bibliography. _Computers & Operations Research_ , <u>37,</u> 1–19. 

KNUST, S. (2010). Scheduling non-professional table-tennis leagues. _European Journal of Operational Research_ , <u>200,</u> 358–367. 

KNUST, S. (2014). _Classification of Literature on Sports Scheduling_ . Webpage `http://www.inf.uos.de/knust/sportlit_class/sportlit_class.html` . Last checked on May 10, 2014. 

KNUST, S. and LUCKING,<sup>¨</sup> D. (2009). Minimizing costs in round robin tournaments with place constraints. _Computers & Operations Research_ , <u>36,</u> 2937–2943. 

KNUST, S. and VON THADEN, M. (2006). Balanced home-away assignments. _Discrete Optimization_ , <u>3,</u> 354–365. 

105 

KOVACS, A. A., PARRAGH, S. N., DOERNER, K. F. and HARTL, R. F. (2012). Adaptive large neighborhood search for service technician routing and scheduling problems. _Journal of Scheduling_ , <u>15,</u> 579–600. 

LAMKEN, E. R. (1990). Generalized Balanced Tournament Designs. _Transactions of the American Mathematical Society_ , <u>318,</u> 473–490. 

LARSON, J. and JOHANSSON, M. (2014). Constructing Schedules for Sports Leagues with Divisional and Round-robin Tournaments. _Journal of Quantitative Analysis in Sports_ , <u>10,</u> 119–129. `doi:10.1515/jqas-2013-0090` . 

LENTEN, L. J. A. (2013). Measurement of Competitive Balance in Conference and Divisional Tournament Design. _Journal of Sports Economics_ , 1–23. `doi:10.1177/1527002512471538` . 

LIM, A., RODRIGUES, B. and ZHANG, X. (2006). A simulated annealing and hill-climbing algorithm for the traveling tournament problem. _European Journal of Operational Research_ , <u>174,</u> 1459–1478. 

MACDONALD, B. and PULLEYBLANK, W. (2014). Realignment in the NHL, MLB, NFL, and NBA. _Journal of Quantitative Analysis in Sports_ , <u>10,</u> 225–240. `doi:10.1515/jqas2013-0070` . 

MELO, R. A., URRUTIA, S. and RIBEIRO, C. C. (2007). Scheduling Single Round Robin Tournaments with Fixed Venues. In _3rd Multidisciplinary International Conference on Scheduling: Theory and Applications (MISTA’07)_ . Pages 431–438. 

MIYASHIRO, R., IWASAKI, H. and MATSUI, T. (2003). Characterizing feasible pattern sets with a minimum number of breaks. In E. Burke and P. De Causmaecker, editors, _Practice and Theory of AutomatedTimetabling IV_ , Springer-Verlag, Berlin Heidelberg, LNCS 2740. Pages 78–99. 

MIYASHIRO, R. and MATSUI, T. (2005). A polynomial-time algorithm to find an equitable home-away assignment. _Operations Research Letters_ , <u>33,</u> 235–241. 

MIYASHIRO, R. and MATSUI, T. (2006). Semidefinite programming based approaches to the break minimization problem. _Computers & Operations Research_ , <u>33,</u> 1975–1982. 

NEMHAUSER, G. and TRICK, M. (1998). Scheduling a Major College Basketball Conference. _Operations Research_ , <u>46,</u> 1–8. 

NURMI, K., GOOSSENS, D., BARTSCH, T., BONOMO, F., BRISKORN, D., DURAN, G., KYNGAS, J., MARENCO, J., RIBEIRO, C., SPIEKSMA, F.<sup>¨</sup> _ET AL_ . (2010). A framework for a highly constrained sports scheduling problem. In _Proceedings of the International MultiConference of Engineers and Computer Scientists_ . vol. 3. Pages 1991–1997. 

106 

OBERHOFER, H., PHILIPPOVICH, T. and WINNER, H. (2010). Distance matters in away games: Evidence from the German football league. _Journal of Economic Psychology_ , <u>31,</u> 200–211. 

PISINGER, D. and ROPKE, S. (2007). A general heuristic for vehicle routing problems. _Computers & Operations Research_ , <u>34,</u> 2403–2435. 

PISINGER, D. and ROPKE, S. (2010). Large Neighborhood Search. In M. Gendreau and J.-Y. Potvin, editors, _Handbook of Metaheuristics_ , Springer US, vol. 146 of _International Series in Operations Research & Management Science_ . Pages 399–419. 

POST, G. and WOEGINGER, G. J. (2006). Sports tournaments, home-away assignments, and the break minimization problem. _Discrete Optimization_ , <u>3,</u> 165–173. 

RASMUSSEN, R. and TRICK, M. (2006). The Timetable Constrained Distance Minimization Problem. In J. C. Beck and B. Smith, editors, _Integration of AI and OR Techniques in Constraint Programming for Combinatorial Optimization Problems_ , Springer Berlin Heidelberg, vol. 3990 of _Lecture Notes in Computer Science_ , book section 15. Pages 167–181. RASMUSSEN, R. and TRICK, M. (2009). The timetable constrained distance minimization problem. _Annals of Operations Research_ , <u>171,</u> 45–59. 

RASMUSSEN, R. V. (2008). Scheduling a triple round robin tournament for the best Danish soccer league. _European Journal of Operational Research_ , <u>185,</u> 795–810. 

RASMUSSEN, R. V. and TRICK, M. A. (2007). A Benders approach for the constrained minimum break problem. _European Journal of Operational Research_ , <u>177,</u> 198–213. 

– RASMUSSEN, R. V. and TRICK, M. A. (2008). Round robin scheduling a survey. _European Journal of Operational Research_ , <u>188,</u> 617–636. 

REGIN,<sup>´</sup> J.-C. (2001). Minimization of the number of breaks in sports scheduling problems using constraint programming. In E. C. Freuder and R. J. Wallace, editors, _Constraint programming and large scale discrete optimization_ , American Mathematical Society, Rutgers, New Jersey, vol. 57 of _DIMACS Series in Discrete Mathematics and Theoretical Computer Science_ . Pages 115–130. 

REINFELD, N. V. and VOGEL, W. R. (1958). _Mathematical programming_ . Englewood Cliffs, N. J. : Prentice-Hall. 

RIBEIRO, C. C. (2012). Sports scheduling: Problems and applications. _International Transactions in Operational Research_ , <u>19,</u> 201–226. 

ROKOSZ, F. M. (2000). _Procedures for structuring and scheduling sports tournaments: elimination, consolation, placement, and round-robin design_ . C.C. Thomas, Springfield, Ill., third edition. 

107 

ROPKE, S. and PISINGER, D. (2006). An adaptive large neighborhood search heuristic for the pickup and delivery problem with time windows. _Transportation Science_ , <u>40,</u> 455–472. 

ROSEN, D. (2013). _Realignment plan approved by Board of Governors_ . Webpage `http://www.nhl.com/ice/news.htm?id=660138` . Last checked on July 3, 2014. 

RUSSELL, R. A. and LEUNG, J. M. Y. (1994). Devising a cost effective schedule for a baseball league. _Operations Research_ , <u>42,</u> 614–625. 

SCHAERF, A. (1999). Scheduling sport tournaments using constraint logic programming. _Constraints_ , <u>4,</u> 43–65. 

SCHONBERGER,<sup>¨</sup> J., MATTFELD, D. C. and KOPFER, H. (2000). Automated timetable _–_ generation for rounds of a table-tennis league. In _Evolutionary Computation, 2000 Proceedings of CEC2000_ . vol. 1. Pages 277–284. 

SCHONBERGER,<sup>¨</sup> J., MATTFELD, D. C. and KOPFER, H. (2004). Memetic Algorithm timetabling for non-commercial sport leagues. _European Journal of Operational Research_ , <u>153,</u> 102–116. 

SCHREUDER, J. (1992). Combinatorial aspects of construction of competition Dutch professional football leagues. _Discrete Applied Mathematics_ , <u>35,</u> 301–312. 

SCHREUDER, J. A. M. (1980). Constructing timetables for sport competitions. _Mathematical Programming Study_ , <u>13,</u> 58–67. 

SCHRIMPF, G., SCHNEIDER, J., STAMM-WILBRANDT, H. and DUECK, G. (2000). Record breaking optimization results using the ruin and recreate principle. _Journal of Computational Physics_ , <u>159,</u> 139–171. 

SHAW, P. (1998). Using constraint programming and local search methods to solve vehicle routing problems. _Principles and Practice of Constraint Programming - Cp98_ , <u>1520,</u> 417– 431. 

SMITH, D. R., CIACCIARELLI, A., SERZAN, J. and LAMBERT, D. (2000). Travel and the home advantage in professional sports. / Avantage du terrain par rapport a un deplacement pour les sportifs professionnels. _Sociology of Sport Journal_ , <u>17,</u> 364–385. 

SUZUKA, A., MIYASHIRO, R., YOSHISE, A. and MATSUI, T. (2007). The home-away assignment problems and break minimization/maximization problems in sports scheduling. _Pacific Journal of Optimization_ , <u>3,</u> 113–133. 

TRICK, M. (2001). A schedule-then-break approach to sports timetabling. In E. Burke and W. Erben, editors, _Practice and Theory of Automated Timetabling III_ , Springer Berlin Heidelberg, vol. 2079 of _Lecture Notes in Computer Science_ . Pages 242–253. 

108 

TRICK, M. (2005). Formulations and Reformulations in Integer Programming. In R. Bart´ak and M. Milano, editors, _Integration of AI and OR Techniques in Constraint Programming for Combinatorial Optimization Problems_ , Springer Berlin Heidelberg, vol. 3524 of _Lecture Notes in Computer Science_ , chapter 27. Pages 366–379. 

TRICK, M. (2011). Sports Scheduling. In P. van Hentenryck and M. Milano, editors, _Hybrid Optimization_ , Springer New York, vol. 45 of _Springer Optimization and Its Applications_ . Pages 489–508. 

URRUTIA, S. and RIBEIRO, C. C. (2006). Maximizing breaks and bounding solutions to the mirrored traveling tournament problem. _Discrete Applied Mathematics_ , 154, 1932–1938. UTHUS, D., RIDDLE, P. and GUESGEN, H. (2009). DFS* and the Traveling Tournament Problem. In W.-J. Hoeve, J. Hooker, D. Uthus, P. Riddle and H. Guesgen, editors, _Integration of AI and OR Techniques in Constraint Programming for Combinatorial Optimization Problems_ , Springer Berlin Heidelberg, vol. 5547 of _Lecture Notes in Computer Science_ . Pages 279–293. 

UTHUS, D., RIDDLE, P. and GUESGEN, H. (2012). Solving the traveling tournament problem with iterative-deepening A*. _Journal of Scheduling_ , <u>15,</u> 601–614. 

VAN HENTENRYCK, P. and MICHEL, L. (2009). _Constraint-Based Local Search_ . The MIT Press. 

VAN HENTENRYCK, P. and VERGADOS, Y. (2005). Minimizing breaks in sport scheduling with local search. In _Proceedings of the Fifteenth International Conference on Automated Planning and Scheduling (ICAPS) 2005_ . vol. 1. Pages 22–29. June 5-10, 2005, Monterey, California, United States. 

VAN WEERT, A. and SCHREUDER, J. (1998). Construction of basic match schedules for sports competitions by using graph theory. In E. Burke and M. Carter, editors, _Practice and Theory of Automated Timetabling II_ , Springer Berlin Heidelberg, vol. 1408 of _Lecture Notes in Computer Science_ , book section 13. Pages 201–210. 

109 

# **APPENDIX A** 

# **PSEUDOCODE OF THE ALNS ALGORITHM** 

# **A.1 Pseudocode of the ALNS algorithm** 

The main features of the ALNS algorithm we propose for the NHL Scheduling Problem can be summarized as stated in Algorithm 1. It essentially consists of the construction of an initial solution ( _Sinit_ ) and a loop that, while not all constraints are satisfied (or equivalently while _f_ ( _Sbest_ ) _>_ 0), tries to improve the current solution ( _Scurr_ ) through a fixed number of iterations (with _k_ varying from 0 to _Kalns_<sup>_max−_1).Theparametersprovidedtothealgorithm</sup> are the maximum number of iterations, _Kalns_<sup>_max_;thesegmentsize,</sup><sup>_Kseg_;thestarttemperature</sup> control parameter, _τ_ ; the score adjustment parameters, _σbes_ , _σbet_ , and _σacc_ ; the reaction factor, _ρ_ ; the set of destroy operators, _I_<sup>_−_</sup> , and the set of repair operators, _J_<sup>+</sup> , with their respective initial weights, _ωo ∀o ∈ I_<sup>_−_</sup> _∪ J_<sup>+</sup> . In order for us still to focus on the master level of the approach, the statement of the algorithm evokes three “external” procedures (denoted with a `typewriter` style font), which we describe in a rather informal way. On line 1, a complete schedule is constructed as the initial solution, _Sinit_ , by the procedure `constructInitialSolution()` . This procedure implements the multi-heuristic approach proposed by Fleurent (1987), which we describe in the next subsection. In the body of the loop (from lines 9 to 33), one destroy operator and one repair operator are initially selected by two calls, on lines 9 and 10, to the procedure `selectOperator(` _·_ `)` , whose argument can be seen as a vector of weights for the random weighted selection among the corresponding candidate operators. That procedure implements thus the strategy on the operator selection explained earlier. The just-selected pair of destroy and repair operators are applied to the current solution by the procedure `applyOperators(` _·_ `)` on line 11. The resulting destroyedand-repaired solution is then either accepted or rejected by the procedure `acceptSA(` _·_ `)` , on line 12, which implements the solution acceptance criteria from Simulated Annealing. In particular, the initial temperature, _T_ 0, and the cooling factor, _c_ , are calculated as being equal to ( _τ/_ 100)( _f_<sup>ˆ</sup> ( _Sinit_ ) _/_ ( _−_ ln(0 _._ 5))) and ( _T_ 0 ( _−_ ln(0 _._ 01)))<sup>(</sup><sup>_−_1</sup><sup>_/K_</sup> _alns_<sup>_max_)</sup> , respectively, where _f_<sup>ˆ</sup> ( _Sinit_ ) is the weighted sum<sup>�9</sup> _i_ =3<sup>_wifi_(</sup><sup>_Sinit_)ofthenumberofviolations,</sup><sup>_fi_(</sup><sup>_Sinit_),ofeveryconstraint</sup> C _i_ , for _i ∈{_ 3 _,_ 4 _, . . . ,_ 9 _}_ , in the initial solution, _Sinit_ . The other parts of Algorithm 1 keep track of the best-found solution, _Sbest_ , and adjust the scores of the operators, which are used to recalculate the operator weights (and thus their selection probabilities) at the end of each _Kseg_ iterations defining an ALNS segment. 

110 

# **Algorithm 1:** ALNS for the NHL Scheduling Problem 

**parameters** : _Kseg_ , _σbes, σbet, σacc_ , _ρ_ , _Kalns_<sup>_max_,</sup><sup>_τ_,</sup> _I_<sup>_−_</sup> , _J_<sup>+</sup> , _ωo ∀o ∈ I_<sup>_−_</sup> _∪ J_<sup>+</sup> **1** _Sinit ←_ `constructInitialSolution()` **2 foreach** _o ∈ I_<sup>_−_</sup> _∪ J_<sup>+</sup> **do 3** _πo ←_ 0; _θo ←_ 0 **4** _T_ 0 _←_ ( _τ/_ 100)( _f_<sup>ˆ</sup> ( _Sinit_ ) _/_ ( _−_ ln(0 _._ 5))); **5** _c ←_ ( _T_ 0 ( _−_ ln(0 _._ 01)))<sup>(</sup><sup>_−_1</sup><sup>_/K_</sup> _alns_<sup>_max_)</sup> **6** _k ←_ 0; _kseg ←_ 0 **7** _Scurr ← Sinit_ ; _Sbest ← Sinit_ **8 while** _k < Kalns_<sup>_max_</sup><sup>**_a_**</sup><sup>_ndf_(</sup><sup>_Sbest_)</sup><sup>_>_0</sup><sup>**do**</sup> **9** _i ←_ `selectOperator(` _ωo ∀o ∈ I_<sup>_−_</sup> `)` **10** _j ←_ `selectOperator(` _ωo ∀o ∈ J_<sup>+</sup> `)` **11** _Stemp ←_ `applyOperators(` _i, j, Scurr_ `)` **12 if** `acceptSA(` _f_ ( _S_ _`temp`_ ) _− f_ ( _S_ _`curr`_ ) _, Tk_ `)` **then 13** _Scurr ← Stemp_ **14** _σ_<sup>_′_</sup> _← σacc_ **15 else 16** _σ_<sup>_′_</sup> _←_ 0 **17 if** _f_ ( _Stemp_ ) _< f_ ( _Sbest_ ) **then 18** _Sbest ← Stemp_ **19** _σ_<sup>_′_</sup> _← σbes_ **20 else 21 if** _f_ ( _Stemp_ ) _< f_ ( _Scurr_ ) **then 22** _σ_<sup>_′_</sup> _← σbet_ **23** _πi ← πi_ + _σ_<sup>_′_</sup> ; _πj ← πj_ + _σ_<sup>_′_</sup> **24** _θi ← θi_ + 1; _θj ← θj_ + 1 **25 if** _k < K_ **then** _seg seg_ **26** _kseg ← kseg_ + 1 **27 else 28** _k ←_ 0 _seg_ **29 foreach** _o ∈ I_<sup>_−_</sup> _∪ J_<sup>+</sup> : _θo >_ 0 **do 30** _ωo ←_ (1 _− ρ_ ) _ωo_ + _ρ_ ( _πo/θo_ ) **31** _πo ←_ 0; _θo ←_ 0 **32** _Tk_ +1 _← c Tk_ **33** _k ← k_ + 1 **34 return** _Sbest_ 

111 

# **APPENDIX B** 

# **FLEURENT’S HEURISTICS** 

# **B.1 Fleurent’s heuristics** 

In the heuristics by Fleurent (1987), a “feasibly possible” scheduling is a game-day assignment that satisfies all the constraints in the set C _F_ = _{_ C0 _,_ C1 _,_ C2 _,_ C4 _,_ C5 _,_ C6 _}_ , except perhaps C5 on the minimum number of games per week. 

# **B.1.1 Forced-trip heuristic** 

The forced-trip heuristic generates as many forced trips as feasibly possible. Every forced trip is generated by repeating the following description. At first, the heuristic scans all teams with at least two distant (more than 900 miles) away games to be scheduled, and chooses the longest period of consecutive days with neither arena-available nor already-assigned dates for a team. Let the chosen period be denoted by [ _dl, du_ ] and the corresponding team by _a_ . To anticipate, _a_ will be the team to play away on the undertaken trip generation. In order to actually start building up the new trip, the heuristic selects two days, _d_ 1 and _d_ 2, both from within [ _dl, du_ ], and two distant opponents, _h_ 1 and _h_ 2, that allows the team _a_ to play away in the course of a single trip against _h_ 1 and _h_ 2 on days _d_ 1 and _d_ 2, respectively, without violating any constraint in C _F_ (except perhaps C5 on the minimum number of games per week). If more than one choice is identified, the selection of those two days and two opponents is one that maximizes the saving measure value _sa_ ( _h_ 1 _, h_ 2) = _dist_ ( _h_ 1 _, a_ ) + _dist_ ( _a, h_ 2) _− dist_ ( _h_ 1 _, h_ 2). It then carries out the corresponding game-day assignments for the visiting team, _a_ , to create a trip _r_ ( _a_ ), which is then formed by only two away games. 

Next, the heuristic attempts to extend the trip _r_ ( _a_ ) by trying to schedule the team _a_ to directly visit other distant rivals both before having played against _h_ 1 on day _d_ 1 and after having played against _h_ 2 on day _d_ 2. In fact, it first tries to extend the end of the trip _r_ ( _a_ ), whenever _d_ 2 (the current last game day of _r_ ( _a_ )) is far enough from _du_ + 1 (the next arenaavailable date of team _a_ ) to possibly allow at least one more feasible away game to be played before _a_ returns home, with no violation of the constraints in C _F_ . If this is the case and suitable rival exists, a team _h_ 3 is selected as to maximize the saving value _sa_ ( _h_ 2 _, h_ 3), and _a_ is scheduled to visit _h_ 3 on a day _d_ 3, which now becomes the last game day of the trip _r_ ( _a_ ). Such end-of-trip augmentation process is repeated until there exists no more distant rivals with arena dates yielding an away game scheduling for _a_ at the end of the same trip, without 

112 

violating the constraints in C _F_ . 

The process on extending the begin of the trip is essentially the same as that for the end. Indeed, the heuristic attempts to schedule new feasible away games for _a_ by trying to select distant rivals which maximizes the saving measure defined above, but the course of the assignments now goes backward from _d_ 1 (the current first game day of _r_ ( _a_ )) to day _dl_ (the first non arena date for _a_ on the selected period for the current trip generation). 

# **B.1.2 Forced-home heuristic** 

The forced-home heuristic selects all the long-lasting trips in decreasing order of their duration, and tries to schedule free games by repeating the following steps for each trip _r_ ( _t_ ) where a team _t_ starts playing a game on day _d_<sup>_r_</sup> 1<sup>and finishes playing some other game on day</sup> _d_<sup>_r_</sup> 2<sup>,suchthatthecondition</sup><sup>_dr_</sup> 2<sup>_−dr_</sup> 1<sup>_≥_7holds.</sup> 

- **_Step 1._** _Schedule a home game before the current long-lasting trip._ At first, regarding only the arena dates of the team _t_ that are before the day _d_<sup>_r_</sup> 1<sup>,identifytheday</sup><sup>_d_1thatis</sup> the closest day to _d_<sup>_r_</sup> 1<sup>,andthen,amongthehomegamesfor</sup><sup>_t_thatcanbescheduledon</sup> _d_ 1 with no violation of constraints in C _F_ , schedule on _d_ 1 the free game for which, if possible, the visiting rival of _t_ does not have _d_ 1 as one of its arena dates. In case of tie, prefer a rival located the closest to the arena of team _t_ . 

- **_Step 2._** _Schedule a home game after the current long-lasting trip._ At first, regarding only the arena dates of the team _t_ that are after the day _d_<sup>_r_</sup> 2<sup>,identifytheday</sup><sup>_d_2thatisthe</sup> closest day to _d_<sup>_r_</sup> 2<sup>,andthen,amongthehomegamesfor</sup><sup>_t_thatcanbescheduledon</sup> _d_ 2 with no violation of constraints in C _F_ , schedule on _d_ 2 the free game for which, if possible, the visiting rival of _t_ does not have _d_ 2 as one of its arena dates. In case of tie, prefer a rival located the closest to the arena of team _t_ . 

# **B.1.3 Free-trip heuristic** 

The free-trip heuristic tries to schedule all remaining games that individually opposes two distant teams by repeating the following steps on generating a single trip with no more than three games, where any condition of feasibility refers to the constraints in C _F_ only: 

- **_Step 1._** _Select a visiting team._ Choose a team _a_ with the highest number of distant (more than 900 miles) away games remaining to be scheduled, and let _T_<sup>˜</sup> _a_ be the set of the respective (distant) rivals. 

- **_Step 2._** _Determine a sequence of away games._ Among the teams in _T_<sup>˜</sup> _a_ , select two rivals, _h_ 1 and _h_ 2, to be visited by _a_ in a row, such that the saving measure value _sa_ ( _h_ 1 _, h_ 2) = _dist_ ( _h_ 1 _, a_ ) + _dist_ ( _a, h_ 2) _− dist_ ( _h_ 1 _, h_ 2) is the maximum over all pairs of teams from _T_<sup>˜</sup> _a_ . 

113 

Identify, also, a third opponent _h_ 3 _∈ T_<sup>˜</sup> _a \ {h_ 1 _, h_ 2 _}_ that provides the new largest saving value _sa_ ( _h_ 3 _, h_<sup>_′_</sup> ), where _h_<sup>_′_</sup> is any team, other than _h_ 3, from _T_<sup>˜</sup> _a_ (perhaps even _h_ 1 or _h_ 2); and let now _r_ be the sequence of teams given by the following conditional definition: _r_ = ( _h_ 1 _, h_ 2 _, h_ 3) if _h_<sup>_′_</sup> = _h_ 2; or _r_ = ( _h_ 3 _, h_ 1 _, h_ 2) if _h_<sup>_′_</sup> = _h_ 1; or _r_ = ( _h_ 1 _, h_ 2) otherwise. 

- **_Step 3._** _Assign dates to the games._ Recursively try to schedule the team _a_ to play away against its rivals in the sequence _r_ , as follows. Initially, assign any feasible day to the first corresponding game so as to define a single-game trip. Then, try to extend the trip by sequentially scheduling _a_ to visit the other teams in the order they appear in _r_ . Clearly, from the definition of a trip, any pair of those consecutive games must take place within a period of three days. At each attempt to schedule a game, if none of the potential days allows an assignment without violating the constraints in C _F_ then, before to proceed, backtrack by canceling the last successful scheduled game and trying to assign another feasible day to it. If the whole recursive approach does not find any feasible period for the current free trip then apply it to: either the sequence _r_ in inverse order if it has not been tried before; or a modified sequence in which the team geographically closest to _a_ is discarded. On the contrary, determine all possible periods of assignment for the current trip and schedule its respective games to the period having the least number of arena dates for the travelling team, _a_ . 

# **B.1.4 Weekend-game heuristic** 

For each pair of a team _t_ and a weekend day _d_ , let the “cost” of scheduling _t_ to play away on day _d_ be defined as _c_ ( _t, d_ ) = 3 _δtd_ + 2 _δtd′_ + 2 _δtd′′_ , where _d_<sup>_′_</sup> and _d_<sup>_′′_</sup> are the other two days (aside from _d_ ) in the weekend of _d_ , and _δtd_ ˆ is equal to 1 if the day _d_<sup>ˆ</sup> is an arena date of team _t_ , and it is equal to 0 otherwise. The weekend-game heuristic initially carries out the steps below for the set _D_ of the regular season days that fall on a Saturday. 

- **_Step 1._** _Create a set of promising games for every target day._ For each day _d ∈ D_ , generate ˜ ˜ 

- the set _G_<sup>˜</sup> _d_ of every free game _a_ @ _h_<sup>˜</sup> where a team _a_ must visit a non-distant (not farther than 900 miles) rival _h_<sup>˜</sup> and such that all the following conditions are satisfied: _(1) d_ yields an assignment with no violation of the constraints in C _F_ ; _(2) d_ is not within any ˜ ˜ 

- long-distance trip period for neither _a_ nor _h_<sup>˜</sup> ; and _(3) d_ is either unavailable for _a_ or it is the only day available for _a_ ˜ among the three days of the corresponding weekend. 

- **_Step 2._** _Sequentially schedule games to target days for each level of preference regarding the visiting team availability._ Whenever possible, select (at random if more than one) a target day _d ∈ D_ and a free game _a_ ˜@ _h_<sup>˜</sup> in _G_<sup>˜</sup> _d_ such that _c_ (˜ _a, d_ ) is the minimum over all dates in _D_ and their respective promising games; remove _a_ ˜@ _h_<sup>˜</sup> from _G_<sup>˜</sup> _d_ ; and assign _d_ to 

114 

_a_ ˜@ _h_<sup>˜</sup> if it does not violate any constraint in C _F_ . 

The heuristic repeats then these same steps two more times over different target days of the regular season period: first for _D_ as the Fridays, and finally, for _D_ as the Sundays. 

# **B.1.5 Weekday-game heuristic** 

The weekday-game heuristic carries out the following steps, where any condition of feasibility refers to the constraints in C _F_ only: 

- **_Step 1._** _Generate a set of feasible days for the free games._ Initially, create the set _G_<sup>˜</sup> of all free games between non-distant (not farther than 900 miles) rivals. Then, for each ˜ _a_ @ _h_<sup>˜</sup> _∈ G_<sup>˜</sup> , generate the set _D_ (˜ _a_ @ _h_<sup>˜</sup> ) of feasible weekdays (from Monday through Thursday) which ˜ 

- are not within any long-distance trip period for neither _a_ nor _h_<sup>˜</sup> . 

- **_Step 2._** _Define the costs of the potential assignments._ Compute, for each pair of a free game _a_ ˜@ _h_<sup>˜</sup> _∈ G_<sup>˜</sup> and a feasible day _d ∈ D_ (˜ _a_ @ _h_<sup>˜</sup> ), a _game-day assignment cost c_ ([˜ _a_ @ _h_<sup>˜</sup> : _d_ ]) as _nH_ ( _d_ ) + _M_ if the arena of _a_ ˜ is available on day _d_ , and as _nH_ ( _d_ ) otherwise, where _nH_ ( _d_ ) is the amount of teams that have _d_ as one of their arena dates, and _M_ is any big constant (the amount of teams in the League, for example). 

- **_Step 3._** _Evaluate the regrets for the free games._ Compute, for each game _a_ ˜@ _h_<sup>˜</sup> _∈ G_<sup>˜</sup> , the regret _p_ (˜ _a_ @ _h_<sup>˜</sup> ) as the difference between the costs _c_ ([˜ _a_ @ _h_<sup>˜</sup> : _d_<sup>_′′_</sup> ]) and _c_ ([˜ _a_ @ _h_<sup>˜</sup> : _d_<sup>_′_</sup> ]), where _d_<sup>_′_</sup> and _d_<sup>_′′_</sup> are two days in _D_ (˜ _a_ @<sup>˜</sup> _b_ ) corresponding to the first and to the second less costly assignments for _a_ ˜@ _h_<sup>˜</sup> , respectively. If only one day happens to be feasible for a game then make the corresponding regret equal to the assignment cost. 

- **_Step 4._** _Sequentially schedule games to weekdays._ Whenever possible, select (at random if more than one) a free game _a_ ˜@ _h_<sup>˜</sup> _∈ G_<sup>˜</sup> such that the regret _p_ (˜ _a_ @ _h_<sup>˜</sup> ) is the maximum over all free games in _G_<sup>˜</sup> ; and assign the day _d_<sup>_′_</sup> to _a_ ˜@ _h_<sup>˜</sup> , where _d_<sup>_′_</sup> , which is involved in ˜ 

- the computing of _p_ (˜ _a_ @ _h_<sup>˜</sup> ), yields the first less costly assignment for _a_ @ _h_<sup>˜</sup> . After every assignment of a day _d_<sup>_′_</sup> to a game _a_ ˜@ _h_<sup>˜</sup> , update the costs and the regrets for each game in _G_<sup>˜</sup> that involves either _a_ ˜ or _h_<sup>˜</sup> and for which the day _d_<sup>_′_</sup> is also implicated in one of its respective (two) less costly assignments. 

# **B.1.6 Exchange heuristics** 

Both the single and the double exchange heuristics are presented as a recursive procedure on which every call to itself _returns_ an output status indicating whether or not the respective game scheduling has been achieved. Given a partial schedule, the following two definitions regarding the potential assignment of a day _d_ to a free game _a_ ˜@ _h_<sup>˜</sup> must be considered beforehand. We say that any scheduled game on day _d_ is a C0 _-conflicting game for_ 

115 

the assignment [˜ _a_ @ _h_<sup>˜</sup> : _d_ ] if, and only if, the scheduled game involves at least one of the teams ˜ _a_ and _h_<sup>˜</sup> . Moreover, given a non-negative integer _q ≤_ 2, a day _d_ is a _q-interchange feasible day for a_ ˜@ _h_<sup>˜</sup> if _(1)_ there is no conflicting game for [˜ _a_ @ _h_<sup>˜</sup> : _d_ ], but if so, _(2)_ there are at most _q_ conflicting games for [˜ _a_ @ _h_<sup>˜</sup> : _d_ ] and they are scheduled to that same day, _d_ . Naturally, when a day _d_ is a _q_ -interchange feasible day for _a_ ˜@ _h_<sup>˜</sup> , no constraint of the problem is violated if _d_ is assigned to the game _a_ ˜@ _h_<sup>˜</sup> by first canceling all respective C0-conflicting games that _d_ may contain. The single and the double exchange heuristics, therefore, schedule games respectively to 1-interchange and to 2-interchange feasible days. Indeed, whether _q_ = 1 or _q_ = 2, the corresponding exchange heuristic can be seen as a recursive procedure that for each free game _a_ ˜@ _h_<sup>˜</sup> carries out the following steps, where _lmax_ is a given maximum recursive level and any condition of feasibility refers to the constraints in C _F_ only: 

- **_Step 1._** _Try to find a promising day d for the game_ ˜ _a@h_<sup>˜</sup> _._ If all _q_ -interchange feasible days for the game _a_ ˜@ _h_<sup>˜</sup> have already been considered (on possible previous “calls” to the current procedure) then _return “fail”_ ; otherwise, set _d_ as any day selected at random among all the _q_ -interchange feasible days for the game _a_ ˜@ _h_<sup>˜</sup> that minimize the respective number ˜ 

- of conflicting games and that have not yet been selected for _a_ @ _h_<sup>˜</sup> . Go to Step 2. 

- **_Step 2._** _Assign the day d to the game a_ ˜ _@h_<sup>˜</sup> _if it is feasible._ Schedule the game _a_ ˜@ _h_<sup>˜</sup> on the day _d_ if there is no conflicting game for [˜ _a_ @ _h_<sup>˜</sup> : _d_ ] and _return “success”_ ; otherwise, go to Step 3. 

- **_Step 3._** _Schedule a_ ˜ _@h_<sup>˜</sup> _on d and cancel any respective C_ 0 _-conflicting game if a new recursive level is allowed._ If _l_ = _lmax_ then _return “fail”_ ; otherwise, let _G_<sup>_′_</sup> ([˜ _a_ @ _h_<sup>˜</sup> : _d_ ]) be the set of C0-conflicting games for [˜ _a_ @ _h_<sup>˜</sup> : _d_ ], cancel every C0-conflicting game _a_ @ _h ∈ G_<sup>_′_</sup> ([˜ _a_ @ _h_<sup>˜</sup> : _d_ ]), assign _d_ to _a_ ˜@ _h_<sup>˜</sup> , and then go to Step 4. 

- **_Step 4._** _Recursively call the current procedure for the cancelled C_ 0 _-conflicting games for_ [˜ _a@h_<sup>˜</sup> : _d_ ] _._ For each cancelled game _a_ @ _h ∈ G_<sup>_′_</sup> ([˜ _a_ @ _h_<sup>˜</sup> : _d_ ]), call the current procedure (go to Step 1) with _a_ ˜@ _h_<sup>˜</sup> and _l_ being replaced by _a_ @ _h_ and _l_ + 1, respectively. After all those calls have finished (by a “ _return_ ”), go to Step 5. 

- **_Step 5._** _Undo all changes that might have been done by the Step 4 if it has failed to reschedule any of the cancelled C_ 0 _-conflicting games for_ [˜ _a@h_<sup>˜</sup> : _d_ ] _._ If every recursive call from the Step 4 has returned _success_ as final status then _return “success”_ ; otherwise, remove the game _a_ ˜@ _h_<sup>˜</sup> from the day _d_ and undo all changes (new assignments and new cancellations) that might have been done on the partial schedule by the Step 4 when trying to reschedule some C0-conflicting game in _G_<sup>_′_</sup> ([˜ _a_ @ _h_<sup>˜</sup> : _d_ ]), and then go to Step 1. 

116 

# **APPENDIX C** 

# **DESTROY OPERATORS** 

# **C.1 Destroy operators** 

Let _f_ **–** be a function that evaluates the extended incremental cost of removing a game-day assignment [ _a_ @ _h_ : _d_ ] from a schedule _S_ as 



where _f_ **–**<sup>∆(</sup><sup>_a, h, d_)isthecorresponding</sup><sup>_removalincrementalcost_,namely,</sup><sup>_f_(</sup><sup>_S \ {_[</sup><sup>_a_@</sup><sup>_h_:</sup><sup>_d_]</sup><sup>_}_)</sup><sup>_−_</sup> _f_ ( _S_ ); and _A_<sup>¯</sup> _a,h,d_ , which we refer to as the _arena-utility value_ for having the day _d_ assigned to the game _a_ @ _h_ , is a constant given by 



Regarding this evaluation, the lower is the value _f_ **–** ( _a, h, d_ ), the “worse” is the assignment [ _a_ @ _h_ : _d_ ], so the better is its removal from _S_ . In addition, let _f_ **+**<sup>∆(</sup><sup>_a, h, d_)bethe</sup><sup>_insertion_</sup> _incremental cost_ for assigning a day _d_ to a game _a_ @ _h_ , namely, _f_ ( _S ∪{_ [ _a_ @ _h_ : _d_ ] _}_ ) _− f_ ( _S_ ). 

Given a schedule _S_ with _n_ game-day assignments, and the integers _n_ ˆ and _n_ ˜, such that 0 _< n_ ˜ _< n_ ˆ _≤ n_ , the destroy operators in our ALNS algorithm perform the instructions that we informally state below. 

# **C.1.1 Random-based removal** 

_Random-based removal_ ( 01<sup>**_–_**</sup> ) Initially, form a set _S_<sup>ˆ</sup> of target game-day assignments by ˆ ˜ choosing at random _n_ assignments from the schedule _S_ . Then, remove from _S_ the _n_ target assignments in _S_<sup>ˆ</sup> with the lowest extended incremental cost determined by the values of _f_ **–** . 

117 

# **C.1.2 Structure-based removals** 

- _Divisional removal_ ( 02<sup>**_–_**</sup> ) Initially, select at random an NHL division, _TD_<sup>_′_.Then,forma</sup> ˆ 

- set _S_<sup>ˆ</sup> of target game-day assignments by choosing at random _n_ assignments from the current schedule, _S_ , such that each chosen assignment involves at least one team from the division _TD_<sup>_′_.Finally,removefrom</sup><sup>_S_the</sup><sup>_n_˜targetassignmentsin</sup><sup>_S_ˆwiththelowest</sup> extended incremental cost determined by the values of _f_ **–** . 

- _Intradivisional removal_ ( 03<sup>**_–_**</sup> ) Initially, select at random an NHL division, _TD_<sup>_′_.Then,form</sup> ˆ 

- a set _S_<sup>ˆ</sup> of target game-day assignments by choosing at random _n_ assignments from the current schedule, _S_ , such that both teams on each chosen assignment are from the division _TD_<sup>_′_.Finally,removefrom</sup><sup>_S_the</sup><sup>_n_˜ “worst” targetassignments,whicharethe</sup> assignments in _S_<sup>ˆ</sup> with the lowest values of _f_ **–** . 

- _Interdivisional removal_ ( 04<sup>**_–_**</sup> ) Initially, select at random two NHL divisions, _TD_<sup>_′_and</sup><sup>_T_</sup> _D_<sup>_′′_.</sup> ˆ 

- Then, form a set _S_<sup>ˆ</sup> of target game-day assignments by choosing at random _n_ assignments from the current schedule, _S_ , such that each chosen assignment involves a team from the division _TD_<sup>_′_andateamfromthedivision</sup><sup>_T_</sup> _D_<sup>_′′_.Finally,removefrom</sup><sup>_S_the</sup><sup>_n_˜</sup> target assignments in _S_<sup>ˆ</sup> with the lowest extended incremental cost determined by the values of _f_ **–** . 

- _Conferential removal_ ( 05<sup>**_–_**</sup> ) Initially, select at random an NHL conference, _TC_<sup>_′_.Then,form</sup> ˆ 

- a set _S_<sup>ˆ</sup> of target game-day assignments by choosing at random _n_ assignments from the current schedule, _S_ , such that each chosen assignment involves at least one team from the conference _T_<sup>_′_Finally, remove from</sup><sup>_S_the</sup><sup>_n_˜ target assignments in</sup><sup>_S_ˆwith the</sup> _C_<sup>.</sup> 

- lowest extended incremental cost determined by the values of _f_ **–** . 

- _Intraconferential removal_ ( 06<sup>**_–_**</sup> ) Initially, select at random an NHL conference, _TC_<sup>_′_.Then,</sup> ˆ 

- form a set _S_<sup>ˆ</sup> of target game-day assignments by choosing at random _n_ assignments from the current schedule, _S_ , such that both teams on each chosen assignment are from the conference _T_<sup>_′_Finally,removefrom</sup><sup>_S_the</sup><sup>_n_˜targetassignmentsin</sup><sup>_S_ˆwiththelowest</sup> _C_<sup>.</sup> 

- extended incremental cost determined by the values of _f_ **–** . 

- _Interconferential removal_ ( 07<sup>**_–_**</sup> ) Initially, form a set _S_<sup>ˆ</sup> of target game-day assignments by choosing at random ˆ _n_ assignments from the current schedule, _S_ , such that the two teams on each chosen assignment are not from the same conference. Finally, remove from _S_ the _n_ ˜ target assignments in _S_<sup>ˆ</sup> with the lowest extended incremental cost determined by the values of _f_ **–** . 

118 

# **C.1.3 Neighboring-based removals** 

- _Day-neighboring removal_ ( 08<sup>**_–_**</sup> ) Initially, select at random a day _d_<sup>_′_</sup> from the regular season. Then, given a positive integer _q_ , form a set _S_<sup>ˆ</sup> of target game-day assignments by selecting all assignments involving the days from _d_<sup>_′_</sup> to _d_<sup>_′_</sup> + _q_ on the current schedule, ˜ 

- _S_ . Finally, remove from _S_ the _n_ target assignments in _S_<sup>ˆ</sup> with the lowest extended incremental cost determined by the values of _f_ **–** . 

- _Place-neighboring removal_ ( 09<sup>**_–_**</sup> ) Initially, select at random a day _d_<sup>_′_</sup> from the regular season and a team _t_<sup>_′_</sup> from the League. Then, given a positive integer _q_ , form a set _S_<sup>ˆ</sup> of target game-day assignments by selecting the _n_ ˆ assignments on the current schedule, _S_ , involving the geographically closest arenas to the arena of the team _t_<sup>_′_</sup> , and restrict ˜ 

- to the period from _d_<sup>_′_</sup> to _d_<sup>_′_</sup> + _q_ . Finally, remove from _S_ the _n_ target assignments in _S_<sup>ˆ</sup> with the lowest extended incremental cost determined by the values of _f_ **–** . 

# **C.1.4 Critical removals** 

- _Arena-critical removal_ ( 10<sup>**_–_**</sup> ) Repeat the following three steps until at least _n_ ˜ games have been removed from the schedule _S_ : _(1)_ firstly, select at random and then cancel an assignment [˜ _a_ @ _t_<sup>_′_</sup> : _d_<sup>_′_</sup> ] having the minimum arena-utility value over all the current assignments; _(2)_ similarly, select and then cancel some assignment [ _t_<sup>_′_</sup> @ _h_<sup>˜</sup> : _d_<sup>_′′_</sup> ] having the minimum arena-utility value among the current assignments that has _t_<sup>_′_</sup> as the visiting team on a day _d_<sup>_′′_</sup> that, regarding the game _a_ ˜@ _t_<sup>_′_</sup> , does not violate the constraint C6 on the minimum span for similar consecutive visits; _(3)_ eventually, select and remove up to two C _i_ -conflicting games (if any) for the possible assignment of _d_<sup>_′′_</sup> to _a_ ˜@ _t_<sup>_′_</sup> , regarding every constraint C _i_ , with _i_ = 0 _,_ 1 _,_ 2 _,_ 3 _,_ 4, in this order. 

- _Sequential greedy removal_ ( 11<sup>**_–_**</sup> ) Sequentially remove a total of _n_ ˜ games from the schedule _S_ by cancelling, at each time, the game-day assignment with the currently lowest extended incremental cost determined by the value of _f_ **–** . 

- _Cost-critical removal_ ( 12<sup>**_–_**</sup> ) Repeat the following three steps until at least _n_ ˜ games have been removed from the schedule _S_ : _(1)_ firstly, select and then cancel some assignment [˜ _a_ @ _h_<sup>˜</sup> : _d_<sup>˜</sup> ] with the lowest extended incremental cost determined by the value of _f_ **–** over all the current assignments; _(2)_ secondly, among the days provided by the team _h_<sup>˜</sup> , select a C6-feasible day _d_<sup>_′_</sup> for ˜ _a_ @ _h_<sup>˜</sup> having the minimum number of conflicting games on _S_ for the possible assignment of _d_<sup>_′_</sup> to _a_ ˜@ _h_<sup>˜</sup> and, in case of tie, leading to the minimum insertion incremental cost, which is given by the corresponding value of _f_ **+**<sup>∆;</sup><sup>_(3)_eventually, select</sup> and remove up to two C _i_ -conflicting games (if any) for the possible assignment of _d_<sup>_′_</sup> to _a_ ˜@ _h_<sup>˜</sup> , regarding every constraint C _i_ , with _i_ = 0 _,_ 1 _,_ 2 _,_ 3 _,_ 4, in this order. 

119 

# **C.1.5 Trip-based removals** 

- _Short-trip removal_ ( 13<sup>**_–_**</sup> ) Repeat the following three steps until at least _n_ ˜ games have been removed from the schedule _S_ : _(1)_ firstly, select at random a trip _r_ ˜ having the minimum number of games and remove all them from the schedule; _(2)_ secondly, for each game _a_ ˜@ _h_<sup>˜</sup> removed from the trip _r_ ˜, select, among the days provided by the team ˜ ˜ _h_ , a C6-feasible day _d_<sup>_′_</sup> for _a_ ˜@ _h_ having the minimum number of conflicting games on _S_ for the possible assignment of _d_<sup>_′_</sup> to _a_ ˜@ _h_<sup>˜</sup> and, in case of tie, yielding the minimum incremental cost on the objective function, which is given by the corresponding value of _f_ **+**<sup>∆;</sup><sup>_(3)_eventually,selectandremoveuptotwoC</sup><sup>_i_-conflictinggames(ifany)for</sup> the assignment of _d_<sup>_′_</sup> to _a_ ˜@ _h_<sup>˜</sup> , regarding every constraint C _i_ , with _i_ = 0 _,_ 1 _,_ 2 _,_ 3 _,_ 4, in this order. 

- _Close-trips removal_ ( 14<sup>**_–_**</sup> ) Initially, select from _S_ two consecutive trips, _r_ ˜1 and _r_ ˜2, for the same visiting team, that minimize the number of days between the end of trip ˜ _r_ 1 and the ˜ ˆ 

- begin of _r_ 2; Then, form a set of target game-day assignments by choosing the _n_ current assignments with the minimum arena-utility value on _S_ , among the games (for any pair of teams) scheduled to days between the begin of trip _r_ ˜1 and the end of _r_ ˜2; Finally, ˜ 

- remove from _S_ the _n_ target assignments in _S_<sup>ˆ</sup> with the lowest extended incremental cost determined by the values of _f_ **–** . 

- _Scattered-trip removal_ ( 15<sup>**_–_**</sup> ) Initially, given a positive integer _q_ , select from _S_ a trip _r_ ˜ with at least _q_ days long and that maximizes the ratio of its number of days to its number of ˆ 

- games; Then, form a set of target game-day assignments by choosing the _n_ assignments with the minimum arena-utility value on _S_ , among the games (for any pair of teams) scheduled to days between the begin and the end of the trip _r_ ˜; Finally, remove from _S_ the _n_ ˜ target assignments in _S_<sup>ˆ</sup> with the lowest extended incremental cost determined by the values of _f_ **–** . 

120 

# **APPENDIX D** 

# **REPAIR OPERATORS** 

# **D.1 Repair operators** 

Let _f_ **+** be a function that evaluates the extended incremental cost of inserting a game-day assignment [ _a_ @ _h_ : _d_ ] in a schedule _S_ as 



where _f_ **+**<sup>∆(</sup><sup>_a, h, d_) is the corresponding</sup><sup>_insertionincrementalcost_, namely,</sup><sup>_f_(</sup><sup>_S ∪{_[</sup><sup>_a_@</sup><sup>_h_:</sup><sup>_d_]</sup><sup>_}_)</sup><sup>_−_</sup> _f_ ( _S_ ); and _A_<sup>¯</sup> _a,h,d_ is the _arena-utility value_ for having the day _d_ assigned to the game _a_ @ _h_ , as defined in Appendix C.1. Regarding this evaluation, the lower is the value _f_ **+** ( _a, h, d_ ), the “better” is the insertion of the assignment [ _a_ @ _h_ : _d_ ] in the schedule _S_ . In addition, let _Dt_ be the set of arena dates provided by a team _t_ , and regarding a schedule _S_ , let a day _d_ be called a _free day_ for a game _a_ @ _h_ if neither the team _a_ nor the team _h_ is currently scheduled to play on day _d_ of the schedule _S_ . 

Given a partial schedule and a set of free games, the repair operators in our ALNS algorithm perform the instructions that we informally state below. 

# **D.1.1 Greedy-based insertions** 

- _Single-evaluation greedy insertion_ ( 01<sup>**_+_**</sup> ) Initially, evaluate by _f_ **+** the extended incremental ˜ ˜ 

- cost of each pair of free game _a_ @ _h_<sup>˜</sup> and arena-feasible day _d ∈ Dh_ that is a free day for _a_ ˜@ _h_<sup>˜</sup> in the current schedule. Then, select in a random order all the free games and, for ˜ ˜ 

- each selected game _a_ @ _h_<sup>˜</sup> , proceed as follows: _(1)_ verify whether there are days from _Dh_ that are still free for _a_ ˜@ _h_<sup>˜</sup> in the current schedule, and if so, _(2)_ select among them a day _d_<sup>_′_</sup> for which the respective cost evaluated at the beginning of the heuristic is the ˜ 

- lowest, and _(3)_ update the current schedule by assigning _d_<sup>_′_</sup> to _a_ @ _h_<sup>˜</sup> . Finally, if not all the free games have been scheduled then repeat this approach by considering all free ˜ 

- days (instead of only the arena-feasible days, _Dh_ ) in the current schedule. 

- _Updated-evaluation greedy insertion_ ( 02<sup>**_+_**</sup> ) Select all the free games, one at a time, by first choosing a team _h_<sup>˜</sup> with the maximum number of free home games and then choosing a team _a_ ˜ with the maximum number of free away games among which at least one is against _h_<sup>˜</sup> . Each time a game ˜ _a_ @ _h_<sup>˜</sup> is selected, proceed as follows: _(1)_ verify whether there 

121 

˜ ˜ are days from _Dh_ that are still free for _a_ @ _h_<sup>˜</sup> in the current schedule, and if so, _(2)_ select among them a day _d_<sup>_′_</sup> leading to the lowest extended incremental cost determined by the value of _f_ **+** with respect to the current schedule, and _(3)_ update the schedule by ˜ assigning _d_<sup>_′_</sup> to _a_ @ _h_<sup>˜</sup> . If not all the free games have been scheduled then repeat this ˜ approach by considering all free days (instead of only the arena-feasible days, _Dh_ ) in the current schedule. 

# **D.1.2 Regret-based insertion** 

Let _f_ **+**<sup>_A_(</sup><sup>_a, h, d_)beafunctionthatevaluatesthecostofschedulingafreegame</sup><sup>_a_@</sup><sup>_h_toa</sup> corresponding arena-feasible date _d_ that is free on a partial schedule _S_ as 



where _M_ 1 and _M_ 2 are large constants, such that _M_ 1 _≫ M_ 2; _Aa,d_ is equal to 1 if the day _d_ is also provided by the away team _a_ , and equal to 0 otherwise; _f_ **+**<sup>∆(</sup><sup>_a, h, d_)istheincremental</sup> cost of assigning _d_ to _a_ @ _h_ , namely, _f_ ( _S ∪{_ [ _a_ @ _h_ : _d_ ] _}_ ) _− f_ ( _S_ ); and _|G_<sup>˜</sup> ( _d_ ) _|_ , which can be seen as a “competitiveness” factor for _d_ , is the current number of free games that are arena-feasible (it would satisfy C1) for the day _d_ . 

_Max-regret insertion_ ( 03<sup>**_+_**</sup> ) Whenever there is still any free game, proceed as follows: _(1)_ evaluate the _regret value_ of each free game as the difference between its two lowest costs of _f_ **+**<sup>_A_,whichareprovidedbytwocorrespondingarena-feasibledatesthatturns</sup> out to be free days in the current schedule; _(2)_ select a free game _a_ ˜@ _h_<sup>˜</sup> for which the regret value is the maximum over all free games; and _(3)_ update the current schedule by assigning to _a_ ˜@ _h_<sup>˜</sup> the respective lowest-cost day (with regard to the function _f_ **+**<sup>_A_).</sup> 

# **D.1.3 exchange-based insertion** 

Let _a_ ˜@ _h_<sup>˜</sup> be a free game and let _D_<sup>_′_</sup> (˜ _a_ @ _h_<sup>˜</sup> ) be its set of _1-exchange feasible days_ , which are either feasible days for _a_ ˜@ _h_<sup>˜</sup> or days that would become feasible by first removing a single (conflicting) game currently scheduled on any day. If feasible days are available, the current free game is scheduled to a day _d_<sup>ˆ</sup> _∈ D_<sup>_′_</sup> (˜ _a_ @ _h_<sup>˜</sup> ) that maximizes the corresponding arena-utility value, _A_<sup>¯</sup> _a,_ ˜ _h,_ ˜ ˆ _d_ ; otherwise, only days that would result in a single conflicting game are considered. In this case, the current free game is assigned to a day _d_<sup>ˆ</sup> _∈ D_<sup>_′_</sup> (˜ _a_ @ _h_<sup>˜</sup> ) that maximizes, over all 1-exchange feasible days, the respective arena-utility difference, _A_<sup>¯</sup> _a,_ ˜ _h,_ ˜ ˆ _d − A_<sup>¯</sup> _a′,h′,d′_ , where the game _a_<sup>_′_</sup> @ _h_<sup>_′_</sup> , currently scheduled on a day _d_<sup>_′_</sup> (which is not necessarily equal to _d_<sup>ˆ</sup> ), is the ˜ conflicting game for the assignment of _d_<sup>ˆ</sup> to _a_ @ _h_<sup>˜</sup> . 

122 

- _Single-exchange insertion_ ( 04<sup>**_+_**</sup> ) Select all the free games, one at a time, in decreasing order of their quantity for the same _away-home_ pair of teams. Try to insert each selected game _a_ ˜@ _h_<sup>˜</sup> in the current schedule, _S_ , by calling the _single-exchange procedure_ while considering the 1-exchange feasible days with regard to all the constraints of the problem and selecting the most promising day as the one that _(1)_ maximizes the arena-utility value over feasible days (if any) or _(2)_ maximizes the difference between the arena-utility value for a 1-exchange feasible day and the arena-utility value for the corresponding conflicting game in _S_ (otherwise). Eventually, apply the strategy from _Updated-evaluation greedy insertion_ (02<sup>**_+_**</sup> ) whenever no 1-exchange feasible day exists for a free game. 

# **D.1.4 Fleurent’s approach-based insertion** 

- _Fleurent’s approach-based insertion_ ( 05<sup>**_+_**</sup> ) Initially, apply the _forced-trip heuristic_ but, instead of building one entire trip at a time, proceed as follows. At first, create trips made up of exactly two long-distance visits, such that each visit is scheduled during a period with no other game between two consecutive arena-available dates for the corresponding away team. After having created as many of such “partial” trips as possible, try to extend the current long-distance trips by only scheduling free games that define long-distance visits. Subsequently, apply the _free-trip heuristic_ with no modifications. Then, apply the _weekend-game heuristic_ to all the free games (not only those concerning long-distance visits) by trying to schedule them on any free weekend day that provides a feasible assignment, even if it is a day within a period of a long-distance trip for the respective teams. Finally, apply the _weekday-game heuristic_ to all the free games (not only those concerning long-distance visits) by trying to schedule them to any free weekday that provides a feasible assignment, even if it is a day within a period of a long-distance trip for the respective teams. In addition, replace the _nH_ ( _d_ ) from the _weekday-game heuristic_ , which is the amount of teams that are available on a day _d_ , by the number of free games that are actually feasible candidates for _d_ at the moment of each evaluation. Eventually, apply the strategy from _Max-regret insertion_ (03<sup>**_+_**</sup> ) if there still is any free game. 


