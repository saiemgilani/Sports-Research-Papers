<!-- source: randoms/Variations_on_multimedia_data_mining.pdf -->

The Sixth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining 



Working Notes Workshop on Multimedia Data Mining August 20, 2000 Boston, MA, USA Chairs Simeon J. Simo�, University of Sydney Osmar R. Zaiane, University of Alberta 



<!-- Start of picture text -->
2000<br>MDM/KDD<br><!-- End of picture text -->

## **Proceedings of the First International Workshop on** 

# **Multimedia Data Mining (MDM/KDD’2000)** 

**August 20, 2000 Boston, MA, USA** 

**Edited by: Simeon J. Simoff and Osmar R. Zaïane** 

in conjunction with 

**Sixth ACM SIGKDD International Conference on** 

**Knowledge Discovery & Data Mining August 20 - 23, 2000, Boston, MA, USA** 

Web Page: http://www.cs.ualberta.ca/~zaiane/mdm_kdd2000/ 

© The copyright of these papers belongs to the paper's authors. Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000  (S.J. Simoff, O.R. Zaïane, eds.) 

The official workshop web site is: http://www.cs.ualberta.ca/~zaiane/mdm_kdd2000/ 

An electronic version of the proceedings will be archived after the workshop at the ACM digital library archive site: http://www.acm.org/sigkdd/proceedings/mdmkdd00/ 

iv 

##### **Foreword** 

Multimedia computing, especially networked multimedia, in science, business, academia, medicine and government generates substantial amount of digital media data sets. Vinton G. Cerf, President of the Internet Society and Senior Vice-President of MCI Data Services compares the activities surrounding multimedia ideas with the metaphor of a disturbed ant hill, in which the inhabitants run hither and yon to discover the cause of disturbance and, perhaps, to do something about it. No wonder researchers and developers in multimedia information systems turn to data mining and knowledge discovery methods looking for techniques for improving the indexing and retrieval of necessary information out of these data sets. Furthermore, as the ultimate goal of the knowledge discovery process is turning data into knowledge, there is a need for methods, techniques and tools that on the one hand, extract patterns from such divergent data sets and transform them into useful information and knowledge, and, on the other hand, provide consistent framework for incorporation and use of discovered knowledge in the information systems. 

This volume contains the papers selected for presentation at the First International Workshop on Multimedia Data Mining (MDM/KDD’2000) held in conjunction with the Sixth ACM SIGKDD International Conference on Knowledge Discovery & Data Mining in Boston, Massachusetts, USA on August 20<sup>th</sup> , 2000. The aim of the workshop is to bring together experts in analysis of digital media, state-of-art data mining and knowledge discovery in multimedia database systems, knowledge engineers and domain experts from various applied disciplines with potential in multimedia data mining. The papers in this volume describe recent advances both in theoretical and practical aspects of data mining in digital media representations. They are grouped in the following streams: 

- Mining spatial multimedia data 

- Mining audio data 

- Mining image and video data 

- Multimedia support for data mining 

The papers are of particular interest to researchers, developers and users of advanced data analysis and mining methodologies. 

KDD conference series is a very competitive forum and winning a space and time to conduct a workshop is not a trivial task. We would like to thank all those, who anticipated the need in a multimedia data mining workshop and continuously supported our efforts through all the stages - from the submission of competitive proposal to bringing the workshop to reality. There were 27 submitted papers from 12 different countries: Australia, Belgium, Canada, China, France, Germany, Japan, Malaysia, Switzerland, Taiwan, United Kingdom, and United States of America. All papers were extensively reviewed by three referees drawn from the program committee and external reviewers. Special thanks go to them for the final quality of selected papers depends on their efforts. 

Simeon J. Simoff  &  Osmar R. Zaïane July 2000 

v 

##### **Workshop Chairs:** 

- Simeon J. Simoff, University of Sydney, Australia 

- Osmar R. Zaïane, University of Alberta, Canada 

##### **Program Committee** 

- Max Bramer, University of Portsmouth,UK 

- Alex Duffy, University of Strathclyde,UK 

- Max J. Egenhofer, University of Maine, USA 

- Tom Gedeon, Murdoch University, Australia 

- William Grosky, Wayne State University, USA 

- Howard J. Hamilton, University of Regina, Canada 

- Jiawei Han, Simon Fraser University, Canada 

- Odej Kao, Technical University of Clausthal, Germany 

- Nik Kasabov, University of Ottago, New Zealand 

- Raymond Ng, University of British Columbia, Canada 

- Timothy K. Shih, Tamkang University, Taiwan 

- Jaideep Srivastava , University of Minnesota, USA 

##### **External Reviewers** 

- Terry Caelli 

- Hang Cui 

- Mohammad El Hajj 

- Randy Goebel 

- Mark Haffey 

- Kamran Karimi 

- Mario Nascimento 

- Tong Zheng 

##### **Acknowledgements** 

Special thanks and appreciation go to Osmar Zaïane for his tremendous organisational and intellectual effort and input in the paper collection, organisition of the review process and the camera ready version of the proceedings. 

vi 

##### **Program for MDM/KDD2000 Workshop** Sunday, August 20, 2000, Boston, MA, USA 

###### **8:45 - 9:00** Opening and Welcome 

###### **9:00 - 10:00** Session 1 (Mining Spatial Multimedia Data) 

- 09:00- 09:20 Geo-Spatial Clustering with User-Specified Constraints 

   - Anthony K.H. Tong, Raymond T. Ng, Laks V.S. Lakshmanan, Jiawei Han 

- 09:20- 09:40 Multi-level Indexing and GIS Enhanced Learning for Satellite Imageries 

   - Krzysztof Koperski and Giovanni B. Marchisio 

- 09:40-10:00 Predicting Locations Using Map Similarity(PLUMS): A Framework for Spatial Data Mining.     Sanjay Chawla, Shashi Shekhar, Weili Wu and Uygar Ozesmi 

###### **10:00 - 10:30** Coffee break 

###### **10:30 - 12:00** Session 2 (Mining Audio Data & Multimedia Support) 

- 10:30-10:50 Learning Prosodic Patterns for Mandarin Speech Synthesis Yiqiang Chen, Wen Gao, Tingshao Zhu 

- 10:50-11:10 Unsupervised Classification of Sound for Multimedia Indexing Bruce Matichuk, Osmar R. Zaïane 

- 11:10-11:30 Effective Retrieval of Audio Information from Annotated Text Using Ontologies Latifur Khan and Dennis McLeod 

- 11:30-11:50 Incorporating Domain Knowledge with Video and Voice Data Analysis in News Broadcasts.    Kim Shearer, Chitra Dorai, Svetha Venkatesh 

- 11:50-12:10 Multimedia Support for Complex Multidimensional Data Mining Monique Noirhomme-Fraiture 

###### **12:00 - 13:00** Lunch 

###### **13:00 - 15:00** Session 3 (Mining Image and Video Data) 

- 13:00-13:20 A Self Organizing Map (SOM) Extended Model for Information Discovery in a 

   - Digital Library Context.  Jean-Charles Lamirel, Jacques Ducloy, Hager Kammoun 

- 13:20-13:40 Learning Feature Weights from User Behavior in Content-Based Image Retrieval Henning Müller, Wolfgang Müller, David McG Squire 

- 13:40-14:00 When image indexing meets knowledge discovery Chabane Djeraba 

- 14:00-14:20 Semantic indexing and temporal rule discovery for time-series sattelite images Rie Honda, Osamu Konoshi 

- 14:20-14:40 Data Mining from Functional Brain Images Mitsuru Kakimoto, Chie Morita, Yoshiaki Kikuchi, Hiroshi Tsukimoto 

- 14:40-15:00 Mining Cinematic Knowledge Work in Progress- An Extended Abstract Duminda Wijesekera and Daniel Barbara 

###### **15:00-16:00** Session 4 (Discussion) 

- 15:00-15:15 Variations on Multimedia Data Mining 

   - Simeon J. Simoff 

- 15:15-16:00 Discussion: What does Multimedia Mining encompass and what are the open issues 

###### **16:00-16:30** Coffee break 

###### **16:30 - 19:00** SIGKDD'2000 Conference Opening and awards 

vii 

viii 

##### **Table of Contents** 

|Geo-Spatial Clustering with User-Specified Constraints|
|---|
|Anthony K.H. Tong, Raymond T. Ng, Laks V.S. Lakshmanan, Jiawei Han  …………………. 1|
|Multi-level Indexing and GIS Enhanced Learning for Satellite Imageries<br>Krzysztof Koperski, Giovanni B. Marchisio …………………………………………………… 8|
|Predicting Locations Using Map Similarity(PLUMS): A Framework for Spatial Data Mining.<br>Sanjay Chawla, Shashi Shekhar, Weili Wu, Uygar Ozesmi …………………………………... 14|
|Learning Prosodic Patterns for Mandarin Speech Synthesis|
|<br>Yiqiang Chen, Wen Gao, Tingshao Zhu ………………………………………………………..25|
|Unsupervised Classification of Sound for Multimedia Indexing<br>Bruce Matichuk, Osmar R. Zaïane ……………………………………………………………...31|
|Effective Retrieval of Audio Information from Annotated Text Using Ontologies<br>Latifur Khan, Dennis McLeod ………………………………………………………………... 37|
|Incorporating Domain Knowledge with Video and Voice Data Analysis in News Broadcasts.<br>Kim Shearer, Chitra Dorai, Svetha Venkatesh ………………………………………………... 46|
|Multimedia Support for Complex Multidimensional Data Mining<br>Monique Noirhomme-Fraiture …………………………………………………………………54|
|A self organizing map (SOM) extended model for information discovery in a digital library<br>context.  - Jean-Charles Lamirel, Jacques Ducloy, Hager Kammoun …………………………60|
|Learning Feature Weights from User Behavior in Content-Based Image Retrieval<br>Henning Müller, Wolfgang Müller, David McG Squire ……………………………………… 67|
|When image indexing meets knowledge discovery<br>Chabane Djeraba ……………………………………………………………………………… 73|
|Semantic indexing and temporal rule discovery for time-series sattelite images<br>Rie Honda, Osamu Konoshi …………………………………………………………………... 82|
|Data Mining from Functional Brain Images<br>Mitsuru Kakimoto, Chie Morita, Yoshiaki Kikuchi, Hiroshi Tsukimoto ……………………... 91|
|Mining Cinematic Knowledge Work in Progress- An Extended Abstract<br>Duminda Wijesekera, Daniel Barbara ………………………………………………………… 98|
|Variations on Multimedia Data Mining|
|Simeon J. Simoff ………………………………………………………………………………104|



ix 

x 

Geo-spatial Clustering with User-Sp eci�ed Constraints. � Anthony K. H. Tung y Raymond T. Ng Laks V.S. Lakshmanan Jiawei Han Simon Fraser U. U. of British Columbia I IT, Bombay & Concordia U. Simon Fraser U. khtung@cs.sfu.ca rng@cs.ub c.ca laks@cs.concordia.ca han@cs.sfu.ca Abstract ing metho ds [KR90, NH94, BFR98], hierarchical Capturing application semantics and allowing a human metho ds [KR90, ZRL96, GRS98, KHK99], densityanalyst to express his fo cus in mining have b een the based metho ds [EKSX96, ABKS99, HK98], gridmotivation for several recent studies on constrained mining. based metho ds [WYM97, SCZ98, AGGR98], and In this pap er, we intro duce and study the problem of mo del-based metho ds [SD90, Fis87, CS96, Koh82]. constrained clustering|�nding clusters that satisfy certain user-sp eci�ed constraints. We argue that this problem arises In the context of GIS, cluster analysis can b e very naturally in practice. Two typ es of constraints are discussed useful in identifying groups of similar p oints on the in this pap er. The �rst typ e of constraints are imp osed by map and p erforming detail analysis of each group. physical obstacles that exist in the region of clustering. The This can b e useful for tasks like facilities planning second typ e of constraints are SQL constraints which every cluster must satisfy. We provide a prelimary intro duction since a facility can then b e allo cated to serve each to b oth typ es of constraints and discuss some techniques for group of ob jects separately. solving them. Unfortunately, the task of planning the lo cation of facilities is usually quite complicated since users 1 Intro duction could like to enforce some constraints when p erforming such a task. One p ossible constraint might Cluster analysis, which groups data for �nding overb e due to the existence of obstacles in the clustering all distribution patterns and interesting correlations region. Let us illustrate this with an example. among data sets, has numerous applications in pattern recognition, spatial data analysis, image proExample 1.1 A bank manager wishes to locate 4 cessing, market research, etc. Cluster analysis has ATMs in the area shown in Figure 1a to serve b een an active area of research in computational the customers who are represented by points in the statistics and data mining, with many e�ective and �gure. In such a situation however, obstacles may scalable clustering metho ds develop ed recently. exist in the area which should not be ignored. This These metho ds can b e categorized into partitionis because ignoring these obstacles wil l result in � Research was supp orted in part by research grants clusters like those in Figure 1b which are obviously from the Natural Sciences and Engineering Research Council wrong. Since cluster C1 for example is split by a of Canada, and grants NCE:IRIS3 and NCE:GEOID from the Networks of Centres of Excellence of Canada. river, some customers on one side of the river wil l yPerson handling corresp ondence. Postal Address: Computhave to travel a long way to the al located ATM on ing Science, Simon Fraser University, 8888 University Drive, Burnaby, B. C., Canada. the other side of the river. 2 



Besides constraints imp osed by obstacles, users © The copyright of this paper belongs to the paper's authors. Permission to copy without can also face constraints due to op erational requirefee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. ment as follows. Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 (O.R. Zaïane, S.J. Simoff, eds.) Example 1.2 Consider a package delivery company which is seeking to use a GIS to help de- 

1 

clustering is a very practical problem faced by the users who are not givenen waysaysys to sp ecify the typyp e ofofclusteringclustersthis, clustersthis, thatintrothistrotheypapduceerwantanttheandt theypapduceerwantanttheandt wantanttheandt tonotionintrodiscovered.tro discovered.tro Ininitialview view ofclusteringclustersthis, this, weinethatintrothistrotheypapduceerwantanttheandt introthistrotheypapduceerwantanttheandt duceerwantanttheandt theandt notionintrodiscovered.tro ofered.someconstrainedIninitialview constrainedIninitialview clusteringclustersthis, inethatintrothistrotheypapduceerwantanttheandt thistrotheypapduceerwantanttheandt papduceerwantanttheandt erwantanttheandt andt introdiscovered.tro ducevered.ofered.someconstrainedIninitialview someconstrainedIninitialview initialview workork whichh is b eing done to address these problems. Thefollows.ws.organizationIn organizationIn ofnextthesection,rest thesection,rest rest of thise pap ergiveeis is as follows.ws.organizationIn In the nextthesection,rest section,rest wethise willpap giveeis anas introtro duction to the problem of clustering with obstacles entities.tities. Wee will describ ed techniqueshniques whichh are used to improvevee the scalabilityy of our algorithm when obstacle constraintsts are takenen intoto consideration.theconstraintsclusteringpapproblemertswithwithandofSectionsuchdiscussInclusteringh Inclusteringh Section4.somewith3,ts.prelimaryweWeeSQLe 3,ts.prelimaryweWeeSQLe weWeeSQLe willaggregateconcludeworkloorkok loorkok ok at theconstraintsclusteringpapproblemertswithwithandofSectionsuchdiscussInclusteringh problemertswithwithandofSectionsuchdiscussInclusteringh ofSectionsuchdiscussInclusteringh clusteringh with3,ts.prelimaryweWeeSQLe SQLe aggregateconcludeworkloorkok constraintsclusteringpapproblemertswithwithandofSectionsuchdiscussInclusteringh andofSectionsuchdiscussInclusteringh discussInclusteringh somewith3,ts.prelimaryweWeeSQLe prelimaryweWeeSQLe workloorkok onat clusteringpapproblemertswithwithandofSectionsuchdiscussInclusteringh withandofSectionsuchdiscussInclusteringh suchdiscussInclusteringh constraints.Section4.somewith3,ts.prelimaryweWeeSQLe WeeSQLe willwillaggregateconcludeworkloorkok concludeworkloorkok ourconsideration.theconstraintsclusteringpapproblemertswithwithandofSectionsuchdiscussInclusteringh papproblemertswithwithandofSectionsuchdiscussInclusteringh ertswithwithandofSectionsuchdiscussInclusteringh withwithandofSectionsuchdiscussInclusteringh SectionsuchdiscussInclusteringh 4.somewith3,ts.prelimaryweWeeSQLe 

river ���� ����� users who are not givenen waysaysys to sp ecify the typyp e ����������������������������������������������� �������������������������� bridge � ofofclusteringclustersthis, weinethatintrothistrotheypapduceerwantanttheandt tonotionintrodiscovered.tro ducevered.ofered.someconstrainedIninitialview � � ����� hill ��������� workork whichh is b eing done to address these problems. river ������ �� ����� ����� ���� Thefollows.ws.organizationIn the ofnextthesection,rest of wethise willpap ergiveeis anas introtro duction to the problem of clustering with (a) Customers' lo cation and obstacles. obstacles entities.tities. Wee will describ ed techniqueshniques whichh are used to improvevee the scalabilityy of our � ����� algorithm when obstacle constraintsts are takenen intoto � �� ������������������������ C1 ���������� ��������������������� C3 ������������� C2 � ������������������������� C4 ���������� �� ourconsideration.theconstraintsclusteringpapproblemertswithwithandofSectionsuchdiscussInclusteringh constraints.Section4.somewith3,ts.prelimaryweWeeSQLe willwillaggregateconcludeworkloorkok onat ���� �������� ����� � ������ 2 Clustering with Obstacle Entitiestities (COE) (b) Clusters formed when ignoring In order to solvee the problem shownwn in Example 1.1, obstacles. let us �rst formally de�ned the problem as follows.ws. Figure 1: Planning the lo cation of ATMs De�nition 2.1 We aree given a set P of n pointsoints fp1p11 ; p22 ; :::; pnn g and a set O of m non-intersectingtersecting termine the lo cations for k service stations in a obstacles fo1o11 ; :::; omm g in a two dimensional region,egion,gion, city. Supp ose the GIS contains the information of R . Each obstacle oii is representedepresentedesentedd by a simple customers based on the scheme: customer (N ame, polygonolygon with oii :nv sides and eachach vertex of the Addr X coor d,Addr Y coor d, M ember T y pe, polygonolygon is denotedd as oii :vjj , 1 � j � oii :nv . Av g M onthC hg ). The company may formulate The distance,e, dff (p;p; q ) betweenetweenen any two points,oints, p this lo cation selection problem as an instance of and q is de�nedd as the length of the shortest the clustering problem, using the address �elds Euclideanan pathath fromom p to q without cutting throughough Addr X coor d and Addr Y coor d to de�ne the disany obstacles. Too distinguish this distancee fromom tance function df (). the directectct Euclideanan distance,e, we wil l referefer to this Supp ose further that the company has two kinds distancee as obstructed distance in this paper.aper.er. Our of customers in consideration: gold customers, objectivective is to partitionartition P into k clusters C l11 ; :::; C lkk who need frequent, regular services, and ordinary such that the fol lowing square-errore-erroror function, E , is customers, who require o ccasional services. In minimized:d: order to save the cost and provide go o d service, the manager may add the following constraints: E = Pki=1ki=1i=1=1 Pp2Cp2C2CC lii d22 (p;p; mii ) (1) that each station should serve at least 50 In order to solve the ab ove problem, a trivial gold customers; and (2) that each station should solution is to argue that obstacles in e�ect only serve at least 5000 ordinary customers. With cause a change in the distance function and thus the constraints, this b ecomes an instance of the can b e hidden from the actual clustering algorithm constrained clustering problem. 2 by simply providing a di�erent distance function As can b e seen, the problem of constrained call to it. However our work in [THH00] shows that 

2 Clustering with Obstacle Entitiestities (COE) In order to solvee the problem shownwn in Example 1.1, let us �rst formally de�ned the problem as follows.ws. De�nition 2.1 We aree given a set P of n pointsoints fp1p11 ; p22 ; :::; pnn g and a set O of m non-intersectingtersecting obstacles fo1o11 ; :::; omm g in a two dimensional region,egion,gion, R . Each obstacle oii is representedepresentedesentedd by a simple polygonolygon with oii :nv sides and eachach vertex of the polygonolygon is denotedd as oii :vjj , 1 � j � oii :nv . The distance,e, dff (p;p; q ) betweenetweenen any two points,oints, p and q is de�nedd as the length of the shortest Euclideanan pathath fromom p to q without cutting throughough any obstacles. Too distinguish this distancee fromom the directectct Euclideanan distance,e, we wil l referefer to this distancee as obstructed distance in this paper.aper.er. Our objectivective is to partitionartition P into k clusters C l11 ; :::; C lkk such that the fol lowing square-errore-erroror function, E , is minimized:d: E = Pki=1ki=1i=1=1 Pp2Cp2C2CC lii d22 (p;p; mii ) 

2 

a clustering algorithm which takes these obstacles First, a pre-clustering step similar to those in into consideration can in fact b e optimized to BIRCHCH [ZRL96],], ScaleKM [BFR98]] and improve clustering eÆciency. [KHK99]] is takenen to group the ob jects intoto a set of In [THH00], we develop ed a clustering algorithm micro-clusters.o-clusters.. Gantiti et. al. in [GGR99] giveses an called COE-CLARANS to handle clustering with analogy to pre-clustering as follow:w: obstacles. COE-CLARANS is an improved version "... if eachh data p ointt is a marble on a table of CLARANS in [NH94] which is a k -medoid top, wee replace clusters of marbles byy tennis clustering algorithm. The CLARANS algorithm balls and then lo ok for clusters of tennis �rst randomly cho oses k ob jects as the set of cluster balls." centers, cur r ent. It then assigns the rest of the ob jects to the nearest cluster center and compute A micro-clustero-cluster is the tennis ball in the analogy.. the square-error function E for the initial solution. It is a group of p ointsts whichh are so close to eachh A search is then done for a b etter solution by taking other that they are veryery likelyely to b elong to the each cluster center following randomize order and same cluster. Too compress the data set, a p ointt trying to replace it with another randomly selected from eachh micro-cluster is selected to representt the ob ject not in cur r ent. If a b etter solution is found, micro-cluster. Since the size of these representativetativee i.e,. a lower value of E is computed for the new p ointsts is muchuchh smaller than the actual data set, solution, cur r ent is set to the new solution and the they could b e clustered using the COE-CLARANS whole pro cess is rep eated with the new cur r ent. algorithm in the main memory.. Too facilitate the For each cluster center, the attempt to �nd a clustering, information ab out the micro-cluster are b etter solution by center replacment is rep eated stored together with the representativetativee p oints.ts. This maxneig hbor times and the b est solution is kept. information wouldould include statistic likee the numbumbb er If no b etter solution is found after maxneig hbor of p ointsts in the micro-cluster, the diameter of the attempts on all the k cluster centers, it is concluded micro-cluster, etc. that a lo cal minima is reached. This pro cess rep eats Second, to avoid the unnecessary computation numl ocal times and the b est lo cal minima that is of the square-error function E , an initial lower found will b e output as the solution. b ound of E , E 0 , is �rst computed. If E 0 is There are however certain issues which must b e already higher than the b est solution so far, then addressed in order to adopt CLARANS to cluster the generated solution can never b e b etter than the ob jects with obstacle constraints imp osed. As b est solution and thus can b e abandoned without can b e seen, CLARANS is a generate-and-test the need for E to b e computed. To compute algorithm which frequently recompute the squareE 0 , we underestimate the distance b etween the error function E for testing a generated solution. randomly chosen center or andom and the microTo p erform this op eration, a scan must b e done clusters by using direct Euclidean distance instead through the n ob jects to compute their distance of the obstructed distance. By doing so, each microfrom their cluster center. If the ob jects are stored clusters so formed will fall into one of the following in secondary storage, high I/O cost will b e incurred. categories: Furthermore, since the solution is generated by 1) p is correctly assigned to orr andom . randomly picking another ob ject to replace a cluster Since the direct Euclidean distance b etweenweeneen p and center, there is a go o d chance that it is not a orr andom mustust b e shorter than the obstructed disb etter solution and thus do es not justify the time tance b etweenweeneen p and orr andom , wee havevee underestisp ent on computing E . In the case of clustering mate the actual distance b etweenweeneen p and orr andom . with obstacles, such overhead is even higher as the 2) p is wrongly assigned to or andom . obstacles have complicated the distance function. Let oi b e the cluster center that p should rightfully In order to overcome these problems, the following b e assigned to. Since p is assigned to or andom two approaches are adopted. instead, the direct Euclidean distance b etween p 

First, a pre-clustering step similar to those in BIRCHCH [ZRL96],], ScaleKM [BFR98]] and CHAMELEON [KHK99]] is takenen to group the ob jects intoto a set of micro-clusters.o-clusters.. Gantiti et. al. in [GGR99] giveses an analogy to pre-clustering as follow:w: "... if eachh data p ointt is a marble on a table top, wee replace clusters of marbles byy tennis balls and then lo ok for clusters of tennis balls." 

A micro-clustero-cluster is the tennis ball in the analogy.. It is a group of p ointsts whichh are so close to eachh other that they are veryery likelyely to b elong to the same cluster. Too compress the data set, a p ointt from eachh micro-cluster is selected to representt the micro-cluster. Since the size of these representativetativee p ointsts is muchuchh smaller than the actual data set, they could b e clustered using the COE-CLARANS algorithm in the main memory.. Too facilitate the clustering, information ab out the micro-cluster are stored together with the representativetativee p oints.ts. This information wouldould include statistic likee the numbumbb er of p ointsts in the micro-cluster, the diameter of the micro-cluster, etc. 

1) p is correctly assigned to orr andom . Since the direct Euclidean distance b etweenweeneen p and orr andom mustust b e shorter than the obstructed distance b etweenweeneen p and orr andom , wee havevee underestimate the actual distance b etweenweeneen p and orr andom . 

3 

and or andom must b e shorter than the obstructed distance b etween p and oi which is computed b efore the iteration b egins. Thus, we have underestimated the actual distance b etween p and oi . 3) p is not assigned to or andom . Since the obstructed distance of p to the rest of the k � 1 cluster centers oj is computed b efore the iteration b egin, the distance used to compute E 0 must b e correct. As we can see, for all the three categories, we either underestimate or compute correctly the obstructed distance of a micro-cluster p to its nearest cluster center. As such E 0 must b e a lower b ound for the actual square-error function E . By adopting the ab ove two approaches, we are able to make our algorithm scalable for a large numb er of ob jects and a mo derate numb er of (a) Clustering when considering obstacles. obstacles. We illustrate the di�erence b etween clustering with obstacles and without obstacles in Figure 2. Further details of our work in this area can b e found in [Hou99]. 3 Clustering Under SQL Aggregate Constraints In order to handle the typ e of constraints that we seen in Example 1.2, we lo ok into the problem of clustering under SQL aggregate constraints in [TNLH00]. We de�ne SQL aggregate constraints as follows. De�nition 3.1 (SQL Aggregate Constraints) Let each ob ject pi in the database D b e asso ciated with a set of m attributes fa1 ; : : : ; am g. The value of an attribute aj of an ob ject pi is denoted as pi [aj ]. Let the aggregate functions ag g1 2 fmax(); min(); (b) Clustering when Ignoring Obstacles. av g (); sum()g and ag g2 2 fcount()g. Let � b e a comparator function, i.e., � 2 f<; �; =; =; �; > Figure 2: How Obstacles a�ect clusters. g, and c represent a numeric constant. Given a cluster C l , an SQL aggregate constraint on C l is a constraint in one of the following forms: (i) ag g1 (fpi [aj ] j pi 2 C l g) � c; or (ii) ag g2 (C l ) � c. 2 De�nition 3.2 (Existential Constraints) Let W � While solving some of these SQL constraints can D b e any subset of ob jects. We often call them b e rather complicated, a large numb er of them could pivot ob jects. Let c b e a p ositive integer. An exhowever b e reduced to a typ e of constraints called istential constraint on a cluster C l is a constraint existential constraints de�ned as follows. of the form: count(fpi jpi 2 C l ; pi 2 W g) � c. 2 

4 

By examining the class of SQL constraints that actually nearer to the centerter of cluster C l11 . Because we have de�ned, we can see that some of the SQL of this, the constraintt k -means algorithm whichh wee constraints can b e easily reduced to an existential introtro duce in [TNLH00]] �rst tries to satisfy userconstraint. For example, \count(C l ) � c" is in fact sp eci�ed constraintt b efore trying to re�ne the clusa sp ecial case of existential constraints in which all ters byy swappingapping ob jects b etweenweeneen the clusters. In ob jects are pivot ob jects. Similarly, a constraint order for the clusters to b e validalid after the re�nelike \max(fpi [aj ] j pi 2 C l g) � d" can also b e ment,t, the swappingapping of the an ob ject is only done if reduced to an existential constraint in which the the changehange in membb ership of the ob ject do es not inpivot ob jects are in the set fpi jpi [aj ] � dg and each validatealidate the user-sp eci�ed constraint.t. More details cluster must contain more than one pivot ob ject. of the algorithm can b e obtained from [TNLH00]. Becauses of its imp ortance, we fo cus on solving the constrained clustering involving in one existential constraint in [TNLH00]. More sp eci�cally, our problem de�nition is as b elow. Cl1 De�nition 3.3 The Constrained Clustering (CC) Problem Given a data set D with n objects, a distance function df : D � D �! <, a positive integer k , and an existential constraints E C , �nd Cl3 a k -clustering (C l1 ; : : : ; C lk ) such that D I S P = (Pki=1 disp(C li )) is minimized, and each cluster C li satis�es the constraint E C , denoted as C li j= C . Cl2 The \disp ersion" or \square-error" of cluster C li , disp(C li ), measures the total distance b etween each ob ject in C li and some representative r epi of C li , i.e., disp(C li ) de�ned as Pp2C li df (p; r epi ). (a) Clustering without constraints. Typically, these representatives are the centroids or the medoids of the clusters which will minimize the disp ersion of each cluster and thus their lo cations Cl1 are go o d candidates for lo cating the facilities that serve the clusters. With the intro duction of an existential conCl3 straint, one ma jor complication is that instead of b eing assigned to the nearest center, a pivot object might b e assigned to a cluster center which is Cl2 further away b ecause of the need to satisfy the existential constraint. Let us consider the example shown in Figure 3a. In the �gure, the hollow p oints represent pivot ob jects while the solid p oints are non-pivot ob jects. Without any constraint imp osed on the clustering, a natural way to group the p oints (b) Clustering with Constraints. is shown in Figure 3a. However if we imp ose a constraint that each cluster must at least contain one Figure 3: How an existential constraint a�ects pivot p oint, then a solution could b e in Figure 3b clusters. where one pivot p oint is \forced" to b e in cluster C l2 and one in C l3 although b oth these p oints are 

actually nearer to the centerter of cluster C l11 . Because of this, the constraintt k -means algorithm whichh wee introtro duce in [TNLH00]] �rst tries to satisfy usersp eci�ed constraintt b efore trying to re�ne the clusters byy swappingapping ob jects b etweenweeneen the clusters. In order for the clusters to b e validalid after the re�nement,t, the swappingapping of the an ob ject is only done if the changehange in membb ership of the ob ject do es not invalidatealidate the user-sp eci�ed constraint.t. More details of the algorithm can b e obtained from [TNLH00]. 

5 

- 4 Conclusion [EKSX96] M. Ester, H.-P. Kriegel, J. Sander, and X. Xu. A density-based algorithm 

- In this pap er, we have intro duced and studied for discovering clusters in large spatial 

- the problem of having user-sp eci�ed constraints in databases. In Proc. 1996 Int. Conf. 

- geo-spatial clustering. Even though constrained Know ledge Discovery and Data Mining 

- clustering problems arise naturally in practice, this (KDD'96), pages 226{231, Portland, 

- app ears to b e the �rst attempt to tackle these Oregon, August 1996. 

- problems. Two typ es of constraints are discussed in this pap er. The �rst typ e of constraints are imp osed [Fis87] D. Fisher. Improving inference through by physical obstacles that exist in the region of conceptual clustering. In Proc. 1987 clustering. The second typ e of constraints are SQL AAAI Conf., pages 461{465, Seattle, constraints which every cluster must satisfy. We Washington, July 1987. discuss some techniques for solving these two typ es of constraints and hop e that more work will b e done [GGR99] V. Ganti, J. Gehrke, and R. Ramakrin these area. ishnan. Mining very large databases. COMPUTER, 32:38{45, 1999. 

- References [GRS98] S. Guha, R. Rastogi, and K. Shim. 

- [ABKS99] M. Ankerst, M. Breunig, H.-P. Kriegel, Cure: An eÆcient clustering algorithm and J. Sander. Optics: Ordering p oints for large databases. In Proc. 1998 to identify the clustering structure. In ACM-SIGMOD Int. Conf. Management Proc. 1999 ACM-SIGMOD Conf. on of Data (SIGMOD'98), pages 73{84, Management of Data (SIGMOD'99), Seattle, Washington, June 1998. pages 49{60, Philadelphia, PA, June [HK98] A. Hinneburg and D. A. Keim. An ef- 

- 1999. �cient approach to clustering in large multimedia databases with noise. In 

- [AGGR98] R. Agrawal, J. Gehrke, D. Gunopulos, and P. Raghavan. Automatic subspace Proc. 1998 Int. Conf. Know ledge Disclustering of high dimensional data for covery and Data Mining (KDD'98), data mining applications. In Proc. 1998 pages 58{65, New York, NY, August 1998. 

- ACM-SIGMOD Int. Conf. Management of Data (SIGMOD'98), pages 94{105, [Hou99] J. Hou. Clustering with Obstacle Enti- 

- Seattle, Washington, June 1998. ties. M.Sc. Thesis, Simon Fraser Uni- 

- [BFR98] P. Bradley, U. Fayyad, and C. Reina. versity, Canada, Decemb er 1999. Scaling clustering algorithms to large [KHK99] G. Karypis, E.-H. Han, and V. Kumar. 

- databases. In Proc. 1998 Int. Conf. CHAMELEON: A hierarchical cluster- 

- Know ledge Discovery and Data Mining ing algorithm using dynamic mo deling. 

- (KDD'98), pages 9{15, New York, NY, COMPUTER, 32:68{75, 1999. 

- August 1998. [Koh82] T. Kohonen. Self-organized formation 

- [CS96] P. Cheeseman and J. Stutz. Bayesian of top ologically correct feature maps. classi�cation (AutoClass): Theory and Biological Cybernetics, 43:59{69, 1982. results. In U.M. Fayyad, G. PiatetskyShapiro, P. Smyth, and R. Uthurusamy, [KR90] L. Kaufman and P. J. Rousseeuw. Findeditors, Advances in Know ledge Discoving Groups in Data: an Introduction to ery and Data Mining, pages 153{180. Cluster Analysis. John Wiley & Sons, AAAI/MIT Press, 1996. 1990. 

6 

- [NH94] R. Ng and J. Han. EÆcient and e�ective clustering metho d for spatial data mining. In Proc. 1994 Int. Conf. Very Large Data Bases (VLDB'94), pages 144{155, Santiago, Chile, Septemb er 1994. 

- [SCZ98] G. Sheikholeslami, S. Chatterjee, and A. Zhang. WaveCluster: A multiresolution clustering approach for very large spatial databases. In Proc. 1998 Int. Conf. Very Large Data Bases (VLDB'98), pages 428{439, New York, NY, August 1998. 

- [SD90] J.W. Shavlik and T.G. Dietterich. Readings in Machine Learning. Morgan Kaufmann, 1990. 

- [THH00] A. K. H. Tung, J. Hou, and J. Han. COE: Clustering with obstacles entities, a preliminary study. In Proc. 4th Paci�c-Asia Conf.on Know ledge Discovery and Data Mining (PAKDD'00), Kyoto, Japan, 18-20, Apr. 2000. 

- [TNLH00] A. K. H. Tung, R. Ng, L. Lakshmanan, and J. Han. Constraint-based clustering in large database. In Submitted to ICDT'00, Jun. 2000. 

- [WYM97] W. Wang, J. Yang, and R. Muntz. STING : A statistical information grid approach to spatial data mining. In Proc. 1997 Int. Conf. Very Large Data Bases (VLDB'97), pages 186{195, Athens, Greece, Aug. 1997. 

- [ZRL96] T. Zhang, R. Ramakrishnan, and M. Livny. BIRCH: an eÆcient data clustering metho d for very large databases. In Proc. 1996 ACMSIGMOD Int. Conf. Management of Data (SIGMOD'96), pages 103{114, Montreal, Canada, June 1996. 

7 

### **Multi-level Indexing and GIS Enhanced Learning for Satellite Imageries** 

###### Krzysztof Koperski 

Data Analysis Products Division of Mathsoft, Inc. 1700 Westlake Ave. N, Suite 500, Seattle, WA, 98109-3044 USA (206) 283-8802 Ext. 243 krisk@statsci.com 

###### Giovanni B. Marchisio 

Data Analysis Products Division of Mathsoft, Inc. 1700 Westlake Ave. N, Suite 500, Seattle, WA, 98109-3044 USA (206) 283-8802 Ext. 280 

###### giovanni@statsci.com 

###### **ABSTRACT** 

Satellite technology produces data at an enormous rate. Most of the database research on the analysis of remotely sensed images concentrated on data retrieval and simple queries that involved spatial joins and spatial selections. For example, the Sequoia 2000 project [13] aimed at the retrieval of raster data, while the Sloan Digital Sky Survey [14] poses the need for the creation of multiterabyte astronomy archive. The large scale systems for the analysis of remotely sensed images were specialized toward the detection of particular features like volcanoes [2], or proposed distributed and parallel data storage and query processing systems for handling of geo-scientific data retrieval queries [11]. The GeoBrowse project aims to provide infrastructure that would enable the analysis of large databases containing satellite images. Our work addresses two issues. One is the extraction of information that enables reduction of the data from multi-spectral images into a number of features. Second is the organization of the features that would allow flexible and scalable discovery of the knowledge from the databases of remotely sensed images. In this paper we present the concept of data mining system for the analysis of satellite images and preliminary results of the experiments with the collection of LANDSAT images. 

###### **Keywords** 

Remote Sensing, Image Databases, Bayesian Classification, Similarity Searches. 

###### **1. INTRODUCTION** 

Satellite data is used in many different areas ranging form agriculture, forestry, and environmental studies to transportation and mining. The applications include measurements of crop and timber acreage, forecasting crop yields and forest harvest, monitoring urban growth, mapping of ice for shipping, mapping of pollution, recognition of certain rock types, and many others. The United States Geological Survey web site [15] presents other 

> © The copyright of this paper belongs to the paper's authors. Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. 

> Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 

> (O.R. Zaïane, S.J. Simoff, eds.) 

applications that use the results of the satellite data analysis. 

The _GeoBrowse_ project aims at providing the infrastructure required for the analysis of satellite images. Most of the systems for analyzing remotely sensed images allow simple queries based on the date of image capture and location. Such systems also allow only simple analyses of single images. When we deal with large collections of remotely sensed images, the current systems do not scale well. Therefore new algorithms and new indexing methods are needed to enable the analysis of data produced by satellite systems. 

In order to facilitate the analysis of large amount of image data, we propose to extract features of images. Large images are partitioned into a number of smaller and more manageable image tiles. In addition to faster extraction of segments the partitioning allows to fetch only the relevant tiles when only retrieval of part of the image is requested. Then these image tiles are processed in order to extract feature vectors. The _GeoBrowse_ architecture distinguishes between three types of feature vectors: 1) _pixel level features_ , 2) _region level features_ , and 3) _tile level features_ . Pixel level features store spectral and textural information about each pixel of the image. For example, the fraction of the endmembers, such as concrete or water, can describe the content of the pixels. Due to the large size, pixel feature vectors are used only for the extraction of other feature vectors and can be utilized in the refinement step of the queries. Region level features describe groups of pixels. Following the segmentation process, each region is described by its boundary and a number of  attributes which present information about the content of the region in terms of the endmembers and texture, shape, size, fractal scale, etc. Image tile level features present information about whole images using texture, percentages of endmembers, fractal scale and others. 

There are many similarities between data mining in the collections of photographic images and data mining in the collections of sattellite images. In both cases features, such as texture, or color histograms are used in the analysis. However, in the case of the remotely sensed images a user can use additional information, such as Digital Elevation Models (DEM), or land use maps, to enhance the search capabilities and improve the quality of the classification and prediction process. 

In this paper we give an overview of the GeoBrowse system and present the results of similarity searches for different types of urban areas. For the experiments we used the LANDSAT image of Western Washington State. This image contains about 500MB of raw pixel information in 6 bands (3 visible range and 3 near infrared bands). The image was corrected for atmospheric and terrain distortions, and  georeferenced. In order to enable work 

8 

with chunks of images that are feasible for the segmentation algorithm, the whole image was divided into 512 pixels × 512 pixels _image tiles_ . 

The remaining part of the paper is organized as follows. In Section 2 we present the architecture of the system. Section 3 describes the algorithm for the segmentation of multiband images and features that describe the regions. In Section 4 we present theresults of the similarity retrieval queries. Section 5 outlines the data mining methods for the analysis of remotely sensed images. The paper ends with conclusions and the description of future work. 

###### **2. ARCHITECTURE** 

We decided to use a database system for storage of images and their features. This way we may overcome limits related to the maximum size of files and benefit from indexing, query optimization, and partitioning features of the database. The image tiles and pixel level features are stored as BLOBs, each band in a separate column. The region and tile level features are stored in regular database tables, which can be easily accessed for further processing using GeoBrowse functions or by over 3000 function of S-PLUS software [12]. 

Spatial information about region level is stored in ESRI’s Spatial Data Engine (SDE) together with the relevant GIS information. SDE provides open data access across local and wide area networks and the Internet using the TCP/IP protocol. It can retrieve data and perform spatial and geometric analysis with 14 topological searches, buffering, overlays and intersections, dissolve and clip, and topological data cleaning. Data stored in SDE can be also accessed from other ESRI products like ArcInfo, ArcView, and MapObjects, which provide alternative environment for the visualization of the query results. 



<!-- Start of picture text -->
MATHSOFT<br>GUI DATA MINING<br>��� MODULE<br>ODBC<br>JNI  +<br>C API<br>C API<br>DBMS ESRI<br>(Oracle) SDE<br><!-- End of picture text -->

**Figure 1. Architecture of GeoBrowse** 

A mining process or a similarity search is initiated by submitting a query written in a language similar to SQL-like data mining languages, such as DMQL [5] and GMQL [8]. In a query a user can specify the type of knowledge to be discovered; the set of data relevant to the mining process; and the thresholds to filter out uninteresting rules. Based on this query an SQL statement is constructed to retrieve the relevant data. If spatial conditions exist in the query the SDE is used for the processing, otherwise the data 

is retrieved directly from the database system. The data mining module processes the data and passes the information about the resulting tiles and regions to GUI, which in turn directly retrieves the images from the database. 

Based on the classification model the data can be classified into a number of land cover classes and the resulting GIS map can be stored in the SDE for future use or a presentation by the GIS system. 

###### **3. SEGMENTATION AND FEATURE EXTRACTION** 

The segmentation process is using the function based on the algorithm presented in [7]. This function segments an input image into non-overlapping regions by minimizing an energy functional which trades off the similarity of regions against the length of their shared boundary. It starts by breaking the image into many small regions. The algorithm merges into one region the two adjoining regions that are the most alike in terms of the specified polynomial model given the length of the border between the two regions. Internally, the energy functional is evaluated using a Lagrangian parameter called lambda. Parameter is also called the scale parameter as it controls the coarseness of the segmentation where a small value of lambda corresponds to a finer segmentation with more regions and a large value corresponds to a coarse segmentation with fewer regions. Since the algorithm grows regions by merging alike regions, the value of lambda increases as the number of regions decreases. To achieve the segmentation uniformity between tiles the final value of lambda is set to be approximately the same for each image tile. 

In the case of multi-band satellite images the values of the pixels are often correlated. Therefore, the Principal Component Analysis is performed based on a large sample of pixels from all tiles, all tiles are rotated to the same axes and the first three components are used for the segmentation of each image tile. After the segmentation the shape features such as eccentricity, orientation of the main axis, and invariant moments are extracted and stored in the database. 

###### **3.1 Texture Feature Extraction** 

We extract pixel level texture features based on Gabor wavelets. In the comparison study of texture based classification, Gabor features were judged to perform superior to other texture analysis methods, such as edge attribute processing methods, the circular simultaneous autoregressive model method and hidden Markov model methods [3]. In GeoBrowse for each pixel we extract eight features<sup>_a_</sup> _i i_ = 7,0 using Gabor Filters with kernels rotated by 

_i_ π / 8 . To achieve the rotation invariant features we find the values of the autocorrelation function 7 _t n_ = ∑ _ai a_ ( _i_ + _n_ ) mod 8 [6]. To minimize the size of the pixel _i_ = 0 

index, we have chosen to compute values of autocorrelation for _n_ = 4,2,0 . These values correspond to the 0 ° , 45 ° , and 90 ° difference in the orientation of Gabor kernels. Such shift should allow for distinguishing of urban road network, which usually are correlated within 90 ° rotation of the wavelet kernels. The extraction of other microfeatures such as frequency, orientation, is also possible [6] and we plan to perform more experiments with these features in the future. 

9 





**Figure 2.** 

**Spectral Mixture Analysis region features (the prevalent endmembers).** 

**Percentage of pixel that belong to one of the clusters.** 

###### **3.2 Spectral Mixture Analysis Features** 

Spectral Mixture Analysis (SMA) [1, 4] enables the analysis of remotely sensed images using spectral endmembers such as concrete, water, soil, trees, etc. The pixels usually cover the area with the mixture of different endmembers. For example, in the urban areas we may find a mixture of concrete, trees, soil, grass, etc. The result of SMA represents the percentage of the contents of the endmembers within the area of the pixel. This way we can distinguish areas with different mixture of concrete, soil, water, and vegetation. The region and tile level features present the percentage of the area of a region a tile that is covered by particular endmembers. Region level texture and SMA features are presented in Figure 2. 

###### **4. SIMILARITY SEARCH** 

The GeoBrowse uses an SQL like query language that enables specification of the data mining task, features that are used in the mining process and further constraints. The system is capable of performing similarity searches based on any combination of features. A user can look for the most similar image tiles or the most similar regions based on a pattern tile or a region. GeoBrowse enables arbitrary weighting of the features. The values of the features can be adjusted to have the range [0, 1], they can be multiplied by a specific value, or they can remain the same. 

In the case of region based searches we looked only for the regions with areas larger than 2000 pixels. The feature values were scaled to the range [0,1]. We compared the results of the similarity searches based on SMA features with the searches based on texture features and searches based on the combination of these two features. When only a single feature vector is used the results tend to have a high percentage of the areas, which could be classified as _false hits_ . The selectivity of the SMA features seems to be quite high for urban patterns, but some rocks and crops have spectral signatures similar to the spectral signature of concrete and are classified as such. The selectivity of searches based on texture features is lower, but rotation invariance can be observed regardless of the orientation of the 

street networks. For example, the suburban area of New Westminster in the Greater Vancouver area is judged to be similar to East Vancouver, despite the fact that the main direction of the street network differs by about 30 ° for these two region. Figure 3 presents the result of the search for regions similar to downtown Seattle and Burnaby in British Columbia. Only regions in Puget Sound are shown. In the case of downtown Seattle the set of returned regions contained downtown areas of Vancouver, Burnaby, Bellingham, Bellevue, Tacoma, and Everett together with industrial areas of Renton, Tukwila and South Tacoma. Regions similar to Burnaby contain high-density residential areas with some small industrial and commercial pockets. 

We compared the results of the tile similarity search with the region similarity search in the case when the tile containing the pattern region is treated as a pattern tile. In this case the returned tiles contained only about 40% of the top 20 most similar regions returned by region based similarity function. The features of the smaller regions tend to be overwhelmed by the overall features of the tile. 

###### **5. DATA MINING FUNCTIONALITY** 

In addition to the similarity search the GeoBrowse system will provide functionality for other types of the remotely sensed data analysis. This functionality will include the clustering of the data, building regression and classification models, prediction of land cover types, summarization of the data, etc. 

###### **5.1 Clustering** 

A user has an option to find clusters of image tiles based on any combination of feature vectors. Figure 4 shows the centroids (i.e., the image tiles located the most centrally in the feature space) for the four clusters. The clusters were found based on the relative content of endmembers in an image tile. In this case we may see that the image tiles that are the centroids of the discovered clusters represent mountain areas with large content of conifer trees; areas covered with deciduous trees; forested areas close to water; and urban areas close to water. 

10 





**Figure 3.** 

**Regions similar to downtown Seattle.               Regions similar to West Burnaby, BC.** 



**Figure 4. The centroid tiles of the clusters.** 

###### **5.2 User Feedback Label Learning** 

In many cases it is very difficult to describe analytically the features of the objects that a user is looking for. Therefore the improvement of the description quality may play an important role in the image analysis. A method for interactive training of land cover labels using Naïve Bayesian classifiers is described in [10]. In that approach a user can interactively train Bayesian model to define a number of land cover classes, which can be based on textural or spectral properties of images. The training is done based on pixel level features, which are partitioned into a number of clusters. A user selects the pixels that belong to a new class and the pixels that do not belong there. Based on this information a model that estimates a posteriori probability of pixel’s class membership is build. Using this model a user can 

find images with the highest probability of the defined class, or images with low or high separability of the classes. While the training is based on the pixel level features the retrieval is based on tile level features. Due to the nature of Naïve Bayesian classifier, which assumes the conditional independence of the attributes, it is possible to find out the probabilities of the pixel class assignment based on the aggregated information about all pixels in the image tile. Unfortunately the assumption of conditional independence is not always true. Therefore, Naïve Bayesian classifiers may perform well.  We plan to add other classification methods, such as tree classifiers to improve user feedback label training. Because the classification process on the pixel level would be extremely expensive to compute we intend 

11 

to perform experiments with the classification based on the region level features. 

Building a classifier based on millions pixel features of the data would be a very time process. Instead of that we build the classifier based on region level features. In addition to spectral properties of the regions we can perform classification also based on shape properties and area of the regions, as well as auxiliary GIS information. For example, the spectral reflectance of concrete is very similar to spectral reflectance of different type of rocks. Additional information, such as Digital Elevation Models can be used to distinguish between these two types of land cover types. 

###### **6. FUTURE WORK AND CONCLUSIONS** 

We plan to perform experiments using multiple level spatial transformation methods for progressive refinement using more level than tile, region, and pixel levels. Multiscale image coding techniques, such as wavelets, can also be used for the analysis of images on multiple levels. 

Such multilevel information can be combined with the auxiliary data in both vector and raster formats to enhance the data analysis capabilities of _GeoBrowse._ These auxiliary data can be used both during feature extraction process and during data mining process. We intend to do more experiments with other data mining methods such as regression, clustering and classification. 

The quality of classification of land cover classes can be improved using time series of data, which can better differentiate between different types of crops due to the different times of crop growing seasons. We also plan to provide the functionality of multilevel presentation of the discovered knowledge. For example, the system should allow a user to see the generalized summary of the areas of particular crops by county, state, region, etc. 

We designed, and we are in the process of implementing the _GeoBrowse_ system for data mining of remotely sensed images. Three levels of feature are extracted from image tiles and used in the data mining process. In addition to simple queries based on simple properties, such as geographic location or acquisition date, a user can submit queries based on properties of images derived from feature vectors describing the images. The system also will allow for interactive training of the classification models that describe new types of objects. Scalability to the large databases is addressed through indexing of the feature vectors and by using scalable data mining algorithms in the query processing. Our region level indexing strategy enhances the data analysis and similarity search processes by allowing for the more refined classification of information derived from images. 

###### **7. REFERENCES** 

- [1] Adams, J. B., M. O. Smith, and P. E. Johnson, Spectral Mixture Modeling: a New Analysis of Rock and Soil Types at Viking Lander 1. In _J. Geophys. Res_ . 91:8113 – 8125, 1986. 

- [2] Fayyad, U. M., and P. Smyth. Image Database Exploration: Progress and Challenges. In _Proc. 1993_ 

_Knowledge Discovery in Databases Workshop_ , Washington, DC, p. 14 – 27, 1993. 

- [3] Fountain, S. R., T. N. Tan, K. D. Baker. A Comparative Study of Rotation Invariant Classification and Retrieval of Texture Images. In _On-Line Proceedings of the Ninth British Machine Vision Conference_ 1998. <u>http://www.bmva.ac.uk/bmvc/1998/index.htm.</u> 

- [4] Gillespie, A. R., M. O. Smith, J. B. Adams, and S. C. Willis, Spectral Mixture Analysis of Multispectral Thermal Infrared Images, In _Proceedings of the 2nd Thermal IR Multispectral Scanner Workshop_ , JPL Publication 90-55:57 – 74, 1990. 

- [5] Han, J., Y. Fu, W. Wang, K. Koperski, and O. R. Zaïane. DMQL: A Data Mining Query Language for Relational Databases. _In Proc. of the Workshop on Research Issues on Data Mining and Knowledge Discovery_ , Montreal, QB, pp. 27 – 34, 1996. 

- [6] Hayley, G. M., and B. M. Manjunath, Rotation Invariant Texture Classification using Modified Gabor Filters, In _Proc. of IEEE ICIP95_ , pp. 262 – 265, 1994. 

- [7] Koepfler, G., C. Lopez and J. M. Morel, A Multiscale Algorithm for Image Segmentation by Variational Method, _SIAM Journal of Numerical Analysis_ , vol. 31, pp. 282 – 299, 1994. 

- [8] Koperski, K. _A Progressive Refinement Approach to Spatial Data Mining_ . Ph.D. Thesis. Simon Fraser University, 1999. 

- [9] Patel, J., et al. Building a Scalable Geo-Spatial DBMS: Technology, Implementation, and Evaluation. In _Proc. ACM-SIGMOD International Conference on Management of Data_ , Tucson AZ, pp. 336 – 347, 1997. 

- [10] Schröder, M. Interactive Learning in Remote Sensing Image Databases In _IEEE Intern. Geoscience and Remote Sensing Symposium IGARSS’99_ . Hamburg, 1999. 

- [11] Shek, E. C., R. R. Muntz, E. Mesrobian, and K. Ng. Scalable Exploratory Data Mining of Distributed GeoScientific Data. In _Proc. of The Second International Conference on Knowledge Discovery & Data Mining_ , Aug. 2-4, Portland OR, pp. 32 – 37, 1996. 

- [12] _S-PLUS 2000 Programmer’s Guide_ , Data Analysis Products Division, MathSoft, Seattle, WA, 1999. 

- [13] Stonebraker, M., J. Frew, K. Gardels, and J. Meredith. The Sequoia 2000 Storage Benchmark. In _Proc. ACM-SIGMOD International Conference on Management of Data_ , Washington, D.C., pp. 2 – 11, 1993. 

12 

- [14] Szalay, A., P. Kunszt, A. Thakar, J.Gray, D. Slutz, and  R. J. Brunner. Designing and Mining Multiterabyte Astronomy Archives: The Sloan Digital Sky Survey. In _Proc. ACM-SIGMOD International Conference on Management of Data_ , Dallas TX, pp. 451 – 462, 2000. 

- [15] U.S. Department of the Interior, U.S. Geological Survey, Landsat 7 data users and applications <u>http://edcwww.cr.usgs.gov/l7dhf/L7MMO/L7applicat n.htm, 1999.</u> 

13 

### **Predicting Locations Using Map Similarity(PLUMS): A Framework for Spatial Data Mining** � 

Sanjay Chawla Shashi Shekhar Weili Wu Vignette Corporation Computer Science Computer Science Waltham, Massachusetts University of Minnesota University of Minnesota chawla@cs.umn.edu Minneapolis, MN 55455, USA. Minneapolis, MN 55455, USA. shekhar@cs.umn.edu wuw@cs.umn.edu **ABSTRACT** are spread across many domains including ecology and enviSpatial data mining is a pro cess to discov er in teresting, p o- ronment management, public safety , transp ortation, public ten tially useful and high utility patterns emb edded in spatial health, business logistics, trav el and tourism. [2, 15, 17, 21, databases. EÆcient to ols for extracting information from 28, 34, 38]. spatial data sets can b e of imp ortance to organizations which Classical data mining algorithms [1, 10] often make aso wn, generate and manage large spatial data sets. The cursumptions(e.g. indep endent, iden tical distributions), which ren t approach tow ards solving spatial data mining problems violate the �rst law of Geography: ev erything is related to is to use classical data mining to ols after \materializing" ev erything else but nearby things are more related than disspatial relationships. Ho w ev er, the k ey prop erty of spatial tan t things [5, 35]. In other words, the v alues of attributes data is that of spatial auto correlation. Lik e temp oral data, of nearb y spatial ob jects tend to systematically a�ect each spatial data values are in�uenced by values in their immediother. In spatial statistics, an area within statistics devoted ate vicinit y . Ignoring spatial auto correlation in the mo deling to the analysis of spatial data, this is called spatial autopro cess leads to results which are a p o or-�t and unreliable. correlation [6]. Knowledge discov ery tec hniques which igIn this pap er we will prop ose PLUMS(Predicting Lo cations nore spatial auto correlation typically p erform p o orly in the Using Map Similarity), a new approach for sup ervised spapresence of spatial data. Spatial statistics tec hniques on tial data mining problems. PLUMS searc hes the space of the other hand do take spatial auto correlation directly into solutions using a map-similarity measure which is more apaccoun t [3] but the resulting mo dels are computationally propriate in the context of spatial data. We will show that exp ensive and are solved via complex numerical solvers or compared to state-of-the-art spatial statistics approaches, sampling based Marko v Chain Monte Carlo(MCMC) methPLUMS achiev es comparable accuracy but at a fraction of o ds [22]. the computational cost. F urthermore, PLUMS pro vides a In this pap er w e will prop ose PLUMS(Predicting Lo cageneral framework for sp ecializing other data mining techtions Using Map Similarity), a new approach for sup ervised niques for mining spatial data. spatial data mining problems. PLUMS searches the parameter space of mo dels using a map-similarity measure which is more appropriate in the context of spatial data. We will **1. INTRODUCTION** sho w that compared to state-of-the-art spatial statistics apWidespread use of spatial databases [14, 30, 33, 37] is leadproac hes, PLUMS ac hiev es comparable accuracy but at a ing to an increasing interest in mining interesting and useful fraction of the cost(tw o orders of magnitude). F urthermore, but implicit spatial patterns[19, 24, 12, 29]. EÆcient to ols PLUMS pro vides a general framework to sp ecialize other for extracting information from geo-spatial data, the fo cus data mining techniques for mining spatial data. of this work, are crucial to organizations which make decisions based on large spatial data sets. These organizations **1.1 An Illustrative Application Domain** � This work was supp orted in part by the Army High PerThe av ailabilit y of accurate spatial habitat mo dels is an formance Computing Research Center under the auspices of imp ortant to ol for wildlife management, protection of critDepartment of the Army , Army Research Lab oratory Coical habitat and endangered sp ecies. Since the underlying nopumerativb er De AAH04-95-C-0008,agreement n umb er andD AAH04-95-2-0003/conb y the National Sciencetract pro cess go v erning the interaction b etw een wildlife and enF oundation under grant 9631539. vironmental factors is complex, statistical mo dels are built to gain some insight on the basis of data collected during �eld work. One of authors has b een inv olv ed in the development of spatial mo del for the nesting lo cations of a marshnesting bird sp ecies [25, 26]. We will use this application, © The copyright of this paper belongs to the paper's authors. Permission to copy withoutfee all or part of this material is granted provided that the copies are not made or and the accompanying data, to explain the lo cation predicadistributed for direct commercial advantage. tion problem and its unique asp ects vis-a-vis classical data Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 mining. (O.R. Zaïane, S.J. Simoff, eds.) The learning and testing datasets that w e will b e used w as collected in 1995 and 1996 from two wetlands(Darr and Stubble) lo cated on the shores of Lak e Erie in Ohio. F or 



14 

0 Nest sites for 1995 Darr location 0 Vegetation distribution across the marshland 10 10 20 20 30 30 40 40 Marsh land 50 50 Nest sites 60 70 60 80 70 0 20 40 60 80 100 120 140 160 nz = 5372 80 0 20 40 60 80 100 120 140 160 nz = 85 0 10 20 30 40 50 60 70 80 90 (a) Nest Lo cations (b) Vegetation 0 Water depth variation across marshland 0 Distance to open water 10 10 20 20 30 30 40 40 50 50 60 60 70 70 80 80 0 20 40 60 80 100 120 140 160 0 20 40 60 80 100 120 140 160 nz = 5372 nz = 5372 0 10 20 30 40 50 60 70 80 90 0 10 20 30 40 50 60 (c) Water Depth (d) Distance to Op en Water Figure 1: (a) Learning dataset: The geometry of the wetland and the lo cations of the nests, (b) The spatial distribution of vegetation durability over the wetland, (c) The spatial distribution of water depth, and (d) The spatial distribution of distance to open water. the purp ose of data collection, a lo cal co ordinate system tic regression, make assumption ab out indep endent distriwas established for each wetland and a regular grid conbutions for the prop erties of each pixel, ignoring spatial ausisting of approximately 5000 cells was sup erimp osed. The to correlation. Figure 3(a) shows a spatial distribution concells of the grid had square geometries of size 5 meters by 5 sistent with assumption of classical regression. It lo oks like meters. In each cell the values of several structural and en\white noise" as prop erties of pixel are generated from invironmental variables were recorded, including water depth, dep endent and identical distributions. Note that the maps dominant vegetation durability index and distance to open of explanatory variable in Figure 1 have much more gradwater. These three factors play the role of most signi�cant ual variation indicating high spatial auto correlation. Figure explanatory variables. At each cell was also recorded the 3(b) shows a random distribution of nest lo cations which is fact whether a bird-nest(red-winged blackbird) was present quite di�erent from the distribution of actual nests shown or not. The presence of the nest played the role of dep enin Figure 1(a). dent variable. The geometry of the Darr wetland, lo cations A second, more subtle but equally imp ortant reason is the of the nests and spatial distribution of the explanatory variob jective function of classi�cation measure accuracy. For ables are shown in Figure 1. The corresp onding maps for a two-class problem the standard way to measure classi�the Stubble wetland are shown in Figure 2. cation accuracy is to calculate the p ercentage of correctly One of the authors has applied classical data mining techclassi�ed ob jects. This measure may not b e the most suitniques like logistic regression[26] and neural networks[25] to able for spatial data. Spatial accuracy is as imp ortant in build spatial habitat mo dels. Logistic regression was used this application domain due to the e�ects of discretization b ecause the dep endent variable is binary(nest/no-nest) and of continuous marsh into discrete pixels, as shown in Figthe logistic function \squashes" the real line onto the uniture 4. Figure 4(a) shows the actual lo cations of nests and interval. The values in the unit-interval can then b e inter4(b) shows the pixels with actual nests. Note the loss of inpreted as probabilities. They concluded that using logistic formation during the discretization of continuous space into regression the nests could b e classi�ed at a 24% rate b etpixels. Many nest lo cation barely fell within the pixels later than random[25]. The use of neural networks actually b eled `A' and were quite close to other pixels with lab el of decreased the classi�cation accuracy[25] but led to a b etter no-nest. Now consider two predictions shown in Figure 4(c) understanding of the interaction b etween the explanatory and 4(d). Domain scientists prefer prediction 4(d) over and the dep endent variable. 4(c), since predicted nest lo cations are closer on average to There are two imp ortant reasons why, despite extensive some actual nest lo cations. Classi�cation accuracy measure domain knowledge, the results of classical data mining are cannot distinguish b etween 4(c) and 4(d), and one needs not \satisfactory". First, classical techniques, e.g. logisa measure of spatial accuracy to capture this preference. 

15 

0 Nest sites in Stubble marshland in 1995 Vegetation distribution across the marshland (Stubble 95) 90 10 10 80 20 20 70 30 30 60 40 40 50 40 50 50 30 60 60 20 70800 10 20 30 40nz = 30 MarshlandNest sites50 60 70 80 7080 10 20 30 40 50 60 70 80 100 (a) Nest Lo cations (b) Vegetation Water depth variation across the marshland (Stubble 95) 200 Distance to open water across the marshland (Stubble 95) 50 10 180 10 45 160 40 20 20 140 35 30 120 30 30 40 100 40 25 50 80 50 20 60 60 60 15 40 10 70 70 20 5 80 10 20 30 40 50 60 70 80 0 80 10 20 30 40 50 60 70 80 0 (c) Water Depth (d) Distance to Op en Water Figure 2: (a) The geometry of the wetland and the lo cations of the nests, (b) The spatial distribution of vegetation durability over the wetland, (c) The spatial distribution of water depth, and (d) The spatial distribution of distance to open water. ^Y A simple and intuitive measure of spatial accuracy is the Find : A function f 2 F . Average Distance to Nearest Prediction(ADNP) from the ^Y actual nest sites, which can b e de�ned as Ob jective : maximize similarity(mapsi 2S (f (fX1 ; AD N P (A; P ) = K1 XkK=1 d(Ak ; Ak :near est(P )): (:=�: : )spatial(1; fX�K�))) ;classi�cationaccuracy((map(fY (sif^)))Y accuracy; fY ) (f^Y ; fY ) + Here the Ak 's are the actual nest lo cations, P is the map Constraints : layer of predicted nest lo cations and Ak :near est(P ) denotes the nearest predicted lo cation to Ak . K is the numb er of 1. Geographic Space S is a multi-dimensional Eu1 actual nest sites. We now formalize the spatial data mining clidean Space . problem by incorp orating notions of spatial auto correlation 2. The values of the explanatory functions, the fXk 's and spatial accuracy in the problem de�nition. and the resp onse function fY may not b e indep en- **1.2 Location Prediction: Problem Formula-** dent with resp ect to those of nearby spatial sites, i.e. spatial auto correlation exists. **tion** The Lo cation Prediction problem is a generalization of the 3. The domain R k of the explanatory functions is nest lo cation prediction problem. It captures the essential the one-dimensional domain of real numb ers. prop erties of similar problems from other domains includ4. The domain of the dep endent variable, R Y = ing crime prevention and environmental management. The f0; 1g. problem is formally de�ned as follows: The ab ove formulation highlights two imp ortant asp ects Given : of lo cation prediction. It explicitly indicates that (i) the � A spatial framework S consisting of sites fs1 ; : : : ; sn g data samples may exhibit spatial auto correlation and, (ii) for an underlying geographic space G. an ob jective function i.e., a map similarity measure is a combination of classi�cation accuracy and spatial accuracy. � AR kcollection; k = 1; : : :ofKexplanatory. R k is the rangefunctionsof p ossiblefXk : Sval-! Thepredictedsimilarityvariableb etwf^eenY isthea depcomendenbinationt variableof the ftraditionalY and the ues for the explanatory functions. accuracy" and a representation dep endent \spatial classi�Y � A dep endent function fY : S ! R cation" accuracy. The regularization term � controls the � A family F of learning mo del functions mapping 1 The entire surface of the Earth cannot b e mo deled as a 1 K Y R � : : : R ! R . Euclidean space but lo cally the approximation holds true. 

16 

Random distributed nest sites 0 White Noise −No spatial autocorrelation 0 10 10 20 20 30 30 40 50 40 60 50 70 60 80 70 0 20 40 60 nz = 537280 100 120 140 160 80 0 20 40 60 80 100 120 140 160 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 nz = 195 (a) pixel prop erty with indep en(b) Random nest lo cations dent identical distribution Figure 3: Spatial distribution satisfying distribution assumptions of classical regression P Legend A P P A P A = nest location A  =  actual nest in pixel P P P   = predicted nest in pixel A A A A A A (a) (b) (c) (d) Figure 4: (a)The actual lo cations of nest, (b)Pixels with actual nests, (c)Lo cation predicted by a mo del, (d)Lo cation predicted by another mo de. Prediction(d) is spatially more accurate than (c). degree of imp ortance of spatial accuracy and is typically mining. domain dep endent. As � ! 0, the map similarity measure Spatial Statistics: The goal of spatial statistics is to approaches the traditional classi�cation accuracy measure. mo del the sp ecial prop erties of spatial data. The primary Intuitively, � captures the spatial auto correlation dep endent distinguishing prop erty of spatial data is that neighb oring in the data. data samples tend to systematically a�ect each other. Thus The study of nesting lo cation of red-winged black bird [25, the classical assumption that data samples are generated 26] is an instance of the lo cation prediction problem. The from indep endent and identical distributions is not valid. underlying spatial framework is the collection of 5mX5m Current research in Spatial Econometrics, Geo-statistics and pixels in the grid imp osed on marshes. Explanatory variEcological mo deling [3, 23, 13] has fo cused on extending ables, e.g. water depth, vegetation durability index, disclassical statistical techniques in order to capture the unique tance to op en water, map pixels to real numb ers. Dep encharacteristics inherent in spatial data. In Section 2 we will dent variable, i.e. nest lo cations, maps pixels to a binary brie�y review some basic spatial statistical measures and domain. The explanatory and dep endent variables exhibit techniques. spatial auto correlation, e.g. gradual variation over space, Spatial Data Mining: Spatial data mining [9, 18, 19, as shown in Figure 1 and 2. Domain scientist prefer spa20, 29], a sub�eld of data mining [1, 10], is concerned with tially accurate predictions which are closer to actual nests, discovery of interesting and useful but implicit knowledge i.e, � > 0. in spatial databases. Challenges in Spatial Data Mining Finally, it is imp ortant to note that in spatial statistics the arise from the following issues. First, classical data mingeneral approach for mo deling spatial auto correlation is to ing[1] deals with numb ers and categories. In contrast, spaenlarge F , the family of learning mo del functions(see Section tial data is more complex and includes extended ob jects 2.3). The PLUMS 2 approach(See Section 3) allows �exibilsuch as p oints, lines, and p olygons. Second, classical data ity of incorp orating spatial auto correlation in the mo del, the mining works with explicit inputs, whereas spatial prediob jective function or b oth. Later on we will show that recates (e.g. overlap) are often implicit. Third, classical data taining the classical regression mo del as F but mo difying mining treats each input to b e indep endent of other inputs, the ob jective function leads to results which are comparable whereas spatial patterns often exhibit continuity and high to those from spatial statistical metho ds but incur only a autocorrelation among nearby features. For example, p opufraction of the computational costs. lation density of nearby lo cations are often related. In the presence of spatial data the standard approach in the data **1.3 Related Work and Our Contributions** mining community is to materialize spatial relationships as Related work includes spatial statistics and spatial data attributes and rebuild the mo del with these \new" spatial 2 An interesting piece of trivia is that there is actually attributesOur con[20,tributions:19]. In this pap er we will prop ose a new asacPLUMhusetts.bird island just o� the coast of Boston, Masframework for spatial data mining. This framework con- 



17 

sists of a combination of statistical mo del, a map similarity low negative value is an indication that high and low values measure along with a search algorithm and a discretization are intersp ersed. Thus like values are de-clustered and tend of the parameter space. We will show that the characteristo rep el each other. A value close to zero is an indication tic prop erty of spatial data, namely, spatial auto correlation, that no spatial trend (random distribution) is discernible can b e incorp orated in the statistical mo del or the ob jective using the given measure. The exact de�nition of MI is given function. We will also conduct exp eriments on the \birdin the App endix. nesting" data to compare our approach with spatial statisAll spatial auto correlation measures are crucially dep entical techniques. The rest of the pap er is as follows. In dent on the choice and design of the contiguity matrix W. Section 2 we will brie�y review some imp ortant spatial staThe design of the matrix itself is predicated on determining tistical concepts. In Section 3 we will prop ose PLUMS, a \what constitutes a neighb orho o d of in�uence?" Two comnew framework for spatial data mining. Exp eriments carmon choices are the four and the eight neighb orho o d. Thus ried out to compare PLUMS and spatial statistical metho ds given a lattice structure and a p oint S in the lattice, a fourwill b e elab orated up on in Section 4. We will close in Section neighb orho o d assumes that S in�uences all cells which share 5 with some comments and directions for future work. an edge with S. In an eight-neighb orho o d it is assumed that S in�uences all cells which either share an edge or a vertex. **2. BASIC CONCEPTS:MODELING SPATIAL** An eight neighb orho o d contiguity matrix is shown in Figure 5. The contiguity matrix of the uneven lattice(left) is shown **DEPENDENCIES** on the right hand side. The contiguity matrix plays a crucial role in the spatial extension of the regression mo del. **2.1 Logistic Regression Modeling** Given an n�vector y of observations and an n � m matrix **2.3 Predicting Locations Using Spatial Statis-** X of explanatory data, classical linear regression mo dels the **tics** relationship b etween y and X as We now show how spatial dep endencies are mo deled in the y = X� + �: framework of regression analysis. This may serve as a template for mo deling spatial dep endencies in other data mining Here X = [1; X ] and � = (�0 ; : : : ; �m )t . The standard techniques. In spatial regression the spatial dep endencies of assumption on the error vector � is that each comp onent is the error term or the dep endent variable are directly mo d- generatedmal distribution,from ani.e,indep�i =endenN (0;t�and2 ). and identical and noreleddent invaluesthe regressionyi0 are relatedequationto each[3].other,Assumei.e. ythati = fthe(yj )depi =en-j: When the dep endent variable is binary, as is the case in Then the regression equation can b e mo di�ed as the \bird-nest" example, the mo del is transformed via the y = �W y + X� + �: logistic function and the dep endent variable is interpreted as the probability of �nding a nest at a given lo cation. Thus, Here W is the neighb orho o d relationship contiguity matrix P r ob(y = 1) = 1+eXeX� � . This transformed mo del is referred and � is a parameter that re�ects the strength of spatial deto as logistic regression. p endencies b etween the elements of the dep endent variable. The fundamental limitation of classical regression mo delAfter having intro duced the correction term �W y , the coming is that it assumes that the sample observations are inp onents of the residual error vector � are now assumed to b e dep endently generated. This may not b e true in the case of generated from indep endent and identical standard normal spatial data. As we have shown in our example application, distributions. the explanatory and the indep endent variables show a mo d- We will refer to this equation as the Spatial Autoreerate to high degree of spatial auto correlation(see Figure gressive Mo del(SAM). Notice when � = 0 , this equation 1). The inappropriateness of the indep endence assumption collapses to the classical regression mo del. The b ene�ts of shows up in the residual errors, the �i 's. When the sammo deling spatial auto correlation are many: (1) The residples are spatially related, the residual errors reveal a sysual error will have much lower spatial auto correlation, i.e., tematic variation over space, i.e., they exhibit high spatial systematic variation. With prop er choice of W , the residauto correlation. This is a clear indication that the mo del ual error should, at least theoretically, have no systematic was unable to capture the spatial relationships existing in variation. (2) If the spatial auto correlation co eÆcient is the data. Thus the mo del is a p o or �t to the data. Incidenstatistically signi�cant then it will quantify the presence of tally the notion of spatial auto correlation is similar to that spatial auto correlation. It will indicate the extent to which of time auto correlation in time series analysis but is more variations in the dep endent variable (y) are explained by the diÆcult to mo del b ecause of the multi-dimensional nature of average of neighb oring observation values. (3) Finally, the space. We now intro duce a statistic which quanti�es spatial mo del will have a b etter �t, i.e., higher R-squared statisauto correlation. tic(See the App endix for a dramatic example). As in the case of classical regression, the SAM equation **2.2 Spatial Autocorrelation and Examples** has to b e transformed via the logistic function for binary There are many measures available for quantifying spatial dep endent variables. The estimates of � and � can b e deauto correlation. Each have their own strengths and weakrived using maximum likeliho o d theory or Bayesian statisnesses.In mostHerecaseswe willthebrie�yMoran'sdescribI measuree the Moran(henceforthI measure.MI) spatialtics. Weeconometricshave carried outmatlabpreliminarypackageexp3 whicerimenh tsimplemenusing thets ranges b etween -1 and +1 and thus is similar to the classical a Bayesian approach using sampling based Markov Chain measureindicativeofofcorrelation.high spatialInautotuitivcorrelation.ely, a higherThisp ositivimpliese valuethatis Lesage(h3 We ttp://www.econ.utoledo.edu/would like to ~lesage)thank for Jamesmaklike values tend to cluster together or attract each other. A ing the matlab to olb ox available on the web. 



18 

A A B C D A 0 1 0 0 B 1 0 1 1 B 0 1 0 1 C C D 0 1 1 0 D (a) Map b)  Contiguity Matrix W Figure 5: A spatial neighb orho o d and its contiguity matrix Monte Carlo(MCMC) metho ds [23]. The general approach parameter-value-set �nd-A-lo cal-maxima(parametervalue-set PVS, discretization-of-parameter-space SF, of MCMC metho ds is that when the joint-probability dismap-similarity-measure-function tribution is to o complicated to b e computed analytically, MSM, learning-map-set LMS) f then a suÆciently large numb er of samples from the conparameter-value-set b est-neighb or, a-neighb or; ditional probability distributions can b e used to estimate real b est-improvement=1, an-improvement; the statistics of the full joint probability distribution. While while(b est-improvement > 0) do f thisstatistics,approacithisis averycomputationally�exible and theexpworkhorseensive proof cessBayesianwith bbest-neighbest-improvementor = PVS.get-a-neighb= MSM(b est-neighbor(SF);or,LMS) - MSM(PVS,LMS); slow convergence prop erties. Furthermore, and at least for foreach a-neighb or in PVS.get-all-neighb ors(SF) non-statisticians, it is very diÆcult to decide what \priors" do f to cho ose and what are the appropriate analytic expressions an-improvement = MSM(a-neighb or,LMS) for the conditional probability distributions. - MSM(PVS,LMS); if(an-improvement > b est-improvement) f b est-neighb or = a-neighb or; b est- **3. PREDICTING LOCATIONS USING MAP** improvement = an-improvement; **SIMILARITY(PLUMS)** g g Recall that we prop osed a general problem de�nition for if (b est-improvement > 0) then PVS=b estthe Lo cation Prediction problem, with the ob jective of maxneighb or; imizing \map similarity", which combines spatial accuracy g /* found a local maxima in parameter space */ and classi�cation accuracy. In this section, we prop ose the return PVS; PLUMS framework for spatial data mining. g **3.1 ProposedApproach: Predicting Locations** Algorithm 1: greedy-search-algorithm **Using Map Similarity(PLUMS)** Predicting Lo cations Using Map Similarity(PLUMS) is eter space, a map-similarity function and a learning data the prop osed sup ervised learning approach. Figure 6(a) set consisting of maps of explanatory and dep endent varishows the context and comp onents of PLUMS. It takes a ables. It evaluates the parameter-value tuple in the immeset of maps for explanatory variables and a map for the diate neighb orho o d of current parameter-value tuple in the dep endent variable. The maps must use a common spagiven discretization. An example of a current parametertial framework, i.e. common geographic space and common value tuple in a red-winged-black bird application with 3 discretization, and pro duces a "learned spatial mo del" to explanatory variables is (a,b,c). Its neighb orho o d may inpredict the dep endent variable using explanatory variables. clude the following parameter value tuples: (a+Æ ,b,c), (aPLUMS has four basic comp onents, namely, a map similarÆ ,b,c),(a,b+Æ ,c),(a,b-Æ ,c),(a,b,c+Æ ), (a,b,c-Æ ) given a uniform ity measure, a family of parametric functions representing grid with cell-size Æ discretization of parameter space. A spatial mo dels, a discretization of parameter space, and a more sophisticated discretization may use non-uniform grids. search algorithm. PLUMS uses the search algorithm to exPLUMS evaluates the map similarity measure on each paplore the parameter space to �nd the parameter value tuple rameter value tuple in the neighb orho o d. If some of neighwhich maximize the given map similarity measure. Each b ors have higher values for the map similarity measure, the parameter value tuple sp eci�es a function from the given neighb or with highest value of map similarity measure is family as a candidate spatial mo del. chosen. This pro cess is rep eated and it ends when no neighA simple map similarity measure fo cusing on spatial acb or has a higher value of map similarity measure, i.e., a locuracy for nest-lo cation maps(or p oint sets in general) is the cal maxima has b een found. Clearly, this search algorithm average distance from an actual nest site to the closest precan b e improved using a variety of ideas including gradidicted nest-site. Other spatial accuracy and map similarity ent descent [4, 11] and simulated annealing [32, 36] etc. measures can b e de�ned using nearest neighb or index [7], A simple function family is the family of generalized linear principal comp onent analysis of a pair of raster maps [31] mo dels, e.g. logistic regression [22] with or without auto coretc. relation terms. Other interesting families include non-linear A sp ecial case of PLUMS using greedy search is describ ed functions. In the spatial statistics literature many functions in Algorithm 1. The function "�nd-A-lo cal-maxima", takes have b een prop osed to capture the spatial auto correlation a seed value-tuple of parameters, a discretization of paramprop erty. For example, Econometricians use the family of 

19 

Generalized Linear Generalized Linear Non-Linear with Autocorrelation with Autocorrelation Search Greedy(G) SimulatedAnnealing(SA) G SA G SA Discretized Discretized Dependent Independent var. map var. maps binary raster raster Learning data PLAN PLAN PLAN PLAN **A** (1) (2) (3) PLUMS Family of functions Algo. to search Map Similarity Discretization graph (i.e. spatial models) parameter space Measures for parameter space PLAN (4) Learned Spatial PLAN Model (5) (a) PLUMS Framework (b) Space of Design Choice Figure 6: (a)The framework for the lo cation prediction pro cess. (b)Space of Design Choice for PLUMS spatial autoregression mo dels [3, 23], Geo-statisticians [17] actual nest sites. The FPR measures the ratio of the numb er use Co-Kriging and Ecologists [16] use the Auto-Logistic of sites where the nest was absent but predicted divided by mo dels. Table 1 summarizes several sp ecial cases of PLUMS the numb er of sites where the nests were absent. The ROC by enumerating various choices for the four comp onents. curve is the lo cus of the pair (T P R (b); F P R (b)) for each The design space of PLUMS is shown in Figure 6(b). cut-o� probability. The higher the curve ab ove the straight Each instance of PLUMS is a p oint in the four dimensional line T P R = F P R the b etter the accuracy of the mo del. conceptual space spanned by similarity measure, family of functions, discretization of parameter space and external search algorithm. For example, the PLUMS implementation laMetric of Comparison for Spatial Accuracy Spab eled A in Figure ?? corresp onds to the spatial accutial accuracy achieved by PLUMS, classical regression and racy measure(ADNP), generalized linear mo del(for the famSAM(Spatial Autoregressive Mo del) are compared based on ily of functions), a greedy search algorithm and uniform disADNP(Average Distance to Nearest Prediction), which is cretization. de�ned as K **4. EXPERIMENT DESIGN AND EVALUA-** 1 **TION** AD N P (A; P ) = K Xk =1 d(Ak ; Ak :near est(P )): Goals: The goals of the exp eriments are (1) to evaluate the e�ects of including the spatial autoregressive term, �W y , in Here the Ak 's are the actual nest lo cations, P is the map the logistic regression mo del and (2) compare the accuracy layer of predicted nest lo cations and Ak :near est(P ) denotes and p erformance of an instance of PLUMS with spatial rethe nearest predicted lo cation to Ak . K is the numb er of gression mo dels. The exp erimental setup is shown in Figure actual nest sites. The units for ADNP is the numb er of 7. The 1995 Darr wetland data was used as the learning set pixels in the exp eriment. to build the classical and spatial mo dels. The parameters Result of Comparison b etween Classical and Spatial of the classical logistic and spatial regression mo del were Regression (SAM) mo dels: We use the 1995 Stubble derived using maximum likeliho o d estimation and MCMC wetland data to make comparison b etween the two mo dels. metho ds(Gibbs Sampling). The two mo dels were evaluated The result is shown in Figure 8. Clearly, by including a based on their ability to predict the nest lo cations on the spatial auto correlation term, there is substantial and systest data. Classi�cation accuracy, which we describ e next, tematic improvement for all levels of cut-o� probability on was used to evaluate the two mo dels. Then we compare b oth the learning data(1995 Darr) and test data(1995 Stubthese two mo dels with PLUMS in terms of p erformance and ble). However, the p erformance of SAM mo del is very slow spatial accuracy(ADNP). and not scalable. The choice of contiguity matrix w is nonMetric of Comparison for Classi�cation accuracy: trivial, but very crucial to SAM mo del. Classi�cation accuracy achieved by classical and spatial loResult of comparison b etween PLUMS, Classical registic regression are compared on the test data. We use gression and SAM mo dels: We carried out exp eriments the Receiver Op erating Characteristic(ROC) [8] curves to to compare PLUMS with classical and spatial regression compare classi�cation accuracy. ROC curves plot the relamo dels. For this we also used the 1995 data acquired in the tionship b etween the true p ositive rate(TPR) and the false Stubble wetland. The results of our exp eriments are shown p ositive rate(FPR). For each cut-o� probability b, T P R (b) in Table 2. From the exp eriments it is clear that PLUMS(A) measures the ratio of the numb er of sites where the nest is achieves similar spatial accuracy on test datasets as SAM, actually lo cated and was predicted divided by the numb er of while it needs order of magnitude less computational time 

20 

**Solution Procedure** 

###### **Spatial Autocorrelation** 

**Learning Data Preliminary Data Build Set tests for Model Selection Model (1995 Darr data) model selection Learning Model Dataset Parameters Evaluate Testing** **<u>(SAR vs PLUMS)</u> Model Data Set (1995 Stubble data) Map Similarity (ROC Curve + ADNP)** Figure 7: Exp erimental Metho d for evaluation spatial autoregression to learn. **6. ADDITIONAL AUTHORS** The run-time for learning lo cation prediction mo dels for Additional authors: Uygar Ozesmi (Departmentt of Enthe three metho ds are shown in Table 2. We note that spavironmentaltal Sciences, Ericyeses University,ersity,y,, Kayseri,yseri, Turkey,urkey,ey,, tial regression takes two orders of magnitude more computaemail: uygar.ozesmi-1@tc.umn.edu) tion time relative to PLUMS using the public domain co de [23] despite the sparse matrix techniques [27] used in the co de. **7. REFERENCES** Figures 9(a) is the ROC curves for the three mo dels built [1] R. Agrawal. Tutorial on database mining. In using the Darr learning data and Figure 9(b) is the ROC Thirteenth ACM Symposium on Principles of curve for the Stubble test data. It is clear that by using Databases Systems, pages 75{76, Minneap olis, MN, spatial regression resulted in b etter predictions at all cut1994. o� probabilities relative to PLUMS(A), a simple and naive [2] P.S. Alb ert and L.M. McShane. A generalized implementation of PLUMS. Alternative smarter implemenEstimating Equations Approach for Spatially tations of PLUMS enumerated in Figure ?? need to b e Correlated Binary Data: Applications to the Analysis explored to close the gap. of Neuroimaging Data. Biometrics (Publisher: Washington, Biometric Society, etc.), 51:627{638, **5. FUTURE WORK AND CONCLUSION** 1995. In this pap er we have prop osed PLUMS(Predicting Lo ca[3] L Anselin. Spatial Econometrics: methods and models. tions Using Map Similarity), a framework for spatial data Kluwer, Dordrecht, Netherlands, 1988. mining. We have shown how spatial auto correlation, the [4] Vladimir Cherkassky and Filip Mulier. Learning From characteristic prop erty of spatial data can b e incorp orated Data Concepts, Theory, and Methods. John Wiley & in the PLUMS framework. When compared with state-ofSONS Inc., 1998. the-art spatial statistics metho d in predicting bird-nest lo ca[5] P. Could. The Geographer at Work. Routledge and tions, PLUMS achieved comparable spatial accuracy while Kegan Paul, London, 1985. incurring only a fraction of the cost. Furthermore, PLUMS [6] N.A. Cressie. Statistics for Spatial Data (Revised provides a template for sp ecializing other data mining techEdition). Wiley, New York, 1993. niques for spatial data. [7] P.J. Diggle. Statistical analysis of spatial point Our future plan is to bring in other data mining techpatterns. Academic Press, 1993. niques, including clustering and asso ciation rules, within the [8] J.P. Egan. Signal Detection Theory and ROC analysis. PLUMS framework. We also plan to investigate other search Academic Press, New York, 1975. algorithms , new map-similarity measures and non-uniform parameter spaces and determine their dominance zones. [9] M. Ester, H-P Kriegel, and J. Sander. Knowledge discovery in spatial databases. In Advances in 1 10,000 draws for Gibbs sampling, 1000 burn-outs Arti�cial Intel ligence, 23rd Annual German 

Additional authors: Uygar Ozesmi (Departmentt of Environmentaltal Sciences, Ericyeses University,ersity,y,, Kayseri,yseri, Turkey,urkey,ey,, 



21 

- ROC Curve for learning data(Darr marshland 1995) 

- 1 1 ROC Curve for testing data(Stubble marshland 1995) 

- 0.9 0.9 0.8 0.8 0.7 0.7 0.6 0.6 0.5 0.5 0.4 0.4 0.3 0.3 0.2 0.2 Classical Regression 

- 0.1 Classical Regression 0.1 Spatial Regression Spatial Regression 

- 00 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 0 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 False Positive Rate False Positive Rate 

- (a) Learning Data (b) Test Data 

- Figure 8: (a) Comparison of the logistic and logistic with spatial auto correlation on the 1995 Darr wetlandetland learning data. (b) Comparison of the two mo dels on the 1995 Stubble wetland testing data. Conference on Arti�cial Intel ligence, pages 61{74, Research Issues on Data Mining and Know ledge Bonn, Germany, Septemb er 1999. Discovery(DMKD'96), pages 1{10, Montreal, Canada, 

- [10] U. M. Fayyad. Knowledge discovery in databases: An 1996. overview. In Inductive Logic Programming, 7th [20] K. Kop erski and J. Han. Discovery of spatial International Workshop, ILP-97, Lecture Notes in asso ciation rules in geographic information databases. Computer Scienc, volume 1297, pages 3{16. Springer, In Advances in Spatial Databases, Proc. of 4th Septemb er 1997. International Symposium, SSD'95, pages 47{66, 

- [11] B. Flury. A First Course in Multivariate Statistics Portland, Maine, USA, 1995. (Section 7.5: Simple Logistic Regression). Springer, [21] P. Krugman. Development, geography, and economic 1997. theory. MIT Press, Cambridge, MA, 1995. 

- [12] C. Greenman. Turning a map into a cake layer of [22] J. LeSage. Regression Analysis of Spatial data. The information. New York Times, January 20th Journal of Regional Analysis and Policy (Publisher: (http://www.nytimes.com/library/tech/00/01/ Mid-Continent Regional Science Association and UNL circuits/arctiles/20giss.html) 2000. Col lege of Business Administration), 27(2):83{94, 

- [13] D. GriÆth. Statistical and mathematical sources of 1997. regional science theory: Map pattern analysis as an [23] J.P. LeSage. Bayesian estimation of spatial example. Papers in Regional Science (Publisher: autoregressive mo dels. International Regional Science Springer), (78):21{45, 1999. Review, (20):113{129, 1997. 

- [14] R.H. Guting. An Intro duction to Spatial Database [24] D. Mark. Geographical information science: Critical Systems. Vary Large Data Bases Journal issues in an emerging cross-disciplinary research (Publisher:Springer Verlag), Octob er 1994. domain. In NSF Workshop, Feburary 1999. 

- [15] M. Hohn and L. Gribko A.E. Liebhold. A [25] S. Ozesmi and U. Ozesmi. An Arti�cial neural Geostatistical mo del for Forecasting the Spatial network approach to spatial habitat mo deling with Dynamics of Defoliation caused by the Gypsy Moth, intersp eci�c interaction. Ecological Model ling Lymantria dispar (Lepidoptera:Lymantriidae). (Publisher: Elsevier Science B. V.), (116):15{31, 1999. Environmental Entomology (Publisher: Entomological [26] U. Ozesmi and W. Mitsch. A spatial habitat mo del for Society of America), 22:1066{1075, 1993. the Marsh-breeding red-winged black-bird(agelaius 

- [16] F. Hu�er and H. Wu. Markov chain monte carlo for pho eniceus l.) In coastal lake Erie wetlands. Ecological autologistic regression mo dels with application to the Model ling (Publisher: Elsevier Science B. V.), distribution of plant sp ecies. Biometrics (Publisher: (101):139{152, 1997. Washington, Biometric Society, etc.), 54(3):509{535, [27] R. Pace and R. Barry. Sparse spatial autoregressions. 1998. Statistics and Probability Letters (Publisher: Elsevier 

- [17] Issaks, Edward, and Mohan Srivastava. Applied Science), (33):291{297, 1997. Geostatistics. Oxford University Press, Oxford, 1989. [28] R.J.Haining. Spatial Data Analysis in the Social and 

- [18] E. Knorr and R. Ng. Finding Aggregate Proximity Environmental Sciences. Cambridge University Press, Relationships and Commonalities in Spatial Data Cambridge, U.K., 1989. Mining. IEEE TKDE, 8(6):884{897, 1996. [29] John F. Ro ddick and Myra Spiliop oulou. A 

- [19] K. Kop erski, J. Adhikary, and J. Han. Spatial data bibliography of temp oral, spatial and spatio-temp oral mining: Progress and challenges. In Workshop on data mining research. ACM Special Interest Group on 

Darr wetlandetland 

22 

1 ROC Curve for learning data(Darr) 1 ROC Curve for testing data(Stubble marshland) 0.9 0.9 0.8 0.8 0.7 0.7 0.6 0.6 0.5 0.5 0.4 0.4 0.3 0.3 0.2 0.2 Classical Regression Classical Regression Spatial Regression Spatial Regression 0.1 PLUMS(A) 0.1 PLUMS 0 0 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 False Positive Rate False Positive Rate (a) ROC curves for Learning Data (b) ROC curves for Test Data Figure 9: (a) Comparison of PLUMS(A) with other metho ds on the Darr learning data. (b) Comparison of the mo dels on the test data. Know ledge Discovery in Data Mining(SIGKDD) **8.1 Moran’s I measure** Explorations, 1999. There are many measures available for quantifying spatial [30] S. Shekhar and S. Chawla. Spatial Databases: Issues, auto correlation. Each have their own strengths and weakImplementation and Trends. (Under Contract)Prentice nesses. The two most well known measures are Moran's I Hall, 2000. and Geary's C measure. Here we will brie�y describ e the [31] R. Schowengerdt. Remote Sensing:Models and Moran I measure. Methods for Image Processing. Academic Press, 1997. In most cases the Moran's I measure (henceforth MI) [32] S. Shekhar and B. Amin. Generalization by neural ranges b etween -1 and +1 and thus is similar to the classical networks. IEEE Trans. on Know ledge and Data Eng., measure of correlation. Intuitively, a higher p ositive value is 4(2), 1992. indicative of high spatial auto correlation. This implies that [33] S. Shekhar, S. Chawla, S. Ravada, A.Fetterer, X.Liu, like values tend to cluster together or attract each other. A and C.T. Lu. Spatial databases: Accomplishments and low negative value is an indication that high and low valResearch Needs. IEEE Transactions on Know ledge ues are intersp ersed. Thus like values are de-clustered and and Data Engineering, 11(1), Jan-Feb 1999. tend to rep el each other. A smo oth surface will have a high [34] S. Shekhar, T. A. Yang, and P. Hanco ck. An spatial auto correlation and a chessb oard-like surface a high intelligent vehicle highway information management negative spatial auto correlation. A value close to zero is system. Intl Jr. on Microcomputers in Civil an indication that no spatial trend (random distribution) is Engineering (Publisher: Blackwel l Publishers), 8(3), discernible using the given measure. 1993. The formula for MI is [35] Ge1979.W.R.ographyTobler.. GaleCelandlularOlsson,Geography,Eds.,PhilosophyDordrecht,inReidel, M I = Pii==1n Pnjj ==1n Wij � Pii==1n PjjP==1nii==1Wn (ijx(ix�i �x�)x�2)(xj � x� ) [36] V. Vapnik. The Nature of Statistical Learning Theory. where n is the numb er of data p oints, x0i s are the data Springer Verlag, New York, 1997. values, x� is the mean and W is the design or contiguity [37] M.F. Worb oys. GIS: A Computing Perspective. Taylor matrix. All spatial auto correlation measures are crucially and Francis, 1995. dep endent on the choice and design of the contiguity matrix [38] Y. Yasui and S.R. Lele. A Regression Metho d for W. Spatial Disease Rates: An Estimating Function Approach. Journal of the American Statistical **8.2 Summary of different methods** Association, 94:21{32, 1997. We summarized all the metho ds that have b een used to build the bird habitat mo del in Table 3. **8.3 Example of including the spatial autore8. APPENDIX:SPATIAL AUTOCORRELAgressive term TION** 

23 



<!-- Start of picture text -->
Contiguity Matrix(W) of the spatial locations<br>0<br>5<br>10<br>15<br>20<br>25<br>30 R-square Moran I<br>(residual)<br>35<br>40 Ordinary Regression 0.5521 0.23<br>45<br>500 5 10 15 20 25 30 35 40 45 50 Spatial Auto Regression 0.6518 0.04<br>nz = 232<br><!-- End of picture text -->



<!-- Start of picture text -->
Discretization of parameter space Uniform, non-uniform, multi-resolution, ...<br><!-- End of picture text -->



<!-- Start of picture text -->
Learning Run-time(Seconds) 80 10 19420 1<br><!-- End of picture text -->



<!-- Start of picture text -->
Metho d Mo del Spatial Dep endent Accuracy Solution<br>Name Typ e AC Var. Typ e Measure Pro cedure<br><!-- End of picture text -->



<!-- Start of picture text -->
Linear Linear No Numeric Total Square Closed Form<br>Regression Error(TSE)<br><!-- End of picture text -->



<!-- Start of picture text -->
Regression Error(TSE)<br>Neural NonLinear No Numeric/ TSE Gradient Descent<br><!-- End of picture text -->



<!-- Start of picture text -->
Networks Categorical Back-Propagation<br>Probit Gen. No Binary TPR/FPR Gradient Descent<br><!-- End of picture text -->



<!-- Start of picture text -->
Linear<br>Logit Gen. No Binary TPR/FPR Gradient Descent<br><!-- End of picture text -->



<!-- Start of picture text -->
Linear<br>SAM + Gen. Yes Binary TPR/FPR ML/EM/Gibbs<br><!-- End of picture text -->



<!-- Start of picture text -->
Probit Linear<br><!-- End of picture text -->

24 

#### **Learning Prosodic Patterns for Mandarin Speech Synthesis** 

Yiqiang Chen Wen Gao Institute of Computing Technology Chinese Academy of Sciences Beijing, China 100080 Email: yqchen@ict.ac.cn 

Tingshao Zhu Dept. of Computing Science University of Alberta Edmonton, Canada T6G 2H1 Email: tszhu@cs.ualberta.ca 

###### **ABSTRACT** 

Higher quality synthesized speech is required for widespread use of text-to-speech (TTS) technology, and prosodic pattern is the key feature that makes synthetic speech sound unnatural and monotonous, which mainly describes the variation of pitch. The rules that are now being used in most Chinese TTS systems are constructed by experts, qualitatively and with low precision. In this paper, we propose a combination of clustering and machine learning techniques to extract prosodic patterns from actual large mandarin speech database to improve the naturalness and intelligibility of synthesized speech. Typical prosody models are found by clustering analysis, some machine learning techniques including Rough Set, ANN and Decision tree are trained respectively for fundamental frequency and energy contours, which can be directly used in a pitch-synchronous-overlap-add-based (PSOLA-based) TTS system. The experimental results showed that synthesized prosodic features quite resembled their original counterparts for most syllables. 

###### **Keywords:** 

TTS, Pitch, Mandarin Speech Synthesis, Data Mining 

###### **1.INTRODUCTION** 

Text-To-Speech (TTS) technology is currently useful only in a limited number of applications because the quality of synthetic speech is not as good as people expected. Prosody, which includes the phrase and accent structure of speech, is one of important component for TTS system. In the field of speech signal process, pitch (fundamental frequency and F0) is the most mysteriously expressive of the prosodic phenomena, and the variation of pitch in speech can be used to express the speaker’s intention, especially in Mandarin. 

Although many researchers have proposed some prosodic variation patterns, the patterns are described qualitatively, or with great limitation. Wu [1][2] found that in Mandarin when syllables are combined, their tones changed to be continuous, and he gave some qualitative rules. Chu [3] uses some pitch patterns in Chinese speech synthesis system, including 14 kinds of pitch shapes of isolate syllables and 22 kinds of shapes of two-word phrases, but obviously only these shapes can’t describe the variations of Mandarin to a large extent. 

In recent years, some researchers intend to learn the variation 

© The copyright of this paper belongs to the paper's authors. Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 (O.R. Zaïane, S.J. Simoff, eds.) 

patterns base on large speech database. Lee S. and Oh Y-H [4] describes the tree-based modeling of prosodic phrasing, pause duration for Korean TTS system. Ostendorf [5] describes a dynamical system model for generating fundamental frequency, which allows automatic estimation of parameter from labeled large speech database. Hu [6] proposed a template-driven generation of prosodic information for Chinese text-to-speech conversion. Ross KN. Chen [7] proposed a new RNN-based prosodic information synthesizer for Mandarin Chinese text-to-speech. Cai [8] establish a Chinese text to speech system and a prosody learning system based on NN. 

Although these methods have made advances, they are still far away from reaching the goal of generating proper prosodic information for synthesizing speech with high naturalness. The drawback lies in their inability to elegantly invoke higher-level linguistic features in exploring the prosodic phrase structure of Mandarin speech. This motivates us to use a combination of clustering and ML techniques to learn prosodic variation patterns to improve the naturalness and intelligibility. 

This paper is organized as follows. Sections 2 introduce TTS, Sections 3 discuss the clustering of prosodic pattern. The Training process and the prediction are described in Section 4, and some conclusions of our on-going research will be given in Section 5. 

###### **2.  TEXT TO SPEECH** 

The three main steps in the TTS process are illustrated in Figure.1. 



**Figure 1 TTS system** 

25 

Speech synthesized from text suffers from a major shortcoming - it sounds synthetic. It is found that synthetic speech significantly more difficult to comprehend than natural speech.  There is broad consensus that poor prosody is the key feature that makes synthetic speech sound unnatural and monotonous.  Prosody conveys the relative importance of words by making these words stand out acoustically (prominence), and helps listeners "chunk" the message by inserting acoustic punctuation marks (phrasing) as pauses, decreases in rate, and characteristic pitch movements. Speech with inappropriate prosody prevents listeners from understanding the spoken message. It will also undermine the credibility and effectiveness of the animated character that produces it. 

Prosody in TTS systems involves three levels. First, text analysis components compute phrase boundary locations and prominence ("prosodic structure"). Second, acoustic prosodic components compute phoneme duration, fundamental frequency (or pitch) contours, and (optionally) contours for additional acoustic parameters such as amplitude or spectral tilt. Finally, signal processing components compute a digital speech wave that expresses the phoneme sequence having the desired timing and pitch contour. 

The main goal of our work is to improve the prosodic structure of speech generated from text. The TTS system must analyze text and use this information to generate both a symbolic structure (e.g., locations and type of phrase boundaries and prominence of important words) and an acoustic waveform that expresses the desired meaning of each utterance. 

This general problem of lack of an appropriate prosodic model was encountered in Mandarin TTS prosodic information synthesis. Mandarin Chinese is a tonal language. Each character is pronounced as a syllable. Only about 1300 phonetically distinguishable syllables comprise the set of all legal combination of 411 base-syllables and five tones. Each base-syllable is composed of an optional consonant initial and a vowel final. The word, which is the smallest syntactically meaningful unit, consists of one to several syllables. Because syllables are the basic pronunciation units in Mandarin speech, they are commonly chosen as the basic synthesis units in Mandarin TTS systems. Accordingly, the prosodic information that must be synthesized includes syllable pitch (F0) contour, syllable energy contour, syllable initial and final duration, as well as intersyllable pause duration. Among them, syllable pitch contour has the most important effect on naturalness of synthetic speech. So pitch contour synthesis is of primary concern in Mandarin TTS. The tone of syllable is mainly determined by its F0 contour. However, the pronunciation is usually highly context-dependent, It would seem that syllable F0 contour are various modification in continuous speech. Therefore, the F0 generation is not a trivial task. There are many methods have been proposed in the past, including rule-based methods [9][10], statistical model-based methods [4][6], and MLP-based methods [7]. In contrast to other researchers who employ a single technique, we present a combination of clustering and ML techniques, applied for the identification of relationship(s) between sound characteristics of speech pattern and linguistic features of the corresponding text. 

We assume that the F0 contour in the continuos speech data are not variety randomly but can be obtained through modifying some classic F0 model with duration and mean. These classic F0 models can be obtained from the preprocessed actual F0 contours. 

###### **3.DATA PROCESSING** 

###### **3.1 Speech Database** 

The speech corpora and the labeled speech corpora will be used for our acoustic prosody and signal processing efforts. The Speech Database that we are using is a Chinese speech synthesis database called CoSS-1. CoSS-1 includes the pronunciation of all isolate syllables, the 2-4 word phrases and some sentences. The number of isolate syllables with tone is 1268, and that of word phrase is 1640 and sentence is 210. 

CoSS-1 records the speech wave and laryngograph synchronously. The sampling rate is 16000/s, and each sample is stored in two bytes. The sentence in the database covers almost the whole tone collocations in Chinese pronunciation. 

The preprocessing mainly deals with the data from speech database directly, which extracts pitch, wraps the duration and normalizes and smooth and zero mean the pitch values to meet the requirement of cluster algorithm. 

###### **3.2 Pitch Extraction** 

To learn the patterns, the pitch should be calculated at first. There are many methods to extract pitch from speech wave, but the precision is very low [11]. Since we want to learn the patterns and use them to generate pitch after training, the accuracy is very important. 



**Figure. 2.** A snapshot of Pitcher. A tool called Pitcher is implemented to extract pitch from laryngograph. It works by annotating each cycle’s beginning and ending point, then calculating the pitch. Let Xi be the beginning point of one cycle and Xj be the ending point, then the pitch of this cycle should be 16000/(Xj - Xi). Pitcher can also be used to split phrases and play the speech data. Figure 2 gives a snapshot of Pitcher. 

Pitcher can be used to split a phrase and annotate each syllable. 

26 

The results of splitting and annotating are stored in database, then the algorithm can retrieve them for training and testing. To annotate pitches, you should firstly sign the reference cycle, then the beginning and ending point of the period. Pitcher deals with cycles one by one within the period to calculate pitches. 

###### **3.3 Time Wrapping and Normalization** 

The length of pitches that should acts as the training examples differs from each other significantly. A new algorithm is designed to wrap the pitches, which differs from the traditional time wrapping method DTW [11](Dynamic Time Wrapping) which is widely used in speech signal process. Figure 3 gives the new algorithm. 



The ISODATA [12](Iterative Self-organizing Data) algorithm is chosen for our clustering, the main procedures are the following: 

###### **_3.6.1Present the clustering parameters_** 

**_C:_** number of expected classes; _MaxIterate_ : the Max times for adjusting; **_MinSamples:_** the Min number of objects in one class; **_I_** _:_ combination parameter; **_J:_** partition parameter. 

###### **_3.6.2Choose initial cluster centers_** 

For the speech data we used, the pitches’ value domain is between 50 – 260. In this paper, the following equation is used to normalize the pitch value. 

###### _Normalized = (Pitch – min) / (max - min)_ (1) 

Where _max_ is the maximum of all pitches’ value and _min_ is the minimum. _Pitch_ stores the pitch to be calculated and _Normalized_ is the normalized value. 

**3.4 Smoothing and filter:** There are many filter algorithms in signal processing [11]. In this paper, the window design filter is presented to eliminating the large fluctuant data. Assume a sequence of observations _X_ = [ _x_ 0 , _x_ 1, K ,<sup>_x_</sup> _n_ ] , the windows width is m. we can gain another sequence states _Y_ = [ _y_ 0 , _y_ 1, K ,<sup>_y_</sup> _n_ − _m_ + 1] with the following formulation (2): 



**3.5 Zero-mean:** To avoid the effect of F0 energy, zero-mean method is proposed for each pitch fundamental frequency. The zero-mean method represents a sequence of observation _X_ = [ _x_ 0 , _x_ 1, K ,<sup>_x_</sup> _n_ ] in terms of a sequence of states _Y_ = [ _y_ 0 , _y_ 1, K ,<sup>_y_</sup> _n_ ] with the following equation (3): 



**3.6Clustering method:** The quantification of the similarity notion is important for clustering, and in our clustering, we use the following one: 



> Calculate the mean<sup>_x_</sup> _i_<sup>and variance</sup> _si_ ( _i_ = 3,2,1,..., _n_ ) 



###### **_3.6.3Classify and adjust the objects based on K-means algorithm_** 

If there is no re-distribution of the objects in any cluster happens or the max times **_MaxIterate_** for adjusting is achieved, the process terminates, otherwise, the adjusting will be repeated as following: 

**_Deleting_** if the number of objects in some class is less than **_MinSample_** then the class should be deleted, at the same time, the objects in that class will not be reused. 

**_Partition_** assume that m classes are generated after several times overlapping, and there must be  one character in n of each class holding the Max variance. Let 



> Where _s_ max reprsent the mean of max variance of all the classes. 

To each class, the max variance SI  of  every character can be calculated if Si> _Sthreshold_ then this class should be partitioned as following: ( _x_ 1, _x_ 2 ,..., _xi_ ± _si_ ,..., _xn_ ) , _i_ = 2,1,..., _n_ 

**_Combination:_** assume that m classes are generated after several times overlapping, and the min distance value between every two centers can be obtained. Let 



27 

Where _D_ min reprsent the mean of min distance of all the classes. 

To every two classes, if the distance between their centers is less than _Dthreshold_ then they are combined, and the center of new class should be recalculated. After clustering, there are 18 F0 pattern are classified, Figure 3 shows them: 

After clustering, there are 18 F0 pattern are classified, Figure 3 shows them: 





































**Figure 3: F0 patterns after clustering analysis.** 

The original pitch from sentences is discreted with extracted classic F0 models, and at the same time the original length and mean should be kept for future learning. The original prosody pattern is preprocessed into three parts: zero-mean F0 pattern, duration, and mean. 

###### **4. PROSODIC LEARNING** 

###### **4.1 Linguistic Features** 

Our aim is to explore the relationship between the prosodic pattern of Mandarin speech and the linguistic features of the input text to simulate human’s prosody pronunciation mechanism. 

The Chinese Dictionary that we are using includes the spell, vowel, constant, tone, part of speech (POS), and some word syntax and semantic. From this dictionary and the existence of a text processing model, the lexical information (phonemic representations and lexical stress) and symbolic prosodic markers can be obtained. In this paper, after parsing, the linguistic features including the following: 

The number of pitch in word The sequence number serial number of pitch in word Word class and POS Is substantive or function word? Is prediction or noun word? The vowel, constant and tone of current pitch The vowel, constant and tone of prior and post pitch 

###### **4.2 Feature Selection** 

Before training, the Rough set [13][14] is proposed to find the minimum attribute set. The rough set theory is based on indiscernibility relation. Suppose four finite, non empty sets R, A, V and f, where R is the universe, and A is a set of attributes, V is the value set of each attribute and f is a function map _f_ ( _U_ , _A_ ) → _V_ . The indiscernible relation I is associated with every subset of attributes _P_ ∈ _A_ and defines as: _I(P)_ = _{(ri,rj )_ ∈ _U_ × _U:f(ri,attr)_ = _f(rj,attr),_ ∀ _attr_ ∈ _P}_ Where _f (rI, attr)_ is the value of attribute _attr_ in object _ri_ . If ( _ri_ , _rj_ ) ∈ _I_ ( _P_ ) , then _ri_ and _rj_ are P-indiscernible. 

Rough set can remove unnecessary attributes from the set A by considering redundancies and dependencies between attributes. Let P be a subset of A, and the initial P is the set A. If _I_ ( _P_ ) ≠ _I_ ( _P_ − { _attr_ }) , then we say that the _attr_ can be moved from the set A. Thus the main features are selected by Rough set. The main features are used as input of ANN and the condition attributes of decision tree. We construct three ANN or decision trees respectively, they can predict the F0 model, the F0 mean and the F0 duration. 

###### **4.3 Training and Prediction** 

There are many kinds of neural networks, which can be used for learning. We intend to learn the mapping between the linguistic features and the F0 mean value. Since backpropagation network has implicit input layer and output layer [15], and it can also give very good result, thus it is chosen to be trained in our system. 

In order to generate training and testing data, all the sentences are split firstly, calculating the pitches, wrapping the pitches to the same length, normalizing pitches’ value and discrete the pitch. Then the pitch class, the linguistic parameters obtained by text parsing are labeled for neural net training and testing. For the network learning the F0 model, its input layer consists of 28 units, and the hidden layer consists of 34 units. There is only one unit in output layer. The input layer’s units are described as Table 1. 

**<u>Table 1: the definition of input layer</u>** 

|<br>Numberofunits|<br>Description|
|---|---|
|4|Length of word(1-4)|
|4|Pitch’slocation inword|
|5|Partofspeech|
|6|Vowel/consonant|
|3|Tone ofpitch|
|3|Tone ofprevious pitch|
|3|Tone of next pitch|



The training of the F0 length and the F0 mean are as same as the training of F0 model. Then Three different neural networks are constructed to predict the F0 model, the F0 mean and the F0 length respectively. 

Using the same linguistic parameters as condition attributes and the F0 model, the F0 mean and the F0 lengths as decision 

28 

var _iation_ 1 + var _iation_ 2 + _mean unsimilarity_ = 

attribute, three different decision trees are constructed respectively. The C4.5 system [16], which has many advantages in building decision tree, is selected for our construction. 

After training, the NN and the decision tree can be used to predict and generate the fundamental frequency. We compared two ways and results shows in Table 2. 

OL means original Length of pitch LPDT means Length predicted by decision tree LPNN means Length predicted by ANN OM means original mean of pitch MPDT means mean predicted by decision tree MPNN means mean predicted by ANN 

|**Table 2:**<br>|**some pre**<br>|**dict result**<br>|**of NN an**<br>|**d Decisio**<br>|**n tree**<br>|
|---|---|---|---|---|---|
|OL|LPDT|LPNN|OM|MPDT|MPN<br>N|
|(zhi2)24|17.5|27.8|261.4|185|246.4|
|(pai2)45|37.5|29.1|234.4|175|239.2|
|(shi4) 32|27.5|36.2|251|265|235|
|(ran2)38|7.5|31.5|197|165|167.5|
|(qi4)26|27.5|24.2|275.5|285|248.5|
|(re4) 35|32.5|24.1|277.3|255|255.3|
|(shui3)5|17.5|8.9|173|245|163.8|
|(qi4)26|27.5|24.4|211.6|185|206.7|
|(yan2)31|22.5|21.8|196|215|198|
|(jin4)16|27.5|22.2|252.7|235|249.8|
|(an1)24|17.5|32.2|249.5|315|239.3|
|(zhuang4<br>)36|17.5|41.4|275.9|275|262.4|
|(zai4)28|42.5|30.1|233.3|305|277.3|
|(yu4)43|27.5|34|266|285|257.2|
|(shi4)6|37.5|25.5|173.7|185|189|
|(nei4)30|22.5|23.2|238.9|305|238.6|
|(shi3)12|27.5|14.7|140.9|185|144.2|
|(yong4)1<br>0|37.5|20.3|168.6|245|195.1|



The experiment was taken on our labeled large speech database, the variation of the data between the original data and the predicted one was calculated as follow: 



<!-- Start of picture text -->
n<br>−<br>( prediction original )<br>mean = ∑ i = 1<br>n<br>n<br>− 2<br>( prediction original )<br>∑ i = 1<br>var iation 1 =<br>n<br>n<br>( prediction − original − mean )2<br>∑ i = 1<br>var iation 2 =<br>n<br><!-- End of picture text -->

###### 3 

Table3 shows the variations of predicted result: 

**<u>Table 3: The variations of predicted result</u>** 

|variation|F0model|F0 duration|F0mean|
|---|---|---|---|
|Decision<br>tree|2.6|5.9|33.8|
|ANN|1.8|3.3|11.7|



The results show that the decision tree is not good at predicting the continuous attribute while ANN can do it well. Thus the decision tree is only be used to predict the F0 model while the BP was used to predict the F0 mean and F0 length. The linguistic features are reselected focus on each prediction respectively, and Table 3,4 shows the summary of our features selection: 

**Table4: Attributes of Decision tree for F0 model** 

|Number ofpitches in word(len)|
|---|
|Series number ofpitches(wordno)<br>**Condition**|
|Part of  Speech(type)<br>**Attributes**|
|Substantive or function word(xs)|
|prediction or noun word(tw)|
|Current tone, pretone, posttone|
|**Decision**<br>F0 model|



Some rules for F0 model prediction 



type = 1 and tone = 2 and pretone = 3 and posttone = 2-> class 4 len = 3 and type = 1 and tone = 2 and posttone = 5 -> class 4 type = 4 and tone = 2 and pretone = 5 and posttone = 4 -> class 13 type = 6 and tone = 2 and pretone = 4 -> class 14 

**<u>Table 5: the definition of input/output layer</u>** 

|<br>Number ofpitches in word(len)|
|---|
|Series number ofpitches(wordno)<br>**Input layer**|
|Part of  Speech(type)<br>**Definition**|
|Substantive or function word(xs)|
|Prediction or noun word(tw)|
|Consonant and tone(pycon,tone)|
|pretone, posttone|
|**Output of**<br>**NN**<br>Length of F0(discreted)|



###### **4.4Experiment** 

The F0 models are predicted by decision tree while the F0 duration and mean are predicted by ANN. The F0 model can be modified in accordance with F0 duration and F0 mean. The modification is based on a simple interpolation method. The experiment was taken on the CoSS-1 speech database, some experiment results are showed in figure 4. 

zhi pai shi re shui qi yan jin an zhuang zai yu shi nei shi yong 

29 





































###### **6.REFERENCES** 

- [1] Zongji Wu, “The tone variation in mandarin”, _Chinese grammar_ . No. 6, pp.439-449, 1982. 

- [2] Zongji Wu, “The design of prosodic rule for improving the naturalness of the Marian TTS”, _The research on Chinese language and words_ , _Tsinghua University press,_ pp.355-365, 1996. 

- [3] Min Chu, “Research on Chinese TTS system with high intelligibility and naturalness”, _Ph.D thesis_ , Institute of Acoustics, Academia Sinica, 1995. 

- [4] Lee S, Oh Y-H, “Tree-based modeling of prosodic phrasing and segmental duration for Korean TTS system”, _Speech Communication_ , Vol.28, No.4, pp.283-300, 1999. 











wo3qing3ta1jie4shao4yi1xia4ke4dian4deqing2kuang4 































**Figure 4 above is original pitch, lower is synthesis one** 

###### **5.CONCLUSION** 

In this paper, we propose a combination of clustering and machine learning techniques to extract prosodic patterns from actual large mandarin speech database to improve the naturalness and intelligibility of synthesized speech. Typical prosody models are found by clustering analysis, some ML techniques including Rough Set, ANN and Decision tree are trained respectively for fundamental frequency and energy contours, which can be directly used in a pitch-synchronousoverlap-add-based (PSOLA-based) TTS system. The prediction result of ANN and Decision Tree can be combined to generate the fundamental frequency and energy contours. So, the effects of high-level linguistic features on prosodic information generation are well handled. The experimental results showed that synthesized prosodic features quite resembled their original counterparts for most syllables. 

- [5] Ross KN, Ostendorf M, “A dynamical system model for generating fundamental frequency for speech synthesis”, IEEE _Transaction on speech and audio processing_ , Vol. 7, No. 3, pp.295-309, 1999. 

- [6] Chung-Hsien Hu, Jan-Hung Chen, “Template-driven generation of prosodic information for Chinese concatenate synthesis”, IEEE _International Conference on Acoustics, Speech, and Signal Processing_ , Vol.1, pp.65-68, 1999. 

- [7] Sin-Horng Chen, Shaw-Hwa Huang, Yih-Ru Wang, “An RNN-Based Prosodic Information Synthesizer for Mandarin Text-to-Speech”, IEEE _Transaction on speech and audio processing_ , Vol. 6, No. 3, pp.226-239, 1998. 

- [8] Cai Lianhong, Zhang Wei, Hu Qiwei, “Prosody learning and simulation for Chinese text to speech system”, _Qinghua Daxue Xuebao/Journal of Tsinghua University_ , Vol.38, No.S1, pp.92-95, 1998. 

- [9] L.S.Lee, C.Y. Tseng, and M. Ouh-Young, “The synthesis rules in a chinese text-to-speech system”, _IEEE trans. Acoust., speech, signal Processing,_ Vol. 37, pp. 13091320, 1989. 

- [10]C.H. Wu, C. H. Chen, and S. C. Juang, “An CELP-based prosodic information modification and generation of Mandarin text-to-speech”, _in proc. ROCLING VIII_ , pp. 233-251, 1995. 

- [11]L.Rabiner and B.Juang. “Fundamentals of Speech Recognition.” _TsingHua University Publishing Company_ . 1999. 

- [12]Bian Zhaoqi and Zhang Xuegong, “Pattern recognition”, _TsingHua University Publishing Company_ . 1999. 

- [13]Pawlak Z, “Rough classification”, _International Journal of Human-Computer studies_ , Vol.51, No.2, pp.369-383, 1999. 

- [14]Walczak B, Massart DL, “Rough sets theory”, _Chemometrics &Intelligent Laboratory Systems_ , Vol.47, No.1, pp.1-16, 1999. 

- [15]Wang Wei. Principle of Artificial Neural Network ---rudiment and implement. _Beijing University of Aeronautics and Astronautics Press_ , 1995 

- [16]J.Ross Quinlan, “C4.5: Programs for Machine Learning”, _Morgan Kaufmann Publishers press_ , 1993. 

30 

### **for Multimedia Indexing** � 

###### Osmar R. Za¨ıane 

Bruce Matichuk 

Department of Computing Science Department of Computing Science University of Alberta University of Alberta Edmonton, Alberta, Canada Edmonton, Alberta, Canada matichuk@cs.ualberta.ca zaiane@cs.ualberta.ca **ABSTRACT** the division of samples into small recognizable sound segSegmenting audio streams in a signi�cant manner and clusments that can b e combined to recognize complex sound pattering sound segments ob jectively, is a signi�cant challenge terns. Sounds are comp osed of signals at multiple frequendue to the nature of audio data. This pap er presents some cies that can b e graphed on a Time-Frequency Distribution preliminary work on clustering sound segments based on fregraph (TFD). Real world ob jects vibrate with characterisquency and harmonic characteristics. New metrics for comtic vibrations and thus pro duce sound waves with characparing the similarity of sound segments are also devised. teristic harmonics that allow p eople and systems to p erform sound recognition. A harmonic is a comp onent frequency **Keywords** of a complex wave that is an integral multiple of the fundaMultimedia Data Mining, Sound Pro cessing, Classi�cation, mental frequency. A sound segment is analyzed by observing Clustering, Similarity comparison the frequency amplitude pattern that o ccurs in the segment. Standard pattern recognition techniques can b e used to recognize a frequency amplitude pattern including, neural nets, **1. INTRODUCTION** b elief nets, decision trees, distance metrics, etc. Multimedia systems play an increasingly imp ortant role in our daily lives. Access to media through the Internet, and The diÆcultyy in analyzing comp ound sounds lies in the by a growing numb er of electronic media recording and playproblem of dividing a comp ound sound intoto recognizable back devices, is in�uencing and changing our lives in a prosegmentsts and classifying these segments.ts. Consider the sp eech found way. Navigating through the vast amounts of multirecognition problem. Sp eechh can b e vieweded as a sequence media data b eing generated is b ecoming an overwhelming of sound segmentsts that can b e recognized individually and problem. Although automated techniques for accessing electherefore combinedbined intoto comp ound segmentsts representingting tronic media are b eing develop ed, the science is still in an phonemes and words.ords. Other real-worldorld sounds can b e treated embryonic stage. In the area of audio-data, there has b een in a similar way.ay.y.. Foror example, consider the sounds of a dog promising early research fo cusing on sup ervised learning techbarking or a childhild crying. Both representt sounds that can b e niques. The authors argue that unsup ervised techniques describ ed byy collections of individually recognizable sound are required to handle real world retrieval situations. The segments.ts. research presented investigates a clustering technique that provides an automated classi�cation scheme for short sound The �rst task of classi�cation is to decide up on a classisamples. Recognition of short samples can b e combined with �cation scheme. With sounds, this is diÆcult b ecause of well-known pattern recognition algorithms to provide a vithe large numb er of variations p ossible for any given sound able sound retrieval system. The research could b e applied segment. Our hyp othesis is that clustering techniques can to synthetising sp eech and sound, automatic text to sp eech b e used to classify sound segments in an unsup ervised way. conversion and sound compression. This hyp othesis is based on the observation that sound samples are comp osed of recurring sound segments and that the General sound recognition is a diÆcult problem requiring characteristics of these segments can b e determined by clus� Work in Progress. tering segments that seem similar. The segments within Research is supp orted in part by the Natural Sciences and each cluster can b e analyzed to determine each cluster's repEngineering Research Council of Canada. resentative feature set. The remainder of the pap er is organized as follows. In Section 2, we intro duce some related work to audio analysis. In © The copyright of this paper belongs to the paper's authors. Permission to copy without Section 3, We present the metho dology adopted for clusterfee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. ing sound segments. A similarity metric for clustering sound Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), is presented in Section 4. Section 5 describ es some prelimin conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 (O.R. Zaïane, S.J. Simoff, eds.) inary exp eriments on frequency-based and harmonic-based clustering. Finally, we conclude our study and give some p ointers to future work in Section 6. 

The diÆcultyy in analyzing comp ound sounds lies in the problem of dividing a comp ound sound intoto recognizable segmentsts and classifying these segments.ts. Consider the sp eech recognition problem. Sp eechh can b e vieweded as a sequence of sound segmentsts that can b e recognized individually and therefore combinedbined intoto comp ound segmentsts representingting phonemes and words.ords. Other real-worldorld sounds can b e treated in a similar way.ay.y.. Foror example, consider the sounds of a dog barking or a childhild crying. Both representt sounds that can b e describ ed byy collections of individually recognizable sound segments.ts. 



31 

**2. RELATED WORK** signal are relative to the harmonic characteristics of a vibratAudio retrieval techniques are generally classi�ed as contenting ob ject and tend to b e indep endent of pitch. Consider a based or browser-based [13]. Content-based retrieval allows p erson making the sound `oh' with a low pitch versus a high the search through audio for a segment using some prepitch. The harmonic characteristics in b oth cases will b e virde�ned criteria. Browsing allows a user to scan through tually identical although the frequency comp osition will b e audio based on some navigational parameters. Both methcompletely di�erent. Similarity clustering using frequencies o ds require some kind of lab eling of audio data that can b e will cluster sounds that are similar in pitch regardless of the used in the search pro cess. Audio analysis to supp ort searchharmonics. Consider the sound `oh' versus `ee' at the same ing can vary with resp ect to the semantic nature of the data. pitch. Both of these sounds will have closely matched freSearch tasks can b e semantically simple such as \Find the quencies at a given pitch and will thus b e indistinguishable next lo cation of 1 second of silence." Search tasks can also based on a frequency by frequency comparison. b e semantically diÆcult, such as \Find all o ccurrences of the word `the'." Some techniques b eing used to index sounds use A further consideration in sound analysis is the length of a generated feature vector as an index [12]. Some systems time of a sample segment. Shorter segments are more usecan analyze temp oral patterns [6]. The main diÆculty of ful in describing complex sounds such as sp eech. FFTs over currently researched techniques stems from the inability to shorter segments, however, are less accurate. There is an detect \in-context" high-level semantics of sound. Recent ideal length for a variety of sound typ es and optimal length research that uses cognitive mo dels[13] app ears promising may even vary within a sound sample. Tests regarding timbut is limited by the small numb er of classi�cations used to ing are not rep orted in this pap er but the to olkit that was segment sounds. No attempt is made to discover high-level develop ed allows for timing variations. All of our tests were structure in sound in an automated way. Research in [10] p erformed using 1/10th-second time segments. The testexplores a broader range of sound classes but also do es not ing software we develop ed is able to handle arbitrary time attempt to deal with complex structure. Instead, heuristics segments, however, 1/10th-second intervals seemed to proare used to detect features within sound that can b e used duce the b est results. A future pap er will rep ort results on to classify sounds in some pre-determined way. varying time segments. Most research in advanced audio pro cessing has b een p erformed in the context of sp eech recognition. However, the techniques used are �nely tuned toward extracting human **3.1 Clustering Sound Samples** sp eech patterns and detecting pre-determined natural lanTo investigate sound sample clustering, a test system was guage structures. We are examining a technique that is able develop ed whereby a tester could easily record sounds and to automatically determine the features and the structure of apply a clustering algorithm to the sample. Two techniques sounds suitable for general recognition and audio retrieval. for comparing sound samples were investigated. One technique was devised to compare two samples on a frequency **3. METHODOLOGY** by frequency basis. Another technique was devised which The real world is comp osed of ob jects that generate sounds allows the comparison of harmonic characteristics. A sethat vary in pitch and volume. Pitch refers to the fundaries of tests were p erformed to determine the e�ectiveness mental frequency of a wave. Volume refers to the overall of the comparison algorithms and their capability for correct energy of a wave. In some cases, pitch and volume convey clustering. The test b ed devised uses a graphical technique imp ortant information that must b e incorp orated into the for examining the samples and the cluster constituent. A recognition pro cess. Recognizing a song, for example, revariant of the ROCK clustering algorithm[5] was chosen to quires attention to pitch and volume. However, for sounds cluster sound segments. like parts of sp eech, recognition requires a mechanism that analyzes sounds in terms of harmonic comp onents. The proAlthough further investigation using other clustering techcess of harmonic feature extraction involves several steps. niques is required, the ROCK algorithm has some essential First, convert the signal from the time domain to the frefeatures that make it an attractive technique for clusterquency domain using the Fast Fourier Transform (FFT) [2]. ing sound. ROCK do es not merely classify items based on This is a standard technique used in all sound recognition similarity alone. Rather, ROCK considers the numb er of algorithms. Second, extract a small sample of p oints that neighb ours that app ear to b e similar to an item a more imrepresent lo cal p eaks. This allows the selection of features p ortant clustering metric than the degree of item similarity. that are imp ortant to the recognition of a segment. Third, Initially all items under consideration by the algorithm are normalize the sample by cho osing the largest sample value treated as b elonging to separate clusters. Based on a simiand setting it to a value of 1 and scale the other sample larity \threshold" value, each \cluster" is assigned a list of values relative to the maximum. This step provides volume neighb our clusters that seem similar. The two clusters that indep endence for the sample. The resulting set of values repseem to share the most neighb ours are combined into a sinresents a harmonic feature set that can b e used to identify gle cluster. A rep eated evaluation of all clusters is made, the original sample indep endent of the volume or pitch. combining clusters that share the most neighb ours, until a desired numb er of clusters is achieved or until all discovered The kinds of clusters that are found in a signal will dep end clusters have no neighb ours. Classi�cation is made of new on the similarity technique used to compare segments. Simielements by counting the numb er of elements within a cluslarity clustering that is based on harmonics will cluster parts ter that are similar to the new element and cho osing the of sp eech in a way that do es not dep end on pitch. The reason cluster with the largest neighb our count scaled relative to for this is that the relative strength of the frequencies in a overall size of each cluster. 

32 

**3.2 The Threshold Phase Transition Problem** neighb or link b etween the sample and one of the cluster Unfortunately, the ROCK algorithm is very sensitive to the samples. Note that the implication here is that the \searchvalue of the threshold. Ab ove a particular value, clustering ing" is not done manually. In fact the \searching" is done is p o or and recognition is not very e�ective; most p oints automatically within the classi�cation lo op. are classi�ed as disconnected. Below a certain threshold, clustering is also p o or and recognition is not e�ective since **4. SIMILARITY METRICS FOR** most p oints are classi�ed as neighb ours. To alleviate these **CLUSTERING** problems, reduced sensitivity to thresholds is required b oth in clustering and in later classi�cation. **4.1 Sound Sample Comparison** Sound sample analysis b egins with the transformation of _3.2.1 Trimming_ a sound segment into the frequency domain using a Fourier To reduce the sensitivity of ROCK to the threshold value, Transform. The result of the transform is a series of complex \trimming" reduces the numb er of allowed neighb ours. This numb ers representing the frequency comp onents of the samallows for a varying value in the threshold while maintaining ple. Using an intensity function, each frequency comp onent a reasonable numb er of neighb ours to cluster. A neighb ourcan b e converted into a real numb er. This set of frequency ing pair of clusters is any two clusters that share suÆcient intensity values for a sound segment can b e analyzed, and neighb our links that allow the classi�cation of b oth clusters can b e transformed further into a set of characteristics repinto a single cluster. The neighb our vector for any cluster is resenting the sound. In order to use the ROCK algorithm, ordered according to link counts. The trimming algorithm a similarity metric was devised which distinguishes b etween works by eliminating neighb ours from the most linked clussound samples. The similarity metric used in ROCK cluster until pre-determined maximum numb er of neighb ours is tering must pro duce a value from 0 to 1: 0 indicating no achieved. It is imp ortant when doing this trimming that match, whereas 1 indicates an exact match. The euclidean neighb ours are trimmed in pairs. Without this recipro cal distance is often used as a similarity metric in clustering. trimming, the rest of the ROCK algorithm will get \out-ofHowever, another metric that pro duces similar results is a sync" and the algorithm p erformance will deteriorate. The calculation S that sums up relative ratios. In this case, given ROCK algorithm requires all neighb our activity to work in two signals comp osed of frequency vectors X and Y, S can pairs: one action for the link \to" no de and a corresp onding b e calculated as follows: action for the link \from" no de. Therefore, when trimming, for each neighb our that is eliminated from a cluster's neighneighb our blist,ourthelist recipromust alsocal enb etryeliminated.in the correspAn assumptiononding cluster'sthat S = Pi maxmin((xxii;y;yii)) (1) d was made in cho osing the trimming value was to assume that each cluster was relatively similar in size; no cluster was signi�cantly larger than all others. This implies that where d represents the dimensionality of the data. The value a go o d cluster trimming value is approximately the average d varies and is calculated using a counter. Pairs, which had cluster size. In our case we chose a trimming value calcuvalues b elow a certain threshold, were discarded from the lated using the sample size divided by the desired cluster calculation. This was necessary since large numb ers of low count. values do not contribute to the analysis. _3.2.2 Threshold Searching_ **4.2 Harmonic Filter Based Similarity Metric** Once the clustering algorithm has completed, the �nal phase To compare harmonics, a metric is desired that is indep enof op eration is the assignment of items to clusters. Certain dent from pitch or volume. To provide this comparison, a threshold values will cause many items to b e unclassi�able. harmonic comp onent vector is calculated which is comprised In some cases, this might b e acceptable, however, in cases of the harmonics of a sample. Natural sounds other than where a classi�cation is required, an alteration to the sugnoise consist of a numb er of harmonic frequencies ab ove a gested classi�cation technique is necessary. Consider, for base frequency. By comparing the intensities of the harmonexample, the sounds `aw', `oh', `ee', `ay' and `eh'. Supp ose ics, one sound can b e distinguished from another. Similar we are lo oking for �ve clusters. Below a certain similarity to the Frequency Based Metric, the Harmonic Based Metthreshold, ROCK would likely classify new sounds, which ric uses the same metric as S in (1) where d represents the were not in the original clustering, as b elonging to none of dimensionality of the data. The value d is calculated by these categories. Ab ove a certain threshold, new sounds that adding up all pairs of harmonics where b oth x and y are are similar will all b e placed in the �rst category. ab ove a given cuto�. Each x and y value represents a harmonic pair. The harmonics are ordered such that the �rst The solution is to search for a useful threshold during each harmonic of sound x is compared with the �rst harmonic of assignment. The threshold value must start low. Each clussound y , etc. Harmonics are found by scanning the FFT of ter is checked for neighb our counts using a low threshold. a sample and lo oking for p eaks. If an insuÆcient assignment is made, the threshold value is increased until a similarity count for one of the clusters is **4.3 Calculating Harmonics** ab ove a certain value. To employ threshold searching our To calculate the harmonic intensities the following algorithm mo di�cation to the ROCK classi�cation algorithm wraps was deployed using the FFT sample: the original ROCK classi�cation routine with a threshold searching lo op. Through each iteration, the threshold is multiplied by 0.9. Our algorithm searched for at least one 1. Lo ok for a value that is a maximum. 

33 



Figure 1: FFT of the recording used in a frequency clustering test. 2. For each successive value determine if the values are declining. 3. If values decline for two simultaneous measurements, record the last maximum and reset it to zero. **5. PRELIMINARY EXPERIMENTS** The test system was built using Microsoft Visual C++ 6.0 and Develop er Studio. The recording co de, Fourier transform co de and the co de that draws the frequency histograms was originally develop ed by a company called Relisoft Inc. based in Seattle. The co de was mo di�ed to add: the ROCK algorithm, buttons to control sampling and clustering, and extensions to the draw co de to allow for the drawing of cluster contents and frequency histograms with harmonic indicators. The following tests were p erformed using frequency clustering and harmonic clustering. The �rst test involved whistling three distinct notes and searching for frequency clusters. The second involved recording the long vowel sounds \A" \E" and \U" and p erforming harmonic clustering. In Figure 1 the FFT of the recording used in a frequency clustering test is displayed. The vertical axis indicates frequency. The horizontal axis is time. The tests p erformed called for 5 clusters from 50 samples. Using a theta value of 0.5, a cuto� of 0.4 and trimming each initial cluster to 10 neighb ours, the results obtained are displayed in Figure 2. Figure 3 displays the results of the segment assigment for the entire original frequency test sample using the classi�cation scheme derived from the frequency clustering results. In Figure 4 the FFT of the recording used in a harmonic comp onent clustering test is displayed. The tests p erformed also called for 5 clusters from 50 samples. Using a theta value of 0.25, a cuto� of 0.1 and without trimming, the results obtained are displayed in Figure 5. The divisions b e- tween phonemes can b e visually distinguished by the varia- 



Figure 2: Clusters of frequency-based segment samples from original audio source. 



34 





Figure 7: Example of histogram graph. Figure 4: FFT of the recording used in a harmonic clustering test. Figure 8: Histograms for the sounds \Aaa", \Oo o", \Eee". tion in harmonic comp onents. Figure 6 displays the results of the segment assignment for the entire original harmonic test sample using the classi�cation scheme derived from the harmonic clustering results. The test illustrated ab ove was clearly very successful in that the clustering technique was able to precisely delineate the 3 vowel sounds. Figure 7 is an example of the histogram graph. The white lines are used to indicate the lo cations of p eaks. These p eak values are used in the harmonic similarity equation. The graphics in Figure 8 show the frequency histograms for the phrases \Aaa", \Oo o" and \Eee". The white spikes indicate p eaks. The vertical axis indicates p ower. The horFigure 5: Clusters of harmonic-based segment samizontal axis is frequency. ples from original audio source. Although a large numb er of tests were done using sp eech, the results rep orted here represent a small sample of those tests. A later pap er will rep ort on these tests and other tests using various kinds of sounds. The similarity technique that we are currently exp erimenting with do es not deal very well with noise. Further work is required to allow noises to b e included in the similarity metrics. **6. CONCLUSIONS AND FUTURE WORK** The ROCK algorithm is a very pro cessing intensive technique for clustering. However, the algorithm is very intuitive and is general enough to apply to many di�erent kinds of clustering problems. One ma jor problem with ROCK is its sensitivity to the threshold value. The correct value to use is determined by the nature of the data and the nature of the similarity metric. To alleviate this problem we introduced the notion of \trimming" and the notion of threshold \searching". These techniques greatly reduced the sensitivity of the algorithm to the threshold value. Further research Figure 6: Harmonic-based cluster assignments. is required to determine if these techniques can b e applied to broader problem sets. We were also able to determine 

35 

- that sound clustering is a viable technique for unsup ervised classi�cation of sounds. Further work will fo cus on comparing ROCK to other clustering algorithms in the contexct of sound[14, 9, 3, 4, 7, 8, 11]. Other similarity metrics should b e investigated including neural nets, decision trees and other pattern recognition algorithms. Additional similarity metrics are required to classify noise and inter-segment transitions [1]. Finally, clustering techniques that combine segments into complex groupings are required to classify higher order sounds. This would require multiple clustering passes that cluster groups corresp onding to sound patterns such as rhythms, melo dies or sp eech. Further research will also investigate classi�cation techniques that will allow segments to b elong to multiple clusters. This can b e achieved by applying a \fuzzy" similarity threshold value during classi�cation in contrast to the current classi�cation technique which is binary. **7. REFERENCES** [1] A. Czyzewski. Mining knowledge in noisy audio data. In Proc. Second Int. Conf. on Know ledge Discovery and Data Mining (KDD96), pages 220{225, Portland, Oregon, August 1996. 

- [2] D. E. Dudgeon and R. M. Mersereau. Multidimentional Digital Signal Processing. Printice-Hall, 1984. 

- [3] M. Ester, H.-P. Kriegel, J. Sander, and X. Xu. A density-based algorithm for discovering clusters in large spatial databases. In Proc. 1996 Int. Conf. Know ledge Discovery and Data Mining (KDD'96), pages 226{231, Portland, Oregon, August 1996. 

- [4] V. Ganti, J. E. Gehrke, and R. Ramakrishnan. CACTUS - clustering categorical data using summaries. In Proc. 1999 Int. Conf. Know ledge Discovery and Data Mining (KDD'99), San Diego, CA, 1999. 

- [5] S. Guha, R. Rastogi, and K. Shim. ROCK: A robust clustering algorithm for categorical attributes. In Proc. 1999 Int. Conf. Data Engineering (ICDE'99), pages 512{521, Sydney, Australia, March 1999. 

- [6] D. Hindus, C. Schmandt, and C. Horner. Capturing, structuring and representing ubiquitous audio. ACM Transactions on Information Systems, 11(4):376{400, Oct. 1993. 

- [7] A. Hinneburg and D. A. Keim. An eÆcient approach to clustering in large multimedia databases with noise. In Proc. 1998 Int. Conf. Know ledge Discovery and Data Mining (KDD'98), pages 58{65, New York, NY, August 1998. 

- [8] Z. Huang. Extensions to the k-means algorithm for clustering large data sets with categorical values. Data Mining and Know ledge Discovery, 2:283{304, 1998. 

- [9] A. K. Jain, M. N. Murty, and P. J. Flynn. Data clustering: A survey. ACM Comput. Surv., 31:264{323, 1999. 

- [10] K. Melih and R. Gonzalez. Audio retrieval using p erceptually based structures. In Proc. IEEE Intl. Conf. on Multimedia Computing and Systems, pages 338{347, 1998. 

- [11] G. Sheikholeslami, S. Chatterjee, and A. Zhang. WaveCluster: A multi-resolution clustering approach for very large spatial databases. In Proc. 1998 Int. Conf. Very Large Data Bases (VLDB'98), pages 428{439, New York, NY, August 1998. 

- [12] E. Wold, T. Blum, D. Keislar, and J. Wheaton. Content-based classi�cation, search and retrieval of audio. In Proc. 1999 IEEE Multimedia Conf., pages 27{36, 1996. 

- [13] T. Zhang and C.-C. J. Kuo. Heuristic approach for generic audio data segmentation and annotation. In Proc. 1999 ACM-Multimedia Conf., pages 67{76, Orlando, FL, Octob er 1999. 

- [14] T. Zhang, R. Ramakrishnan, and M. Livny. BIRCH: an eÆcient data clustering metho d for very large databases. In Proc. 1996 ACM-SIGMOD Int. Conf. Management of Data (SIGMOD'96), pages 103{114, Montreal, Canada, June 1996. 

36 

### **Effective Retrieval of Audio Information from Annotated Text Using Ontologies**<sup>**1**</sup> 

**Latifur Khan and Dennis McLeod** 

Department of Computer Science and Integrated Media Systems Center 

University of Southern California Los Angeles, California 90089 

[latifurk, mcleod]@usc.edu 

###### **ABSTRACT** 

To improve the accuracy in terms of precision and recall of an audio information retrieval system we have created a domainspecific ontology (a collection of key concepts and their interrelationships), as well as a novel, pruning algorithm.  Taking into account the shortcomings of keyword-based techniques, we have opted to employ a concept-based technique utilizing this ontology.  The key problem in the retrieval of audio information is to achieve high precision and high recall.  Typically, in traditional approaches, high recall is achieved at the expense of low precision, and vice versa.  Through the use of a domain-specific ontology appropriate concepts can be identified during metadata generation (description of audio) or query generation, thus improving precision.  In case of the association of irrelevant concepts to queries or documents there is a loss of precision.  On the other hand, if relevant concepts are discarded, a loss of recall will ensue.  Therefore, in conjunction with the use of a domain specific ontology we have proposed a novel, automatic pruning algorithm which prunes as many irrelevant concepts as possible during any case of query generation.  By associating concepts in the ontology through techniques of correlation, this algorithm presents a method for the selection of concepts in the query generation.  To improve recall, controlled and correct query expansion mechanism is proposed. This guarantees that precision will not be lost.  Moreover, we present a way for the query generation in which domain-specific ontology can be used to generate information selection requests in terms of database queries in SQL.  In trial implementations we have demonstrated that our ontology-based model outperforms keyword-based technique (vector space model) in terms of precision and recall. 

###### **Keywords** 

Metadata, Ontology,  Audio, SQL, Precision, and Recall. 

###### **1 Introduction** 

The development of technology in the field of digital media generates huge amounts of non-textual information, such as audio, video, and images, as well as more familiar textual information. The potential for the exchange and retrieval of information is vast, and at times daunting.  In general, users can be easily 

overwhelmed by the amount of information available via electronic means.  The transfer of irrelevant information in the form of documents (e.g. text, audio, video) retrieved by an information retrieval system and which are of no use to the user wastes network bandwidth and frustrates users.  This condition is a result of inaccuracies in the representation of the documents in the database, as well as confusion and imprecision in user queries, since users are frequently unable to express their needs efficiently and accurately. These factors contribute to the loss of information and to the provision of irrelevant information.  Therefore, the key problem to be addressed in information selection is the development of a search mechanism which will guarantee the delivery of a minimum of irrelevant information (high precision), as well as insuring that relevant information is not overlooked (high recall). 

The traditional solution to the problem of recall and precision in information retrieval employs keyword-based search techniques.  Documents are only retrieved if they contain keywords specified by the user.  However, many documents contain the desired semantic information, even though they do not contain user specified keywords.  This limitation can be addressed through the use of query expansion mechanism.  Additional search terms are added to the original query based on the statistical co-occurrence of terms [20].  Recall will be expanded, but at the expense of deteriorating precision [17, 24]. In order to overcome the shortcomings of keyword-based technique in responding to information selection requests we have designed and implemented a concept-based model using ontologies [12]. This model, which employs a domain dependent ontology, is presented in this paper. An ontology is a collection of concepts and their interrelationships which can collectively provide an abstract view of an application domain [5, 8]. 

There are two distinct questions for ontology-based model: one is the extraction of the semantic concepts from the keywords and the other is the indexing. With regard to the first problem, the key issue is to identify appropriate concepts that describe and identify documents on the one hand, and on the other, the language employed in user requests.  In this it is important to make sure that irrelevant concepts will not be associated and matched, and that relevant concepts will not be discarded.  In other words, it is important to insure that high precision and high 

> 1 This research has been funded [or funded in part] by the Integrated Media Systems Center, a National Science Foundation Engineering Research Center, Cooperative Agreement No. EEC-9529152. 

> © The copyright of this paper belongs to the paper's authors. Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. 

> Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 

> (O.R. Zaïane, S.J. Simoff, eds.) 

37 

recall will be preserved during concept selection for documents or user requests. In this paper, we propose an automatic mechanism for the selection of these concepts from user requests by addressing the first problem.  This mechanism will prune irrelevant concepts while allowing relevant concepts to become associated with user requests.  Furthermore, a novel, scalable disambiguation algorithm for concept selection from documents using domain specific ontology is presented in [13]. 

With regard to the second problem, one can use vector space model of concepts or more precise structure by choosing ontology. We adopt the latter approach. This is because vector space model does not work well for short queries. Furthermore, one recent survey about web search engines suggests that average length of user request is 2.2 keywords [4]. For this, we have developed a concept-based model, which uses domain dependent ontologies for responding to information selection requests.  To improve retrieval, we also propose an automatic query expansion mechanism which deals with user requests expressed in natural language.  This automatic expansion mechanism generates database queries by allowing only appropriate and relevant expansion.  Intuitively, to improve recall during the phase of query expansion, only controlled and correct expansion is employed, guaranteeing that precision will not be degraded as a result of this process.  Furthermore, for the disambiguation of concepts only the most appropriate concepts are selected with reference to documents or to user requests by taking into account the encoded knowledge in the ontology. 

In order to demonstrate the effectiveness of our disambiguation model we have explored and provided a specific solution to the problem of retrieving audio information. The effective selection/retrieval of audio information entails several tasks, such as metadata generation (description of audio), and the consequent selection of audio information in response to a query. Relevant to our purpose, ontologies can be fruitfully employed to facilitate metadata generation.  For metadata generation, we need to do content extraction by relying on speech recognition technology which converts speech to text.  After generating transcripts we can deploy our ontology-based model to facilitate information selection requests. At present, an experimental prototype for the implementation of the model has been developed and implemented.  As of today, our working ontology has around 7,000 concepts for the sports news domain, with 2,481 audio clips/objects of metadata in the database.  For sample audio content we use CNN broadcast sports and Fox Sports audio, along with closed captions. To illustrate the power of ontology-based over keyword-based search techniques we have taken the most widely used vector space model as representative of keyword search.  For comparison metrics we have used measures of precision and recall, and an F score that is the harmonic mean of precision and recall.  Nine sample queries were run based on the categories of broader query (generic), narrow query (specific), and context query formulation.  We have observed that on average our ontology outperforms keyword-based technique.  For broader and context queries, the result is more pronounced than in cases of narrow query. 

The remainder of this paper is organized as follows. In Section 2, we review related work. In Section 3, we introduce the research context in terms of the information media used (i.e., audio) and some related issues that arise in this context.  In Section 4, we introduce our domain dependent ontology.  In Section 5, we present metadata management issues that arise for 

our ontology based model in the context of audio information unit.  In Section 6, we present a framework through which user requests expressed in natural language can be mapped into database queries in order to support index structure along with pruning algorithm.  In Section 7 we give a detailed description of the prototype of our system, and provide data showing how our ontology-based model compares with traditional keyword-based search technique.  Finally, in Section 8 we present our conclusions and plans for future work. 

###### **2 Related Works** 

Historically ontologies have been employed to achieve better precision and recall in the text retrieval system [9].  Here, attempts have taken two directions, query expansion through the use of semantically related-terms, and the use of conceptual distance measures, as in our model.  Among attempts using semantically related terms, query expansion with a generic ontology, WordNet [15], has been shown to be potentially relevant to enhanced recall, as it permits matching a query to relevant documents that do not contain any of the original query terms.  Voorhees [22] manually expands 50 queries over a TREC1 collection using WordNet, and observes that expansion was useful for short, incomplete queries, but not promising for complete topic statements.  Further, for short queries, automatic expansion is not trivial; it may degrade rather than enhance retrieval performance.  This is because WordNet is too incomplete to model a domain sufficiently.  Furthermore, for short queries less context is available, which makes the query vague. Therefore, it is hard to choose appropriate concepts automatically. The notion of conceptual distance between query and document provides an alternative approach to modeling relevance.  Smeaton et al. [20] and Gonzalo et al. [7] focus on managing short and long documents, respectively.  Note here that in these approaches queries and document terms are manually disambiguated using WordNet.  In our case, query expansion and the selection of concepts, along with the use of the pruning algorithm, is fully automatic. 

Although we use audio, here we show related work in the video domain which is closest to and which complements our approach in the context of data modeling for the facilitation of information selection requests. Key related work in the video domain for selection of video segments includes [1, 11, 16].  Of these, Omoto et al. [16] use a knowledge hierarchy to facilitate annotation, while others use simple keyword based techniques without a hierarchy.  The model of Omoto et al. fails to provide a mechanism that automatically converts a generalized description into a specialized one(s).  Further, this annotation is manual and does not deal with the disambiguation issues related to concepts. 

###### **3 Research Context: Audio** 

Audio is one of the most powerful and expressive of the nontextual media.  Audio is a streaming medium (temporally extended), and its properties make it a popular medium for capturing and presenting information.  At the same time, these very properties, along with audio’s opaque relationship to computers, present several technical challenges from the perspective of data management [6].  The type of audio considered here is broadcast audio.  In general, within a broadcast audio stream, some items are of interest to the user and some are not.  Therefore, we need to identify the boundaries of news items of interest so that these segments can be directly and efficiently 

38 

retrieved in response to a user query.  After segmentation, in order to retrieve a set of segments that match with a user request, we need to specify the content of segments. This can be achieved using content extraction through speech recognition. Therefore, we present segmentation and content extraction technique one by one. 

###### **3.1 Segmentation of Audio** 

Since audio is by nature totally serial, random access to audio information may be of limited use.  To facilitate access to useful segments of audio information within an audio recording deemed relevant by a user, we need to identify entry points/jump locations.  Further, multiple contiguous segments may form a relevant and useful news item. 

As a starting point both a change of speaker and long pauses can serve to identify entry points [2].  For long pause detection, we use short-time energy ( _En_ ), which provides a measurement for distinguishing speech from silence for a frame (consisting of a fixed number of samples) which can be calculated by the following equation [18]: 



Where _x(m)_ is discrete audio signals, _n_ is the index of the shorttime energy, and _w(m)_ is a rectangle window of length _N_ . When the _En_ falls below a certain threshold we treat this frame as pause. After such a pause has been detected we can combine several adjacent pauses and identify what can be called a _long pause_ . Therefore, the presence of speeches with starting and ending points defined in terms of long pauses allows us to detect the boundaries of audio segments. 

###### **3.2 Content Extraction** 

To specify the content of media objects two main approaches have been employed to this end: fully automated content extraction [10], and selected content extraction [23]. In fully automated content extraction, speech is converted to equivalent text (e.g., Informedia). Word-spotting techniques can provide selected content extraction in a manner that will make the content extraction process automatic.  Word-spotting is a particular application of automatic speech recognition techniques in which the vocabulary of interest is relatively small.  In our case, vocabularies of concepts from the ontology can be used. Furthermore, content description can be provided in plain text, such as closed captions. However, this manual annotation is labor intensive. For content extraction we rely on closed captions that came with audio object itself from fox sports and CNN web site in our case (see Section 7). 

###### **3.3 Definition of an Audio Object** 

An audio object, by definition and in practice, is composed of a sequence of contiguous segments.  Thus, in our model the start time of the first segment and the end time of the last segment of these contiguous segments are used respectively to denote start time and end time of the audio object.  Further, in our model, pauses between interior segments are kept intact in order to insure that speech will be intelligible.  The formal definition of an audio object indicates that an audio object’s description is provided by a set of self-explanatory tags or labels using ontologies.  An audioobject _Oi_ is defined by five tuple ( _idi, Si, Ei, Vi, Ai_ ) where _Idi_ is an object identifier which is unique **,** _Si_ is the start time, _Ei_ is the end time, _Vi_ (description) is a finite set of tag or label, i.e., _Vi={v1i , v2i , ... ,vji, ...,vni}_ for a particular _j_ where vji  is a tag or label name, 

and Ai is simply audio recording for that time period. For example, an audio object is defined as {10, 1145.59, 1356.00, {Gretzky Wayne}, *}. Of the information in the five tuple, the first four items (identifier, start time, end time, and description) are called _metadata_ . 

###### **4 Ontologies** 

An ontology is a specification of an abstract, simplified view of the world that we wish to represent for some purpose [5, 8]. Therefore, an ontology defines a set of representational terms that we call _concepts._ Interrelationships among these concepts describe a target world. An ontology can be constructed in two ways, domain dependent and generic.  CYC [14], WordNet [15], or Sensus [21] are examples of generic ontologies. For our purposes, we choose a domain dependent ontology. First, this is because a domain dependent ontology provides concepts in a fine grain, while generic ontologies provide concepts in coarser grain. Second, a generic ontology provides a large number of concepts that may contribute large speech recognition error. 



**Figure 1. A Small Portion of an Ontology for Sports Domain** Figure 1 shows an example ontology for sports news. This ontology is usually obtained from generic sports terminology and domain experts. This ontology is described by a directed acyclic graph (DAG). Here, each node in the DAG represents a concept. In general, each concept in the ontology contains a label name and a synonyms list. Note also that this label name is unique in the ontology. Further, this label name is used to serve as association of concepts with audio objects. The synonyms list of a concept contains vocabulary (a set of keywords) through which the concept can be matched with user requests. Formally, each concept has a synonyms list _(l1, l2, l3, ..., li ,...,ln )_ where user requests are matched with this _li_ what we call _element_ of list. Note that a keyword may be shared by multiple concepts’ synonyms lists. For example, player “Bryant Kobe,” “Bryant Mark,” “Reeves Bryant” share common word “Bryant” which may create ambiguity problem. 

39 

###### **4.1 Interrelationships** 

In the ontology, concepts are interconnected by means of interrelationships. If there is a interrelationship R, between concepts Ci and Cj, then there is also a interrelationship R ′ between concepts Cj and Ci. In Figure 1, interrelationships are represented by labeled arcs/links. Three kinds of interrelationships are used to create our ontology:  IS-A, Instance-Of, and Part-Of. These correspond to key abstraction primitives in object-based and semantic data models [3]. 

**IS-A:** This interrelationship is used to represent concept inclusion. A concept represented by Cj is said to be a specialization of the concept represented by Ci if Cj is kind of Ci . For example, “NFL” is a kind of “Professional” league. In other words, “Professional” league is the generalization of “NFL.” In Figure 1, the IS-A interrelationship between _Ci_ and _Cj_ goes from generic concept _Ci_ to specific concept, _Cj_ represented by a broken line. The IS-A interrelationship can be further categorized into two types: _exhaustive group_ and _non-exhaustive group_ . An exhaustive group consists of a number of IS-A interrelationships between a generalized concept and a set of specialized concepts, and places the generalized concept into a categorical relation with a set of specialized concepts in such a way so that the union of these specialized concepts is equal to the generalized concept. For example, “Professional” relates to a set of concepts, “NBA”, “ABL”, “CBA”, ..., by exhaustive group (denoted by caps in Figure 1). Further, when a generalized concept is associated with a set of specific concepts by only IS-A interrelationships that fall into the exhaustive group, then this generalized concept will not participate in the metadata generation and SQL query generation explicitly. This is because this generalized concept is entirely partitioned into its specialized concepts through an exhaustive group. We call this generalized concept a _non participant concept (NPC)_ . For example, in Figure 1 “Professional” concept is NPC. On the other hand, a non-exhaustive group consisting of a set of IS-A does not exhaustively categorize a generalized concept into a set of specialized concepts. In other words, the union of specialized concepts is not equal to the generalized concept. 

**Instance-Of:** This is used to show membership. A _Cj_ is a member of concept _Ci_ . Then the interrelationship between them corresponds to an Instance-Of denoted by a dotted line. Player, ”Wayne Gretzky” is an instance of a concept, “Player.” In general, all players and teams are instances of the concepts, “Player” and “Team” respectively. 

**Part-Of:** A concept is represented by _Cj_ is Part-Of a concept represented by _Ci_ if _Ci_ has a _Cj_ ( as a part) or _Cj_ is a part of _Ci._ For example, the concept “NFL” is Part-Of “Football” concept and player, “Wayne Gretzky” is Part-Of “NY Rangers” concept. 

###### **4.2 Disjunctness** 

When a number of concepts are associated with a parent concept through IS-A interrelationship, it is important to note that these concepts are disjoint, and are referred to as concepts of a disjoint type. When, for example, the concepts “NBA”, “CBA”, or  “NFL” are associated with the parent concept “Professional,” through IS-A, they become disjoint concepts. Moreover, any given object’s metadata cannot possess more than one such concept of the disjoint type. For example, when an object’s metadata is the concept “NBA,” it cannot be associated with another disjoint concept, such as “NFL.”  It is of note that the property of being disjoint helps to disambiguate concepts for keywords during metadata or query generation phases.  Similarly, concept “College Football”, “College Basketball” are disjoint concepts due to their associations with parent concept, “College League” 

through IS-A. Furthermore, “Professional,” and “Non Professional” are disjoint. Thus, we can say that “NBA,” “CBA,” “ABL,” “College Basketball,” and “College Football,” are disjoint. Each of these league and its team and player form a boundary what we call _region_ (see Figure 2). During annotation of concepts with an audio object we strive to choose a particular region. This is because an audio object can be associated with only one disjoint-type concept. However, it may be possible that a particular player may play in several leagues. In that case, we make multiple instances of the player. In other words, for each league he plays, we maintain a separate concept for him. This way we preserve disjoint-property. 

Concepts are not disjoint, on the other hand, when they are associated with a parent concept through Instance-Of or Part-Of. In this case, some of these concepts may serve simultaneously as metadata for an audio object. An example would be the case in which the metadata of an audio object are team “NY Ranger” and player “Gretzky Wayne,” where “Grezky Wayne” is Part-Of “NY Rangers.” 



**Figure 2. Different Regions of  an Ontology** 

###### **5 Metadata Acquisition and Management of Metadata** 

Metadata acquisition is the name for the process through which descriptions are provided for audio objects. For each audio object we need to find the most appropriate concept(s).  Recall that using content extraction (see Section 3.2) we get a set of keywords which appear in a given audio object.  For this, concepts from ontologies will be selected based on matching terms taken from their lists of synonyms with those based on specified keywords. Furthermore, each of these selected concepts will have a score based on a partial or a full match.  It is possible that a particular keyword may be associated with more than one concept in the ontology.  In other words, association between keyword and concept is one:many, rather than one:one.  Therefore, the disambiguation of concepts is required.  The basic notion of disambiguation is that a set of keywords occurring together determine a context for one another, according to which the appropriate senses of the word (its appropriate concept) can be determined.  Note, for example, that base, bat, glove may have several interpretations as individual terms, but when taken together, the intent is obviously a reference to baseball.  The reference follows from the ability to determine a context for all the terms.  Thus, extending and formalizing the idea of context in order to achieve the disambiguation of concepts, we propose an 

40 

efficient pruning algorithm based on two principles: cooccurrence and semantic closeness.  This disambiguation algorithm first strives to disambiguate across several regions using first principle, and then disambiguates within a particular region using the second (see [13] for more details). 

Effective management of metadata facilitates efficient storing and retrieval of audio information.  To this end, in our model most specific concepts are considered as metadata. Several concepts of the ontology, for example, can become the candidate for the metadata of an audio object.  However, some of these may be children of others.  Two alternative approaches can be used to address this problem. First, we can simply store the most general concepts. But we may get many irrelevant objects (precision will be hurt) for queries related to specific concepts.  For example, an audio object becomes the candidate for the concepts, “NHL,” “Hockey,” and “Professional.” We can simply store the general concept, “Professional” for this object. When user request comes in terms of specific concept, “NHL”, this object will be retrieved along with other irrelevant objects that do not belong to NHL ( say, NFL, CFL, and so on). Therefore, precision will be hurt. Second, the most specific concepts can be stored in the database. Corresponding generalized concepts can then be discarded.  In this case, recall will be hurt. Suppose, for example, an audio object becomes the candidate for the concepts "NHL", "Hockey", and "Professional."  During the annotation process the object will only be annotated with the most specific concept, "NHL."  In this case, the metadata of the audio objects stored in the database will be comprised of the most specific concepts. If query comes in terms of “Hockey” or “Professional”, this object will not be retrieved. 

We follow the latter approach. By storing specific concepts as metadata, rather than generalized concepts of the ontology, we can expect to achieve the effective management of metadata.  In order to avoid recall problem, user requests are first passed through ontology on the fly and expressed in terms of most specific concepts. Even so, the audio object, in the above example, can still be retrieved through querying the system by "NHL", "Hockey", and "Professional." 

Here, we consider an efficient way of storing audio objects in the database: we maintain a single copy of all the audio data in the database. Further, each object’s metadata are stored in the database. Thus, this start time, and end time of an object point to a fraction of all the audio data. Therefore, when the object is selected, this boundary information provides relevant audio data that are to be fetched from all the audio data and played by the scheduler. The following self-explanatory schemas are used to store audio objects in the database: _Audio_News (Id, Time_Start, Time_End, ...), and Meta_News_ _<u>(Id, Label)</u>_ . Each audio object’s start time, end time and description correspond to Time_Start, Time_End, and Label respectively. Furthermore, each object’s description is stored as a set of rows or tuples in the Meta_News table for normalization purpose. 

###### **6 Query Mechanisms** 

We now focus specifically on our techniques for utilizing an ontology-based model for processing information selection requests.  In our model the structure of ontology facilitates indexing.  In other words, ontology provides index terms/concepts which can be used to match with user requests.  Furthermore, the generation of a database query takes place after the keywords in the user request are matched to concepts in the ontology. 

We assume that user requests are expressed in plain English. Tokens are generated from the text of the user's request after stemming and removing stop words. Using a list of synonyms these tokens are associated with concepts in the ontology through Depth First Search (DFS) or Breadth First Search (BFS).  Each of these selected concepts is called a _QConcept_ .  Among QConcepts, some might be ambiguous. However, through the application of a pruning technique that will be discussed in Section 6.1 only relevant concepts are retained. These relevant concepts will then be expanded, and will participate in SQL query generation as is discussed in Section 6.2. 

###### **6.1 Pruning** 

Disambiguation is needed when a given keyword matches more than one concept.  In other words, multiple ambiguous concepts will have been selected for a particular keyword.  For disambiguation, it is necessary to determine the correlation between selected concepts based on semantic closeness.  When concepts are correlated, the scores of concepts strongly associated with each other will be given greater weight based on their minimal distance from each other in the ontology and their own matching scores based on the number of words they match.  Thus, ambiguous concepts which correlate with other selected concepts will have a higher score, and a greater probability of being retained than ambiguous concepts which are not correlated. 

For example, if a query is specified by "Please tell me about team Lakers," QConcepts "Team," "Los Angeles Lakers," and major league baseball player, "Tim Laker" (of team "Pittsburgh Pirates") are selected.  Note that selected concepts, "Los Angeles Lakers," and "Tim Laker" are ambiguous.  However, "Los Angeles Lakers" is associated with selected QConcept, "Team" due to Instance-Of interrelationship.  Therefore, we prune the non-correlated ambiguous concept, player "Tim Laker."  The above idea is implemented using score-based techniques.  Now, we would like to present our concept-pruning algorithm for use with user requests. 

###### **6.1.1 Formal Definitions** 

Each selected concept contains a score based on the number of keywords from the list of synonyms which have been matched with the user request.  Recall that in an ontology each concept (Q _Ci_ )  has a complementary list of synonyms ( _l1, l2,  l3, ..., lj ,...,ln_ ). Keywords in the user request are sought which match each keyword on the element _lj_ of a concept.  The calculation of the score for _lj_ , which we designate an _Escore_ , is based on the number of matched keywords of _lj_ .  The largest of these scores is chosen as the score for this concept, and is designated _Score_ . Furthermore, when two concepts are correlated, their scores, called the _Propagated-score_ , are inversely related to their position (semantic distance) in the ontology.  Let us formally define each of these scores. 

**_Definition 1: Element-score (Escore):_** The Element-score of an element _lj_ for a particular QConcept _QCi_ is the number of keywords of _lj_ matched with keywords in the user request divided by total number of keywords in _lj_ . _#of keywords of lj matched Escoreij_ ≡ _#of keywords inlj_ 

The denominator is used to nullify the effect of the length of _lj_ on _Escoreij_ and ensures that the final weight is between 0 and 1. **_Definition 2: Concept-score (Score):_** The Concept-score for a QConcept, Q _Ci_ is the largest score of all its element-scores.  Thus, 

_Score i_ = _max Escore ij  where 1_ ≤ _j_ ≤ _n_ 

41 

**_Definition.3: Semantic distance (SD (QCi , QCj )):_** _SD(QCi, QCj )_ between QConcepts _QCi_ and _QCj_ is defined as the shortest path between two QConcepts, _QCi_ and _QCj_ in the ontology. Note that if concepts are in the same level and no path exists, the semantic distance is infinite. For example, the semantic distance between concepts “NBA” and team “Lakers” is 1 (see Figure 2). This is because the two concepts are directly connected via a Part-Of interrelationship. Similarly, the semantic distance between “NBA,” and “Bryant Kobe” is 2. The semantic distance between “Los Angeles Lakers,” and “New Jersey Nets” is infinite. 

**_Definition.4: Propagated-score (Si):_** If a QConcept, Q _Ci_ , is correlated with a set of QConcepts _(Cj, Cj+1,...,Cn)_ , the propagated-score of _QCi_ is its own Score, _Scorei_ plus the scores of each of the correlated QConcepts' _(QCk k=j, j+1, ..., n) Scorek_ divided by _SD (QCi, QCk)._ Thus, 

_k_ = _n Scorek Si_ = _Scorei_ + ∑ _k_ = _j SD(QCi,QCk) Scorej Scorej_ + _1 Scoren_ = _Scorei_ + + + _..._ + _SD(QCi,QCj) SD(QCi,QCj_ + _1) SD(QCi,QCn)_ For example, in Figure 2 let us assume that values of _Scorei_ for "Los Angeles Lakers" and "Bryant Kobe" be 0.5 and 1.0 respectively.  Furthermore, these concepts are correlated with a semantic distance of 1, and their Propagated-scores are 1.5 (0.5 + 1.0/1) and 1.5 (1.0+0.5/1) respectively. The pseudo code for the pruning algorithm is as follows: 

_QC1, QC2 , …, QCl, …, QCr_ are selected with concept-score 

_Score1,…,Scorel,,…Scorer_ 

Determine correlation of selected concepts _(QCi, QCj, QCj+1, .., QCn)_ and update their Propagated-scores using 



Sort all QConcepts ( _QCi_ ) based on _Si_ in descending order //Find Ambiguous QConcepts and prune some of them 

//which have low Propagated-score… 

For a keyword that associated with ambiguous QConcepts, 

_QCi, QCj, QCl_ , …  where _Si > Sj >Sl, ..._ 

Keep only _QCi_ and discard _QCj, QCl,_ … 

//End of For Loop for a keyword. 

Keep all specific QConcepts and discard corresponding generalized concepts 

For each QConcept that are not pruned 

Query_Expansion_SQL_Generation (QConcept) //see Figure 4 

//End of For loop each QConcept 

###### **Figure 3. Pseudo Code for Pruning Algorithm** 

Using pruning algorithm (see Figure 3), for a user request, “team Lakers,” at the beginning selected QConcepts are “Team”, “Los Angeles Lakers” and “Tim Laker” (see Figure 2). Note that ambiguous concepts are “Los Angeles Lakers,” and “Tim Laker.” In Figure 2  the SD between concepts, "Team," and "Los Angeles Lakers" is 1 while the SD between concepts, "Team" and "Tim Laker" is 2.  Furthermore, the Scores for concepts, "Team," "Los Angeles Lakers," and "Tim Laker" are 1.0, 0.5, 0.5 respectively. It is important to note that when two concepts are correlated with 

each other where semantic distance is greater than one, they will have a lower Propagated-scores, _Si_ and _Sj_ compared to concepts with the same concept-scores and a semantic distance of 1.  This is because for the higher semantic distance concepts are correlated in a broader sense. Thus, concepts which are correlated have a higher _Si_ in comparison with non-correlated concepts.  Now, the Propagated-score for QConcepts, “Team,” “Los Angeles Lakers,” and “Tim Laker” becomes 1.75 (1.0+0.5/1+0.5/2), 1.5 (0.5+1.0/1), and 1.0 (0.5+1.0/2) respectively.  Therefore, we keep the concept "Los Angeles Lakers" from among these ambiguous concepts and prune the other.  Thus, the SD helps us to discriminate between ambiguous concepts. 

Among selected concepts, one concept may subsume the other concept. In this case, we use specific concept for SQL generation. For example, if a user request is expressed in terms of "Please tell me about Lakers' Bryant," the QConcepts, team "Los Angeles Lakers," players, "Bryant Kobe", "Bryant Mark," "Reeves Bryant," are selected.  Their concept-scores are 0.5, 0.5, 0.5 respectively.  The latter three are ambiguous concepts.  However, among these selected concepts, only "Bryant Kobe," and "Los Angeles Lakers" are correlated with a semantic distance of 1 (see Figure 2).  Therefore, their propagated-scores Si are high as compared to other concepts, in this case, 1.0, 1.0, 0.5, 0.5 respectively.  Consequently, we throw away "Bryant Reeves" and "Bryant Mark."  Furthermore, "Bryant Kobe" is a sub-concept of "Los Angels Lakers," due to a Part-Of interrelationship.  In this case, we keep the more specific concept, "Bryant Kobe," and the SQL generation algorithm will be called for this QConcept only. 

**6.2 Query Expansion and SQL Query Generation** We now discuss a technique for query expansion and SQL query generation.  In response to a user request for the generation of an SQL query, we follow a Boolean retrieval model.  We now consider how each QConcept is mapped into the "where" clause of an SQL query.  Note that by setting the QConcept as a Boolean condition in the "where" clause, we are able to retrieve relevant audio objects.  First, we check whether or not the QConcept is of the NPC type.  Recall that NPC concepts can be expressed exhaustively as a collection of more specific concepts.  If the QConcept is a NPC concept, it will not be added in the "where" clause.  On the other hand, it will be added into the “where” clause. Likewise, if the concept is leaf node, no further progress will be made for this concept.  However it is non-leaf node, its children concepts are generated using DFS/BFS, and this technique is applied for each children concept.  One important observation is that all concepts appearing in an SQL query for a particular QConcept are expressed in disjunctive form. Furthermore, during the query expansion phase only correct concepts are added which will guarantee that addition of new terms will not hurt precision.  The complete algorithm is shown in Figure 4. 

_Query_Expansion_SQL_Generation (QCi)_ 





Add label of _QCi_ into where clause of SQL as disjunctive form 

//Regardless of NPC type concept 

If _QCi_ is not leaf node and not visited yet 

For each children concept, QChl of  QCi using DFS/BFS Query_Expansion_SQL_Genertaion (QChl ) 

**Figure 4. Pseudo Code for SQL Generation** 

42 

The following example illustrates the above process. Suppose the user request is "Please give me news about player Kobe Bryant."  "Bryant Kobe" turns out to be the QConcept which is itself a leaf concept.  Hence, the SQL query (for schema see Section 5) generated by using only "Bryant Kobe" (with the label "NBAPlayer9") is: 

**SELECT** Time_Start, Time_End 

**FROM** Audio_News a, Meta_News m 

**WHERE** a.Id=m.Id 

**AND** Label="NBAPlayer9" 

Let us now consider the user request, "Tell me about Los Angeles Lakers."  Note that the concept "Los Angeles Lakers" is not of the NPC type, so its label ("NBATeam11") will be added in the "where" clause of the SQL query.  Further, this concept has several children concepts ("Bryant Kobe," "Celestand John," "Horry Robert," .... i.e. names of players for this team).  Note that these player concepts’ labels are "NBAPlayer9," "NBAPlayer10," and "NBAPlayer11," respectively.  In SQL query: 

**SELECT** Time_Start, Time_End 

**FROM** Audio_News a, Meta_news m 

**WHERE** a.Id = m.Id **AND** (Label="NBATeam11” 

**OR** Label="NBAPlayer9" **OR** Label **=** "NBAPlayer10"...) 

###### **6.2.1 Remedy of Explosion of Boolean Condition** 

Since most specific concepts are used as metadata and our ontologies are large in the case of querying upper level concepts, every relevant child concept will be mapped into the "where" clause of the SQL query and expressed as a disjunctive form.  To avoid the explosion of Boolean conditions in this clause of the SQL query, the labels for the player and team concepts are chosen in an intelligent way. These labels begin with the label of the league in which the concepts belong.  For example, team "Los Angeles Lakers" and player "Bryant, Kobe" are under "NBA." Thus, the labels for these two concepts are "NBATeam11" and "NBAPlayer9" respectively, whereas the label for the concept "NBA" is "NBA." 

Now, when user requests come in terms of an upper level concept (e.g., "Please tell me about NBA.") the SQL query generation mechanism will take advantage of prefixing: 

**SELECT** Time_Start, Time_End 

**FROM** Audio_News  a, Meta_News m **WHERE** a.Id=m.Id 

**AND** Label Like “%NBA%” 

On the other hand, if we do not take advantage of prefixing, the concept NBA will be expanded into all its teams (28), and let us assume each team has 14 players.  Therefore, we need to maintain 421 (1+ 28 + 28 *14) Boolean conditions in the where clause of SQL query.  This explosion will be exemplified by upper level concept like basketball. 

###### **7 Experimental Implementation** 

In discussing implementation we will first, present our experimental setup, and then we will demonstrate power of our ontology-based over keyword-based search techniques. We have constructed an experimental prototype system which is based upon a client server architecture.  The server (a SUN Sparc Ultra 2 model with 188 MBytes of main memory) has an Informix Universal Server (IUS), which is an object relational database system.  For the sample audio content we use CNN broadcast sports audio and Fox Sports.  We have written a hunter program 

in Java that goes to these web sites and downloads all audio and video clips with closed captions.  The average size of the closed captions for each clip is 25 words, after removing stop words. These associated closed captions are used to hook with the ontology.  As of today, our database has 2,481 audio clips.  The usual duration of a clip is not more than 5 minutes in length.  Wav and ram are used for media format. Currently, our working ontology has around 7,000 concepts for the sports domain.  For fast retrieval, we load the upper level concepts of the ontology in main memory, while leaf concepts are retrieved on a demand basis.  Hashing is also used to increase the speed of retrieval. **7.1 Results** 

We would like to demonstrate the power of our ontology over the keyword-based search technique.  For an example of keywordbased technique we have used the most widely used model-vector space model [19]. 

###### **7.1.1 Vector Space Model** 

Here, queries and documents are represented by vectors. Each vector contains a set of terms or words and their weights.  The similarity between a query and a document is calculated based on the inner product or cosine of two vectors' weights.  The weight of each term is then calculated based on the product of termfrequency ( _TF_ ) and inverse-document frequency ( _IDF_ ). _TF_ is calculated based on number of times a term occurs in a given document or query. _IDF_ is the measurement of inter-document frequency.  Terms that appear unique to a document will have high _IDF_ .  Thus, for _N_ documents if a term appears in n documents, _IDF_ for this term = _log(N/n) +1_ .  Let us assume query ( _Qi_ ) and document ( _Dj_ ) have _t_ terms and their associated weights are _WQik_ and _WDik_ respectively for _k_ = 1 to _t_ .  Similarity between these two is measured using the following inner product: 



The denominator is used to nullify the effect of the length of document and query and ensure that the final value is between 0 and 1. 

###### **7.1.2 Types of Queries** 

Sample queries are classified into 3 categories, with each category containing 3 queries.  The first category is related to broad/general query formulation such as "tell me about basketball" which is associated with an upper level concept of the ontology.  The second category is related to narrow query formulation such as "tell me about Los Angeles Lakers," which is associated with a lower level concept of the ontology.  The third category is context query, in which a user specifies a certain context in order to make the query unambiguous, such as Laker's Kobe, Boxer Mike Tyson, and Team Lakers. The comparison metrics used for these two search techniques are precision, recall, and F score.  We discuss precision, recall, and F score for individual queries. 

###### **7.1.3 Empirical Results** 

In Figures 5, 6, and 7, the X axis represents sample queries.  The first three queries are related to broad query formulation, the next three to narrow query formulation, and the last three queries to context queries.  In Figures 5, 6, and 7 for each query the first and second bars represent the recall/precision/F score for ontologybased and keyword-based search techniques respectively. 

43 

Although, the vector space model is ranked-based and our ontology-based model is a Boolean retrieval model, in the former case we report precision for maximum recall in order to make a fair comparison. 



<!-- Start of picture text -->
100<br>90<br>80<br>70<br>60<br>Recall 50<br>Ontology<br>40<br>Keyword<br>30<br>20<br>10<br>0<br>1 2 3 4 5 6 7 8 9<br>Sample Queries<br><!-- End of picture text -->

**Figure 5. Recall of Ontology-based and Keyword-based Search Techniques** 

In Figure 5, the data demonstrates that recall for our ontology-based model outperforms recall for keyword-based technique.  Note that this pattern is pronounced related to broader query cases.  For example, in query 1, 90% verses 11% recall is achieved for ontology-based as opposed to keyword-based technique whereas for query 4, 90% and 76% recall are obtained. This is because in the case of a broader query, more children concepts are added, as compared to narrow query formulation or a context query case.  Furthermore, in a context query case, it is usual for broader query terms to give context only.  In an ontology-based model these terms will not participate in the query expansion mechanism.  Instead, broader query terms will be subsumed under specific concepts.  For example, in query 7, the user requests "tell me about team Lakers."  Concepts referring to "team" will not be expanded.  Therefore, the gap between the two techniques is not pronounced. 



<!-- Start of picture text -->
100<br>90<br>80<br>70<br>60<br>Precision 50<br>Ontology<br>40<br>30 Keyword<br>20<br>10<br>0<br>1 2 3 4 5 6 7 8 9<br>Sample Queries<br><!-- End of picture text -->

**Figure 6. Precision of Ontology-based and Keyword-based Search Techniques** 

In Figure 6, for broader query cases, usually the precision of the ontology-based model outperforms the precision of the keyword-based technique.  This is because our disambiguation algorithm disambiguates upper level concepts with greater accuracy compared to lower level concepts.  For example, the disambiguation algorithm for metadata acquisition chooses the most appropriate region for each audio object.  Recall that a region is formed by a league, its team, and its players. Thus if a query is requested in terms of a particular league, that is related to 

upper concept in this region, precision will not be hurt.  However, the algorithm might fail to disambiguate lower level concepts in that region (e.g. players).  For a narrow query formulation case, the precision obtained in the ontology-based model may not be greater than that obtained through use of the keyword-based technique.  In query 4, the user requests "tell me about Los Angeles Lakers."  In the ontology-based model the query is expanded to include all this team’s players.  It might be possible during disambiguation in metadata acquisition for some of these players to be associated with audio objects as irrelevant concepts; in particular when disambiguation fails.  Some relevant concepts, such as other players, are also associated with these audio objects. Thus, for our ontology-based model these objects will be retrieved as a result of query expansion, leading to a deterioration in precision.  In a keyword-based case, we have not expanded "Lakers" in terms of all of the players on the Lakers team. Therefore, we just look for the keyword "Lakers" and the abovementioned irrelevant objects associated with its group of players will not be retrieved.  Thus, in this instance we observed 76% and 90% precision for ontology-based and keyword-based technique respectively. 

In the case of the context query, it is evident that the precision of the ontology-based model is much greater than that of the keyword-based model.  Since in the ontology-based model some concepts subsume other concepts, audio objects will only be retrieved for specific concepts.  On the other hand a search using keyword-based technique looks for all keywords.  If the user requests "team Lakers" the keyword-based technique retrieves objects with the highest rank when the keywords "team" and "Lakers" are present.  Furthermore, in order to facilitate maximum recall, we have observed that relevant objects will be displaced along with irrelevant objects in this rank.  Note that some irrelevant objects will also be retrieved that only contain the keyword "team."  Thus, for query 7, levels of precision of 76% and 29% have been achieved. 



<!-- Start of picture text -->
100<br>90<br>80<br>70<br>60<br>F score 50<br>Ontology<br>40<br>30 Keyword<br>20<br>10<br>0<br>1 2 3 4 5 6 7 8 9<br>Sample Queries<br><!-- End of picture text -->

**Figure 7. F score of Ontology-based and Keyword-based Search Techniques** 

Finally, the F score of our ontology-based model outperforms (or at least equals) that of a keyword-based technique (see Figure 7).  For the broader and context query case, precision and recall are usually high for the ontology-based model in comparison with keyword-based technique.  Therefore, F scores differences, for the ontology-based model are also pronounced. For example, for query 1, the F scores for ontology-based and keyword-based technique are 94% and 20% respectively.  For the narrow query case, the F score of our ontology-based model is slightly better or equal to that of the keyword-based technique. 

44 

For example, in query 4, we observed a similar F score (83%) in both cases; however in queries 5 and 6 we observed that the F score of the ontology-based model (91%, 87%) outperformed the keyword-based technique, (71%, 79%). 

###### **8 Conclusions** 

In this paper we have proposed a potentially powerful and novel approach for the retrieval of audio information. The crux of our innovation is the development of an ontology-based model for the generation of metadata for audio, and the selection of audio information in a user customized manner.  We have shown how the ontology we propose can be used to generate information selection requests in database queries.  We have used a domain of sports news information for a demonstration project, but our results can be generalized to fit many additional important content domains including but not limited to all audio news media.  Our ontology-based model demonstrates its power over keyword based search techniques by providing many different levels of abstraction in a flexible manner with greater accuracy in terms of precision, recall and F score.  Although we are confident that the fundamental conceptual framework for this project is sound, and its implementation completely feasible from a technical standpoint, some questions remain to be answered in future work. These include detailed work on user studies and evaluation.  In this connection, we are confident that we will ultimately be able to develop an intelligent agent that will dynamically update user profiles. This will provide a level of customization that can have broad application to many areas of content and user interest. 

###### **9 References** 

- [1] S. Adali, K. S. Candan, S. Chen, K. Erol, and V. S. Subrahmanian, “Advanced Video Information System: Data Structures and Query Processing,” _ACM-Springer Multimedia Systems Journal_ , vol. 4, pp. 172-186, 1996. 

- [2] B. Arons, “SpeechSkimmer: Interactively Skimming Recorded Speech,” in _Proc. of ACM Symposium on User Interface Software and Technology_ , pp. 187-196, Nov 1993. 

- [3] G. Aslan and D. McLeod, “Semantic Heterogeneity Resolution in Federated Database by Metadata Implantation and Stepwise Evolution,” _The VLDB Journal, the International Journal on Very Large Databas_ es, vol. 18, no. 2, Oct 1999. 

- [4] R. Baeza and B. Neto, _Modern Information Retrieval_ , ACM Press New York, Addison Wesley, 1999. 

- [5] M. Bunge, _Treatise on basic Philosophy, Ontology I: The Furniture of the World_ , vol. 3, Reidel Publishing Co., Boston, 1977. 

- [6] S. Gibbs, C. Breitender, and D. Tsichritzis, “Data Modeling of Time based Media,” in _Proc. of ACM SIGMOD_ , pp. 91-102, 1994, Minneapolis, USA. 

- [7] J. Gonzalo, F. Verdejo, I. Chugur, and J. Cigarran, “Indexing with WordNet Synsets can Improve Text Retrieval,” in _Proc. of the Coling-ACL’98 Workshop: Usage of WordNet in Natural Language Processing Systems_ , pp. 38-44, August 1998. 

- [8] T. R. Gruber, “A Translation Approach to Portable Ontology Specifications. Knowledge Acquisition,” _An International Journal of Knowledge Acquisition for Knowledge-based Systems_ , vol. 5, no. 2, June 1993. 

- [9] N. Guarino, C. Masolo, and G. Vetere, “OntoSeek: Content-based Access to the Web,” _IEEE Intelligent Systems_ , vol. 14, no. 3, pp. 70-80, 1999. 

- [10] A. G. Hauptmann, “Speech Recognition in the Informedia Digital Video Library: Uses and Limitations,” in _Proc. of the Seventh IEEE International Conference on Tools with AI_ , Washington, DC, Nov 1995. 

- [11] R. Hjelsvold and R. Midstraum, “Modeling and Querying Video Data,” in _Proc. of the Twentieth International Conference on Very Large Databases (VLDB’94)_ , pp. 686-694, Santiago, Chile, 1994. 

- [12] L. Khan and D. McLeod, “Audio Structuring and Personalized Retrieval Using Ontologies,” in _Proc. of IEEE Advances in Digital Libraries, Library of Congress_ , pp. 116-126, Bethesda, MD, May 2000. 

- [13] L. Khan and D. McLeod, “Disambiguation of Annotated Text of Audio Using Onologies,” to appear in _Proc. of ACM SIGKDD Workshop on Text Mining_ , Boston, MA, August 2000. 

- [14] D. B. Lenat, “Cyc: A Large-scale investment in Knowledge Infrastructure,” _Communications of the ACM_ , pp. 33-38, vol. 38, no. 11, Nov 1995. 

- [15] G. Miller, “WordNet: A Lexical Database for English,” _Communications of the ACM,_ ” vol. 38, no. 11, Nov, 1995. 

- [16] E. Omoto and K. Tanaka, “OVID: Design and Implementation of a Video-Object Database System,” _IEEE Transactions on Knowledge and Data Engineering_ , vol. 5, no. 4, August 1993. 

- [17] H. J. Peat and P. Willett, “The Limitations of Term Cooccurrence Data for Query Expansion in Document Retrieval Systems,” _Journal of ASIS_ , vol. 42, no. 5, pp. 378-383, 1991. 

- [18] L. R. Rabiner and R. W. Schafer, _Digital Processing of Speech Signals_ , Prentice Hall, 1978. 

- [19] G. Salton, _Automatic Text Processing_ , Addison Wesley, 1989. 

- [20] A. F. Smeaton and V. Rijsbergen, “The Retrieval Effects of Query Expansion on a Feedback Document Retrieval System,” _The Computer Journal_ , vol. 26, no. 3 pp. 239-246, 1993. 

- [21] B. Swartout, R. Patil, K. Knight, and T. Ross, “Toward Distributed Use of Large-Scale Ontologies,” in _Proc. of the Tenth Workshop on Knowledge Acquisition for Knowledge-Based Systems_ , Banff, Canada, 1996. 

- [22] E. Voorhees, “Query Expansion Using LexicalSemantic Relations,” in _Proc. of the Seventeenth Annual International ACM SIGIR Conference on Research and Development in Information Retrieval_ , pp. 61-69, 1994. 

- [23] L. D. Wilcox and M. A. Bush, “Training and Search Algorithms for an Interactive Wordspotting System,” in _Proc. of ICASSP_ , vol. 2, pp. 97-100, San Francisco, CA, 1992. 

- [24] W. Woods, “Conceptual Indexing: A Better Way to Organize Knowledge,” _Technical Report of Sun Microsystems_ , 1999. 

45 

### **Incorporating Domain Knowledge with Video and Voice Data Analysis in News Broadcasts** 

_∗_ 

Kim Shearer IDIAP P.O. BOX 592 CH-1920 Martigny, Switzerland Kim.Shearer@idiap.ch 

Chitra Dorai IBM T. J. Watson Research Center P.O. Box 704, Yorktown Heights New York 10598, USA dorai@watson.ibm.com 

Svetha Venkatesh School of Computing Curtin University of Technology P.O. BOX U1987, Australia svetha@cs.curtin.edu.au 

###### **ABSTRACT** 

This paper addresses the area of video annotation, indexing and retrieval, and shows how a set of tools can be employed, along with domain knowledge, to detect narrative structure in broadcast news. The initial structure is detected using low-level audio visual processing in conjunction with domain knowledge. Higher level processing may then utilize the initial structure detected to direct processing to improve and extend the initial 

The structure detected breaks a news broadcast into segments, each of which contains a single topic of discussion. Further the segments are labeled as a) anchor person or reporter, b) footage with a voice over or c) sound bite. This labeling may be used to provide a summary, for example by presenting a thumbnail for each reporter present in a section of the video. The inclusion of domain knowledge in computation allows more directed application of high level processing, giving much greater efficiency of effort expended. This allows valid deductions to be made about structure and semantics of the contents of a news video stream, as demonstrated by our experiments on CNN news broadcasts. 

###### **Categories and Subject Descriptors** 

H.3.3 [ **Information Storage and Retrieval** ]: Information Search and Retrieval; H.2.4 [ **Database Management** ]: Systems— _Multimedia Databases_ ; H.2.8 [ **Database Management** ]: Database Applications— _Data mining_ 

###### **General Terms** 

Video annotation, domain knowledge, algorithm fusion 

###### **1. INTRODUCTION** 

Research into image databases and image indexing and retrieval has led to the creation of a number of useful tools for similarity retrieval for images [6, 9, 4, 16]. Application of these tools to video is possible, but the principles embodied in the tools do not yield a useful query system. Previous work on video indexing and retrieval [22, 10, 20, 23, 3, 9] has most commonly relied largely on one aspect of video, be it vision or sound, and has been restricted to low-level or undirected processing. The results of this processing are then used for classification, with the goal of detecting either video events, or some form of structure within video. Detection of events or structure permits a summary of the video to be formed, thus permitting more rapid user browsing by a restriction of the information or segments presented for browsing. 

Examples of the form of summaries are the Video Icons of Tonomura and Abe [18, 19], the excellent work by Davis [5] on MediaStreams, general systems such as [14, 8, 17] and the scene transition graphs of Yeo and Yeung [21, 2]. These methods aim at presentation of video content in a condensed manner so that the extreme amount of information available may be scanned by the user in a more efficient manner. The scene transition graphs of Yeo and Yeung go slightly further than most earlier work in that they present a possibility for automated deduction of semantically related structure from a video stream. 

Shot syntax, colour coherence vector, voice clustering 

###### **Keywords** 

- _∗_ Corresponding author. 

In this paper we describe a collection of tools and their application to the detection of narrative structure in a news broadcast. In particular, these tools are used to break the broadcast into segments, each of which contains a single topic of discussion. These segments are classified further by labeling each individual shot as one of 

- anchor person or reporter, 

> © The copyright of this paper belongs to the paper's authors. Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 

(O.R. Zaïane, S.J. Simoff, eds.) 

- footage with a voice over, 

- sound bite, 

46 

which gives a clear indication of structure within the video. This work differs from earlier work in that it employs not only low-level processing, but uses results from this processing, along with initial deductions about structure within video, to apply higher level processing in a directed manner. This allows a novel iterative approach to be used, with alternating processing and deduction employing progressively more complex computation as the interpretations become more finely focused. The summary produced from this work can then go further than simply presenting a representative sampling of video, by providing a summary based on the semantics of the content. 

The aim of this work is to allow automated annotation of video, which will allow intelligent construction of summaries for large video databases. The particular target area is news broadcast and news magazine footage, such as that kept by major news companies. The annotation created will break the video into segments of homogeneous topic, and further label shots as anchor or report footage. A typical summary that might then be created would be a thumbnail of each anchor person or reporter present in a section of video. The user may then select the reporter who filed a story, rather than having to search for a representative frame which might be contained in the story required. Given the large volume of video data retained for such applications, and the volume captured at each moment, this could result in a large reduction in unproductive human time and lead to a scalable and efficient solution for content management in studios. 

###### **2. COMPONENTS AS TOOLS** 

A number of components may be employed in the analysis of video streams. These components are employed to assess similarity of shots within the video stream, along a number of axes. This similarity within the video stream is then used with a knowledge of shot syntax, and higher level processing, to deduce structure within the news video stream. 

###### **2.1 Detection of Anchor Segments** 

The concept of shot syntax was developed to describe the regular structure of camera parameters employed to capture a particular type of semantic content [2, 21]. The clearest example of regular shot syntax is in interviews. In an interview video it is generally the case that the interview will be introduced by the interviewer. There will then usually be either a shot of the interviewer and the interviewee, or a shot of the interviewee alone. Subsequent shots will be of either; interviewer, interviewee, a mid-range shot of the two people involved, or background footage. This repetitive structure is adopted for interviews as it has been found to be the best method of producing this type of program. 

If the assumption can be made that such repeated structure will be present within a video stream of a particular program genre, then detection of repetition in shot settings provides a useful first pass for the grouping of shots into meaningful segments. News broadcast does in general adhere to such a structure, as shown in Figure 1. In this figure solid lines indicate required minimum paths through the syntax diagram, with dashed lines denoting optional paths. The regular structure displayed makes it useful to search for repetitions of anchor or reporter segments. That is, shots with one person addressing the camera, and this person pre- 



**Figure 1: Shot syntax of a broadcast news program.** 



**Figure 2: Typical syntax of a news program with a field report.** 

senting a particular segment of the program, therefore, appearing repeatedly. The term anchor shot will be used to refer to this type of shot, whether it is a shot of an actual anchor person, or a shot of a reporter who is the presenter for a particular story. A story presented (or anchored) by a reporter in the field generally represents a self contained sub–syntax of a larger report. Figure 2 shows a possible syntax for such a segment, the field report presented by a reporter is contained within the dashed line box. The shot syntax for this report is clearly similar to the syntax for a general report. 

In our news video processing system, the search for anchor shots takes advantage of a property inherent to such shots. Anchor shots are intended to provide continuity for a news broadcast, which means that the intent of such shots is to present a consistent appearance to viewers. Therefore such shots are captured in a consistent location, with mostly consistent shot parameters. This visual consistency makes detection of repetitions of the anchor simple to detect. Reporters in the field also usually present a highly consistent appearance, however, this is less dependable due to outside factors. 

Initially colour coherence vectors (CCVs) [11, 8] were used to detect similarity between frames sampled from a video 

47 









**Figure 3: Facial rotation for which CCV performs poorly.** 

**Table 1: Similarity measure using CCV for the video frames shown in Figure 3.** 

||111|112|113|
|---|---|---|---|
|112|5886|||
|113|25759|25559||
|114|7839|4681|25544|



**Table 2: Similarity measure using spatial histograms for the video frames shown in Figure 3.** 

||111|112|113|
|---|---|---|---|
|112|71112|||
|113|71410|5374||
|114|70844|8220|5454|



to indicate anchor sections. However, CCVs perform poorly with a number of scenarios that occur frequently in news video. The main problem occurs with faces which dominate the frame, and rotate under studio lighting. In these cases the coherence of the colour regions can change dramatically for a small movement. This situation often occurs in anchor shots, where a reporter glances down at a page of notes, or to the left or right to pass to an interviewee or other reporter. 

Simple colour histograms provide a useful indication of similarity, but as expected find too many shots to be similar. Using such a global measure allows too many frames of similar colour to be clustered as similar, and will also find frames within a shot that has a great deal of motion similar. For the task of separating anchor and reporter shots from other shots, it is acceptable that motion in the shot, such as the motion apparent in crowd scenes, cause frames to be found dissimilar. The goal is then that each anchor or reporter shot be found coherent (internally similar) and similar to other shots of the same reporter or anchor. 

As a result a different similarity measure was employed in our system, where each frame is broken into 12 subframes, and a colour histogram is computed for each. Each histogram is quantized to 16 bins, and histogram difference ∆ is a sum of the differences between values for each bin _i_ . That is 



The histograms for spatially corresponding subframes are then compared, with the sum of the histogram differences for the subframes representing the distance between frames. The similarity values for the video frames in Figure 3 are given in tables 1 and 2. As can be seen from Table 1, the CCV algorithm finds that frame 111 is far more similar to frame 112 than frame 112 is to frame 113, and also that frame 114 is similar to frames 111 and 112 but not 113. This is due to the changes in colour values for the face and hair of the pictured person in frame 113 as the head tilts slightly. The size of areas containing a particular colour change dramatically with only small head movements. For the same four frames the histogram measure performs much more as expected, easily separating the frames correctly. 

In addition to addressing the problem illustrated in Figure 3 the algorithm we employed has another useful property. While each shot of an anchor person or reporter is found to be coherent, most other shots are not. This is due to the sensitivity of the algorithm to overall fluctuations in colour and position of colour. Scenes which might seem likely to be found similar under a colour based measure, such as shots of a crowd, are in fact separated into numerous short pieces. This has the advantage of reducing the number of shots that are detected as repeated shots within a video stream, thus making the task of shot syntax analysis simpler. 

There are of course other shots which will be repeated during a broadcast, such as the logo of the news station, advertisements which are repeated and footage used as a preview for stories in later programs. One tool which is often useful in distinguishing these shots from anchor shots is face detection. While face detection is only reliable in constrained 

48 

applications, it is suitable for this problem. A search for faces in anchor shots will be assisted by the regular presentation of these shots, while advertisements are generally quite erratic and have few static, and therefore detectable, faces. 

The face detection part of classification is performed using the CMU face detection software [13]. This is a neural network based face detector, in which neural networks are applied directly to each 20 by 20 pixel location in the image. In order to accommodate scaling transformations the image is presented to the system at actual size, and then repeatedly scaled down by a factor of 1.2 and again presented to the system. Training is accomplished on a set of face images, and non-face images, with false positives in the non-face images being used as negative examples in further training. A number of heuristics are used both to improve accuracy and to improve speed. This system is chosen as representative of the current state of the art in face detection, and its performance is easily sufficient for the given task. 

Anchor shots exhibit the following properties which make face detection more reliable: 

- the face is turned directly towards the camera, 

- the face dominates the shot. 

Face detection can therefore be restricted to searching for large faces. The majority of false detections that are artifacts of other parts of the image are small relative to the faces in anchor shots, so size can be used as an effective filter. Searching for only those faces which directly face the camera also simplifies the problem, further reducing the error rate. 

Shots that repeat with a suitable shot syntax and have a consistently visible face are highly likely to be anchor shots. The assumption of temporal consistency can be used to further reduce error from face recognition by discarding faces that move rapidly or erratically. This will tend to discard footage of people addressing a crowd, but include field reporters. Reporters in the field will be less static than anchors in the studio, but all field reports in the data set tested were detected as dominant faces. Temporal consistency can also be applied to the colour histogram work by using an average histogram for each group of frames which are considered similar, to represent the matching attribute set. This limits the spread of a single group by preventing a chain of frames with small error from each other remaining part of a single group even though the error diverges further and further from a previous group. 

Once these two steps of visual processing have been completed a first pass is performed to determine structure from shot syntax. This yields a preliminary label for each shot as either an anchor shot, or a non-anchor shot. To label the shots in finer detail the sound associated with the video is processed. This presents a difficult problem, as there is no simple method to ensure clean audio samples. While voice recognition in an environment for which extensive training samples are available, and voice samples are well separated 

can show good performance, this is not the case for this application. 

###### **2.2 Audio Analysis** 

To label the shots in finer detail, the audio associated with the video is analyzed. Much of the sound from news broadcast will contain noise of various forms, such as background noise for field reports. In addition, there are a number of behaviours presented by anchor people, which aid in keeping the flow of dialogue, that prevent clean segmentation of sound samples. One example is that the anchor person will often begin speaking before a field reporter or piece of footage has stopped, which aids flow but makes it impossible to separate one voice from another. In addition, the anchor will generally start speaking before the cut from one shot to another, or will start speaking just after the cut with sound from the previous segment continuing slightly past the cut. This means that most audio samples will contain multiple voices when segmentation of the audio stream is performed. 

Previous work has suggested that four seconds is a suitable segment length for vocal samples to exhibit a consistent attribute profile [7], and this is the length employed in this work. Three methods of segmentation for sound were studied for comparison. Two methods attempt intelligent segmentation, the first using silence as an indicator for segmentation points and the second using cuts in the video. The final method employed was to simply cut the video every four seconds starting at the first frame. For each of the first two methods, sections longer than 4 seconds are cut into four second pieces, and segments shorter than 4 seconds are discarded. Segmentation based on silence detection performs significantly worse than either of the other methods, for reasons mentioned earlier. As there is little to choose between the performance of the two other methods, simple fixed time segmentation is used in our system for simplicity. 

Audio classification is performed using formant frequency estimators [12, 15] and other low-level attributes as in [1], and k-means clustering. The most suitable number of clusters is chosen by minimizing total error, within a reasonable range. Thus at the end of audio processing, each four second audio segment is assigned an audio cluster label. 

###### **3. FUSION OF COMPONENT RESULTS** 

The three initial pieces of low-level processing are combined to determine the initial classification of shots as either anchor shot, voice over or sound bite using the following rules: 

- Anchor shots will be repeated shots with a sequence of not more than 4 shots between, and a time between anchor shots of not more than 8 times the length of the anchor shot. They will also have a prominent face detected. 

- Other shots will be initially classified as footage. 

- Footage shots with vocal clustering similar to an anchor shot in the same grouping will be determined as voice over. 

- Footage shots with vocal clustering dissimilar from any anchor shot in the initial grouping will be labeled as sound bite. 

49 

||**Table 3**<br>Total<br>number|**: Classifc**<br>False<br>positives|**ation resu**<br>False<br>negatives|**lts.**<br>Accuracy|
|---|---|---|---|---|
|Anchor<br>shots|44|4|6|79%|
|Voice<br>Over|54|2|8|82%|
|Sound<br>Bite|28|4|4|75%|



The first rule is also used to break the video stream into segments, with each segment containing a single story topic. 

In practice the grouping of shots based on identification of anchor and reporter shots and duration between these shots detects 100% of the structure in the news video. The test set for this work contains two videos of approximately 50 minutes in length each, and includes a number of CNN news and magazine style programs. The structure detected represents a slight over segmentation, in that some reports have the anchor shot which introduces the segments, and the anchor shot concluding the segment discarded. This is due to the segment being anchored by a reporter, and thus exhibiting the shot syntax expected within the report (Figure 2), with the introductory and concluding segments being no more than a tie–in to the news program. It is deemed reasonable that these shots be discarded. The important feature of the segmentation is that no segment contains more than one topic, which could result in hiding of information from the user. 

Table 3 gives a summary of the results from classification using the initial low-level processing and shot syntax. As can be seen, detection of shot syntax allows accurate classification of most of the video. The values in the accuracy column of Table 3 are calculated from the equation 



where _Actual_ is the correct number of samples for the shot type, and _Fneg_ and _Fpos_ are the number of false negatives and false positives for the classification. The majority of the misclassifications are due to too few sound samples being available for accurate audio classification of a shot. The false negatives for the anchor shots are due partly to the lead and trailing shots of a long report being dropped as discussed earlier, and also to one group discussion having two presenters. The anchor shots for this section are detected as similar, but have no single dominant face. Further processing discussed in later sections in this paper could be used to improve detection to include this case. 

###### **4. DIRECTED APPLICATION OF HIGH LEVEL PROCESSES** 

Given this initial segmentation of the shots within the video stream into structured blocks, further processing may now be considered. The main additional processing is a more detailed face detection pass applied to the shots classified as footage. This allows _interview_ shots to be more accurately detected. 

|**Table 4: **|**Intervie**<br>|**w shot de**<br>|**tection.**<br>|
|---|---|---|---|
||Total|False|False|
|||positives|negatives|
|Sound bite|4|8|0|
|Interview|24|0|8|



Allowing a greater range of sizes for a face increases both the time required, and the error rate for face detection. However, when footage is taken in the field it is less likely that an interview shot will show a dominant face front on. In this case greater care must be taken in assessing the results from the face detection algorithm. Results are examined closely for consistency of location and size of faces that are detected. Erratic size and or location can be sufficient to discard a face from consideration. Any shot which presents a single consistent face for the majority of the shot is labelled as a reporter. 

The result of this further classification applied to the sound bite shots is given in Table 4. These results indicate that the detection of faces in these shots is still less than perfect, however, two thirds of the interview shots were detected. Given this level of recognition further classification can be performed as determined by shot syntax. 

Further processing could be employed to specifically search for faces that are not perpendicular to the camera, which could add to the accuracy of this second step. In particular shots which are likely to be part of an interview segment, and which have no dominant face, could be tested for two faces. This would help detect the interviewer and interviewee shots, which would add further weight to the classification of such shots. This is intended as future work. 

###### **5. RESULTS** 

Figure 4 shows the thumbnails for the shots from one segment of detected structure. The caption for each thumbnail gives the visual similarity group computed using segmented colour histograms, the number of faces detected using the CMU face detection software [13], and the similarity group from aural clustering for the shot. 

The topic of the segment is a report on the public view of the Medicare bill recently introduced in the USA. There is an anchor shot (Figure 4(a)), followed by a shot of only one sample which coincides with a fade (Figure 4(b)). This shot would be discarded from consideration. There is then a shot of explanatory text (Figure 4(c)), which is correctly identified as a voice over. The next shot (Figure 4(d)) is of Bill Clinton addressing a group of reporters, this is identified as a voice over due to incorrect vocal clustering. No face was detected due to the mobility of the speaker around the stage. Figure 4(e) shows another anchor shot, which is correctly identified. Figures 4(f) and 4(g) are of “people on the street”, interviewed about their views on the topic. They are correctly identified as separate pieces of footage, and labelled as sound bites. In both cases the camera parameters are too irregular to expect face detection. The final figure, Figure 4(h) is the closing anchor shot, and is identified as such. 

50 





(a) Visual group 116, Faces 1, Aural group 1. 

(b) Visual group 117, Faces 1, No aural group. 







<!-- Start of picture text -->
(d) Visual group 119,<br>Faces 0, Aural group 1.<br><!-- End of picture text -->

(c) Visual group 118, Faces 0, Aural group 1. 







<!-- Start of picture text -->
(f) Visual group 120,<br>Faces 0, Aural group 2.<br><!-- End of picture text -->

(e) Visual group 116, Faces 1, Aural group 1. 







<!-- Start of picture text -->
(g) Visual group 121, (h) Visual group 116,<br>Faces 0, Aural group 3. Faces 1, Aural group 1.<br><!-- End of picture text -->

**Figure 4: Structure in an example news program.** 





(a) Shot 394 – Visual group 122, Faces 1, Aural group 1. 

(b) Shot 395 – Visual group 335, Faces 1, Aural group 2. 





(c) Shot 396 – Visual group 336, Faces 1, Aural group 3. 

(d) Shot 397 – Visual group 122, Faces 1, Aural group 1. 







<!-- Start of picture text -->
(e) Shot 398 – Visual (f) Shot 399 – Visual<br>group 337, Faces 0, Au- group 122, Faces 1, Au-<br>ral group 1. ral group 1.<br><!-- End of picture text -->

**Figure 5: Thumbnails of a news report with male anchor.** 

As can be seen, the clip of Bill Clinton (Figure 4(d)) is classified as a voice over, rather than a separate piece of footage. This is in part due to the brevity of the shot, and in part due to the noise and length of pause in the spoken voice. Improved audio processing would perhaps reduce this difficulty. However, it must be assumed that many of the voices which occur in these shots will be unseen. While some people are regularly included in news bulletins (Bill Clinton as President), many others will be involved in news for only a brief period, corresponding to the time of a particular event and story. Moreover, the “people on the street” interviewed are intended to be random choices. This makes the task of separating such voices from each other more difficult. A further difficulty observed is that the anchor people will have numerous samples of their voice present, and any agglomerative classification method should associate these. The smaller groups of other voices, often with only a small number of samples, and the samples containing multiple voices, make it difficult to distinguish between outliers and separate samples. 

51 

**Table 5: Vocal** **<u>(dis)similarity</u> for shots in Figure 5.** 

||395|396|397|398|399|
|---|---|---|---|---|---|
|394|0.747|0.720|0.054|0.102|0.142|
|395||0.340|0.958|0.887|0.907|
|396|||0.931|0.860|0.881|
|397||||0.167|0.228|
|398|||||0.005|



An example where voice classification does work well is shown in Figure 5 and Table 5. This sequence of shots shows a male anchor person, Lou Waters, presenting a story on harassment, with two people interviewed (Figures 5(b) and 5(c)) and a commentary over a still (Figure 5(e)). Table 5 presents value of the distance measure used in audio similarity detection for the six shots. The values for the comparison of the two interviewees to the anchor person are clearly separable from those for the comparison of anchor person shots, with a range of [0 _._ 72 _−_ 0 _._ 958] compared to a range of [0 _._ 005 _−_ 0 _._ 228] for the similar shots. The voices of the two interviewees are quite similar, and could reasonable be clustered together, their dissimilarity value of 0.34 is classified by the system as similar. 

Figure 5 also provides a further example of the frame similarity algorithm, with the shots in Figure 5(f) containing an extra image, but still being found similar to the earlier anchor shots. In addition to this the two shots of interviewees, although visually quite similar are correctly separated. Figure 5(f) also gives an additional example of the type of head movement which is misclassified by the CCV algorithm. 

###### **6. CONCLUSIONS** 

The process employed in this work combines a number of image and aural low–level processes that, in isolation, are unreliable for classification of video. The fusion of the results of these processes, together with knowledge of the shot syntax for a particular domain, leads to a reliable and high level structure labeling of the video. While the resulting classification is less than perfect, all significant structure is recognized, albeit slightly over segmented. 

The segmentation produced separates shots into homogeneous story segments, and is able to identify the shots which contain anchor people and reporters. The ability to extract the shots containing reporters and anchors is particularly important, as this provides a powerful key for access to the video content. This gives a suitable starting point from which a summary may be produced without hiding information from the user. 

Further processing, such as the proposed refinement of face detection, would allow extraction of more detailed structure. Detection of interviewer and interviewee shots in interview segments would allow not only the presenting reporter to be identified visually as a key, but also the interviewee. 

Further visual processing in the form of text detection and recognition is a possible future extension. Improvement to the audio processing is also an avenue for increasing the accuracy of the system, and perhaps allowing further information to be extracted. Given key words recognized from 

audio, and text recognized from video such as can be seen in Figure 4(c), further fusion of results may be useful for improving recognition of these stages. 

The inclusion of shot syntax as a model for structure within news video is a major advantage for detection of shot type. This allows the extension of simple attribute based indexing to deduction of semantic structure within video, and the separation of video into segments of homogeneous semantic content. Extraction of semantic segments and deduction of shot type from a video stream greatly increases the utility of a video warehouse. Currently research is being undertaken to examine how well the shot syntax concept generalizes to other forms of video. Interview and news footage have a very regular shot syntax, but there are other forms of video with regular shot syntax which might be detected using similar techniques, or by application of additional measures. Research is also being undertaken to determine methods for the deduction of shot syntax structure from samples of a particular video form. Such a process could be of great value in multimedia and video data mining. 

###### **7. ACKNOWLEDGMENTS** 

The authors would like to acknowledge the assistance of CNN for providing news footage that formed the base data set for this work. 

###### **8. REFERENCES** 

- [1] T. Blum, D. Keisler, J. Wheaton, and E. Wold. Audio databases with content–based retrieval. In M. Maybury, editor, _Intelligent Multimedia Information Retrieval_ , chapter 6, pages 113–135. The MIT Press, 1997. 

- [2] R. Bolle, B.-L. Yeo, and M. M. Yeung. Video query and retrieval. In _Advanced Topics in Artificial Intelligence_ , volume 1342 of _Lecture Notes in Artificial Intelligence_ , pages 13–24. Springer, December 1997. 

- [3] A. Cheyer and L. Julia. MVIEWS: multimodal tools for the video analyst. In _Proceedings of the International Conference on Intelligent User Interfaces_ , pages 55–62. ACM, January 1998. 

- [4] J. M. Corridoni, A. Del Bimbo, and P. Pala. Image retrieval by color semantics. _Multimedia Systems_ , 7(3):175–183, May 1999. 

- [5] M. Davis. Media streams: An iconic visual language for video annotation. In _Proceedings of the IEEE Symposium on Visual Languages_ , pages 196–202. IEEE, April 1993. 

- [6] M. Flickner, H. Sawhney, W. Niblack, J. Ashley, Q. Huang, B. Dom, M. Gorkani, J. Hafner, D. Lee, D. Petkovic, D. Steele, and P. Yanker. Query by image and video content: The QBIC system. _IEEE Computer_ , 28(9):23–32, September 1995. 

- [7] H. Gish, M. Sui, and R. Rohlicek. Segregation of speakers for speech recognition and speaker identification. In _ICASSP–91_ , pages 873–876. IEEE, IEEE, 1991. 

52 

- [8] R. Lienhart, S. Pfeiffer, and W. Effelsberg. Scene determination based on video and audio features. In _Proceedings IEEE Multimedia 99_ , pages 685–690, Firenze, June 1999. IEEE. 

- [9] W. Y. Ma and B. S. Manjunath. NeTra: A toolbox for navigating large image databases. In _Proceedings of the International Conference on Image Processing_ , pages 568–571, 1997. 

- [10] K. Minami, A. Akutsu, H. Hamada, and Y. Tonomura. Video handling with music and speech detection. _IEEE Multimedia_ , 5(3):17–25, July 1998. 

- [11] G. Pass, R. Zabih, and J. Miller. Comparing images using colour coherence vectors. In _Proceedings ACM Multimedia 96_ , pages 65–74, Boston, November 1996. ACM. 

   - [21] B.-L. Yeo and M. M. Yeung. Classification, simplification and dynamic visualization of scene transition graphs for browsing. In _Storage and Retrieval for Image and Video Databases VI_ , pages 60–70. SPIE, December 1998. 

   - [22] M. Yeung, B.-L. Yeo, W. Wolf, and B. Liu. Video browsing using clustering and scene transitions on compressed sequences. In _Proceedings of the SPIE_ , volume 2417, pages 399–413. SPIE, 1995. 

   - [23] S. J. Young, M. G. Brown, J. T. Foote, G. J. F. Jones, and K. S. Jones. Acoustic indexing for multimedia retrieval and browsing. In _ICASSP 97_ , volume 1, pages 199–202. IEEE, IEEE, 1997. 

- [12] L. R. Rabiner and R. W. Schafer. _Digital Processing of Speech Signals_ . Signal Processing Series. Prentice Hall, 1978. 

- [13] H. A. Rowley, S. Baluja, and T. Kanade. Neural network–based face detection. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , 20(1):23–38, January 1998. 

- [14] C. Saraceno and R. Leonardi. Audio as a support to scene change detection and characterization of video sequences. In _Proceedings of ICASSP 97_ , pages 2597–2600. IEEE, IEEE Computer Society Press, 1997. 

- [15] K. Shearer, S. Venkatesh, and C. Dorai. Attribute based discrimination of speaker gender. Technical Report 4, Curtin University of Technology, GPO Box U1987, Perth 6001, Western Australia, November 1999. 

- [16] D. M. Shotton, A. Rodriguez, N. Guil, and O. Trelles. Analysis and content–based querying of biological microscopy videos. In _Proceedings of the 15th International Conference on Pattern Recognition_ . IAPR, IAPR, 2000. 

- [17] S. Srinivasan, D. Petkovic, and D. Ponceleon. Towards robust features for classifying audio in the CueVideo system. In _Proceedings of ACM Multimedia 99_ , pages 393–400. ACM, ACM, 1999. 

- [18] Y. Tonomura and S. Abe. Content oriented visual interface using video icons for visual database systems. In _IEEE Workshop on Visual Languages_ , pages 68–73. IEEE, 1989. 

- [19] Y. Tonomura, A. Akutsu, K. Otsuji, and T. Sadakata. VideoMAP and VideoSpaceIcon: Tools for anatomizing video content. In _INTERCHI 93 Conference Proceedings_ , pages 131–138, 1993. 

- [20] S. Tsekeridou and I. Pitas. Audio–visual content analysis for content–based video indexing. In _IEEE International Conference on Multimedia Computing and Systems_ , pages 667–672. IEEE, IEEE, 1999. 

53 

### **Multimedia Support for Complex Multidimensional Data Mining** 

Monique Noirhomme- Fraiture 

Institut d’Informatique, FUNDP 

Namur, Belgium 

mno@info.fundp.ac.be 

###### **ABSTRACT** 

ISO-3D project aims to develop tools in order to analyse and represent business information from large collection of data. The designed tools are mainly representation tools using 3D graphics, sound and animation. 

In this paper, we will present two of the graphic representation tools which use also sound and animated picture. We will explain why and how we use sound and animation with graphical representation in this data mining approach. 

###### **Keywords** 

Symbolic Objects, Visualisation, Sound, Animation. 

###### **1. INTRODUCTION** 

Economical data usually depend upon time but are also explained by an important number of heterogeneous variables. When recorded systematically, like in portfolio management (for banks) or audience monitoring (for TV), they constitute rapidly huge data bases. Managers need tools for extracting daily knowledge from these data. 

Symbolic Analysis is a kind of data analysis which is able to deal with complex multidimensional heterogeneous  data and to summarise information. It is broadly accepted that graphic representation facilitates interpretation of results. 

Development of multimedia techniques allow now other representation means than visualisation by graphics; we think here to sound and animation. Moreover, in order to take quick decisions, it is necessary to work without delay on data which are often stocked on another site. It is why network technology is used. 

ISO-3D project aims to develop tools in order to analyse and represent business information from large collection of data integrating also those new techniques. The prototype is running in 

© The copyright of this paper belongs to the paper's authors. Permission to copy without 

- fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. 

- Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 

(O.R. Zaïane, S.J. Simoff, eds.) 

a client/server architecture called Infobus, based on more recent network technology. The designed tools are mainly representation tools using 3D graphics as well as sound and animation. 

In this paper, we will present two of the graphic representation tools which use also sound and animated picture. Before that, we will explain what is Symbolic Analysis in order to understand the data in input of our representation process for introduction of multimedia support and we will develop some arguments for the use of sound in data exploration. 

###### **2. COMPLEX OBJECTS CALLED SYMBOLIC OBJECTS** 

The standard methods of statistical data analysis accept as input, « individuals » by « variables » matrix. Each cell (i,j) of such an array contains the value taken by individual i for variable j. The value is said to be « atomic » in the sense that it is not a list or a set of values. 

The Symbolic Data Analysis [BOCK&00] extends the input data structure to « individuals » by « variables » arrays where the value taken by an individual on a variable may be non-atomic, but possibly a set of values, intervals of values or a probability distribution. 

For example this values can be 

1. A set of quantitative values : [Age = {15, 22, 45, 47}]. It means that the age of family members are 15, 22, 45 and 47. 

2. A set of categorical values : [TV preference = {RAI1, R4}] 

(notice that standard quantitative and categorical values are special cases of 1 and 2). 

3. An interval : [Age = [15, 47]] which means that age in the family is between 15 and 47. 

4. A set of weighted categorical values : [TV preference = {RAI1 (0.3), R4 (0.7)}] which means that 30 % of the family has daily preference for RAI1 channel and 70 % of the family has daily preference R4 channel. 

We will give the name of Symbolic Object (SO) to a row of non atomic value. 

54 

###### **3. VISUAL REPRESENTATION** 

m 

From user requirements in SODAS [NOIRHOMME&00] and ISO-3D projects, we know that users need to visualise a Symbolic Object (SO), a SO inside the reference population, various SOs in principal components space, SO during time and important changes, they also need to point out particular SOs on other graphs (like hierarchies, result of SO classification) and visualise them. 

In ISO-3D, to meet these requirements, we have suggested the Temporal Star and the Simple Star graphical representation. 

First, we will remember the principles of the Zoom Star [NOIRHOMME&00]. 

The **Zoom Star** representation is a radial graph where each axis corresponds to a variable . 

We allow variables in intervals, multivaluate values, weighted values to be represented. We chose conventions for axes representation (colour, dots). A two dimensional and a threedimensional representation have been designed. 

In the 2D Zoom star, axes are linked according to each variable values (see figure 1 of Simple Star). Most weighted value of a categorical variable are linked as well as extremities of intervals. A surface is drowned by joining extremities of intervals or points of highest weight. This representation does not allow details about distributions associated to weighted categorical variables. However, the user can ask for the complete distribution to be displayed in another window by selecting the axis. 

On the 3D Zoom Star representation, distributions corresponding to each weighted values are shown directly on the axis. We provide the user with the opportunity to animate the graphic by turning the picture around a vertical and an horizontal axis in order to make easier the retrieval of pertinent information. On the 3D representation, axes are not linked because the image is continuously changing due to animation feature. The iconic representation is then meaningless in that case. 

Let us note that evaluation of the Zoom Star has been made in the past with students [NOIRHOMME& 98] and that validation has been made by many users of SODAS project [Bisdorff99] and by researchers[MENNESSIER&98]. 

Whereas users had no preliminary experiment with this kind of representation, it appeared that the Star was user friendly and answered user problems. 

###### **3.1 Simple Star** 

The Simple Star will be mostly used to show the detail of a Symbolic Object represented on a preliminary graphic (like Temporal Star or classification representation). 

The Simple Star is analogue to the Zoom Star in 2D but the functionality are slightly different. 

To be consistent with Temporal Star, some conventions of colour and colour shade are used. 

Several stars representing different objects can be superposed (figure 1). 

**Figure 1. Two Superposed Simple Star.** 

###### **3.2 Temporal Star** 

The aim of the Temporal Star is to represent a Symbolic Object at different epochs. 

A star in perspective represents the symbolic object at a given epoch (like in the 3D Zoom Star). 

The stars at different epochs are thread on one axis representing time (figure 2). This figure can be moved and zoomed. Different colours can be chosen for the different axes.  On each axis, representing a categorical variable, the histogram can be shaded, coloured. To emphasise the evolution from one epoch to another, when the axis represents a quantitative variable (mean or intervals), the extremities of the intervals (min, max) or means can be joined. and a transparent veil will be added to the stars (on demand). 

It must be also possible to select a particular star on the thread and to display it on the form « Simple Star » (see figure 2). 

###### **4. USE OF SOUND IN GRAPHICAL DISPLAY** 

Most modern graphical displays are highly visually demanding because all information is graphically presented. Our visual sense on the other hand has a rather small area of high focus. A problem arises when a user must concentrate on the visual feedback from one part of the display, so that feedback from another part of the display may be missed as it is outside the area of visual focus. As the amount of information contained by the visual display increases, it may arise that the user become overloaded and the display ineffective. This problem has been extensively documented in recent research, for example by S.A. Brewster who studied auditory enhancements to tool palettes [BREWSTER98a], graphical buttons [BREWSTER&95], etc. 

55 



**Figure 2. Temporal Star** 

Another problem arises when representing multi-modal information. In real life, a person is interacting with more then only visual sensations. Most Human-Computer Interfaces represent however only one mode, namely the visual mode. Since it is impossible to convey all the information received by all modes using only visual representation, the user would benefit from a multi-modal interface, because of an increased amount of information and a more natural way of representing it. [ANRIJS99] 

_How sound can improve the graphical interface?_ 

In [KRAMER94], G.Kramer distinguishes several advantages that result from combining the graphical interface with sound. 

The main advantage is that sound can be integrated without interfering with the visual display. Sound is eyes-free. This _nonintrusive enhancement_ offered by sound ensures that the user does not become overloaded. It even decreases the overload because sound can replace insufficient or inappropriate visual cues 

When representing data, sound offers high dimensionality of up to seven dimensions [CONVERSY&95] and, compared to the visual display, offers _a superior temporal resolution_ and _complementary pattern recognition abilities_ . The human ear is more sensitive to changes than human vision and perceives the same information in a completely different way, thus providing new and complementary ways to detect occurring trends and relationships in datasets. Moreover, this complementary information leads to _intermodal correlations_ where patterns detected by one sensory display are confirmed and verified by the other sensory display. 

Another advantage (not mentioned by Kramer) is that short-term memory processes (and therefore remembers) 

auditory and visual data in a different way. Auditory data has been shown to be remembered longer than visual data. 

A sonic interface has one important disadvantage, namely that, unlike the human eye, which can ignore visual stimuli by moving its focus or simply closing its eyelid, a human ear cannot ignore auditory stimuli. In an office environment, this can cause severe problems as users are disturbed by sounds coming from other users. 

The most obvious solution is the use of headphones, but this isolates the user from events and communication in the office and is thus undesirable. A method using only one earphone has been proposed and tested with satisfactory results. With this method the right ear has an earphone and captures information coming from the computer, while the left ear is free to capture information from the office. 

###### **5. USE OF MUSIC IN GRAPHICAL DISPLAY** 

The potential of music as an output medium has hardly been examined. However music is the most sophisticated medium of the auditory media. The information is highly organised into complex structures and sub-structures. It can then be used to transmit complex information to a user. As emphasised by  James L. Alty [ALTY95], music has some advantages on other media : 

« - music is all-pervasive in life. It is very memorable and durable. Most people are reasonably familiar with the language of music in their own culture. Once learned, tunes are difficult to forget ». 

« - music involves the simultaneous transmission of complex ideas related over time, within an established semantic framework ». 

Let us add two other related arguments: 

- Music is often used to transmit information, even if we are not as conscious of that phenomenon as for video channel. We think here about the use of music and sound in movies. 

- Western music is organised mathematically with ratios, equal frequency differences between sounds, predefined duration (note value, silence value). It is then not surprising that mathematical structure, and numerical data can be transmitted through music. 

Music has a large variety of parameters. Besides characteristics for elementary sounds like pitch, timbre, loudness, duration, reverberation and location, music uses chords (harmony), rhythm and polyphony. This one is very helpful because it can be used to transmit several information simultaneously. 

We could think that only musicians are able to perceive musical sound with accuracy. 

56 

In [ALTY95], J. Alty describes experiments about perception of tones. Of course, he observes differences between individuals but he can conclude the following : 

- Human beings can perceive numerical difference between two tones, usually to about ± 1 tone within the octave though the accuracy decreases away from their reference point (large or small intervals are better perceived than middle ones). 

- Subjects seem to be able to follow and remember the general pattern of a tune, but the magnitude of variation vary considerably from one to another. 

- Rhythm appear as a candidate for improving intelligibility. More rapid presentation of the sequence could help. Not surprisingly, response is more accurate when the notes are organised into a tuneful sequence than when they are sorted. 

###### **6. USE OF SOUND IN ISO3D** 

We have seen the interest of using sound in HumanComputer Interface. The problem is now to decide when choosing graphic or audio. Audio can replace graphic in special cases : when the user is concentrated on a task which does not allow him any distraction by a screen, when the user is blind or is not able to see, for any kind of reason (for example, lack of light). 

In ISO 3D, these reasons have not been identified in the user requirements, (but it could happen that some users are partiallysighted). It is thus not appropriate to use audio alone. We have decided to use audio in complement to graphic representation. Graphic representation is the normal way to summarise data. Sound is not usual at all for statisticians. We think that users will be less disturbed if we use sound as a complement to graphic representation. 

Let us add that in a previous survey for SODAS project we have asked to statistical users if they were ready to use 3D, colour, sound. The answer was positive for 3D and colour but negative for sound. We have then to take into account a certain negative a priori against sound. Perhaps, that if we ask the same question to younger users, from video game generation, the answer would be different, but at the present moment, with present users, we have to introduce sound carefully. For example, sound cannot be imposed but can be chosen at the beginning of the session. 

We have tried, in absence of sound user requirement, to imagine for what kind of information sound could be used. In systems supervision or process control, sound is often used to attract attention on particular problems. 

In complex multidimensional data representation, situation is different. The more accurate problem is to represent a large amount of information : large amount of variables of different types, given generally not by single value but by an interval or a distribution. It is then difficult to give all the information at once. In graphic interface, we choose an interactive approach but sound can help to give some kind of information on demand. We have chosen characteristics which seemed hard to be given visually. 

###### **6.1 The type of axes** 

The variable can be numerical, given by an interval of value, categorical, given by a distribution and non applicable, when the axis is represented but is not used for the present object. 

A warning can be given on the axes type, when selecting an axis. This warning will be given in the form of a musical earcon. Different sounds have then to be designed for each type and must be very distinct. Rhythm chord and timbre will be important elements to improve the disambiguation between sounds 

###### **6.2 Dissimilarity between two symbolic objects** 

When the symbolic objects are represented on a Temporal Star, linked by a central thread representing time or in different windows, like in the Simple Star way, user can be interested to know in which amount the objects differ from each other. 

The first step is to compute a dissimilarity measure between both objects and then to show dissimilarity on the form of a number. 

Process can be lighten if dissimilarities are computed automatically, at the beginning of the session, and given to users, in audio way, on request, by a selection click on both objects. A musical sound will be played, with duration proportional to dissimilarity value. 

In a first approach, we have divided the range of dissimilarity measure into five equal intervals and to map each of these intervals into a sound with proportional number of chords or notes. For example, if the dissimilarity has a value of 3 (in a scale between 1 to 5), three notes or chords are played successively. 

Let us note that sounds for dissimilarity must be very distinct from earcons for axis type. 

###### **6.3 The weight of axes** 

When representing axes in a radial shape, there is no first axis, no last one and axes order is usually arbitrary. When variables are the result of a Principle Component Analysis, they are given with a weight corresponding to the percentage of information (or inertia) explained by each one. This element is important but is usually given in a table, annexed to the graphical representation. 

It could be much more helpful using sound. When moving the cursor over an axis, a sound according to the importance of the axis will be played. The visual display will remain unchanged and the user will not have to shift his focus off the symbolic object. 

Earcons or musical sounds are of different length/height according to the weight of the axis. A mapping between weight and pitch is tried. 

###### **7. ISO3D CHOICE TO GENERATE SOUND** 

Several decisions had to be taken in order to create sound inside ISO-3D software. 

57 

The first step was to make the choice of the type of sonic representation. We have chosen musical sound instead of speech, natural or virtual sound. In preceding paragraphs , we have explained most of the reasons for choosing music but we have to admit that it is also the result of a personal subjective choice. 

The second step concerns the way to create musical sound: to copy sound in wave format and transform it into MP3 standard or to design our original sounds. 

Copying sound to create musical earcons would be like copy parts of paintings to create icons. It would not be well appropriated, not sufficiently flexible, not easy to tune, not master. We then decided to create our own musical sound. 

At the third step, we have to decide who will design the sound. An orchestra ? It is out of our budget ! A musician ? We know some very well. 

The first possibility would be to record (in audio or wave format) and then digitalise and compress the result. This solution needs studio record material. 

An alternative, and it is the solution that we have chosen, consists to use a synthesiser which transforms directly a large variety of sounds into MIDI format files. This solution allows a large range of timbres, tones, which cannot be obtained with a single instrument. It can also generate polyphony. 

The last step concerns hardware/software synthesiser. For our musician, who is pianist, it is much more natural to use keyboard then to tune the sounds on a computer. Moreover, virtual or software synthesiser need still some improvement to have the same quality as hardware synthesiser. The advantage of external production on internal one is that these sounds are easy to integrate in the application and that they are hardware independent, meaning that, no matter the used soundcard is, the sounds produced are the same. The disadvantage is that only few parameters, like balance and loudness, can be modified while using the musical sounds in the application tool. 

To design a more adaptable product, we have decided to offer a library of sounds, with a choice by default (like when you choose your bell ring on your portable telephone or the colour of screen). 

###### **8. ANIMATION** 

Animation of an object can help to understand his evolution along time. 

We have used this technique to show the evolution of an object represented by a Simple Star. Considering, for example, the data of TV audience of a family recorded by minutes, if we superpose quickly the pictures of Simple Star for each minute, we obtain an animated picture which shows the evolution of family preference all along the day. 

###### **9. SOFTWARE DESIGN** 

A first version of the software has been developed using Java 2.0, Open Inventor, 3D-MasterSuite and Java Media Framework 

2.0 (JMF). It runs in a client/server architecture on the web (InfoBus technology). 

OpenInventor is a 3D graphic API using OpenGL standard. 3D-MasterSuite extends and includes Open Inventor and high level 3D graphic classes. We have used the Java version so that , when necessary, objects not available in 3D-MasterSuite can be programmed in Java. 

The JMF is an application programming interface (API) for incorporating media data such as audio and video into Java applications and applets. It is specifically designed to take advantage of Java platform features and supports several audio and video formats. JavaSound has been incorporated into JMF (which has been lately incorporated into Java 1.3). 

The JMF 2.0 API extends the framework by providing support for capturing and storing media data, controlling the type of processing that is performed during playback, and performing custom processing on media data streams. In addition, JMF 2.0 defines a plug-in API that enables advanced developers and technology providers in more easily customising and extending JMF functionality. 

To implement the sound, we had to make a link between Open Inventor and JMF. A special sound object has been implemented. Its task is to: 

- initialise the soundcard 

- to load a sampled file (e.g. WAV) or a MIDI file 

- to play that file 

###### **10. EVALUATION** 

Next step is to evaluate the prototype with the users who provided pilot applications. It will be done for November 2000. These applications are TV Audience in RAI (Italy) and portfolio management in ING (The Netherlands). 

###### **11. ACKNOWLEDGMENTS** 

ISO-3D project is an ESPRIT project sponsored by European Community. Partners come from universities, private companies and a bank. It is a two years project and it started in November 1998. 

Participants: 

Universities : Paris-Dauphine (France), Naples (Italy), Namur (Belgium), Liubljana (Sloveny). 

Companies : Matra System & Information, TGS (France), CISIA (France). 

Bank : ING (The Netherlands) 

Open Inventor environment has been furnished by TGS Company for project duration. 

Many thanks to Adolphe Nahimana and Benoît De Greift who worked hardly on software programming, to Koen Anrijs who designed a first prototype with Java Sound and prepared the state of the art. 

58 

###### **12. REFERENCES** 

- [1] [ALTY95] Alty, J.(1995). _Can we use Music in Computer- Human Communication?_ , HCI 95, UK. 

- [2] [ANRIJS99] Anrijs, K. (1999) _The use of sound in 3D representations of Symbolic Objects,_ Mémoire de Licence en Informatique, Institut d’Informatique, FUNDP. 

- [3] [BISDORFF00] Bisdorff, R.(2000). _Illustrative Benchmark Examples_ , chap. 13 in Bock,H.H., Diday, E., _Analysis of Symbolic Data.Exploratory methods for extracting statistical information from complex data._ , Springer Verlag, Heidelberg, pp 355-385. 

- [4] [BLY85] Bly, S. (1985). _Communicating with Sound,_ Proceedings of CHI'85 Conference on Human Factors in Computing Systems, pp 115-119, ACM. 

- [5] [BOCK&00] Bock, H.H., Diday E.(eds.) (2000). _Analysis of Symbolic Data.Exploratory methods for extracting statistical information from complex data._ Springer Verlag, Heidelberg, pp 54- 75. 

- [6] [BREWSTER&95] Brewster, S.A., Wright, P.C., Dix, A.J. & Edwards, A.D.N. (1995). _The sonic enhancement of graphical buttons_ . In Nordby, K., Helmersen, P., Gilmore, D. & Arnesen, S. (Eds.), Proceedings of INTERACT'95, Lillehammer, Norway: Chapman & Hall, pp. 43-48. 

- [7] [BREWSTER98a] Brewster, S.A. (1998). _Using earcons to improve the usability of tool palettes_ . In Summary Proceedings of CHI98 (Los Angeles, Ca), ACM Press, Addison-Wesley, pp 297-298. 

- [8] [CONVERSY&95] Conversy, S. & Beaudouin-Lafon, M. (1995). _Le son dans les applications interactives_ , Université de Paris-Sud. 

- [9] [KIENTZLE98] Kientzle, T., (1998). _A Programmer’s Guide to Sound,_ Addison-Wesley. 

- [10] [KRAMER94] Kramer, G. (1994). _An Introduction to Auditory Display, Auditory Display: Sonification, Audification, and Auditory Interfaces,_ A proceedings volume of the Santa Fe institute studies in the science of complexity, pp 1-78. 

- [11] [MENNESSIER&98] Mennessier, M.O., Alvarez, R., Noirhomme, M., Rouard, M. (1998) _Physics and Evolution for LPVs from HIPPARCOS Kinematics_ , in IAU191 Symposium, Montpellier. 

- [12] [MEZRICH&84] Mezrich, J.J., Frysinger, S.P. & Slivjanovski, R. (1984). _Dynamic Representation of Multivariate Time Series Data_ , J. Amer. Stat. Assoc. 79,pp 34-40. 

- [13] [NOIRHOMME&98] Noirhomme-Fraiture, M., Rouard, M. (1998). _Visualisation de données multivariés: évaluation de la représentation en étoile zoom_ , in IHM 98, Nantes, pp 121-126. 

- [14] [NOIRHOMME&00] Noirhomme-Fraiture, M., Rouard, M. (2000). _Visualising and Editing Symbolic Objects,_ chap 7 in Bock, H.H., Diday, E. (eds.) _Analysis of Symbolic Data.Exploratory methods for extracting statistical information from complex data._ , Springer Verlag, Heidelberg, pp 125-138. 

59 

### **A self organizing map (SOM) extended model for information discovery in a digital library context** 

###### Jean-Charles Lamirel 

LORIA, BP 239 54506 Vandoeuvre Cedex, FRANCE 33-3-83-59-20-88 lamirel@loria.fr 

Jacques Ducloy Hager Kammoun INIST, LORIA, 2, allée du Parc de Brabois BP 239 54514 Vandoeuvre Cedex, 54506 Vandoeuvre Cedex, FRANCE FRANCE 33-3-83-50-46-00 33-3-83-59-20-88 Ducloy@inist.fr lamirel@loria.fr 

###### **ABSTRACT** 

This paper presents the MicroNOMAD Discovering Tool. Its main characteristic is both to provide an user with emergent analyses of a multimedia database content and with querying and browsing guidelines through the use of an advanced topographic interface model. The model also allows the user to dynamically exploit semantic exchanges between multiple viewpoints on the database. The tool basic principles are firstly described. A tool experimentation which is achieved on the multimedia data-base associated to the BIBAN"Art Nouveau" server is then developed. It clearly demonstrates that the combination of both the topographic structures, the textual and iconographic interaction, and the viewpoint exchanges proposed by the MicroNOMAD core model could play an essential role in several discovering and browsing processes. 

###### **Keywords** 

data visualization, information retrieval 

###### **1. INTRODUCTION** 

Digital Libraries are generally requested to provide access to a large variety of information. As a result, most of DL architectures are issued from Information Retrieval models and are designed to help end-users in retrieving information «he already knows but he has lost a link to». Then, a kernel strategy of many available systems or search engines consists in asking a user to formulate a preliminary query, as an initiate value, and to start an inter-active process of reformulation. From an users point of view there is a risk that he will quickly get lost if he has been too generic or imprecise. We therefore aim at building Information Discovering Systems rather than Information Retrieval Systems. Indeed, we want to give some ways for exploring the knowledge of a corpus. In other words, we would like to answer questions like this: «what is the most important feature in this topic? what’s new? what do I not know in this domain? etc.». We further worked on textual «Digital Libraries» in the framework of two projects dealing with biomedical information: MedExplore and WebStress. These experiences have shown that a complex exploration requires the user to handle a fairly big set of various tools. Moreover, these tools are selected in a «non predictable» order, depending on the intermediate results. Thus, the user needs a fast and global analysis 

© The copyright of this paper belongs to the paper's authors. Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 (O.R. Zaïane, S.J. Simoff, eds.) 

of intermediate data. In that context, images, graphics and iconographic resources have appeared to be a very fundamental component in man-machine interface. For instance, when the system delivers to an user a list of titles, the user needs to read the abstracts to determine whether the topic is relevant or not; let us mention that a fast glance is sufficient on an image to achieve this. To build up our own Information Discovering System turning to account this "outstanding explanatory power" of the images, we have experienced a specific approach which led to the MicroNOMAD Discovering Tool. The core model of that tool strongly derives from the multimap topographic model which has been successfully tested on textual data in the framework of the NOMAD IR System [10]. This latter model, which can be itself considered as a extension of the basic Kohonen topographic map model, enables the user to browse through a documentary database by means of an advanced topographic interface. The MicroNOMAD core model added-value is then mainly to develop a synergy between the browsing and discovering capabilities of the NOMADs original multimap model, on the one hand, and the natural capability of the imbedded Kohonen map model to support at the same time concept mapping and image mapping, on the other hand. In a first part we will briefly describe our previous research. In a second part, we will explain the basics of our new Discovering Tool and we will conclude with experiments on this tool. 

###### **2. THE BIBAN PROJECT** 

BIBAN (Bibliographic and Iconographic and Base Art Nouveau) is a research prototype for iconographic Digital Libraries. BIBAN is an application of a generic XML workbench DILIB [3] and has been designed for investigating Digital Libraries containing images and heterogeneous documents in a multilingual context. BIBAN covers the "Art Nouveau" period, a widespread movement for a renewal of the decorative art at the end of 19th century. BIBAN’s content includes: 

- a set of electronic books in French with their translation in English and German: each book keeps its own style and is implemented as a individual web server (with several HTML pages). One of them is «Nancy and the Art Nouveau Style» [6] which deals with the collections of «Musée de l’Ecole de Nancy». 

- an iconographic base: this base contains a set of images. A metadata record which, coded with an elementary XML schema, is made for each image. 

- a bibliographic base: this base is a subset (300 references) of BHA (Biblographie de l’Histoire de l’Art) selected by «Art Nouveau» or «Ecole de Nancy». This bibliography is connected with a much larger set (6000 references) randomly extracted from the whole BHA. 

All documents are indexed with BHA search entries. Thus, the same description vocabulary is used for images, bibliographic records and pages of electronic books. To this end, each HTML page contains Dublin Core [18] elements. 

60 











**Figure 1: BIBAN context** 

We have put an early version of the BIBAN server on the INTERNET with a limited advertising, mainly intended for information specialists. BIBAN was put on the Web without any kind of assistance, by people with a poor knowledge of the domain. As a result, one important point was raised: the iconographic tools we have provided in this first experiment have been intensively used during browsing and querying steps. Nevertheless, these tools were mainly based on elementary text to image links or image to image links. They appeared to be useful for widening a query but not sufficient for giving a global view of the main topics of a collection and their relationships. We have then implemented a new set of techniques for producing structured iconographic maps. This point will be developed in the further paragraph. 

###### **3. ADAPTIVE MODEL 3.1 Introduction** 

The implementation of the IR process on iconographic databases considering the specificities of the images has been tackled through time with a lot of different approaches. 

On one hand, in some early approaches, as the one proposed in the RIVAGE prototype [2], as well as the one more recently adopted for the first BIBAN prototype, the implementation of the concept of image mosaic or 2D mapping of images has been considered as a convenient way to give the user an overall view of its query results and moreover to help him in its relevance judgments. These approaches rely on the psychological facts that, conversely to textual information, the interpretation and judgment on a relatively large image set could easily be performed in one pass on such a mosaic by an user, without any explicit information on the image content. The early IDIM prototype described by Aigrain and al. [1] has gone one step further on this latter way, proposing a more categorical approach in which the user IR session on a iconographic database is reduced to an user multidirectional browsing through a 3x3 evolutive image mosaic. Conversely to the preceding models, one of the most interesting characteristics of this model is the very exploitation of the 2D structure of the image mosaic for defining different research directions based themselves on different background keywords classification profiles. Nevertheless, the lack of any access to this latter background information often led the user to make arbitrary choice in its browsing. 

On the other hand, the use of alternative profiles like visual indexes for image description has been thoughtfully investigated these latter years [5]. Even if these approaches seem to be promising they surely could not cover all the user needs in an image retrieval process. These points have also been noticed by Duffing and al. [4]. Indeed, their original contribution consists in combining an image classification based on visual indexes and 

another one based on keyword indexes for computing the result of an user query. Unfortunately, their model do not at all rely on an image mosaic approach. 

We found an interesting challenge in the trial of both combining the advantages of all the preceding models (i.e. image mosaic mapping, 2D structure exploitation, and multiple classification use) and dealing with advanced discovery capabilities through a federating approach. We therefore choose to derive our approach, which we called MicroNOMAD, from the topographic multimap model of the NOMAD IR System [9]. The role of the NOMAD’s topographic multimap model is both to provide an user with emergent and «easy to use» analyses of a documentary database contents and with overall querying and browsing guidelines through an advanced topographic interface. Conversely to a lot of other more classical models, the NOMAD model allows the user to exploit dynamic exchanges between multiple viewpoints (i.e classifications) on the database, those being implemented through Said exchanges could be used in several ways. For instance, they enable an user to highlight semantic correlation between different themes belonging to different viewpoints or to indirectly access to documents which may well be unreachable when considering only one viewpoint. They could also be used by a IR system in an automatic mode for elaborated thematic reasoning tasks [10]. To take benefit of the discovering and browsing properties of the NOMAD multimap model in an iconographic context we have mainly based our adaptation of the original model for the MicroNOMAD approach on a parallel implementation of a thematic mapping and of an image mapping on the same maps. 

The basic principles of the multimap model along with these adaptations are presented in the next section. 

###### **3.2 Basic maps construction process** 

The MicroNOMAD basic image classification process is based on the Kohonen topographic map model [8]. This model considers that a data<sup>1</sup> classification can be viewed as a mapping on a 2D neuron grid in which neurons establish predefined neighborhood relation. After the classification process, each neuron of the map will then play the role of a data class representative. The main advantages of the Kohonen map model, as compared to other classification models, are its natural robustness and its very good illustrative power. Indeed, it has been successfully applied for several classification tasks [11] [12] [14] [17]. In our own case, each topographic map is initially built up by unsupervised competitive learning carried out on the whole iconographic database. This learning takes place through the profile vectors extracted from the image descriptions, which describe the characteristics of these images in the viewpoint<sup>2</sup> associated to the map. 

For each neuron of a map _M_ , the basic competitive learning function has the following global form: 



_profile vector) of the neuron n at time t,Wt tn is the external weights profile vector (i.e. the class Pn is the description, considering the viewpoint associated to the map, of the image i chosen as learning sample at time t,_ 

_n_ * _is the winning neuron at time t, that is the neuron_ 

1. For our experiment, the data correspond obviously to the images of the database. 

2. The "viewpoint" notion is an original notion that has been firstly introduced in the NOMAD IR system for playing the role of semantic context of retrieval [10]. In the framework of our image database specific viewpoints have been associated to each specific keywords set of the image description like "Indexer keywords" set, "Title keywords" set or "Author names" set. Other viewpoints could also have been associated to the visual characteristics of the images, if these latter had ever been computed. 

61 

_a(t) a time decreasing function, k(t) a neighborhood adaptation function._ 

The topological properties associated with the Kohonen maps make it then possible to project the original images (i.e. data) onto a map so that their proximity on the map matches as closely as possible their proximity in the viewpoint associated to said map. 

After the preliminary learning phase, each map is organized so as to be legible for the user through analysis of the main components of the neuron profiles. 

that could optimally represent the class contents when the map is displayed to the user. Due to the fact that there is obviously no absolute strategy for achieving that goal (this problem is well known by automatic classification specialists as the "class naming problem") we choose to implement two different kinds of strategies that could be indifferently used during the map consultation phase: 

- _The class driven strategies:_ they consist of attributing to each class a name that represents the combination of the labels of the components having the maximum values in its profile. These strategies are well-suited in highlighting for the user the main themes described by the map. 

- _The member driven strategies:_ they consist of attributing to each class a name that represent the combination of the labels of the components having the maximum values in either the profile of the most representative member of the class or the average member profile computed thanks to all the class member profiles. In this strategies, no name could obviously be attributed to intermediary classes due to the fact that they do not have any associated member. 

   - These strategies are useful in providing the user with complementary information for the map’s themes content interpretation. Indeed, some important information on a theme could be better represented in the theme’s member profiles, than in its related class profile<sup>1</sup> . 

The second phase of the analysis consist in dividing the map into coherent logical areas or neurons groups. Each area, which can be regarded as a macro-class of synthesis, yields a very reliable information on the relative importance of the different themes described by the map. Main themes are represented as larger areas (i.e. with more neurons) than the marginal themes. This "area effect" could also be considered as a very good illustration of the non linear mapping behavior inherent to the original Kohonen classification method. The area computation is based on the topographic properties of the neuron profiles of a Kohonen map [8]. These properties, that are only valid on a reliable map, guaranteeing both the continuity and the locality of the variations of the map neuron profiles, and indeed the closeness of the computed areas on the map. It has been presented in detail in [10]. The figure 3 represents a partial view of a resulting map in its finalized form. One can see that the "image mosaic" effect is obtained by "illustrating" the map thematic structure by the most representative image of each theme. 

###### **3.3 Intermap communication principles** _3.3.1 General principles_ 

The communication between Kohonen maps, that has been first introduced in the NOMAD IR model [9], represents a major amelioration of the basic Kohonen model. In MicroNOMAD, this communication is based on the use of the images that have been projected onto the maps as intermediaries neurons or activity 

> 1. This phenomenon is due to the fact that the class profiles are drawn from the classification process while the member profiles represent a straightforward information from the original data. 

###### transmitters between maps. 

The communication process between maps could be divided in two successive steps: original activity setting on source maps (1) and activity transmission to target maps (2). The original activity could be directly set up by the user on the neuron or on the logical areas of a source map through decisions represented by different scalable modalities (full acceptance, moderated acceptance, moderated rejection, full rejection) directly associated to neurons activity levels [10]. This protocol could be interpreted as the users choices to highlight (positively or negatively) different themes representing his centers of interest relatively to the viewpoint associated to the source map. The original activity could also be indirectly set up by the projection of an users query on the neurons of a source map. The effect of this process will then be to highlight the themes that are more or less related to that query. Therefore, the activity of each map neuron is set up to the value of the cosine measure [15] between the neuron profile and the profile vector associated to the query. The activity transmission to target maps is based itself on two elementary steps: a first transmission step from the activated source map to its associated image neurons (down activation) and a second transmission steps from the activated image neurons to the target maps (up reactivation). 

_T_ The activity _Ai_ of a class i of a target map T derived from the activity of a source map S can be computed by the formula: 



The activity transmission could be considered as a process of evaluation of the semantic correlations existing between themes of a source viewpoint (source map) and themes belonging to several other viewpoints (target maps). The figure 4 represents the result of such a evaluation on the iconographic database "Art Nouveau" considering three different viewpoints (maps). 

###### _3.3.2 Main computation parameters_ 

_"Possibilistic"_<sup>2</sup> _computation of the semantic correlation:_ in this approach each class inherited of the activity transmitted by its most activated associated data. The _f_ function described above can be given as: 



This approach could help the user to detect weak semantic correlation (weak signals) existing between themes belonging to different viewpoints. 

_Probabilistic computation of the semantic correlation:_ in this approach each class inherited of the average activity transmitted by its associated data, either they are activated or not. The _f_ function described above can be given as: 



2. "Possibilistic" is a neologism meaning that our measure is directly related to the measure of possibilitity defined by the possibility theory. 

62 

Conversely to the possibilistic computation, the probabilistic computation give a more reliable measure of the strength of the semantic correlations and may be then used to differentiate between strong and weak matching. 

###### **4. EXPERIMENTATION** 

###### **4.1 Experimental context** 

We carried out a first experiment with the MicroNOMAD Discovering Tool on the iconographic database "Art Nouveau" managed by the BIBAN server. This database contains approximately 300 images related to the various artistic works of the Art Nouveau school. It covers several domains, such as architecture, painting and sculpture. 

The images have associated bibliographic description containing optionally title, indexer keywords and author information. These description are managed by the DILIB workbench in XML format. We choose to use 3 different viewpoints (profiles) in our experiment: • _The "Indexer keywords" viewpoint._ Its is represented by the keywords set used by the indexer in the keyword description field of the images. 

- _The "Title keywords" viewpoint._ Its associated keywords set is build automatically through a basic keywords extraction (use of a stop word list and plural to singular conversion) of image titles. After the keywords extraction a new "Title keywords" field is added to the image description. 

- _The "Authors" viewpoint._ It is represented by the set of authors cited in the image descriptions. 

The first step of the experiment consists in transforming the image description associated to the chosen viewpoints in profiles vectors. For that step, we also choose to apply a classical LogNormalization step [19] in order to reduce the influence of the most widespread words of the profiles. The second step is the original classifications building. Its has been implemented through the classical Kohonen SOMPACK algorithm [17]. The results, which consists in three different classifications associated to the three different viewpoints are then "dressed" and converted to XML format thanks to the DILIB tools. For the sake of portability, the core of the MicroNomad Discovering Tool has been developed as a Java application. Its entries are the XML classification files produced in the preceding step and it implements the class naming strategies, the maps division into logical areas, the map on-line generalization and the intermap communication process described above. 

From a practical standpoint, the MicroNOMAD interface provides the user with several different querying and browsing capabilities: 

- Browsing through the class of the maps in order to access to their main characteristics and to their associated images. 

- Producing queries and afterwards reformulation with a classical querying interface, which nevertheless implements an interesting secondary effect consisting of the projection of the queries on the maps. Indeed, this latter effect could significantly help the user to evaluate the query consistency with respect to the database content: a focalized activity on the map will correspond to a thematically consistent query, a widespread or badly matched activity on the map will correspond to a thematically inconsistent query. 

- Acting on the classes activities in different ways in order to highlight semantic correspondences between viewpoints, to find connotations of a query, to get complementary information on some images, or to retrieve images similar to the ones of a chosen class but being not indexed by the current viewpoint. 

- Collecting image samples in a session memory for all kinds of future operations. 

- Using peripheral tools, like variance and projection tools, for the evaluation of the quality of the classifications and 

   - for estimating the degree of influence of the different 

- Activating links with the BIBAN server pages for highlighting the context of the different artistic works associated to the images. 

The whole experimental context is synthetically described by the figure 2. 



<!-- Start of picture text -->
Viewpoints<br>extraction and<br>normalization<br>BIBAN Server<br>Generation Iconographic<br>XML database Basic topographic<br>classification<br>(SOMPACK + post<br>processing)<br>CGIs Bibliographic  Basic maps<br>XML databases XML MicroNOMAD<br>Java Application<br>Enhanced Maps<br>BIBAN dynamicServer Pages User’s browsing and+<br>querying Interface<br>Hyperlinks<br><!-- End of picture text -->

**Figure 2: Experimental context** 

###### **5. DISCUSSION** 

The first results which were obtained by our model are very promising. Original multiple viewpoints classification approach have directly produced very interesting results proving one more time the relevance of such an approach which tends to reduce the noise which is inevitably generated in an overall classification approach while increasing the flexibility and the granularity of the analyses<sup>1</sup> . In our experiment we found that a "Title keywords" classification can highlight information that is very complementary to the one highlighted by an "Indexer keywords" classification. For instance, in the context of the Art Nouveau database, we found interesting thematic extrapolation capabilities to the "Title keywords" classification, as well as complementary thematic focalization capabilities to the "Indexer keywords" classification. Indeed, crossings domain, like the common works of the Art Nouveau, are well highlighted by the "Title keywords" classification. As for it, "Indexer keywords" classification isolates very precisely the main artistic domains of the Art Nouveau while focusing on the most investigated sub-domains. Thus, the various naturalist metaphors integrated in the "Art Nouveau" works are very precisely described by this latter classification. 

Maps also represent an useful tool for the indexation specialists. They help them in estimating the quality of the indexation of a database. Thanks to the classification method, strong indexation incoherences could be easily highlighted on the map: such incoherences are obvious if themes that specialists judged of equal weight in a domain appear with strongly different surface areas on a map. One example of such an incoherence that has been found by a specialist is the exaggerated representation of the Butterfly ("Papillon") theme, regarding to the Insect ("Insecte") theme, on the map of the figure 3. 

After experimentation with several users, the opportunity to have simultaneously images and coherently organized textual information on the same support (map) seems to be definitely of great utility. Classification results interpretation are really made easier by the presence of images, as well as text represent a good 

1. See [LAM 95] for another experimental and theoretical justification on that point. 

63 

help in the choice of reliable browsing points in the iconographic database. The model on-line generalization capabilities and its ability to derive the map description context in several ways could also significantly help the user in its database contents interpretation and browsing. 

Thanks to the user opinion, the intermap communication process appears to be a very interesting and original feature of the model. It provides the system with a new capability that could be called a dynamic and flexible browsing behavior. Conversely to classical browsing mechanism, like hypertext links, the browsing effect could then be directly tied to the users information and explanation needs (see figure 4). Moreover, the number and the type (i.e. concurrent or complementary) of viewpoints that could be simultaneously used is not limited by the model. For example, one can easily add a new map representing a classification based on "visual indexes" extracted from the images. These last properties could led us to consider our approach as a good basis for building an intelligent multimedia discovering system that could be used for various discovering and analysis tasks, especially for the ones which are strongly tied to image interpretation. Indeed the model is now tested in two important applications: 

- Interactive browsing through museum database and intelligent setting up of exhibitions in the framework of the technical collection of the french "Musée de la Villette". 

- • Management of multiple classifications of butterflies (colour, shape, ...) in the Taiwanese NSC Digital museum of butterflies [7]. 

###### **6. CONCLUSION** 

The MicroNOMAD Discovering Tool development represents obviously a important step for providing an Iconographic interface to Digital Library Server with a high level of interactivity. We have said that the first reactions we received in demonstrating it in the BIBAN server context were very encouraging. Nevertheless, we have still a lot of work to do if we want to put such an interface on the Internet or to produce a tool allowing anyone to build this kind of application. The basic browsing and querying capabilities of our Tool seem to be well-suited for over-all browsing and querying tasks, whatever are the users abilities. Nevertheless, a real challenge comes from the relative difficulty for the non specialists of precisely analyzing the classification results that are produced by the Tool (and working on them). As shown in this paper, sophisticated tools give better hypothesis but they are more difficult to validate. Thus, in a «BIBAN like» context, we think that we will have to provide three different ways, depending of the user profile. People who just want to surf in a «tourist approach» will be more confident in a pre-computerized map which will give them a lot of paths to explore. On the opposite, specialists in classification models who want to investigate in a precise strategy could use a dynamic interface, closer to our present prototype. Another problem comes from domain specialists which want to get effective results by a deeper exploitation of both the expressive and the discovering power of the MicroNOMAD Tool but which are not familiar with neural theories and their background behavior: the MicroNOMAD multimap core model will be very useful to them in proposing new assumptions but we will have to connect him with very simple tools enabling non classification specialists to verify these assumptions. For that goal, we planned to interface our model with such a simple validation tool based on gallois lattice and dealing with logical inference [16]. In this way, our programing approach based on XML interfaced components will be very useful in declining various implementations from one model. 

As the dimensions of the topographies processed by our system are not "à priori" limited, we are also planning to make use of rather strongly multidimensional topographies in order to represent much better some complex data relations<sup>1</sup> . In order to interpret this relations, the user will then be provided with multiple 2D projections of a same multidimensional topography. 

###### **7. REFERENCES** 

- [1] Aigrain P. and Longueville V. A Connection Graph for User Navigation in a Large Image Bank, in Proc. RIAO, Vol. 1, p. 25–44, Barcelona, Spain, avril 1991. 

- [2] Créhange M. and Halin G. Machine Learning and Vectorial Matching for an Image Retrieval Model, in Proc. SIGIR, p. 99–114, 1990. 

- [3] Ducloy J. DILIB, une plate-forme XML pour la génération de serveurs WWW et la veille scientifique et technique, in Le Micro Bulletin Thématique, No. 3, april 99. 

- [4] G. An alternative image retrieval system based on visual and thematic corpus organisation, in Proc. ICMCS, Florence, Italia, 1999. 

- [5] El Kwae E. and Kabuka M.R. A robust Framework for Content-Based Analysis Retrieval by Spatial Similarity in Images Database. ACM TOIS, Vol. 17, No. 2, april 1999. 

- [6] Gnaedig I. & al. Nancy et l’Art Nouveau, http:// www.biban.fr/AN96 (restricted use). 

- [7] Hong J. & al. A digital museum of Taiwanese in Proc. ACM/DL 00, San Antonio, Texas, june 2000. 

- [8] Kohonen T. Self-Organisation and Associative Memory. Springer Verlag, New York, USA, 1984. 

- [9] Lamirel J.C. and Créhange M. Application of a symbolicoconnectionist approach for the design of a highly interactive documentary database interrogation system with on-line learning capabilities, in Proc. ACM-CIKM 94, Gaitherburg, Maryland, november 94. 

- [10] Lamirel J.C. Application d’une approche symbolicoconnexionniste pour la conception d’un système documentaire hautement interactif. PhD, Université de Nancy, France, november 95. 

- [11] Lin X., Soergel D. and Marchionini G. A Self-Organizing Semantic Map for Information Retrieval, in Proc. SIGIR, Chicago, USA, 1991. 

- [12] Martinetz T.M. and Schulten K.J. Topology Representing Networks. Neural Networks, 7 (3) : 507-522, 1994. 

- [13] Michelet B. L’analyse des associations. PhD, Université de Paris 7, Paris, France, october 1988. 

- [14] Orwig E., Chen H. and Nunamaker Jr J. F. A graphical, Self Organizing Approach to Classifying Electronic Meeting Output.JASIS, 48 (1): 157-170, 1997 

- [15] Salton G. The SMART Retrieval System: Experiments in Automatic Document Processing. Prentice Hall Inc., Englewood Cliffs, NJ, USA, 1971. 

- [16] SimonA. and Napoli A. Building Viewpoints in an ObjectBased Representation System for Knowledge Discovery in Databases, in Proc. IRI-99. 

- [17] 

- [18] Weibel S. L., Stuart L. and Miller E. J. Dublin Core Metadata Element Set Reference Page, http://purl.oclc.org/metadata/ dublin_core 

- [19] Wilbur W.J. and Coffee L. The Effectiveness of Document Neighboring in Search Enhancement. Information Processing and Management, 30 (2) : 253-266, 1994. 

1. A straightforward example of such relation is a relation between several authors which is impossible to clearly describe on a 2D map. 

64 

###### **8. APPENDIX : MAPS** 





<!-- Start of picture text -->
5) Center of gravity<br>of the logical area<br>(symbolized by an<br>external thin circle<br>on one specific neu-<br>ron of the area) =<br>neuron whose pro-<br>file is the nearest to<br>the average profile<br>of the area.<br>1) Class neuron<br>presented jointly<br>with its best associ-<br>ated image or class<br>member. The other<br>images associated to<br>the class neuron can<br>be accessed through<br>the map interface.<br>4) Logical area =<br>group of neurons<br>with the same profile<br>dominances.<br>2) Class neuron<br>without members<br>also called interme-<br>diary neuron.<br>3) Class label or<br>name considering<br>the current naming<br>strategy.<br><!-- End of picture text -->

**Figure 3: Map example** 

_Partial view of a topographic map of 12 x 12 neurons (i.e. classes). The map is initially organized as a square 2D grid of neurons. The profile of the classes are then generated through an unsupervised competitive learning carried out on the profiles of 300 images of the BIBAN iconographic database considering one specific viewpoint. The viewpoint chosen for the showed map is the "Indexer keywords" viewpoint, with represents the bibliographic description of the images made by indexers (for more details, see Experimentation section).The names of the classes illustrate the themes (considering the chosen viewpoint) that have been highlighted by the learning. After the learning, the neurons related to the same themes have been grouped into coherent areas thanks to the topographic properties of the map. The number of neurons of each area can then be considered as a good indicator of the theme weight in the database. Considering, on the one hand, that themes or areas near one to another represent related notions and, on the other hand, that images, which represents the learning data, have been associated to their nearest classes on the map, the map could be considered both as a analysis tool and as a navigation mosaic with a semantically coherent organization._ 

65 







**Figure 4: Intermap communication example** 

_When navigating on a single map like an "Authors" map, the user can have a view of an author main works and of its main collaborations. When exploiting the communication between this "Authors" map and different thematic maps (here an "Indexer keywords" map and a "Title keywords" map) he can highlight the author various influence on the main thematic areas of the Art Nouveau, and moreover, its main artistic skills (see Experimentation section for more detailed descriptions of the "Author", "Indexer keywords" and "Title keywords" viewpoints)._ 

_For the sake of readability of these activities on the maps, the "Image display" mode has been switched off on the "Indexer keywords" map. and on the "Title keywords" map._ 

66 

### **Learning Feature Weights from User Behavior in Content-Based Image Retrieval** 

David McG Squire Computer Science and Software Engineering Monash University Melbourne, Australia 

Henning M¨uller, Wolfgang M¨uller, David McG Squire St´ephane Marchand-Maillet, Thierry Pun Computer Science and Software Engineering Computer Vision Group, University of Geneva Monash University 24 Rue du G´en´eral Dufour, Melbourne, Australia CH-1211 Gen`eve 4, Switzerland henning.mueller@cui.unige.ch **ABSTRACT** knowledge obtained from older query steps of the same sesThis article describ es an algorithm for obtaining knowledge sion or of other query sessions is forgotten. Often, the feedab out the imp ortance of features from analyzing user log back is limited to one p ositive image [16] or several p ositive �les of a content-based image retrieval system (CBIRS). The feedback images [4]. Only few systems o�er b oth p ositive user log �les from the usage of the Viper web demonstration and negative feedback as Sur�mage [6, 27] and Viper [26]. system are analyzed over a p erio d of four months. Within Even these systems often have problems with to o much negathis p erio d ab out 3500 accesses to the system were made tive feedback as describ ed in [11], although solutions similar with almost 800 multiple image queries. All the actions of to those already used in text retrieval (TR) [17] exist. the users were logged in a �le. Image browsers like PicHunter [5] o�er the p ossibility to The analysis only includes multiple image queries of the syshave feedback over more than one step and thus to really tem with p ositive and/or negative input images, b ecause learn from the user interaction in order to �nd one target only multiple image queries contain enough information for image. Using a sequence of queries to discover the user's the metho d describ ed. Features frequently present in imgoal creates another problem whenever the user changes the ages marked together p ositively in the same query step get goal of a query in the querying pro cess. Solutions to this a higher weighting, whereas features present in one image problem referred to as \moving targets" are given in Trackmarked p ositively and another image marked negatively in ingViper [13]. the same step get a lower weighting. The Viper system offers a very large numb er of simple features. This allows the Yet,et, existing learning algorithms mostly try to �nd out the creation of �exible feature weightings with high values for goal of a user oververer one or a few feedbackk steps. Minkaa [10] imp ortant and low values for less imp ortant features. These prop oses across-session learning for FourEyesourEyes in PhotoBook.ok.. weightings for features can of course di�er b etween collecIn [8], an approachh to cluster images markeded together p ositions and as well b etween users. The results are evaluated tivelyely and divide images markeded negativelyely from the clusters with an exp eriment using the relevance judgments of real is explained. In the domain of colol laborativeorativeative �ltering [7], user users on a database containing 2500 images. The results of judgmentsts havevee b een used to prop ose new items to users the system with learned weights are compared to the system based on items b eing markeded together p ositivelyely byy other without the learned feature weights. users. This has b een applied to art images of a museumuseum as wellell [1]. The searchh for user preferences byy giving p ositivee **Keywords** and negativee examples for webeb pages has also b een studied long term learning, log �le analysis, content-based image [15]. Bayesianyesianesian networksworksorks havevee b een used to �nd out if an retrieval, web usage analysis, multimedia retrieval unknownwn page mightt �t to the users' pro�le or not. This sup ervised learning is out of the scop e of this pap er as wee wantantt to use unsup ervised learning techniqueshniques to avoidvoidoid additional **1. INTRODUCTION** workork for the user. Wee also wantantt to learn information for Much has b een written ab out Relevance Feedback (RF) in new queries and not just improvevee one already knownwn query content-based image retrieval (CBIR) [18]. Most feedback byy augmentingting imp ortantt features. metho ds only takes into account one query step and the In the domain of electronic commerce, log �les resulting from web usage have b een analyzed for a long time and the knowledge from this analysis is employed to improve new systems and to adapt them to the users' needs [28]. Part of © The copyright of this paper belongs to the paper's authors. Permission to copy without this research concentrates on analyzing the b ehavior of users fee all or part of this material is granted provided that the copies are not made or within webpages and the links they use [2]. In the domain distributed for direct commercial advantage. Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), of electronic commerce, there are many di�erent concepts to in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 identify users and track their activities, but problems arise (O.R. Zaïane, S.J. Simoff, eds.) with p eople just trying out pages and making very short 

Yet,et, existing learning algorithms mostly try to �nd out the goal of a user oververer one or a few feedbackk steps. Minkaa [10] prop oses across-session learning for FourEyesourEyes in PhotoBook.ok.. In [8], an approachh to cluster images markeded together p ositivelyely and divide images markeded negativelyely from the clusters is explained. In the domain of colol laborativeorativeative �ltering [7], user judgmentsts havevee b een used to prop ose new items to users based on items b eing markeded together p ositivelyely byy other users. This has b een applied to art images of a museumuseum as wellell [1]. The searchh for user preferences byy giving p ositivee and negativee examples for webeb pages has also b een studied [15]. Bayesianyesianesian networksworksorks havevee b een used to �nd out if an unknownwn page mightt �t to the users' pro�le or not. This sup ervised learning is out of the scop e of this pap er as wee wantantt to use unsup ervised learning techniqueshniques to avoidvoidoid additional workork for the user. Wee also wantantt to learn information for new queries and not just improvevee one already knownwn query byy augmentingting imp ortantt features. 

67 

visits. Longer visits can b e analyzed to facilitate the design **2.3 Weighting schemes** of a web page. We have implemented several weighting schemes known from the TR literature [21]. They are all based on the collection The quality of user data gained from the internet might and do cument frequencies of the features. For the exp erinot b e the highest. Nevertheless, we can learn from the ments in this pap er, we use the inverse document frequency usage information, and the related analysis in this pap er weighting, which weights the features in the following way: shows that we can get qualitatively and quantitatively b etter results, even by using p otentially p o or web user data. N **2.** The Vip **THE** er systemVIPER **SYSTEM** is a CBIRS that is describ ed in more relevance j = N1 Xi=1 (tf ij � Ri ) � l og 2 � cf1i � ; (1) detailfrom TRin [23,applications24]. The andsystemaimsusesat incorpmany oratingtechniquesthemknoinwnto score k q = X (tfk j � relevance j ) ; (2) j the domain of CBIR. where tf is the term frequency of a feature, cf the col lection **2.1 System Architecture** frequency of a feature, j a feature number, q corresp onds to The main di�erence compared with other systems is the a query with i = 1::N input images, k is one result image presence of a very large numb er of more than 85000 p osand Ri is the relevance of an input image i within the range � sible features. Most images contain b etween 1000 and 2000 [ 1; 1]. of theses features. The access metho d to the features is the inverted �le, which is the most common access metho d used We can see in Equation 1 that the �nal result mainly dein TR. Thus, Viper allows a fast and eÆcient access to the p ends on the collection frequency of a feature. Rare features large numb er of features [12]. are weighted high, whereas features very common in the collection are weighted low b ecause they contain less informaThe emphasis of the pro ject is on user interaction. Hence, tion. The term frequency of a feature in the input images it emb eds several interaction strategies using several steps has a has a minor in�uence. We can see in Equation 2 that of p ositive and negative feedback. Both online and o�ine b esides the relevance factor for a feature, the term frequency learning are employed in the system. Viper o�ers a go o d of the feature in the resulting image has a small in�uence �exibility for learning as it has a very large numb er of feaon the �nal score. tures for the creation of feature weights. Esp ecially the extensive use of negative feedback has shown to b e very e�ec- **3. LEARNING FEATUREWEIGHTSFROM** tive [11] and is also very imp ortant for the long term learning **USER BEHAVIOR** approach in this pap er. Reference [26] p oints to the web demonstration of the CBIRS Viper we used for this study. Every time a user accesses this **2.2** Viper **Features** page and do es an action, it is logged with a time stamp. Like The system used for this study implements four di�erent this, we can always see what the user did and which probgroups of image features: lems he might have encountered with the system. This also o�ers the p ossibility to make an o�ine analysis of the data � A global color histogram based on the HSV color space to b etter suit the information needs of a user. The host which corresp onds roughly to the human color vision [22]; name of the user is also saved, but no other private data. � lo cal color blo cks at di�erent scales for �xed regions by using the mo de color for each of the �xed blo cks; **3.1 Analyzing the Log Files** the image is successively partitioned into four equally This section gives a general overview of the data we logged sized blo cks and each blo ck is partitioned again four into a �le. Between Septemb er 1999 and January 2000, we times; had 3500 accesses to the system. Ab out half of the accessors just lo oked at random or sorted image sets or watched the � global texture characteristics are represented by the parameters, but ab out 1700 accesses actually were queries. histograms of the resp onse to gab or �lters of di�erent This shows that many p eople visited the page, but a large frequencies and directions; gab or �lters are known to numb er of them just played around with the system. This b e a go o d mo del for the human p erception of edges [9]; can b e con�rmed with the fact that only 24 of the 201 hosts � lo cal Gab or �lters at di�erent scales and regions by uswhich accessed the system had more than 20 actions with ing the same blo cks as for the lo cal color features and the system. Ab out 40 p ercent of the queries came from applying Gab or �lters with di�erent directions and fredi�erent hosts within the University of Geneva. Of the 1700 quencies to these blo cks. queries, 786 where multiple image queries. Only multiple image queries contain enough information for the algorithm we want to employ. 

These features are only low level features, but b ecause of the high numb er, very complex queries can b e constructed In the log �les, the query data from 10 di�erent databases with them. Higher level features like image regions may is regarded. It is hard to map the imp ortance of features provide b etter results, but we still su�er from the semantic from one database to another database although they use gap b etween the semantics the user is lo oking for and the the same set of features. The distribution of the features visual content the system can o�er. actually present in the database is very di�erent for every 

68 

T�el�evision Suisse Romande (TSR) b ecause our user exp erTable 1: The di�erent functions of the system and iments are based on this database. For the TSR database, their usage statistics in the web demonstration we had 3.800 image pairs and 1.02 million feature pairs (0.47 Chose Database 668 times million p ositive and 0.55 million negative), which represents Browse Image Names 251 times ab out 10% of all the accesses to the system. Image Queries 1586 times Random Images 586 times Features with a very high collection frequency like the hisChange Options 114 times togram features o ccur ab out the same time as p ositive and Clear Judgments 100 times negative pairs. Hence, their resp ective weight should stay very similar as b efore. database. Only the histogram features for color and texThe additional factor we want to calculate should b e in the ture are present in a very large numb er of images in every database. range of [0; 2] to allow p o or features to disapp ear completely and go o d features to b e weighted signi�cantly high. Features From the log �les, we could also analyze the problems the which o ccur only negatively should have a value of zero and user had with our system. Several p eople did queries withfeatures which o ccur only p ositively should have a value of 2. out marking any image as relevant. As a result, we inserted a comment telling the user that at least one image needs to This leads to the following simple formula for the additional b e marked. Another problem encountered while analyzing factor factor j : the log �les was related to using to o much negative feedback. This can as well remove all the imp ortant features from the factor j = 1 + pj � nj ; (4) query and lead to bad results. We therefore implemented pj + nj pj + nj a mo di�ed version of Ro cchio's formula [17] for separately weighting p ositive and negative relevance feedback [11]. where j is the feature numb er, pj then numb er of p ositive marks for feature j and nj the numb er of negative marks. **3.2 Learning from Log Files** The two rationales for our learning algorithm are: The new weighting formula for a feature is basically the same as it was b efore with only the additional factor from Equation 4 b eing calculated and included into Equation 1 � Features which o ccur often in two images marked toas can b e seen in Equation 5. gether p ositively in the same query step should have a higher weighting than others; � features which o ccur often in images marked once p osN itivhavee anda lowonceweighnegativting. e in the same query step should relevance j = f actorj � N1 Xi=1 (tfij � Ri ) l og 2 � cf1i � : (5) Based on these principles, we identi�ed all pairs of images marked together. Queries with two input images just have Because improvements were lower than exp ected for the one pair, whereas queries with three images have three and queries with relevance feedback (see Figure 2), we implequeries with four images have six. Thus, the numb er of mented a second factor similar to the factor in Equation 4 image pairs in a query with n images is: for comparison. We think that a complete disapp earance of p o or features might reduce the p ossibility to move in feature space, an e�ect which is stronger visible in feedback queries. number of image pairs = n � (n2 � 1) : (3) canHence,onlywereacimplemenh a minimteduma factorof 0:25,wherewhereasthe negativthe maxime valueum factor can b e up to four, when only p ositive marks o ccur. If p ositive and negative marks o ccur with the same frequency, imageTheb oth 786negativpairsmultiplemarkely, theedimagetogether.imagequeriespairIf isimagesleaddiscarded,toaremoremarkas thisthaned together,do31.000es not bthedi�ereny rescalingfactort wastaytheysas canatp ositivone.b e eseenTheandinresultingnegativEquatione partsfactor26. ofj factoris obtainedj in a contain much information. Images can b e marked together negativnegativeelyinforcommon.di�erent reasons and may not have anything 8 0:25 + factor0:75 j : factor j < 1 factor2 j = < 1 : factor j = 1 (6) We then analyzed which features the two images of a pair : 1 + (factor j � 1) � 3 : factor j > 1 have in common. Positive image pairs lead to a p ositive mark for the features they have in common and negative For the calculation of the weight, factor2 j is used in exactly image pairs to a negative mark. Negative pairs have in the same way as factor j in Equation 5. general a smaller numb er of features in common. On average the image pairs have slightly more than 300 features The fact that there are slightly more pairs marked together in common. In total, the 31.000 image pairs lead to 10 milp ositively than there are negative pairs may lead to a diflion feature marks (6.1 million p ositive and 3.9 million negferent quantization of p ositive and negative parts, but do es ative). We separately analyzed the image database of the not alter the quality of the results. 

69 

**4. EXPERIMENTAL RESULTS** When we use the factor learned from all the di�erent databases, To analyze the success of this metho d, we use a user exthe results are ab out 3% to 5% b etter than without the p eriment p erformed in [12]. This includes a very heterogelearned factor. We think that this improvement was only neous database of 2500 images from the T�el�evision Suisse small b ecause the additional factor can b ecome 0 for bad Romande (TSR). 14 queries were presented to 3 users for features which limits the �exibility to move in feature space. relevance judgments. The users had to mark all the images As a consequence, we rep eated the exp eriments with a secin the database they regard as b eing similar to each of the ond factor explained in Equation 6. 14 query images. Interestingly, the result sets for each user di�er strongly in size and also in the images b eing selected. Version with factor=1 Similar e�ects were already rep orted in [25]. 1 With learnt factor of TSR databaseWith learnt factor of all databases To evaluate the p erformance, we use precision/recall (PR) 0.8 graphs which are the standard evaluation metho d in TR [19] and are more and more used in CBIR [24]. The results shown b elow are the PR graphs averaged over the relevance 0.6 sets of all users and all queries from the user exp eriment. To simulate relevance feedback based on the user judgments, we used the algorithm explained in [11]. We feed back all 0.4 images the user regards as relevant and which are in the �rst 20 images the system returns for the initial query. 0.2 The training data is only taken from the usage of the web demonstration system and do es not have any connection 0 with the user exp eriment we p erformed. 0 0.2 0.4 Recall 0.6 0.8 1 We see in Figure 1 that the results of the system with the adFigure 2: PR-Graph for a system with and without ditional factor are up to 10% b etter than the original graph a learned factor (with feedback). when all queries of the same database (TSR) are used to calculate the weights. Using all queries of all the di�erent Figure 3 compares the results obtained using the two facdatabases still gives an improvement of 7% to 8%, but only tors, resp ectively learned on the queries of the TSR database in the b eginning of the graph. The overall improvement is and learned with all databases. We can see that the results lower when using the data of all databases. with the second factor are in b oth cases b etter for factor2 j . The b eginning part of the graphs is almost identical, but in Version with factor=1 the middle parts of the graph the results improve with the 1 With learnt factor of TSR database second factor. With learnt factor of all databases 0.8 With learnt factor 1 of TSR database 1 With learnt factor 2 of TSR database With learnt factor 1 of all databases With learnt factor 2 of all databases 0.6 0.8 0.4 0.6 0.2 0.4 0 0 0.2 0.4 0.6 0.8 1 0.2 Recall Figure 1: PR-Graph for a system with and without 0 0 0.2 0.4 0.6 0.8 1 a learned factor (without feedback). Recall In Figure 2, we can see that the results of the �rst feedback Figure 3: Comparison of the two di�erent weighting step are much b etter (up to 100% in the middle parts) than factors (without feedback). the results b efore feedback (compare Figure 1). An improvement in the b eginning of the graphs is esp ecially imp ortant Figure 4 shows a comparison of the results obtained using b ecause this part represents the images the user actually the two factors for the queries with feedback. Here, we can views. The results with the learned factor are signi�cantly clearly see the improvements of factor2 j compared to factor j b etter than without the factor, even on this high level. This of up to 7%, esp ecially in the middle parts of the graph. shows that the gain with the additional f actorj is not just This shows that it might b e b etter to let the factor always limited to one query step as it favors image pairs already b e ab ove zero to not reduce the mobility in feature space. marked together. The small drop o� in the b eginning of the curve for factor2 j 

70 

can b e explained with one query with only very few features mostly true when the feature imp ortance is learned on the and basically no textures, where the �rst returned image same database. In this case, the results are very go o d. was non-relevant. Much b etter results will b e p ossible once the data is obtained from serious users and even b etter if the study is restricted With learnt factor 1 of TSR database 1 With learnt factor 2 of TSR database to a certain domain or a certain user. Like this sp eci�c With learnt factor 1 of all databases With learnt factor 2 of all databases user pro�les or group pro�les can b e learned. We prop ose a hierarchy of learned feature weightings on a user, domain 0.8 and global level. 0.6 Besides the learning of a feature weight for future queries we can evaluate the usefulness of features. This can also b e used for the creation of new features. New features can b e 0.4 extracted for the old images and can directly b e evaluated by using this metho d with the old log �les. 0.2 More work needs to b e done on �nding an optimal factor to calculate a feature weight. We only prop osed a very 0 simple factor without any optimization. Another promis0 0.2 0.4 Recall 0.6 0.8 1 ing approach is to not only analyze pairs of images marked together, but directly evaluate multiple image queries by Figure 4: Comparison of the two di�erent weighting lo oking at all the images marked in a query. Features confactors (with feedback). tained in n > 2 images marked together in the same query step should for example get a much higher weighting than features only contained in two images. We also made some exp eriments where we tried to learn f actorj based on feedback queries p erformed on a com- **6. REFERENCES** pletely di�erent database. The results were basically the [1] Active web museum. same as without learning. The results using all the feedback http://abyss.eurecom.fr:1111/ AWM/login.html, from every database show clearly that not much feedback 2000. of the same database is necessary to improve the results of a query. Feedback from other databases do es not change [2] B. Berendt and M. Spiliop oulou. Analysis of the results much as the feature space is only very sparsely navigation b ehaviour in web sites integrating multiple p opulated and the databases p opulate di�erent areas of the information systems. VLDB Journal: Special Issue on feature space. Databases and the Web - to appear, 2000. We see that calculating weights from user log �les brings [3] IEEE Workshop on Content-based Access of Image strong improvements, esp ecially, when the factor is learned and Video Libraries (CBAIVL'99), Fort Collins, based on queries of the same database. Learned over all Colorado, USA, June 22 1999. queries and all databases, the improvement was not ex[4] Compass web page. http://compass.itc.it, 2000. tremely strong, but clearly visible. De�ning a user pro�le for learning could bring even stronger improvements, esp e- [5] I. J. Cox, M. L. Miller, S. M. Omohundro, and P. N. cially if the user is often p erforming similar search tasks. Yianilos. Target testing and the PicHunter Bayesian Therefore, we prop ose to have a hierarchy of factors, cormultimedia retrieval system. In Advances in Digital resp onding to a user, a domain and a global factor to b e Libraries (ADL'96), pages 66{75, Library of Congress, learned. To do this, a user identi�cation needs to b e inWashington, D. C., May 13{15 1996. serted into the log �le. [6] Sur�mage web demo. http://www-rocq.inria.fr/ cgi-bin/imedia/surfimage.cgi, 1999. **5. CONCLUSIONS AND FURTHER WORK** In this pap er, an approach is presented on how to learn the [7] A. Kohrs and B. Merialdo. Clustering for collab orative imp ortance of features in CBIR from log �les containing user �ltering applications. In Proceedings of the b ehavior of a web demonstration system. The problems of International Conference on Computational log �les on the web is of course that we do not know much Intel ligence for Model ling Control and Automation, ab out the quality of the user data. Many p eople may come Vienna, Austria, February 1999. IOS Press. to a web page to try out the system and to see how it reacts [8] C. S. Lee, W.-Y. Ma, and H. Zhang. Information and might even challenge the system with inconsistent data. Emb edding Based on User's Relevance Feedback for This means that we can not always learn much from this Image Retrieval. In Panchanathan et al. [14]. (SPIE kind of data. With the prop osed approach, artifacts can b e Symp osium on Voice, Video and Data minimized as combinations of image pairs with high feature Communications). similarity have much more imp ortance than image pairs with low feature similarity. The exp eriments with the factors we [9] W. Y. Ma, Y. Deng, and B. S. Manjunath. Too ols for use show that, even with this kind of data, a signi�cant textureand color-based searchh of images. In B. E. improvement in retrieval quality can b e reached. This is Rogowitzwitz and T. N. Pappas,appas, editors, Human Vision 

- [9] W. Y. Ma, Y. Deng, and B. S. Manjunath. Too ols for textureand color-based searchh of images. In B. E. Rogowitzwitz and T. N. Pappas,appas, editors, Human Vision 

71 

- and Electronic Imaging II, volume 3016 of SPIE [22] J. R. Smith and S.-F. Chang. VisualSEEk: a fully Proceedings, pages 496{507, San Jose, CA, February automated content-based image query system. In The 1997. Fourth ACM International Multimedia Conference and Exhibition, Boston, MA, USA, Novemb er 1996. 

- [10] T.fromMinkusera. inAnteraction.image databaseMaster'sbrothesis,wser MITthat Medialearns [23] D. M. Squire, H. Muller,� and W. Muller.� Improving Lab oratory, 20 Ames St., Cambridge, MA 02139, 1996. resp onse time by search pruning in a content-based image retrieval system, using inverted �le techniques. 

- [11] H. Muller,� W. Muller,� D. M. Squire, In CBAIVL99 [3], pages 45{49. S. Marchand-Maillet, and T. Pun. Strategies for � � p ositive and negative relevance feedback in image [24] D. M. Squire, W. Muller, H. Muller, and J. Raki. retrieval. In Proceedings of the 15th International Content-based query of image databases, inspirations Conference on Pattern Recognition (ICPR 2000), from text retrieval: inverted �les, frequency-based Barcelona, Spain, Septemb er 2000. IEEE. weights and relevance feedback. In The 11th Scandinavian Conference on Image Analysis 

- [12] H. Muller,� D. M. Squire, W. Muller,� and T. Pun. (SCIA'99), pages 143{149, Kangerlussuaq, Greenland, EÆcient access metho ds for content-based image June 7{11 1999. retrieval with inverted �les. In Panchanathan et al. [25] D. M. Squire and T. Pun. Assessing agreement 

- [14]. (SPIE Symp osium on Voice, Video and Data b etween human and machine clusterings of image Communications). databases. Pattern Recognition, 31(12):1905{1919, � � 1998. 

- [13] W. Muller, D. M. Squire, H. Muller, and T. Pun. Hunting moving targets: an extension to Bayesian [26] Vip er web demo. web page: http://viper.unige.ch/, metho ds in multimedia databases. In Panchanathan 1999. et al. [14]. (SPIE Symp osium on Voice, Video and Data Communications). [27] A. Winter and C. Nastar. Di�erential feature distribution maps for image segmentation and region 

- [14] S. Panchanathan, S.-F. Chang, and C.-C. J. Kuo, queries in image databases. In CBAIVL99 [3], pages editors. Multimedia Storage and Archiving Systems IV 9{17. (VV02), volume 3846 of SPIE Proceedings, Boston, Massachusetts, USA, Septemb er 20{22 1999. (SPIE [28] K.-L. Wu, P. S. Yu, and A. Ballman. Sp eedtracer: A Symp osium on Voice, Video and Data web usage mining and analysis to ol. IBM Systems Communications). Journal on Internet Computing, 37(1), 1998. 

- [15] M. Pazzani and D. Billsus. Learning and revising user pro�les: The identi�cation of interesting web sites. Journal on Machine Learning, 27:313{331, 1997. 

- [16] QBICTM { IBM's Query By Image Content. http://wwwqbic.almaden.ibm.c om/~q bic/ , 1998. 

- [17] J. J. Ro cchio. Relevance feedback in information retrieval. In The SMART Retrieval System, Experiments in Automatic Document Processing [20], pages 313{323. 

- [18] Y. Rui, T. S. Huang, M. Ortega, and S. Mehrotra. Relevance feedback: A p ower to ol in interactive content-based image retrieval. IEEE Transactions on Circuits and Systems for Video Technology, 8(5):644{655, Septemb er 1998. (Sp ecial Issue on Segmentation, Description, and Retrieval of Video Content). 

- [19] G. Salton. Evaluation parameters. In The SMART Retrieval System, Experiments in Automatic Document Processing [20], pages 55{112. 

- [20] G. Salton. The SMART Retrieval System, Experiments in Automatic Document Processing. Prentice Hall, Englewo o d Cli�s, New Jersey, USA, 1971. 

- [21] G. Salton and C. Buckley. Term weighting approaches in automatic text retrieval. Information Processing and Management, 24(5):513{523, 1988. 

72 

### **When image indexing meets knowledge discovery** 

###### Chabane Djeraba 

IRIN, Ecole Polythechnique de l’Université de Nantes, 

2 rue de la Houssinière, BP 92208 - 44322 Nantes Cedex 3, France 

E-mail : djeraba@irin.univ-nantes.fr 

###### **ABSTRACT** 

In our paper, we deal with the challenge of extending automatically the classic image indexing by visual relationship features. The visual relationship features are discovered automatically from images. They contribute to make more efficient the content-based indexing. More particularly, we develop an advanced content-based indexing articulated around the following notions : - classic indexing, - clustering algorithm, - visual feature book and relationship qualification. 

###### **Keywords** 

Image, Indexing, retrieval, content, similarity, knowledge discovery, relations. 

###### **1. INTRODUCTION** 

In large image databases, finding images that contain semantic content, such as flowers during autumn or goals during football plays, is not simple. To do so, images should be well annotated by experts when inserted in the database. So, the quality of retrievals depends on the quality of the manual annotations. This solution characterizes classic information retrieval systems initiated by [Moo 51], and developed by [Sal 68], [Rij 79], and others. However, manual annotations tend to be incomplete and inconsistent, and they do not allow visual content-based image indexing and retrieval. Visual information systems, also known by content-based indexing and retrieval systems, such as in [Dje 00], [Jai 98] and others, overcome some of these shortcomings. The index is, generally, created automatically, and the final users have the possibility to formulate content-based queries. In spite of these appreciable advantages, the automatic indexing, which is the most important advantage of visual information systems, support weak semantic description, and therefore weak semantic queries. So finding images that contain flowers during autumn remains a very 

> © The copyright of this paper belongs to the paper's authors. Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. 

> Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 

> (O.R. Zaïane, S.J. Simoff, eds.) 

###### difficult query. 

Content-based image indexing associated to knowledge discovery may be seen as a new way of thinking and regarding retrieval of multimedia information and it opens up to a lot of new applications which have not been possible, previously. For image archives the new possibilities given by content-based image indexing and knowledge discovery lies in the ability to perform "advanced queries-by-example’’, meaning that we can present an image of an object, pattern, texture, etc., and fetch the images in the database that most resemble the example of the query. For image databases the new possibilities lie in the ability to access efficiently and directly selected images of the database. 

Our paper deals with the following challenge : how do we build automatically the semantic content of images, based on basic content descriptions ? We believe that discovering hidden relations among basic features contributes to extract semantic descriptions useful to make the content-based image retrieval more efficient. In our case, the relationship discovery are held into two important steps : symbolic clustering based on the new concept of visual feature book and relevant relationships discovery. 

The originality of our work concerns the following points : 

- the definition of a new algorithm of global/local clustering 

- and classification, based on : - visual quantization, powerful image descriptors and - suitable similarity measures, 

- the creation of an efficient feature (texture, color) book 

- which is the most representative of database image features, 

- the power qualification of the relationship among visual 

- features. They are composed of conditional probability and implication intensity measures, 

- the extension of the classic indexing by relevant relationships 

- that are automatically discovered. 

The implementation of these notions together in the same framework constitute our advanced content-based indexing which is the scope of the paper. 

We organize the paper as follow : in section 2, we describe the classic and advanced content based indexing and retrieval. We answer to the following questions : how images are searched in image database. We will not focus on speed data structures necessary to support the index, however, we will focus on the knowledge necessary to advanced content-based retrieval. In section 3, we present how the content of images are extracted and represented, how descriptors of images may be used to discover 

73 

relations between descriptors, and how the discovered relations are useful to content-based image retrieval. In section 4, we describe some experiment results. 

###### **2. YOU SAID CONTENT-BASED IMAGE INDEXING AND RETRIEVAL ?** 

The content-based image indexing and retrieval architecture is composed of three important components : extraction, representation and retrieval. Extraction and representation components constitute the heart of the architecture, together, they constitute the indexing component. The extraction component extract, automatically or semi-automatically, regions in images and compute features such as color, texture and shape of these regions. The whole image may constitute itself a region. The extracted contents are represented as or transformed into suitable models and data structures, and then stored in a persistent index. 

The retrieval component constitute the eyes of the architecture. It searches images by selecting target images or content properties such as color, sketched shape, texture of image regions, or combinations of these. The retrieval process computes distances between source (example) and target features, and sorts the most similar images. 

The central question is : how to extract and represent the content in order to make the retrieval process efficient ? Before answering this question, we will start by presenting the classic approach, and we will compare the benefits of the knowledge discovery to image indexing and retrieval efficiency. 

###### **2.1 Classic indexing** 

Indexing responds to how the content should be extracted and represented to allow efficient and effective search and access ? 

Sequential searching of images with simple similarity computations is quite appropriate in a small database. However, the larger the database is, the slower the sequential approach is. So efficiency will not be respected. Classic access structures such as B-trees [Bay 72], K-D trees [And 85], point quadtrees [Fin 74] and R-trees [Gut 84] have advantages and disadvantages. Point quadtrees are simple to implement. However, there is a complexity of both insertion and search. Furthermore, deletion in point quadtrees is complex because finding a candidate replacement node for the node being deleted is generally difficult. Finally, the range retrieval in point quadtrees is time consuming. It takes O(2 √ n), where n is the number of image references in the tree. K-D-trees are very simple to implement. However, the search and insertion complexity in k-d-tree is high. In MX-quadtrees, range retrieval is very efficient, and the insertion, deletion and search take time proportional to O(n). We assume that the image (ex. map) is split up into a grid of size (2<sup>n</sup> x 2<sup>n</sup> ) cells. R-trees have been preferred over k-d trees and point quadtrees, because they store a large number of rectangles in each node. So, they are suitable for disk accesses by reducing the height of the tree, this leading to fewer disk accesses. The disadvantage of R-trees is that, in certain cases, instead of following one path in the search process, multiple paths may be followed, because bounding rectangles associated with different nodes may be overlapped. Multiple paths means more disk accesses that might be compared to disk accesses of the other quadtrees. 

These representations are physical access structures, they deal with applications that require massive amounts of storage and disk accesses. So they concern low level representation of the access structures. These access structures are necessary, but not enough to access effectively image materials. They need to be completed by high level representations (logical representation) that organize efficiently the descriptors of images, independently of their physical representations. 

###### **2.2 Advanced indexing** 

To obtain efficient access data structures, we should combine physical and logical representations of high-dimensional features. In our context, to effective up the content-based retrieval, we consider semantic representations that include image class hierarchy (images of flowers, panorama, etc.) characterized by knowledge and access speed data structures (K-D-trees). The K-D trees are implemented for high-dimensional features, at least eleven-dimension color and texture attributes, and voluminous classes. However sequential search is used for low-dimensional features and less voluminous classes. The K-D-trees are implemented at eleven-dimension because the color is represented by one dimension and the texture is represented by ten dimensions (ten couple of coefficients). 

For example, when the user asks for images that contain waterfalls (figure 1), the system matches the user examples with the knowledge in the form of rules. In certain case, the image may belong to several classes, because the distance between the gravity center of the examples and the knowledge of the image classes are near together. In all cases, the retrieval process focuses its matches in the sub-classes of the current ones. In the sub-class, it triggers the same match process. When the leaf class is reached, the physical data structure is used to find the best images. When the number of the images in a class is low (ex. less than 100), than the search process is limited to sequential order. 

In the example presented bellow, the first images returned contain waterfall, and the other images contain flowers. The whole images are visually similar to the example images. This example illustrates the « advanced query by examples » that is based on combination of visual features (texture and color) and knowledge. «advanced query by examples» specifies a query that means «find images that are similar to those specified». The query may be composed of several images. Several images accurate the quality of retrieval. For example, Several images of a «waterfall» accurate the description of the waterfall. This property makes possible the refinement of retrieval based on the feed backs (results of previous queries). 

In the retrieval task (figure 2), features (colors, textures) of the query specification are matched with the knowledge associated to classes (ex. natural, people, industries, etc.). The suited classes are « Natural », then the matching process focus the search on the sub-classes of Natural : « Flowers », « Mountain », « Water », « Snow », etc. The knowledge associated to flowers and waterfalls are verified, so the matching process focuses the search on the « Flower » and « Water » classes. « Flowers » and « Water » classes are leaves, so the matching process compares the features of the examples with features of the image database to determine which images are similar to the example features. The matching task is based on computing the distance between target and source 

74 

image regions. When mixing several features, such as colors and textures, the resulting distance is equal to the Sum taking into account the ponderation values of the considered features. The resulting images are sorted, the shortest distance corresponds to the most similar images. 



<!-- Start of picture text -->
User’s query composed of four<br>examples (four images)<br>Sorted results<br>Image<br>results o f<br>the user’s<br>query<br><!-- End of picture text -->

**Figure 1 : «find images that contain waterfalls».** 

"automatically" in the class hierarchy. At the end of the classification process, the image is inserted in a specific class. In this case, the distance between the image and the knowledge associated to the class is the shortest one, compared to the distance between the image and the other classes. Otherwise, the instantiation relationship between the image and the class, will not be considered. 



<!-- Start of picture text -->
Root<br>Natural People Industries Transports<br>Water Flowers Mountains Snow<br>D11 D1 D2 D3 D4<br>D12<br>D11  ≤  D12<br>D1  ≤  D2  ≤  D3  ≤  D4<br>Classification process Classes matched with success<br><!-- End of picture text -->

**Figure 2 : Example of image insertion into the class hierarchy** 

This architecture avoids efficient retrievals and browsing through classes. For example, the user may ask "find images similar to the source image but only in People classes" or "find me all images that illustrate the bird class with such colors and such shapes". 

###### **3. DISCOVERY HIDDEN RELATIONS** 

An important advantage of the advanced indexing is the efficiency of the content-based retrieval. When the user gives examples of image to formulate his query, and asks "find images similar to the examples", the system will not match the source image with all the images in the database. It will match the source image features with only the target image features of suited classes. If the knowledge associated to a class is globally verified, then the considered class is the suited one. Then, the system will focus the search on the sub-classes of the current one. In the target classes that contain few instances, the search is limited to sequential accesses. Another advantage is the richness of descriptions contained in the results of queries since the system presents both similar images and their classes. 

###### **2.3 New architecture** 

The advanced approach for content-based image indexing needs an advanced architecture. The advanced architecture extends the classic architecture by knowledge in the form of simple rules. Simple rules that characterize each semantic class (flowers, natural, mountain, etc.) are automatically extracted. The classic indexing is base exclusively on low level representations of images and physical access structures, without any knowledge and logical representations of the content. The rules describe relationships between visual features (colors and textures of images). Each set of rules associated to a class summarizes image contents of the class. Rules contribute in the discrimination of each class, so they represent knowledge shared by the classes. When images are inserted in the database, it is classified 

Based on image content description, the knowledge are discovered. The discovered knowledge characterizes visual properties shared by images of the same semantic classes (Birds, Animals, Aerospace, Cliffs, etc.). 

The discovery is held into two steps : symbolic clustering and relationship discovering and validation. 



2- `relationship discovery and validation` 

In the first step, numerical descriptions of images are transformed into symbolic form. The similar features are clustered together in the same symbolic features. Clustering simplifies, significantly, the extraction process. For example, in the figure presented bellow (figure 3), the image is composed of region1 and region2. Region1 is characterized by light red color, and region2 by water color and water texture. 



<!-- Start of picture text -->
Region1<br><!-- End of picture text -->



**Figure 3 : Original representation of the image. Numeric representation of image B8169** 

75 

Light red color is not described by a simple string, but by a color histogram. Even if the region colors of different images of the same class, as presented in figure 4, are similar (i.e. light red), the histograms (numerical representation of color) associated with them are not generally identical. 



<!-- Start of picture text -->
- texture : bird_texture - texture : bird_texture<br>Region2<br>Region1 - color : red_light<br>- color : water_color<br>- texture : water_texture<br><!-- End of picture text -->

**Figure 4 : Symbolic description of image B8169** 

```
/* Declaration of composition relations
between images and regions. */
```

```
is_composed_of(imageB8169, [region1,
region2]).
```

```
/* Region features declaration. A region is
usually described by texture and color */
/* text  attributes.  */
```

```
features(region1, [texture,
bird_texture], [color, red_light]]).
features(region2, [[texture,
```

```
water_texture], [color, water_color]]).
```

```
/* Image features declaration. An image is
usually described by the texture, color.  */
features(imageB8169, [[text, text1]]).
```

In the second step, the knowledge discovery engine automatically determines common features between the considered images in rule form. These rules are relationships in the form of `Premise => Conclusion` with a certain accuracy. These rules are called statistical as they accept counter-examples. 

```
(texture, water_texture) => (color,
water_color) (CP 100%, II 96.08%)
```

```
(texture, waterfall_texture) => (color,
white_color) (CP 100%, II 87.43%)
```

```
(texture, texture_bird) => (color,
red_light) (CP 100%, II 40.45%)
```

Before presenting the algorithm of discovering, we will present how the image content (color, texture) are represented and extracted automatically. More details about image descriptors have been presented in [Dje 00]. 

###### **3.1 Image descriptors** 

###### _3.1.1 Color_ 

The color is the first descriptor of image content. The color feature is extracted automatically from an image or a region. In the first step of the extraction process, based on a physical format, the region or image color is extracted and represented in the RGB model. Based on the RGB model, the color is transformed into HSV model, characterized by three means H, S and V. The HSV model is more suited than the RGB model, in which certain ambiguities appear between colors (ex. Yellow and Green). 

In the object-oriented modeling, we define a class of colors called HSV. HSV class includes color histogram and methods (ex. distance measures). The color of a region is represented by a histogram of 256 colors. Each element of the histogram represents the number of pixels that have the suited color (see figures 5, 6). So, comparing the colors of two regions is equivalent to compute the distance between the histogram of the target and the source regions. Before submitting the query, the user may choice the distance, by default quadratic distance is activated. 



<!-- Start of picture text -->
Design of the whole<br>& 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011100000000000000000000000000011111000000000000000000000000001111100000000000000000000000000111111000000000000000000000000111111110000000000000000000000111111111100000000000000000000011111111111000000000000000000001111111111110000000000000000000011111111111100000000000000000000111111111111000000000000000000001111111111100000000000000000000011111111110000000000000000000001111011111000000000000000000000111000011110000000000000000000001110000000000000000000000000000011100000000000000000000000000000111000000000000000000000000000010000 image histogramregion histogramDesign of the Database<br><!-- End of picture text -->

**Figure 5 : Extraction of colors.** 

In figure 5, the color is represented by a histogram. One histogram represents the color of the whole image, and other histograms represent image region colors. An image region is designed by a binary mask. For example, the binary mask designs the image region that characterizes the bird. The binary mask is equal to 1 inside the region, and 0 outside the region. The histogram of colors are calculated on the basis of the binary mask and the photo. 



<!-- Start of picture text -->
y = histogram<br>of the color x Image<br>Color x<br><!-- End of picture text -->

**Figure 6 : Color histogram.** 

In figure 6, the graphic representation of the image color histogram is displayed. For example, y is the histogram of the color x � y = number of pixels that have the color x. 

###### _3.1.2 Texture_ 

The texture is an important aspect of human visual perception, and it is the second important feature extracted automatically from image regions. 

When two patterns differ only in scale, the magnified one is coarser. The variance measures the dispersion of the difference of gray-level with a certain distance. The contrast measures the vividness of the texture and is a function of the gray-level 

76 

difference histogram. The directionality measures the « peakedness » of the distribution of gradient directions in the image. For example the region may have a favored direction. It is not a powerful texture representation, but may be interesting for retrieval process when mixing it with color features. 

The approach, considered, implements a powerful texture representation. Thus, we use a mathematical model which is one of the best : Fourier model [Zah 72]. Fourier model has very interesting advantages : - the texture can be reconstructed from the descriptors. – it has a mathematical description rather than a heuristic one. - And finally, the model supports the robustness of description to translation, rotation and scale transformations. An important contribution of our representation is our extension of Fourier model to texture description. This extension considers the matching process. In this extension, we consider texture(t) composed of two functions : x(t) and y(t). 

So texture(t) =(x(t), y(t)). x(t) represents the different level of gray of x, and y(t) represents the different level of gray of y. t indicates the different indices of the signal texture. t = 0, N-1. N is the period of the function, and N = number of x values and y values = length of the normalized image. So, we have two suites of coefficients S(an, bn) and S(cn, dn) that represents Fourier coefficients of x(t) and y(t) respectively. 



<!-- Start of picture text -->
x(t)<br>y(t)<br><!-- End of picture text -->

**Figure 7 : x(t), y(t)** 



```
and
```

`an = 2/N` ∑ `k=1,N x(t) cos(2` π `kt/N) bn = 2/N` ∑ `k=1,N x(t) sin(2` π `kt/N) cn = 2/N` ∑ `k=1,N x(t) cos(2` π `kt/N) dn = 2/N` ∑ `k=1,N x(t) sin(2` π `kt/N)` 

**Figure 8 : Fourier Coefficients formulas** 

We consider only eleven coefficients of Fourier that select the lowest frequencies of the sub-band k ∈ [0-10]. In this extension, 

we modify the similarity measures (Euclidean distance) in order to consider the coefficients of the two signals x(t) and y(t), as we will see in the following section. 

###### **3.2 Symbolic clustering algorithm** 

The clustering of numeric features in symbolic form raises several problems. The first problem is that a feature may belong to one or several symbol(s). The problem is the same for texture and color features. The second problem is a consequence of the first one. After the symbol creation, we can obtain two different symbols that may be either composed of the same numerical features (equal symbols), or composed of several symbols that differ on only one feature. If we obtain two different symbols composed of the same features, the system keeps only one symbol among symbols composed of the same features. If we obtain several symbols that differ on only one numerical feature, then, it is more difficult to resolve. The problem is the same for the other features. The third problem is that the system generates a symbolic feature base bigger than the numeric feature base since the system computes for one fact containing numeric values, several facts containing symbolic values. The figure presents a part of a symbolic feature and illustrates the possibility of feature fact explosion. 

To resolve these problems, we implemented a technique that clusters numerical representation of color, texture, by using data quantization of colors and textures, we use also the term of feature book creation. The color and texture clustering algorithms are similar, the difference is situated in the distance used. 

###### _3.2.1 Principle of the algorithm_ 

The algorithm is a classification approach based on the following observation. The scalar quantification of Lloyd developped in 1957 is valide for our vectors (color histogram, fourier coefficients), four rate distribution and for a large variety of distortion criteria. It generalizes the algorithm by modifying the feature book iteratively. This generalization is known by k-means [Lin 80]. The objective of the algorithm is to create a feature book, based on automatic classifications themselves based on a learning set. The learning set is composed of feature vectors of unknown probability density. Two steps should be distinguished : 

- A first step of classification that clusters each vector of the learning set around the initial feature book that is the most similar. The objective is to create the most representative partition of the vector space. 

- A second step of optimization that permits the correct adaptation in a class of the feature book vector. The gravity center of the class created in the previous step is computed. 

The algorithm is reiterated in the new feature book in order to obtain a new partition. The algorithm converges to stable position by evolving at each iteration the distortion criteria. Each application of the iteration of the algorithm should reduce the mean distortion. The choice of the initial feature book will influence the local minimum that the algorithm will achieve, the global minimum corresponds to the initial feature book. The creation of the initial feature book is inspired of the splitting technique [Gra 84]. 

The splitting method decomposes a feature book Yk into two different feature books Yk- ε and Yk+ ε , where ε is a random vector of weak energy, and its distortion depends of the distortion of the 

77 

splited vector. The algorithm is then applied to the new feature book in order to optimize the reproduction vectors. 



<!-- Start of picture text -->
Texture learning set of length T Color learning set of length T<br>Clustering Clustering<br>L <<< T<br>Texture book of length L Color book of length L<br><!-- End of picture text -->

**Figure 9 : Clustering and reduction algorithm. In our experiments T = 30.000 and L = 256** 

###### _3.2.2 Distances_ 

The system clusters similar colors together in a symbolic form by using a suitable distance. In our case, for the color, we implement the quadratic distance which is one of the most accurate distances. 



###### **Figure 10 : Quadratic_distance definition.** 

This distance takes into account the color similarity between the histogram bins by using the symmetrical similarity matrix _A_ . The matrix weights may be normalized to obtain 0 ≤ _a pq_ ≤ 1. So, 

the matrix diagonal is equal to 1, since any color is identical with itself ( _app_ =1). A coefficient _apq_ close to 0, represents a dissimilarity between _p_ and _q_ bins. For example, in QBIC, the quadratic distance between two color histograms, is used with a similarity matrix _A_ whose elements are defined by [Haf 95]: aij = (1 – dij/dmax), with dmax = maxij(dij), dij being Euclidean distance between the color i and j in any color space. The two distributions _H_ and _I,_ may also be normalized in order that 0 ≤ _hc p_<sup>_,i_</sup> _c p_ ≤ 1 



<!-- Start of picture text -->
and ∑ hc p = 1 = ∑ icp .<br>p p<br>n<br>DL 2( H I , ) = ( hcl − icl )2<br>∑ l = 1<br><!-- End of picture text -->

**Figure 11 : L2-distance or Euclidean distance definition.** 

This distance makes it possible to obtain satisfactory results since it appreciates color similarity correctly. However, its major drawback is that it is time-consuming compared to the other distances. Euclidean distance results from the quadratic distance where _A_ matrix is the identity matrix (no correlation between the histogram bins). 

In our example, the light red color zones in the different images are grouped together in the symbolic form red_light as they are similar. Water color in not clustered in red_light, because the distance between them is not short enough. However, it is 

clustered in the symbolic form water_color shared with other images. In the same way and based on appropriate distances, the system clusters respectively similar shapes, similar textures together in a symbolic form. 

For the texture, we implement an adaptation of the Euclidean distance to Fourier coefficients, we call it « texture_Fourier_distance ». So, the matching distance between the Fourier descriptors of the texture _t’_ of an image image’ and the Fourier descriptors of the texture _t_ of an image « image », is triggered by computing the distance between _t_ and _t’_ , namely: `d(t,t’) =` √ `(` ∑ `n=1,N (|T’n - K.|Tn|)`<sup>`2`</sup> `),` N=10, for t and t’ textures, we have a positive constant K, and for any n ≠ 0, `|T’n| = K*|T n|,` where `Z n =` √ `(|X n|`<sup>`2`</sup> `+ |Y n|`<sup>`2`</sup> `)=` √ `(a n 2 + b n 2 + c n 2 + d n 2)` That is to say, the textures are identical near to one geometric transformation. The translation, scale and rotation have no effect on the module of Fourier coefficients. `K = 1/N*(` ∑ `n=1,N(|T’n|/|Tn|))` is an estimation of _K_ which minimizes the error on the _N_ (e.g. 11) first coefficients of Fourier. 

###### _3.2.3 Algorithm_ 

Based on the learning set of length equal to T, the algorithm finds a feature book of colors and textures of length equal to L, that are the most representative colors and textures of image databases. 

###### _Global Clustering_ 

```
FeatureBook Yf = SymbolicClustering (visual
feature = VisualFeature, learning set =
LearningSet, Y0, T, L)
```

```
{
```

if the `VisualFeature = color` then `LearningSet = {H1, H2, H3, ..., HT}` , a set of `T` histograms. 

If `VisualFeature = texture` then `LearningSet = {S1, S2, ...., ST}` , a set of `T` sequence of Fourier coefficients. `Y0` is the initial feature book with distortion `D0` and cardinal equal to `L` . 

Pre-conditions : `L << T` 

Invariant : `s` ≤ `S=L/2` 

1- Initialization : `D0 = Distortion (Y0) ; E0 = Entropy(Y0) ; s = 0 ;` s = number of splitting activated. `Class0 = {Class0,k` <u>`; k = 1, ..., L}`</u> 







<!-- Start of picture text -->
Classe1 Classe2<br><!-- End of picture text -->

**Figure 12 : Distorsion(Classe1) < Distorsion(Classe2)** 

```
While (s < S)
{
2 - s = s + 1
```

78 

3 - Splitting of the VisualFeature of the feature book `Ys-1` that support the highest apparition probability `pi. pi` corresponds to the `class` that has the maximum number of instances. The `s,i` VisualFeature of the feature book corresponds to the gravity center of the `classs,i. (Ys-1,i’, Y s-1,i’’`<sup>`)`</sup> `= splitting(Ys-1,i)` . 

4 - Deletion of the `VisualFeature` of the feature book `Ys-1` that support the lowest apparition probability `pj. pj` corresponds to the `class` that has the minimum number of of instances. `s,j` The `VisualFeature` of the feature book corresponds to the gravity center of the `classs,j` . 

Each splitting is followed by a deletion, so the cardinal of the feature book remains constant (equal to `L` ). 

5 - A local clustering with the parameter `E1` is executed on the class `classs,i` on the local feature book composed of `Ys-1,i’, Ys-1,i’’` and `E1` the stop criteria of the algorithm. 

```
YVisualFeature, feature book = (Ys= Clustering(visual feature s-1,i’, Ys-1,i’’),=
E1, learning set = classs,i).
```

6 - A global clustering is executed on the global feature book composed of `Ys` with the parameter `E2. E2` is the stop criteria of the algorithm. 

`Ys = Clustering(visual feature = VisualFeature, feature book = Ys, E2, learning set = classs) ; Ds = Distortion (Ys) ; Es = Entropy(Ys). Ds < D0` : the distortion is reduced and `Hs > H0` : the entropy is augmented}} 

Ideally, the stop criteria of the algorithm should depend of the distortion `Ds` , however, the distortion `Ds` depends of the number of splitting. 

###### _Local clustering_ 

```
FeatureBook Yf = Clustering(visual feature =
VF, learning set = LS, Y0, Yf, T, L, E)
{
```

`Y0` is the initial feature book with distortion `D0` and length equal to `L. LS` is the learning set with a length is equal to `L. E` is the stop criteria. 

Pre-conditions : `L << T` 

1 - Initialization : `D0 = Distortion (Y0) ; s = 0` ; s = number of splitting activated. 

```
Do
{
```

2 - Based on the feature book `Ys = {Ys,k k=1,..,L}` and the learning set `LS` ; we extract the partition `Classs = {Classs,k ; k = 1, ..., L}` , in which `distance(x, y)` is minimal. So : 

`xt` ∈ `Classi,k when distance(xt, yk)` ≤ `distance(xt, yj)` ∀ `j` ≠ `k. Ds = 1/T` ∑ `t=1,T minY distance(xt, y), y` ∈ `Ys` 



3 - Creating the optimal catalogue `Ys+1 = {centroid(Classs,k) k=1,..,L}` ; `centroid(Classs,k)` corresponds the gravity center of the class `Classs,k` . `centroid(Classs,k) = (1/|Classs,k|)*` ∑ `xt / t : xt` ∈ `Classs,k. |Classs,k|` is the number of instances in `Class` . `s,k` 

```
4 - s = s + 1
```

```
} Until (Ds-1 - Ds)/Ds < E}
```

The distortion `Ds` is a positive and decreasing function. Each iteration of the algorithm reduce the distortion. So, `Ds-1` ≥ `Ds.` 

The experimental results showed that the distortion values decrease quickly compared to splitting evolution. After the quick decreasing, the distortion values decrease very slowly. Conversely, The entropy increase quickly compared to splitting evolution, and then, it increases very slowly. 

###### **3.3 Relationship discovery and validation** 

Based on the feature book, the discovery engine is triggered to discover the shared knowledge in the form of rules, and this constitutes the second step the general algorithm. 

Accuracy is very important in order to estimate the quality of the rules induced. The user should indicate the threshold above which rules discovered will be kept (relevant rules). In fact, the weak rules are rules that are not representative of the shared knowledge. In order to estimate the accuracy of rules, we implement two statistical measures : conditional probability and implication intensity. The conditional probability formula of the rule `a => b` makes it possible to answer the following question: ‘‘what are the chances of proposition `b` being true when proposition `a` is true ? The definition of this measure is `P(b/a) = Card(A` ∩ `B)/Card(A)` 

More intuitively, conditional probability allows us to estimate the accuracy of a rule, considering the number of counter-examples. For example, let us consider `p1 (a => b)` and `p2 (b => a)` conditional probabilities are respectively 100% and 5.6%. So, the rule `b =>a` has a lot of counter-examples. In _`E`_ (universe set), there are lots of objects that belong to `B` , but not to `A` . Conversely, the rule `a => b` has no counter-example. So, objects that respect `proposition a,` respect also `proposition b` . 

Conditional probability allows the system to determine the discriminating characteristics of considered images. Furthermore, we completed it by the intensity of implication [Gra 82]. For example, implication intensity requires a certain number of examples or counter-examples. When the doubt area is reached, the intensity value increases or decreases rapidly contrary to the conditional probability that is linear. In fact, implication intensity simulates human behavior better than other statistical measures and particularly conditional probability. Moreover, implication intensity increases with the considered population sample representativity. The considered sample must be large enough in 

79 

order to draw relevant conclusions. Finally, implication intensity takes into consideration the sizes of sets and consequently their influence. For example, conditional probability of `a => b` is `P1` (100%) and implication intensity of `a =>b` is ϕ `1` (23%) values are very different because conditional probability does not take into consideration the fact that `proposition b` is verified by lots of objects. On the contrary, implication intensity considers that it is not surprising that an object of _A_ verifies `proposition b` because `proposition b` is verified by many objects of the considered sample. 

Let `A,B` and `E` sets respectively be the sets of instances that verify `proposition a,` the set of instances that verify `proposition b` , and the set of all instances or the `universe set.` From a theoretical point of view, implication intensity measures the degree of statistical astonishment of size _A_ ∩ _B_ (this set contains objects that verify `proposition a` and that do not verify `proposition b` ) considering the sizes of _`A`_ `,` _`B`_ and `E` sets, and assuming there is no a priori link between `A` and `B` . The cardinals or the sizes of `A` and `B` subsets of `E` are determined by the objects of the database belonging to `A` and `B.` 

The knowledge discovery engine returns the rules in the form of `Premise => Conclusion` whose intensity and conditional probability are greater than or equal to a certain threshold. For the moment, this threshold is defined manually (ex. 90 %). Samples of extracted rules by the prototype are `(texture, water_texture) => (color, water_color), (texture, waterfall) => (color, white)` with respective conditional probability values of  100% and 100%, and implication intensity values of 96.08% and 87.08 %. 

###### **3.4 Some comments** 

The set of induced rules corresponds to knowledge shared by classes. This knowledge is helpful for user‘s comprehension of the class. Extracted rules are validated when the conditional probability and the rule intensity are greater than a special value (i.e. 90% for conditional probability and 80% for implication intensity). For example, `(texture, bird_texture) => (color, red_light)` has 100% conditional probability and 40.4598% implication intensity. Since the rule intensity is less than 80%, the system will not store it. We explain this weak measure of rule intensity by the fact that there are few examples that respect this rule. 

In our example, the searched class is characterized by a set of rules such as  rule 1. So, if we have the ‘‘water_texture’’ texture in an image of the class, then the region color inside the image is red_light with 100% conditional probability and 96,08 % rule intensity. So, during image database creation, the classification of an image in a class is possible if the class rules, previously extracted and validated, are globally respected. At least 50 % of rules are respected. If not, we will  not consider the instantiation relationship between the image and the class. 

`x => y` has 15.3846% conditional probability and 61.79% implication intensity, that is to say that the conditional probability value is less than 90%. So, the system did not store this rule. We explain this weak measure of conditional probability by the fact that there are a lot of counter-examples of the considered rule. `(texture, waterfall) => (color, white)` is a good rule because the conditional probability value is 100% and the implication intensity is 81.79%. This rule means that when we 

have a texture that includes water, then we would have a white region color. 

In the retrieval task, when the user specifies an image (called source image) as the basis of his query, and asks ‘‘find images similar to the source image’’, the system will not match the source image with all the images of the database. It will match the source image features with all the target images of the appropriate classes. These classes contain rules globally respected by the source image. 

For example, if we have a source image that contains a ‘‘texture_waterfall’’, but it does not globally verify the rules associated with this concept, we can deduce the weakness of the relationship between the source image and the class. The system matches the source image with classes through their rules stored in the database. 

##### **4. EXPERIMENTAL RESULTS AND CONCLUSION** 

We have conducted extensive experiments of varied data sets to measure the performance of the advanced content-based query. The recall and precision graphic for our system are computed as follows. References («query») of images are selected from a test collection. A sub-set of images is selected per class (waterfalls, fires, panorama, etc.). For each image, a knowledge content-based query is formulated. For an image reference, we associate a knowledge content-based query that includes visual features (color, texture, color + texture). We also associate a classic content-based query that uses classic indexing (there is no knowledge integration). 

To demonstrate the efficiency of the knowledge content-based queries, the results of the advanced content-based queries are compared with the results of queries that do not use classic content-based queries. Since it is not possible to retrieve all relevant images, our experiment evaluates only the first ranked images. 

Judging on the results, it is obvious that the use of knowledge leads to improvements in both precision and recall over majority queries tested. The average improvements of advanced contentbased queries over classic content-based queries are 23% for precision and 17 % for recall. Precision and recall are better for concept-based queries (queries that mix visual features and textual descriptions with different degrees of importance) than for queries that use only visual features such as color or shapes or textures or textual descriptions, but not both. 

##### **Acknowledgement** 

Many thanks to Henri Briand for his encouragement. 

##### **REFERENCES** 

- [And 85] Andrew W. Appel, An Efficient Program for ManyBody Simulation, SIAM Journal of Statistical and Scientific Computing, 6(1), January 1985. 

- [Bay 72] Bayer, R., E. McCreight. Organization and Maintenance of Large Ordered Indexes. Acta, 1972, Informatica 1(3), 173-189. 

- [Dje 00] Djeraba C., Bouet M., Henri B., Khenchaf A. « Visual and Textual content based indexing and retrieval », to 

80 

appear in International Journal on Digital Libraries, Springer-Verlag 2000. 

- [Fay 96] Fayyad U. M., Piatetsky-Shapiro G., Smyth P., Uthurusamy R., «Advances in Knowledge Discovery and Data Mining», AAAI Press, MIT Press, 1996. 

- [Gut 84] Antonin Guttman: R-Trees: A Dynamic Index Structure for Spatial Searching. SIGMOD Conference 1984, pages 47-57, 1984. 

- [Gra 82] Gras Régis, THE EISCAT CORRELATOR, EISCAT technical note, Kiiruna 1982, EISCAT Report 82/34, 1982. 

- [Gra 84] Gray R. M. « Vector Quantization », IEEE ASSP Mag., pages 4-29, April 1984. 

- [Gup 97] Amarnath Gupta, Ramesh Jain «Visual Information Retrieval», A communication of the ACM, May 1997/Vol. 40, N°5. 

- [Haf 95] Hafner J., al. «Efficient Color Histogram Indexing for Quadratic Distance Functions». In IEEE Transaction on Pattern analysis and Machine Intelligence, July 1995. 

- [Jai 98] Ramesh Jain: Content-based Multimedia Information Management. ICDE 1998: 252-253 

- [Lin 80] Linde Y., Buzo A., Gray R. M. « An algorithm for Vector Quantizer Design », IEEE Trans. On Comm., Vol. COM-28, N° 1, pages 84-95, January, 1980. 

- [Moo 51] Moores C. N. «Datacoding applied to mechanical organization of knowledge» AM. Doc. 2 (1951), 2032. 

- [Rag 89] Raghavan, V., Jung, G., and Bollman, P., “A Critical Investigation of Recall and Precision as Measures”, ACM Transactions on Information Systems 7(3), page 205-229, 1989. 

- [Rap 74] Raphael A. Finkel, Jon Louis Bentley: Quad Trees: A Data Structure for Retrieval on Composite Keys. Acta Informatica 4: 1-9, 1974. 

- [Rij 79] C. J. Keith van Rijsbergen «Information retrieval», Second edition, London: Butterworths, 1979 

- [Sal 68] Salton Gerard «Automatic Information Organization and Retrieval», McGraw Hill Book Co, New York, 1968, Chapter 4. 

- [Zah 72] C. T. Zahn, R. Z. Roskies, « Fourier descriptors for plane closed curves », IEEE Trans. On Computers, 1972. 

81 

### **Semantic Indexing and Temporal Rule Discovery for Time-series Satellite Images** 

Rie Honda Hirokazu Takimito Osamu Konishi Kochi University Kochi University Kochi University Akebono-cyo 2-5-1 Akebono-cyo 2-5-1 Akebono-cyo 2-5-1 Kochi, JAPAN 780-8520 Kochi, JAPAN 780-8520 Kochi, JAPAN 780-8520 honda@is.kochi-u.ac.jp takimoto@is.kochikonishi@is.kochiu.ac.jp u.ac.jp **ABSTRACT General Terms** Feature extraction and knowledge discovery from a large DESIGN, EXPERIMENTATION, PERFORMANCE amount of image data such as remote sensing images have b ecome highly required recent years. In this study, we present a framework for data mining from a set of **Keywords** time-series images including moving ob jects using clusSatellite image database, clustering, self-organizing featering by self-organizing mapping(SOM) and extraction ture map, time dep endent asso ciation rule, R-tree, contentof time-dep endent asso ciation rules. We applied this based image retrieval, SQL query metho d to weather satellite cloud images taken by GMSand evaluated its usefulness. The images are classi- **1. INTRODUCTION** �ed automatically by two-stage SOM. The results were A huge amount of data has b een stored in databases examined and the cluster addresses were describ ed in in the areas of business or science. Data mining or regard to season and prominent features such as tyknowledge discovery from database(KDD) is a metho d pho ons or high-pressure masses. Sequential images are for extracting unknown information such as rules and then transformed into a data series expressed by cluspatterns from a large-scale database. The well-known ter addresses and time of o ccurrence, from which timedata mining metho ds include decision tree, asso ciation dep endent asso ciation rules (simple serial rules) are exrules[], classi�cation, clustering, and time-series analtracted using a metho d for �nding frequently co-o ccurring ysis[][]. term-pairs from text. Semantic indexed data and extracted rules are stored in the database, which allows The pro cess of the data mining is comp osed of the folhigh-level queries by entering SQL through user interlowing six parts: () acquisition of input data, () seface, and thus supp orts knowledge discovery for domainlection of input data, () prepro cessing, () transforexp erts. We b elieve that this approach can b e widely mation, () extraction of patterns, rules, etc., and () useful and applicable to knowledge discovery from an interpretation and evaluation of the results. enormous amount of multimedia data, which includes unknown sequential patterns. There are two main areas of in the data mining: one fo cused on business data and one fo cused on scienti�c data. **Categories and Subject Descriptors** H.. [Information Systems]: Database Applications| One of well-known cases of scienti�c data mining is the data mining, image database, scienti�c databases Sky Image Cataloging and Analysis to ol (SKICAT) de; H.. [Information Systems]: Information Search velop ed for the second Palomar Observatory Sky Surand Retrieval|clustering ; J. [Computer Applicavey[]. They extracted astronomical b o dy candidates tions]: Physical Science and Engineering|earth and from enormous raw images and classi�ed them using atomspheric science a decision tree. In this pro cess the researchers discovered b oth the classi�cation rules and the novel b o dies. Smyth et al.[] and Burl et al.[] have also rep orted a discovery system for venusian volcano es based on synthetic ap erture radar images taken by the spacecraft Magellan, which are very e�ective as recognition guides. 

###### **ABSTRACT** 

> © The copyright of this paper belongs to the paper's authors. Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. 

Image data such as satellite images and medical images distributed for direct commercial advantage. Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), often amount to several Tera bytes, thus manual and in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000  (O.R. Zaïane, S.J. Simoff, eds.) detailed analysis of these data b ecomes impractical[]. Therefore an automated(or semi-automated) pro cedure 

82 

to extract knowledge from these data should b e included The ab ove-describ ed pro cess enables us to characterize in the data mining from the image database. enormous amount of images acquired at a certain time interval semi-automatically, and to retrieve the images In our recent studies[][], we have applied data minby using the extracted rules. For example, this pro cess ing metho ds such as clustering and asso ciation rules to enables queries like "search for frequent events that o c- a large numb er of the satellite weather images over the cur b etween one typho on and the next typho on", or Japanese islands taken by Japanese stationary satellite "search for a weather change such that a typho on o c- GMS-. These weather images are accumulated everycurs within 0 days after a front and high pressure mass day and form a large amount of raw database. develop ed within the time interval of days". Metrological events are considered to b e chaotic phenomena in that an ob ject such as a mass of cloud changes `GUI` its p osition and form frequently. Furthermore they are time-sequential data such as video images. `B A C B E` Features of our studies applied to the weather images `Satellite Images rules` are summarized as follows: () The application of data mining metho d to image `BBAAAAECCCDBBEEE DATABASE` classi�cation and retrieval. `R-tree sequence index` () Feature description from time-series data. `feature map` () Implementation of the result of classi�cation as the user retrieval interface. Figure : Overview of the system. () Construction of the whole system as a domainexp ert supp orting system. **3. TIME-SEQUENTIALDATA DESCRIPTION BY USING CLUSTERING** We describ e an overview of the system in Section . A **3.1 Data set description** clustering algorithm for time-sequential images and its exp erimental results are describ ed in Section . SecSatellite weather images, taken by GMS- and received tion describ es the algorithm of extraction of timeat the Institute of Industrial Science, Tokyo University, dep endent asso ciation rules and its exp erimental results. are archived at the Ko chi University weather page Section describ es details of the construction of the (http://weather.is.ko chi-u.ac.jp). The images used in database by using R-tree and the results of its implethis study are infrared band(IR: moisture band, wavelength of .- �m) images taken Japanese islands, which mentation. Section provides a conclusion. are of 0-pixels in width and 0-pixels in height. Each image is taken every hour, and ab out 000 images are **2. SYSTEM OVERVIEW** archived every year. Figure shows an example of the We constructed a weather image database that gathers image sequence. the sequential changes of cloud images and the domainexp ert analysis supp ort system for these images. We characterize the system's images using clustering metho d (Section ) and describ e the image changes in terms of the sequential cluster numb ers. Then we derive the time-dep endent asso ciation rules from the sequential data (Section ) and index them. The �ow of this system is shown in Figure and describ ed as follows: step Clustering using a self-organizing map. step Generation of time-sequential data from a series of cluster addresses. Figure : Example of weather image(GMS- IR step Extraction of time-dep endent rules from band) sequence. the time-sequential data. step Indexing of rules and a series of cluster addresses by using R-tree, and conWe considered that conventional image pro cessing methstruction of the database. o ds might b e unable to detect moving ob jects such as step Searching for time-sequential variation the cloud masses that change their p osition and form patterns and browsing for the retrieved during the time sequence. Thus we used the followdata in the form of animation. ing SOM-based metho d for the automatic clustering of 

83 

images by using the raster-like scanned image intensity input vector the to a unit i as vectors as the inputs. Ui = [ui ; ui ; ui ; � � �; uin ]: () **3.2 ClusteringandKohonen’sself-organizing** Initial values of uij are given randomly. **map** step E is compared with all Ui , and the b est Similarity analysis from full-text databases or image matching no de which has the smallest databases use sophisticated retrieval metho ds based on Euclidean distance jE � Ui j is deterthe indexing of space or the indexing of feature spaces. mined and signi�ed by the subscript c, Clusteringof these methobasedds.onWhensimilaritstandardy is onefeatureof thepatternsextensionsare c = argmini jE � Ui j: () not given for the ob ject data set, distance criteria in the step Weight vectors of the b est matching no de feature spaces are used to divide the ob ject set into the c and its neighb ors,Nc , are adjusted to subset. This provides the rough structure to the given increase the similarity as follows, non-structured information. new old uij = uij + �uij () Kohonen's self-organizing map (SOM)[ ] is a paradigm which was suggested in   0. The SOM is a two layer where nettureworkrelationsthat organizesbased on ainputfeaturepatternsmap bythroughdiscoveringiterativfea-e �uij = � �(ej �0 uij ) ((ii = NNcc )) () non-sup ervised learning. t �t = �0 � () � T � `competition` The �t is the learning rate at the time `layer` of t iterations, �0 is the initial leaning rate, and T is the total numb er of iter- `N x M` ations. `grid` step The learning rate and the size of neighb or decreases as the learning pro ceeds. The input signals E are classi�ed into the activated (nearest) unit Uc of the input layer and pro jected onto the comp etition grids. The distance on the comp etition grids re�ects the similarity b etween the patterns. After the training is completed, the obtained comp etition grids. i.e., the feature map, represents a natural relationship b etween the patterns of input signals entered into the network. `input layer unit1 unit2 unitn` **3.3 Clustering by two-stage SOM** `input vector E` Figure represents the problem of clustering of weather images. Two images in Figure (a) are considered to Figure : Basic structure of Kohonen's selfhave features similar to those of typho on and a front, alorganizing map though their forms and p ositions are changed. When we take the input vectors simply as the raster-like scanned Figure presents basic schematic structure of Kohointensity vectors, these images are classi�ed into the difnen's self-organizing map. The network, a combination ferent groups based on the spatial variations of intensity. of the input layer and the comp etition layer, is trained We considered that this di�culty is avoided by dividing through non-sup ervised learning. Each unit of the inthe images into blo cks as shown in Figure (b). put layer has a vector whose comp onents corresp ond to the input pattern elements. The pro cedure adopted here, named two-stage SOM, is describ ed as follows: The algorithm of the SOM is describ ed as follows: stage Clustering of pattern cells step Let the input pattern vector E R n as, step All Images are divided into N�M blo cks. E = [e ; e ; e ; � � �; en ] () step SOM generates the feature map, taking the each blo ck's raster-like scanned instep Assume the weight of union from the tensity vectors as the input vectors. 

84 





Figure : Problem for clustering of weather images. step The SOM map cluster address is used to describ e blo cks of the original images. We refer to this characterized blo cks as the pattern cells. stage Clustering of the images by using frequency histograms of pattern cells. step Each image is represented as the freFigure : Clustering of weathereather images byy SOM. quency histogram of the pattern cells. step The feature map of SOM is generated by taking the frequency histogram of ate the accuracy of clustering quantitatively,titatively,ely,, wee de�ned each image's pattern cell as the input. the followingwing parameters, P r ecision = B =(B(BB + C );; () Extraction of frequency histogram of pattern cells in R ecal l = B =(A(AA + B );; () step of stage reduces the spatial information of blo cks included in the images. Thus this pro cess enwhere A is the numbumbb er of the nonrelevantantt images that ables to classify time-series images which have similar are classi�ed intoto the cells, B is the numbumbb er of the releob jects at di�erent p ositions as the same typ e of images. vantantt images that are classi�ed intoto the validalid cell, and C is the numbumbb er of the relevantantt images that are classi�ed Figure schematically shows the ab ove-describ ed prointoto the invalidvalidalid cell. cess of the two-stage SOM. The images that have similar ob jects are clustered into similar cells on the second Table show the precision values for and to stage feature map. Note that the di�erence in seasons b e .0% and .%, resp ectively, and that the values of is not distinguished at this p oint. recall are .% and .%, resp ectively. These values indicate that the clustering of weather images by two- **3.4 Result of experiments on clustering** stage SOM can successfully learn the features of images In our exp eriments, we sampled GMS- IR images with and can classify them with a high degree of accuracy. hour time intervals obtained b etween and   , Table : Accuracies of clustering and comp osed two data set for and which year Recall Precision include 0 and images, resp ectively. We de�ned .0%(/0) .%(/0) numb er of blo cks for each image to b e � . The .%(/ ) .%(/ ) sizes of feature maps of b oth �rst stage SOM and second stage SOM are de�ned to b e � . Learning pro cesses Furthermore, we describ e the semantic representation of are iterated 000-0000 times. clusters by sp ecifying the season in which the clusters are observed, based on the frequency of each cluster evThe results of the exp eriment show that images with ery month, and by describing the representative ob ject similar features are classi�ed into similar cells. To evalusuch as front or typho on by means of visual observation 

Figure : Clustering of weathereather images byy SOM. ate the accuracy of clustering quantitatively,titatively,ely,, wee de�ned the followingwing parameters, P r ecision = B =(B(BB + C );; () R ecal l = B =(A(AA + B );; () where A is the numbumbb er of the nonrelevantantt images that are classi�ed intoto the cells, B is the numbumbb er of the relevantantt images that are classi�ed intoto the validalid cell, and C is the numbumbb er of the relevantantt images that are classi�ed intoto the invalidvalidalid cell. 

85 

of images in the cluster from a domain-exp ert like view. Table shows the semantical descriptions of and Table : Semantical description of each cluster.   . The distribution of similar clusters for is difCluster address is represented by the character ferent from since we p erformed the SOM leaning of A, B, C, � � �, P for the raster-like cells scanned for these datasets indep endently. However, most of the from the upp er left corner to the lower right groups are observed in b oth maps, thus the obtained recorner. sult is meaningful even in the view of the domain-exp ert knowledge. cluster season prominent characterisThe obtained map is considered to b e dep endent on address tics the blo ck size of the original images and size of SOM map. Hierarchical division of each blo ck in the origiA spring sumfront, typho on nal image by using standard deviation of intensity will mer b e a solution to the determination of blo ck sizes. The B,C spring high pressure in the west algorithm of Growing Hierarchical SOM[], which is autumn and low pressure in the east capable of growing b oth in terms of map size as well as the three-dimensional tree structure, will b e e�ective D,H spring band-like high-pressure autumn for the adaptation of map size. E autumn migratory anticyclone F spring front **4. SEQUENTIAL ANALYSIS AND EX-** autumn **TRACTION OF TIME-DEPENDENT** G autumn linear clouds **ASSOCIATION RULES** winter **4.1 Association rules** I summer Paci�c high pressure, front Asso ciation rules are one of the key concepts of data mining[]. An item i is de�ned to b e a minimum element J spring sumrainy season's front, tyfor extraction of rules. We de�ne the set of items I and mer pho on transaction database D as K,L winter winter typ e, whirl-like cloud I = [i ; i ; � � � ; im ]; D = [T ; T ; � � � ; Tn ]; (Ti � I ); ( ) M summer Paci�c high pressure, typho on wherecombinationTi is anof kelemenitemstisofreferredthe transactionto as the itemdatabase.set withA N spring sumhigh pressure, typho on mer the length of k . O winter cold front Then asso ciation rule is represented as P spring migratory anticyclone autumn X ) Y (X ; Y � I ; X \ Y = �): (0) Evaluating parameters of the asso ciation rule X ) Y , supp ort and on�dence, are de�ned by suppor t(X ) Y ) = N (Ti j Ti � X [ Y ) ; () clusteraddress season prominentics t characterisN (D ) A,F,O spring sumfront, typho on conf idence(X ) Y ) = N (NT(i Tj iTji T�i �X X[ )Y ) ; () B merspring front, migratory anticyautumn clone where N is the numb er of transactions in each condiC summer Paci�c high-pressure tion. These parameters re�ect the pro cessing time and D autumn migratory anticyclone e�ectiveness of the rule. E spring band like high-pressure autumn Rule extraction is de�ned to �nd all rules that have G spring sumPaci�c high pressure, larger con�dence and supp ort than the minimum threshmer front old de�ned by users. The following pro cess describ es the H spring sumrainy season's front extraction of asso ciation rules. mer I,K,N winter winter typ e, linear . The item set that has larger supp ort clouds(high pressure than the threshold is selected (referred in the west and low to as the large item set). pressure in the east) J summer Paci�c high pressure, . The rules that have larger con�dence front than the threshold are selected from the L,M winter cold front large item set. P autumn linear clouds winter 





86 

**4.2 Time-series pattern analysis** where n is the total numb er of the events in the seTime-sequential data analysis is the metho d used to exquence. Figure shows a representation of event setract unknown patterns from time-sequential informaquence in the case of Sif � . tion, is related to the asso ciation rules, and is remarkable in the area of data mining. Episo de rule[0][] are known as one of those metho ds. Episowindodesw. areEvende�nedts in timeas thesequenceevent pairsareinrepresena certaintedtimeby `B B’B B A AA’A E C CC’C C D B B’B B AA’A B clusterEvent` (e; t), where e is the class of the event and t is its o c- `1 5 10 15 20 time` currence time. In Figure , an event sequence given by a `neighbor=8` string are represented by (E,)(F,)(A,)(B,)(C,) � � � (D, ), where A, B, C are the event classes, and the numb er is the time of o ccurrence. Figure : Example of description of cluster sequence, event sequence, and extraction of timeFigure represents simple examples of episo de rules dep endent asso ciation rules. such as those regarding serial episo des as "event B o c- curs after event A", parallel episo des such as "b oth events E and F o ccurs", or a combination of serial episo des We extract the event pairs that o ccur closely in the seand parallel episo des such as "event C o ccurs after event quence by intro ducing the neighb orho o d distance. The E and F". pattern change E is then represented by E = h[ei ; ej ]; neig hbor i(i = ; � � � ; n � ; j = ; � � � ; n); () `E` where [ei ; ej ] represents a combination of the two events `A B F C B A episode` of ei and ej which satis�es i < j , and neig hbor is the neighb orho o d distance. `E F A B C E F C D B A D event` Although neig hbor is an idea similar with a time win- `30 35 window 40 45 50`<sup>`time`</sup> dow in episo de rules[0][], we use this concept as the time interval necessary to extract only serial episo des such as A ) B . We exclude parallel episo de rules and Figure : Example of event sequence and combination of serial/parallel episo de rules which are episo de. included in [0][]. In order to de�ne how closely these events o ccur, ManFurthermoreurthermore wee use the metho d of co-o ccurring termnila et al.[0] considered the time window that is shifted pair [] to evaluatealuate the set of combinationsbinations of eventsentsts in an orderly manner in the sequence. Candidates of whichh o ccurs closely and frequentlytly in the lo cal time episo des are extracted as the co-o ccurring events in the window,w, and to extract them. The cohesion of the evententt time window. And combinations of events that have eii and ejj in a lo cal time windoww is representedted byy largerterminedfrequenciesto b e episothandes.theAthresholdmore �exiblefrequencymethoared thatdecohesion(ei ; ej ) = Ef (ei ; ej ) ; () uses the minimal o ccurrence interval has also b een sugp[f (ei ) � f (ej )] gested in []. where f (ei ) and f (ej ) are the frequencies of ei and ej , resp ectively, and Ef (ei ; ej ) is the frequency of the co- **4.3 Time-dependent association rule** o ccurrence of b oth ei and ej . The time-dep endent asIn this study we present time-dep endent asso ciation rules so ciation rules are extracted when the event pair has which mo dify the episo de rules using the concept of larger cohesion than the threshold. cohesion, and represent lo cal asso ciation rules such as "weather pattern B o ccurs after weather pattern A". The pro cedure of extraction of time-dep endent asso ciation rule is shown schematically in Figure , and is First we generate the sequential data of a weather patdescrib ed in the following: tern using cluster addresses as (A; ); (A; ); (C ; ); � � �. We de�ne the event as continuously o ccurring clusters. step The frequency of each event is deterThe event ei in the sequence is then represented by mined (Fig. ()). ei =< Ci ; Sif ; Tis ; Tie > (i = ; �; �; n); () step A combinational set of event pairs are determined as the candidates of rules, where Ci is the cluster addresses, Sif is the continuity, assuming the neighb orho o d distance (FigTis is the starting time, and Tie is the ending time. The ure ()). sequence S is then represented by step Event pairs are sorted lexicographically S =< e ; e ; � � �; en >; () in regard to the �rst event (Fig. ()). 

Furthermoreurthermore wee use the metho d of co-o ccurring termpair [] to evaluatealuate the set of combinationsbinations of eventsentsts whichh o ccurs closely and frequentlytly in the lo cal time window,w, and to extract them. The cohesion of the evententt eii and ejj in a lo cal time windoww is representedted byy 

87 

step Event pairs are sorted lexicographically in regard to the following event (Fig. Table : Relationship b etween neig hbor and numb er of rules. ()). step The candidates' frequency of co-o ccurrence neig hbor 0 0 0 0 0 and cohesion are calculated(Fig. ()). numb er of rules(  ) 0 step The event pairs that have larger cohenumb er of rules(  ) 0 sions than the threshold are extracted. **5. CONSTRUCTION OF WEATHER IM-** e e freq e1 e2 e1 e2 **AGE DATABASE** `B’ B’ 2 B’ A’ A’ C’` We constructed a weather image database which re- `A’C’` (1) `A’C’ 21` (2) `B’A’ C’C’` (3) `A’B’ A’B’` trievimages,es thevisualizesab ove-describtime-depedendencharacteristicst variation pattern,of weatherand `B’ B’ 2 A’ B’ B’ C’` supp orts the analysis and scienti�c discovery by domainexp erts. `A’ A’ 2 C’ B’ B’ A’ C’ A’ C’ B’` First we indexed the sequential time data by using events `B’ A’ C’ A’` and time-dep endent asso ciation rules, and constructed a weather satellite image database which contains index e1 e2 e1 e2 f(e1) f(e2) Ef cohesion information regarding patterns such as time variations `A’ C’ A’ C’ 2 2 1 0.50` in weather. `A’ B’ A’ B’ 2 1 1 0.71` (4) (5) `B’ A’ B’ A’ 2 2 2 1.00` **5.1 Definition of attributes** `B’ C’ B’ C’ 2 2 2 1.00` We stored weather patterns extracted in the exp eri- `B’ A’ B’ A’ 2 1 1 0.71` ments in the following three tables: "series", "date id", `C’ B’ C’ B’ 1 2 1 0.71` and "e series" that represent contexts of time-dep endent `C’ A’ C’ A’ 1 2 1 0.71` rules, the relationship b etween the observation date and image ID, and the contents of time-dep endent rule candidates (those obtained in step in .), resp ectively. Figure : Pro cedure of a extraction of timedep endent asso ciation rule, where e and e are the �rst event and the following event, resp ecTable : List of three table "series", "data id", tively, f (e) and f (e) are the frequencies of e "e series" and e , resp ectively, Ef is the frequency of co(a) "series" that represents time-dep endent rule in which o ccurrence, and cohesion is the strength of col term is the cluster numb er of left term, r term is hesion b etween e and e . The neighb orho o d data(rectangular),the right term, loandcation�rst isandthelastreferenceare the imageto theID R-treeof the distance is taken to b e in this case. l term starting p oint and r term ending p oint, resp ectively .) Strongly correlated event pairs in neig hbor have large l term r term cohesion lo cation �rst last cohesion even if each event o ccurs less frequently. Inint int �oat b ox int int versely, weakly correlated event pairs have small cohesion even if each event o ccurs very frequently. (b) "date id" that indicates the relationship b etween the observation date date and image ID id. **4.4 Result of experiments regarding time-** id date **dependent association rules** int int We p erformed the exp eriment by applying the ab ovedescrib ed time-dep endent asso ciation rule to the result (c) "e series" that indicates the candidate of time-dep endent of the clustering describ ed in .. Here we take the event rules, where ter m is the cluster numb er, f ir st and l ast threshold of cohesion as 0., and neig hbor ranging from areter mthe, respimageectivIDely.of the starting p oint and ending p oint of 0 to 0. Since we sampled data every hours, the virtual length of neig hbor is b etween . days and . term �rst last days. int int int Table shows the relationship b etween neig hbor and the numb er of extracted rules. Although the assessment _5.1.1 Indexing by using R-tree_ of the context of the extracted rules is ongoing, the reWe indexed the image IDs at the starting and ending sult suggests the similar numb ers of rules are extracted p oint of the obtained pattern using R-tree. As shown from the di�erent year's data set, which indicates that in Figure , spring encloses March to May, and summer our present metho d is useful and robust. encloses June to August. Taking note of this relation, 

88 

we index the enclosure relation b etween seasons and = t.first and t.id = t.last and t.first months, and index the starting and the ending times < t.first order by t.first of variation patterns. This allows each variation pattern to contain an index which includes the enclosure "Search for weather patterns in which typhoon relations by month or season as keys. occurs within 0 days after the development of front and typhoon during days." `spring summer season` select t.first, t.last, t.date, t.date from series t, e series t, date id t, date id t `3 4 5 6 7 8 month` where (t.l term = 0 or t.l term = or t.l term = or t.l term = or t.l term = ) `s_cluster` and (t.r term = or t.r term = or t.r term = `time` or t.r term = or t.r term = or t.r term `1 10 20 30 40` = or t.r term = or t.r term = or t.r term Figure : Indexing by using R-tree, remarking = ) at the continuing sequence. and t.first >=(t.last - ) and t.id = first and t.id = last and(t.term = 0 or t.term = **5.2 Query by SQL** or Rule storage in the database enables the retrieval of t.term = or t.term = ) and the various queries by using SQL statements. We show t.first >=(t.last - 0) and t.last <= t.last examples of the queries and corresp onding SQL statement in the following: **5.3 Result of implementation** "Search for typhoons that occurred within 0 Figure 0 shows the browse page of the system which days after July th,   ." retrieves weather images using R-tree index. Entering the SQL in the upp er frame p erforms retrievals. select first, last, t.date, t.date This example shows the results of query: "Is there any from series, date id t, date id t weather pattern in which a typho on o ccurred in 0 days where t.date = 0 and t.id = first after the development of front and typho on during and t.id = last and(r term = 0 or r term = days". Seven p erio ds are retrieved and listed in the or r term = or r term = ) and location lower left frame as the result, and the weather variation @ '((0, 0), in these p erio ds is shown as an animation in the lower right frame. (0,))'::box The problem of this metho d is that the accuracy of clus"Search for weather changes between one tytering and the semantical description of clusters changes phoon and the another." the retrieval results signi�cantly. Interactive pro cessing interface, such as adjustment of the sample data or asselect first, last, t.date, t.date sumed parameters with metrological exp erts who are from series, date id t, date id t p otential users, are required to solve this problem. where(l term = 0 or l term = or l term = or l term = ) and(r term = 0 or r term **6. CONCLUSION** = or r term = or r term = ) and t.id We applied clustering and time-dep endent asso ciation = first and t.id = last rules to a large-scale content-based image database of weather satellite images. Each image is divided into or N � M blo cks and automatically classi�ed by two-stage select t.first, t.last, t.date, t.date SOM. We also extracted unknown rules from timesefrom e series t, e series t, date id t, quential data expressed by a sequence of cluster addate id t dresses by using time-dep endent asso ciation rules. Furwhere(t.term = 0 or t.term = or t.term thermore, we develop ed a knowledge discovery supp ort = or t.term = ) and(t.term = 0 or t.term system for domain exp erts, which retrieves image se= or t.term = or t.term = ) and t.id quences using extracted events and asso ciation rules. Here cluster addressees are represented by numb ers http://zeus.is.ko chi-u.ac.jp/~takimoto/java/servlets/ ranging from 0 to instead of characters A-P in Table indexe. . html 



89 

- [] O. R. Zaiane, J. Han, Z. N. Li, J. Y. Chiang and S. Chee. Multimedia-miner : a system prototyp e for multimedia data mining. At Proceedings ACM-SIGMOD Conference on Management of Data, system demo,   . 

- [] U. M. Fayyad, S. G. Djorgovski and N. Weir. Automatic the analysis and cataloging of sky surveys. Advances in Know ledge Discovery and Data Mining, pages {  , AAAI Press/MIT Press,   . 

- [] M. C. Burl, L. Asker, P. Smyth, U. M. Fayyad, P. Perona, L. Crumpler and J. Aub ele. Learning to recognize volcano es on venus. machine learning, 0(/):{ , February,   . 

- [] P. Smyth, M. C. Burl and U. M. Fayyad. Mo deling sub jective uncertainty in image annotation. In Advances in Know ledge Discovery and Data Mining, pages { . AAAI Press/MIT Press,   . 

- Figure 0: Example of the result of retrieval result from sequential image data. [ ] T. Kohonen. Self-organizing maps. Springer,   . [0] H. Mannila, H. Tovinen and A. I. Verkano. 

- From the p ersp ective that high-level queries make the Discovering frequent episo des in sequences. In analysis easier, we stored the extracted rules in the First International Conference on Know ledge database to admit sophisticated queries describ ed by Discovery and Data Mining(KDD' ), pages SQL. The retrieval resp onses to various queries shows 0{ , AAAI Press,   . the usefulness of this approach. [] H. Mannila, H. Tovinen. Discovering generalized episo des using minimal o ccurrences. In Proceeding 

- The framework presented in this study, clustering ) of the Second International Conference on transformation into time-sequential data ) extraction Know ledge Discovery and Data Mining(KDD' ), of time-dep endent asso ciation rules, is considered to pages {, AAAI Press,   . b e useful in managing enormous multimedia datasets which include sequential patterns such as video infor[] T. N. Raymond, J. Han. E�cient and e�ective mation and audio information. clustering metho ds for spatial data mining. In Proceeding of 0th VLDB Conference, Santiago, 

- **7. ACKNOWLEDGEMENTS** Chile,   . The authors are grateful to Prof. T. Kikuchi for of[] O. Konishi. A statistically build knowledge based fering us well-prepared GMS- images. This research terminology construction system (in Japanese). is partly supp orted by grants-in-aid for intensive reTransaction of Information Processing Society of search(A)()(Pro ject 00) from the Ministry of Japan `!$` 0(): { ,   . Education, Science, and Culture of Japan. [] K. Katayama and O. Konishi. Construction 

- **8. REFERENCES** satellite image databases for supp orting [] J. Fomg,(Edt.). Data mining, data warehousing & knowledge discovery(in Japanese). Transaction of client/server databases. In Proceedings th Information Processing Society of Japan, International Database Workshop, Springer,   . 0(SIG(TOD)): {,    . 

- [] A. F. Alex and H. L. Simon. Mining very large [] K. Katayama. and O. Konishi. Discovering databases with paral lel processing. Kluwer co-o ccurencing patterns in event sequences (in Academic Publishers,   . Japanese). DEWS'  ,    . 

- [] R. Agrawal, T. Imelinski and A. Swani. Mining in [] D. Merkl and A. Raub er. Uncovering the asso ciation rules b etween sets of items in large hierarchical structure of text archives by using database. In Proc. ACM SIGMOD International unsup ervised neural network with adaptive Conference, pages 0{,   . architecture. In PAKDD 000, pages { , 000. 

- [] R. Agrawal and R. Srikant. Fast Algorithms for mining asso ciation rules. In Proceedings of 0th International Conference on VLDB, pages {  ,   . 

90 

### **Data Mining from Functional Brain Images** 

###### Mitsuru Kakimoto 

Corporate Research & Development Center, Toshiba Corporation 

- 1, Komukai Toshiba-cho, Saiwai-ku, Kawasaki 212-8582 Japan 

mitsuru.kakimoto@ toshiba.co.jp 

###### Chie Morita 

Corporate Research & Development Center, Toshiba Corporation 

- 1, Komukai Toshiba-cho, Saiwai-ku, Kawasaki 212-8582 Japan chie.morita@ toshiba.co.jp 

Hiroshi Tsukimoto Corporate Research & Development Center, Toshiba Corporation 

- 1, Komukai Toshiba-cho, Saiwai-ku, Kawasaki 212-8582 Japan 

- hiroshi.tsukimoto@ toshiba.co.jp 

###### **ABSTRACT** 

discovery from real world data grows, however, metho ds for identi-tideriving knowledgewledge from structured data (including time sefuncries, images and data embb edded in graphical structures) are b e- strongly desired. 

Recent advances in functional brain imaging enable identi-tideriving knowledgewledge from structured data (including time se�cation of active areas of a brain p erforming a certain funcries, images and data embb edded in graphical structures) are tion. Induction of logical formulas describing relations b e- strongly desired. tween brain areas and brain functions from functional brain images is a category of data mining. It is di�cult, howKnowledge discovery from functional brain images is a canever, to apply conventional mining techniques to functional didate �eld for the application of such metho ds. As a result brain images due to several reasons, such as the di�culty of of the ongoing development of non-invasive measurement of reducing images to symb olic data, p ossible existence of corbrain function, detailed functional brain images can b e obrelations b etween adjacent pixels in a image and the limited tained, from which the relations b etween brain areas and numb er of samples available from a single sub ject. Tsukibrain functions can b e understo o d. These relations, howmoto and Morita presen ted an algorithm for data mining ever, could b e complicated since several brain areas might from functional brain images and showed that the algorithm b e resp onsible for a brain function. Some of them are conworks well for arti�cial data. The algorithm consists of two nected in series, and others are connected in parallel. Brain steps. The �rst step is nonparametric regression. The secareas connected in series are describ ed by \AND" and brain ond step is rule extraction from the linear formula obtained areas connected in parallel are describ ed by \OR". Thereby the nonparametric regression. The authors have applied fore, the relations b etween brain areas and brain functions the algorithm to real f-MRI images. This pap er rep orts that are describ ed by rules. the algorithm works well for real f-MRI data and has led to the discovery of certain rules for a �nger tapping action and It is of crucial imp ortance for researchers involved in mapa sp eech-related action. ping brain functions to �nd such rules from functional brain images. Although several statistical metho ds, such as the **Categories and Subject Descriptors** Statistical Parametric Map[] and Indep enden t Comp onent I.. [Learning ]: Concept learning; J. [Life And MediAnalysis[], are b eing used in human brain mapping, these cal Sciences]: Medical information systems metho ds can only present some principal areas for the function and cannot discover rules. Furthermore, several factors prevent conventional data mining techniques from b eing ap- **Keywords** plied to functional brain imaging. First, observed images Knowledge discovery, Functional brain images, Nonparaconsist of real values and it is not easy to reduce them to metric regression, Rule extraction, Human brain mapping simple symb olic data such as \active" / \inactive". Second, it is exp ected that strong correlations exist b etween adja- **1. INTRODUCTION** cent pixels in an image. Therefore, a mining scheme should Conventional data mining techniques deal with symb olic take the structure of the image into account so as to imand/or numerical data contained in tables in which the indeprove its quality. Third, in a usual function brain imaging p endence of rows is tacitly assumed. This simple structure exp eriment, the numb er of samples obtained from a single makes the data easy to mine. As demand for knowledge sub ject is limited. This scarcity of samples makes it hard to obtain accurate rules. 

© The copyright of this paper belongs to the paper's authors. Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. 

Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 

(O.R. Zaïane, S.J. Simoff, eds.) 

Tsukimoto and Morita ha ve presented a new algorithm capable of extracting rules from such structured data, which is now called the Logical Regression Analysis(LRA). They con�rmed that the LRA works well for arti�cial functional brain image data[]. The LRA consists of two steps. In the �rst step, a linear formula describing the relation b etween an image and a brain function is derived using regression 

91 

analysis. In order to obtain a linear formula from relatively few samples, nonparametric regression is used. The subsequent step extracts rules from the linear formula obtained in the previous step. 

Table : Data sample � class S on o� � o� Y S on on � o� N S o� o� � on N S o� on � on Y S on o� � o� N S o� on � on N S o� o� � on Y If an activity of a pixel is strongly correlated with the class value, the pixel is considered to b e a part of an area resp onsible for the function. On the contrary, if a pixel is always inactive, it is considered to b e a part of inhibitory area. Otherwise, i.e. a pixel's activity do es not have any correlation with the class value, it is regarded as irrelevant to the function. Combining pixel values of resp onsible areas and negation of pixel values in inhibito ry areas pro duces a logical formula that describ es a rule governing the brain function. It is thus clear that rule extraction from functional brain images is formulated as a typical sup ervised inductive learning. 

This pap er rep orts the applicatio n of the LRA to real f- MRI data obtained in the exp eriments of �nger tapping and sp eech actions. Section brie�y outlines a scheme of the data mining from functional brain images. Section gives exact formulation of nonparametric regression used in the analysis. Section explains the rule extraction algorithm from a linear formula. Section shows exp erimental results obtained by applying the LRA to real f-MRI images and discusses its meaning in brain science. Conclusions are presented in Section . **2. DATA MINING FROM FUNCTIONAL BRAIN IMAGES** Fig. is a schematic illustration of a -dimensional functional brain image with a circle representing a contour of a brain. In Fig., the image is divided into �(=) pixels. In an exp eriment using f-MRI, sub jects are told to do some task and rest for a while rep eatedly. If a pixel includes or intersects brain areas resp onsible for that task, activation of the area by the task results in enhanced value of the pixel. Detecting di�erence of the value of a pixel b etween the image taken while the sub ject is doing the task and one while he/she is resting thus makes it p ossible to identify areas resp onsible for the task. 

What makes the rule extraction di�cult, however, is that variation of a pixel value correlated to brain function is so subtle that there is no clear-cut way to reduce observed numerical pixel values to simple `on'/`o� ' symb ols. Combining regression analysis and rule extraction, the LRA evaluates quantitative signi�cance of each pixel resp ecting the brain function, which makes fast and rigorous rule extraction p ossible. 

`1 2 3 4 5 6` **3. NONPARAMETRIC REGRESSION** `7 8 9 10 11 12` As explained earlier, the LRA uses regression in its �rst step. In functional brain image analysis, each image has more than a thousand pixels, which mean that there are more than a thousand indep endent variables. The numb er of samples ob- `13 14 15 16 17 18` tained in a single exp eriment is around one hundred, which is signi�cantl y small compared with a numb er of indep endent variables. It is therefore imp ossible to use conventional `19 20 21 22 23 24` linear regression which requires a larger numb er of samples than the numb er of indep endent variables. Another problem inherent in image analysis is that strong `25 26 27 28 29 30` correlation is exp ected b etween adjacent pixels. This also applies in the analysis of functional brain images where contribution of each pixel to brain function cannot b e regarded `31 32 33 34 35 36` as truly indep endent. As shown b elow, these two problems are resolved simultaneFigure : Brain image ously in a framework of nonparametric regression. The next subsection explains the conventional -dimensional nonparametric regression[]. Extension to -dimensions, which is used in the analysis of functional brain images, is describ ed Although values of pixels in a real f-MRI image are continin the later subsection. uous, for simpli�catio n, we assume here that the values are binary, that is, on(active) or o�(inactive). Also, we assume that there are seven samples. Table shows the data. In **3.1 1-dimensional nonparametric regression** Table , 'on' and 'o� ' mean that the pixel is active and inNonparametric regression is de�ned as follows: Let y stand active, resp ectively. Y in class shows that a sub ject is doing for a dep endent variable and tj (j = ; ::; m) stand for ina certain task and N shows that he/she is resting. dep endent variables. Then, the regression formula is as fol- 

92 

lows: **3.2 2-dimensional nonparametric regression** y^ = X aj tj + e(j = ; ::; m); Theviousnonparametricsubsection is extendedregressiontosctheheme-dimensionalexplained in casethe pre-and where aj are real numb ers and e is a zero-mean random applied to f-MRI data. In -dimensional data, there are four variable. When there are n measured values of y , adjacent measured values , whereas in -dimensional data, there are only two. Hence, the evaluation value for the cony^i = X aj tij + ei (i = ; ::; n): tinuity of co e�cients aj is mo di�ed so that continuity with adjacent four pixels is taken into account. For example, In usual linear regression, the co e�cients aj are de�ned so pixel in Fig. has four adjacent pixels ( , , and ), that residual error(i.e., di�erence b etween measured value of and the evaluation value is as follows: y and calculated value by the formula) is minimized, whereas in nonparametric regression, continuity of co e�cients is also (a � a ) + (a � a ) + (a � a ) + (a � a ) : taken into account[Miwa, private communication]. Therefore, the evaluation value is now describ ed as follows: **4. RULE EXTRACTION** n m =n X(yi � y^i ) + � X (aj + � aj ) **4.1 Rule extraction in the discrete domain** i= j = In this subsection, a metho d for rule extraction in the diswhere y^^ is an estimated value.alue. The second term in the ab ovevee cretefunctiondomainwhicish explained.is nearest Theto amaingivenidealinearis toform�nd ulaa Boinoleanthe formulaula is the di�erence of �rst order b etweenweeneen the adjacentt Bo olean function space. 

where y^^ is an estimated value.alue. The second term in the ab ovevee formulaula is the di�erence of �rst order b etweenweeneen the adjacentt co e�cients, that is, the continuity of the co e�cients. � is the co e�cient of continuity. Consideration of two extreme cases facilitates understanding of the characteristics of the ab ove evaluation value. When � ! 0, the evaluation value consists of only the �rst term, that is, error, which means the usual regression. In this case, the e�ective numb er of co e�cients is exactly the same as the actual numb er of co e�cients. On the other hand, if � is in�nitely large, the evaluation value consists of only the second term, that is, continuity, which means that the error is ignored and aj is a constant. This is equivalent to the case where there is a single co e�cient. The e�ective numb er of co e�cients is thus controlled by the value of �. By determining the value of � adaptively, a nonparametric regression scheme can handle the situation in which the numb er of samples available is smaller than the numb er of co e�cients. 

Let (fi ) b e the values of a linear formula. Let (gi )(gi = 0 or ) b e the values of Bo olean functions. The basic metho d is as follows: gi = (fi � 0:); � 0(fi < 0:): This metho d minimizes Euclidean distance. 

Generally, let g (x ; :::; xn ) stand for a Bo olean function, and let gi (i = ; :::; n ) stand for values of a Bo olean function and then the Bo olean function is represented by the following formula: 

n g (x ; :::; xn ) = X gi ai ; i= where P is disjunction, and ai is the atom corresp onding to gi , that is, n n ai = Y e(xj ) (i = ; :::; ); j = where e(xj ) = � xxjj ((eejj == 0));; where Q stands for conjunction, x stands for the negation of x, and ej is the substitution for xj , that is, ej = 0 or . The ab ove formula can b e easily veri�ed. 

We determined the value of � using the leave-one-out method cross validation[], whose formulation can b e describ ed as follows. Let X stand for n � m matrix. Let tij b e an element of X. Let y stand for a vector consisting of yi . m � m matrix C is as follows: � C = 0B � � C B � � C ::: @ A 



Fig. shows a case of two variables, x and y. Crosses stand for the values of a linear formula and circles stand for the values of a Bo olean function. Values on the horizontal axis, 00; 0; 0 and , stand for the domains. For example, 00 stands for x = 0; y = 0. 

where DiagA is a diagonal matrix whose diagonal comp o- nents are A's diagonal comp onents. Then the co e�cients ^a = (a ; � � � ; am )t are obtained by ^ t � t a = (X X + n�o C) X y ; 

In this case, the values of the Bo olean function g (x; y ) are as follows: g (0; 0) = ; g (0; ) = ; g (; 0) = 0; g (; ) = 0: 



where �o is the � that minimizes the cross validation function C V . 

One might think of a neighb or consisting of eight surrounding pixels. We did not pursue this p ossibil ity. 

93 

###### **4.3 Extension to the continuous domain** 

Continuous domains can b e normalized to [0,] domains by some normalization metho d. So we assume here that the 1 values lie in [0,] domains without loss of generality. First, we have to present a system of qualitative expressions corresp onding to Bo olean functions, in the [0,] domain. The expression system is generated by direct prop ortion, reverse prop ortion, conjunction and disjunction. The direct prop ortion is y = x. The inverse prop ortion is y = � x, which is a little di�erent from the conventional one (y = �x), b ecause y = � x is the natural extension of the negation in Bo olean functions. The conjunction and disjunction will b e also obtained by a natural extension. The functions generated by direct prop ortion, reverse prop ortion, conjunction and dis0 junction are called continuous Bo olean functions, b ecause they satisfy the axioms of Bo olean algebra. For details, refer to []. In the domain [0,], linear formulas are approxxy imated by continuous Bo olean functions. The metho d for deriving such an expression is exactly the same as the one 00 01 10 11 in the discrete domain[], []. Figure : Approximation **5. EXPERIMENTS** Therefore, in the case of Fig. , the Bo olean function is as Two f-MRI exp eriments are conducted, each with a single sub ject. Data obtained consist of series of cross-sectional follows: brain images, i.e. slices(Fig. ). Nonparametric regression g (x;x; y ) is p erformed on each series of images and average residual = g (0;; 0)x�x�� y�� + g (0;; )xy�xy�� + g (;; 0)xy�xy�y�� + g (;; )xyxy error of the regression is calculated. Small error value of a = x�� y�� + xy�� + 0xy�xy�y�� + 0xyxy slice is deemed to b e an evidence of the existence of signals = x�y��y�y�� + xy�� correlated to the task on the slice. Rule extraction is p er= x:�� formed on these slices to identify brain areas related to the task. Detailed results of each exp eriment are given in the **4.2 The fast polynomial time algorithm** following subsections. A naivee implementationtation of the rule extraction ab ovevee requires computational time whichh growsws exp onentiallytially with `31` the numbumbb er of indep endentt variables.ariables. Tsukimoto presentedted `30` the p olynomial time algorithm[ ], [0], the outline of whichh `29` is noww describ ed. `28 27` Let a linear formula b e as follows: f = p x + ::: + pn xn + pn+ ; The Bo olean function whichh approximatesximates f is obtained byy the followingwing steps. `2 1 0 @` . Check if xi � �xik xik+ � �xil exists in the Bo olean function after the approximation b the follo formula: Figure : Slices 

g (x;x; y ) = g (0;; 0)x�x�� y�� + g (0;; )xy�xy�� + g (;; 0)xy�xy�y�� + g (;; )xyxy = x�� y�� + xy�� + 0xy�xy�y�� + 0xyxy = x�y��y�y�� + xy�� = x:�� **4.2 The fast polynomial time algorithm** A naivee implementationtation of the rule extraction ab ovevee requires computational time whichh growsws exp onentiallytially with the numbumbb er of indep endentt variables.ariables. Tsukimoto presentedted the p olynomial time algorithm[ ], [0], the outline of whichh is noww describ ed. 



The Bo olean function whichh approximatesximates f is obtained byy the followingwing steps. 



###### **5.1 Finger tapping** 

In a �nger tapping task exp eriment, the sub ject is asked to tap four �ngers with thumb using his right hand. 

- . Execute the ab ove pro cedures up to a certain (usually two or three) order. 

The exp erimental conditions are summarized as follows: 

94 

magnetic �eld intensity: .0 Tesla numb er of pixels: � numb er of slices: sub ject: male( years old ) numb er of task samples: 0 numb er of rest samples: 

- Fig.(slice No.) Activity in the right (dominant) motor-sensory area. 

- Fig. (slice No.) Neural activity was clearly observed in motor, sensory, and supplementary motor areas in the right (dominant) hemisphere, and di�usive activity in the left motor-sensory area. 

Table shows the error of nonparametric regression for each slice. Note that slices are numb ered from b ottom to top, i.e., slice 0 is lower part of the brain and slice is lo cated at the top of the brain. 

- Fig. (slice No.) Activity in the right (dominant) premotor area related to motor programming and pattern generation. 

� Fig.0(slice No.) Table : Error (Finger tapping) Activity in the right (dominant) premotor and suppleslice err. slice err. slice err. slice err. mentary areas. 0 0. .00 0. 0.  0.0 0. 0.  0.0 **5.2 Shiritori** 0. 0 0. 0.0 0. The next exp erimental task is shiritori, which is a well0. .00 0. 0. known Japanese word game for two or more players. Each 0.0 0.0 0 0.  0. player utters a word that starts with the same syllable as 0.0 0. 0 0.0 0. the last syllable of a word uttered by a previous player. An 0. 0. 0. 0 0. example is shown b elow. 0. 0.0 0. 0. toki ! ki mono ! (time) (wear)ear) Slices with small errors (0. or less) are listed as follows: no mimono ! nonkinki ! : : : (drink) (optimism) slice This pro cess is rep eated untiltil someone fails to come up with error 0.0 0.0 0.0 0.0 0.0 0.0 0.0 a word.ord. In our shiritori exp eriment,t, the sub ject is presentedted 

toki ! ki mono ! (time) (wear)ear) no mimono ! nonkinki ! : : : (drink) (optimism) This pro cess is rep eated untiltil someone fails to come up with a word.ord. In our shiritori exp eriment,t, the sub ject is presentedted a single Japanese character at the b eginning of each task p e- rio d, then he b egins playing shiritori by himself starting with the character. While doing the task, he do es not actually utter words but sp eaks silently. 



The errors of No. and No. slices are nearly .0, which means that these slices have no relations to �nger tapping. 

Figure - Figure 0 are graphical representations of the rules for slices of No. , , , , , and , resp ectively. In the �gures, white areas show activation areas related to �nger tapping and dark gray areas show inhibitio n areas. Note that these �gures illustrate cross sections seen from b elow, i.e., left side of �gures corresp ond to the right side of sub ject's head and vice versa. Note also that upp er side and lower side of �gures corresp ond to the front and back of sub ject's head, resp ectively. 

The exp erimental conditions are as follows: 



<!-- Start of picture text -->
magnetic �eld intensity: .0 Tesla<br>numb er of pixels: �<br>numb er of slices:<br>sub ject: male( years old)<br>numb er of task samples: 0<br>numb er of rest samples: 0<br><!-- End of picture text -->

Interpretations of these rules in terms of brain physiology are given as follows: Movements of the non-dominant hand usually induce neural activity in motor and sensory areas in b oth hemispheres, and cause higher activity in the dominant hemisphere (contralateral to the non-dominant hand). In this case, the sub ject was left-handed and he moved his right hand (nondominant). Higher activity was observed in the right (dominant) motor and sensory areas than in those on the left as shown in Figs. - . 

Table shows the errors of nonparametric regression. The result of nonparametric regression is worse than that of �nger tapping. In shiritori, no slice has an error of 0. or less and the least error is 0.. That means that shirotori is complicated and therefore is related to several areas such as sp eech area, vision area, auditory area, motor area, and so on. 

Slices with small errors (0. or less) are as follows: 

- Fig., , (slice No. , , ) Higher activity was observed in the right cereb ellum. The result agrees with the fact that the neural activity in the cereb ellum ipsilateral to the moving hand is higher than in the cereb ellum contralateral to the moving hand. 

slice error 0. 0. 0. 0. 0. There are strong correlations b etween shiritori and slices No., , , and , since errors in the slices are small. 

95 









Figure : Rule (Finger ) Figure : Rule (Finger ) Figure : Rule (Finger ) Figure : Rule (Finger ) 







Figure : Rule (Finger ) Figure : Rule (Finger ) Figure 0: Rule (Finger ) 

The cereb ellum predominantly connects with the contralateral frontaltal cortex, and the rightt cereb ellum wasas activatedated asso ciated with the left prefrontaltal area. 

Table : Error (Shiritori) tralateral frontaltal cortex, and the rightt cereb ellum wasas slice err. slice err. slice err. slice err. activatedated asso ciated with the left prefrontaltal area. 0 0.  0. 0. 0. 0. 0. 0. 0. 0. 0 0. 0. 0. Physiologic al meanings of other rules observed during the 0. 0. 0. 0. task are to b e studied in future. 0.0 0. 0 0. 0. 0. 0. 0.0 0. **6. CONCLUSIONS** 0. 0. 0. 0 0.  We have applied the Logical Regression Analysis to real f- 0. 0. 0. 0. MRI images obtained by exp eriments of �nger tapping and sp eech actions, i.e., shiritori tasks. It is con�rmed that the nonparametric regression extended for functional brain image analysis, which consists of the �rst step of the LRA, can Figure - Figure show rules for slices No. , , , successfully identify slices of a brain relevant to the tasks. and , resp ectively. Rule extractions, the second step of the LRA, p erformed on these relevant slices induced rules which are reasonably Some of the rules presented are interpreted as follows: interpreted in terms of brain physiology. **7. ACKNOWLEDGMENTS** � Fig. (slice No.) Wee wouldould likee to thank Dr. T. Kobayakawayakawaakawaawawaa of the National 

- Fig. (slice No.) Activationation of the left prefrontaltal area. The left prefrontaltal area wasas activatedated related to work-orking memory required for mentaltal wordord generation . 

Activationation of the left prefrontaltal area. Wee wouldould likee to thank Dr. T. Kobayakawayakawaakawaawawaa of the National The left prefrontaltal area wasas activatedated related to work-orkInstitute of Bioscience Human-Technology for instruction ing memory required for mentaltal wordord generation . and planning of f-MRI exp eriments. This research is partly supp orted by Grant-in-Aid for Scienti�c Research on Prior� Fig. (slice No.) ity Areas \Discovery Science" from the Ministry of EducaActivation of the right cereb ellum. tion, Science and Culture, Japan(grant 00). This showed that the cereb ellum was related to some cognitive functions in addition to motor functioning. **8. ADDITIONAL AUTHORS** 

96 







Figure : rule (shiritori ) Figure : rule (shiritori ) Figure : rule (shiritori ) 







<!-- Start of picture text -->
Figure : rule (shiritori Figure : rule (shiritori<br>) )<br><!-- End of picture text -->

- Additional authors: Yoshiaki Kikuchi (Tokyo Metrop olitan University of Health Sciences, Higashi-ogu --0, Arakawaku, Tokyo,- Japan email: ykikuchi@post.metro-hs.ac.jp) **9. REFERENCES** [] Eubank, R.L.: Spline Smo othing and Nonparametric Regression, Marcel Dekker, New York,  . 

- [] Friston et al.: SPM course notes,   . http://www.fil.ion.bpmf.ac.uk/spm 

- [] McKeown, M., Makeig, S., Brown, G., Jung, T.-P., Kindermann, S., Lee, T.-W., and Sejnowski, T.J. : Spatially indep endent activity patterns in functional magnetic resonance imaging data during the stro op color-naming task. Proceedings of the National Academy of Sciences, , pp.0-0, February   . http://www.cnl.salk.edu/~tewon/ica cnl.html 

- [] Morita,C. and Tsukimoto,H.: Knowledge discovery from numerical data, Know ledge-based Systems, Vol.0, No., pp.- ,   . 

- [] Posner, M.I., Raichle,M.E.: Images of Mind, W H Freeman & Co,   . 

- [] Stone, M.: Cross-validatory choice and assessment of statistical prediction (with discussion), Journal of the 

Royal Statistical Society, Series B, , pp.-,  . 

- [] Tsukimoto, H.: The discovery of logical prop ositions in numerical data. AAAI'  Workshop on Know ledge Discovery in Databases, pp.0-,   . 

- [] Tsukimoto, H.: On continuously valued logical functions satisfying all axioms of classical logic. Systems and Computers in Japan, Vol., No.. pp.-,   . 

- [ ] Tsukimoto,H. and Morita,C.: E�cient algorithms for inductive learning-An application of multi-linear functions to inductive learning, Machine Intel ligence , pp.- , Oxford University Press,   . 

- [0] Tsukimoto,H., Morita,C., Shimogori,N.: An Inductive Learning Algorithm Based on Regression Analysis, Systems and Computers in Japan, Vol., No.. pp.-0,   . 

- [] Tsukimoto,H. and Morita,C.: The Discovery of Rules from Brain Images, Discovery Science, Proceedings of the First International Conference DS' , pp. -0 , 



<!-- Start of picture text -->
  .<br><!-- End of picture text -->

- [] Tsukimoto,H: Extracting Rules from Trained Neural Networks, IEEE Transactions on Neural Networks, Vol., No., pp.- , 000. 

97 

### **Mining Cinematic Knowledge: Work in Progress** 

##### [An Extended Abstract] 

Duminda Wijesekera Daniel Barbar´a Department of Information and Software Department of Information and Software Engineering Engineering George Mason University, MS 4A4, George Mason University, MS 4A4, Fairfax, VA 22101, U.S.A. Fairfax, VA 22101, U.S.A. duminda@ise.gmu.edu dbarbara@ise.gmu.edu **ABSTRACT** �D5 ��5  (��>  /D��3�O= #@9: ( DG8<0���I �
��
��� ����! #"$#% #'&# ( &)*+ 
, = ( H0RU9:P.S  E��L� (�� �t 'F@G#=;?# G#=G^ ./0
213 #&(546#� #873 9:;� <03 /=$�>? 9@ A>? & � =O"VZ�K�=G�]#�8"f=�# &(�B�8"V (>�9: �Q= �B0�B>C�D��� � 0EF��B �&= # = (?=G�� (H, 9@�  R�H8 �
�B � �H?=H
 OG#��L (�L&#�B��8# "fD, #&#0IJ �)>?��#� �K #"� �L� MN=? � %F�>?��?�O��H, =�#/>? D9:>?�
 '�>O# =) "z #>OD (IJ �;XDt>O@0 ��HN0P "3F �B &%= #=��L DG%>? ���&6 %>LH >? �Q@R  #�>?�U 9( (�9: ( &Y� �$T�H�BZR:.S�H�O S=�U�BG .S 5 5�>O@ =$= (T �T >?U���H 9:/ = (��B= #"U�KDY ' >O&(# � R 3 �3 
Z�B0 O� �H"V0]yw 0?"V� & GK (G# "V #>W= (>?� #��B#>?�I$4X uvfsm?szuZ#x #vfsm#u]Z#� H0I)= ( H0Ri &(�;?yw #uvfsfE= (, �� "V #K� �Y�� (�E�Z9:?X� (J[ 6  # � <0' #"/ �& O>O0= (G# � >? 6�# (��BZ#> " G@R �= #=;ZIA\] ��=�� �� ���$ @9: (�9: L>? ���&3^@ Z.SH, # = (��ZH0RT� #>?O>?=;�#���>?�Y O;@ywO �O�BZ#>?� &(
"Q (>_ #! (�>? D9@ �S#  #� (�Y� #>?Y� (�� (��I  # ! LF@G#=�Y= #>?>? (6�>O# =�8 I/ � ��H � (�> �t '���HG# ��HN0¡ "#� H0� �&PF��B �& G >? &?= (= �Y #�&# #�H�>?�¢z�3�Z9:8%��==��B"V **Categories and Subject Descriptors** GL>? ���&X` a%bTcVdZefa'g�hieVj�kml$= >OD�=Y^@� D.S� &( .S�H�?G �H (#;F# G(£A 8= #>?��F+R("V� >L�H�>? � DG.S�H� *+;K¤#¥ szvf¦OB
yw;x;§Zsf;w8=;�G= �B =�,2.S �=G� =Z¨6�B.5 #H0P.S� X �O>?#��t #"3�==�� **Keywords** 6 -- ����& �B�<.� �����I$ #�DH0R�/9@� �= GL>? ���&�R >L�H�>? �R = >O =� "V #>©.� ^' �>O&(? # 6#H0� �O`�Z@RU#@RT(RT(ª@R5(#R #@R$:@R$«RSZDkY` ªR$(@R2¬�RSZ«@RUR5Dk$�)D)  #�K &( **1. INTRODUCTION** >? &^@ Z.S� &#Y= (G# � 6>L�H�>? � G@I 4X�H�>? �E# -6DGL>? &L
<.� E0 #&L# -)n #� �� �& �R.S�H�?��H5 D.S)��� =ZD� # (>O���lA>L�H�>? �3= #�, �2 #MN= 9:U #"@� �F@ #��BG#=i � / �T�� MN= =G &6 #]9@�  6= (�"V�= &�RTp$ #qr�9@ =�R G##��R �DE �E� ;./0?13 #&#%46#� #7! 9:��H<0J.S�;X�=G� = (i#� 9##:# -YG/>? &/= (=G &S ( , # ? 9@�  L##H0���S=G���Q��SY �&E�  L>? = &tsVuv<w;xw;yvfszu{)���5"V #>r�^: GR�9:@5�= �R szu�v<w;xw;yvfszu@{­u®S¥w¯{w]"Q (>°>H >? � G= (G# � .5�,|#� "z #>OD (6=#I >? D9@��I2 �!>O#0KZ#� #�5"V #5��= &K= >O@I2T�H�BZR F=�i"V #T $ZDH0?yGsz¥w;uv #§Zsmw;yGR#= >OS @9: #9(�i>? U�# = &~szuv<w;xw;yGvfsVu@{#vfv<w;xGuyJ= (G# � >H >? � (�>? �?�BZ#>6R+ = #�Z@H0X��
O&#  #=K );, G@R (� "A�8��=K  #�>?�S�D!� � OK -��� &( 6>? ���&L^@ Z.S� &(
"V #> DG
;@yw¯?"V #>W>L�� 3>? � �
 ��L #"$F@G#= &t�>O# =K�"z >O (%"V #># �R �BZ>?�I= # �0R+>? D9@ �3 #= (>?�= �^�
# G��Y >O&(�R# 9@�  K,5 � �/��/  D9:) LYL=G��&( �& 9:�0Z�B0 ==��I '�L �#=(RA>? �� 6� (>? � (�>.S �L >?�H �==��$ L��=� =S# �� =Z #�I23  = �H*+=�Y "� #� (R>? 9@ �
�Z9:L� #>?tyvfx;�vf@xw;RT�=G�J� �=��$# �� #�U=(R# �SD� #>?/�BG# =��>O � H0L����  0E #1!G#U"V (>13 &(346#� # �BN0��I±� ZRSDX�Z�Bt 6�B=G#! ( D��) "Y� 7! 9:��H<0 "z >?
=#% = .S�H�%F �B &O=;  # #&#0P` #R¬�R;k �#�H06���� # 0OY�]&G# }} ,N(#(@( ¢f�@MB=$ K
�>O#>? #U #"�=G# N0I £8 (�H0R:>? � ^@ Z.S� &#S=Z#E/9(� #&: �B��@�>O## =�R:�@0 &: &3>?Z��U #"�9(�� (K #"��U= #=��2 #  , �D��! #"2>? ^@ Z.S� &#(I²5 (��� &)��Y"f=�R ²5 >OK�9:�S�&(  �BS=Z#�
"V #>? &8"z ^� Z.S &( © The copyright of this paper belongs to the paper's authors. Permission to copy without = #@G �>? #5�#K (��>? �SN0�(R## = #�Z@H0Y fee all or part of this material is granted provided that the copies are not made ordistributed for direct commercial advantage. �  (^"z K#  (�����Y #"/;F� �B &)>? &t#�&# #�H�>?�8 Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), = #=��/"z #>H >? �I 



> Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 

> (O.R. Zaïane, S.J. Simoff, eds.) 

�Y�B! #"2 Y�#�;3 � #&: [ �!"z #� Z.S�I3= (' ;, 

98 

�=;��!�9##!#=G^@&# # �t�KZ? "2>LH >? �Q G 9@�  JG=;^@�R�.S =;���? # (�= (>?6��D "V #O� >? ���&�I@= ( �=;��? (�.� ^P�� (&#��R� =� # �=(IU � (5>? ���&Y*+ #�R.53��>?S�D5>?G G �& #�t (@MB=;�9(�6 ��t =; 9:�>6IC= #¡¬ # >? D9@ �YZ9## #�#Ri�� #% t����B #0 '�H� �= �L O  # N0�?�B �E � &%= (��B= F@"V #>W #H06�L>?Z#��/ #"A9##�� D &? (/�H�I @= (³= (G���S= (�=� �&E (��9(D (�I �%N0�% #"K^@ Z.S� &(%.�J �B �~>? �&]"V (> **2. BACKGROUND** >? D9@��/=Z#6Y=Q��� �"V (�� Z.S�l �X�= #� D9� �6]�;"��>?>O0 #"K=G���Q��)#   #���DKE�9##8 6 #�8.� ^+It´µ� #&(;��>?>O0% " .5 #^) 6>L�� >? � GL>? �&E# �Z�S ]` («DkmI ÉKÊ a'Ë ÊÌ eVdZe ÊÍ jc!ÎdÏbTÐ(dbiÏDg+ÑY � �T =� ��U�>L �Z�= &J "
�X>? 9@ 6  J�=�RS� #�O�&(>?@� S¶@v| #vfsm/·'#§Zs|w3¸U#uv<w;u�v¶u(¥ ¦#yszy¹z·�¸i¶�º:`HDZk� MN= =(R# .S  �=;� �� �0I DY�73?� #3 #"2=G���Q��/ ?�&(>?!9@�9:;� <0% #"/46#�� >©�#� O#9:� #�# �I 8 >?06�D9( D9: dg@ÏDg>?  dZe ÍiÓÔÕRA��HN0Ri9Ñ!@�=� #=O�9:$=(I�RU ;F>?��(Ri=0@,=29:@�+�Di =Z2>?  (�R �� 9(� (� #�;8#�&( �H�>?�8�=G�J�
"z K"z#= =;� #R ��&>O0J =ZO� ��t¢f #��� ���G£;R2=# � &  &#�E= (&#�H (P #"�>? 9@ �R= #&( [ �&6F@K# >L���=L� Q&#�@;E>O0J =Z)�� ����E  #>L]�Q�B�L  p»= (>?>?=��=(I!4X #�B
 "U �Y=G���=#8� &(t�� �>O0) �=Y�B9@ (��=(I  >? �E @;�B &6���K -- J ]>? D9@��RA #K� # #�  "NI Ô!Õ dLÖjddgÏ ÍTÌ ÑY�=;�Y�Åsm(¥w;u;w$sVy(¥z¥�#®5w¯ ¦y;:¯!y;Gw;u+w;y .S �X� (>?
� ( ��HN0I �L "��>O#  ����Y�
�Z9: t= (&(� [ '>?�, �&t"z 8�B= '>? D9 �3��!= (&# [ &t��HY # �I czb dg@Ï#e ÍiÓ×±ÊÕ eVg Ñ!T ��&S=��B� #">? D9 ��=G�8#�� 
D
>O#0L>?� �$ 8= (&# [ �=�
=�5� �&K (#Ø �/.S�H�ty;:¯tw;u¯szu@{#I 9@�  ` (@R/¬#kmR�# ` @R�(ª@RSkS O #�~` kmI\¡�H� X�� "L= (>?>?=�3  (���=G�~#�t�'��=G ,m #,mF@)G#�D # gcVjdZe ÊÍTÌZÚ eVË ÌtÛ gdGÜKgg Í×±ÊÕ eQg gdjJÝ)jdjÑ � !QD (� ��/�=G�)#�·'#§Zs|w;y®UsVvVÞ)y(¯Ow;u¯#szu{#y$x( q!G#&( #½`H#k# F@E#H0[�L�=G��L\]  !X` Dk|R$�HE � #�� �Y E�#�=3� = #6 #"A�B�=�3�X>? 9@ �I ¯#�;w¯ ¦Lß�vf�¯#sm8àµw#xGuy #xw3vVÞ�#uáâ sf¥z¥ sm#u)szutvVÞw;szx xGyGv5¦w#xä /.� #^L }B¾ 4¿´!�>O LÀ�ZD=;�)²5@;5= D9:;��&6Á�w;x;¦ ¦]Ã Z{w¸U#u�v<w;uv¹Á$Ä�Ã¸+º:`HkK# Á�w�Åsm¯:w~` ªk8� MN=� \]L Z.åF�# ]Z=;�J >� G mRA# � Z.å ( #� �Z9:!>O S� &(�� =Z#� 9##�=�$�?= (&(��H� #R F��&K#   #<0��3��/ E>? �3�>6I = (%� 9##K #"E9�  ±` (DkmRL � ±` ¬#kL# >E, &(�I >? H0R
�PÃGuZx w¯sm¨q &(�HGÆ �G �%� MN= DL²�&( )4X�� (]7! 9:��HN0` Zk5�#�8>O L� &(�� =Z#K **3.1 Compositional Structure** 9##�=�A L F &3# ##H0� �$ " &# G>? �S.S�H���= �3�B=
 #"A>? D9@ �/=ZX �= ����&EL=��>O  %= #� �BG# &RA ;F� �&%# =;Z ( " &(�HG# � GD=;�0L`�Çk@��=;�K#��=��.S $#=G�K�=U 9@� � �GD �I! �L·%¥ vfs w¯#sfD·%szuw;xt` ¬(ÇR+¬�#R#DkA  DMB=Y �H� 8�Z�=! "i� #�/ Z=;�)�� / 9@�  8�Z= � =�� #2� MN= ªR:¬#kDU >? #8�G#�T73 9:;� <0
�D9( #"8"QG#>?�R!#�)&( 9:¡�~T &I3(I»\J�'#HZ 9: #� = (�B�= >O@0t >O#&#K� �BG# &R ;F� �&?# >?�, =G���Q��5` (@R(¬R«R:#@R:@k@ =T9�  # # �=;, �&t=G���Q��3 &(�HG#2>? �I   DMB=�R�; =�R2# 9: #�P6 >? D0J=Q��� =ZD� # "S>? D9 � �Z9:Y6= (�� G#�K 9##=�S�X>?�� &L^@� D.S� &(Y"V #> #�5K= (��= () #"�==�� 9:!�=�IU���;ZR:�/ >?S�BG#>?� ���#$` #ÇkT# &( #&#G�� =O` @;k DG##��I #"�!9�  G=;^?=Zt!�  L FO  K KG#=G^  ? (G# 6�8= �� ( &) EG�= �DE¯:w;yxGs w;y **3. WORK IN PROGRESS** �t�=�(I 0�� &'= (>?>?=�Q��0Z9## #�% � ' ';F 8 (@MB= 9:8 "$ #�szuw szu+w;xK �S ? Y;xB w;®$#x­ G#�� #�'`H(;k|R/.56=Z¨ (G#  XF@S= (? "
� = (� �B & #"= #=��R! �H6 >?��>?@GD (¡>?=G� �>?�R �� (^(O= (@9:�D (I 0?#H0�[��&K ;F# �= #�R .�Y #X E= (�B�=S= >O =Y� GD=; ��! "A>? D9 �I 9(@i#�&# #�H�>?�i# 5�B,<  />?��/szuv<w;xw;yGvfsVu@{­u#®S¥H w¯Z{w8= (G�� 6>? D9@ �IA\]Y= #=@GDY X>? &L� &( �9(+^� Z.S &(
"Q (>r�B#>?�/� �&E#HZ 0tZ9( Q� ;=,  #� Z.S &'# #,|9@�  t=;  # #&#0=Z#JE� "z #8 ?��, #R� @� =Z (' 0 &L=Z#�# ��H �3"z 
� ;�0 & � (��! "A=ZD��&?= >OD =
�B=(I � ]# 9@�  �R5.S ��6;F��=G (�DO (�O= (= �R >?=;�# �>?�!# &# #�H�>?�!.S��A��?= H0&# =L# � S "U Y H0 &E>? �L��=� = #%# Ýtg@dgÐ(de ÍiÓ ÎÐ#g bid Ñ!73� &?�� S=G�#�&(�S 6=G  #>? #�=(R�>? =5# �T9 �#@�DG#>?�iN.5 � =Z #J>?=G� �>?�Y# �@��3.S $#== (>?>? E�. �==���9(X9@�  "VG>?�L�HL��L� (�� �t =L�= 9##�=�S t��8Z�I =� .S�H�L=G#   # � <0'` #R¬#kmI q
G¨= #G# �RK ## #�'¨>? D9@ ]= (>?]"Q (>È�9(G# Ýtg@dgÐ(de ÍiÓÉ g�ajdZeVÐæ)ÏDdZeVç|jÐ#d ÑY73� �&¨� >? QD=G� #H, � #�=�IT �BH0R Y �3� #>?Y>?G DGR��=;�6#�3#>?�S " (&#0K�H2 �2#�� 
� #������ ;=2= >O =/�H"z#=�2�=G� L=;.C��=� ��&X= #�R �H=; #D¢f�G£!=#R.S L>? D9@� #�/=Z>?G�#�R@ H�R[  (>? &R=!.S 6�=E` #R .�#� >? # A� �T�� �� G@R(=�H = �>?�RG, kmI �&(�R� #�D <0K>?Z#��R 9: �>?@�i=(I2 �/=Z#L #�G�� t;F#"z >6I$= ( H0R�Lyv|#xG¦)>OZ0O
D9## H, Ýtg@dgÐ(de ÍiÓ ÚÊ Ü?eVd jPÎÐ(g gÑ 03� &/=��>O =U, � )� (>?3F@#"z >µ  �I$ H0R�3Y L# "z#=�$ ==��&Y.S t
�=(R: 5 �$� #�����! 9@� 

99 

- Movie 

- **Scene 1 Scene 2 Scene 3 Scene 4** 

- Shot 1.1 Shot 1.2 Shot 1.3 Shot 2.1 Shot 2.2 Shot 2.3 Video 1.2.1 Video 1.2.2 Video 1.2.3 Video 1.2.4 Video 1.3.1 Video 1.3.2 Video 1.3.3 Audio 1.2.1 Audio 1.2.2 Audio 1.2.3 Audio 1.2.4 Audio 1.3.1 Audio 1.3.2 Audio 1.3.3 biÏDgPéÑ ×±ÊÕ eQg%ê6eVg@ÏDjÏÐ Ú+ë 

- ]�=� @ ]]�Z�= #"?yBÞ�#vfyI #)F�#>? �(RS (� -��H (RF@#>?;G GK# #�5>? 9@ �$�=G�t�5� �H=;, �=�O= (� )%ìZZ szu@{szu#= (P "3³#ÇX"VG>?�8"z (H,  #ZR#G &R:� #�D <0R#0:ZA " = #R(#>? (�A #">? #0 � Z.� 0t?ìZZ szu@{)#@v/ #"2(³K"VG>?�8` kmI ��ZR�B Y� R= #0L " �= (L<0� "+>? D9 8¢f�fI (I ��ZR=; � Ø �
>? D9@ �R+ (&G# �@0R #>O#�=(R./DZRi;� 

- = # =�R4X 9##�B #0=D£T= #�RZ.� �2.5 (E;=/S� 

- @ >?�D�0Ri�ODO=; ��Y 6�&#>?8�O# 6G#=G^ Z9( Q�(I 0X� &?��K�BGD �B�=�3.�8�6 )>? �
"z #!� = (� �B &? "A"z #���=Y�B��8` kmI "z #� Z.S &?<0��3 #"2^@ Z.S� &#(l Î+gËijÏDjdZe ÊÍÊ ezÐ�í2î ezÐ(gí$ÎezcQg Ð(g%j hï gÑ 0
�B, ÏDgõbg ËAe ÌÊ hig Ñ!\¡�D5D/�S>? (�B2"V@�U� � � &]"QZ�=0¨��=>6R�QD 9:% # ��t# # �J>? 9@ �RA L Pt>? 9@ DöC (�� Z.S &%�BG# ;>? 

- �DG#>?; #"TG �H (#+� (� #H0�� �R��HS��/� #�� �  (� #&#0E E>?� G# G
>? ���&�R:#E � = (����B�$ #" HX � # G=;^¨� >L���=#R39: # =(I 0�B, �Z�=S #"5w;§#w;uvfyR@.S�S.�= #�� �#?9(U 8 

- &� >? 8=G���RT�HL �89:]� (�� �? 6�&#>? #0�H>¿� >? D9@ �;G=G�@0R�=G��3"VG>?(R+�� ZR 

- �L>L� =E�B#> �H*+ w#vfyI6 �O?=�, �=' #6#=ZI3  ='�t   t #� H0^@ Z.S H0PZ9## #�X#�L = (>?>?=�Q� =�K #, #�&(  >?�E"z t>? ���&"V #?"V@�O� � �?.�6� �ZD=;�6� # N0��8` :³@R#«@R+#@R@kmI  ��=�>C L== #>?>? �"z (�� Z.S & *+;, =�l 

- ÏDj ÍTÌ cVjde ÍiÓ ezÐ#ge gñd(Ñ! �;U=�H0
F �B9: ( =  6F@YG#�� #�K 6G#��QD?�?9: #�=)�B#> @ eVÐ Ô!Õ @� =Z ( #"/#� =O9:�Y�#�Y� 

- �8F@T"z >OZI8 �EDL= #>?>?=�#�H0'Z9(�� "z #� Z.S &ON.5 ? -�= (>? ;F��H �I `H(;k|I ÉKÊ aË h¡ïXjdbiÏDg+Ñ T.� ^
 #"46#� @R:�i # 9: #, 

- hig@Ï dj hTe ÍiÓ g@ñd(Ñ 0J@u¯:w;x;yv|#u¯#szu@{L�Þx#yw;y8 6F@� ` (³DkE# # �RK� � =ZD (± "O��= kmR
�H �t� (�� � =ZD&(  [PPF@X�BZ>ó= #, 9:� J #t� (�'@0  #�>?�l�fI #I� 

- �� ( &' J'�Z�=X "
��=�E0F@G= & #�� =�D F@/ =Z6 =Z�? "!� @>/ #"T^:0O.�  �I 9:E.�#�) �@O ) #ZI ¨ #�)=Z�(R/� � D.5�BT�9(: #"�9:@�D$= #>?��F3 (@MB=�i= (, 

- gÐ ÊÓÍ eVôe ÍÓ Î+ËUgÐ:eQjcÎ �#�Y� D.S
�T{#@u � �B��&3 "T#�B2 (��= #>?� (@i #"# yBÞ�#vfyRxGs|w;yR+¥�;:sVu@{L -XÂ Â
Â ¥�#yvfyS=ZE/� � 9@�  �I .S�H�6� (>? &Y #"T=G# N0IU´�� �;Y
�=G� Ö
Ï Ê÷ ezcze dZeVÐJïXj�dZbiÏDgÑ
´��BGD �?` #³DkmRD�2� ,   #<0���T�2=#L 9(�� (� �T�UD
yGs sf¥�#x/ � =ZD� #E #"+#� =S (@MB=;�$ �U (L  (#��� �B =(l 

- (� �� #^:E 8>? = #� (#I/¢m �!##� (& #"5¤w;xG¦ �fI #I6�H�;K 0'.�?��K # #ZI J (� Z{w#u�v<w;uv;`�kmR+=Z� ¤w;xG¦ ¦LÞ@ L szu@{`H¬#kV£;I =Z#�#R L �YO #�,|�"V=Y� ( ��HN0'#�� , =� .S�H�' >6R#�8# 6 9@� =;, 

- \J! #? w;xm{w3^@ Z.S� &(&:# � 0L9�  8�&(>?GD� #R ()>?� �/ �&(G@
#t#�� (�� � Y�&(>?G #E# F@@ �BG# &! 
=;�G=, =�� #R���= (>? .S�H�X#6�� =� � (, 

- [SZ=;�L>? 9@ �= #� �B &Y "!"z #�U�9:� GD=;�0L#�2&( 9:L� #����HN0I 

- T &IT(I´�Z#=G��9: #"A K G=G�06 9(8�! #"A"QG#>?�R % # 3 ) -- ��
 (
>? &E@��H>?�R.� .5t= (��=E�G>?�RA��=;��K )�@�=? #"=Z#>?;G, S,< -��� &8�S#� ="V #> (O "�w<szy;Z¯w �H"z#=�R+^:;0X G#��R��=�#i� ( �K¢f�=G�#�!#&#�ZR= �R szu�szu@{
 Y== (�U"V #$��=/>? �,<#�/9(�A= (, &#t�� #�R #>L)#�B�/=Z£�# �BG# D &#G� �=��G>?, � �B��&6 #"�= (>?� #�
 �&X� � .S�H�J� (, ;�
�=G�%#�YZ9:;G#&(À1 R+�>? =#R=;� (>? =8=#I �"z=6� ( ��H��I �)� (&];> &# : �) 

100 

- F@ � �!.5 #^6 )?=Z#�K.S�K (� Y>? #8 " &6 "�N0�E´8RTDG#=G�  t �BK (@MB=# � ��X= #>?� (@�E sVyGyszu{P# �X#��>?�,  (#����HN0) "A & #"T<0�� RG#=G�  L 3�= # ( #"3�"z=;?>?� #G�B0�=;� (0P �E � (&# =Z#63�B&�� ¢f9@�EL � �B =Y  = �Z£;I 

- 9##�� -X�3 E�N.5 #^O� >? �Q � 9:0I \]#�� L #? 8F@ #�/�� =� ()�>?�� &Y"z  

- ê6eVg@ÏDjÏÐ Úë Ñ3 �P �'¨� GD=;�0 #"E9:�6��=;�±#� ¤uvfszv|#vfsV§#w6­u®S¥w¯{w;R/.S� =;�6=��B (>OD�H0=Z#�� "VG>?�RT� #�RA�=�RA#=�8�D #&X �H*+, @#�HG 9:!#�� =�D� #X�(IU´OF�#>?��S.� # Y¶ A�9:�2 "&#G��HN0IA²5 (�@�H0R(����&3�, ÂYÂ ¥�#yvU¥�#yvfszu@{Xÿ szu@v<w;ySszy(¥V¥�#®5w¯ ¦vf®$?:vfy3B ��3 #"59:�YD8O Z.58&#G��HN0' &)= #�, #@xGuszu{#R��EO{#u�yBÞ�#vszy�(¥z¥�#®5w¯ ¦xG¦szu@{Xszuvf®5 G# � )D&(/� � �$.S �O= (�!&#G# O&#G@�, GuywvfsV§#wyGw;uw;yKB
vVÞwKy; wK:vfI �HN0
� �&O L^@ Z.S� SU 9(�B&(L&(#&: IAD
�K� D.58�9:T �T�� S (� czb dg@Ï#e P=��B)>? D9@�6ÍiÓ×±ÊÕ eVg ÏDg �O����&P (tjdg ÓÊ ÏeVô(jdZeG=G�ÊÍ =Z
Ñ
\]2�"z ,Q ��t�Y>? &E3E� &( 9:fIS � � �!� >? >O (IY73� &O�K �"V #>O # #�G# � "Q (> >?�� &  
�S ��S"f= ?= (@9:@ ##�� � !>? �&�R �t �� =� (~��R! (�'=#"z > 9(= # EZ�H�?� #>?6��#�=>?�L J#== (?"V # #"5"VZ�Y�D �=;��L>? D9@ (I �Ri=��B &  # � �!#�� =�QD .S�H�6 (@MB=3� <0I #�&(  >?�`HZk!=Z¨���  & (�>? D9 �? ��>? =���I 

- ÍiÓ ÏDg ÌLø eVd Í~×±Ê�Õ eVg ÑS\]$�#K ! @9:�B�H, &:D$ ��=G�8#�AùKY(¥z¥ #§Zs|w;y wm{#szuKÞ�G:sf¥ ¦
#u¯Yw;u¯ **4. PROTOTYPE CINEMA MINER** y;:¯�¥ ¦ú6 #�9@ =S9:�@I ?>? �&3"z ��=G�?^@ Z.S� &#.5 T &�IUX� Z.S��O�B�=�? "! #�   #N0�(I´!�K�BG  ?=;�G= [EÞ�;:¦ wm{#szuu�szu@{#yK #Ky;:¯w;u¯#szu@{#yI = (~(RU�H?= (�� �B�E #"!� &#HZ 0Z9## #�X# J 

- =;��&�=G�J �RT.5)=#P�%¢z"V #K�?#=G^J " 9@�  '##H0� �E=; ��8 '��DG6 �H"V0]= (>?� , 

- L.� # £EPÞ�G:szuw;yGyX ;F�=G�¨�E�X>?�HF@� @�!# -D>W�D
DK�� 6�8>? &?� =��I! � ¢f #3�=G&(L>?�HF@�� "G£&(�
 #
=;0� �&O.S�H � � GD=;�0Y= (�B�= #ZRDF@T#H0�[A >? D9 2>? iU� �X�=#R/^:0P.5 # �? )� G��O#�� =�QD .S�H� = #>?� (@��D3.S �2= 9:L #�Y= (=G @ # �=�/>O=G� &� #���2�Z9:� ,|=G�DG#= [ � �2  DMB=ZI2ûU#=G�E #" ����H�A=Z#E5= (��� !>? � #�? =Z �&J�� ����R5# �)F �B=6 #"!��=�# %E   #N0�
.5K #X ?� �BG#&(�
#�!L���! #"A = >O =8*+=�S #3Z9:G&(KÀ1 = (� #�R �� �ZD=;�6#&( @I >L�� =D£;I3 # =�O� �O �tZ��9##�? P=�� "Q0��& >? D9@��R#==  &] P=G# ¡=�H�IûSI &IR3]>? D9@� =Z >? Þ�G:¦] E� #Zü3§Zsf(¥w;uv8 Xuum§Zsm(¥w;uvfI g@ñdbijc$æ jc ëÌ ÌEÊ ç!ætbThie Ñ3´!��� Z.S8�8T &I@RZ ��>? =S �S= (�=��5D3�� =� .S�H�t
�;��5 #"�, � �3"V 9: ( =F@G#= "Q (>¿�# )�B#> .S�H� 

- G#>?; ¢m#� �=�� "z 5"z 5Þ�;:szu+w;yy� F£;R (� #�� (��QDX >?6�BG#>? �I O �E�"z  JF@? *, =ZE��=Q��� =ZD� #?=; ��5` #@R@#ÇR³@R@«@RZª@RZDk �,|���";FU�0� �5>? �(R#.S�/�S � 
.S � #=G� 9(!� �5G�^I23 # =
#�� �SK>? 9@ =Z#)� (�& G#�D  t?��8 "$;FZI! K��K8=Z#  %>? #O�P ()=#��l)(I &IR5%>? 9@ O=Z#XÞ�;(¦#R K��  O#H0[8�Eyv|#xG¦X ?� #>?YF@ZI�\]8� # (¯#¥ vmN#xGs|w;u�v<w¯I/ �;
3 #&(�)>? D9@��5 9(�H"V0  (� #�6 ]�X��= 9:%��G#��)# .5 # �?�) �L#==�G#=;0 "�� �Q2 �=;� #�Y��=;�#�¶ � =ZD�9(Y #"A� #.5 #�0X ��B��&E9:@�I ¥�#yv8szy(¥V¥�#®5w¯ ¦vf®$ szu@v<w;ytBOy(¯JyGw;uw;yGR5 #OD ga'j g@Ï@Ñ � �K>? �E= (��=�#�$ ?�"z >O ( 

- X �&#�K�9:/ÃGu(vfsm#u #§Zsmw;yGý3#u:v
BL§Zsm(¥w;u;w?szy � 6"z >ó "LJ"VZ9(= #ZR = &] (� ;, (¥V¥�#®5w¯ ¦Yvf®$K:vfy #xw8¹��w;xÞ�;ySxw;v|#¥ sm#v|#xG¦#xA@usf = @0P 69@�  P # P##H0���O= #>?� (��R vfsz§#wNºB3§Zsm(¥w;uGw;R# �9##�� �HN0? "i��=;�O=�>? ! # >? /"V #­u#®S¥w¯Z{w3 (� " >6I � �9@� 
�B 0t���B ��I = (RS9:?�Z=6>? ���&�R�#�� =� # ��# =��B;��&?�= (��R� �= � ZI 

- ÌZÌÊ Ð:eVj�dZe ÊÍ bTcVg Ì?× ÍiÓ Ñ!\]2�#
 9:� #�
=; ��  K>?��"V #�� =� (6��
`H(R@R+D³ZkS9:;0?�9: " g@Ï?îYjczezhij�dZe ÊÍ¡Ê g�h¨ÝtjdjÑ\]?�] =Z0J (� �K� GD=;�0I3 #3 �BG#�=(R+ #K=Z# �D
=G �5��9:0�U &(� (5 !9##�� �HN0E #"T>? � ^@ Z.SH, ^@ �K #"! (@MB=�L 6"VG#>??��G 9:) #"!�=� &#)"Q (> >? 9@ �R2 ]�)���H�H #"!�=�� #P�B �� 3 #"V#�� =�D .S�H�X # S^@ �5 #"T #MN=�S t  L>LH >? �Q8� ��HN0` (DkmI "VG>?)� �@�K�)F@�=�(IP´�K�)� &( �9:fR2 #?=Z �= D9:#�� =�QD (��#>? (�&6� &# **5. CONCLUSIONS** �9:A= (= �Y "z��Y�=G�� �H=; #�Ri#>? (� \]$�Z9:U �@ S� T"z 2>?�� &S �"z >O ( L #">? #0��ZR:N0�/ ">? D9@ (Rvfxw;u¯6¢m�5>? @0 ( # #�!>? D9 �S�D3�#�!= (>?Y"VZ#� �@0t= #>L ���&?F �B, #�&# #�H�>)£?� R!>? (�0¨ R�B �  "� �=, &'=;  # #&#0 ¨ >O&((R�# ]# F@O##H0���) �, (R � K (I2! # =S�DS# �H0��&8�BG# #�� = ;�BG# &�I!´�!�BGD % 8� = (R9:6 � #��
=; �� X>L�H�>? �? #
 (H0%�= D9, #���>? (��O #"8�"V=O >?X.S �'�B0�=;� (0R�>? �&]= (>E, 

- �$^� Z.S &(#R@�5#�� K�� �$ ?�S (@MB=5= (&(��H� # >? (L�;�5;F� �B &Y )
= #�=;� #t "+"z� >? �
�BZ#>?�  #�>6R@0X� #�#�H0��= &E 8  (#����HN0#�B, �5
=G��&(/�U&( �U9:E0 # �H?=�H$� (, 

- � &(�  O� (@MB=ZIE #
���BG#�=(R "5 (�E^@ Z.S�3�D �>?�
 "� >O#&#(R;F
# t �BG# &IKûU9(� )� (@MB=�TN0�U´# ==�"VZ��03 (&(;�/¢z.S�H � >? #U >?� #G@ ��� �i #�i "= #>?>? (Y= #= �i�� /.S� Z.P "þ�"VG>?�G£;R(# �HA ��= 9( �Y 5>? D9@� ]>? (�BH0F@8#� >? ���&X��=;�J#�8=��B �&�RA9(Y�D, �DS ���&E>? =�0O�#t (@MB=;ZR� 9: ��8# = (>?>? #H0 ==� &6�#�H�
.� # E�?=  EY "AN0�Y´± (@MB=!� 9:  EY #"A<0�� �= E= (>?>? #%�;�Y �� -- ^@� D.S� &(LD9## #�� D3 ==� &8"VZ��0 (&#�ZR@ !� ( ��HN0? " 6= >OI 101 

- **_ANALYSIS Textual Analysis of Audio_** Concept Hierarchies 

- **AUDIO MINER** Stories Special Key word 

- Type Separator Special key Phrases 

- Audio Sample Music **_Hierarchy Constructor_** 

- Voice 

- Audio Audio Audio Audio Special Sounds Video 

- Video Video Video Seperation **_<u>Movie Miner</u>_ VIDEO MINER** Trend Mining 

- Video Video Video Association Rules Frame Frame Frame Scene Cuts Eposide Mining 

- Artifacts 

- **MOVIE** Outlier Detection Objects Clustering 

- TEXTUAL DETAIL **_User Validation_** 

- Director Budget Actors Validate Mined Knowledge 

- Awards Ratings Type **_Validated Mined Knowledge_** by user surveys biÏDg Ñ8Ö
Ï ËUg ga'j g@Ï 

- **6. REFERENCES** `HZÇDk1IqYZ9:� #ZR��3I´KI>?�H�R� KI =9:ZI `�;kYÀ8I´&#G./mR�3I >? ����^@�mR# ´8I ./>?�mI4X & ²5��>O =Y��>?�H 9: "V #>L�H�>? �IÃ () ¸U @v<w;x ´!�� =�QD (%À!��� <.��S #" >?�/ Æ&( x;Þ@smyK#u¯E¶5:¥ sm#vfsf#uyR*#H0%Z(@(I qYDG#��I �� xZGww¯#szu@{#yB
vVÞw
¶K¸i· ß@Ã��$·��$ù `H(;kK´! (>? !@0 G#&( #6�B0�B>?�/ =(I´!9## #��8 

- ¸U#uZw;xw;u;w#u6·#u{w w;uv/B!ùK#v|#R>O0Z(#I + ,-,.(/10-032-465�768�9;:�<6:=>8@? 

- ZkYÀ8I´&#G./mR��I46#� RÀKI @ ^##ZR
�I�i ( 9: #R ´KI ^:�fI��B!q3��= 9(0X "2´!�� =�QD (À��I `HDZkY\IûA*+��&I´! (>OD�=3>? 9@ 
= ##H0�� �I 7I 0@0@ R1I@���H �R I@>0@�R À8I7!�@���#>K0R �@�l D././.YI �"V #>OD�^I ��H, >O#�� >6I A �"V #>O ; � MN=� #4X ²�´KR 

-  �RÃGuX¶S¯#§#uGw;yYszu Yu#®S¥w¯Z{wYù
szy;#§#w;x;¦t#u¯ Z(¬�I 

- ùKv|E·%sVuszu{#I´!´3´ ��R((«@I 

- DkYÀ8I =;^.S�H�R5I²!I�RqLI1! (��R EI4X �;ZR1I´8I4X���ZR `HZDk4IT� =;^@�ZR��KI.S�;0R \I! #=G^I*B3�0O0 # À8I�i�&(�fIT 9:3�#�;�/ (t.5 # Zl$@�=�#+ ��Y " �>O&(8 9@�  E= (ZlU 8@� =
�B0�B>6IÃ )( �$MB (i #"T;F� = #&#G��0I @xGu#¥AB Tw #sm{#xG�Þ@¦R ¸U @v<w;xGR+ªl # :RtZ#:³I �¢f¬:£;Ri((Ç@I `H¬kK´KI13���R �IÆ (&(#RqLI²5�>L� #R I²!I>?�H�I 

- ¬k �I+I #=[^0t# ÆUI�´KI�À! Z.5(I´= (>?� � (t #"29@� 30)0O�@>?>? &l24X� =Zi �"V #>OD� #6 9##� ��  ( D0 = #X=G���I @xGu#¥TB # G#�#I �� xZGww¯szu@{#yB
vVÞwtÿÞszx¯¶K¸i· ¥wvfxB#usf8Ã Z{#sVu@{#R��#&#�YD# Z#ª@R�>L3Z(#«I ÃGuv<w;xGu#vfsmu(¥5¸UuZZw;xw;uGwL#uX·%¥ vfs w¯#sm#R��&(� # («I´²/4 ��R((³@I 

- ³Zk8ÆUI >OR��I� >O#RÀKI´KI ��R# ²!I@ (�(I ¸2¥�#yys #vfsf#u]u¯ wm{#xw;yysm#uÿxwGw;yI²5�# >O#X# `HD³ZkC�I��3# ED I�I�q �= D9:0) "2>LH ��,|�9: #�� =� #%���/"V (>_&# G��I �� xZGww¯szu@{#y 

- �mRZ#ª#¬�I B
vVÞwGF&-&HEÃGu�vm¥ä�¸UuZZäT#u~Åw;xG¦Ii#xm{w
ùK#v|EÄ!#yw;y 

- «DkK²!I �&(�I´½ #�# (X��� S9:= >O#=G� "V # ¹Å Tù!Ä$ &-H;ºDR�&(�S¬Ç ¬:#R�>L;
Z#:³@I �Dt= (&#�H (IùK#v|L·%szu�szu@{O#u¯ 8u#®S¥w¯Z{w `HZ«Dk 6�
D�HG# (&#�RqI6�
.5  R# ÆUI�IqYZ9 �I
J"K#lA\¡� :ö 

- ùYsVy#§#w;xG¦RTZ#(ªI .S�öt.S�DöX.S�;ö(l$´Z >?
�B0�B>r"z  

- ZkK4I²5 �BfR+I9:��R KI@\PDZI "z >? � =;��&?# G=;^@ &E� (��(ILM�(!$ &N(Ri(#ªI &# Gi� �GD0I$¸U  @usfGvfsm#uyYB
vVÞwY¶K¸i·%R ´!9## #�8D 

- #¬�¢m:£;l ³( ³ªR´!� U(#¬I + ,-,.(/10-0�O�?*P35 >-:=QOR?;2S=1T23O
0�O;:3T34
:0-U6:�2 03V
:-5@?0RW O-X;:=Q+6,A?U 

- ªDk8 �Y=9@�  L  DMB=ZI `HDZkK�3I ( (#=G� >?�I´  ##� �B =K##H0��� #"i�
 ==G� ��l Z././.YI #�>O I >6I = #> =� D=9@� F+I �>?mI #�&(  >?�/.S �t ""z !F@S=ZD&(  [Z (I ÃGu /xBZ;ww¯#szu{#yB
vVÞw
ÃGu�vm¥ä�¸UuZZw;xw;uGwL#u6·:GÞszu+w 

- Dk8´KI²5[0[.S�^@�fI+4X ���&E^@ Z.S� &#Y 6 #��B0X# GI Tw#x;u�szu@{#RZ#:@I 

- !�/xBZGwGw¯#sVu@{#yB
vVÞw8ßwGu¯?ÃGu�v<w;x;u#vfsm#u(¥5¸U#uZw;xw;uGw 

- B"8u#®S¥w¯Z{wYùYsVy#§#w;xG¦t#u¯LùKv|E·%sVuszu{¹#
ù!ù%$ & 'GºDR `HZªDkK�3I ( (#=G� >?�I�F@S=Z&# # [ZD� #.S �X��� S9:=  �&(�3(Ç ((³R # &( #RZ#(«I´3´3´ ��I >O#=G� �lUÆZ� &L.S�H�6>O@0?9(@/"VZ�I 

102 

- xZGww¯szu@{#yB
vVÞwGF(âvVÞ @x;�w#u¸U#uZw;xw;u;w#u :Zk+I� #�R I�
^(>LGR# �3I;8# (I�
>?�HZl 

- ·:GÞszu+w"Tw#x;u�szu@{#RZ#(ªI #>? �&E# -X= &"f#=�! 6�.S�S>? �@IÃ (( ·%¥ vfs w¯#smR��#&#�
# :³@R*:#@D0@,B46D=;�Z(#I 

- `Hk8qLI;Y >_# ´KI
�!����&I²5���B &O =G���Q��/"z # ÆiD&(8qYDG? ,$i #>_ #�BS L�
T��#I (Dk+I�H 9(�#RqLI #=� #R# qLI�´!>?�HZR �i #�#��� ( 6´²/4 YYq
q (# ´KI ^: D9@ =(I�\� �/�DS9�  ?#0@./0ö(l t�Z=G�6 #" ²5 ("z= Y� Z.S &(Yq3��= 9(06 qYG S� Z.S� &I �� xZGww¯szu@{#yB!Ã () ÃGu�v<w;x;u#vfsm#u(¥ 4X &I+#Xq3�&( �R²�#��H"z �RZ(�L(#I ¸U#uZZw;xw;uGwL#u6·%¥ vfs w¯#sm6¸U vfsVu@{tu¯?ß¦yGv<w yR �#&#�(ª#ª #:I ûUû$û/R û$ûUû ��R*#Z(#I 

- Çk EI;Y (��^@�fR I´ ^(D0R�# �I;�
#I@�D�Q G >? &l  #&#��!# =G�#���&(�I ß@Ã��$·��$ù #¬k+I@ 9##�R�qLI #= (R# qLI ^: D9@ =(I� D.� #x­yBÞ�GP#u!Sw;yw#xBGÞXÃGyyw;yK#u6ùK#v| szu�szu@{O#u¯  (��B/"zZD��S"z 3=Q���H"V0 &O# E X 
=9� 

- 8u#®S¥w¯Z{wYùYsVy#§#w;xG¦¹¹zù3·!
ù�$ & ';ºZR�#&#�3( :R �B0��B>6I %¶K¸i··%¥ vfs w¯smE&-&#I´!²/4R´²/4 ��R 4X (6\ZfR+²�# Ri(#«I 3 D9:>
Z#(@I 

- k EI;Y (��^@�fR I��3#R# � ^#0I�4X �&?^� Z.S &( :³Zk I��i (� (>�GR´KI�´^�R I��T &(�=; �fR# 6&( (&#G� �=# GIU¸U  @usm#vfsf#uy8NYvVÞ�wY¶K¸i·%R 1I@[�^�fI@�=� 9@�  L= (>? � &IÃ (( Z#(ª@I ·%¥ vfs w¯#smR��#&#�3¬ ¬:R#�2Z(¬�I 

- #DkKÆUI;YZR GD^: �R# ÀKI4X =G�#��^@�fI·(GÞ@szu+w («Dk8qLI�\� MN�^:;GE# qLI G@I·%szu�szu@{K·%¥ vfs w¯sm ùK#v|#yw;vfyR=G� !2@R;�   (^O #"2qYDG?4X &I 

- Tw#xGuszu{X#u¯Eù8#v|E·szuszu{#ýi·Jw;vVÞ�Z¯#yKu¯L¶�:¥ sm#vfsm#u�yGI F"V # 73 9:;� <0 ��R#Ç#Ç(ÇI 

- ( #�X\¡ �0X#  #�RZ#(ªI :Zk8qLI�\� MN�^:;GR*I�9##�BGZ9#R´KI3; (R# 

- kI]TI ,|KIÆ�mR IÀKI]+#�#�(R TI�T#�ZI ��>? # 4I �B�fIûAF� >?G#+9##�D� #6 #"T #��!�;= # @9(D�Q=8 (@MB=!>?  6= (,|#� >O#&# (6= #�@� (�/>? �I·%¥ vfs w¯smEß¦yGv<w yR@l ¬:ª#« ¬:(@R 

- # 9@� 9(fI^@#@xGu(¥iB6Åszy�(¥U¸U L u�sm#vfsm#u = (8((@I #u¯EÃ Z{w_Sw<xw;yw;u�v|#vfsm#u�RAZ(#ªI (ªDkKûSI\] # R�3I �>6R# �I\¡ Z #I²5 (,|#� 

- D¬#kI]TI ,|KIÆ�mR IÀKI]+#�#�(R #I²$,|�H =#��� =ZD (R�Z=G�# 9## #"2 � IÃ () ²5 (,|� >O&(
 9## &(�HGi� �G �� �& ¸U @v<w;xGR+ªl ( («@RtZ#(«@I =G  (>OD =�HN0t# = #&(� #^:fI %ÃGuv<w;xGuvfsm#u#¥ #x­yBÞ�GP#u%ßv|xZ{wLu¯ w;vfxGs|w;§(¥ÃGyyw;y
szuXÃ Z{w (Dk8ÀKI�]+# R �I4X �ZR# EI46#�fI´~"zZD�,|� 

- #u¯L·�¥ vfs w¯#smùKv| #yw;yGý$szu%#ua`@uvfsm#u%®2szvVÞtvVÞwC&#vVÞ #�&(  >W"z # = &E# =#���H"V0 &?� =;� # ÃGuv<w;xGuvfsm#u#¥5¸U#uZw;xw;uGwLuù8#v| #ywL#u¯ ;�w;xGv *+=�I¶K¸i··%¥ vfs w¯#smEß�¦#yv<w yRl�(Z Z#ªR46D=;� ß¦yv<w y?¹zù à!¶�$ &3NºZRp3 �@R´�B�RZ#(ªI Z(#I 

- #³Dk�I46#� R��I��i ( 9: #R ´8I I�p$^##>? I ¬:ÇDk IÀ8I�]�Q(R �I;�
#R*]TI ,|I�Æ�fR+I;�I²5�(R# ²!I �I q �= D9: �&E&(�G#� [ � � �� �&E>? >O# I4XH >? �>?��ZlU´½�B0�B>W� # N0�3"z  ===�I !� xZGww¯#szu@{#yKNYvVÞ�w8ywGu¯?ÃGu�v<w;x;u#vfsm#u(¥ >LH >? �Q DGL>? &I �� xZGww¯#szu{#yLNYvVÞ�wGF&-&N ¸U#uZw;xw;u;w_8u#®S¥w¯Z{w3ùYszy;#§#w;xG¦t#u¯LùK#v|E·%szu�szu@{#R ¶K¸i·'|ß@Ã��$·��$ù¿¸UuZZw;xw;uGwL#u6·#uZ{w w;u�v$ùKv| �&(�8¬(« D³@#I+´3´!´ ��RiZ#(«@I ¹|y¦yv<w ùKw ºZR�9: (��>?
(ª@R@Z�(R@\]#�� �&# (R(#ªI 

- «k EI4X�#>?�fR´KI�´!^@��R�# I;�
>O @Ip3� ¬�;k IÀ8I�]�Q(R �I;�
#R*]TI ,|I�Æ�fR# �I��! (I4X �& � �&L.S�H�6>L���=
# ��=G� ;= (I+Ã () >LH >? �Q DGI !�/xBZ;ww¯#szu{#yB
vVÞw)¸i¶3ßi¸e�)f!$ &N6g ·%¥ vfs w¯sm#R��#&#�YD (³R:MB�H0,N@ >
((ª@I ·Jww;vfszu@{)B!·%szu¯yGR��&(�3( (@R+�i  ( �R²�# R Z(#ªI 

- #Dk EI4X >?�fR´KI@´^�R �KI �
>O R@ GD I@� ( #>LGI p3�  E� �&L.S�H�6>L���=3# ��=G� = (I () ·�¥ vfs w¯#sm#R��&(�YZ #³@Rb#H0@,B@ >L
(#I 

- ªk8À8I�3I�3&? �I��3#IûA?= !# *+=;�9(Y=��B & >? "z ��� DGL>? &I !� xZGww¯#szu{#yLNYvVÞ�w ÃGuv<w;xGuvfsm#u#¥5¸U#uZw;xw;uGwLNÅw;xG¦Ii#xf{wYùK#v| yw;y ¹DÅ*iù3Ä$ &@c(ºZR�#&(�8¬(¬ D³#³@R#�#&( R+²5 ��(RZ##¬�I 

- k+I "z�H*+ZR+I�T �=; ZR \±IûA*+��&�I´! (>O # E= ##H0�� �I �� xZLB!¶K¸i· ·�¥ vfs w¯#sm#R �&(�3@ #ÇR+´²/4 ��R!. ^+R+((«@I 

- #Çk8À8I*B3���#I2¸ZcädH)S� x{#xB y$x!·:GÞ@sVu+wYiwx;u�szu@{#I 4X #&(#�8�*+>O#R+Z(#I 

- @k²!I+G= E# ÀKIÆ (D �fI´! ?#�L���� #/ �=�Y=;�#�&( ;= ( =;�G#=; [Z (% "A9@� �Z=�I !�/xBZGwGw¯#sVu@{#yB
vVÞw
Ã¸i¶3ßß �/R ûUûUû ²5 (>? �!@ = N0 ��Ri(:I 

103 

### **Variations on Multimedia Data Mining** 

Simeon J. Simoff Faculty of Information Technology University of Technology, Sydney Broadway, NSW 2009, Australia +61 2 9514 1838 

simeon@socs.uts.edu.au 

###### **ABSTRACT** 

Is multimedia data mining just a new combination of buzz-words or is it a new interdisciplinary field which not only incorporates methods and techniques from the relevant disciplines, but is also capable to produce new methodologies and influence related interdisciplinary fields. Rather than making an overview of existing methods and techniques, or presenting a particular technique, this paper aims to present some facets of multimedia data mining in the context of its potential to influence some relatively new interdisciplinary domains. 

###### **Keywords** 

multimedia, digital media, data mining, knowledge discovery, knowledge representation, case-based reasoning, computersupported collaborative work. 

###### **1. INTRODUCTION** 

Multimedia and digital media, and data mining are perhaps among the top ten most overused terms in the last decade. The field of multimedia and digital media is at the intersection of several major fields, including computing, telecommunications, desktop publishing, digital arts, the television/movie/game/broadcasting industry, audio-video electronics. The advent of Internet and lowcost digital audio/video sensors accelerated the development of distributed multimedia systems and on-line multimedia communication. The list of their application spans from distancelearning, digital libraries, and home entertainment to fine arts, fundamental and applied science and research. As a result there is some multiplicity of definitions and fluctuations in terminology [2]. In this paper digital (multi)media denotes computer-mediated and controlled integration of numeric, text, graphics and other geometry representations (CAD drawings, 3D models, virtual universes), images, animation, sound, video and any other type of information medium which can be represented, stored, processed and transmitted over the network in digital form. 

Another result of the rapid progress in these fields is the number of challenges for computer systems research and development, 

> © The copyright of this paper belongs to the paper's authors. Permission to copy without fee all or part of this material is granted provided that the copies are not made or distributed for direct commercial advantage. 

> Proceedings of the International Workshop on Multimedia Data Mining (MDM/KDD'2000), in conjunction with ACM SIGKDD conference. Boston, USA, August 20, 2000 

> (O.R. Zaïane, S.J. Simoff, eds.) 

including: 

- enlarged data sets with variety of formats and structures; 

- variety of models for integration of media elements and components; 

- demands on computational efficiency of media analysis and retrieval algorithms; 

- knowledge representation schemes; 

- visualisation metaphors. 

Multimedia (or digital media) representations comprise a collection of domain descriptions in "native" for the domain format. Figure 1 illustrates that variety in terms of the degree to which representation is structured and to what degree the specification of this representation complies with some formal models. The term "hypermedia" is added to stress the presence of links in the digital media under consideration. of knowledge representation and specification. 



<!-- Start of picture text -->
Representation<br>rigorously structured : structured<br>frames, databases<br>semi-structured :<br>multimedia case bases<br>semi-informal : semi-formal : rigorously formal :<br>highly informal : expressed in a expressed in meticulously<br>expressed loosely restricted form of artificial formally defined terms with<br>in natural language natural language defined language formal semantics<br>informal formal<br>tree-structured digital semi-unstructured : Specification<br>rmedia (hypermedia)<br>highly unstructured :<br>flat digital rmedia(hypermedia) unstructured<br><!-- End of picture text -->

**Figure 1. Digital media and domain description (adapted from [8]).** 

The specifics of the domain, where multimedia is used may influence the conceptual model that defines the representation of the multimedia content. The knowledge about the model can be invaluable in the development of multimedia data mining schemes, providing some initial assumptions and structure insights and assisting in the attribute identification. 

Researchers in the database community are viewing multimedia data mining basically as an extension of the knowledge discovery 

104 

in databases, for example, as "the mining of high-level multimedia information and knowledge from large multimedia databases," a "subfield of data mining that deals with the extraction of implicit knowledge, multimedia data relationships, or other patterns not explicitly stored in multimedia databases [14]. Consequently, the framework of KDD applied in multimedia database mining provides similar knowledge representation schemes - association, classification, characterisation and other types rule patterns. This approach, more extensively described in [15], is consistent with the overall KDD methodology. 

In the information system approach, the methods of multimedia data mining are better known as multimedia information analysis and retrieval. The research in the field includes a collection of works in content-based image and video search, fusion of pictorial and other media and efficient storage organisation for multimedia data [3]. 

Is multimedia data mining just a new combination of buzz-words or is it a new interdisciplinary field which not only incorporates methods and techniques from the relevant disciplines, but is capable to produce new methodologies and influence related interdisciplinary fields? The aim of this paper is to present some facets of multimedia data mining in the context of case-based reasoning and computer-supported collaborative work environments. 

###### **2. MULTIMEDIA DATA MINING IN HYPERMEDIA CASE BASES - AN** 

###### **EXAMPLE OF EXTENDING AI SCHEMES** 

Methods developed in multimedia data mining can have significant impact on related fields from data analysis and artificial intelligence. The potential is illustrated on the use of multimedia data mining approach in hypermedia case bases for automating case-based reasoning with unstructured case data. 

###### **2.1 Knowledge representation** 

Case models based on hypermedia representations are becoming popular alternatives to the strict format of object-oriented and attribute-value representations. What exactly is denoted by a case and how it is represented are major structural issues in CBR. When in financial and business applications cases are usually well-structured object-oriented or relational attribute-value representations, in interdisciplinary domains like design, digital media production and visual reasoning, cases are represented in more informal way (see Figure 1). Among the reasons for such diversity, perhaps the major one is the limited expressive power of formal representations. Hypermedia case representation is suitable for domains where it is difficult to fit domain knowledge into structured knowledge representation schemes (see Figure 1). Hypermedia case models offer richer semantics which may be considered both as alternative and extension to the strict format of object-oriented and attribute-value representations. The hypermedia representations comprise a collection of case descriptions represented as text in free or table format and other multimedia data, such as CAD drawings, images, video, sound, etc. Another characteristic of hypermedia is the use of links, where the links can connect information within a case, between different cases, or links to data that lies outside the case library. 

Usually, the representation of the cases in the library is organised according to some conceptual model of the domain. This approach towards complexity is based on the following assumptions: 

- a case is a hierarchy of concepts, or “subcases”; 

- a case is represented by different views. 

This supports case-based reasoning paradigm because subdividing a case in this way allows reasoning to focus only on the relevant parts of that case. By processing only some of the knowledge associated with a case, reasoning can become more efficient. The development of a case-base that has a hierarchical structure usually requires defining a typical decomposition of domain experience. Figure 2 presents an example of domain decomposition - the decomposition of the building design domain according to a structural engineering view of the building. Figure 3 illustrates the use of the ontology in Figure 2 for organising the access to case elements (subcases). 



<!-- Start of picture text -->
Horizontal Vertical Load<br>Span Transfer<br>Horizontal Load<br>Transfer<br><!-- End of picture text -->



<!-- Start of picture text -->
Vertical Longitudinal<br>Span Loads<br>Transverse<br>Loads<br><!-- End of picture text -->



<!-- Start of picture text -->
Footing<br>Depth types<br><!-- End of picture text -->

**Figure 2. Case as a hierarchy of concepts.** 



**Figure 3. Example of hypermedia case organisation.** 

The use of different views of a domain case recognises that the experience in a domain can be understood from different perspectives. An example of this approach is presented in [12]. In this approach, a single, complex design project is represented as multiple cases. The use of multimedia can make it easier to understand complex systems - icons, images, sketches, etc. can highlight and illustrate corresponding text or tabular information. 

Figure 4 illustrates a typical case page, which includes text description, images, CAD drawings and videos. In general, page layout and format are not restricted. Different people develop the actual page content of the different cases over time. The developments in web and multimedia technologies may influence 

105 

the variety of elements, included in these loosely structured case descriptions. 



**Figure 4. An example of a case page.** 

Figure 5 illustrates the idea of shaping the case structure according to a conceptual hierarchy. The semantics of the links depends on the relations between concepts that constitute the representation (Figure 5a). The tree-like structure (Figure 5b) may include some links between pages within a same level. Such links usually appear at a lower level in the hierarchy, where a concept may be related to concepts that belong to different branches in the hierarchy (Figure 5a). 



<!-- Start of picture text -->
P49<br><!-- End of picture text -->



<!-- Start of picture text -->
P24<br><!-- End of picture text -->



<!-- Start of picture text -->
P32<br><!-- End of picture text -->



<!-- Start of picture text -->
P44<br><!-- End of picture text -->



<!-- Start of picture text -->
P48<br><!-- End of picture text -->

attributes, without utilising the advantages of the multimedia information available in the case. 



<!-- Start of picture text -->
Case 1se 1<br><!-- End of picture text -->



<!-- Start of picture text -->
Case 1se 1 Case N<br>....<br><!-- End of picture text -->





###### **Figure 6. Hypermedia case base with additional attributevalue representation** 

###### **2.2 A framework for multimedia data mining in hypermedia case libraries** 

Discovering implicit knowledge in hypermedia case bases is substantially different to data mining in databases. The data organisation units in database data mining are the data tables, in particular their columns or rows. Inside the hypermedia case base the organisational unit is the case or subcase, which merely consists of one or more multimedia pages. The pages comprise a variety of data formats. Knowledge discovery then, in our use of the term, involves finding patterns in primarily unstructured data. More formally the knowledge discovery process in multimedia case representations can be viewed as _machine learning where a case library replaces the training set_ . The approach is illustrated in Figure 7. 



<!-- Start of picture text -->
Hypermedia case library<br>Front page<br>CaseA1 CaseB1<br>CaseA2<br>CaseAn CaseBm<br>….. …..<br><!-- End of picture text -->





###### **Figure 5. Hierarchy of domain concepts, reflected in the case representation.** 

The use of hypermedia to develop case base systems, however, does not solve the problems in building automated reasoning algorithms, which benefit directly from the information in the library. Hypermedia representation as it is supports human reasoning rather than automated reasoning. When this is a reasonable compromise for educational purposes, there is not much use of this approach in the research and industrial case base systems – the system remains simply a structured hypermedia handbook. A common solution is to build an additional structured representation layer, a vector of case attributes. As a rule, the methodology for building such additional layers employs some knowledge engineering techniques for identifying the attributes that represent the domain case and involves domain expert(s). The attribute-value representation of the case is linked to the "entry" page of the corresponding multimedia case representation (an example of entry case page is shown in Figure 3), as shown in Figure 6. The reasoning algorithms operate over the values of the 

**Figure 7. Knowledge discovery in hypermedia case libraries.** 

As illustrated in Figure 8, the information model of the case library constitutes the initial basis for the multimedia data mining [10]. During the data segmentation multimedia data are divided into logical interconnected segments. For example, in a hypermedia case library each segment can include one or more pages. Within particular media type a segment may have different meaning. For example, within a text a segment could be a paragraph, a sentence. The actual mining and analysis procedures are expected to reveal some relations in the segments and between the segments at different levels. For instance, the text analysis can identify relations between concepts presented in the text and the CAD drawings presented on that page (or vice versa, find that the actual CAD drawings are not connected with the content of the text description). The analysis within text segments can identify word concordances that denote complex terms, not explicitly 



106 

defined in the case base. Extracted patterns are incorporated and linked under the framework of the information model. As a result there can be additional attributes, change in links, revision of identified attributes, changes in some attribute values. Some paragraphs, images or other media segments could become insignificant. Consequently, the information model should be able to accommodate changes in the structure and media content. 



<!-- Start of picture text -->
Entrance to a hexagon<br>Knowledge lounge room<br>representation<br>Pattern<br>Entrance to a hexagon<br>extraction lounge room<br>Data<br>segmentation<br>Information<br>modeling<br><!-- End of picture text -->

**Figure 8. A model of multimedia data mining** 

The model is expanded in Figure 9. In case-based reasoning systems the specific interest can be focused in finding patterns in the cases that can assist with indexing and adapting cases as a way of improving the retrieval of related previous experience and indication when an adaptation lies outside some reasonable constraints, based on the experience in the case base. Patterns in the form dynamic thematic paths<sup>1</sup> can assist with the navigation in retrieved cases. The framework combines two consecutive complementary strategies - dataand hypothesis-driven exploration, discussed in more details in [12]. 

The above described data mining schema can be integrated in the learning loop of the cased-based reasoning. The overall enhanced model of case-based reasoning with knowledge discovery backend, as shown in Figure 10, illustrates the dynamics of case manipulation, analysis, mining, knowledge formulation and case update. The visual "symmetry" in Figure 10 reflects in some sense the mutual benefit from the amalgamation of these computing approaches. On the one hand, multimedia data mining has the potential to improve the case-based system. On the other hand, the case-based paradigm provides mechanism for incorporation and management of discovered knowledge. On the indexing side potential advantages in the extended case-based reasoning model include: 

   - generation of term indexing schemes, based on the words used in the text representation [11]; 

   - generation of term indexing schemes, based on relating terms to regularities discovered in other media types; 

   - generation of alternative indexing schemes (for example, a graph structure indexing scheme), based on structural patterns discovered in graphics, image, audio and video media in the case 

- 1 Thematic path is a set of multimedia pages, each of which is part of the case library, that are relevant to the explanation and illustration of particular concept and have to be visited in particular sequence. 

- association of multiple indexing schemes to one case library; 

- dynamic generation of the above listed indexing schemes. 



<!-- Start of picture text -->
Knowledge source Knowledge discovery techniques Extracted knowledge<br>Indexing knowledge<br>Domain vocabulary<br>Ontologies<br>Adaptation knowledge<br> Case library Text statististics<br>Text analysi s Cluster analysis of<br>Case 1 Case N Link tracin g terminology and case texGraph extraction ts Adaptation rules<br>CAD databaanalysis s e Object-relational analysiShape analysis s relationshipsQualitative<br>.... segmentatioImage  n Image analysis methodsAudio/Video dataanalysis Quantitative relationships<br>Navigation knowledge<br>Theme paths<br>Problem profiles<br><!-- End of picture text -->

**Figure 9. The process for multimedia data mining in case libraries** 

On the retrieval side the major advantage comes from the terminological flexibility in formulating queries due to the ontology-guided semantic transformation of the initial query and its match against the ontology-based indexing scheme [7]. 



<!-- Start of picture text -->
3UREOHP &DVH 5HFDOO 5HTXHVW Case base Case parser Structures<br>IRUPXODWLRQ KnowledgeIndexing  5HWULHYHG FDVHV Unstructured text data NarrativeText data AnalyserStructured data ApproximationsStatistics,<br>User<br>Link data User<br>3UREOHPVROXWLRQ &DVH Adaptation  $GDSWDWLRQ 8SGDWLQJ Relational data structures $WWULEXWH�YDOXH SDLUV Knowledge discovery processorCase updater .QRZOHGJH RelationsPatterns,<br>Knowledge<br><!-- End of picture text -->

**Figure 10. Enhanced case-based reasoning model based on the symbiosis between MDM and case-based reasoning.** 

The advantage for the adaptation in the enhanced model is the possibility to modify the new case description based on the information discovered from the multimedia analysis of retrieved cases in the context of the requirements. 

###### **3. MULTIMEDIA DATA MINING IN CSCW**<sup>**2**</sup> **ENVIRONMENTS** 

There are numerous approaches and techniques for setting up a computer-mediated environment for collaborative work [8]. The most common approach is to extend the desktop environment to include tools for meeting and sharing files. This approach takes the individual work environment and adds tools for communicating with others. An alternative approach is to create a virtual world environment in which the collaborators meet, work, and organise their projects. This approach differs conceptually because it creates a sense of place that is unique to the project, sort of a shared office space. A variation on this approach is to create a virtual world that is the model of the product or system being designed or developed. 

The major feature of this kind of collaborative environment is the development of the project within the collaborative, multi-user 

> 2 Computer Supported Collaborative Work 



107 

environment. Project participants can work alone or collaboratively building the model and discussing the product as they view the model. There is only one representation of the model so there isn’t a problem with simultaneous changes to different versions. There is a continuum of the process – a person does not shift environments when designing alone or collaboratively, and there is a continuum of the workspace during the design session - all working information about the product is accessed and shared through the same environment. An example of a project scenario in such environment based on Active Worlds, Inc. virtual world support is shown in Figure 11. 

Such environment is a repository of multimedia data. Multimedia data mining in such environment can be used to enhance the functionality of computer support to project participants. The data includes 3D geometry of the product, data about allocation and behavior of participants in such environments, web multimedia data used in project documentation, presentation of ideas in collaborative sessions, communication transcripts, audio and video records. The example, from on-line analysis of bulletin board records, illustrates the potential for multimedia data mining and support in this field. 



<!-- Start of picture text -->
The project model A link between the design site and the<br>description of the design concept.<br>Client<br>Designers<br><!-- End of picture text -->

**Figure 11. An example of a collaborative project in 3D/2D virtual world** 

Transcripts from online sessions, audio and video files can be used in the CSCW research or in education to form part of the student’s assessment by including the amount and content of the student's participation. Text-based virtual worlds provide in explicit form a descriptive record of all activities inside the world. 3D virtual worlds provide transcripts from synchronous communications. Personal contribution to a collaborative session can be evaluated using text analysis of seminar transcripts [13] and multimedia analysis of related web pages. 

Multimedia bulletin boards preserve the threads and the content of each message. Thus, the analysis of these data sets can be used to evaluate team collaboration. Below is an example of using a visualisation technique, which can provide quick feedback for monitoring collaborative projects. 

Figure 12 presents a fragment from a team bulletin board. The messages on the board are grouped in threads. 

A threefold split of the thread structure of e-mail messages in discussion archives in order to explore the interactive threads was proposed in [1, 9]. It included (i) reference-depth: how many references were found in a sequence before this message; (ii) reference-width: how many references were found, which referred 

to this message; and (iii) reference-height: how many references were found in a sequence after this message. The threefold split was extended in [4] to include the time variable explicitly. This model, expressed graphically as tree, allows the comparison of the structure of discussion threads both in a static mode (for example, their length and width at corresponding levels) and in a dynamic mode (for example, detecting moments of time when one thread dominates another in multi-thread discussions). 



<!-- Start of picture text -->
A<br>B<br><!-- End of picture text -->

**Figure 12. Fragments from an asynchronous communication in a virtual world bulletin board.** 

Visualisation techniques based on this model are modified versions of the nested set visualisation of tree structures [5]. Figure 13 shows an example of such visualisation applied to threads "A" and "B" from Figure 12. Each first message in a level is represented by a corresponding rectangle, labeled in this example to illustrate the message correspondence. Thus, there are four nested rectangles in Figure 13a. When messages are at the same level the thickness of the line is estimated based on the content-analysis of the message, including the text, included graphics and images. Each of the relevant messages on the same level is represented as additional 0.5 pt to the baseline thickness. " In Figure 13b the base line thickness is 1 pt, thus rectangle "M2B has thickness 2.5 pt. 

Figure 14 illustrates the application of the technique for monitoring collaborative design teams. Collaboration on a shared design and development task can be considered at different levels of abstraction and "degrees" of task sharing. Two extreme approaches to sharing design tasks during collaboration are identified in [6]: single task collaboration and multiple task collaboration. During single task collaboration the resultant design (or project development) is a product of a continued attempt to construct and maintain a shared conception of the design task. In other words each of the participants has his/her own view over the whole design problem and the shared conception is developed during intensive discussions. An example, of the visual pattern of such type of collaboration is presented in Figure 14b. It is characterised with relatively large amount of nested rectangles, usually indicating also several messages in respond to particular message. During multiple task collaboration the design problem is divided among the participants so that each person is responsible for a particular portion of the design. Thus, multiple task collaborative design does not necessarily require the creation of a single shared design conception, thus messages are usually related to the project management. Isolated messages and short threads dominate this collaboration style, as illustrated in Figure 14a. 

108 



<!-- Start of picture text -->
• M1A<br>A • M2A • M3A • M4A M4A M3A M2A M1A<br>a. Nested rectangles for single message per level.<br>• M1B<br>• M2B<br>• M3B<br>B • M2B+<br>• M• M2B2B++ M3B M2B M1B<br>•M3B +<br><!-- End of picture text -->

- b. Nested rectangles when there are multiple messages on some levels. 

**Figure 13. Visualisation of discussion threads.** 



a. collaboration connected b. intensive collaboration for more with coordinating creating a joint understanding project tasks and submissions of the problem 

**Figure 14. Patterns of collaboration.** 

Such visualisation techniques, combined with multimedia analysis of (i) video sequences of communications, (ii) elements of the 3D models in the scenery, and (iii) 2D representation of the project media, are expected to be part of the next generation CSCW environments. 

###### **4. EPILOGUE** 

So is multimedia data mining just a new combination of buzzwords or is it an exciting new area, capable to produce new methodologies and influence related interdisciplinary fields. The answer is left to the reader. 

###### **5. ACKNOWLEDGMENTS** 

Author would like to thank the Australian Research Council for the support of the related projects. 

###### **6. REFERENCES** 

- [1] Berthold, M. R., F. Sudweeks, S. Newton and R. Coyne "Clustering on the Net: Applying an Autoassociative Neural Network to Computer-Mediated Discussions," _Journal of_ 

###### _Computer Mediated Communication_ , 2 (4), 

http://www.ascusc.org/jcmc/vol2/issue4/bert-hold.html (1997). 

- [2] Fluckiger, F. Understanding Networked Multimedia: Applications and Technology, Prentice Hall, London (1995). 

- [3] Ip, H. H. S. and A. W. M. Smeulders, eds., _Multimedia Information Analysis and Retrieval_ , Springer, Heidelberg, (1998). 

- [4] Jones, S. ed., _Doing Internet Research_ , Sage Publications, Thousand Oaks, CA, 29-55 (1999). 

- [5] Knuth, D E., _The art of computer programming_ , _Vol 1: Fundamental algorithms_ , Addison-Wesley, Reading, MA, 311-312 (1973). 

- [6] Maher, M. L., S. J. Simoff and A. Cicognani, "Potentials and limitations of Virtual Design Studio," _Interactive Construction On-line_ , January, a1 (1997). 

- [7] Maher, M. L. and S. J. Simoff, "Knowledge discovery from multimedia case libraries", in Smith, I., ed., _Artificial Intelligence in Structural Engineering_ , Springer, Berlin, 197213 (1998). 

- [8] Maher, M. L., S. J. Simoff and A. Cicognani, _Understanding Virtual Design Studios_ , Springer, Heidelberg (2000). 

- [9] Sudweeks, F., M. McLaughlin and S. Rafaeli, eds, _Network and Netplay: Virtual Groups on the Internet_ , AAAI/MIT Press, Menlo Park, CA, 191-220 (1998). 

- [10] Simoff, S. J. and M. L. Maher, "Ontology-based multimedia data mining for design information retrieval", _Proceedings of the ACSE Computing Congress_ , Cambridge, MA, 310 - 320 (1998). 

- [11] Simoff, S. J. and M. L. Maher, "Deriving ontology from design cases", _International Journal of Design Computing_ , 1, http://www.arch.usyd.edu.au/kcdc/journal/vol1 (1998). 

- [12] Simoff, S. J. and M. L. Maher, "Knowledge Discovery in Hypermedia Case Libraries - A Methodological Framework," _Proceedings of the Knowledge Acquisition Workshop, 12th Australian Joint Conference on Artificial Intelligence, AI'99_ , 213-225 (1999). 

- [13] Simoff, S. J. and Maher, M. L. "Analysing Participation in Collaborative Design Environments," _Design Studies_ , 21, 119-144 (2000). 

- [14] Zaïane, O. R., J. Han, Z.-N. Li, S. H. Chee, S. H. and J. Y. Chiang. "MultiMediaMiner: A system Prototype for MultiMedia Data Mining, _Proceedings of ACM SIGMOD International Conference on Management of Data_ , 581 - 583 (1998). 

- [15] Zaïane, O. R., J. Han, Z.-N. Li, J. Hou, "Mining Multimedia Data" _Proceedings CASCON'98: Meeting of Minds_ , Toronto, Canada, 83-96 (1998). 

109 


