<!-- source: Lan2020_Article_Semi-onlineMulti-peopleTrackin.pdf -->

International Journal of Computer Vision https://doi.org/10.1007/s11263-020-01314-1 



# **Semi-online Multi-people Tracking by Re-identification** 

#### **Long Lan**<sup>**1**</sup> **· Xinchao Wang**<sup>**2**</sup> **· Gang Hua**<sup>**3**</sup> **· Thomas S. Huang**<sup>**4**</sup> **· Dacheng Tao**<sup>**5**</sup> 

Received: 8 August 2018 / Accepted: 20 February 2020 © Springer Science+Business Media, LLC, part of Springer Nature 2020 

#### **Abstract** 

In this paper, we propose a novel semi-online approach to tracking multiple people. In contrast to conventional offline approaches that take the whole image sequence as input, our semi-online approach tracks people in a frame-by-frame manner by exploring the time, space and multi-camera relationship of detection hypotheses in the near future frames. We cast the multi-people tracking task as a re-identification problem, and explicitly account for objects’ appearance changes and longerterm associations. We model our approach using a Multi-Label Markov Random Field, and introduce a fast _α_ -expansion algorithm to solve it efficiently. To our best knowledge, this is the first semi-online approach achieved by re-identification. It yields very promising tracking results especially in challenging cases, such as scenarios of the crowded streets where pedestrians frequently occlude each other, scenes captured with moving cameras where objects may disappear and reappear randomly, and videos under changing illuminations wherein the appearances of objects are influenced. 

**Keywords** Multi-object tracking · Semi-online methods · Combinatory optimization · Deep learning 

## **1 Introduction** 

Communicated by Larry Davis. B Xinchao Wang xinchao.wang@stevens.edu Long Lan long.lan@nudt.edu.cn Gang Hua ganghua@gmail.com Thomas S. Huang t-huang1@illinois.edu Dacheng Tao dacheng.tao@sydney.edu.au 

- 1 Institute for Quantum Information and State Key Laboratory of High Performance Computing, College of Computer, National University of Defense Technology, Changsha 410073, China 

- 2 Department of Computer Science, Stevens Institute of Technology, Hoboken, NJ, USA 

- 3 Wormpex AI Research, Bellevue, WA, USA 

- 4 Image Formation and Processing Group (IFP), Beckman Institute, University of Illinois Urbana-Champaign (UIUC), Urbana, IL, USA 

- 5 UBTECH Sydney Artificial Intelligence Centre and the School of Computer Science, in the Faculty of Engineering, The University of Sydney, 6 Cleveland St, Darlington, NSW 2008, Australia 

Multipleobjecttracking(MOT)isafundamentaltaskincomputer vision. Its goal is to locate objects of interest in image sequences and meanwhile preserve the objects’ identities. In spite of the recent progress, MOT remains to be a very challenging task because of many factors such as mutual occlusions among the targets and changes of targets’ appearances due to the varying illumination. 

The early approaches of MOT rely on Bayesian filtering that runs in an online manner, meaning that the trackers have access to only the current and the previous frames (Fortmann et al. 1983; Hong-Yoon et al. 2016; Hamid-Rezatofighi et al. 2015; Lan et al. 2016; Bae and Yoon 2014; Shu et al. 2012). These approaches are therefore suitable for real-time applications.However,duetotheirrecursivenature,theyareproneto drifts that are very difficult to correct. To alleviate this problem,offlineapproachesthatworkonimagebatcheshavebeen proposed. By optimizing an objective function that accounts for physical constraints and detection hypotheses in a batch of frames, usually the whole sequence, such approaches tend to achieve more robust results (Milan et al. 2016; Dehghan et al. 2015; Wen et al. 2016; Yang and Nevatia 2012). This however comes at the cost of losing the real-time tracking capability and resulting in a computationally intensive model to solve. 



123 

International Journal of Computer Vision 



**Fig. 1** Examples of semi-online multi-people tracking on PETS09S2.L1 (Camera 1). The trajectories on the ground refer to recovered pedestrian tracks, while the silhouettes with dash line refer to the detection hypotheses from the future. Tracks and detections of the same color correspond to the same target. _di,_ 1 denotes the ground-truth detection in the _i_ -th frame, which is missed by the detector, and _di_ +1 _,_ 1 denotes the detection in the _i_ + 1-th frame. Since the track _T_ 1 can be successfully re-identified to _di_ +1 _,_ 1 in the near future _i_ + 1-th frame, we thus allow _T_ 1 to match no detection in the current _i_ -th frame rather than to match the distractor _di,_ 2 

To combine the merits of both online and offline methods, semi-online MOT approaches have been proposed in the recent years Choi (2015), Lenz et al. (2015), Wang et al. (2017). Such approaches run in a delayed online manner. More specifically, to obtain the tracking results at the current frame, they delay for a short period of time and collect a small batch of future frames, and then conduct data association by optimizing an objective function defined on these future frames.We show an example of semi-online tracking in Fig. 1, where the silhouettes with dash line refer to the detection hypotheses from the future, and the trajectories on the ground correspond to recovered tracks at the current frame. 

Existing semi-online approaches like (Lenz et al. 2015) focus on designing memory-bounded shortest-path algorithms to reduce the computational costs of the tracker. Other approaches, such as (Choi 2015), focus on designing local motion features for computing affinities between detection hypotheses. Even though these algorithms have achieved promising results in the recent MOT challenges (https:// motchallenge.net/results/MOT16/), they are still prone to errors in challenging cases, where people occlude each other for long or where the illumination changes so that the targets’ appearances change. This is because existing semi-online methods do not have a mechanism to explicitly associate detections under varying conditions, such as the changes of illuminances and viewpoints that are common for in-the-wild data. 

In this paper, we propose a novel semi-online approach for tracking multiple people that explicitly accounts for data association under varying conditions. Unlike prior 



**Fig. 2** Multi-people tracking results under different illumination. (a) All the compared methods including ours and the state-of-the-art ones (Levinkov et al. 2017; Tang et al. 2016; Kim et al. 2015; Milan et al. 2014), produce the same result in Frame 80. (b) Our result in Frame 160. (c) Result of Levinkov et al. (2017), Tang et al. (2016), Kim et al. (2015), Milan et al. (2014) in Frame 160. Our method successfully tracks Pedestrian 1 and 2 in different lighting conditions, thanks to the fact that we cast the tracking problem as a re-identification one. The approaches of Levinkov et al. (2017), Tang et al. (2016), Kim et al. (2015), Milan et al. (2014), however, fail to track the pedestrians with changing appearances and initialize two new trackers for these two pedestrians who existed the scene 

approaches, we cast the multi-people tracking problem as a re-identification one, whose goal is to re-identify detection hypotheses to existing trajectories. Our method explores the space, time and multi-view constraints of hypotheses in the near future, and incorporates motion and state-of-the-art reidentification features into tracking. We model our method as a Multi-Label Markov Random Field (MLMRF), where each target is assigned a unique label. To solve the optimization of MLMRF, we propose an improved _α_ -expansion approximation that yields a significant speedup. As such, our method is able to track pedestrians with different appearances due to illumination changes as shown in Fig. 2, while the state-ofthe-art methods like (Levinkov et al. 2017; Tang et al. 2016; Kim et al. 2015; Milan et al. 2014), in this case, fail to do so and initialize two new tracks for the two pedestrians with significant appearance change. 

Our contribution is therefore, to our best knowledge, the first semi-online approach that tracks multiple people by reidentification, achieved by MLMRF. Our tracker is robust to occlusions and illumination changes, and yields superior tracking results compared to the state-of-the-art. By the time we submit this manuscript, the MOTA score achieved by our method is the highest among all the online and semi-online trackers, and is among the top four of all trackers on the MOT17 challenge. 

Even though MRF has been applied in prior multi-people tracking methods like (Milan et al. 2016), they focus on offline settings. When applied in the online mode, these methods often require successive sliding windows with temporal overlaps and then rely on a suboptimal stitching strategy to merge consistent trajectories between adjacent windows (Berclaz et al. 2011; Shitrit et al. 2014). Our method, in contrast to these existing ones, explicitly focuses 

123 

International Journal of Computer Vision 

on the semi-online setting and is therefore suitable for realtime applications such as video surveillance. 

## **2 Related Works** 

In this section, we review the prior work related to ours. We first discuss tracking approaches of three schemes: online approaches, offline approaches and semi-online ones. We then look at appearance models and re-identification in tracking. Finally, we review the MRF-based approaches, as our method is modeled as an MLMRF. 

### **2.1 Three Tracking Schemes** 

We review the online, offline and semi-online approaches in the following subsections. 

#### **2.1.1 Online Approaches** 

Online MOT approaches aggregate image evidences from the current and the past frames to track the targets. The early approaches in this category mainly rely Bayesian filtering such as Kalman filtering and particle filtering (Breitenstein et al. 2011; Benfold and Reid 2011; Liwicki et al. 2015; Yang et al. 2007; Liwicki et al. 2012), which are later proven to be error-prone when applied in complex real-world scenes (Possegger et al. 2014; Shu et al. 2012; Yoon et al. 2015; Bae and Yoon 2017, 2014; Chen et al. 2014; Dehghan et al. 2015; Pang et al. 2015; Collins et al. 2005; Galoogahi ey al. 2017). Joint probabilistic data association (JPDA) (Fortmann et al. 1983) is another classical online MOT method. However, its very high computational complexity makes it very difficult to be applied to crowded scenes directly. Recently, Hamid-Rezatofighi et al. (2015) revisited JPDA as a trackingby-detection approach and considered data association as an integer linear program which is then approximated by the fast _m_ -best solutions. Xiang et al. (2015) formulated the online MOT data association as a decision-making problem. The carefully designed Markov Decision Process learns the state transition policy frame by frame. Hong-Yoon et al. (2016) exploited the spatial relations between targets and proposed the Relative Motion Network to improve the position prediction for targets in the future frames. Chu and Ling (2019) recently presented an end to end neural network, named FAMNet, to jointly learn the feature, affinity and data association for online multi-object tracking. 

As online methods only consider information from the current and the past frames, they tend to make locally optimal decision rather than globally optimal ones, leading to lowerranked results compared to the offline and semi-online ones, as shown in the recent MOT challenge (https://motchallenge. net/results/MOT16/). 

#### **2.1.2 Offline Approaches** 

Offline MOT methods rely on applying data association on all the detection candidates, and thus often leads to better tracking results (Wang et al. 2016; Tang et al. 2015; Sullivan and Carlsson 2006; Nillius et al. 2006; Maksai et al. 2017; Wang et al. 2014). In fact, data association finds its application in many tasks other than tracking, such as lower-level vision tasks including matching (Qiu et al. 2020), indexing (Wang et al. 2011), and image rectification (Yin et al. 2018), as well as higher-level ones including human pose estimation (Wang et al. 2019), segmentation (Ye et al. 2019), and 3D vision (Qiu et al. 2019), and even learning tasks including knowledge distillation (Song et al. 2019; Shen et al. 2019) and network compression (Yu et al. 2017). However, data association comes at the cost of a huge state space of variables. To reduce the computational complexity, methods such as (Dehghan et al. 2015; Milan et al. 2016; Wen et al. 2016; Yang and Nevatia 2012; Brendel et al. 2011; Chan et al. 2008) conduct data association based on tracklets that consist of highly correlated hypotheses. Methods such as (Pirsiavash et al. 2011; Wang et al. 2014; Turetken et al. 2017; Zhang et al. 2008; Wu et al. 2012; Butt and Collins 2013; Chari et al. 2015; Wu and Betke 2016; Lenz et al. 2015; Wang et al. 2009), on the other hand, simplify spatial-temporal relations between consecutive neighbors and optimize data association over a global flow network. Recently, some methods are proposed to model the higher-order motions (Maksai et al. 2016; Arora and Globerson 2013; Liu et al. 2013) of the targets to facilitate the data association. Tang et al. (2015) modeled the tracklet-based data association as a Minimum Cost Subgraph Multicut Problem, and Dehghan et al. (2015) modeled it as a Maximum Multi Clique one. Wen et al. (2016) considered data association using hypergraphs, and Butt and Collins (2013) introduced Lagrangian Relaxation to incorporate higher-order track smoothness in their data association network. Lan et al. (2018) explored both the close and distant interacting tracklets in multi-object tracking, to help distinct the closely positioned tracklets from different objects and associate the distant tracklets from the same objects. Jerripothula et al. (2016) introduced an unsupervised approach for discovering and tracking objects of interest in a collection of videos. 

However, the offline methods, despite their state-of-theart performance, focus on tracking using the whole sequence and is therefore not suitable for real-time applications. 

#### **2.1.3 Semi-online Approaches** 

Recently, semi-online approaches have been proposed in the aim to integrate the advantages of both offline and online methods. Intuitively, hypotheses that are temporally far apart are usually less informative due to the targets’ unpredictable 

123 

International Journal of Computer Vision 

motion. Therefore, approaches that utilize a batch of future frames like (Choi 2015; Kim et al. 2015; Lenz et al. 2015; Fagot-Bouquet et al. 2016), yield very promising results in terms of both tracking accuracy and speed. More specifically, Kim et al. (2015) delayed making data association decisions if there are ambiguities. Choi (2015) used a small batch of frames in the near future to help the data association in the current frame, and Lenz et al. (2015) proposed a memory and computational efficient min-cost flow network by considering hypotheses within a small batch frames. None of existing semi-online approaches, to our best knowledge, focuses on robust data association in varying conditions. 

Our approach, on the other hand, explicitly focuses on tracking by re-identification, and is therefore suitable for crowded scenes where targets frequently occlude one another, and for varying conditions such as the changing of illumination and viewpoint. 

### **2.2 Appearance and Re-identification** 

Appearance modeling is crucial for multi-object tracking. Many prior work focus on developing discriminant appearance models (Shu et al. 2012; Kuo et al. 2010; Bae and Yoon 2014; Hu et al. 2012; Kim et al. 2015; Yu et al. 2016; Zhai et al. 2016; Ramanan et al. 2006; Fan et al. 2013; Liang et al. 2015; Fan et al. 2012; Fu et al. 2019). Among them, Bae and Yoon (2014) proposed the incremental linear discriminant analysis approach (IDLA) to distinguish targets with similar appearances. Hu et al. (2012) proposed a Riemannian subspace learning algorithm to model the appearance. Kim et al. (2015) adopted CNN features to obtain robust appearance representation. These methods, however, are prone to errors when applied in the real-world multi-object tracking scenarios where the illumination or view-port changes dramatically (https://motchallenge.net/results/MOT16/). 

To alleviate this problem, re-identification techniques (Liao et al. 2015; Geng et al. 2016; Cheng et al. 2016; Zheng et al. 2016a, b; Yu et al. 2016; Su et al. 2016; Wang et al. 2016) are proposed. They explicitly focus on recognizing the same object of varying appearances. For example, Kuo and Nevatia (2011) introduced person re-identification features to improve the appearance modeling. In their work, to incorporate re-identification into tracking, they collect the tracklet-based person pairs to learn a discriminant metric. Fleuret et al. (2014) conducted the multi-person tracking using simple features such as color histograms. Leal-Taixé et al. (2016) introduced a siamese CNN architecture to explore the local spatio-temporal features. Tang et al. (2016) used the deep matching (Weinzaepfel et al. 2013) to study the potential optical flows between hypotheses. Ristani and Tomasi (2018) proposed to learn the discriminative features for both the multi-camera tracking and re-identification. Bergmann et al. (2019) emphasized the importance of re- 

identification techniques for the multi-object tracking and attempted to strip the bells and whistles from multi-object tracking. Kim et al. (2018) explored the neural gating using the Bilinear LSTM to learn the long-term appearance modeling. McLaughlin et al. (2016) studied the video based re-identification using the recurrent convolutional network, different from the previous re-identification strategy, they focused on the sequence to sequence re-identification. Tang et al. (2017) introduce the StackNetPose based VGG16 to explore the re-identification in multi-object tracking, in their works, the pose information is incorporated in their model and great help the re-identification. 

Our approach, in contrast to the aforementioned reidentification ones, focuses on the semi-online scenario. We collect the detection hypotheses in the near future frames, and optimize an objective defined over existing trajectories and these detections. Our multi-object tracking appearance modeling is similar to Sadeghian et al. (2017), which adopted the recurrent neural networks (RNN) to extract features of trackers and proposed the sequence-to-single re-identification. However, inspired by several recent video basedre-identificationworks(McLaughlinetal. 2016;Zhang et al. 2017; Zheng et al. 2016b; Chen et al. 2018), we find that the RNN weaken the appearance effect of earlier steps and use only the output of the last time step fade the reidentification performance. The recent work (Maksai and Fua 2019) pointed the potential defeats of metric mismatch and exposure bias when training recurrent neural networks in multi-object tracking. To be different, we incorporate a mean pooling layer for all our RNN units to summarize the relevant information over a full sequence. Furthermore, we utilize the state-of-the-art people re-identification features, discriminant local maximal occurrence (LOMO) (Liao et al. 2015), to model the appearance of pedestrians. This feature has been proven robust to illumination changes, partial occlusions and long-term disappearances of the targets (Liao et al. 2015, https://motchallenge.net/results/MOT16/, Janai et al. 2017). We combine LSTM with the appealing LOMO to build a more discriminative appearance model. The experiments on both the MOT evaluation metrics and person re-identification metric show that this combination achieves very promising performances. 

### **2.3 MRF-Based Tracking** 

In recent years, Markov Radom Field (MRF) has been introduced to multi-object tracking and has led to promising results. Milan et al. (2016) attempt to introduce an all-encompassing MRF to simultaneously handle the detection based and tracklet-based label assignment problem, which results in a very complex optimization process. Yang and Nevatia (2012) proposed to apply Conditional Random Field (Lafferty et al. 2001) to explore interactions between 

123 

International Journal of Computer Vision 

**Table 1** Notations 

|_C_|The total number of cameras|
|---|---|
|_I _<sup>_c_</sup><br>_t_|The input frame at the time_t_ from camera_c_|
|_h_<sup>_c_</sup><br>_t,k_|A detection hypothesis at time_t_ from camera_c_|
|_H_<sup>_c_</sup><br>_t_ <sup>= {</sup><sup>_hc_</sup><br>_t,_1<sup>_, hc_</sup><br>_t,_2<sup>_, . . . , hc_</sup><br>_t,m_<sup>_c_</sup><br>_t_ <sup>}</sup>|The set of detection hypotheses in _I _<sup>_c_</sup><br>_t_ <sup>.</sup><sup>_mc_</sup><br>_t_ <sup>is the total</sup><br>number of hypotheses in the frame|
|_Ht_ =_H_<sup>1</sup><br>_t_ <sup>∪</sup><sup>_H_2</sup><br>_t_ <sup>∪· · · ∪</sup><sup>_HC_</sup><br>_t_|The set of all detection hypotheses from all cameras<br>at time_t_|
|T<sup>_c_</sup><br>_t,i_|The_i_-th active trajectory in camera_c_and at time_t_|
|_T _<sup>_t_</sup><br>_i_ <sup>= {T1</sup><br>_t,i_<sup>_,_ T2</sup><br>_t,i_<sup>_, . . . ,_ T</sup><sup>_C_</sup><br>_t,i_<sup>}</sup>|The_i_-th active target at time_t_. Here, we<br>defne an active target to be the set of its<br>active trajectories in all camera views|
|_T _<sup>_t_ </sup>= {_T _<sup>_t_</sup><br>_i _<sup>_, T t_</sup><br>_j _<sup>_, . . . , T t_</sup><br>_n_ <sup>}</sup>|The set of all active targets at time_t_|
|V<sup>_c_</sup><br>_t,i_|The velocity of target_T _<sup>_t_</sup><br>_i_ <sup>in camera</sup><sup>_c_</sup>|
|_H_=_Ht_ ∪_Ht_+1∪· · · ∪_Ht_+_τ_|The set of all hypotheses from all cameras from_t_ to_t_ +_τ_|
|_L_= _Le_∪_Lo_∪_L f_|The label set for all hypotheses. Each hypothesis is<br>assigned one label. The subset _Le_ consists of labels of<br>existing targets, _Lo_ consists of labels of new coming<br>targets, and _L f_ has the only one label which<br>corresponds to the false positive|
|_l_<sup>_c_</sup><br>_t_<sup>′</sup>_,k_|The label of the hypothesis_h_<sup>_c_</sup><br>_t_<sup>′</sup>_,k_|
|_VS(l_<sup>_c_′</sup><br>_t_<sup>′</sup>_,i_<sup>_,lc_′′</sup><br>_t_<sup>′′</sup>_, j_<sup>_), VT (lc_′</sup><br>_t_<sup>′</sup>_,i_<sup>_,lc_′′</sup><br>_t_<sup>′′</sup>_, j_<sup>_), VV (lc_′</sup><br>_t_<sup>′</sup>_,i_<sup>_,lc_′′</sup><br>_t_<sup>′′</sup>_, j_<sup>_)_</sup>|The space, time and view constraints considered for<br>the hypothesis pair_h_<sup>_c_′</sup><br>_t_<sup>′</sup>_,i_ <sup>and</sup><sup>_hc_′′</sup><br>_t_<sup>′′</sup>_, j_|



tracklets which fail in many complex scenes as robust tracklets are hard to obtain. The approaches of Milan et al. (2015), Tsai et al. (2012), Keuper et al. (2016), on the other hand, propose to conduct tracking and segmentation jointly using MRF. Specifically, Tsai et al. (2012) focused on single-target trackingandpixel-level segmentation. Milanet al. (2015) and Keuper et al. (2016) analyzed the potential links between pixels or super-pixels and detection hypotheses to assist tracking. 

Existing MRF-based multi-object tracking models focus on offline settings. Our approach, however, works in a semionline manner by looking at detection hypotheses in the near future frames. Specifically, we proposed an MRF for every frame, and focused each MRF on more important cues, such as the appearance, quantity and interaction of objects. Furthermore, by explicitly introducing re-identification into data association, our model achieves the state-of-the-art result, superior to all except only one offline approaches in the MOT17 challenge. 

## **3 Model** 

In this section, we describe our Multi-Label MRF (MLMRF) for tracking multiple people by re-identification. We start by introducing the proposed MLMRF, which comprises three components: unary term, pairwise term, and label cost term. The unary term accounts for the targets’ appearance and 

motion, while the pairwise term accounts for the spatial, time and view constraints. The label cost term, on the other hand, encourages re-identification of the targets by penalizing the total number of labels. We then provide details for each term in the following subsections. Our notations are summarized in Table 1, and the overall work flow is depicted in Fig. 3. 

### **3.1 Multi-Label MRF (MLMRF)** 

We assume that we are given detection hypotheses in each frame, and our goal is to associate them into trajectories. Let _h_<sup>_c_</sup> _t,k_<sup>denote the</sup><sup>_k_-th hypothesis obtained from the frame</sup> _It_<sup>_c_,where</sup><sup>_c_and</sup><sup>_t_arethecameraIDandtimerespectively.</sup> We use _Ht_<sup>_c_={</sup><sup>_hc_</sup> _t,_ 1<sup>_, hc_</sup> _t,_ 2<sup>_, . . . , hc_</sup> _t,m_<sup>_c_</sup> _t_<sup>} to denote the set of all</sup> detection hypotheses in camera _c_ at time _t_ , where _m_<sup>_c_</sup> _t_<sup>denotes</sup> the total number of such hypotheses. Let T<sup>_c_</sup> _t,i_<sup>={</sup><sup>_hc_</sup> _t_<sup>′</sup> _,k_<sup>|1≤</sup> the _t_<sup>′</sup> ≤ _active trajectoryt_ − 1 _, h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>∈</sup><sup>_H_</sup> of the _t_<sup>_c_′</sup><sup>_,_∃</sup><sup>_h_</sup> _i_<sup>_c_</sup> _t_<sup>′′</sup> -th target in camera _,k_<sup>_, t_−</sup><sup>_π_≤</sup><sup>_t_′′≤</sup><sup>_t_</sup> _c_<sup>−</sup> and at time<sup>1} denote</sup> _t_ . In other words, an active trajectory T<sup>_c_</sup> _t,i_<sup>comprises at least</sup> to claim no detection hypothesis at a specific frame, to modelone detection in the past _π_ frames. Note that, we allow T<sup>_c_</sup> _t,i_ the targets’ leaving and re-entering the scene, or the missed detections caused by occlusions and detection failures. Also, let _Ti_<sup>_t_= {T1</sup> _t,i_<sup>_, . . . ,_T</sup><sup>_C_</sup> _t,i_<sup>} denote the</sup><sup>_i_-th active target, or the</sup> set of all trajectories of active target _i_ in all camera views at time _t_ . Furthermore, let _T_<sup>_t_</sup> = [ _T_ 1<sup>_t, T_</sup> 2<sup>_t, . . . , T_</sup> _n_<sup>_t_]denotethe</sup> set of all active targets at time _t_ . 

123 

International Journal of Computer Vision 



**Fig. 3** Workflow of our semi-online approach. At time _t_ , we have two types of data as input, the trajectories obtained using previous frames and the raw detections from the future frames. The identities of the trajectories are color-encoded, and the raw detections are shown in black. In the multi-camera setting, we map all the trajectories and detections 

to the ground plane. We then cast the multi-object tracking problem as a re-identification one, and model it using a Multi-Label MRF (MLMRF). Each detection may be assigned a label of the existing trajectories, a new label or a false positive shown as a black bounding box in the output 

Let _Ht_ = _Ht_<sup>1∪· · ·∪</sup><sup>_H_</sup> _t_<sup>_C_denote the detection hypotheses</sup> from all camera views at time _t_ and let _H_ = _Ht_ ∪· · ·∪ _Ht_ + _τ_ denote all detection hypotheses from all camera views at frames [ _t, t_ + _τ_ ],where _τ_ isthenumberofthedelayedframes. At each time _t_ , the goal is to associate a detection hypothesis _h_<sup>_c_</sup> _t,k_<sup>∈</sup><sup>_H_withalabel.Weformulatethisdataassociation</sup> problem as an MLMRF. Let _L(Ti_<sup>_t)_∈Z+bethelabelof</sup> of the detectiontarget _Ti_<sup>_t_, and</sup><sup>_l_</sup> _t_<sup>_c_</sup> _h_<sup>′</sup> _,k_<sup>_c_</sup> _t_<sup>′</sup> _,_<sup>be the random variable denoting the label</sup> _k_<sup>.</sup><sup>_l_</sup> _t_<sup>_c_′</sup> _,k_<sup>may take one of the following val-</sup> ues: 

- one label in the set _L e_ , where _L e_ = { _L(T_ 1<sup>_t), . . . , L(T_</sup> _n_<sup>_t)_},</sup> denoting _h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>is associated with a existing active target;</sup> 

- – one label in the set of new labels _L o_ ⊂ Z<sup>+</sup> , where _L o_ ∩ and a new target is initialized; _L e_ = ∅,denoting _h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>isnotlinkedtoanyexistingtargets</sup> 

- – _L f_ = 0, denoting _h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>is treated as a false positive.</sup> 

Also, we denote _L_ = _L e_ ∪ _L o_ ∪ _L f_ . Figure 4 shows an example of the different types of labels. 

_h_<sup>_c_</sup> _t_<sup>′</sup> _,_ Intuitively, _k_<sup>is associated with an existing target, and assigning</sup> assigning _h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>alabel</sup><sup>_l_</sup> _t_<sup>_c_′</sup> _,k_<sup>∈</sup><sup>_Le_means</sup><sup>_l_</sup> _t_<sup>_c_′</sup> _,_<sup>that</sup> _k_<sup>∈</sup> _L o_ means that we find strong evidences where a number of hypotheses are likely to form a new target. Otherwise, _h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>is</sup> treated as a false positive and assigned the label _L f_ . Notably, a false positivea hypothesis _h_<sup>_c_</sup> _t_<sup>′</sup> at the current _,k_<sup>∈</sup><sup>_H, t_′=</sup><sup>_t_</sup> frame can<sup>thatisincorrectly</sup> be corrected<sup>treated</sup> in the<sup>as</sup> future, as the processing window slides forward only one frame each time. 





**Fig. 4** Each hypothesis in the temporal window [ _t, t_ + _τ_ ] may be assigned one of the three types of labels, one of the existing targets _L e_ , a new target _L o_ , or a false positive _L f_ 

The objective function of our MLMRF at time _t_ is formulated as 



where **l** = { _lt_<sup>1</sup> _,_ 1<sup>_,l_</sup> _t_<sup>1</sup> _,_ 2<sup>_, . . . ,l_</sup> _t_<sup>_c_′′</sup> _,k_<sup>_, . . . ,l_</sup> _t_<sup>_C_</sup> + _τ,m_<sup>_C_</sup> _t_ + _τ_<sup>}isthesetof</sup> labels we seek, _c_<sup>′</sup> _, c_<sup>′′</sup> ∈[1 _, C_ ], _t_<sup>′</sup> _, t_<sup>′′</sup> ∈[ _t, t_ + _τ_ ], and _k, j_ are the indexes of the hypotheses. _N_ denotes the set of hypothesesintheneighborhood. _U_ istheunarytermthatmeasuresthe distance between hypotheses and targets, and _V_ is the pairwise term that accounts for the spatial, temporal and view 

123 

International Journal of Computer Vision 



**Fig. 5** Illustration of our proposed MLMRF. The MLMRF explores the view, spatial and temporal consistencies across frames, and models the data association problem as a re-identification one. Furthermore, the label cost term, which accounts for the total number of labels, encourages a detection to be re-identified as an existing target 

constraints between the hypotheses. The third term _δl_ penalizes the number of assigned labels to avoid the number of targets becoming arbitrarily large. _λ_ is the label cost parameter. Figure 5 shows a schematic illustration of the proposed MLMRF. In the following subsections, we give details for each of the terms. 

### **3.2 Unary Term** 

In the unary term, we account for appearance and motion, the two most important clues for data association. We build our appearance model using a state-of-the-art person reidentification feature, LOMO (Liao et al. 2015), and build our motion model using the Kalman filter. 

Theunaryterm _U (lt_<sup>_c_′</sup> _,k_<sup>_)_where</sup><sup>_t_′∈[</sup><sup>_t, t_+</sup><sup>_τ_] and</sup><sup>_c_∈[1</sup><sup>_, C_]</sup> 



where _A_ accounts for the appearance-based distance, _M_ accounts for the motion-based distance, _Λ_ is an additional term that encourages re-identification, 1 is the indicator varidetectionable, and scores _st_<sup>_c_′</sup> _,k_<sup>is</sup> of<sup>the</sup> false<sup>detection</sup> positives<sup>score</sup> are<sup>of</sup> inconsistent<sup>_hc_</sup> _t_<sup>′</sup> _,k_<sup>.Because</sup> on dif-<sup>the</sup> ferent video sequences even using the same detector, we introduce _ε_ to trade off the tracking performance. Note that, the third term is turned on only when _t_ = _t_<sup>′</sup> , or equivalently, three terms.when _h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>∈</sup><sup>_Ht_. In what follows, we give details for all the</sup> 



**Fig. 6** The illustration of our appearance re-identification framework 

#### **3.2.1 Appearance** 

We introduce re-identification technique in our appearance modeling of multi-object tracking. Re-identification in our multi-object tracking explore the sequence-to-single matching. Different the popular single-to-single strategy, we utilize the previous but informative appearance of tracker for reidentification. As it is hard to collect reliable sequence for a specific tracker from the future, we can not apply the sequence to sequence re-identification strategy straightforward. The flow of our sequence-to-single re-identification is showed in Fig. 6. 

We utilize the discriminative person re-identification feature LOMO (Liao et al. 2015) to model the appearance. The LOMOdescriptorprovidesaconceptuallysimpleandconsistent way to generate discriminative and robust features that describe color and textural information simultaneously. To use LOMO in our case, we resize each detection hypothesis to a bounding box of size 128 × 48. The LOMO feature of each such hypothesis has a high dimensionality _d_ = 26 _,_ 960. To reduce the computational cost and meanwhile retain the re-identification performance, we apply PCA to learn a lowdimensional representation to 256 dimensions. For the re-id feature, we use both the LOMO feature and size information as256 for the appearance while 2 for the size, width and hightthetheinputinput.re-idLetfeature _zt_<sup>_c_′</sup> _,k_<sup>∈</sup> vector<sup>R</sup><sup>_r_where</sup> of the<sup>_r_</sup> hypothesis<sup>=256+2</sup> _h_<sup>_c_</sup> _t_<sup>′denotes</sup> _,k_<sup>.The</sup> respectively. The length of hidden vector in our LSTM unit is set to 258 as well. We add a mean pooling layer to average the output of all LSTM units as we assuming that the previous appearance is great important and will be weaken in the recurrent of LSTM. 

To evaluate the re-identification distance between a target their respective features from the final fully-connected layer _Ti_<sup>_t_∈</sup><sup>_Tt_and a hypothesis</sup><sup>_hc_</sup> _t_<sup>′</sup> _,k_<sup>in the testing, we first obtain</sup> (FC layer) and calculate their cosine distance as 

123 

International Journal of Computer Vision 



(3) 

Note that, here we only measure the distance between active trajectories and detection hypotheses from the same view. Since _A(_ T<sup>_c_</sup> _t,i_<sup>_, hc_</sup> _t_<sup>′</sup> _,k_<sup>_)_measures the cosine distance, the smaller</sup> the _A(Ti_<sup>_t, hc_</sup> _t_<sup>′</sup> _,k_<sup>_)_is,themorelikely</sup><sup>_hc_</sup> _t_<sup>′</sup> _,k_<sup>isassociatedwith</sup> _T_ linear scaling to keep a unified scale. _i_<sup>_t_. We also constrain</sup><sup>_A(T_</sup> _i_<sup>_t, hc_</sup> _t_<sup>′</sup> _,k_<sup>_)_in the range of [−1</sup><sup>_,_1] by</sup> 

#### **3.2.2 Motion** 

We model our motion prediction using Kalman filter. Many offline multi-object tracking methods generate tracklets in their first step, which are usually too short to make a right motion prediction. In contrast, our semi-online approach collects a long trajectory for each target on the fly, and thus is more robust in predicting motions. For each target _Ti_<sup>_t_,we</sup> calculate its 2D velocity, denoted by V _t_<sup>_c_</sup> _,i_<sup>, for the</sup><sup>_c_-th cam-</sup> era view. We use 2D velocities but not the 3D one because we found that the triangulation step brings additional errors. Specifically, we first interpolate and smooth hypotheses and generate a continuous 2D trajectory in each camera view, and then predict the 2D velocity in that view by feeding the generated trajectory into the Kalman filter model. Note that, in the 2D trajectory generation, we interpolate the missing hypotheses using the existing hypotheses of the same target from other views, if any. 

The motion-based distance between the target _Ti_<sup>_t_and</sup><sup>_hc_</sup> _t_<sup>′</sup> _,k_ 



sis in the same view. We measure the motion-based distancewhere _M(_ T<sup>_c_</sup> _t,i_<sup>_, hc_</sup> _t_<sup>′</sup> _,k_<sup>_)_accounts for the target and the hypothe-</sup> between targets and hypotheses using their overlaps. If the predicted position of a target overlaps significantly with a hypothesis, it is very likely that the hypothesis belongs to the the target. Let h<sup>_c_</sup> _t,_<sup>_,_</sup> _i_<sup>_t_′=</sup><sup>_P(_T</sup><sup>_c_</sup> _t,i_<sup>_,_V</sup> _t_<sup>_c_</sup> _,i_<sup>_, t_′</sup><sup>_)_computes the pre-</sup> dicted position of trajectory T<sup>_c_</sup> _t,i_<sup>attime</sup><sup>_t_′usingV</sup> _t_<sup>_c_</sup> _,i_<sup>.We</sup> consider the predicted position h<sup>_c_</sup> _t,_<sup>_,_</sup> _i_<sup>_t_′to be highly overlapped</sup> thresholdwith the _β_ position. We writeof _h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>,iftheoverlapisgreaterthana</sup> 



where _o_ is the ratio between the intersection area and the union the area _(IoU )_ of the predicted hypothesis h<sup>_c_</sup> _t,_<sup>_,_</sup> _i_<sup>_t_′and</sup> _h_<sup>_c_=</sup><sup>_t_′ −</sup><sup>_t_is the time gap.</sup> _t_<sup>′</sup> _,k_<sup>,</sup><sup>_η_is the decay factor, and</sup><sup>_Δt_</sup> Note that, the scale of _M(Ti_<sup>_t, hc_</sup> _t_<sup>′</sup> _,k_<sup>_)_is limited within the range</sup> 

of _(_ −1 _,_ 0]. IoU is a simple and effective method to associate objects of moderate movement. We use this motion account for all the hypotheses in the temporal window [ _t, t_ + _τ_ ]. However,IoUisnotaproperoptionwhenmeasurethemotion of fast moving object or objects in the moving camera, we introduce the section of re-identification in the following to handle more challenging scene and focus only hypotheses in the current frame _t_ 

#### **3.2.3** 

additional penalty for target re-identification, only for detec-The last term in our unary 1 _t_ = _t_ ′ · _Λ(Ti_<sup>_t, hc_</sup> _t_<sup>′</sup> _,k_<sup>_)_imposesan</sup> tion hypotheses at time _t_ . Recall that h<sup>_c_</sup> _t,_<sup>_,_</sup> _i_<sup>_t_′=</sup><sup>_P(_T</sup><sup>_c_</sup> _t,i_<sup>_,_V</sup> _t_<sup>_c_</sup> _,i_<sup>_, t_′</sup><sup>_)_</sup> denotes the predicted location of trajectory T<sup>_c_</sup> _t,i_<sup>attime</sup><sup>_t_′.</sup> If the distance between the h<sup>_c_</sup> _t,_<sup>_,_</sup> _i_<sup>_t_′</sup> and a hypothesis at the same time is small, we encourage our tracker to associate the hypothesis to T<sup>_c_</sup> _t,i_<sup>;ifnot,wepenalizesuchassociation</sup> by a cost. We write 



where _dist(_ · _)_ calculatestheEuclideandistance,and _width(_ · _)_ denotes the width of a target. Specifically, we define _width(_ T<sup>_c_</sup> _t,i_<sup>_)_tobethewidthofthelasthypothesisinT</sup><sup>_c_</sup> _t,i_<sup>.</sup> For longer term occlusions, the motion of a target is hard to predict, especially when the camera is not static. We therefore set a threshold _ϵ_ to allow spatially distant hypotheses that, when the appearance evidences are strong, a target can _h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>to match to a target</sup><sup>_T_</sup> _i_<sup>_t_. We observe in our experiment</sup> indeed be re-identified when reappearing in a distant position after a long-term missing. 

### **3.3 Pairwise Term** 

In our MLMRF, we define three types of pairwise terms, i.e., the space, time and view. The spatial pairwise handles hypotheses in the same frame, the temporal pairwise explores hypotheses between consecutive frames, and the view pairwise identifies the same target across different cameras. We take our pairwise term to be 



where _VS_ and _VT_ respectively account for the spatial and temporal constraints in the same view. _VV_ explores constraints across views at the same time. We provide details of these terms as follows. 

123 

International Journal of Computer Vision 

#### **3.3.1 Spatial Constraints** 

We consider two types of spatial constraints so as to produce physically plausible results. The first type describes the fact that, one hypothesis can be assigned to at most one target. It is explicitly satisfied by our MRF model since we assign each hypothesis a unique label. The second type of constraints enforces that one target cannot simultaneously appear in two different locations at one time instant in the same view. In other words, two hypotheses in the same frame of the same view are not allowed to take the same label. However, in practice, detectors tend to produce more than one hypotheses that are similar in scale and location for one target. We therefore relax this hard constraint to a soft one and allow hypotheses that significantly overlap each other to take the same label. We write the spatial pairwise term as 



Here, _ω_ is the penalty of assigning two highly overlapped hypotheses _h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>and</sup><sup>_hc_</sup> _t_<sup>′</sup> _, j_<sup>to the same target. We only penalize</sup> the case where the hypothesis is assigned to an existing target or a new target. 

#### **3.3.2 Temporal Constraints** 

We explore the temporal consistency between detection hypotheses across frames in the same camera view. If two hypotheses are similar in appearance, it is likely that they belong to the same target and should be assigned the same label. To account for the appearance-based distance between such detection hypotheses, we use _Ad_ again. We define our temporal pairwise term to be 



where we have _t_<sup>′</sup> = _t_<sup>′′</sup> . In practice, to reduce the computational complexity, we only consider hypothesis pairs at most two frames away from each other, i.e., _h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>_, hc_</sup> _t_<sup>′′</sup> _, j_<sup>where</sup> _t_<sup>′</sup> − _t_<sup>′′</sup> ∈{−2 _,_ −1 _,_ 1 _,_ 2}. 

#### **3.3.3 View Constraints** 

To take advantage of the multiple camera views, we explore the inter-view consistency of the detection hypotheses. Intuitively, if two detection hypotheses from two views map to the same 3D location, it is more likely that they correspond to the same target. As we focus on pedestrians, we assume all 

the targets walk on the ground. Therefore, we use the bottom centers of the 2D bounding boxes of the hypotheses to compute the 3D ground-plane locations. For any hypothesis pair _h_<sup>_c_</sup> _t_<sup>′′</sup> _,k_<sup>∈</sup><sup>_I c_</sup> _t_<sup>′′and</sup><sup>_hc_</sup> _t_<sup>′′′</sup> _, j_<sup>∈</sup><sup>_I c_</sup> _t_<sup>′′′, where</sup><sup>_t_′∈[</sup><sup>_t, t_+</sup><sup>_τ_], we compute</sup> their ground-plane location in 3D using the calibration information. Let g<sup>_c_</sup> _t_<sup>′′</sup> _,k_<sup>=</sup><sup>_(_u</sup><sup>_c_</sup> _t_<sup>′′</sup> _,k_<sup>_,_v</sup><sup>_c_</sup> _t_<sup>′′</sup> _,k_<sup>_,_0</sup><sup>_)_denote the 3D locations</sup> of _h_<sup>_c_′</sup> _t_<sup>′</sup> _,k_<sup>. We define the view-based distance between a pair of</sup> hypotheses _h_<sup>_c_</sup> _t_<sup>′′</sup> _,k_<sup>_, hc_</sup> _t_<sup>′′′</sup> _, j_<sup>as</sup> 



where ∥ _gt_<sup>_c_′′</sup> _,k_<sup>−</sup><sup>_g_</sup> _t_<sup>_c_′′′</sup> _, j_<sup>∥2isthedeviationbetweenthetwo</sup> hypotheses in 3D. The smaller the deviation is, the more likely that the hypothesis pair corresponds to the same target in 3D. 

### **3.4 Label Cost Term** 

To penalize the total number of labels assigned to the targets and to avoid it becoming arbitrarily large, we introduce the label cost term. It encourages the re-identification of a hypothesis to an existing track rather than the initialization of a new track. We write the label cost term as 



Intuitively, we penalize a label _l_ as long as there is one hypothesis assigned to it. As a result, hypotheses with strong appearance and motion evidences tend to be re-identified to existing targets, through the temporal and view constraints. 

## **4 Optimization** 

We use the popular _α_ -expansion algorithm (Boykov et al. 2001) to optimize our model. _α_ -expansion transfers the MLMRF into a number of binary problems by iteratively expanding an individual label. To be specific, for each iteration, _α_ -expansion selects a label _α_ from _L_ . Each hypothesis, which does not take the label _α_ , has a binary choice: either to keep its current label or to switch to _α_ . Such switch is called _α_ -expansion, as only the number of _α_ label grows in holdsthe expansion. We usevariable, whereits current _xt_ label<sup>_c_′</sup> _,k_<sup>=</sup> _lx_<sup>0</sup><sup>_c_</sup> _t_<sup>_c_′</sup> _,_<sup>indicates that the hypothesis</sup> _k_<sup>∈{while0</sup><sup>_,_1</sup><sup>_x_} to denote the indicator</sup><sup>_c_1indicates</sup><sup>_hhc_</sup> _t_<sup>_c_′</sup> _,k t_<sup>′</sup> _,k_<sup>,</sup> _t_<sup>′</sup> _,k_<sup>=</sup> _t_<sup>′</sup> _,k_ switches its label to _α_ . 

The binarizations of unary and pairwise terms are straightforward using _xt_<sup>_c_′</sup> _,k_<sup>.Webinarizethelabelcosttermof(11)</sup> as 

123 

International Journal of Computer Vision 



current label **Fig. 7** Illustration _α_ ¯ or change to labelof _α_ -expansion. _α_ . Each hypothesis either keeps the 



wherethe same _Xl_ label= { _xlt_<sup>_c_</sup> .<sup>′</sup> _,_ If _k_<sup>|</sup><sup>_l_</sup> _t_ all<sup>_c_′</sup> _,k_ the<sup>=</sup><sup>_l_</sup> indicators<sup>}istheset</sup> in<sup>of</sup> _Xl_<sup>indicators</sup> take the value<sup>with</sup> of 1, then _δl (_ **l** _)_ = 0, resulting in a small objective of (1). Therefore, (12) encourages all indicators with the same label to simultaneously take 1 or change to label _α_ , in other words, it encourages a smaller number of labels. Figure 7 shows the _α_ -expansion subgraph for all the hypotheses with the samelabel ¯ _α_ .Here,thetradeoffsbetweenthere-identification cost and the label cost determine whether the hypotheses are pushed to _α_ . 

We convert the higher-order term in (12) to a combination of the quadratic and linear terms as done in Delong et al. (2012), as follows 



where _yl_ is the auxiliary binary parameter (Delong et al. 2012). The binarized MRF model, for a fixed label _α_ , can be therefore written as 



whereThe **x** binary<sup>_α_</sup> = { _xt_ energy<sup>_c_′</sup> _,k_<sup>|</sup><sup>_l_</sup> _t_<sup>_c_′</sup> _,k_ function<sup>=</sup><sup>_α_}, and</sup> of<sup>_x_¯</sup> (14<sup>= 1</sup> )<sup>−</sup> includes<sup>_x_.</sup> many nonsubmodular items in the pairwise part which cannot be solved like (Delong et al. 2012). We thus apply the quadratic pseudoBoolean optimization (QPBO) (Boros and Hammer 2002) to this minimization problem. We iteratively optimize the 

energy function of (14) using QPBO to expand different labels.However,foreach _α_ -expansionround,weneedtoconsider all the remaining hypotheses, which heavily burdens the QPBO especially when the number of hypotheses is large. We therefore assume that, each hypothesis can only expand its label to those of its nearby hypotheses. Our assumption is reasonable because a target cannot move to a distant location within a short period of time. In this way, we significantly reduce the size of the QPBO graph and speed up the optimization. We name this approach as _fast α-expansion_ in this paper. 

We provide the details of our fast _α_ -expansion in Algorithm 1.Here, _dist(h_<sup>_c_</sup> _t_<sup>′′′′</sup> _, j_<sup>_,Hα)_computesthedistancebetween</sup> _h_<sup>_c_</sup> _t_<sup>′′′′</sup> _, j_<sup>andallthehypotheses</sup><sup>_hc_</sup> _t_<sup>′′</sup> _,k_<sup>∈</sup><sup>_Hα_.If</sup><sup>_Hα_isempty,</sup> the distance is set to 0. In the case of multi-camera setting, _dist(_ · _,_ · _)_ computes the 3D distance, while in the case of single camera, it computes the 2D image-plane distance. 

#### **Algorithm 1 Fast** _α_ **-expansion** 



Even though our proposed fast _α_ -expansion is a simple extension of _α_ -expansion, it is very effective. In Fig. 8, we show the running time for optimizing the QPBO using our fast and the original _α_ -expansion. In this experiment, we set the maximum number of iterations to three, as our MLMRF function can reach a considerable good local minimum after such a small number of iterations. For each iteration round, we push all the existing labels once and record the computing time. The blue curves in Fig. 8 correspond to the computing time using the original _α_ -expansion setting, where we need to construct a global graph for each _α_ -expansion step. The red curves correspond to the running time using our fast _α_ - expansion. We also report the achieved objectives after each iteration. As can be seen, the objectives are almost the same 

123 

International Journal of Computer Vision 





<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->

**Fig. 8** Running time for optimizing the QPBO on **a** PETS09-S2.L2 and **b** PETS09-S2.L3 using the proposed fast _α_ -expansion and the original _α_ -expansion. Both methods achieve very similar objectives but the fast _α_ -expansion yields a much faster speed 

for the two settings, yet the fast _α_ -expansion significantly speeds up the optimization. 

## **5 Implementation Details** 

In this section, we show the implementation details of our tracker. We first show the parameter settings in our experiments, then introduce the pruning strategies to speed up our tracker, and finally provide details on the labeling initialization. 

### **5.1 Parameter Settings** 

We set _π_ = 50 for all our experiments. Larger _π_ allow for object can be re-identified in more distant future but lead to 

heavier computational cost. Parameter _ε_ relates to the quality of detection hypotheses or the ratio of false positives. It is the only tunable parameter as the detection qualities vary from one another. In our case, we set _ε_ = 0 _._ 5 on the PETS09 dataset and _ε_ = 1 _._ 0 on the MOT17 benchmark. We set the _λ_ = 1, _ϵ_ = 2, _β_ = 0 _._ 5 and _η_ = 0 _._ 98 for all our experiments. 

### **5.2 Pruning Strategies** 

Through our experiments, we found out that computing the affinity is the most time-consuming part of our tracker. We therefore introduce two techniques to speed up the computation. First, we compute the affinities between trajectories and hypotheses in parallel, as these affinities are independent from each other. Second, given a trajectory, we ignore those hypotheses that are far from it. In the single camera case, we set _Ad (_ T<sup>_c_</sup> _t,i_<sup>_, hc_</sup> _t_<sup>′</sup> _,k_<sup>_)_= 0 when</sup><sup>_dist(p(_T</sup> _t_<sup>_c_</sup> _,i_<sup>_), hc_</sup> _t_<sup>′</sup> _,k_<sup>_) >_</sup> 2 ∗ _width(_ T<sup>_c_</sup> _t,i_<sup>_)_;inthemultiplecameracase,wesetset</sup> _Ad (_ T<sup>_c_</sup> _t,i_<sup>_, hc_</sup> _t_<sup>′</sup> _,k_<sup>_)_=0whentheir3Ddistanceislargerthan</sup> two meters. 

### **5.3 Labeling Initializing** 

Our tracker runs in a frame-by-frame manner. At each time _t_ , we initialize the label of a hypothesis _h_<sup>_c_</sup> _t_<sup>′</sup> _,k_<sup>∈</sup><sup>_H_</sup> _t_<sup>_c_′</sup><sup>_, t_≤</sup><sup>_t_′≤</sup> _t_ + _τ_ − 1 using the data association results from the previous frame. For a hypothesis _h_<sup>_c_</sup> _t_ + _τ,k_<sup>∈</sup><sup>_H_</sup> _t_<sup>_c_</sup> + _τ_<sup>, we initialize a new</sup> label to it. 

**Table 2** Re-identification performance with different appearance features and LSTM units 

|LSTM Units|Features|Rank 1|Rank 2|Rank 3|Rank 4|Rank 5|Rank 6|Rank 7|Rank 8|Rank 9|Rank 10|
|---|---|---|---|---|---|---|---|---|---|---|---|
|5|RGB|0.7895|0.8224|0.8421|0.8684|0.8882|0.9013|0.9079|0.9079|0.9211|0.9276|
||LBP|0.8289|0.8553|0.8816|0.9013|0.9013|0.9145|0.9145|0.9145|0.9211|0.9276|
||CNN|0.7566|0.8421|0.875|0.8816|0.8947|0.9013|0.9079|0.9145|0.9145|0.9145|
||LOMO|0.8816|0.9342|0.9474|0.9539|0.9539|0.9539|0.9539|0.9605|0.9605|0.9605|
|10|RGB|0.8487|0.9013|0.9145|0.9276|0.9408|0.9474|0.9539|0.9605|0.9671|0.9737|
||LBP|0.8553|0.9211|0.9342|0.9342|0.9408|0.9474|0.9539|0.9539|0.9605|0.9671|
||CNN|0.8816|0.9474|0.9539|0.9539|0.9539|0.9605|0.9737|0.9737|0.9737|0.9737|
||LOMO|0.9408|0.9671|0.9737|0.9803|0.9803|0.9868|0.9868|0.9868|0.9868|0.9934|
|15|RGB|0.8487|0.8947|0.9145|0.9342|0.9474|0.9474|0.9605|0.9605|0.9605|0.9605|
||LBP|0.8947|0.9342|0.9474|0.9605|0.9605|0.9671|0.9671|0.9737|0.9737|0.9737|
||CNN|0.9079|0.9474|0.9474|0.9605|0.9737|0.9737|0.9803|0.9803|0.9803|0.9803|
||LOMO|0.9803|0.9803|0.9803|0.9803|0.9868|0.9868|0.9868|0.9868|0.9934|0.9934|
|20|RGB|0.9013|0.9079|0.9539|0.9605|0.9671|0.9671|0.9671|0.9671|0.9671|0.9737|
||LBP|0.9145|0.9342|0.9605|0.9737|0.9737|0.9803|0.9868|0.9868|0.9868|0.9868|
||CNN|0.9079|0.9342|0.9605|0.9605|0.9605|0.9671|0.9737|0.9803|0.9803|0.9803|
||LOMO|0.9868|0.9934|0.9934|0.9934|0.9934|0.9934|0.9934|1.0000|1.0000|1.0000|



123 

International Journal of Computer Vision 



**Fig.9** Qualitative tracking results on different sequences of the MOT17 dataset with SDP detections. Pedestrians significantly occlude each other 





<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->

**Fig. 10** Tracking performance for different window sizes on **a** MOT1702 and **b** MOT17-11 with SDP detections 

## **6 Experiment** 

In this section, we first detail the datasets and evaluation metrics we used, and then show our experimental results. We respectively evaluate the effects of four factors in our multiobjecct tacking model, the re-identification, the semi-online model, the quality of detector and the multi-view setting. Our 

code will be made publicly available upon the final version of the manuscript. 

### **6.1 Datasets** 

We have used the two most popular datasets for people tracking, namely the MOT17 challenge dataset (Milan et al. 2016) and the PETS09 dataset [117], and have compared our results with those of the state-of-the-art trackers. We briefly summarize the two datasets as follows: 

- **MOT17 Challenge Dataset:** It comprises fourteen sequences, covering a wide domain of scenarios. The sequences are recorded using different types of cameras, suchassurveillancecameras,handheldones,andvehiclemountedones.Thefourteensequencesisdividedintotwo subsets of seven sequences, one for training and the other for testing. The MOT17 challenge provides three types of detector for each sequences, DPM, FRCNN and SDP to comprehensively evaluate different trackers. Thus, we can obtain 14 x 3 tracking results for the MOT17 challenge dataset. 

- **PETS09 Dataset:** It is a multi-camera dataset that features crowded scenes where pedestrians frequently occlude one another. Some pedestrians are even occluded all the time for the whole sequence. We have run our tracker and compared it with the state-of-the-art ones using single and multiple cameras. To make all the compared methods in the same detections and ground truth, for the single camera tracking, we used the public detections and ground truth provided by Milan et al. (2013). While in the multi-camera tacking case, we used the pub- 

**Table 3** Tracking results on the MOT17 challenge 

|||MOTA↑|IDF1↑|MT↑|ML↓|FP↓|FN↓|IDS↓|FM↓|
|---|---|---|---|---|---|---|---|---|---|
|Methods|Tracktor17 (Bergmann et al.2019)|**53.5**|52.3|19.5|36.6|**12201**|248047|2072|4611|
||JBNOT (Henschel et al.2019)|**52.6**|50.8|19.7|35.8|31572|**232659**|3050|3792|
||**Ours**|52.4|51.0|**22.6**|**34.6**|23660|**242953**|2070|3170|
||FAMNet (Chu and Ling2019)|52.0|48.7|19.1|**33.4**|**14138**|253616|3072|5318|
||FWT (Roberto et al.2017)|51.3|47.6|21.4|35.2|24101|247921|2648|4279|
||jCC (Keuper et al.2016)|51.2|54.5|20.9|37.0|25937|247822|**1802**|2984|
||MOTDT17 (Chen et al.2018)|50.9|52.7|17.5|35.7|24069|250768|2474|5317|
||MHT-DAM (Kim et al.2015)|50.7|47.2|20.8|36.9|22875|252889|2314|**2865**|
||EDMT17 (Chen et al.2017)|50.0|51.3|**21.6**|36.3|32279|247297|2264|3260|
||DMAN (Zhu et al.2018)|48.2|**55.7**|19.3|38.3|26218|263608|2194|5378|
||MHT_bLSTM (Kim et al.2018)|47.5|51.9|18.2|41.7|25981|268042|2069|3124|
||SAS_MOT17 (Maksai and Fua2019)|44.2|**57.2**|16.1|44.3|29473|283611|**1529**|**2644**|
||EAMTT (Sanchez-Matilla et al.2016)|42.6|41.8|12.7|42.7|30771|288474|4488|5720|



Numbers being both bold and underlined indicate the best performances, and numbers being bold only indicate the second best ones. We compare the average results with those of the state-of-the-art trackers. The up arrows indicate that higher scores correspond to better performances, while the down arrows indicate the opposite 

123 

International Journal of Computer Vision 

**Table 4** Single-camera tracking results 

|Dataset<br>**PETS09 S1.L1-2**|Method<br>Milan et al. (2016)|MOTA↑<br>58.7|<br>MOTP↑<br>**69.4**|<br>MT↑<br>**19**|ML↓<br>14|FP↓<br>150|FN↓<br>1427|IDS↓<br>12|FM↓<br>**8**|
|---|---|---|---|---|---|---|---|---|---|
||Hamid-Rezatofghi et al. (2015)|**63.5**|64.5|17|**9**|**112**|**1279**|13|–|
||Kim et al. (2015)|62.1|**70.3**|**21**|**9**|–|–|**11**|14|
||**Ours**|**65.1**|65.7|**21**|**10**|**40**|**1290**|**12**|**10**|
||Wen et al. (2016)|56.6|56.3|16|7|**72**|1023|28|26|
||Milan et al. (2014)|57.9|59.7|**19**|11|148|918|21|**13**|
||Hamid-Rezatofghi et al. (2015)|**70.0**|**64.8**|**21**|**5**|108|**658**|**10**|–|
||**Ours**|**68.4**|**71.1**|**20**|**5**|**40**|**766**|**10**|**7**|
|**PETS09 S1.L2-1**|Milan et al. (2016)|29.8|60.1|**5**|23|**104**|3400|47|38|
||Hamid-Rezatofghi et al. (2015)|**32.8**|57.6|**5**|**15**|218|**3108**|76|–|
||Kim et al. (2015)|25.4|**62.2**|3|24|–|–|**25**|**30**|
||**Ours**|**32**|**61.9**|**8**|**18**|**47**|**3373**|**18**|**22**|
||Milan et al. (2014)|30.8|49|7|**20**|**227**|**2308**|61|**35**|
||Hamid-Rezatofghi et al. (2015)|**32.8**|**59.8**|**9**|**20**|230|**2238**|**52**|–|
||**Ours**|**34.5**|**66.1**|**9**|**19**|**42**|2395|**19**|**21**|
|**PETS09 S2.L2**|Milan et al. (2016)|57.0|59.8|10|3|**485**|3801|**137**|**131**|
||Hamid-Rezatofghi et al. (2015)|58.2|58.5|**11**|**0**|1051|**3108**|143|–|
||Kim et al. (2015)|**59.2**|**61.4**|10|**2**|–|–|120|162|
||**Ours**|**62.5**|**61.5**|**13**|**0**|**295**|**3458**|**111**|**125**|
||Milan et al. (2014)|56.9|**59.4**|**28**|12|**622**|2881|**99**|**73**|
||Hamid-Rezatofghi et al. (2015)|**58.3**|59.3|**22**|**6**|910|**2468**|**103**|–|
||**Ours**|**62.7**|**64.6**|**28**|**11**|**224**|**2805**|**84**|**84**|
|**PETS09 S2.L3**|Milan et al. (2016)|40.1|65.1|**9**|23|**74**|2527|22|21|
||Hamid-Rezatofghi et al. (2015)|**48.0**|62.3|**13**|**18**|161|**2092**|23|–|
||Kim et al. (2015)|38.5|**70.8**|**9**|**22**|–|–|**8**|**9**|
||**Ours**|**46.9**|**67.6**|**9**|**18**|**16**|**2295**|**12**|**14**|
||Milan et al. (2014)|45.4|**64.6**|9|18|169|1572|38|**27**|
||Hamid-Rezatofghi et al. (2015)|**53.9**|61.6|**15**|**17**|**162**|**1320**|**20**|–|
||**Ours**|**51.5**|**69.3**|**12**|**16**|**12**|**1554**|**14**|**17**|
|**Average**|Milan et al. (2016)|46.4|63.6|10.8|15.8|**203.3**|2788.8|54.5|**49.5**|
||Hamid-Rezatofghi et al. (2015)|**50.6**|60.7|**11.5**|**10.5**|385.5|**2396.8**|63.8|–|
||Kim et al. (2015)|46.3|**66.2**|10.8|14.3|–|–|**41**|53.8|
||**Ours**|**51.6**|**64.2**|**12.8**|**11.5**|**99.5**|**2604.0**|**38.3**|**42.8**|
||Milan et al. (2014)|47.8|58.2|15.8|15.3|**291.5**|1919.8|54.8|**37**|
||Hamid-Rezatofghi et al. (2015)|**53.8**|**61.4**|**16.8**|**12**|352.5|**1671**|**46.3**|–|
||<br>**Ours**|**54.3**|**67.8**|**17.3**|**12.8**|**79.5**|**1880.0**|**31.8**|**32.3**|



Numbers being both bold and underlined indicate the best performances, and numbers being bold only indicate the second best ones. Our tracker consistently ranks among the top two in terms of almost all metrics. The results of compared methods are taken from their papers directly. In some of their work, parts of the metrics are not reported. All the methods here use the same detections and ground truth 

lic detections and ground truth provided by Wen et al. (2016). 

### **6.2 Evaluation Metrics** 

We use the standard MOT evaluation metrics, including the Multiple Object Tracking Accuracy (MOTA), ID F1 score (IDF1), Multiple Object Tracking Precision (MOTP), 

Mostly Tracked targets (MT), Mostly Lost targets (ML), and Fragments (FM). Among these metrics, MOTA is considered to be the most important one, as it accounts for False Positive (FP), False Negative (FN) and Identity Switches (IDS). For details on the how to compute these metrics, please refer to https://motchallenge.net/ results/MOT16/. 

123 

International Journal of Computer Vision 



<!-- Start of picture text -->
(a) (b) (c)<br>(d) (e) (f) (g)<br><!-- End of picture text -->

**Fig. 11** Qualitative tracking results on **a** PETS09 S2.L1, **b** PETS S2.L2 and **c** PETS S2.L3. For each sequence, results on three camera views are shown 

### **6.3 Re-identification Results** 

To validate the performance of re-identification in our multiobject tracking task, we conduct re-identification experiments on the training sets of MOT17. Recall that our goal is to re-identify a detection hypothesis to existing tracks, and thus we introduce a sequence-to-single architecture based on LSTM. In the training stage, we extract all object trajectories by measuring the IOU between detections and their ground truth, and thus obtain a sequence-to-single sample from the trajectory. We use the contrastive loss as the objective for our deep model, and set the training batch size to 8. In our case the ration between positive and negative samples are around 1 to 8. 

Inexperiments,Weevaluatetheeffectsofdifferentappearance features for re-identification. Four different appearance features are compared, including LOMO, CNN (Girshick et al. 2014), the simple RGB histogram and LBP histogram. The CNN features are extracted using the convolutional neural network trained on the ImageNet + PASCAL VOC dataset (Girshick et al. 2014). We note that, the extracted CNN features have 4096 dimensions, for consistency, in the preprocessing, we use the PCA to reduce all features into a consistent 256 dimension. 

We also test the performances of re-identification versus the different numbers of LSTM units. The number of LSTM units encodes the amount of historical information to be accounted for. We vary the numbers of LSTM units from 5 to 20, and show the corresponding results in Table 2. As can be seen, LOMO always yields the best results. Since the historical information is often redundant and too much such information will unavoidably burden computation, we fix the LSTM units to 15 for the rest of our experiments. To make direct comparisons of our re-identification model 

with different appearance features in MOT, we apply them respectively to the MOT17-02 video sequence and observe their performances on MOTA and IDs in Fig. 9. 

### **6.4 Semi-online Results** 

In this section, we explore the benefits of semi-online model in multi-object tracking. In specific, we introduce several future frames to help the data association between detections in current frame and existing trackers. As we have discussed, the frames in the future provide important feedbacks to the exisiting trackers and prevent them incorrectly matching to false detection. In spite of the fact that the semi-online model bring many performance benefits, the more future frames will seriously burden the computation. In this section, we explore how we can set the window size of future frames to balance the computation and tracking performance. Here, we range the window size from 1 to 30 to observe the their MOTA and MOTP changes in Fig. 10. It is easy to observe that for both sequences the larger window size can achieve better performance, while the improvement is not linear, thus, in our setting, we fix the window size _τ_ to 10 for all our experiments. 

### **6.5 Single-Camera Results** 

We show the quantitative tracking results of our tracker and those of the state-of-the-art ones on the MOT17 dataset in Table 3 and on the four sequences of PETS09 in Table 4. We also show the qualitative results on MOT17 using a single camera in Fig. 11. 

In Table 3, we compare the our tracking results with the state-of-the-art trackers. As shown in the table and also on the 

123 

International Journal of Computer Vision 

**Table 5** Mulit-camera tracking results on PETS09 

|Dataset<br>**PETS09 S2.L1**|Method<br>**Ours**|Camera ID<br>1|s<br>MOTA↑<br>94.30|<br>MOTP↑<br>80.10|<br>GT<br>19|MT↑<br>100.00|ML↓<br>0.00|FM↓<br>13|IDS↓<br>67|
|---|---|---|---|---|---|---|---|---|---|
||Leal-Taixé et al. (2012)|1+5|85.74|67.87|19|89.47|**0.00**|115|150|
||Hofmann et al. (2013)|1+5|91.89|**79.50**|19|**94.74**|**0.00**|29|41|
||Wen et al. (2016)|1+5|**95.51**|**80.60**|19|**100.00**|**0.00**|**12**|**14**|
||**Ours**|1+5|**96.90**|80.10|19|**94.74**|**0.00**|**2**|**4**|
||Leal-Taixé et al. (2012)|1+5+7|82.06|66.23|19|89.47|**0.00**|125|270|
||Hofmann et al. (2013)|1+5+7|91.66|**79.40**|19|**94.74**|**0.00**|31|45|
||Wen et al. (2016)|1+5+7|**95.08**|**79.80**|19|**100.00**|**0.00**|**13**|**13**|
||**Ours**|1+5+7|**96.80**|79.90|19|**100.00**|**0.00**|**1**|**2**|
|**PETS09 S2.L2**|**Ours**|1|61.3|60.4|43|25.58|0.00|220|236|
||Leal-Taixé et al. (2012)|1+2|40.14|54.13|43|4.65|9.30|581|621|
||Hofmann et al. (2013)|1+2|58.94|**65.80**|43|25.56|**2.33**|288|385|
||Wen et al. (2016)|1+2|**67.00**|**61.50**|43|**51.16**|**0.00**|**239**|**239**|
||**Ours**|1+2|**72.3**|57.4|43|**67.44**|**0.00**|**173**|**153**|
||Leal-Taixé et al. (2012)|1+2+3|36.38|53.83|43|2.33|9.30|678|865|
||Hofmann et al. (2013)|1+2+3|58.85|**66.00**|43|30.23|**2.33**|293|388|
||Wen et al. (2016)|1+2+3|**65.24**|**61.80**|43|**44.19**|**0.00**|**246**|**249**|
||**Ours**|1+2+3|**72.1**|58.30|43|**72.09**|**2.33**|**183**|**142**|
|**PETS09 S2.L3**|**Ours**|1|56.3|60.9|44|36.36|25.00|38|54|
||Leal-Taixé et al. (2012)|1+2|48.49|51.74|44|22.73|**9.09**|250|279|
||Hofmann et al. (2013)|1+2|54.39|**60.20**|44|25.00|25.00|**67**|**106**|
||Wen et al. (2016)|1+2|**57.06**|**59.30**|44|**38.64**|15.91|120|129|
||**Ours**|1+2|**65.4**|59.1|44|**40.91**|**9.09**|**55**|**60**|
||Leal-Taixé et al. (2012)|1+2+4|40.22|49.46|44|9.09|**15.91**|234|300|
||Hofmann et al. (2013)|1+2+4|49.79|**63.00**|44|**29.55**|25.00|**80**|123|
||Wen et al. (2016)|1+2+4|**54.39**|54.90|44|**29.55**|20.45|99|**92**|
||**Ours**|1+2+4|**54.3**|**56.4**|44|**36.36**|**6.82**|**87**|**82**|
|**Average**|**Ours**|(1)|70.63|67.13|–|53.98|8.33|90.33|119.00|
||Leal-Taixé et al. (2012)|(2)|58.12|57.91|–|38.95|6.13|315.33|350|
||Hofmann et al. (2013)|(2)|68.41|**68.50**|–|48.43|9.11|128.00|177.33|
||Wen et al. (2016)|(2)|**73.19**|**67.13**|–|**63.27**|**5.30**|**123.67**|**127.33**|
||**Ours**|(2)|**78.20**|65.53|–|**67.70**|**3.03**|**76.67**|**72.33**|
||Leal-Taixé et al. (2012)|(3)|52.89|56.51|–|33.63|8.40|345.67|478.33|
||Hofmann et al. (2013)|(3)|66.77|**69.47**|–|51.51|9.11|134.67|185.33|
||Wen et al. (2016)|(3)|**71.57**|**65.5**|–|**57.91**|**6.82**|**119.33**|**118**|
||**Ours**|(3)|**74.40**|64.87|–|**69.48**|**3.05**|**90.33**|**75.33**|



Numbers being both bold and underlined indicate the best performances, and numbers being bold only indicate the second best ones. Our tracker consistently ranks the best among all in terms of IDS thanks to the tracker’s re-identification capability. In terms of MOTA, our tracker achieves the highest scores for all but one sequences. All the methods here use the same detections and ground truth. The selections of cameras comply with that of Hofmann et al. (2013) for fair comparisons 

123 

International Journal of Computer Vision 

**Fig. 12** MOTA and IDS of our tracking results using different appearance features on the MOT17-02 sequence 



<!-- Start of picture text -->
(a)<br>(b)<br>(c)<br><!-- End of picture text -->

official website of MOT17,<sup>1</sup> our method named SemiOMOT achieves a MOTA score of 52 _._ 4. Thanks to the optimization over the existing tracks and the future frames, our model is able to utilize image evidences in the future to make decisions in the current frame. By explicitly incorporating the state-ofthe-art re-identification, appearance and motion affinity into data association, our approach is able to re-identify targets even after long-term occlusions, and yields superior results to the offline methods including (Milan et al. 2016, 2014). 

Table 4 shows the tracking results on the four crowded sequences of PETS09. To make a comprehensive comparison, for each sequence, we record two sets of tracking results under different experimental settings. The first one follows (Milan et al. 2016) where all pedestrians in the video frames are considered; the second follows (Milan et al. 2014) whereamonitoredareais definedandonlypedestrians within the area are considered. In both cases, our tracker achieves very promising results. 

### **6.6 Multi-camera Results** 

We show the quantitative multi-camera tracking results on the PETS09 dataset in Table 5, and the qualitative ones in Fig. 12. For comparisons, we follow the same experiment 

> 1 https://motchallenge.net/results/MOT17/, accessed on Aug 10, 2019. 

**Table 6** Running time and speed of our tracker on single-camera sequences 

|Dataset|Frames|Running time|Speed (fps)|
|---|---|---|---|
|S1.L1-2|241|40|6.0|
|S1.L2-1|201|51|4.0|
|S2.L2|436|291|1.5|
|S2.L3|240|61|4.0|
|MOT17|17_,_757|27_,_099|0.7|



settings as (Hofmann et al. 2013): we select the same cameras for tracking and use the same detections and ground truth. Our tracker achieves the best IDS for all sequences and the best MOTA for all but one sequences. It is obvious that multi-object tracking in multi-camera bring much improvement than in single camera. This is, pedestrian lose in one camera is likely to be visible from another camera. Our tracker explore the complementary mechanism with a window of future frames and greatly boost the tracking performance. Note that, in some cases the tracking performances using three cameras are worse than those obtained using two. This is because two cameras often provide sufficient and complementary information, and the detection in the third one may bring in noises and further downgrade the tracking performance. This trend is observed for all the compared trackers. 

123 

International Journal of Computer Vision 

|**Table 7** Running time and<br>speed of our tracker on|Dataset|Camera number|Frames|Running time|Speed (fps)|
|---|---|---|---|---|---|
|multi-camera sequences|S2.L1|2|795|183|4.3|
||S2.L1|3|795|225|3.5|
||S2.L2|2|436|670|0.7|
||S2.L2|3|436|103|0.4|
||S2.L3|2|240|188|1.3|
||S2.L3|3|240|509|0.5|



### **6.7 Time Analysis** 

We show the running time of our tracker on single-camera sequences in Table 6 and that of multi-camera ones in Table 7 respectively. Note that, the time for extracting features is not included here. We implement our tracker in C++ and test it on an 8-core 3.2 GHz PC with 16 GB memory. We use the NVIDIA GTX 1080 to train our re-identification appearancemodel.Withspeeduptechniqueslikeaspruning,parallel computation and fast _α_ -expansion in optimizing MRF, our code, which is not fully optimized, runs reasonably fast. 

## **7 Conclusion** 

In this paper, we propose a novel semi-online multi-people tracking approach. It conducts data association progressively by optimizing an objective function defined over existing trajectories and detection hypotheses from a batch of the future frames. We cast the tracking problem as a re-identification one and explicitly handle longer-term occlusions and appearance changes of the targets. Our method is modeled as an MLMRF that accounts for the appearance and motion of the targets, as well as the time, space and view constraints. We introduce a simple yet effective extension of the _α_ -expansion to solve the MLMRF. Our tracker achieves very promising tracking performance on the challenging MOT17 and PETS09 dataset. 

- Bergmann, P., Meinhardt, T., & Leal-Taixe, L. (2019). Tracking without bells and whistles. In _ICCV_ . 

- Boros, E., & Hammer, P. (2002). Pseudo-Boolean optimization. _Discrete Applied Mathematics_ , _123_ (1), 155–225. 

- Boykov, Y., Veksler, O., & Zabih, R. (2001). Fast approximate energy minimization via graph cuts. _TPAMI_ , _23_ (11), 1222–1239. 

- Breitenstein, M., Reichlin, F., Leibe, B., Koller-Meier, E., & Van-Gool, L. (2011). Online multiperson tracking-by-detection from a single, uncalibrated camera. _TPAMI_ , _33_ (9), 1820–1833. 

- Brendel, W., Amer, M., & Todorovic, S. (2011). Multiobject tracking 

as maximum weight independent set. In _ICCV_ (pp. 1273–1280). 

- Butt, A., & Collins, R. (2013). Multi-target tracking by Lagrangian relaxation to min-cost network flow. In _CVPR_ (pp. 1846–1853). 

- Chan, A., Liang, Z., & Vasconcelos, N. (2008). Privacy preserving crowd monitoring: Counting people without people models or tracking. In _CVPR_ (pp. 1–7). 

- Chari, V., Lacoste-Julien, S., Laptev, I., & Sivic, J. (2015). On pairwise costs for network flow multi-object tracking. In _CVPR_ (pp. 5537– 5545). 

- Cheng, D., Gong, Y., Zhou, S., Wang, J., & Zheng, N. (2016). Person re-identification by multi-channel parts-based CNN with improved triplet loss function. In _CVPR_ (pp. 1335–1344). 

- Chen, D., Li, H., Xiao, T., Yi, S., & Wang, X. (2018). Video person reidentification with competitive snippet-similarity aggregation and co-attentive snippet embedding. _CVPR_ (pp. 1169–1178). 

- Chen, J., Sheng, H., Zhang, Y., & Xiong, Z. (2017). Enhancing detection model for multiple hypothesis tracking. In _CVPR workshop_ (pp. 2143–2152). 

- Chen, L., Ai, H., Zhuang, Z., & Shang, C. (2018). Real-time multiple people tracking with deeply learned candidate selection and person re-identification. _ICME_ , _5_ , 8. 

- Chen, S., Fern, A., & Todorovic, S. (2014). Multi-object tracking via constrained sequential labeling. In _CVPR_ (pp. 1130–1137). 

- Choi, W. (2015). Near-online multi-target tracking with aggregated local flow descriptor. In _ICCV_ (pp. 3029–3037). 

- Chu,P.,&Ling,H.(2019).Famnet: Joint learningoffeature,affinityand multi-dimensional assignment for online multiple object tracking. In _ICCV_ . 

## **References** 

- Arora, C., & Globerson, A. (2013). Higher order matching for consistent multiple target tracking. In _ICCV_ (pp. 177–184). 

- Bae, S., & Yoon, K. (2014). Robust online multi-object tracking based on tracklet confidence and online discriminative appearance learning. In _CVPR_ (pp. 1218–1225). 

- Bae, S., & Yoon, K. (2017). Confidence-based data association and discriminative deep appearance learning for robust online multiobject tracking. In _TPAMI_ . 

- Benfold, B., & Reid, I. (2011). Stable multi-target tracking in real-time surveillance video. In _CVPR_ (pp. 3457–3464). 

- Berclaz, J., Fleuret, F., Turetken, E., & Fua, P. (2011). Multiple object tracking using k-shortest paths optimization. _TPAMI_ , _33_ (9), 1806– 1819. 

- Collins, R., Liu, Y., & Leordeanu, M. (2005). Online selection of discriminative tracking features. _TPAMI_ , _27_ (10), 1631–1643. 

- Dehghan, A., Assari, S. M., & Shah, M. (2015). Gmmcp tracker: Globally optimal generalized maximum multi clique problem for multiple object tracking. In _CVPR_ (pp. 4091–4099). 

- Dehghan, A., Tian, Y., Torr, P., & Shah, M. (2015). Target identityaware network flow for online multiple target tracking. In _CVPR_ (pp. 1146–1154). 

- Delong, A., Osokin, A., Isack, H., & Boykov, Y. (2012). Fast approximate energy minimization with label costs. _IJCV_ , _96_ (1), 1–27. 

- Fagot-Bouquet, L., Audigier, R., Dhome, Y., & Lerasle, F. (2016). Improving multi-frame data association with sparse representations for robust near-online multi-object tracking. In _ECCV_ (pp. 774–790). 

123 

International Journal of Computer Vision 

- Fan, J., Shen, X., & Wu, Y. (2012). Scribble tracker: A matting-based approach for robust tracking. _TPAMI_ , _34_ (8), 1633–1644. 

- Fan, J., Shen, X., & Wu, Y. (2013). What are we tracking: A unified approach of tracking and recognition. _TIP_ , _22_ (2), 549–560. 

- Fleuret, F., Shitrit, H., & Fua, P. (2014). Re-identification for improved people tracking. In _Person re-identification_ (pp. 309–330). 

- Fortmann, T., Yaakov, B., & Scheffe, M. (1983). Sonar tracking of multiple targets using joint probabilistic data association. _JOE_ , _8_ (3), 173–184. 

- Fu, Y., Wei, Y., Zhou, Y., Shi, H., Huang, G., Wang, X., et al. (2019). Horizontal pyramid matching for person re-identification. In _AAAI_ (pp. 8295–8302). 

- Galoogahi, H., Fagg, A., Huang, C., Ramanan, D., & Lucey, S. (2017). Need for speed: A benchmark for higher frame rate object tracking. arXiv preprint arXiv:1703.05884. 

- Geng, M., Wang, Y., Xiang, T., & Tian, Y. (2016). Deep transfer learning for person re-identification. arXiv preprint arXiv:1611.05244. 

- Girshick, R., Donahue, J., Darrell, T., & Malik, J. (2014). Rich feature hierarchies for accurate object detection and semantic segmentation. In _CVPR_ (pp. 580–587). 

- Hamid-Rezatofighi, S., Milan, A., Zhang, Z., Shi, Q., Dick, A., & Reid, I. (2015). Joint probabilistic data association revisited. In _ICCV_ (pp. 3047–3055). 

- Henschel, R., Zou, Y., & Rosenhahn, B. (2019). Multiple people tracking using body and joint detections. In _CVPR Workshops_ . 

- Hofmann, M., Wolf, D., & Rigoll, G. (2013). Hypergraphs for joint multi-view reconstruction and multi-object tracking. In _CVPR_ (pp. 3650–3657). 

- Hong-Yoon, J., Lee, C., Yang, M., & Yoon, K. (2016). Online multiobject tracking via structural constraint event aggregation. In _CVPR_ (pp. 1392–1400). 

- http://www.cvg.reading.ac.uk/PETS2009/a.html . 

https://motchallenge.net/results/MOT16/ . 

- Hu, W., Li, X., Luo, W., Zhang, X., Maybank, S., & Zhang, Z. (2012). Single and multiple object tracking using log-Euclidean Riemannian subspace and block-division appearance model. _TPAMI_ , _34_ (12), 2420–2440. 

- Janai, J., Güney, F., Behl, A., & Geiger, A. (2017). Computer vision for autonomous vehicles: Problems, datasets and state-of-the-art. arXiv preprint arXiv:1704.05519. 

- Jerripothula, K., Cai, J., & Yuan, J. (2016). Cats: Co-saliency activated tracklet selection for video co-localization. In _ECCV_ (pp. 187– 202). 

- Keuper, M., Tang, S., Yu, Z., Andres, B., Brox, T., & Schiele, B. (2016). A multi-cut formulation for joint segmentation and tracking of multiple objects. arXiv preprint arXiv:1607.06317. 

- Keuper, M., Tang, S., Zhongjie, Y., Andres, B., Brox, T., & Schiele, B. (2016). A multi-cut formulation for joint segmentation and tracking of multiple objects. arXiv preprint arXiv:1607.06317. 

- Kim, C., Li, F., Ciptadi, A., & Rehg, J. (2015). Multiple hypothesis tracking revisited. In _ICCV_ (pp. 4696–4704). 

- Kim, C., Li, F., & Rehg, J. M. (2018). Multi-object tracking with neural gating using bilinear lSTM. In _ECCV_ (pp. 200–215). 

- Kuo, C., Huang, C., & Nevatia, R. (2010). Multi-target tracking by on-line learned discriminative appearance models. In _CVPR_ (pp. 685–692). 

- Kuo, C., & Nevatia, R. (2011). How does person identity recognition help multi-person tracking? In _CVPR_ (pp. 1217–1224). 

- Lafferty, J., McCallum, A., Pereira, F., et al. (2001). Conditional random fields: Probabilistic models for segmenting and labeling sequence data. _ICML_ , _1_ , 282–289. 

- Lan, L., Tao, D., Gong, C., Guan, N., & Luo, Z. (2016). Online multi-object tracking by quadratic pseudo-Boolean optimization. In _IJCAI_ (pp. 3396–3402). 

- Lan, L., Wang, X., Zhang, S., Tao, D., Gao, W., & Huang, T. S. (2018). Interacting tracklets for multi-object tracking. In _TIP_ . 

- Leal-Taixé, L., Canton-Ferrer, C., & Schindler, K. (2016). Learning by tracking: Siamese cnn for robust target association. In _CVPR workshops_ (pp. 33–40). 

- Leal-Taixé, L., Pons-Moll, G., & Rosenhahn, B. (2012). Branch-andprice global optimization for multi-view multi-target tracking. In _CVPR_ (pp. 1987–1994). 

- Lenz, P., Geiger, A., & Urtasun, R. (2015). Followme: Efficient online min-cost flow tracking with bounded memory and computation. In _ICCV_ (pp. 4364–4372). 

- Levinkov, E., Uhrig, J., Tang, S., Omran, M., Insafutdinov, E., Kirillov, A., Rother, C., Brox, T., Schiele, B., & Andres, B. (2017). Joint graph decomposition and node labeling: Problem, algorithms, applications. In _CVPR_ . 

- Liang, P., Blasch, E., & Ling, H. (2015). Encoding color information for visual tracking: Algorithms and benchmark. _TIP_ , _24_ (12), 5630– 5644. 

- Liao, S., Hu, Y., Zhu, X., & Li, S. (2015). Person re-identification by local maximal occurrence representation and metric learning. In _CVPR_ (pp. 2197–2206). 

- Liu, J., Carr, P., Collins, R., & Liu, Y. (2013). Tracking sports players with context-conditioned motion models. In _CVPR_ (pp. 1830– 1837). 

- Liwicki, S., Zafeiriou, S., Tzimiropoulos, G., & Pantic, M. (2012). Efficient online subspace learning with an indefinite kernel for visual tracking and recognition. In _TNNLS_ (pp. 1624–1636). 

- Liwicki, S., Zafeiriou, S., & Pantic, M. (2015). Online kernel slow featureanalysisfortemporalvideosegmentationandtracking. _TIP_ , _24_ (10), 2955–2970. 

- Maksai, A., & Fua, P. (2019). Eliminating exposure bias and metric mismatch in multiple object tracking. In _CVPR_ (pp. 4639–4648). 

- Maksai, A., Wang, X., & Fua, P. (2016). What players do with the ball: A physically constrained interaction modeling. In _CVPR_ (pp. 972–981). 

- Maksai, A., Wang, X., Fleuret, F., & Fua, P. (2017). Non-Markovian globally consistent multi-object tracking. In _ICCV_ (pp. 2563– 2573). 

- McLaughlin,N.,delRincon,J.M.,&Miller,P.(2016).Recurrentconvolutional network for video-based person re-identification. In _CVPR_ (pp. 1325–1334). 

- Milan, A., Leal-Taixé, L., Reid, I. D., Roth, S., & Schindler, K. (2016). Mot16: A benchmark for multi-object tracking. arXiv preprint arXiv:1603.00831. 

- Milan, A., Leal-Taixé, L., Schindler, K., & Reid, I. (2015). Joint tracking and segmentation of multiple targets. In _CVPR_ (pp. 5397–5406). 

- Milan, A., Roth, S., & Schindler, K. (2013). Continuous energy minimization for multitarget tracking. _TPAMI_ , _36_ (1), 58–72. 

- Milan, A., Roth, S., & Schindler, K. (2014). Continuous energy minimization for multitarget tracking. _TPAMI_ , _36_ (1), 58–72. 

- Milan, A., Schindler, K., & Roth, S. (2016). Multi-target tracking by discrete-continuous energy minimization. _TPAMI_ , _38_ (10), 2054– 2068. 

- Nillius, P., Sullivan, J., & Carlsson, S. (2006). Multi-target tracking— linking identities using bayesian network inference. In _ECCV_ (pp. 2187–2194). 

- Pang, Y., Shi, X., Jia, B., Blasch, E., Sheaff, C., Pham, K., et al. (2015). Multiway histogram intersection for multi-target tracking. In _ICIF_ (pp. 1938–1945). 

- Pirsiavash, H., Ramanan, D., & Fowlkes, C. (2011). Globally-optimal greedy algorithms for tracking a variable number of objects. In _CVPR_ (pp. 1201–1208). 

- Possegger, H., Mauthner, T., Roth, P., & Bischof, H. (2014). Occlusion geodesics for online multi-object tracking. In _CVPR_ (pp. 1306– 1313). 

- Qiu, J., Wang, X., Fua, P., & Tao, D. (2020). Matching seqlets: An unsupervised approach for locality preserving sequence matching. In _TPAMI_ . 

123 

International Journal of Computer Vision 

- Qiu, J., Wang, X., Maybank, S., & Tao, D. (2019). World from blur. In _CVPR_ (pp. 8493–8504). 

- Ramanan, D., Forsyth, D., & Zisserman, A. (2006). Tracking people by learning their appearance. _TPAMI_ , _29_ (1), 65–81. 

- Ristani, E., & Tomasi, C. (2018). Features for multi-target multi-camera tracking and re-identification. In _CVPR_ (pp. 6036–6046). 

- Roberto, H., Leal-Taixé, L., & Bodo, R. (2017). Fusion of head and full-body detectors for multi-object tracking. arXiv preprint arXiv:1705.08314. 

- Sadeghian, A., Alahi, A., & Savarese, S. (2017). Tracking the untrackable: Learning to track multiple cues with long-term dependencies. In _ICCV_ (pp. 300–311). 

- Sanchez-Matilla, R., Poiesi, F., & Cavallaro, A. (2016). Online multitarget tracking with strong and weak detections. In _ECCV_ (pp. 84–99). 

- Shen,C.,Wang,X.,Song,J.,Sun,L.,&Song,M.(2019).Amalgamating knowledge towards comprehensive classification. In _AAAI_ (pp. 3068–3075). 

- Shitrit, H. B., Berclaz, J., Fleuret, F., & Fua, P. (2014). Multi-commodity network flow for tracking multiple people. _TPAMI_ , _36_ (8), 1614– 1627. 

- Shu, G., Dehghan, A., Oreifej, O., Hand, E., & Shah, M. (2012). Partbased multiple-person tracking with partial occlusion handling. In _CVPR_ (pp. 1815–1821). 

- Song, J., Chen, Y., Wang, X., Shen, C., & Song, M. (2019). Deep model transferability from attribution maps. In _NeurIPS_ (pp. 6179–6189). 

- Su, C., Zhang, S., Xing, J., Gao, W., & Tian, Q. (2016). Deep attributes driven multi-camera person re-identification. In _ECCV_ (pp. 475– 491). 

- Sullivan, J., & Carlsson, S. (2006). Tracking and labelling of interacting multiple targets. In _ECCV_ (pp. 619–632). 

- Tang, S., Andres, B., Andriluka, M., & Schiele, B. (2015). Subgraph decomposition for multi-target tracking. In _CVPR_ (pp. 5033– 5041). 

- Tang, S., Andres, B., Andriluka, M., & Schiele, B. (2016). Multi-person tracking by multicut and deep matching. In _ECCV workshops_ (pp. 100–111). 

- Tang, S., Andriluka, M., Andres, B., & Schiele, B. (2017). Multiple people tracking by lifted multicut and person reidentification. In _CVPR_ (pp. 3539–3548). 

- Tsai, D., Flagg, M., Nakazawa, A., & Rehg, J. (2012). Motion coherent tracking using multi-label MRF optimization. _IJCV_ , _100_ (2), 190– 202. 

- Turetken, E., Wang, X., Becker, C., Haubold, C., & Fua, P. (2017). Network flow integer programming to track elliptical cells in timelapse sequences. _TMI_ , _36_ (4), 942–951. 

- Wang, X., Fan, B., Chang, S., Wang, Z., Liu, X., Tao, D., & Huang, T. (2017). Greedy batch-based minimum-cost flows for tracking multiple objects. In _TIP_ . 

- Wang,J.,Huang,S.,Wang,X.,&Tao,D.(2019).Notallpartsarecreated equal: 3D pose estimation by modelling bi-directional dependencies of body parts. In _ICCV_ . 

- Wang, X., Türetken, E., Fleuret, F., & Fua, P. (2014). Tracking interacting objects optimally using integer programming. In _ECCV_ (pp. 17–32). 

- Wang, H., Ullah, M., Klaser, A., Laptev, I., & Schmid, C. (2009). Evaluation of local spatio-temporal features for action recognition. In _BMVC_ (pp. 124–1). 

- Wang, X., Ablavsky, V., Shitrit, H., & Fua, P. (2014). Take your eyes off the ball: Improving ball-tracking by focusing on team play. _CVIU_ , _119_ , 102–115. 

- Wang, X., Turetken, E., Fleuret, F., & Fua, P. (2016). Tracking interacting objects using intertwined flows. _TPAMI_ , _38_ (11), 2312–2326. 

- Weinzaepfel, P., Revaud, J., Harchaoui, Z., & Schmid, C. (2013). Deepflow: Large displacement optical flow with deep matching. In _ICCV_ (pp. 1385–1392). 

- Wen, L., Lei, Z., Chang, M., Qi, H., & Lyu, S. (2016). Multi-camera multi-target tracking with space-time-view hyper-graph. In _IJCV_ (pp. 1–21). 

- Wen, L., Lei, Z., Lyu, S., Li, S., & Yang, M. (2016). Exploiting hierarchical dense structures on hypergraphs for multi-object tracking. _TPAMI_ , _38_ (10), 1983–1996. 

- Wu, Z., Thangali, A., Sclaroff, S., & Betke, M. (2012). Coupling detection and data association for multiple object tracking. In _CVPR_ (pp. 1948–1955). 

- Wu, Z., & Betke, M. (2016). Global optimization for coupled detection and data association in multiple object tracking. _CVIU_ , _143_ , 25–37. 

- Xiang, Y., Alahi, A., & Savarese, S. (2015). Learning to track: Online multi-object tracking by decision making. In _ICCV_ (pp. 4705– 4713). 

- Yang, B., & Nevatia, R. (2012). An online learned CRF model for multitarget tracking. In _CVPR_ (pp. 2034–2041). 

- Yang, M., Yuan, J., & Wu, Y. (2007). Spatial selection for attentional visual tracking. In _CVPR_ (pp. 1–8). 

- Ye, J., Ji, Y., Wang, X., Ou, K., Tao, D., & Song, M. (2019). Student becoming the master: Knowledge amalgamation for joint scene parsing, depth estimation, and more. In _CVPR_ (pp. 2829–2838). 

- Yin, X., Wang, X., Yu, J., Zhang, M., Fua, P., & Tao, D. (2018). Fisheyerecnet: A multi-context collaborative deep network for fisheye image rectification. In _ECCV_ (pp. 475–490). 

- Yoon, J., Yang, M., Lim, J., & Yoon, K. (2015). Bayesian multi-object tracking using motion context from multiple objects. In _WACV_ (pp. 33–40). 

- Yu, S., Yang, Y., Li, X., & Hauptmann, A. (2016). Long-term identityaware multi-person tracking for surveillance video summarization. arXiv preprint arXiv:1604.07468. 

- Yu, X., Liu, T., Wang, X., & Tao, D. (2017). On compressing deep models by low rank and sparse decomposition. In _CVPR_ (pp. 67– 76). 

- Zhai, M., Roshtkhari, M., & Mori, G. (2016). Deep learning of appearance models for online object tracking. arXiv preprint arXiv:1607.02568. 

- Zhang, J., Wang, N., & Zhang, L. (2017). Multi-shot pedestrian re-identification via sequential decision making. arXiv preprint arXiv:1712.07257. 

- Zhang, L., Li, Y., & Nevatia, R. (2008). Global data association for multi-object tracking using network flows. In _CVPR_ (pp. 1–8). 

- Zheng, L., Bie, Z., Sun, Y., Wang, J., Su, C., Wang, S., et al. (2016). Mars: A video benchmark for large-scale person re-identification. In _ECCV_ (pp. 868–884). 

- Zheng, W., Gong, S., & Xiang, T. (2016). Towards open-world person re-identification by one-shot group-based verification. _TPAMI_ , _38_ (3), 591–606. 

- Zhu, J., Yang, H., Liu, N., Kim, M., Zhang, W., & Yang, M. (2018). Online multi-object tracking with dual matching attention networks. In _ECCV_ (pp. 366–382). 

**Publisher’s Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

- Wang, T., Gong, S., Zhu, X., & Wang, S. (2016). Person re-identification by discriminative selection in video ranking. _TPAMI_ , _38_ (12), 2501–2514. 

- Wang, X., Li, Z., & Tao, D. (2011). Subspaces indexing model on grassmann manifold for image search. _TIP_ , _20_ (9), 2627–2635. 

123 


