<!-- source: 2018 Simulating_a_Basketball_Game_with_HDP-Based_Models_and_Forecasting_the_Outcome.pdf -->

2018 7th International Conference on Digital Home (ICDH) 

# **Simulating a basketball game with HDP-based models and forecasting the outcome** 

Xin Du Weihong Cai _Department of Computer Science, College of Engineering Department of Computer Science, College of Engineering Shantou University, STU Shantou University, STU Shantou, Guangdong, China Shantou, Guangdong, China Email: 17xdu@stu.edu.cn Email: whcai@stu.edu.cn_ 

**_Abstract_ —We used HDP-based models to model the progression of a basketball game. As known to all, the hidden Markov model can be used for analyzing sequences of the game’s content. By introducing Hierarchical Dirichlet Processes on feature extraction and HMMs, we can tackle down the challenges of unknown numbers of mixtures in both models by resorting to nonparametric approach. We employ variational inference for model calculation and cluster the extracted rounds of a basketball match in the form of HMM parameters to forecast the overcome. The proposed scheme is then verified by comparing with other commonly used forecasting approaches: logit regression of the outcome, Naive Bayes method, and Neural Networks. We found that HDPbased models are appropriate for modeling a basketball match and produces more accurate predictions.** 

**_Keywords_ -Sports forecasting; Probability forecasting; Hierarchical Dirichlet Processes; Hidden Markov model;** 

## I. INTRODUCTION 

Forecasting the outcomes of sporting events is important for a team. The accurate prediction can not only satisfy the curiosities of the spectators but also help the coaches to make appropriate strategies [1]. However, as Stekler, Sendor, and Verlander (2010) [2] pointed out in their survey, a large amount of effort is spent in doing this work. One way of dealing with these problems in a uniform way is to construct a model that can simulate the sporting event. In this paper, we make a little contribution in this direction by exploring the use of HDP-based models for basketball game simulation. 

## _A. Related work_ 

The research of sports is often driven by sports betting. In the past, only a few betting markets were available for football, so it has received more attention in scientific literature. Since 1979, Zak, Huang, and Sigfried [3] began to rank different teams by calculating their actual efficiencies. However, no attempt was made to predicate the teams’ match. As far as we know, the first research of forecasting the basketball game’s outcome was from Stern(1994) [4], he used the scores at each quarter of 493 NBA matches to fit a Brownian motion model. Their conclusion gained the win probability of every team, given the current points differences. Kvam and Sokol(2006) [5] used a Markov model to 

predict the winner of NCAA basketball games. Compared with other statistical models and polls, the model predicts more accurate. Dragan(2010) [6] applied a Naive Bayes method to the regular part of the 2009/2010 NBA season. They successfully predicted 67% out of 778 games, but their test sample size is too small to distinguish the reasonable participants from the winner. In addition, Stekler(2010) [2] provided a more comprehensive list of basketball-related forecasting references. 

The most relevant are the researches by Shirley(2007) [7] and Erik(2012) [8]. They both used a Markov model with states which corresponded to how a team obtained (retained) possession and how many points were scored during the previous transition. The simulations based their models were good at estimating a teams win probability. However, as the increasing accessibility of in-play betting has brought a demand for real-time forecasts based on the progression of the sporting event, the accuracies of presented methods are beyond satisfaction. 

## _B. Research objectives_ 

Inspired by the works of Shirley and Erik, we investigated the use of Markov models for different domain’s simulation. The main objective of this paper is to judge whether such a more complex model can still improve the veracity of the prediction. We proposed the HDP-based model to simulating the basketball matches and producing accurate forecasts for the match outcome. 

The rest of the paper is organized as follows. We describe in detail the background in Section 2, which includes Hierarchical Dirichlet Process, Hidden Markov Model and Variational Inference. Then, the hybrid ensemble model is detailed in Section 3. In Section 4, the results of the measures are empirically demonstrated. Section 5 is the conclusion. 

## II. BACKGROUND 

## _A. Hidden Markov Model_ 

For each observation _x_ , HMM assumes a hidden state _z_ , so that the generative process of _x_ is described by _p_ ( _x|z_ ). The generative process for the sequence of hidden states can be defined by, 



978-1-5386-9497-8/18/$31.00 ©2018 IEEE DOI 10.1109/ICDH.2018.00042 

193 

Authorized licensed use limited to: Georgia Institute of Technology. Downloaded on February 27,2024 at 22:51:06 UTC from IEEE Xplore.  Restrictions apply. 



For the case in this paper, if we assume there are _K_ hidden states, the parameters of an HMM are the triplet of initial distribution, the transition matrix, and emission parameter ( **_ρ_** _,_ **_A_** _,_ **_φ_** ), as is defined in Table I. 

Table I 

PARAMETERS FOR HMMS 

|Notation|Gloss|
|---|---|
|**Θ**|distribution parameter of the initial latent state **z1**<br>having Θ_k ≡p_(_z_1_,k_ = 1)<br>so that <sup>�</sup><br>_k_ <sup>Θ</sup><sup>_k_ = 1</sup><br>and _p_(**z**1_|_**Θ**)= <sup>�</sup><sup>_K_</sup><br>_k_=1 <sup>Θ</sup><br>_z_1_,k_<br>_k_|
|**_A_**|the matrix of transition probabilities<br>given by _Aij ≡p_(_zn,j_ = 1_|zn−_1_,j_ = 1)<br>having 0_≤Aij ≤_1 and <sup>�</sup><br>_k _<sup>_Aik_ = 1</sup><br>and therefore<br>_p_(**z**_n|_**z**_n−_1_,_**A**) = <sup>�</sup><sup>_K_</sup><br>_j_=1<br>�_K_<br>_i_=1 <sup>_A_</sup><br>_zn−_1_,izn,j_<br>_i,j_|
|**_φ_**|the set of parameters for emission probabilities<br>such that _p_(**x**_n|_**z**_n,_**_φ_**) = <sup>�</sup><sup>_K_</sup><br>_k_=1 <sup>_p_(</sup><sup>**x**</sup><sup>_n|_</sup><sup>**z**</sup><sup>_n,_</sup><sup>**_φ_**</sup><sup>_k_)</sup><sup>_zn,k_</sup>|



The whole model can be define as the joint distribution over observable data and their hidden states, 



Studied by Shirley and Erik’s work, the Markov models take into account the obtainment (retainment) of possession, how it was obtained, and the number of points scored during the transition. A transition encompasses everything that happens between two states. During a transition, 0, 1, 2, or 3 points are scored. The prediction problem of HMM can also be used for describing the game’s process. Furthermore, the HMM can also estimate the players’ performance in different matches, thus improving the accuracy of the result prediction. 

## _B. Hierarchical Dirichlet Process_ 

The HDP is a nonparametric Bayesian model that models mixtures of the potentially infinite number of components [9]. Its applications have been seen in machine learning problems that involve mixtures of probability distributions, such as textual topic modeling, image processing, and clustering problems [10]. Apart from dealing with infinite mixtures, HDP has shown great application potential due to its combination with HMM, granting this model the capability to process sequential data [11–13]. 

HDP specifies the following generative models, 

- 1) Choose a top-level probability measure: _G_ 0 _|γ, H ∼ DP_ ( _γ, H_ ) 

- 2) Choose second-level topic probability measures: _Gj|α_ 0 _<u>, G</u>_ 0 _∼ DP_ <u>(</u> _α_ 0 _<u>, G</u>_ 0) 

<u>where</u> _<u>H</u>_ <u>is the base distribution of observable data. DP is</u> the Dirichlet Process, which for a process _P_ that generates value **X** 1 _,_ **X** 2 _, ..._ can be defined as, 

where 

## **Algorithm 1** Dirichlet Process 



Existing HMM-related algorithms for solving different aspects of sequential data can readily be applied in real-time forecasts based on the progression of the sporting event. 

- _evaluation problem_ calculates _p_ ( **X** _|_ **_π_** _,_ **_A_** _,_ **_φ_** ) 

- _learning problem_ 

- find **_θ_** = ( **_π_** _,_ **_A_** _,_ **_φ_** ) given **X** , 

- such that _p_ ( **X** _|_ **_π_** _,_ **_A_** _,_ **_φ_** ) is maximized. 

- _predictive distribution_ find the distribution of the next data _p_ ( **x** _N_ +1 _|_ **Xo** _,_ **_θ_** ) given the already observed sequence **Xo** and the model **_θ_** . 

|Draw **X**1 from H||
|---|---|
|**for** _n >_1 **do**||
|Draw **X**_n_ from|H with probability<br>_α_<br>_α_+_n−_1|
|Or yield **X**_n_ =|**v**_i_ with probability<br>_ni_<br>_α_+_n−_1<sup>,</sup>|
|where _ni_ = #|_{X ∈{_**X**1_, ...,_**X**_n−_1_}|X_ =**v**_i}_|
|**end for**||



Via drawing from _H_ through two levels of DP, HDP attains _{Gj}_ which is the set of random measures that have shared atoms linked by _G_ 0 and are responsible for drawing parameters for mixture components. By drawing from **_θ_** _j ∼{Gj}_ , we can acquire both parameters for hidden state transitions in HMM learning. We can embed HDP as the top level of the two mixture models and calculate the proportions for each mixture component. 

Inference on HDP can be carried out using one of the two classes of approximation calculation. 

- _Sampling method_ is a stochastic scheme that optimizes posterior status by randomly sampling from the generative process until convergence. For inference of HDP, Markov chain Monte Carlo and beam sampling have been utilized [9]. 

194 

Authorized licensed use limited to: Georgia Institute of Technology. Downloaded on February 27,2024 at 22:51:06 UTC from IEEE Xplore.  Restrictions apply. 



Figure 1. Illustration of HDP two level stick-breaking equivalent construction 



Figure 2. Illustration of comparison between conventional HMM and HDP-HMM transition . In HDP-HMM, stick indicators on the second level are introduced to map second level sticks to top level mixture components. 

- _Variational inference_ can be viewed as an extension of EM algorithm that optimizes parameters by introducing an approximation distribution to the true generative process and iteratively increasing the lower bound. 

In this paper, we use variational inference on HDP in our purposed method. 

## _C. Variational Inference_ 

For the probabilistic models in our case, the variational inference [14] method treats the parameters for distributions as parts of the latent variables. _p_ ( **X** _,_ **Z** ) can then be essentially expressed as the joint distribution of observable variables, latent variables, and parameters. Taking the logarithm of _p_ ( **X** ) and we have, 



To maximize � _q_ ( **Z** ) ln<sup>_<u>p</u>_</sup><sup><u>(</u></sup> _q_<sup>**X**</sup> ( **Z**<sup>_<u>,</u>_</sup><sup>**Z**</sup> )<sup><u>)</u></sup><sup>_d_</sup><sup>**Z**isequivalenttomini-</sup> mizing the Kullback-Leibler divergence between _q_ ( **Z** ) and _p_ ( **Z** _|_ **X** ). This differs from EM algorithm as now **Z** contains parameters. By crafting a certain form of _q_ ( **Z** ), we can make the computation reasonably tractable and achieve the approximation to the true posterior. Typically we choose a series of factorized variational distributions and iteratively increase the lower bound by optimizing a subset of latent variables with the others 

The two-level drawing of HDP is a discrete model. To perform variational inference, we can construct HDP with 

the equivalent continuous model that consists of two-level stick-breaking processes [15]. This is elaborated in our method chapter. 

## III. METHOD 

We first specify the input format of the derivation in detail based on the games and then elaborate calculation in our purposed method. Table II lists the main notation in the method chapter. 

Table II MAIN NOTATION 

|Notation|Gloss|
|---|---|
|**s**|observed sequence|
|x|observed data in a sequence|
|**S**_u_|the collection of sequence for player _u_|
|**z**|hidden state of HMM using 1-of-K coding scheme|
|**Z**_u_|the collection of hidden states corresponding to **S**_u_|
|**Θ**|initial distribution parameter of HMM|
|**A**|transition matrix of HMM|
|**_φ_**|emission parameters of HMM|
|_φk_|_k_th atom as a mixture component on the top level|
|_βk_<br>|_k_th stick variable on the top level|
|_β_<br>_′_<br>_k_|_k_th stick length on the top level|
|_πj_<br>|_k_th stick variable on the second level|
|_π_<br>_′_<br>_j_|_k_th stick length on the second level|
|**c**|indicator vector for picked top-level on second level|
|_μk_|_k_th multivariate Gaussian mean|
|Λ_k_|_k_th multivariate Gaussian precision matrix|
|_mk, ηk_||
|_Wk, νk_|parameters for _k_th Gaussian-Wishart mixture|
|_gk, hk_|parameters for the _k_th stick on the top level|
|_akm, bkm_|parameters for _m_th stick on _k_th mixture|
|_ζkm_<br>|multinomial parameter for _ckm_|
|_ξi_(_k, m_)|auxiliary for transition in forward-backward|



## _HDP-based hidden Markov method in a basketball game_ 

During the basketball game, two teams (A and B) alternate possession of the ball and try to score points. Just like most modern approaches to basketball analysis [8], we were also focusing on the number of possessions a team has and how effectively they convert them into points. These states cover all moments in a game during which the teams can obtain possession of the ball. However, such a state does not imply a change in the different rounds. The importance of players in the competition has also been ignored. In our model, such problems are easily solved by setting the players individually in a sequence. The state transition probability indicates the passing relationships, the initial probability represents the probability of a player being chosen as an organizer, and the observation probability illustrates the probabilities of different points that the player scores in a round. 

## _Stick-breaking equivalent construction for HDP_ 

Next, we take on the inference on our HDP-based Hidden Markov Method. In the background chapter, HDP is defined as a discrete model that can be sampled, but not directly viable for variational inference. The current study suggests 

195 

Authorized licensed use limited to: Georgia Institute of Technology. Downloaded on February 27,2024 at 22:51:06 UTC from IEEE Xplore.  Restrictions apply. 

an equivalent two-level stick-breaking process to construct, providing a model with continuous variables to optimize. The method in [15] is of particular interest, as it decouples the two levels of DP by setting up stick indicators, which results in a clean and simple calculation scheme for HDP inference. 

For the HDP defined as, 





using the work in [15], the two-level stick-breaking construction for HDP equivalence is described as follows, 







## _Variational inference on HDP-HMM_ 

With these distributions specified, the likelihood for joint distributions of observable data and all latent variables and parameters of HDP-HMM is given by, 



We can define the joint variational distribution, base on the underlying distributions, 



where the factorized variational distributions are coherent with those in _p_ , with their respective variational parameters, 



The hidden states **_z_** are left out above because they are to be inferenced by HMM forward-backward framework. 

The optimization target is the variational lower bound given by, 



**_′ ′_** where **_β_** is the top level stick length and **_π_** is the second level stick length. For one DP level, a stick of length 1 is broken into the infinite number of sticks, during each step of which the proportion to be cut is drawn from Beta distribution. 

A second level stick must be the map to a specific top level stick, so that when it is chosen, the top level mixture component for choosing that second level stick is accounted for. 

Inference in this paper should specify base distribution _H_ for HDP. For HDP-HMM in our case, _H_ is the GaussianWishart distribution. 



assuming _μ_ be the mean and Λ be the precision matrix, which is the inverse covariance matrix for Gaussian. 



Lastly, **_c_** are the top-level stick indicators for second level which are subject to multinomial distributions. 



To do this, factorize 9 and 11 so that the variational expectation of each factorized part can be written out, 







where ϝ() is the Digamma function. 

In our research problem, the emission for HDP-HMM assumes multivariate Gaussian distributions. We can perform the calculation of variational expectations as follows, 

196 

Authorized licensed use limited to: Georgia Institute of Technology. Downloaded on February 27,2024 at 22:51:06 UTC from IEEE Xplore.  Restrictions apply. 



The multivariate Gaussian expectations are required in forward-backward calculations for updating. 

Evaluation of transition matrices for HDP-HMM requires slight effort for the interpretation of the two-level sticks. The probability of transferring from hidden state _k_ to _l_ is equal to the sum of lengths of sticks mapped to the _l_ th component on the top level in the _k_ th DP. This is indicated by **_c_** and we have, 



To carry out the calculation, a solution in [16] suggests maintaining a set of auxiliary indicators **_s_** for local lower bound of _zi_ . _si_ is the indicator towards the second level sticks. Hence triplet ( _zi, si_ +1 _, czi,si_ +1 ) describes the hidden state transferring from the _i_ th to the _j_ th item in the sequence. We keep tracks of the following variables, 



Now that all parameters to be recorded are ready, we perform variational inference by taking derivative of the log likelihood and update through each set of factorized components. 

Updating _q_ ( **_z_** ). _q_ ( _zi_ ) is given by HMM forwardbackward, in which for the _k_ th component in the top level sticks, we have the following, 





To make the calculation tractable, the following approximation is introduced, as in [16], 



Now we have the marginal distribution for _q_ ( _zi_ ) that is given by forward-backward, noted as Γ _i_ ( _k_ ) , 



The marginal of _q_ ( _zi_ ) is vital for updating the variational parameters of emission function. 

Updating _q_ ( **_μ,_ Λ** ). This can be done since GaussianWishart is the conjugate prior to multivariate Gaussian [17] . Update for parameters is, 



Updating _q_ ( **_β_** ). To update the stick-breaking variational parameters, we can use the calculation in [18] and attain, 



Updating _q_ ( **_π_** ). In HDP-HMM, the second level sticks are indirect representations of the transition matrices, indicating the mixture components on the top level. By previous specification, we have, 



Updating _q_ ( **_c_** ). 



197 

Authorized licensed use limited to: Georgia Institute of Technology. Downloaded on February 27,2024 at 22:51:06 UTC from IEEE Xplore.  Restrictions apply. 

To update the second level indicator **_ξ_** , recall that it is the marginal probability conditioned on one hidden state transferring to certain second level stick. By the calculation we have, 



These are all it takes for the iteration of inference on HDPHMM in our problem. By this inference, we can simulate the events in a basketball game to forecasting the overcome. To verify the applicability of this model to all games, we played it in 1230 matches. The data for all games in the 2016 season of the NBA were downloaded from the SportVU website. 

## IV. EXPERIMENTS & RESULTS 

We present the results of the computation of the methods for all games played by trajectory data in the 2016 season of the National Basketball Association. The NBA play-byplay data and trajectory data were both obtained from www. sportvu.com. 

In order to demonstrate the outperformance of the HDPHMM model for the basketball outcome prediction, we compare the HDP-HMM model with other models that frequently applied for this task, such as Naive Bayes (NBayes), Logistic Regression (LRegression), Neural Networks (NNetwrks). The accuracies of different methods are shown in Figure 3. When these classic machine learning methods applied to our data, they showed the different forecasting overcome. 



Figure 3. The accurry of different models affected by the games data sets 

As we can see, at the beginning, the accuracy of each model increases with the number of matches. In particular, the HDP-HMM and logistic regression are two of the best predictive models at each gradation. When the 

number of games played as a training set reached 50, the prediction efficiency of each model could achieve optimally. The LRegression and the NBayes have a prediction rate above 70%, which means the predictions are very successful. Nevertheless, inference on HDP-HMM with multivariate Gaussian emission worked well on the progression of a basketball match. Therefore, the accuracy of our model is better than the others. The achieved accuracy of the proposal is of 76%, which is the highest probability of the forecasting the outcome at present. 

## V. CONCLUSION 

Rather than other methods that incorporate transitions between a coarse and ne-grained approach or use basic basketball statistics and score, we utilize the full trajectory data of both offensive and defensive players. In this way, we can construct a hidden Markov chain for each round in the game to simulate the match and produce outcome forecasts of a quality comparable to that of other approaches. Owing to the powerful nonparametric nature of determining a number of mixture components in HDP, we can work with neat quantication models extracted from the process of the whole basketball game using HDP-HMM. The results showed that the purposed method indeed yielded excellent performance and the accuracy of the forecast was above 75%. As far as basketball match simulation is concerned, more work has to be done, with an emphasis on making the transitional probabilities conditional on the point spread and the game time. 

## ACKNOWLEDGMENT 

The research work described herein was funded by the Science and Technology Planning Project of Guangdong Province (No. 2016B010124012, 2016B090920095). 

## REFERENCES 

- [1] J. Gudmundsson and M. Horton, “Spatio-temporal analysis of team sports,” _ACM Computing Surveys (CSUR)_ , vol. 50, no. 2, p. 22, 2017. 

- [2] H. O. Stekler, D. Sendor, and R. Verlander, “Issues in sports forecasting,” _International Journal of Forecasting_ , vol. 26, no. 3, pp. 606–621, 2010. 

- [3] T. A. Zak, C. J. Huang, and J. J. Siegfried, “Production efficiency: The case of professional basketball,” _Journal of Business_ , vol. 52, no. 3, pp. 379–392, 1979. 

- [4] H. Stern, “A brownian motion model for the progress of sports scores,” _Publications of the American Statistical Association_ , vol. 89, no. 427, pp. 1128–1134, 1994. 

- [5] P. H. Kvam and J. S. Sokol, “A logistic regression/markov chain model for ncaa basketball,” _Naval Research Logistics_ , vol. 53, no. 8, pp. 788–803, 2006. 

- [6] D. Miljkovic, L. Gajic, A. Kovacevic, and Z. Konjovic, “The use of data mining for basketball matches outcomes prediction,” pp. 309–312, 2010. 

198 

Authorized licensed use limited to: Georgia Institute of Technology. Downloaded on February 27,2024 at 22:51:06 UTC from IEEE Xplore.  Restrictions apply. 

- [7] K. Shirley, “A markov model for basketball,” 09 2018. 

- [8] E. trumbelj, “Simulating a basketball match with a homogeneous markov model and forecasting the outcome,” _International Journal of Forecasting_ , vol. 28, no. 2, pp. 532–542, 2012. 

- [9] Y. W. Teh, M. I. Jordan, M. J. Beal, and D. M. Blei, “Hierarchical dirichlet processes,” _Publications of the American Statistical Association_ , vol. 101, no. 476, pp. 1566–1581, 2006. 

- [10] J. C. Wang, Y. S. Lee, Y. H. Chin, Y. R. Chen, and W. C. Hsieh, “Hierarchical dirichlet process mixture model for music emotion recognition,” _IEEE Transactions on Affective Computing_ , vol. 6, no. 3, pp. 261– 271, 2015. 

- [11] E. B. Fox, E. B. Sudderth, M. I. Jordan, and A. S. Willsky, “The sticky hdp-hmm: Bayesian nonparametric hidden markov models with persistent states,” _Arxiv Preprint_ , 2009. 

- [12] M. D. Hoffman, D. M. Blei, C. Wang, and J. Paisley, “Stochastic variational inference,” _Computer Science_ , vol. 14, no. 1, pp. 1303–1347, 2013. 

- [13] A. H. H. N. Torbati and J. Picone, “A doubly hierarchical dirichlet process hidden markov model with a nonergodic structure,” _IEEE/ACM Transactions on Audio Speech and Language Processing_ , vol. 24, no. 1, pp. 174–184, 2016. 

- [14] C. M. Bishop, _Pattern Recognition and Machine Learning (Information Science and Statistics)_ . SpringerVerlag New York, Inc., 2006. 

- [15] C. Wang, J. W. Paisley, and D. M. Blei, “Online variational inference for the hierarchical dirichlet process,” _Journal of Machine Learning Research_ , vol. 15, pp. 752–760, 2011. 

- [16] A. Zhang and J. Paisley, “Markov mixed membership models,” 2015. 

- [17] M. Everingham, A. Zisserman, C. K. I. Williams, L. V. Gool, M. Allan, C. M. Bishop, O. Chapelle, N. Dalal, T. Deselaers, and G. Dork, _The 2005 PASCAL Visual Object Classes Challenge_ . Springer Berlin Heidelberg, 2006. 

- [18] D. M. Blei and M. I. Jordan, “Variational inference for dirichlet process mixtures. bayesian anal 1:121-144,” vol. 1, no. 1, 2006. 

199 

Authorized licensed use limited to: Georgia Institute of Technology. Downloaded on February 27,2024 at 22:51:06 UTC from IEEE Xplore.  Restrictions apply. 


