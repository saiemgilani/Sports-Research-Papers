<!-- source: randoms/Neural_Network_Modelling_and_Dynamical_S.pdf -->

Sports Med 2011; 41 (12): 1003-1017 0112-1642/11/0012-1003/$49.95/0 

REVIEW ARTICLE 

ª 2011 Adis Data Information BV. All rights reserved. 

# Neural Network Modelling and Dynamical System Theory 

## Are They Relevant to Study the Governing Dynamics of Association Football Players? 

#### Aviroop Dutt-Mazumder,<sup>1</sup> Chris Button,<sup>1</sup> Anthony Robins<sup>2</sup> and Roger Bartlett<sup>1</sup> 

- 1 School of Physical Education, University of Otago, Dunedin, New Zealand 

- 2 Department of Computer Science, University of Otago, Dunedin, New Zealand 

### Contents 

|Abstract. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1003|
|---|
|1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1004|
|2. Search Methodology. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1004|
|2.1<br>Literature Search Technique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1004|
|2.2<br>Inclusion and Exclusion Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1004|
|3. Performance Analysis of Team Sports: a Complex Challenge. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1005|
|3.1<br>Principles Common to Dynamical Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1005|
|3.2<br>Nonlinear Dynamics of Team Sports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1006|
|3.3<br>Association Football Games as Dynamical Systems. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1007|
|4. Pattern Analysis by Artificial Neural Networks (ANNs) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1007|
|4.1<br>Why do Performance Analysts Need ANN Models?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1008|
|4.2<br>Principles of ANN Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1008|
|4.2.1 Supervised Learning (Learning With a Teacher). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1009|
|4.2.2 Unsupervised Learning (Learning Without a Teacher). . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1009|
|4.2.3 Reinforcement Learning (Environmental Feedback) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1009|
|4.2.4 ANN Modelling for the Dynamical Sports Scene . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1010|
|4.2.5 Kohonen Feature Map (KFM) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1010|
|4.2.6 KFM Learning Algorithm. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1010|
|4.2.7 Drawbacks of a KFM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1011|
|5. Analysis of Team Games Using Network-Based Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1012|
|5.1<br>Neural Network Modelling of the Spatiotemporal Characteristics of Team Players. . . . . . . . . . 1013|
|5.2<br>Limitations of an ANN Approach. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1014|
|6. Conclusions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1015|



### Abstract 

Recent studies have explored the organization of player movements in team sports using a range of statistical tools. However, the factors that best explain the performance of association football teams remain elusive. Arguably, this is due to the high-dimensional behavioural outputs that illustrate the complex, evolving configurations typical of team games. According to dynamical system analysts, movement patterns in team sports exhibit nonlinear self-organizing features. Nonlinear processing tools (i.e. Artificial Neural Networks; ANNs) are becoming increasingly popular to investigate the 

Dutt-Mazumder et al. 

1004 

coordination of participants in sports competitions. ANNs are well suited to describing high-dimensional data sets with nonlinear attributes, however, limited information concerning the processes required to apply ANNs exists. This review investigates the relative value of various ANN learning approaches used in sports performance analysis of team sports focusing on potential applications for association football. Sixty-two research sources were summarized and reviewed from electronic literature search engines such as SPORTDiscus<sup>�</sup> , Google Scholar, IEEE Xplore, Scirus, ScienceDirect and Elsevier. Typical ANN learning algorithms can be adapted to perform pattern recognition and pattern classification. Particularly, dimensionality reduction by a Kohonen feature map (KFM) can compress chaotic highdimensional datasets into low-dimensional relevant information. Such information would be useful for developing effective training drills that should enhance self-organizing coordination among players. We conclude that ANN-based qualitative analysis is a promising approach to understand the dynamical attributes of association football players. 

##### 1. Introduction 

There have been a number of developments in the context of sports performance analysis, which were discussed recently in a stimulating review by Glazier.<sup><u>[1]</u></sup> For example, in the past, performance analysis has been much maligned for its fragmented application and lack of theoretical framework. However, dynamical systems theory (DST) has the power to potentially unify existing sub-disciplines such as sports biomechanics, notational analysis, motor control, physiology and psychology under one macroscopic platform ~~.~~<sup><u>[1]</u></sup> In this review, we will continue where Glazier’s provocative position statement ended, by describing how emerging nonlinear analytical tools (i.e. neural network modelling) are being used to detect the key principles of dynamical systems conceptualized as team sports. 

The review begins by summarizing some of the key challenges facing performance analysts in the 21st century. With recent advances in motion tracking technology (such as global positioning system, radio-based signal detection, automatic video tracking, etc.), there are now ample opportunities to study the collective behaviours of groups of players with a high level of sensitivity and objectivity ~~.~~<sup><u>[2]</u></sup> It is important that performance analysts adopt sensitive and meaningful analytical techniques suited to the high-dimensional datasets, which result from tracking the coordinate profiles 

of players. It is noted that many studies are beginning to identify hallmark features of DST within high-dimensional datasets. In the second half of the review we consider a number of nonlinear data analysis techniques that are potentially suited to summarize the patterns and structure underlying team sports behaviour. In particular, artificial neural network (ANN) modelling emerges as a promising candidate to best cope with the nonlinear, chaotic patterns hidden within the data. 

##### 2. Search Methodology 

###### 2.1 Literature Search Technique 

A literature search was performed in February, 2011. Electronic database literature included SPORTDiscus<sup>�</sup> , Google Scholar, IEEE Xplore, Scirus, ScienceDirect and Elsevier. The search terms used were individual words and/or combinations from the following list ‘team games’, ‘inter-personal coordination’, ‘dynamical system theory’, ‘complex systems’, ‘team behaviour’, ‘association football’, ‘artificial neural network’, ‘self-organizing maps’ and ‘performance analysis’. 

###### 2.2 Inclusion and Exclusion Criteria 

The search was restricted to journal articles, conference proceedings and books written in 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Neural Network Modelling and Dynamical Systems in Association Football 

1005 

English and German. The findings of each source were retrieved, as were any pertinent secondary citations for additional information that had been missed by the primary search. Although a total number of 142 sources were reviewed initially, these were later filtered to the 62 sources deemed most relevant in accordance with the scope of the journal guidelines. 

##### 3. Performance Analysis of Team Sports: a Complex Challenge 

Team sports (such as association football, rugby, handball, basketball, cricket, hockey and netball) constitute some of the most widely participated and watched of all sports played globally. Simple summary statistics in team sport, such as ball possession, territory occupied and number of shots created, provides only a partial explanation of the credibility of a team. Indeed, one of the main challenges facing performance analysts is how to identify common patterns in games that best explain the overall performance of teams. The complex player movements are hard to quantify and predict with most mathematical models. Loose couplings and fluctuations of player movements exist at many different levels on different timescales (e.g. individual players, sub-units of teams – i.e. defenders, dyadic groups, i.e. an attacker and a defender – and also globally between the two teams). Unsurprisingly, it is difficult even for experienced observers such as coaches to reliably detect and interpret such chaotic patterns. Fortunately, knowledge of the theoretical principles common to dynamical systems can allow performance analysts to assist in this challenging endeavour. 

###### 3.1 Principles Common to Dynamical Systems 

Almost all team games share an implicit similarity in terms of the collective movements of players during the ebb and flow of invasive and defensive styles of play.<sup><u>[3]</u></sup> It is likely that common functional principles may underpin a number of different team games because they each represent dynamical systems. In general, dynamical systems are physical, chemical, biological or social systems that exhibit many independent degrees of 

freedom or components that vary over space and time. These complex systems are typically open systems capable of interacting with the environment and are in a constant state of flux due to changes in internal and external flows.<sup>[4]</sup> However, dynamical systems are adaptive ~~,~~<sup><u>[1]</u></sup> and surrounding constraints serve to form orderly<sup><u>[5]</u></sup> and stable relationships among the many degrees of freedom at different levels of the system.<sup>[6]</sup> 

Various sub-systems in a dynamical network provide multiple examples of ‘degeneracy’, the ability of elements that are structurally different to perform the same function or yield the same output. In the context of team sports, degeneracy can be viewed as the phenomenon where different players coordinate among themselves, which results in either attacking or defending processes. The team then interacts and adapts dynamically to attain a common purpose,<sup><u>[7]</u></sup> such as preventing the opponents from scoring. The process of coadaptation has been used to explain how sophisticated biological systems evolve and adapt their behaviour to satisfy long-term, evolutionary constraints.<sup><u>[8]</u></sup> 

At a microscopic level, relevant degrees of freedom (collective variables) are driven by the coordination between the synergetics that also influence the macroscopic behaviour of dynamic systems, i.e. circular causality (see Kelso ~~,~~<sup><u>[9]</u></sup> p. 16). An invasive attack in a typical team game depicts circular causality. For example, an attacker tries to deceive the defender with a repertoire of dribbles whilst team-mates move to support the player in possession (thereby providing passing options) and collectively improving the chances of scoring. Whilst, there is no master equation to quantify the movements of different players, the conceptual framework of the dynamical systems predicts that similar patterns of play result from basic mechanisms and principles ~~.~~<sup><u>[9]</u></sup> 

Dynamical systems have variable quantities of energy moving among their components at any given instance (excepting physical systems in equilibrium) ~~.~~<sup><u>[10]</u></sup> Internal energy within the system (e.g. phosphate utilization within the muscles) interacts with the available energy flows in the environment (e.g. gravity, light, sounds, friction, etc.) and accordingly alters the system (team) organization.<sup>[11]</sup> 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Dutt-Mazumder et al. 

1006 

Drawing upon Bernstein’s<sup><u>[12]</u></sup> ideas, it can be hypothesized that sports teams should organize fluently if the external environmental energy is harnessed efficiently. 

A dynamical system has an implicit relation to nonlinearity. According to DST, a slight perturbation in the present state (e.g. a counter-attack opportunity) can evolve and lead to unpredictable states of the game. However, in the long term, the randomness of the system is said to ascribe to a chaotic attractor once the system has reached a stable state (i.e. no more exchange of energy between the sub-systems). A number of stable states exist within dynamical systems (metastability), where the constraints imposed on the system gives rise to its present state.<sup>[13]</sup> Thus, different functional movement patterns of players can achieve a performance goal under specific environmental circumstances ~~.~~<sup><u>[10]</u></sup> 

###### 3.2 Nonlinear Dynamics of Team Sports 

The study of team sport games as dynamical systems can be approached in two manners. The first approach, which has received limited attention to date, involves the application of analytical tools of nonequilibrium thermodynamics.<sup><u>[14,15]</u></sup> The second approach involves the formulation of synergetic and nonlinear equations to model the dynamics of human movement.<sup>[16]</sup> Sports such as association football,<sup>[17]</sup> badminton,<sup>[18]</sup> basketball ~~,~~<sup><u>[19]</u></sup> boxing,<sup>[20]</sup> rugby union,<sup>[21]</sup> squas ~~h~~<sup><u>[22]</u></sup> and tenni ~~s~~<sup><u>[23]</u></sup> have received this kind of analysis. This latter approach tries to quantify the human movement pattern by devising dynamical formulas, which equate the fluctuations in system behaviour under the influence of constant energy transactions with the environment (i.e. perturbations). However, studying dynamical systems using equations pertaining to perturbations has some practical disadvantages, since these equations are practically limited to weak nonlinearities ~~.~~<sup><u>[24]</u></sup> To overcome this limitation, graphical methods such as Kohonen feature maps (KFMs) to analyse nonlinear behaviour have had an increasing impact. 

Complex social networks can be studied in order to identify players who most frequently interact with fellow players in a match<sup>[25]</sup> (sometimes 

called ‘hot-links’). This methodology can reveal the collective behaviour in team sports by quantifying the frequency of the internodal pairing. Team sports are composed of multiple and dynamic couplings among dyads of players, which function under similar principles of coordination dynamics.<sup>[18,26]</sup> Such couplings appear to exist whether a sport is contested by 2 versus 2, 5 versus 5, or 11 versus 11 players. For example, common attributes of dynamical systems have been demonstrated both in small-side ~~d~~<sup><u>[27]</u></sup> and also conventional association football matches ~~.~~<sup><u>[28]</u></sup> 

Bourbousson and colleagues<sup>[29]</sup> calculated intraplayer relative phases to analyse player movements in basketball matches. The ‘stretch index’ was also implemented, which measured the expansion and the contraction of the team court coverage as the game progressed. Perturbations in game stability were described as destabilizations of the phase relation from which the system either re-stabilizes some time thereafter, or otherwise remains destabilized up to some outcome of the game sequence ~~.~~<sup><u>[30]</u></sup> It was demonstrated that the configuration of each team oscillates longitudinally and laterally with substantial coupling between the teams. However, quantitative analysis using statistical measures such as ‘stretch index’ provides summary, discrete interpretations of pattern analysis. The collective behaviour of a dynamical system cannot be studied by summing the behaviours of the sub-phases ~~.~~<sup><u>[31]</u></sup> A robust approach is needed, which can calibrate and quantify the time evolving the dynamic sports scene. 

Recent studies have advocated the application of relative phase to measure inter-personal dynamics ~~.~~<sup><u>[32]</u></sup> McGarry<sup><u>[31]</u></sup> investigated the attackerdefender dyads in basketball using the dyad pairs contained within an ellipse. The results revealed that strong attraction existed for small (one vs one) attacker-defender dyads, but the strength of the attraction weakens uniformly as the number of players increases.<sup>[29]</sup> In terms of system perturbations, it was found that the attacker tries to create spaces, whereas the defender tries to block spaces.<sup>[18]</sup> Encouragingly, it was noted that the phase relations exemplified the metastability principles of the dynamical system for dyadic interactions in basketball. 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Neural Network Modelling and Dynamical Systems in Association Football 

1007 

The behaviour of a team game may be looked upon as an outcome of dyadic interactions at different scales. This outlook is based on the universality of complex systems, which testifies that complex systems will ascribe to similar descriptions on different levels of analysis and time scales.<sup><u>[9]</u></sup> In the past, performance indicators were used to quantify behaviour in sports. However, the relation between behaviour (action) and outcome (result) is not clearly substantiated.<sup><u>[22]</u></sup> If performance indicators for the player or a team are awarded to show their performance prowess, then this invariably points out the weak performance of the opponent player or a team ~~.~~<sup><u>[31]</u></sup> Thus, performance indicators are influenced by the player-opponent synergetic. Instead, team behaviour may be better represented as a function of the interactions of players and teams.<sup>[29]</sup> In the next sub-section, we suggest that association football is showing encouraging signs in relation to adopting this emerging type of performance analysis. 

- 3.3 Association Football Games as Dynamical Systems 

Association football consists of an intricate web of complex athletic, physical skills that present a high degree of difficulty for performance (match) analysis. Like most team sports, football games result from a blend of tactical and emergent organization. Performance analysts can provide fascinating insights into how players interact and respond to sudden attacks (perturbations) and reorganize themselves to stop such instabilities on the pitch. For example, in the 2011 European Champions League competition, the Fe´ de´ ration Internationale de Football Association (FIFA) website displayed player positional profiles in the form of heat maps as an enhanced analysis feature for the general public.<sup>[33]</sup> 

Existing research has tended to examine only isolated phases of team games as illustrated earlier.<sup>[18,19,21]</sup> As yet, it is unclear whether the findings can be generalized to real-game play, in which numerous other variables including contextual constraints (e.g. score, the time left in the game, etc.) and organismic constraints (e.g. fatigue, injury, relative velocity of dyads) fluctuate substan- 

tially. Intuitively, it seems inappropriate to study the sub-systems individually since they are interdependent and will not provide an overall measure of the complexity. Complexity is something ‘hidden’ within the time series of a movement sequence or strategy as it emerges over time ~~.~~<sup><u>[24]</u></sup> 

A clear requirement for future research is to adopt more holistic analytical approaches to demonstrate the unifying principles of dynamical systems in football matches. For example, it would be interesting to investigate whether the trajectories of the players converge into a strange attractor on the pitch, during critical periods of the game. The considerable remaining challenge is how to make sense of the high-dimensional data sets needed to test such an idea. The application of conventional, assumption driven, linear statistical tools will not allow nonlinear investigations in association football. Primarily, this is because linear statistics are well suited to describing the discrete amounts of information flowing through a system, but are less well equipped to examine the time-evolving, integrated nature of system behaviour, which is where ANN modelling can play a significant role. 

##### 4. Pattern Analysis by Artificial Neural Networks (ANNs) 

Stergiou et al.<sup>[34]</sup> proposed several nonlinear tools to study specific features of complex human movements, e.g. Lyapunov exponent (LyE), correlation dimension (CoD), approximate entropy (ApEn) and ANNs. Such tools, which operate with few assumptions about the structure of the dataset, are undoubtedly useful and their application to complex datasets will become increasingly widespread in the future. However, ANNs have a global advantage over the nonlinear tools, primarily because the architecture addresses the descriptive factors of the global game process (velocity, dispersion rate, task type, team experience/learning, etc.) rather than individual features such as rate of divergence of trajectories in state space (LyE), fractal dimension in dynamical systems (CoD), or the complexity, regularity and predictability of a time series (ApEn). Also, ANNs overcome the computational burden of applying these individual measures separately.<sup><u>[35]</u></sup> 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Dutt-Mazumder et al. 

1008 

In its most popular form, an ANN is a data processing technique based on the computational principles of the brain, performing a task of interest. It captures the input-output behaviour of absolute or dynamic systems. The fundamental task of a typical ANN model is to establish global and complex behaviour defined by the connections between processing elements (nodes) and element parameters (learning rate, momentum, error criterion, activation function, etc). Crucially, their architecture lets them perform nonlinear processing and thereby model real, natural and physical problems such as the BienenstockCooper-Munro theory,<sup>[36]</sup> spiking neuron,<sup>[37]</sup> stock prediction,<sup>[38]</sup> weather forecasting,<sup>[39]</sup> etc. 

###### 4.1 Why do Performance Analysts Need ANN Models? 

Studies suggest that descriptive parameters of players movement behaviour (see section 4), which may reveal important characteristics governing the dynamics of a team game, do not behave as simple periodic functions of space and time,<sup>[40,41]</sup> thereby limiting the application of conventional statistics. Hence, quantifying the highdimensional datasets is beyond the scope of linear statistical tools. From a statistical outlook, ANNs are considered as nonparametric data processing tools.<sup>[42]</sup> 

First of all, ANNs are typically nonlinear as the nodes have nonlinear activation functions. Second, an ANN can be designed to change its synaptic weights in real time ~~.~~<sup><u>[35]</u></sup> Consequently, it is ideal for performing tasks, such as pattern classification and recognition, because ANNs not only select the appropriate pattern but can also provide information about the confidence of the decision made, thereby rejecting ambiguous patterns.<sup><u>[35]</u></sup> ANN models are fault tolerant and well suited to performing realistic tasks. Since all the data are stored across the network, partial damage to the network hardware will not terminate the performance instantaneously. Network-based qualitative techniques allow the extraction of specific striking features from the complex, high-dimensional data sets that are typical to team games. Finally, ANNs compute input data sets through a model- 

free response mechanism, i.e. no prior assumptions are made on the statistical model.<sup><u>[35]</u></sup> 

It is often the case that the inputs to neural networks have a large number of elements (high dimensional). Where such inputs produce outputs of lower dimensionality they are often referred to as performing dimensionality reduction. The most common example of such a network is a KFM network. Thus, ANN models give rise to a new dimension of pattern analysis in a dynamical sports arena. 

Some classes of ANNs are characterized by an ‘energy’ value associated with every possible state, and therefore the dynamical behaviour of the system can be described as the movement of a point on a complex energy surface. The purpose of many learning algorithms is to create stable states as minima on these energy surfaces. Instead of random or chaotic behaviour, the state of the network evolves so as to perform gradient descent to stable energy minima.<sup><u>[43]</u></sup> 

Self-organization refers to the development of patterns or regularities of behaviour without the control of some central or external agent. It is often the case that these patterns are observable at some level of description (such as an apparently goal-directed behaviour) but they arise from mechanisms and some lower level of description (such as a reinforcement learning algorithm). ANNs that use unsupervised or reinforcement-based learning algorithms are often described as self-organizing. Since the behaviour of the networks arises from the interaction of very simple computational elements, their behaviour is also emergent. Hence, ANNs provide us with well understood tools for studying self-organization and emergent processes. 

In a subsequent section, we propose how performance analysts can use ANNs to extract from chaotic patterns of behaviour in team sport, the characteristics that determine successful performance. But first, let us consider at a fundamental level how ANNs operate. 

###### 4.2 Principles of ANN Learning 

Primarily, ANNs have three phases, such as the training phase, test phase and application phase. ANNs undergo training when an empirical or 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Neural Network Modelling and Dynamical Systems in Association Football 

1009 

random data set is presented into the network. The fundamental attribute of an ANN model is that when the network is trained, the internal parameters in the network adapt and respond to the learning rule, i.e. training phase. These prescribed learning rules are chosen according to the task to be studied, and constitute the learning algorithm of the solution. The generalization of the network is assessed in the test phase. Finally, the new datasets are fed into an ANN to evaluate the reality. In principle, an ANN model can be adapted according to the following three broad learning approaches: (i) supervised learning, (ii) unsupervised learning and (iii) reinforcement learning. 

###### 4.2.1 Supervised Learning (Learning With a Teacher) 

The aim of supervised learning is to learn some input-output mapping between data sets using a feed-forward network (figure 1). For each input, the actual output is compared with the desired output. The weights are adjusted to get the actual output closer to the teacher. 

Earlier studies have used supervised learning to model swimming performance.<sup>[44]</sup> However, this form of learning is not ideal for studying dynamical systems as a target output is specified within the network. In a typical dynamical system, the outcome is subjected to perturbations, which keep evolving with time and hence cannot be predefined. 

###### 4.2.2 Unsupervised Learning (Learning Without a Teacher) 

The goal of unsupervised learning is to learn regular or structured aspects of the input pop- 



<!-- Start of picture text -->
Environment<br>Input vector representing<br>the state of the environment<br>Learning Teacher<br>system<br>Actual<br>Error signal response Desired<br>response<br>Decision<br>box<br><!-- End of picture text -->

Fig. 1. Supervised learning in a typical artificial neural network model (adapted from Haykin<sup><u>[35]</u></sup> ). 



<!-- Start of picture text -->
Environment<br>Input vector representing<br>the state of the environment<br>Learning system<br><!-- End of picture text -->

Fig. 2. Unsupervised learning in a typical artificial neural network model (adapted from Hayki ~~n~~<sup><u>[35]</u></sup> ). 

ulation (figure 2). Unsupervised learning is used to address temporal configurations of a dynamical system. In a feed-forward network, for each input, the ‘detector units’ (identify specific features) adjust their weights according to the neighbourhood, activation and learning functions that describe the network behaviour. Weights are optimized according to the prescribed task, which usually maximize the same measure of similarity. Examples of unsupervised learning include the competitive learning rule that operates with the ‘winner-takes-all’ strategy<sup>[34]</sup> and a KFM. 

Unsupervised learning is highly favoured by researchers concerned with pattern recognition/ classification. The absence of any target output vector ensures that the outcome of learning is not predetermined and the network will find its own solution. In the training phase the network is presented with several patterns, which it classifies according to the pattern category. In the test phase it categorizes new unknown patterns, based on the information it had extracted from training datasets. A similar concept was used to investigate tactical structures in handball ~~,~~<sup><u>[45]</u></sup> movement variabilit ~~y~~<sup><u>[46]</u></sup> and coordination using gait data ~~.~~<sup><u>[47]</u></sup> 

###### 4.2.3 Reinforcement Learning (Environmental Feedback) 

The aim of reinforcement learning is to learn typical input-output mapping, using a feed-forward network (figure 3). For each input, the actual output generates some general feedback on the ‘goodness’ of the output, and the synaptic weights are adjusted to try and maximize the goodness. 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Dutt-Mazumder et al. 

1010 



<!-- Start of picture text -->
Environment<br>Input vector representing<br>the state of the environment<br>Primary<br>Actions reinforcement<br>Learning Critic<br>system<br>Heuristic<br>reinforcement<br><!-- End of picture text -->

Fig. 3. Reinforcement learning in a typical artificial neural network model (adapted from Hayki ~~n~~<sup><u>[35]</u></sup> ). 

Desired outputs are not supplied by the teacher, but there is general feedback on how ‘good’ the outputs are, i.e., there is environmental feedback. 

The reinforcement rule is not favoured while analysing real-world problems, as it can be complex and time consuming. The application favours tasks that require nonlinear feedback or decision making (e.g. control of robotic arms and unmanned vehicles). 

###### 4.2.4 ANN Modelling for the Dynamical Sports Scene 

A typical ANN architecture, which implements unsupervised learning, is the KFM. Dynamical controlled network (DyCoN), based on the KFM concept, supplies each node with an individual internal memory and an adaptive learning algorithm.<sup>[48]</sup> This ensures that DyCoN has no final state and can learn continuously and in separate phases. Also, recurrent networks, which are yet to be utilized in sports research, have the architecture to process temporal data sets. They can be tailored, according to the prescribed task with supervised learning<sup><u>[49]</u></sup> or reinforcement learning.<sup><u>[50]</u></sup> In short, there are many architectures in the family of an ANN, but exhaustive study of specific ANN models is beyond the scope of the article. We will now focus on the KFM, which can recognize and classify patterns based on the variables resulting in significant events in a game (i.e. a goal scoring opportunity). 

group basis. For presented inputs, the output node that wins the competition is called a ‘winnertakes-all neuron’ ~~.~~<sup><u>[35]</u></sup> Each node represents process types (section of a match), and each cluster represents a class of a similar process type. Based on competitive learning, the architecture of the network can be fabricated to develop its model such as that of a KFM and the Willshaw and von der Malsburg model ~~.~~<sup><u>[51]</u></sup> The term KFM comes from the capability to recognize patterns or clusters in the data without supervision/target data ~~.~~<sup><u>[52]</u></sup> 

A KFM is an essential tool for analysing dynamical movement patterns in sports. The KFM architecture compresses surplus high-dimensional inputs to a low-dimensional structure (e.g. one- or two-dimensional [2-D]). Dimensionality reduction is performed to recognize and validate structures visually, yet preserve nonlinear topological relationships in the data sets.<sup><u>[53]</u></sup> This helpful feature retains the relevant information and discards irrelevant information in high-dimensional datasets, which is typical of dynamical systems. They consist of an ‘input layer’ and a presumed ‘competition layer’ (figure 4). 

The weights of the connections from the input nodes to a single node in the competition layer are interpreted as a reference vector in the input space, i.e. a self-organizing map represents a set of vectors in the input space and one vector for each node in the competition layer. 

###### 4.2.5 Kohonen Feature Map (KFM) 

Self-organizing maps are a class of ANN model, based on a method called competitive learning, where the output nodes compete amongst themselves to be activated on a per- 

###### 4.2.6 KFM Learning Algorithm 

The aim of a KFM is to activate different nodes of the network to respond similarly to inputs.<sup><u>[35]</u></sup> Node weights are initialized to small random values or sampled evenly by the two largest prin- 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Neural Network Modelling and Dynamical Systems in Association Football 

1011 

cipal component eigenvectors. An initial neighbourhood radius is defined and the subsequent distance between each input and output node is computed, according to the given equation (equation 1):<sup><u>[53]</u></sup> 



where xi (t) = input to node i at time t and wij (t) = weight from input node i to output node j at time t, N = neighbouring nodes. 

For each input vector the ‘winning node’ is determined. There are two possible methods; maximal dot product: i<sup>*</sup> = argmax (wi, x); minimal euclidean distance: i<sup>*</sup> = argmin (wi, x). 

The KFM training phase consists of input vectors (e.g. coordinates of players) in a random order. The KFM training consists of weight updates of ‘winner node’ i<sup>*</sup> and its neighbouring nodes in Ni*i (t) are updated according to the learning equation (equation 2). 



The neighbourhood function can be symmetric (e.g. rectangular and Gaussian) or anti-symmetric (equation 3): 



where the rectangular neighbourhood function is based on the Manhattan distance between nodes dM (i<sup>*</sup> i) where l (t) is the neighbourhood parameter. The Gaussian neighbourhood function (equation 4): 



where the neighbourhood function is based on the Euclidean distance between nodes dE (i<sup>*</sup> i). The Gaussian function is preferred over the rectangular, since it gives smoother mapping from input points to weight coordinates.<sup>[55]</sup> Regardless of the neighbourhood functional form, both shrink with time. The training can be stopped after it undergoes a number of predefined iterations (tmax) defined by t = tmax. 



where wij (t) = initial weight; wij (t + 1) = updated weight; Z (t) = learning rate, which decreases with time and Ni*i (t) = neighbourhood function (adapted from Lippman ~~n~~<sup><u>[54]</u></sup> ~~)~~ 

###### 4.2.7 Drawbacks of a KFM 

Although a KFM is ideal for pattern recognition and classification, it has some crucial limitations. For example, real-time analysis (e.g. evaluating 



<!-- Start of picture text -->
Competition layer: each output node has an associated vector of  N  weights<br>Kohonen layer<br>Wi<br>X<br>Input layer: each node represents one element in a population of  N  element input vectors<br><!-- End of picture text -->

Fig. 4. Kohonen feature map input patterns. Wi = weight from input node I; N = neighbouring node; X = input vector. 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Dutt-Mazumder et al. 

1012 

tactical patterns during half-time in a typical football match) would require considerable effort. Also, the requisition for training data is quite large (20000–30000 epochs), depending upon the complexity and variability of the patterns. The logic behind this is that the impact of any individual training pattern is extremely small, whereas, the number of patterns that have to be learned is statistically large. On completion of training, the KFM freezes and further re-initiation of the training cannot be commenced ~~.~~<sup><u>[53]</u></sup> Also, the learning mechanism in the conventional KFM is externally controlled, which implements predefined and rigid functions for controlling the learning process. In the subsequent sections, we will discuss some of the past studies in team games using network-based tools and suggest some novel techniques to analyse an association football team. 

##### 5. Analysis of Team Games Using Network-Based Techniques 

As mentioned in section 3.3, a typical team game can be considered as a dynamical system, which encourages the scope of applying network modelling tools to study team behaviour. DST proposes that player movements are susceptible to task dependent and environmental perturbations, which result in a new phase state.<sup>[17]</sup> Investigation of individual patterns is a time consuming and challenging task. Instead, similar patterns in the game processes can be identified and clustered in the KFM lattice ~~,~~<sup><u>[56]</u></sup> which is beneficial in replacing complex patterns with simpler specifications. The clusters depict the process type, the highlighted nodes represent the occurrence of the pattern and the diameter of the neighbouring updated nodes highlight the frequency of the associated processes. This approach was used to evaluate the tactical structures in volleyball and squash games.<sup>[48]</sup> 

Also, it is challenging to represent the player movement patterns in terms of nonlinear, threedimensional (x, y, t) spatiotemporal mathematical models.<sup><u>[57]</u></sup> KFMs have categorically been implemented to study the dynamical structures typical to a team game.<sup><u>[58]</u></sup> 

Game intelligence in team games (handball and soccer) has been evaluated using a network- 

based approach.<sup><u>[59]</u></sup> The distribution of clusters on the KFM lattice gives an idea of the quality of training, and also detects striking performancerelated features (correlated and nonrelated). The data matrix (figure 5a) was mapped into a structural mapping on the network (figure 5b) that helped to recognize qualitative features (figure 5c) and analyse the dynamical processes involved. This approach depicts correlated inputs in the form of clusters (figure 5d). A typical team game consists of several processes, and researchers face a daunting task to conduct conventional quantitative analysis (e.g. an ANOVA test) on these different processes. However, a KFM can cluster similar processes into definite classes and the game structure as a whole can be studied ~~.~~<sup><u>[58]</u></sup> 

An intriguing study examined the movements of robotic players in a 2-D simulated soccer RoboCup ~~.~~<sup><u>[53]</u></sup> The dynamics of a virtual team game has sharp contrasting features with the real football game. However, the generated data sets present useful information about the complexity of real games. Relative motion vectors of the players along with the relative position of the balls were aggregated over several time steps that resulted in high-dimensional data sets. These data sets were used to train the KFM. The different clusters highlighted different kinds of motion patterns. The frequency distribution of the data sets was able to demonstrate the credibility of one football team. This interesting technique could potentially allow researchers to objectively quantify the skill level of teams or different players in the game. 

Using the principles of supervised learning, the back propagation algorithm<sup><u>[59]</u></sup> has been applied to study the interpersonal dynamics of rugby players.<sup>[60]</sup> Although the principle of a typical dyadic system is the same, the constraints differ according to the rules of the game. For example in a Rugby game, a forward pass is not permissible, and also the unique shape of the ball makes a kick pass a challenging task. The data sets were in the form of spatial co-ordinates that were presented to the input layer. The input layer consisted of the four nodes (x and y co-ordinates of frontal and transverse camera positions) that provided the spatial configuration of the dyadic system (attacker and defender). The architecture 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Neural Network Modelling and Dynamical Systems in Association Football 

1013 

|**a**|Data m|atrix|of tr|ainin|g p|aramete|rs<br>**b**|
|---|---|---|---|---|---|---|---|
|3|7<br>1|5|5|9|1|1<br>2|1<br>6|
|5|3<br>3|1|5|8|7|7<br>9|2<br>5|
|4|3<br>1|3|6|9|1|1<br>6|7<br>2|
|6|2<br>5|2|4|7|4|3<br>7|1<br>9|
|7|6<br>4|1|2|2|9|3<br>8|8<br>2|
|6|1<br>9|5|4|2|1|4<br>5|7<br>4|
|4|3<br>4|5|3|8|1|8<br>8|3<br>9|
|8|1<br>2|1|1|1|5|3<br>9|7<br>2|
|6|5<br>9|2|4|2|8|4<br>4|7<br>1|
|1|7<br>4|2|5|8|9|1<br>6|3<br>2|
|(0,0,1,0)<br>(0,1,0,1)<br>**c**|(1,1,1,0)<br>(1,0,1,0)||||||MD=midfield defense<br>GD=goal defense<br>GT=goal throw<br>PA=position attack<br>CA=counter attack<br>C=penalty box<br>crossing<br>RWA=right wing<br>attack<br>LWA=left wing<br>attack<br>MD<br>GT<br>PA<br>GD<br>C<br>CA<br>RWA<br>LWA<br>**d**|



Fig. 5. High-dimensional dataset mapped on the Kohonen feature map lattice to illustrate game processes. (a) Data matrix; (b) structural mapping on the network; (c) qualitative features; and (d) dynamical processes. This approach depicts correlated inputs in the form of clusters (figure 5d). 

was used to explore variables such as interpersonal distance with respect to the try line and vertical oscillations of the dyadic system. Although the study demonstrated that successful attacks had increased variability, it had no potential evidence of integrating the sub-phase (dyadic system) with the team (dynamical system). 

Isolated studies investigating the sub-phases of a team game would not make much difference if the researcher is set to study the overall dynamical configurations of a team game. This is because all the sub-phases of the game share implicit nested relations with the entire system (team) as a whole. The sub-phases are in constant interaction with each other, which results in a new state phase over time. One would argue that the boundaries of a dynamical system cannot be demarcated. How- 

ever, in a typical team game such as association football, the dimension of the field is laid down by FIFA. Thus, investigations in a team game underpinning the principles of DST are possible, since all the changing states are confined in the dimensions of the field. 

###### 5.1 Neural Network Modelling of the Spatiotemporal Characteristics of Team Players 

As discussed in section 4.2.2, nonlinear ANN architectures favour pattern recognition and classification; this should allow researchers to investigate the spatiotemporal behaviour of the interacting sub-systems (players) within the dynamical system (team). Although complete, real-time 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Dutt-Mazumder et al. 

1014 

match analysis is challenging, partly because highdimensional datasets slows ANN computational rate, it is also hypothesized that the synergetic interactions between players emerge and decay in different phases of the game. However, a fruitful approach, at least initially, could be to analyse games only during critical periods of the game. The critical periods of the game can be in the form of set plays (free kick, throw in, corners) and during the build up to successful goal attempts. 

The trajectories (spatiotemporal co-ordinates) of the players can be compiled on a data matrix using tracking devices that can be mapped on the KFM lattice, and patterns can be classified according to their behavioural characteristics. This process can be repeated several times and a library of data sets can be compiled for future pattern recognition. Pattern recognition would allow us to investigate the self-organizing behaviour of the players on the field. The study can be further extended by performing a qualitative analysis of the nodal structures on the KFM lattice (e.g. unified distance matrix, which maps high-dimensional data set on a 2-D lattice). One can add noise from tracking variables and induct them during ANN training. This would make the training phase more robust. Adding noise will not be random numbers, since all the variables would be gathered from the match itself. 

In an earlier study, the tactical structures of handball matches were investigated, using a KFM-based model.<sup><u>[45]</u></sup> The offensive patterns were clustered on the KFM lattice using the definite playing processes as input patterns. The tactical structures represent the evolving behaviour of the team through different time frames. It would be interesting to see how the decisionmaking process (tactical structures) of the players changes when they are trained with ‘attention broadening techniques’.<sup><u>[61]</u></sup> Such investigations would lead researchers to understand the principles of interpersonal behaviour in a team game. Based on these results, one can frame training drills that develop better interplayer bonding in a team game. Also, individual performance is a function of the whole team. Hence, investigations on team bonding and inter-relationships would be a crucial factor for the excellence of a team. 

###### 5.2 Limitations of an ANN Approach 

Although a neural network-based approach is advantageous to study typical team games, ANN models have some fundamental limitations. First of all, the parameters have to be defined before the training is initialized. This is a crucial factor in training the network. Unrealistic parameter settings give abstract clusters on the topographical maps. To avoid such ambiguous parameter settings, further heuristics can be used to extend the basic-training algorithm (e.g. every adjustable network parameter of the activation should have its individual learning-rate parameter). Relatedly, training the network model takes time; hence, for the time being, it is more likely that ANNs may be restricted for post-match analysis rather than to inform the tactical decisions of the coach during a game. 

In addition, the behaviour of a typical ANN is opaque; although an investigation contradicted the conception of ANNs as black boxes.<sup>[62]</sup> They produce output without explanations. Therefore, considerable effort and experience is required to study the internal structures of the network for some insight into its ‘reasoning’. Once the training has been completed in KFM, the model freezes and further re-initiation of the training cannot be commenced. Thus, a KFM behaves like a tool after training is terminated. The important analytical procedure of dimensionality reduction means that the researcher has an important role to play in interpreting the low-dimensional outputs in relation to actual high-dimensional game behaviours. 

Whilst network modelling appears a promising approach to identify the emerging patterns in association football, it is interesting to speculate why relatively few empirical studies have been published to date. A number of important procedures in network modelling, such as parameter setting, dimensionality reduction and interpretation of output, are skills that are shared by only a relatively small population of performance analysts around the world. Indeed, considerable effort and experience must be expended to study the internal structures of the network for some insight into its ‘reasoning’. Relatedly, training the 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Neural Network Modelling and Dynamical Systems in Association Football 

1015 

network model takes time; hence, the practical application of an ANN analysis also remains a key challenge for the future. Nevertheless, in our opinion, ANN models represent more appropriate procedures for sport performance analysis in comparison to conventional statistical tools. 

##### 6. Conclusions 

In this review, we have discussed some of the common attributes of DST that may be present in team sports. Earlier studies have investigated the emerging patterns in team sports by implementing conventional, linear statistical tools. However, these studies have tended to analyse the various sub-units of the dynamical system as isolated entities. Instead, we argue that researchers should aim to evaluate game scenarios in which numerous other variables including contextual constraints (score, time, etc.) and organismic constraints (fatigue, injury, interpersonal distance and angles between the players) are present. Integration of the sub-phases of the game using a more robust and sensitive approach is required to identify to what extent the principles of DST can be identified within team sports. 

Nonlinear ANN models share many promising features that may be suited to processing spatiotemporal data sets, which are typical to team sports. ANN architectures, such as the KFM, can be applied to investigate various realmatch scenarios, such as offensive build ups in open play, counter-attacks or set-plays within a match. Pattern classification by a KFM can cluster similar game processes in a match that are camouflaged in the large number of complex variables. Network-based qualitative analysis allows researchers to investigate the dynamical attributes in a team game, and potentially develop modern training drills to promote self-organizing processes between the players. These advances would help us to better evaluate the traditional training procedures and investigate whether they facilitate creative performance in a team game, such as association football. Given the recent advances in performance analysis,<sup><u>[1]</u></sup> we can conceive that sports scientists in the near future will be required to provide coaches with tactical ad- 

vice that is based on a network modelling of game play. 

##### Acknowledgements 

No sources of funding were used to assist in the preparation of this review. The authors have no conflicts of interest that are directly relevant to the content of this review. The authors would like to thank Gavin Kennedy for his input into the article as part of their research discussion group. 

##### References 

1. <u>Glazier PS. Game, set and match? Substantive issues and future directions in performance analysis. Sports Med 2010; 40 (8): 625-34</u> 

2. <u>Barris S, Button C. A review of vision-based motion analysis in sport. Sports Med 2008; 38 (12): 1025-43</u> 

3. <u>Wilson GE. A framework for teaching tactical game knowledge. J Physical Edu Rec Dance 2002; 73 (1): 20-6</u> 

4. Wallace SA. Dynamic pattern perspective of rhythmic movement: an introduction. In: Zelaznik HN, editor. Advances in motor learning and control. Champaign (IL): Human Kinetics, 1996 

5. <u>Clark JE. On becoming skillful: patterns and constraints. Res Q Exercise Sport 1995; 66: 173-83</u> 

6. Kugler PN. A morphological perspective on the origin and evolution of movement patterns. In: Wade MG, Whiting HTA, editors. Motor development in children: aspects of coordination and control. Dordrecht: Martinus Nijhoff, 1986: 459-525 

7. <u>Cooke NJ, Cannon-Bowers JA, Stout RJ. Measuring team knowledge. Hum Factors 2000; 42: 151-73</u> 

8. <u>Kauffman S. The origins of order: self organization and selection in evolution. New York: Oxford University Press, 1993</u> 

9. <u>Kelso JA. Dynamic patterns: the self-organization of brain and behavior. Cambridge (MA): MIT Press, 1995</u> 

10. <u>Davids K, Button C, Bennett S. Dynamics of skill acquisition: a constraints-led approach. Champaign (IL): Human Kinetics, 2008</u> 

11. Kugler PN, Kelso JAS, Turvey MT. On the control and coordination of naturally developing systems. In: Kelso JAS, Clark E, editors. The development of movement control and coordination. New York: Wiley, 1982 

12. <u>Bernstein N. The coordination and regulation of movement. New York: Pergamon, 1967</u> 

13. Kelso JAS. Contrasting perspectives on order and regulation in movement. In: Long J, Baddeley A, editors. Attention and performance IX. Mahwah (NJ): Lawrence Erlbaum Associates, 1981: 437-57 

14. <u>Iberall AS, Soodak H. Physical basis for complex: some propositions relating levels of organisation. Collective Phenomena 1978; 3: 9-24</u> 

15. Prigogine I, George C, Hennin F, et al. A unified formulation of dynamics and thermodynamics. Chem Scr 1973; 4: 5-32 

16. Davids K, Glazier P, Arau´ jo D, et al. Movement systems as dynamical systems: the functional role of variability and its implications for sports medicine. Sports Med 2003; 3: 245-60 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Dutt-Mazumder et al. 

1016 

17. Davids K, Arau´ jo D, Shuttleworth R. Applications of dynamical systems theory to football. In: Cabri J, Reilly T, Arau´ jo D, editors. Science and football V. London: Routledge, 2005 

18. McGarry T, Anderson DI, Wallace SA, et al. Sport competition as a dynamical self-organizing system. J Sports Sci 2002; 20: 771-81 

19. <u>Bourbousson J, Seve C, McGarry T. Space-time coordination dynamics in basketball: part 2. The interaction between two teams. J Sports Sci 2010b; 28 (3): 349-58</u> 

20. Hristovski R, Davids K, Arau´ jo D, et al. How boxers decide to punch a target: emergent behaviour in nonlinear dynamical movement systems. J Sports Sci Med 2006; 5 (CSSI): 60-73 

21. Passos P, Arau´ jo D, Davids K, et al. Information-governing dynamics of attacker-defender interactions in youth rugby union. J Sports Sci 2008; 26 (13): 1421-9 

22. <u>McGarry T, Franks IM. In search of invariant athletic beha-</u> - 

<u>viour in competitive sport systems: an example from cham pionship squash match-play. J Sports Sci 1996; 14: 445-56</u> 

23. <u>Palut Y, Zanone PG. A dynamical analysis of tennis: concepts and data. J Sports Sci 2005; 23: 1021-32</u> 

24. <u>Beek PJ, Beek WJ. Tools for constructing dynamical models of rhythmic movement. Hum Mov Sci 1988; 7: 301-42</u> 

25. Passos P, Davids K, Arau´ jo K, et al. Networks as novel tool for studying team ball sports as complex social systems. J Sci Med Sport 2011; 14 (2): 170-6 

26. Passos P, Arau´ jo D, Davids K, et al. Interpersonal pattern dynamics and adaptive behaviour in multiagent neurobiological systems: conceptual model and data. J Motor Behav 2009; 41 (5): 445-59 

27. <u>Frencken WGP, Lemmink KAPM. Team kinematics of small-sided soccer games: a systematic approach. In: Reill T, Korkusuz F, editors. Science and football VI: proceedings of the 6th World Congress on Science and Football. London: Routledge, 2008: 161-6</u> 

28. <u>Grehaigne JF, Boutheir D, Bernard D. Dynamic-system analysis of opponent relationships in collective actions of soccer. J Sports Sci 1997; 15: 137-49</u> 

29. Bourbousson J, Seve C, McGarry T. Space-time coordination dynamics in basketball: part 1. Intra- and intercouplings among player dyads. J Sports Sci 2010a; 28 (3): 339-47 

30. <u>McGarry T, Khan MA, Franks IM. On the presence and absence of behavioral traits in sport: an example from championship squash match-play. J Sports Sci 1999; 17: 297-311</u> 

31. <u>McGarry T. Applied and theoretical perspectives of performance analysis in sport: scientific issues and challenges. Int J Perform Anal Sport 2009; 9: 128-40</u> 

32. <u>Lames M. Modelling the interaction in game sports: relative phase and moving correlations. J Sports Sci Med 2006; 5: 556-60</u> 

33. Players Heat Map. 2010 FIFA World Cup South Africa<sup>�</sup> [online]. Available from URL: http://www.fifa.com/search/ index.html?q=heat+map [Accessed 2011 Mar 29] 

34. Stergiou N, Buzzi UH, Kurz MJ, et al. Nonlinear tools in human movement. In: Stergiou N, editor. Innovative analysis of human movement. Champaign (IL): Human Kinetics, 2004: 66-77 

35. <u>Haykin S. Neural networks: a comprehensive foundation. 2nd ed. Upper Saddle River (NJ): Prentice-Hall Inc., 1999</u> 

36. <u>Benuskov’a L, Diamond ME, Ebner FF. Dynamic synaptic modification threshold: computational model of experience dependent plasticity in adult rat barrel cortex. Proc Natl Acad Sci U S A 1994; 91: 4791-5</u> 

37. <u>Maass W. Networks of spiking neurons: the third generation of neural network models. Neural Networks 1997; 10 (9): 1659-71</u> 

38. <u>Kimoto T, Asakawa K, Yoda M, et al. Stock market prediction system with modular neural networks. In: Trippi RR, Turban E, editors. Neural networks in finance and investing. Chicago (IL): Probus Publishing Co., 1994: 343-57</u> 

39. <u>Zhang G, Patuwo BE, Hu MY. Forecasting with artificial neural networks: the state of the art. Int J Forecasting 1998; 14: 35-62</u> 

40. Scho¨ llhorn WI, Nigg BM, Stefanyshyn DJ, et al. Identification of individual walking pattern using time discrete and time continuous data sets. Gait & Posture 2002; 15: 180-6 

41. <u>Mateus J. In pursuit of an ecological and fractal approach to soccer coaching. In: Relly T, Cabri J, Arau jo D, editors. Science and football V. London: Routledge, 2004: 561-73</u> 

42. Scho¨ llhorn WI. Applications of artificial neural nets in clinical biomechanics. Clin Biomechanics 2004; 19: 876-98 

43. <u>Hertz J, Krough A, Palmer RG. Introduction to the theory of neural computation. Redwood City (CA): AddisonWesley, 1991</u> 

44. Silva AJ, Costa AM, Oliviera PM, et al. The use of neural network technology to model swimming performance. J Sports Sci Med 2007; 6: 117-25 

45. <u>Pfeiffer M, Perl J. Analysis of tactical structures in team handball by means of artificial neural networks. Int J Comput Sci Sport 2006; 5 (1): 4-14</u> 

46. <u>Barton G, Lees A, Lisboa P, et al. Visualisation of gait data with Kohonen self-organizing neural maps. Gait & Posture 2006; 24: 46-53</u> 

47. <u>Lamb PF. The use of self-organizing maps in analyzing multi-dimensional human movement coordination [PhD thesis]. Dunedin: University of Otago, 2010</u> 

48. Perl J. Modeling dynamic systems: basic aspects and application to performance analysis. Int J Comput Sci Sport 2004; 3 (2): 19-28 

49. <u>Jaeger H. Short term memory in</u> ‘echo’ <u>state networks. German National Research Institute for Computer Science 2002; GMD-Report No.: 152 [online]. Available from URL: http://www.faculty.iu-bremen.de/hjaeger/pubs/ STMEchoStatesTechRep.pdf [Accessed 2011 Sep 20]</u> 

50. <u>Williams RJ, Zipser D. (University of California, Institute for Cognitive Science, San Diego). A learning algorithm for continually running fully recurrent neural networks: final report [report no. 8805]. San Diego (CA): Institute of Cognitive Science, University of California, San Diego, 1988</u> 

51. <u>Konen W, Maurer T, von der Malsburg C. A fast dynamic link matching algorithm for invariant pattern recognition. Neural Networks 1994; 7: 1019-30</u> 

52. <u>Kohonen T. Self-organizing maps. New York: Springer, 1997</u> 

53. <u>Perl J, Dauscher P. Dynamic pattern recognition in sport by means of artificial neural networks. In: Begg R,</u> 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 

Neural Network Modelling and Dynamical Systems in Association Football 

1017 

Palaniswami M, editors. Computational intelligence for movement science. Hershey (PA): Idea Group Publishing, 2006: 299-318 

54. <u>Lippmann RP. An introduction to computing with neural nets. IEEE ASSP Magazine 1987; 4 (3): 4-22 [online]. Available from URL: http://hawk.cs.csuci.edu/William.</u> Wolfe/UCD/engineering/cse/Graduate/courses/CSC5542/ Lippmann.pdf [Accessed 2011 Sep 21] 

55. Leondes CT. Algorithm and architectures. San Diego (CA): Academic Press, 1998 

56. <u>Perl J, Weber K. A neural network approach to pattern learning in sport. Int J Comput Sci Sport 2004; 3: 67-70</u> 

57. <u>Hughes M. Notational analysis: a mathematical perspective. Int J Perform Anal Sport 2004; 4: 97-139</u> 

58. <u>Perl J. Game analysis and control by means of continuously learning networks. Int J Perform Anal Sport 2002; 2: 21-35</u> 

59. <u>Gruen A. Fundamentals of videogrammetry: a review. Hum Movement Sci 1997; 16: 155-87</u> 

60. Passos P, Arau´ jo D, Davids K, et al. Interpersonal dynamics in sport: the role of artificial neural networks and 3-D analysis. Behav Res Meth, 2006; 38 (4): 683-91 

61. <u>Memmert D. Can creativity be improved by an attentionbroadening training program? An exploratory study focusing on team sports. Creativity Res J 2007; 19: 281-92</u> 

62. Fetz EE, Cheney PD, Mewes K, et al. Control of forelimb activity by populations of corticomotoneuronal and rubromotoneuraonal cells. Progr Brain Res 1989; 80: 437-49 

Correspondence: Mr Aviroop Dutt-Mazumder, School of Physical Education, University of Otago, 55 Union Street West, PO Box 56, Dunedin, New Zealand. E-mail: dutav489@student.otago.ac.nz 

ª 2011 Adis Data Information BV. All rights reserved. 

Sports Med 2011; 41 (12) 


