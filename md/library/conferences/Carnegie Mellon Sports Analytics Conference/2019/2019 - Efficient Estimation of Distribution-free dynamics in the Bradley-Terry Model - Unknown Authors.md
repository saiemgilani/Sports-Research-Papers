<!-- source: library/conferences/Carnegie Mellon Sports Analytics Conference/2019/2019 - Efficient Estimation of Distribution-free dynamics in the Bradley-Terry Model - Unknown Authors.pdf -->

# **Efficient Estimation of Distribution-free dynamics in the Bradley-Terry Model** 

**Heejong Bong**<sup>_∗_</sup> **, Wanshan Li**<sup>_∗_</sup> **, Shamindra Shrotriya**<sup>_∗_</sup> Department of Statistics and Data Science Carnegie Mellon University Pittsburgh, PA 15213 `{hbong,wanshanl,sshrotri}@andrew.cmu.edu` 

## **Abstract** 

We propose a time-varying convex generalization of the original Bradley-Terry model. Our model directly captures the temporal dependence structure of the pairwise comparison data without explicit temporal distribution assumptions. This enables the modeling of discrete-time dynamic global rankings of _N_ distinct objects. Different choices of the convex penalization term provide a control on the degree of smoothing in the derived time-varying global rankings of the _N_ distinct objects. Furthermore this directly enables analysis on sparse time-varying pairwise comparison data. We also prove that a relatively weak condition is both necessary and sufficient to guarantee the existence and uniqueness of the solution of our model. We implement various convex optimization algorithms to efficiently estimate the model parameters under the _ℓ_<sup>2</sup> 2<sup>,</sup><sup>_ℓ_2, and</sup><sup>_ℓ_1convex penalization norms.</sup> We conclude by thoroughly testing the practical effectiveness of our model under both simulated and real world settings, including ranking 5 seasons of National Football League (NFL) team data. Our generalized time-varying Bradley-Terry model thus provides a useful minimalist benchmarking tool for other featurerich dynamic ranking models since it only relies on the time-varying pairwise comparison data between the _N_ distinct objects. 

## **1 Introduction and Prior Work** 

### **1.1 Pairwise Comparison Data and the Bradley-Terry Model** 

Pairwise comparison data is very common in daily life especially in cases where the goal is to rank several objects. Rather than directly ranking all objects simultaneously it is usually much easier and more efficient to first obtain results of pairwise comparisons. The pairwise comparisons can then be used to derive a _global_ ranking across all individuals in a principled manner. One such statistical model for deriving global rankings using pairwise comparisons was presented by statisticians R. A. Bradley and M. E. Terry in their classic 1952 paper [3], and thereafter commonly referred to as the Bradley-Terry model in statistical literature. A similar model was also studied by Zermelo dating back to 1929 [19]. The Bradley-Terry model is one of the most popular models to analyze paired comparison data due to its interpretable setup and computational efficiency in parameter estimation. The Bradley-Terry model along with its various generalizations has been studied and applied in various ranking applications across many broad domains. This includes the ranking of sports teams ([11],[5],[7]), scientific journals ([14],[15]), and the quality of several brands ([1],[13]). 

> _∗_ Equal contribution. This version is as submitted for CMSAC 2020 review with minor grammatical corrections and de-anonymization. All code to reproduce analysis in this paper can be accessed from: `https://github.com/shamindras/bradley-terry-convexopt` 

33rd Conference on Neural Information Processing Systems (NeurIPS 2019), Vancouver, Canada. 

In order to describe the original Bradley-Terry model [3], suppose that we have _N_ distinct objects, each with a (positive) score or index ( _si_ ) _i∈_ [ _N_ ] showing their power of competing with each other at a single point in time (static). This model assumes that the comparisons between different pairs are independent and the results of comparisons between a given pair, object _i_ and object _j_ , are independent and identically distributed as Bernoulli random variables, with success probability 



A common way to parameterize ( _si_ ) _i∈_ [ _N_ ] is to assume that _si_ = exp( _βi_ ), for all _i ∈_ [ _N_ ]. In this case, equation (1) is usually expressed as logit(P( _i_ beats _j_ )) = _βi − βj_ , where logit( _x_ ) := log 1 _−xx_<sup>.An</sup> important assumption in the original Bradley-Terry model is that comparisons of different pairs are independent. However, in practice such strong data independence assumptions are unlikely to hold, as discussed further in [2],[6],[4],[15]. A typical way to deal with such data dependence in the pairwise comparison scores ( _si_ ) _i∈_ [ _N_ ] is to use quasi-likelihood approaches [17],[15]. Fortunately under the setting of the original Bradley-Terry model [3] the log-quasi-likelihood and usual log-likelihood are the same, in terms of optimizing for the target parameters **_β_** = ( _β_ 1 _, · · · , βN_ ) as discussed further in [17]. 

### **1.2 The Time-varying (dynamic) Bradley-Terry Model** 

In many applications it is very common to observe paired comparison data spanning over multiple (discrete) time periods. A natural question of interest is then to understand how the _global_ rankings _change_ over time. For example in sports analytics the performance of teams often changes from season to season and thus explicitly incorporating the time-varying dependence into the model is crucial. In particular the paper [7] considers a state-space generalization of the Bradley-Terry model to modelling the sports tournaments data. In a similar manner bayesian frameworks for the dynamic Bradley-Terry model are studied further in [9]. Such dynamic analysis of paired comparison data is becoming increasingly important because of the rapid growth of openly available time-dependent paired comparison data. 

Our main focus in this paper is to tackle the problem of efficiently estimating the parameters in the time-varying Bradley-Terry model under a frequentist framework. Our frequentist approach allows us to assume a _distribution-free_ approach in the _changes in model parameters_ over time in order to perform a dynamic parameter estimation with minimal assumptions. Our proposed model relies only on the time-varying pairwise comparison data across the _N_ distinct objects. This is in contrast to more assumption-heavy recent frequentist dynamic Bradley-Terry models including [5]. The remainder of this paper discusses our model in detail and is organized as follows. First, we formulate our overall time-varying Bradley-Terry estimation requirement as a convex optimization problem under various penalty norms. We then describe the relatively weak necessary and sufficient conditions to guarantee uniqueness of our model solution. We proceed to apply various well known convex optimization algorithms to derive efficient estimation of time-varying parameters with provable computational convergence guarantees, exploiting specific structure of the convex penalty terms as applicable. We then provide two strategies to optimizing our penalization parameter, _λ_ , using both data-driven and heuristic approaches. Finally we conclude by applying our model on synthetic datasets and a real-world example including NFL data demonstrating the practical viability of the model as minimalist benchmarking tool for time-varying rankings. 

## **2 Our proposed Time-varying Bradley-Terry Model** 

In our time-varying frequentist setup of the Bradley-Terry model, we generalize the approach taken in the original Bradley-Terry paper [3] in estimating parameters of interest via maximizing the likelihood (or mimimizing negative likelihood) over the discrete observed time points _{_ 1 _,_ 2 _, . . . , T }_ =: [ _T_ ]. The parameters of interest, **_β_**<sup>(</sup><sup>_t_)</sup> _∈_ R<sup>_N_</sup> , are now given for each time point _t ∈_ [ _T_ ], for each of the _N_ distinct objects. We assume that the pairwise comparison between a given pair, object _i_ and object _j_ , at a given time point _t_ is determined by the corresponding parameter **_β_**<sup>(</sup><sup>_t_)</sup> so that 



2 

Given a **_β_**<sup>(</sup><sup>_t_)</sup> , by equation (2) we can derive the log-likelihood _ℓt_ ( **_β_**<sup>(</sup><sup>_t_)</sup> ) at each time _t ∈_ [ _T_ ]. As the size of data in each _t_ is much smaller than the global data, we might want to _smooth_ the parameter **_β_**<sup>(</sup><sup>_t_)</sup> across different time points and to leverage the dynamic structure in the global data. Our proposal is to include the penalization term _λ_<sup>�</sup><sup>_T_</sup> _t_ =1<sup>_−_1</sup><sup>_h_(</sup><sup>**_β_**(</sup><sup>_t_+1)</sup><sup>_−_</sup><sup>**_β_**(</sup><sup>_t_)) for some convex penalty function</sup><sup>_h_that</sup> can effectively smooth the estimation of parameter by penalizing large differences in subsequent time points. In summary, our proposed time-varying setup of the Bradley-Terry model can be framed as the following convex optimization problem: 



where _λ ≥_ 0, **_β_**<sup>(</sup><sup>_t_)</sup> _∈_ R<sup>_N_</sup> , and _h_ : R<sup>N</sup> _→_ R _≥_ 0 is the convex penalty function. 

First, we observe that if _T_ = 1 and _λ_ = 0 then equation (3) reduces to the same objective as the original (static) Bradley-Terry model [3]. As such our model represents a generalization of the original Bradley-Terry model to the time-varying setting. Furthermore we include an additional constraint, namely<sup>�</sup><sup>_N_</sup> _i_ =1<sup>_β_</sup> _i_<sup>(1)</sup> = 0 which sets the sum of the estimated parameters to 0 at the initial time point _t_ = 1. This artificial constraint is used to guarantee the existence and uniqueness of the global solution set in the convex formulation discussed further in section 3. Since we are only concerned with obtaining _relative_ global object rankings this constraint still maintains our ultimate goal and further ensures that equation (3) is invariant to constant shifts in the model parameters. In our project we consider 3 cases for the convex penalty function _h_ , namely _h_ = _∥·∥_ 1, _h_ = _∥·∥_ 2, and _h_ = _∥·∥_ 2<sup>2to allow for user flexibility in the degree of smoothing in the output global rankings</sup> depending on the underlying sparsity of the available pairwise comparison data. 

## **3 Existence and uniqueness of solution** 

The existence or the uniqueness of solutions for the model (3) is not guaranteed in general. This is an innate property of the original Bradley-Terry model [3]. As pointed out by Ford Jr. [8] the BradleyTerry model requires a sufficient amount of pairwise comparisons so that there is enough information of relative performance between any pair of two entries for parameter estimation purposes. For example, if there is an object which has never been compared to the others, there is no information which the model can exploit to assign a score for the object, so its derived rank could be arbitrary. In addition if there are several entries which have never outperformed the others then Bradley-Terry model would assign negative infinity for the performance of these entries, and we would not be able to compare among them for global ranking purposes. 

In 1957 Ford Jr. [8] discovered the necessary and sufficient conditions which guarantee the uniqueness of the solution in the original Bradley-Terry model. The two equivalent conditions are: 

**Condition** (1) **.** In every possible partition of the objects into two nonempty subsets, some object in the second set has been preferred at least once to some object in the first set 

**Condition** (2) **.** For each ordered pair ( _i, j_ ), there exists a sequence of indices _i_ 0 = _i, i_ 1 _, . . . , in_ = _j_ such that 



for _k_ = 1 _, . . . , n_ . 

We prove that these conditions can also be adapted to guarantee the uniqueness of the solution in our time-varying Bradley-Terry model. This is summarized in the following theorem. 

**Theorem 3.1.** _Given data {x_<sup>(</sup> _i,j_<sup>_t_)</sup><sup>_}i,j,tsatisfies the previous condition, let xi,j_= �</sup><sup>_T_</sup> _t_ =1<sup>_x_(</sup> _i,j_<sup>_t_)</sup><sup>_. If {xi,j}_</sup> _satisfies the condition above, then_ 

_1. If h is continuous and h_ ( _x_ ) _→∞ as x →∞, the solution_ **_β_**<sup>_⋆_</sup> _for_ (2) _is attainable in_ R<sup>_N×T_</sup> _; and_ 

_2. With squared-ℓ_ 2 _penalty, h_ = _∥·∥_ 2<sup>2</sup><sup>_, the uniqueness of solution classes for_(3)</sup><sup>_._</sup> 

Hence, in our proposed time-varying Bradley-Terry model we do not require the strong conditions [8] to hold at each time point, but simply require the _aggregated conditions_ in Theorem 3.1 to hold 

3 

overall. This is a quite weak data requirement in the sense that it is satisfied even when each object does not have pairwise comparisons with all other objects at every single time point. For example, even if one player did not play any game in a season, as long as we have a game record in another season (with at least one win and one loss respectively), we can assign a rank to this player in the missed season. This minimal data requirement for our proposed model is in our view a key advantage to other frequentist time-varying approaches which could be alternatively considered here. A typical such alternative frequentist time-varying approach would be to fit a separate Bradley-Terry model at each discrete time point and then ‘smooth’ the derived global rankings post-hoc. This could be done using kernel smoothing techniques over the _T_ time points. However, such an approach would require the stronger conditions in [8] to hold at _every time point_ rather than the much weaker aggregated conditions required for our model to hold in order for a unique solution. In this sense our model requires not only minimal assumptions on the time-varying dependence but also on the pairwise data information requirements between the _N_ distinct objects. 

## **4 Optimization Methods for Model Estimation** 

Since we have formulated our model as a convex optimization problem per equation (3), we discuss well known algorithms which can be used to efficiently estimate our time-varying model parameters **_β_**<sup>(</sup><sup>_t_)</sup> . More specifically we note that the objective function in equation (3) can be expressed as follows: 



where 



Since _g_ is convex differentiable and _H_ is convex for the convex penalty function _h_ : R<sup>N</sup> _→_ R _≥_ 0 then the proximal gradient descent method (PGD) is a natural optimization technique for this problem when using the _ℓ_<sup>2</sup> 2<sup>-norm for the smoothing penalty.In this case we can derive the closed form of the</sup> proximal operator and run PGD at an inexpensive computational cost. However in the case of other smoothing penalties such as using the _ℓ_ 1-norm or _ℓ_ 2-norm, the proximal operator for _h_ does not have a closed form thereby reducing the computational feasibility of the PGD technique. In such cases we resort to the Alternating Direction Method of Multipliers (ADMM) technique. In our optimization implementations we consider both fixed descent step sizes _si_ and also determined by the backtracking line search with the initial step size _s_ init. Below we separately detail the efficient closed form for the proximal operator with the _ℓ_<sup>2</sup> 2<sup>-penalty and discuss the computational feasibility under more general</sup> _ℓ_ 1-norm and _ℓ_ 2-norm smoothing penalties. 

### **4.1 Efficient PGD for** _ℓ_<sup>2</sup> 2<sup>**-penalty**</sup> 

The proximal operator for the step size _s >_ 0 and the smoothing penalty _H_ is defined as follows: 



Hence, we can decompose the optimization in the proximal operator into the marginal optimizations for _i_ = 1 _. . . N_ so that if **_β_**<sup>+</sup> = prox _s,H_ ( **_β_**<sup>_′_</sup> ), then 



Hence, _∇_ **_β_** _iFi_ = 0 if and only if 

4 

Hence by solving the linear system (9) for each _i_ = 1 _, . . . , N_ , we get the output of the proximal operator for the squared _ℓ_<sup>2</sup> 2<sup>-norm penalty.By exploiting the specific sparse</sup><sup>_tri-diagonal_structure of</sup> the linear system we can solve it in _O_ ( _n_ ) computations which is much more efficient that just using matrix inversion. 

Even though we can solve the proximal operator quite efficiently, we find that in practice the classical Newton’s method can be even more efficient. However, when _λ_ is close to 0, the numerical performance of Newton’s method would become a little bit unstable, so we still need PGD in cases where _λ_ is very small. For moderate _λ_ we recommend Newton’s method. 

### **4.2 ADMM for** _ℓ_ 1 **-penalty and** _ℓ_ 2 **-penalty** 

On the other hand, getting the proximal operator for general smoothing penalty functions is nontrivial. In particular the _l_ 1-norm and _l_ 2-norm penalty terms do not have a closed-form proximal solution and require nontrivial amount of computation to approximate the optimum. In these two cases, we can use ADMM (Alternating Direction Method of Multipliers), as detailed below for our setting. 

Let **_β_** := vec( **_β_**<sup>(1)</sup> _, · · · ,_ **_β_**<sup>(</sup><sup>_T_)</sup> ) _∈_ R<sup>_T N_</sup> be the vector of scores of all individuals at all time points. Define **_θ_** _∈_ R<sup>(</sup><sup>_T −_1)</sup><sup>_N_</sup> by _θt·N_ + _i_ = _µ_<sup>_t_</sup> _i_<sup>+2</sup> _− µ_<sup>_t_</sup> _i_<sup>+1</sup> for _i ∈_ [ _N_ ] _,_ 0 _≤ t ≤ T −_ 2. By introducing a matrix _A ∈_ R<sup>[(</sup><sup>_T −_1)</sup><sup>_N_]</sup><sup>_×T N_</sup> we can express **_θ_** as **_θ_** = _A_ **_µ_** and rewrite the optimization (3) as 



where **_ℓ_** _T_ ( **_β_** ) =<sup>�</sup><sup>_T_</sup> _t_ =1<sup>_ℓt_(</sup><sup>**_β_**(</sup><sup>_t_)) and ˜</sup><sup>_h_= �</sup><sup>_T_</sup> _t_ =1<sup>_−_1</sup><sup>_h_(</sup><sup>**_θ_**</sup><sup>_It_) with the index set</sup><sup>_It_=</sup><sup>_{i_:</sup><sup>_N_(</sup><sup>_t −_1) + 1</sup><sup>_≤_</sup> _i ≤ Nt}_ . The ADMM scheme can be written as 



The update of **_θ_** is simply the proximal operator of _h_<sup>˜</sup> . The update of **_β_** is a convex optimization problem of a well-behaved function with no constraints and can be solved by some basic methods, like Newton’s method. 

## **5 Tuning** _λ_ **(smoothing penalty parameter) in practical settings** 

In our convex formulation of the time-varying Bradley Terry model (3) we note that the penalty coefficient _λ ∈_ R _≥_ 0 is effectively a global smoothing parameter for the fitted **_β_**<sup>(</sup><sup>_t_)</sup> values between subsequent time periods under the various penalty norms. Increasing _λ_ , all else held constant, thus increases the penalty on the difference between subsequent **_β_**<sup>(</sup><sup>_t_)</sup> values over a single time period. This leads to **_β_**<sup>(</sup><sup>_t_)</sup> values (and hence the derived global rankings) becoming ‘smoothed’ together across time. 

Naturally the question remains on how to _tune λ_ in practical applications in a principled manner. This is a fundamentally challenging question since our proposed model is unsupervised i.e. the true **_β_**<sup>(</sup><sup>_t_)</sup> or score ( _si_ ) _i∈_ [ _N_ ] values are not directly observed. We note that in practice the end user of the time-varying Bradley Terry model typically seeks the global time-varying team rankings, rather than the individual fitted **_β_**<sup>(</sup><sup>_t_)</sup> coefficients used to derive pairwise comparisons. As such the usual approach of changing _λ_ to fit the **_β_**<sup>(</sup><sup>_t_)</sup> values and then assessing the associated impact on the time-varying global rankings changes is a rather _indirect approach_ to controlling the degree of smoothing in the sought after time-varying global rankings. We propose both a direct heuristic approch and a data-driven approach in tuning _λ_ in real world settings. We detail the approaches and the conditions under which they would be useful below. 

5 

### **5.1 Heuristic Approach** 

We propose a simple heuristic whereby the user controls the degree of smoothing in global rankings _directly_ by specifying a maximal ranking change parameter _α ∈_ [ _N_ ] over all _N_ teams and over all _T_ time periods. By specifying this global (integer) parameter _α_ we can search over a suitable finite grid of _λ ∈_ R<sup>+</sup> values to meet this user specified global maximum team rank change requirement. In this heuristic we note that the user simply specifies a positive integer _α_ indicating the maximum increase/decrease in global ranks for any team over all time periods. We claim that the user-specified _α_ parameter is much more intuitive for the end user to directly control the global ranking changes. Here _α_ is seen as a global smoothing parameter since controlling the maximum global rank change over all _T_ periods is effectively controlling smoothing across all local consecutive time periods as well. 

Furthermore, since _α_ here is integer-valued it is naturally capped at the total number of teams _N_ , since a team can’t globally change rankings by more than the total number of teams across any time period. However in practice it will be much lower than this and easier to prescribe by the end user based on reasonable domain knowledge of expected time-varying ranking movements. We acknowledge that this heuristic trades the subjectivity of choosing _λ_ for _α_ but that it controls for the degree of smoothing in global rankings directly from the users point of view. The limited choice of _α_ for the end user and the efficiency in grid-fitting _λ_ makes it effective to apply in practical situations where the user has suitable domain knowledge on maximal global ranking changes. 

### **5.2 Data Driven Approach - Sample Splitting and LOOCV (recommended)** 

Alternatively we propose a data-driven approach to tuning _λ_ when sufficient domain knowledge is not available for the end-user. First, we note that in ranking objects from pairwise comparisons, we want the time-varying Bradley-Terry model to sort objects by means of win rates. That is, a higher globally-ranked object should be more likely to win against a lower globally-ranked object. Hence, we choose _λ_ giving the best prediction on pair-wise _win rates_ . In prediction, leave-one-out crossvalidation (LOOCV) has been a provably successful model parameter tuning mechanism without the aid of human heuristics [10]. Given that we don’t observe the ranking values we briefly describe how we adapt LOOCV to our unsupervised time-varying Bradley-Terry model. We then propose several techniques to reduce computational cost for our LOOCV _λ_ -tuning approach. 

In general settings where we have independent and identically distributed (i.i.d) samples, LOOCV assesses the performance of a predictive model by holding out one of the i.i.d samples. In our case, each pairwise comparison can be considered an i.i.d. sample if we take the compared objects and the time point on which they are compared as covariates. Let ( _tk, ik, jk_ ) denote _k_ -th pairwise comparison where object _ik_ won against object _jk_ at time point _tk_ for _k_ = 1 _, . . . , N_ . Then, for a given smoothing penalty parameter _λ_ , LOOCV is adapted to our model as follows: 

1. For _k_ = 1 _, . . . , N_ , given _λ_ : 

   - (a) Solve (3) with _λ_ on the dataset where the _k_ -th comparison is held-out. 

   - (b) Calculate the negative log-likelihood (nll) of the previous solution to ( _tk, ik, jk_ ). 

2. Take the average of the negative log-likelihoods to obtain nll _λ_ as a loss in the predictive performance of time-varying Bradley-Terry model for given _λ_ on our dataset 

3. Choose the _λ_<sup>_∗_</sup> with the smallest nll _λ_ value overall 

Solving (3) with every candidate _λ_ , over a suitable finite grid of candidate values and on every hold-one-out dataset incurs heavy computational cost. To reduce this cost, we can approximate the exhaustive LOOCV with a stochastic estimate. The exhaustive LOOCV fits the model to every possible held-one-out data and takes their average. However, if we have a large number of pairwise comparisons, an average of much fewer losses makes tiny error. Hence, we can uniformly randomly sample a smaller number of matches to be held-out and obtain nll<sup>ˆ</sup> _λ_ efficiently. Also, we can quicken fitting on held-one-out data by giving the original estimate as an initial value. We assume that the parameter fitted on the entire dataset differs little to the fitted on held-one-out datasets. Hence, starting from the original estimate, optimizing functions could reach convergence much faster. These two speed-up techniques make LOOCV a practical and recommended option for time-varying BradleyTerry models with a large number of parameter values, and where there is limited domain knowledge available. 

6 

## **6 Experiments** 

### **6.1 Synthetic Data Generation** 

We can conduct simulation experiments in which we know the underlying global ranks of all entries by generating data from a synthetic process. Given the number of entries _N_ and the number of time points _T_ , the overall synthetic data generation process is as follows: 

1. For each _i ∈_ [ _N_ ], simulate **_β_** _i_<sup>_∗∈_R</sup><sup>_T_from a distribution of time-series.</sup> 

2. For each _i_ = _j_ and _t ∈_ [ _T_ ], generate _n_<sup>(</sup> _ij_<sup>_t_)fromsomedistributionandsimulate</sup><sup>_x_(</sup> _ij_<sup>_t_)by</sup> _x_<sup>(</sup> _ij_<sup>_t_)</sup><sup>_∼_Binom</sup> � _n_<sup>(</sup> _ij_<sup>_t_)</sup><sup>_,_1</sup><sup>_/{_1 + exp[</sup><sup>_β_</sup> _j_<sup>(</sup><sup>_t_)</sup> _− βi_<sup>(</sup><sup>_t_)]</sup><sup>_}_</sup> � _, x_<sup>(</sup> _ji_<sup>_t_)=</sup><sup>_n_(</sup> _ij_<sup>_t_)</sup><sup>_−x_(</sup> _ij_<sup>_t_).</sup> 

For the choice of distribution of **_β_** _i_<sup>_∗_’s in step 1, we use Gaussian process to generate</sup><sup>**_β_**</sup><sup>_∗_since they are</sup> widely used in applications and can generate **_β_**<sup>_∗_</sup> that are _smoothed_ path across time. For each _i ∈_ [ _N_ ], The generation of **_β_** _i_<sup>_∗∈_R</sup><sup>_T_from a Gaussian process GP(</sup><sup>_µi_(</sup><sup>_·_)</sup><sup>_, σi_(</sup><sup>_·, ·_)) includes three steps.</sup> 

1. Set the values of the mean process _µi_ ( _·_ ) at _t ∈_ [ _T_ ] and get mean vector **_µ_** _i ∈_ R<sup>_T_</sup> 

2. Set the values of the variance process _σi_ ( _·, ·_ ) at ( _s, t_ ) _∈_ [ _T_ ]<sup>2</sup> , to derive Σ _i ∈_ R<sup>_T ×T_</sup> . 3. Generate a sample **_β_** _i_<sup>_∗_from Normal(</sup><sup>**_µ_**</sup><sup>_i,_Σ</sup><sup>_i_).</sup> 

### **6.2 Synthetic Simulation Results** 

First we generate the parameter **_β_**<sup>_∗_</sup> via a Gaussian process using the method described in 6.1 for _N_ = 10 and _T_ = 10 (see appendix for more details). We can then compare the true **_β_**<sup>_∗_</sup> and **_β_**<sup>ˆ</sup> by different methods to see how effectively our formulation of time-varying Bradley-Terry Model fits the synthetic ground truth. The results are shown in Figure 1. 



<!-- Start of picture text -->
True β ∗ Win Rate Vanilla Bradley-Terry<br>0 . 8 Team0<br>β ∗ 20 00 .. 64 β ˆ 50 Team1Team2<br>− 2 0 . 2 − 5 Team3<br>− 4 2 4 6 8 10 0 . 0 2 4 6 8 10 − 10 2 4 6 8 10 Team4<br>T T T<br>Dynamic Bradley-Terry ℓ 2-square Dynamic Bradley-Terry ℓ 2 Dynamic Bradley-Terry ℓ 1 Team5<br>Team6<br>2 2 2<br>β ˆ 0 β ˆ 0 β ˆ 0 Team7<br>− 2 − 2 − 2 Team8<br>Team9<br>− 4 − 4 − 4<br>2 4 6 8 10 2 4 6 8 10 2 4 6 8 10<br>T T T<br>Rate<br>Win<br><!-- End of picture text -->

Figure 1: Comparisons of **_β_**<sup>_∗_</sup> and different solutions. From left to right: (first row) **_β_**<sup>_∗_</sup> , win rate, vanilla BT; (second row) **_β_**<sup>ˆ</sup> by _∥· ∥_ 2<sup>2with LOOCV,</sup><sup>_∥· ∥_2,</sup><sup>_∥· ∥_1.</sup><sup>_x_-axis:time points</sup> 

In Figure 1, we also include the paths of the simulated “win rate”, given by the proportion of games that each team wins at each time point, and the path of **_β_**<sup>ˆ</sup> estimated by vanilla Bradley-Terry model at each time point. By comparing these curves, we note that our models produce estimates **_β_**<sup>ˆ</sup> that recover the comprehensive global ranking of each team better than "win rate" and vanilla Bradley-Terry model, and meanwhile give more stable paths over time. In figures of **_β_**<sup>_∗_</sup> and **_β_**<sup>ˆ</sup> for _∥·∥_ 2<sup>2,</sup><sup>_∥·∥_2,</sup><sup>_∥·∥_1,</sup> we can verify that team 2 is almost always dominating and team 0 is maintaining the lowest position in the majority of the time points. However, we can also find some differences of **_β_**<sup>ˆ</sup> from **_β_**<sup>_∗_</sup> which comes from the smoothing property of our model. For instance, the estimated parameters of team 2 and team 0 by our model tend to have larger gaps with other teams, compared with the true **_β_**<sup>_∗_</sup> . 

7 

Another point illustrated by Figure 1 is that, different choices of the penalty function lead to different shapes of the solution. Specifically, the _ℓ_<sup>2</sup> 2<sup>norm produces the smoothest paths of</sup><sup>**_β_**, while the</sup><sup>_ℓ_1</sup> norm imposes a piecewise constant structure on the paths of **_β_** . In applications, the path of **_β_** could have various shapes. Therefore, our model is adaptive to different user requirements on the smoothed shape of **_β_** in different applications. 



<!-- Start of picture text -->
0 . 423<br>0 . 422<br>0 . 421<br>0 . 420<br>0 . 419<br>0 2 4 6 8 10<br>λ<br>nll<br>Averaged<br><!-- End of picture text -->

Figure 2: LOOCV curve of Dynamic Bradley-Terry model with _ℓ_ 2-square penalty. _x_ -axis: coefficient of the penalty, _y_ -axis: the averaged negative log-likelihood. The best _λ_<sup>_∗_</sup> is 4.25. 

Figure 2 shows the curve of LOOCV of our Dynamic Bradley-Terry model with _ℓ_ 2-square penalty. The curve shows a typical shape of CV curve for tuning parameter. The _λ_ with smallest nll _λ_ is _λ_<sup>_∗_</sup> = 4 _._ 25. For _ℓ_ 2 and _ℓ_ 1 penalty, since the LOOCV procedure takes much time, we currently just use _λ_ = 4 _._ 25. 

## **7 Application - NFL Data** 

In order to test our model in practical settings we consider ranking National Football League (NFL) teams over multiple seasons. Specifically we source 5 seasons of openly available NFL data from 2011-2015 (inclusive) using the `nflWAR` package [18]. Each NFL season is comprised of _N_ = 32 teams playing _T_ = 16 games each over the season i.e. _t ∈_ [16] in this case. This means that at each point in time _t_ the pairwise matrix of scores across all 32 teams is sparsely populated with only 16 entries. We fit our time-varying Bradley Terry model over all 16 rounds in the season using the _ℓ_<sup>2</sup> 2 convex penalty and tuning _λ_ using the LOOCV approach described in section 5.2. In order to gauge whether the rankings produced by our model are reasonable we compare our season ending rankings (fit over all games played in that season) with the relevant openly available NFL ELO ratings [12]. The top 10 season-ending rankings from each method across NFL seasons 2011-2015 are summarized in Table 1. 

Based on table 1 we observe that we roughly match between 6 to 9 of the top 10 ELO teams consistently over all 5 seasons. However we can see that there are often misalignment with specific ranking values across both ranking methods. For example in the 2014 season we can see that our rankings are reasonably well aligned and notably a match with Seattle being the number one ranked team by both methods. The 2012 season had slightly more misalignment comparatively across both methods. This is captured in the average ranking difference between ELO and our time varying Bradley-Terry model being 3.2 which is slightly higher than the 2014 season value of 1.9. We observe that the average differences across all seasons between ELO and the Bradley Terry model are uniformly positive indicating that ELO ranks the same teams higher than the Bradley-Terry model on average across all seasons. 

We note that it is difficult to interpret the differences in great further detail given that the underlying ranking methodologies are fundamentally different. In particular the NFL ELO ranking methodology uses both the pairwise scores between teams (similar to our time-varying Bradley Terry model) but also uses the location information of each game in the modeling process. In this sense we view the comparable top 10 ranking results as an encouraging indication of our model viability in this real world application. We thus view our time-varying Bradley Terry model as a useful _benchmarking_ 

8 

||**20**|**11**|**20**|**12**|**20**|**13**|**20**|**14**|**20**|**15**|
|---|---|---|---|---|---|---|---|---|---|---|
|**ran**|||||||||||
||**ELO**|**BT**|**BLO**|**BT**|**ELO**|**BT**|**ELO**|**BT**|**ELO**|**BT**|
|1|GB|GB|NE|DEN|SEA|SF|SEA|SEA|SEA|CAR|
|2|NE|NO|DEN|NE|SF|CAR|NE|DEN|CAR|ARI|
|3|NO|NE|GB|SEA|NE|SEA|DEN|GB|ARI|KC|
|4|PIT|SF|SF|MIN|DEN|ARI|GB|NE|KC|SEA|
|5|BAL|PIT|ATL|SF|CAR|NE|DAL|DAL|DEN|MIN|
|6|SF|BAL|SEA|GB|CIN|DEN|PIT|PIT|NE|DEN|
|7|ATL|DET|NYG|IND|NO|NO|BAL|IND|PIT|CIN|
|8|PHI|ATL|CIN|HOU|ARI|CIN|IND|ARI|CIN|PIT|
|9|SD|PHI|BAL|WAS|IND|IND|ARI|BUF|GB|GB|
|10|HOU|SD|HOU|CHI|SD|SD|CIN|DET|MIN|DET|
|Av. Diff.|2.|6|3.|2|2.|6|1.|9|2.|8|



Table 1: Bradley-Terry vs. ELO NFL top 10 rankings. Blue: perfect match, yellow: top 10 match 

_tool_ for other feature-rich time-varying ranking models since (such as ELO) since our model simply relies on the minimalist time-varying score information for modeling. 

## **8 Conclusion** 

In this paper we propose a time-varying (dynamic) convex generalization of the original (static) Bradley-Terry model [3]. The underlying goal of the model is to derive the _global_ ranking of _N_ distinct objects over _T_ discrete time periods in a principled statistical manner using observed pairwise comparison data at each time point _t ∈_ [ _T_ ]. Our proposed model directly captures the temporal dependence structure of the pairwise comparison data in the form of time-varying model parameters. These time-varying model parameters are modeled in a distribution-free frequentist manner in the form of a convex penalty term. The specific choice of convex penalty norm also acts as a ‘smoothing’ mechanism for the derived time-varying global rankings. In particular the convex penalty term also enables analysis on sparse time-varying pairwise comparison data, which is common in many practical settings including sports analytics. 

From a theoretical perspective we prove that a relatively weak condition is necessary and sufficient to guarantee the existence and uniqueness of the solution of our proposed time-varying Bradley-Terry model. This ensures that we fit using limited temporal distributional assumptions and also means that we require much less time-varying pairwise comparison data to derive our global rankings than other non-sparse time-varying frequentist ranking approaches. In order to tune the model penalty term _λ_ we propose both a heuristic and data-driven approach. This heuristic is driven by user preferences in directly setting the degree of smoothing in the final global rankings. Although subjective, this is computational efficient and viable when such user-domain knowledge applies. The data-driven approach uses a sample-splitting approach via leave-one-out cross validation (LOOCV) to derive optimal lambda across a held out set. Although computationally exhaustive, we discuss methods to optimize this further using random sampling and better initial seeding. From an algorithmic perspective we implement various well studied convex optimization algorithms to solve the model efficiently under the _ℓ_<sup>2</sup> 2<sup>,</sup><sup>_ℓ_2and</sup><sup>_ℓ_1penalization norms.This is done exploiting any specific structure</sup> in our proposed model under the chosen convex penalty norm for additional computational efficiency gain. 

We finally test the practical effectiveness of our model under both simulated and real world settings. In the latter case we separately rank 5 consecutive seasons of open National Football League (NFL) team data [18] from 2011-2015. Our NFL ranking results compare favourably to the well-accepted and feature rich NFL ELO model rankings [12]. We thus view our distribution-free time-varying Bradley-Terry model as a useful _benchmarking tool_ for other feature-rich time-varying ranking models since it simply relies on the minimalist time-varying score information for modeling. 

9 

## **References** 

- [1] Alan Agresti. _Categorical Data Analysis_ . Wiley Series in Probability and Statistics. WileyInterscience [John Wiley & Sons], New York, second edition, 2002. xvi+710. 

- [2] U. Böckenholt and W. R. Dillon. Modeling within-subject dependencies in ordinal paired comparison data. _Psychometrika_ , 62:411–434, 1997. 

- [3] Ralph Allan Bradley and Milton E Terry. Rank analysis of incomplete block designs: I. the method of paired comparisons. _Biometrika_ , 39(3/4):324–345, 1952. 

- [4] Manuela Cattelan. Models for paired comparison data: A review with emphasis on dependent data. _Statistical Science_ , 27(3):412–433, 2012. 

- [5] Manuela Cattelan, Cristiano Varin, and David Firth. Dynamic bradley–terry modelling of sports tournaments. _Journal of the Royal Statistical Society: Series C (Applied Statistics)_ , 62(1):135–150, 2012. 

- [6] R. Dittrich, R. Hatzinger, and W. Katzenbeisser. Modelling dependencies in paired comparison data: A log-linear approach. _Comput. Statist. Data Anal._ , 40:39–57, 2002. 

- [7] Ludwig Fahrmeir and Gerhard Tutz. Dynamic stochastic models for time-dependent ordered paired comparison systems. _Journal of the American Statistical Association_ , 89(428):1438– 1449, 1994. 

- [8] Lester R Ford Jr. Solution of a ranking problem from binary comparisons. _The American Mathematical Monthly_ , 64(8P2):28–33, 1957. 

- [9] Mark E. Glickman. Paired comparison models with time varying parameters. _Doctoral thesis_ , 2012. 

- [10] Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani. _An introduction to statistical learning_ , volume 112. Springer, 2013. 

- [11] Guido Masarotto and Cristiano Varin. The ranking lasso and its application to sport tournaments. _Ann. Appl. Stat._ , 6(4):1949–1970, 12 2012. 

- [12] Neil Paine. NFL Elo Ratings Are Back! `https://fivethirtyeight.com/features/ nfl-elo-ratings-are-back/` . Accessed: 2018-11-30. 

- [13] Filip Radlinski and Thorsten Joachims. Active exploration for learning rankings from clickthrough data. In _Proceedings of the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , KDD ’07, pages 570–579, New York, NY, USA, 2007. ACM. 

- [14] S. M. Stigler. Citation patterns in the journals of statistics and probability. _Statist. Sci._ , 9:94–108., 1994. 

- [15] C. Varin, M. Cattelan, and D. Firth. Statistical modelling of citation exchange between statistics journals. _Journal of the Royal Statistical Society, Series A (Statistics in Society)_ , 179(1):1–63, 2016. 

- [16] Ulrike von Luxburg. A tutorial on spectral clustering. _Statistics and Computing_ , 17(4):395–416, Dec 2007. 

- [17] R. W. M. Wedderburn. Quasi-likelihood functions, generalized linear models, and the gaussnewton method. _Biometrika_ , 61(3):439–447, 1974. 

- [18] Ronald Yurko, Samuel Ventura, and Maksim Horowitz. nflwar: A reproducible method for offensive player evaluation in football. _arXiv preprint arXiv:1802.00998_ , 2018. 

- [19] E. Zermelo. Die berechnung der turnier-ergebnisse als ein maximumproblem der wahrscheinlichkeitsrechnung. _Mathematische Zeitschrift_ , 29(1):436–460, Dec 1929. 

10 

## **9 Appendix** 

### **9.1 Proof of Theorem** 

Throughout this section, let _f_ denote the target loss function: 



**9.1.1 Uniqueness of the solution with squared-** _ℓ_ 2 **penalty** 

We can decompose the loss function with squared- _ℓ_ 2 penalty into two parts: 







Hence, both kinds of Hessians have zero column sums and so does the sum of them, i.e., the Hessian of the loss function. Let _H_ denote the Hessian of _f_ and _H_ ( **_β_** _i_<sup>(</sup><sup>_t_)</sup><sup>_,_</sup><sup>**_β_**</sup> _j_<sup>(</sup><sup>_s_)) denote each element of</sup><sup>_H_.</sup> Then, _H_ has a positive diagonal, and 



As _H_ ( **_β_** _i_<sup>(</sup><sup>_t_)</sup><sup>_,_</sup><sup>**_β_**</sup> _j_<sup>(</sup><sup>_t_))</sup><sup>_<_0 if</sup><sup>_x_(</sup> _ij_<sup>_t_)</sup><sup>_>_0 or</sup><sup>_x_(</sup> _ji_<sup>_t_), Condition (1) implies that</sup><sup>_H_can be regarded as a graph</sup> Laplacian for a connected graph. Following the classical proof of the property of graph Laplacian [16], _v_<sup>_T_</sup> _Hv_ = � _|Xij|_ ( _vi − vj_ )<sup>2</sup> _≥_ 0 _, i<j_ 

and Condition (1) guarantees that "=" is achieved if and only if _v_ = _c_ **1** . This proves the uniqueness up to constant shifts. 

### **9.1.2 Existence of solution** 

Because of its continuity, _h_ attains its minimum in R<sup>_T_</sup> . Since we still get an equivalent optimization after constant shifting _h_ , we can assume _h_ has minimum value 0 without loss of generality. Also, note that _−ℓt_ ( **_β_** _t_ ) is non-negative: 



11 

Plugging in **_β_** = **0** , we get an upperbound for the minimum loss function _f_<sup>_⋆_</sup> : 



As _f_ is continuous, it suffices to show that the level set with<sup>�</sup><sup>_N_</sup> _i_ =1<sup>**_β_**</sup> _i_<sup>(1)</sup> = 0 is bounded so that it is compact. 

We get an upper-bound on the extent to which **_β_**<sup>(</sup><sup>_t_)</sup> ’s are dispersed in the level set: 

and 



_T_ where **_β_** = _T_<sup><u>1</u></sup> � _t_ =1<sup>**_β_**(</sup><sup>_t_).</sup> Then, 



Hence, under the level set, 



and if<sup>�</sup><sup>_T_</sup> _t_ =1<sup>_x_(</sup> _ij_<sup>_t_)= 0 then</sup> **_β_** _j −_ **_β_** _i_ is upperbounded. By Condition (2) and the constraint<sup>�</sup><sup>_N_</sup> _i_ =1<sup>**_β_**</sup> _i_<sup>(1)</sup> = 0, now every elements of **_β_** in the level set are bounded. This proves the existence part of the theorem. 

### **9.2 Synthetic Simulation Results** 

First we generate the parameter **_β_**<sup>_∗_</sup> via a Gaussian process. For each 1 _≤ i ≤ N_ , the value of the mean process is set to be _ci_ **1** _∈_ R<sup>_T_</sup> with _ci_ a random sample from standard Normal, and the covariance matrix is set to be a Toeplitz matrix _G_ whose entry is given by _Gs,t_ = 1 _− T_<sup>_−_1</sup><sup>_/_2</sup> _|s − t|_<sup>1</sup><sup>_/_2</sup> . Then we generated the pairwise comparison data from **_β_**<sup>_∗_</sup> with _n_<sup>(</sup> _ij_<sup>_t_)= 5 for every</sup><sup>_i_=</sup><sup>_j_and</sup><sup>_t ∈_[</sup><sup>_T_]</sup> and solved (2) by different methods. 

12 

### **9.3 Statistical analyses** 

### **9.3.1 Oracle inequality** 

Suppose that an oracle gives the probability _p_<sup>(</sup> _ij_<sup>_t_)with which team</sup><sup>_i_wins team</sup><sup>_j_at time point</sup><sup>_t_.</sup> 

### **oracle loss function:** 



**oracle estimator:** 



**objective for statistical analyses:** 

1. probabilistic bound on _f_<sup>_⋆_</sup> ( **_β_**<sup>ˆ</sup> ) _− f_<sup>_⋆_</sup> ( **_β_**<sup>_∗_</sup> ) 

2. probabilistic bound on _∥_ **_β_**<sup>ˆ</sup> _−_ **_β_**<sup>_⋆_</sup> _∥_ ( _∥· ∥_ 2 or _∥· ∥∞_ ) 

### **9.3.2 Consistency in ranking** 

After we get probabilistic bound on _∥_ **_β_**<sup>ˆ</sup> _−_ **_β_**<sup>_∗_</sup> _∥_ , under an assumption on a lower bound for _|_ **_β_**<sup>_⋆_(</sup> _i_<sup>_t_)</sup> **_β_**<sup>_⋆_(</sup> _j_<sup>_t_)</sup><sup>_|_, consistency in ranking in terms that</sup> 

_i −_ 



from Bradley-Terry score would be easily get. 

We might need arguments or references on nice properties of ranking from **_β_**<sup>_⋆_</sup> . 

### **9.3.3 Consistency in rank change detection** 

We might need assumptions on a lower bound for _|_ **_β_**<sup>_⋆′_</sup> _i_<sup>(</sup><sup>_t_)</sup><sup>_−_</sup><sup>**_β_**</sup><sup>_⋆′_</sup> _j_<sup>(</sup><sup>_t_)</sup><sup>_|_while</sup><sup>**_β_**</sup><sup>_⋆_</sup> _i_<sup>_′_(</sup><sup>_t_) is a derivative of</sup> **_β_**<sup>_⋆_</sup> _i_<sup>(</sup><sup>_t_) as a function of time</sup><sup>_t_.</sup> 

13 


