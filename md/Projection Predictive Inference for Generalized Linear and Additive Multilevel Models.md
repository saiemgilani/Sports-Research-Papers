<!-- source: Projection Predictive Inference for Generalized Linear and Additive Multilevel Models.pdf -->

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 

# **Projection Predictive Inference for Generalized Linear and Additive Multilevel Models** 

### **Alejandro Catalina** 

alejandro.catalina@aalto.fi 

_Helsinki Institute for Information Technology, HIIT Department of Computer Science Aalto University 02150, Espoo, Finland_ 

### **Paul Bürkner**<sup>∗</sup> 

paul.buerkner@gmail.com 

_Cluster of Excellence SimTech University of Stuttgart 70049, Stuttgart, Germany_ 

### **Aki Vehtari** 

aki.vehtari@aalto.fi 

_Helsinki Institute for Information Technology, HIIT Department of Computer Science Aalto University 02150, Espoo, Finland_ 

## **Abstract** 

Projection predictive inference is a decision theoretic Bayesian approach that decouples model estimation from decision making. Given a reference model previously built including all variables present in the data, projection predictive inference projects its posterior onto a constrained space of a subset of variables. Variable selection is then performed by sequentially adding relevant variables until predictive performance is satisfactory. Previously, projection predictive inference has been demonstrated only for generalized linear models (GLMs) and Gaussian processes (GPs) where it showed superior performance to competing variable selection procedures. In this work, we extend projection predictive inference to support variable and structure selection for generalized linear multilevel models (GLMMs) and generalized additive multilevel models (GAMMs). Our simulative and real-word experiments demonstrate that our method can drastically reduce the model complexity required to reach reference predictive performance and achieve good frequency properties. 

## **1. Introduction** 

Variable selection is an important aspect of statistical and predictive modelling workflows, for example, when understanding a model’s predictions is important, or where there is a cost associated to collecting new data. From the perspective of predictive performance, one goal of variable selection is to find the smallest subset of variables in a dataset yielding comparable predictive performance to the full model containing all the available variables. In this context, we assume that there might be variables with true non-zero coefficients that we cannot properly detect due to scarce data or the presence of a highly complex correlation structure. 

> ∗. Research done while in Aalto University as a postdoctoral researcher. 

1 

Catalina, Bürkner and Vehtari 

In this paper, we substantially generalize projection predictive inference to perform variable selection and model structure selection in generalized linear multilevel models (GLMMs) (McCulloch, 2003; Gelman et al., 2013) and generalized additive multilevel models (GAMMs) (Hastie and Tibshirani, 1986; Verbyla et al., 1999). Both types of models are widely used across the quantitative sciences, for instance, in the social and political sciences (e.g. poll or elections data whose measurements are organized in regions or districts with multiple levels), or in the physical sciences (e.g., meteorological or medical data). 

Projection predictive inference (Piironen et al., 2020b) is a general Bayesian decision theoretic framework that separates model estimation from decision. Given a reference model on the basis of all variables, it aims at replacing its posterior _𝑝_ ( _𝜆_ ∗ | D) with a constrained projection _𝑞_ ⊥( _𝜆_ ). This projection is solved so that its predictions are as close as possible to the reference model’s predictions. The uncertainties in the reference model related to the excluded model parts are also projected and thus partially retained in the projection. 

In the context of variable selection, one typically constrains the projection to a smaller subset of variables where the excluded variables have their coefficients fixed at zero. Then, the projection procedure sequentially projects the posterior onto an incremental subspace, until all the variables have entered the projection. At each step, the method selects the variable that most decreases the Kullback-Leibler (KL) divergence from the reference model’s predictive distribution to that of the projection model, a procedure known as forward search. This forms a _solution path_ for the variables into the projection. This approach has been shown to provide better performance than state-of-the-art competitors (Piironen and Vehtari, 2017a; Piironen et al., 2020b; Pavone et al., 2020; Piironen and Vehtari, 2016). Piironen and Vehtari (2017a) demonstrate that, when using the projection approach, overfitting in the model space search is very small compared to other stepwise procedures and that, even in huge model spaces, the selected submodel has similar predictive performance to the reference model. 

Previously, projection predictive inference has been used to perform variable selection only in generalized linear models (GLMs) (Piironen et al., 2020b) and Gaussian processes (GPs) (Piironen and Vehtari, 2016). However, the existing projection solutions do not directly translate to GLMMs or GAMMs because, without further restrictions, the projection is not identifiable for these models (Bickel and Doksum, 1977), that is, there is not a unique solution to the projection. In this paper we extend the projection predictive inference to GLMMs and GAMMs. In Figure 1 we showcase a broader picture of the different types of models that are now supported in our framework, starting from basic GLMs to very complex GAMMs. Along them, we show examples of equations for these kind of models and their correspondence to R formula syntax, which is an easy way of expressing complex models. 

Specifically, our contributions include: 

- Discussing the identifiability issue for projecting to GLMMs and GAMMs. 

- Extending projection predictive inference to support GLMMs and GAMMs by performing a Laplace approximation to the marginal likelihood of the projection. 

- Performing extensive simulations and real data experiments that validate the working of our method. 

- Implementing our proposal in the open source projpred R package for projection predictive inference (Piironen et al., 2020a). 

2 

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 



<!-- Start of picture text -->
Generalized Linear Multilevel Model<br>y ∼ Poisson(exp( η ))<br>η =  α  + hum β 1 + temp β 2 +  αj  + temp β 2 j<br>Generalized Linear Model count ∼ 1 + hum + temp + (1 + temp | month) Generalized Additive Multilevel Model<br>y ∼ Poisson(exp( η )) y ∼ Poisson(exp( η ))<br>η =  α  + hum β 1 + temp β 2 Generalized Additive Model η =  α  + hum β 1 +  f 1 j (temp)<br>count ∼ 1 + hum + temp y ∼ Poisson(exp( η )) + f 2(temp ,  hum) +  αj  + hum β 1 j<br>η =  α  + hum β 1 +  f 1(temp) +  f 2(temp ,  hum) count ∼ 1 + hum + s(temp, by = month)<br>count ∼ 1 + hum + s(temp) + s(temp, hum) + s(temp, hum) + (1 + hum | month)<br>+<br>s(x)<br>|g) +<br>+(u s(x)<br>g)<br>|<br>(u<br>+<br><!-- End of picture text -->

Figure 1: Different types of models supported by projpred now (previously only generalized linear models) and their relationships. We showcase math and R formula correspondence in color-coded terms. 

|Reference model|Forward search|Solution path|Projections|
|---|---|---|---|
|`count` _∼_`hum`<br>`+ s(temp)`<br>`+ (1 + temp | month)`|`count` _∼_`s(temp)`<br>. . .<br>`+ hum`<br>. . .<br>`+ (1 | month)`<br>. . .<br>`+ temp`<br>. . .<br>`+ (temp | month)`|`1.`<br>`s(temp)`<br>`2.`<br>`hum`<br>`3.`<br>`(1 | month)`<br>`4.`<br>`temp`<br>`5.`<br>`(temp | month)`|Optimal projection<br>`count` _∼_`s(temp)`<br>`+ hum`<br>`+ (1 | month)`|



Figure 2: Projection predictive variable and structure selection workflow for an illustrative example on a BikeSharing data model. 

To give an illustration of our developed method’s application, consider the BikeSharing data. These data contain the hourly and daily count of rental bikes between 2011 and 2012 in London’s capital bikeshare system with the corresponding weather and season information. The main variables included are month, season, weather, temperature, humidity and windspeed. In Figure 2 we show the full projection predictive variable and structure selection for an illustrative reference model example for these data. A priori we assume all continuous variables are relevant for predictions and they may interact with all categorical variables. For illustrative purposes we have built a simple model that contains different types of terms for only a subset of all the included variables, namely hum, temp, month. We leave the remaining variables for a more in-depth analysis in the experiments in Section 5.2. Our approach finds a projection model with simplified structure that provides optimal predictive performance with respect to the reference model. 

## **2. Related methods** 

For GLMs, variable selection has been approached from different perspectives. Some methods (Breiman, 1995; Tibshirani, 1996; Fan and Li, 2001; Zou and Hastie, 2005; Candes and Tao, 2007) propose to deal with it by solving a penalized maximum likelihood formulation that enforces sparse solutions, while at the same time trying to select a subset of relevant variables (e.g. LASSO). These approaches suffer from confounding the estimation and selection of variables, often ending up selecting fewer variables than truly relevant in the data, as in the case of correlated covariates. For further information, see the comprehensive review by Hastie (2015). Similarly, Marra and Wood (2011) propose to add an additional penalty term to perform variable selection in GAMs, with similar 

3 

Catalina, Bürkner and Vehtari 

shrinkage capacity as ridge regression. Another set of methods (George and McCulloch, 1993; Raftery et al., 1997; Ishwaran and Rao, 2005; Johnson and Rossell, 2012; Carvalho et al., 2010) suggests imposing a sparsifying prior on the coefficients that favours sparse solutions. Nonetheless, these priors do not actually produce sparse posteriors, because every variable has a non-zero probability of being relevant. One can obtain a truly sparse solution by selecting only those variables whose probability of being relevant is above a certain threshold (Barbieri and Berger, 2004; Ishwaran and Rao, 2005; Narisetty and He, 2014), but this approach ignores the uncertainty in the variables below the threshold. 

Reference models have been used before for tasks other than variable selection, as in Afrabandpey et al. (2020), where the authors constrain the projection of a complex neural network to be interpretable (e.g., projecting onto decision trees). Closer to variable selection and related to our approach, Piironen and Vehtari (2016) use projection predictive inference and impose further constraints on the projection of a GP reference model to perform variable selection, given the identifiability issue of the direct projection. 

While some alternative methods for variable selection in GLMMs and GAMMs exist, they either only allow variable selection for population parameters but not group parameters (Groll and Tutz, 2012; Tutz and Groll, 2012) or, when trying to use Bayes factors (Kass and Raftery, 1995), are computationally infeasible due to combinatorial explosion as soon as there are more than just a few variables. To the best of our knowledge, there are no practically applicable competing methods available in the literature, and so we only focus on the absolute performance of our method. 

## **3. Projection Predictive Inference** 

### **3.1 Formulation of the KL projection** 

Because the domain of both models may be different, formulating the problem in terms of minimizing a discrepancy measure between _𝑝_ ( _𝜆_ ∗ | D) and _𝑞_ ⊥( _𝜆_ ) does not make sense. Instead, we minimize the KL divergence from the reference model’s predictive distribution to that of the constrained projection, which is not easy in its general form: 



where we have collapsed terms that don’t depend on _𝜆_ into _𝐶_ . Here, the expectations over _𝜆_ ∗ _, 𝑦_ ˜ | _𝜆_ ∗ _, 𝜆_ are over the posterior _𝑝_ ( _𝜆_ ∗ | D), the posterior predictive distribution _𝑝_ ( ˜ _𝑦_ | _𝜆_ ∗), and the constrained projection _𝑞_ ⊥ ( _𝜆_ ), respectively. 

In practice, we approximate the KL minimization by changing the order of the integration and optimization in E ˜ _𝑦_ | _𝜆_ ∗ (log E _𝜆_ ( _𝑝_ ( ˜ _𝑦_ | _𝜆_ ))). To make this feasible, Goutis (1998) propose to do the projection draw-by-draw, where we find a direct mapping from a posterior draw of the reference model to the projection’s constrained space. Piironen et al. (2020b) propose a further speedup by demonstrating that it is possible to solve the projection employing only a small subset of posterior draws or even representative points that can be found, for instance, by clustering. 

4 

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 

### **3.2 Variable and structure selection** 

A high level overview of the variable selection procedure of projective predictive inference includes the following steps (Piironen et al., 2020b): 

1. Cluster the draws of the reference model’s posterior. 

2. Perform forward search to determine the ordering of the terms for the projection. At each step include the term that most decreases the KL divergence between the reference model’s predictions and the projection’s. 

3. Sequentially, compute the projections adding one term at a time. 

For a more robust variable selection, we perform a leave-one-out (LOO) cross validation procedure through the model space. In this approach, we repeat the full forward search _𝑁_ times by performing the selection with _𝑁_ − 1 data points and leaving the remaining point as test point each time, resulting in _𝑁_ different solution paths. Instead of running the procedure for every observation, Vehtari et al. (2019) show that we can achieve a similarly robust selection by running the procedure only on a carefully selected subset of points based on their estimated Pareto- _𝑘_<sup>ˆ</sup> diagnostic. 

In GLMMs and GAMMs, we no longer perform variable but model structure selection, that is, select additive model components to which we refer to as _terms_ . In this context, a _term_ may refer to a single variable with a single coefficient, a group level term, corresponding to all the coefficients of the group’s levels, or a smooth term, corresponding to all the coefficients associated with the smooth basis functions. The structure selection involves the same steps as the variable selection only that variables are replaced by terms. 

### **3.3 Solving the projection for exponential family models** 

For GLMs with observation models in the exponential family (McCullagh and Nelder, 1989), projecting a draw _𝜆_ ∗ from the reference model’s posterior to the projection space _𝜆_ ⊥ in Equation (1) coincides exactly with maximizing its likelihood under the projection model. Given a new observation ˜ _𝑦𝑖_ , with expectation over the reference model _𝜇𝑖_<sup>∗= E ˜</sup><sup>_𝑦_|</sup><sup>_𝜆_</sup> ∗<sup>( ˜</sup><sup>_𝑦𝑖_), this reduces to (Piironen et al., 2020b):</sup> 



which does not depend on the dispersion parameter _𝜙_ , for some function _𝐵_ of the natural parameters _𝜉𝑖_ ( _𝜆_ ). 

The above projection holds for observation models other than Gaussian or link functions other than the identity, as long as they belong to the exponential family. In these cases, there is no closed form solution for the projection parameters, and we run iteratively reweighted least squares (IRLS), where at every iteration one computes a pseudo Gaussian transformation of each log likelihood L _𝑖_ as a second order Taylor series expansion centered at the projection’s prediction (McCullagh and Nelder, 1989; Gelman et al., 2013). 

5 

Catalina, Bürkner and Vehtari 

## **4. Projection Predictive Inference for GLMMs and GAMMs** 

### **4.1 Generalized Linear Multilevel Models** 

GLMMs (McCulloch, 2003; Gelman et al., 2013) jointly estimate both _global population_ and _group-specific_ parameters. This approach allows the model to _partially pool_ information across groups, which is particularly useful for the estimates of groups with few data points. In this case, we refer to multilevel structure as terms arising from the levels of a categorical variable and their interactions with other variables. 

Given a response variable _𝑦_ for a population design matrix _𝑋_ with group design matrix _𝑍_ , we can write a GLMM as _𝑦_ ∼ _𝜋_ ( _𝑔_ ( _𝜂_ ) _, 𝜙_ ), where _𝑔_ (·) is the inverse link function of the generalized family _𝜋_ , and _𝜙_ is its dispersion parameter. The only difference to a GLM comes in the linear predictor _𝜂_ = _𝑋𝛽_ + _𝑍𝑢_ , where _𝛽_ are the population parameters and we add the group parameters _𝑢_ ∼ _𝑝_ ( _𝑢_ | _𝜃_ ), which may depend on some hyper parameters _𝜃_ . The goal is to accurately estimate the model parameters ( _𝛽, 𝑢, 𝜙, 𝜃_ ). 

### **4.2 Generalized Additive Multilevel Models** 

GAMMs (Hastie and Tibshirani, 1986; Verbyla et al., 1999) add further complexity to GLMMs by introducing smooth terms, which are presented as a linear combination of non-linear basis functions. 

As for GLMMs, we can formulate the model as _𝑦_ ∼ _𝜋_ ( _𝑔_ ( _𝜂_ ) _, 𝜙_ ). In the case of generalized additive models (GAMs) without multilevel structure, the predictor _𝜂_ can be written as _𝜂_ =<sup>�</sup><sup>_𝐽_</sup> _𝑗_ =1<sup>_𝑓𝑗_(</sup><sup>_𝑋_), where</sup> each _𝑓 𝑗_ is a function of the predictor matrix _𝑋_ (in practice, each _𝑓 𝑗_ uses only a subset of columns of _𝑋_ ). These functions are usually represented via additive spline basis expansion _𝑓_ ( _𝑥_ ) =<sup>�</sup><sup>_𝐾_</sup> _𝑘_ =1<sup>_𝛾𝑘𝑏𝑘_(</sup><sup>_𝑥_)</sup> with B-splines _𝑏𝑘_ ( _𝑥_ ) (Eilers and Marx, 1996). To avoid overfitting, we can either penalize some summary of the spline basis coefficients, or equivalently write it as a GLMM by splitting up the evaluated spline basis function into an unpenalized null-space (appended into _𝑋_ ) and a penalized space (appended as group variables into _𝑍_ ) where the prior on _𝑢_ serves the same purpose (Wood, 2017). Standard multilevel terms of GLMMs can be combined with non-linear smooth terms of GAMs to form the even more powerful GAMM model class (Wood, 2017). However, as soon as smooth terms are added and translated to the GLMM framework, the resulting _𝑍_ matrix becomes much denser than in a standard GLMM, thus further complicating inference. 

### **4.3 Solving the projection for GLMMs** 

Without further constraints, even if its observation model belongs to the exponential family, the projection (1) is not identifiable for GLMMs (Bickel and Doksum, 1977; Lee and Nelder, 1996; Gelman et al., 2013). This means that, given the mean prediction of the reference model _𝜇𝑖_<sup>∗, there is</sup> no unique solution for the parameters in the projection model fitted to _𝜇𝑖_<sup>∗.</sup> 

6 

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 

To make the model identifiable and solve the projection, we propose to further restrict it by integrating out the group parameters _𝑢_ . The resulting likelihood can be written as: 



where _𝑢𝑖_ are the group parameters belonging to observation _𝑖_ and we have assumed conditional independence between datapoints given the group parameters. This integral cannot be evaluated in closed form. For simple models with a single group one can numerically integrate the above expression (employing Gaussian-Hermite quadrature) but this quickly becomes infeasible for higher dimensional problems. Maximizing this likelihood with respect to the model parameters, following Equation (2), gives the constrained projection. 

There are many references in the literature that focus on practical approaches to obtain suitable approximate maximum likelihood estimates for GLMMs (McCulloch, 1997; Bates et al., 2015; Lee and Nelder, 2001; Lee et al., 2006; Ogden, 2013; Booth and Hobert, 1999). For our purposes, it is essential to use an approximate solution that still provides a good proxy for the KL divergence minimising solutions to Equation (1). Some of the methods cited above provide accurate and reliable solutions but often at the expense of a higher computational cost (e.g., Ogden, 2013). 

In the statistics literature, one finds simpler approximations that would scale better for our case, such as the well known Restricted Maximum Likelihood Estimates (REML) (Lee and Nelder, 2001; Lee et al., 2006). This approach obtains a solution by dealing with the group parameters as _fixed_ data and appending them as an extension to the population parameters. One would then solve an augmented GLM. 

### **4.4 Laplace Approximation** 

The REML approach does not provide a tractable approximation to the log marginal likelihood obtained from Equation (3), which takes the form 



where _ℎ𝑖_ = log _𝑝_ ( _𝑦𝑖_ | _𝑔_ ( _𝜂𝑖_ ) _, 𝜙𝑖_ ) + log _𝑝_ ( _𝑢𝑖_ | _𝜃_ ) is the (unnormalized) log joint density. The integrals in the above equation do not exist in closed form except for models where _𝑝_ ( _𝑢_ | _𝜃_ ) is conjugate to the likelihood _𝜋_ . Even in those cases, if the dimensionality of _𝑢_ is not very small, the computation is still intractable. 

As a general purpose solution, we consider a first-order Laplace approximation to the integral (Ha, 2009; Barndorff-Nielsen and Cox, 1989; Bates et al., 2015). We split up the integration problem into sub-problems that are easier to solve. Given a value of _𝜃_ , we can find the conditional mode _𝑢_ ˜( _𝜃_ ) and conditional estimate _𝛽_<sup>˜</sup> ( _𝜃_ ) by solving the following optimization problem 



7 

Catalina, Bürkner and Vehtari 

as the parameters that maximize the likelihood. 

Usually, we express the conditional density on the _deviance scale_ : 



This optimization problem can be solved efficiently using Penalized Iteratively Re-weighted Least Squares (PIRLS), as implemented in the popular lme4 (Bates et al., 2015) package. At each iteration, PIRLS performs a Gauss-Newton iteration in the space of _𝑢_ and _𝛽_ . See Bates et al. (2015) for more details. 

˜ The second order Taylor series expansion of −2 log _ℎ_ at _𝑢_ ( _𝜃_ ) and _𝛽_<sup>˜</sup> ( _𝜃_ ) provides the Laplace approximation to the _profiled deviance_ . On the deviance scale, the Laplace approximation is a function of the so-called _discrepancy_ measure and takes a sum of squares form: 



where _𝜇_ = _𝑔_ ( _𝜂_ ( _𝑢, 𝜃, 𝛽_ )) is the inverse link transformation of the latent predictor _𝜂_ , and _𝑊_ is a diagonal matrix of weights. Optimizing this function with respect to _𝜃_ provides the maximum likelihood estimates of _𝛽, 𝜙_ by substituting _𝜃_ ML into _𝛽_<sup>˜</sup> ( _𝜃_ ) and solving for _𝜙_ in _ℎ_ ( _𝑢_ | _𝑦, 𝛽, 𝜃_ ML _, 𝜙_ ). Importantly, optimizing the Laplace approximation is a problem in the space of constrained _𝜃_ , which is usually small and therefore easy to solve efficiently. 

### **4.5 Solving the projection for GAMMs** 

The identifiability issue that exists in GLMMs is further aggravated by having a dense _𝑍_ matrix in GAMMs, which makes the likelihood in Equation (3) intractable to compute even in conjugate Gaussian models with a single smooth term. This also happens in GAMs without any multilevel structure. 

In order to make these models identifiable, one has to 1) impose a quadratic penalty on the coefficients of the basis functions (Wood, 2017), which also helps in avoiding overfitting, and 2) integrate out the group parameters and group smooth terms. Solving the resulting maximum likelihood equations has similar issues as in the plain GLMM case. Given that GAMMs can be represented as GLMMs, the same Laplace approximation is commonly used to obtain maximum likelihood estimates in these models (Wood, 2010, 2017). 

### **4.6 Computational cost** 

The computational budget of our approach is composed of the following components 

- Running PIRLS, i.e. solving the projection, for a given subset of terms. 

- Solving the same projection for a number draws. 

- Performing forward search to explore the model space. 

- Running LOO cross-validation for many data points. 

8 

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 

Table 1: Data generation process settings for the simulations. 

|Parameter|Description|Values|
|---|---|---|
|_𝐷_|Number of variables|5, 7, 10|
|_𝑉_|Percentage of_𝐷_as group parameters|0.33, 0.67, 1.0|
|_𝐾_|Number of grouping factors|1, 2, 3|
|_𝜌_|Correlation factor|0.0, 0.33, 0.67, 0.9|
|_𝐿_|Levels per grouping factor|5|
|_𝑁_|Number of observations|300|
|_𝜋_|Observation model|Gaussian, Bernoulli|
|_𝑠_|Sparsity|0.4|



Piironen et al. (2020b) demonstrate that a small number of posterior draws is sufficient to find a good solution path, which saves a lot of computation during the forward search. Nonetheless, running PIRLS for complex multilevel models is still expensive especially when done repeatedly for different posterior draws. 

Further, in our approach, we reduce the number of models to explore in forward search by considering only those that are sensible according to common modelling practices for GLMMs (Gelman and Hill, 2006). This means that we only consider a model with a certain group parameter if its population parameter has already entered the projection. Likewise, we only consider an interaction between two variables when both of them have already entered the projection separately. This saves the method from exploring many models that are not considered sensible in the first place. 

## **5. Experiments** 

We now turn to validating our method in both simulated experiments and real world datasets. 

### **5.1 Simulations** 

We first validate our method by running projection predictive variable and structure selection as implemented in projpred (Piironen et al., 2020a) on extensive simulations. We systematically test simple and more complex models with both an increasing number of grouping factors and variables. We also consider correlations between different coefficients per level within a grouping factor. The complete settings of the simulations are shown in Table 1. 

To reduce external noise, we fix the number of observations to 300, the number of levels in each grouping factor to 5 and the sparsity to 0 _._ 4 to make sure that some terms are irrelevant. For each simulation condition, we run 25 data realisations. 

9 

Catalina, Bürkner and Vehtari 

The complete data generation process, common for all observation models _𝜋_ , is given as 



for data points _𝑖_ = 1 _, . . . , 𝑁_ , variables _𝑑_ = 0 _, . . . , 𝐷_ , grouping factors _𝑘_ = 1 _, . . . , 𝐾_ , inverse link function _𝑔_ , and covariance matrix Σ _𝜎𝑔_ 2 _,𝜌_ with diagonal entries _𝜎𝑔_<sup>2and off diagonal elements</sup><sup>_𝜌𝜎_</sup> _𝑔_<sup>2.</sup> We collapse the intercept ( _𝑑_ = 0) into _𝛽_ , _𝑢_ , so that we have _𝐷_ + 1 dimensions by appending a column of ones to _𝑋_ . We choose the identity link function. We fix the mean and standard deviation hyper parameters for the intercept _𝜇 𝑓 , 𝜎_<sup>2</sup> _𝑓_<sup>to 0,20 respectively,for the main terms</sup><sup>_𝜇𝑏, 𝑓, 𝜎_</sup> _𝑏, 𝑓_<sup>2to 5,10</sup> respectively and for the group terms _𝜇𝑔, 𝜎𝑔_<sup>2to 0, 5 respectively.We choose large values to avoid</sup> simulating practically undetectable terms. 

We sample group terms following a two-step procedure: 

1. We first sample _𝐾_ means for all grouping factors from a _𝐷_ + 1 dimensional multivariate normal distribution as 

   - _𝜇𝑔𝑘_ ∼ MultivariateNormal( _𝜇𝑔, 𝜎𝑔_<sup>2</sup><sup>_𝐼_)</sup><sup>_._</sup> 

2. Then, for each level _𝑙_ and grouping factor _𝑘_ , we sample from a _𝐷_ + 1 dimensional multivariate normal (with mean _𝜇𝑔𝑘_ ) as 

_𝑢𝑙𝑘_ ∼ MultivariateNormal( _𝜇𝑔𝑘 ,_ Σ _𝜎𝑔_ 2 _,𝜌_ ) _._ 

We first focus on studying the predictive performance of the projections. We show the optimal size of the projection to reach the reference LOO Expected Log Predictive Density (ELPD) performance for Gaussian simulated data in Figure 3. We normalize this quantity by the total number of possible terms for each model. 

**The projections achieve optimal predictive performance.** From the predictive perspective, projpred aims at finding a projection with good performance independently of the underlying true model. The results show that the projection is able to discard on average 50% of the terms without losing performance. In the supplementary material we show these results for different sparsity factors. 

**The projections are smaller with higher correlation.** Including correlated terms into the projection would not improve its predictive performance, which results in redundant components that can be discarded. 

10 

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 



<!-- Start of picture text -->
rho = 0 rho = 0.33 rho = 0.67 rho = 0.9<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>1.00<br>0.75 D<br>0.50 5<br>7<br>0.25<br>10<br>0.00<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>0.33 0.67 1 0.33 0.67 1 0.33 0.67 1 0.33 0.67 1<br>Percentage of D as group effects<br>K = 1<br>K = 2<br>K = 3<br>Optimal size to reach reference ELPD (%)<br><!-- End of picture text -->

Figure 3: Optimal size for the projections to achieve the reference LOO performance (ELPD). Each column shows a different correlation factor. Each row shows a different number of grouping factors. We include 95% uncertainty interval for the size of the projection. 

**The projections are robust.** Even though the models become more and more complex by adding more variables and a higher proportion of group terms, the size of the optimal projection slightly decreases with respect to the total number of terms. This also applies to the number of grouping factors. 

We now turn our focus to study the selected group terms in the projections with regard to their true relevance. Even though it is not projpred’s goal to select all truly non-zero terms (but only all empirically relevant ones), it is still useful to see how projection predictive selection coincides with the known truth. We show these results for Gaussian data in Figure 4. Importantly, even though in some cases our method may miss relevant variables, it is able to find a projection with optimal performance with just a subset of all variables and group coefficients, as shown in Figure 3. 

To compute true and false positive rates, we decide which terms are relevant by looking at the ELPD improvement of each projection with respect to the previous one. For a varying threshold _𝑡_ ∈[0 _,_ 1], we select as relevant all terms whose projection’s ELPD improvement is above the _𝑡_ th quantile of all ELPD improvements. Then, we compare the selected terms against the ground truth. For models with only a few terms, the discretization implied by the selection of terms results in some straight jumps in Figure 4. 

**The number of variables** _𝐷_ **has a moderate effect.** By increasing the number of variables we introduce more estimates in the model that in turn makes the identification of the relevant terms harder. Then, as the dimension increases, the true positive rate decreases while returning more false positives. 

**The number of grouping factors** _𝐾_ **is the most significant factor.** Increasing the number of grouping factors in the data multiplies the number of total parameters to estimate. This, in turn, dilutes the individual contribution of each one and therefore makes its even more 

11 

Catalina, Bürkner and Vehtari 



<!-- Start of picture text -->
rho = 0 rho = 0.33 rho = 0.67 rho = 0.9<br>1.00<br>0.75<br>0.50<br>0.25 v<br>0.00 0.33<br>1.00 0.67<br>0.75 1<br>0.50<br>0.25 D<br>0.00<br>5<br>1.00<br>7<br>0.75 10<br>0.50<br>0.25<br>0.00<br>0.0 0.5 0.0 0.5 0.0 0.5 0.0 0.5<br>False positive rate<br>K = 1<br>K = 2<br>True positive rate<br>K = 3<br><!-- End of picture text -->

Figure 4: False against true positive rate in a Gaussian model for varying selection thresholds. Each column shows a different correlation factor. Each row shows a different number of grouping factors. We include 95% uncertainty interval for both true and false positive rates. Chance selection in dashed black lines. 

opaque. This is reflected in the figure as we look at the bottom row, where the true positive rate drops to above 75% for 10 variables. 

**The percentage of group terms** _𝑉_ **is important.** In the simulations, we go to the extreme case of having all possible population terms vary across all grouping factors, which, even though unrealistic, sets an interesting bar to the performance of the method. In this extreme case, the false positive rate reaches its maximum for all settings. Typically, though, only some terms vary across grouping factors, and usually different terms vary between different grouping factors. 

**High correlation** _𝜌_ **induces more false positives.** Lastly, we analyze the impact of the correlation. As the terms get more correlated, the chance of selecting an irrelevant one as relevant gets higher, and therefore the ratio of true and false positive rates worsens overall. 

We show further simulations for Bernoulli and Poisson models in the supplementary material. Furthermore, we also simulate more levels per grouping factor and sparsity thresholds. Results of those simulations indicate similar patterns and performance of our method to the results shown above. 

### **5.2 Real data experiments** 

We now turn to validating the performance of our method in real world datasets, including a Bernoulli 

### 5.2.1 Bernoulli classification model 

For the Bernoulli classification model we use the VerbAgg (Bates et al., 2015) dataset. This dataset includes item responses to a questionaire on verbal aggression, used throughout De Boeck and Wilson 

12 

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 

(2004) to illustrate various forms of item response models. It consists of 7584 responses of a total of 316 participants on 24 items. These items vary systematically in multiple aspects as captured by three covariates whose parameters may vary over participants. For the purpose of our study, we randomly draw 50 individuals and their responses to increase the difficulty of the selection. 

Following R’s formula syntax, we fit the reference model r2 ∼ btype + mode + situ + (btype + mode + situ | id), that includes btype, situ and mode as group parameters varying over participants. The full reference model contains 7 terms, counted as the simplest individual components of the model excluding the global intercept, namely btype, mode, situ, (btype | id), (mode | id), (situ | id) and (1 | id). 

We fit the reference model with a regularised horseshoe prior (with global scale 0 _._ 01) (Piironen and Vehtari, 2017b; Carvalho et al., 2010) with rstanarm (Goodrich et al., 2018) and run a leave-one-out (LOO) cross validated variable selection procedure (Piironen et al., 2020a; Vehtari et al., 2016). 

We show ELPD summaries and their standard error in Figure 5 for incremental projections. The red dash line shows LOO performance for the full reference model. 

The optimal projection threshold used by projpred (Piironen et al., 2020b) suggests including the first 6 terms, resulting in the model r2 ∼ btype + mode + situ + (btype + situ | id), effectively implying that almost all terms are relevant. However, the standard error increases for the last two terms, which can be explained by the correlations in the posterior, which may result in a slight unidentifiability issue for those parameters. For more accurate projections one could project more posterior draws or improve the robustness of the reference model (e.g., with some PCA-like approach). The complete sequence of models considered in the solution path is: 

1. r2 ∼ (1 | id), 

2. + btype, 

3. + (btype | id), 

4. + situ, 

5. + (situ | id), 

6. + mode, 

7. + (mode | id). 

### 5.2.2 Poisson GLMM model 

For a Poisson count data model we use the BikeSharing dataset (Fanaee-T and Gama, 2013). These data contain the hourly and daily count of rental bikes between 2011 and 2012 in London’s capital bikeshare system with the corresponding weather and season information. We only use the daily averaged dataset, with 731 observations for 2 years. It includes the following variables: _season_ , _month_ , _holiday_ , _weekday_ , _weather_ , _temp_ , _humidity_ , _windspeed_ and _count_ . 

We build a knowingly overly complicated model that includes very correlated group effects for different grouping factors, such as season, month or weather. Our reference model is count ∼ windspeed + temp + humidity + (windspeed + temp + humidity | month) + (windspeed + temp + humidity | weekday) + (windspeed + temp + humidity | weather) + (windspeed + temp + humidity | holiday) + (windspeed + temp + humidity | season). 

13 

Catalina, Bürkner and Vehtari 



<!-- Start of picture text -->
−500<br>−600<br>−700<br>−800<br>0 2 4 6 8<br>Number of terms in the projection<br>ELPD<br><!-- End of picture text -->

Figure 5: Summaries of incremental projections for VerbAgg dataset. 



<!-- Start of picture text -->
−100000<br>−1e+05<br>−150000<br>−200000<br>−2e+05<br>−250000<br>−3e+05 −300000<br>−350000<br>0 6 12 18 24 0 2 4 6 8 10<br>Number of terms in the projection Number of terms in the projection<br>ELPD ELPD<br><!-- End of picture text -->

(a) Summaries of incremental projections for GLMM (b) Summaries of incremental projections for GAMM model for BikeSharing dataset. model for BikeSharing dataset. 

Figure 6: Summaries for BikeSharing models 

We fit the reference model with a regularised horseshoe prior (with global scale 0 _._ 01) using rstanarm (Goodrich et al., 2018) and provide it as an input to projpred’s LOO cross-validated selection procedure. 

We show ELPD summaries for each incremental projection in Figure 6a. The suggested optimal projection by projpred’s heuristic method (Piironen et al., 2020a) is count ∼ temp + humidity + windspeed + (humidity + temp | month) + (1 | weather) + (1 | season), including only 8 terms out of 23. The rest of the variables add only a marginal improvement. 

14 

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 

### 5.2.3 Poisson GAMM model 

We now used the same data as in the example above to build a simpler GAMM reference model, for computational reasons, of the form count ∼ s(windspeed) + s(temp) + s(humidity) + (1 | month) + (1 | weekday) + (1 | weather) + (1 | holiday) + (1 | season), where we just added smooth terms for the main effects and group intercepts. Note that fitting GAMMs is usually more expensive and take longer time than plain GLMMs. 

We make use of rstanarm again to build this model with a normal prior and provide it as an input to projpred’s LOO-cross-validated selection. 

We show ELPD summaries for each incremental projection in Figure 6b. The suggested optimal projection by projpred’s heuristic method (Piironen et al., 2020a) is count ∼ s(temp) + s(humidity) + (1 | season) + s(windspeed) + (1 | month), including only 5 out of 9 terms. 

## **6. Discussion** 

In this work, we have extended projection predictive inference to variable and structure selection on more complex classes of models, namely GLMMs and GAMMs. For these models, the GLM projection solution cannot be directly translated as it would result in unidentifiable models. For these model classes, combining projpred with a Laplace approximation gives a good approximation that not only enables accurate variable selection but also scales well to larger number of variables and grouping factors. 

We have validated our proposal by performing extensive simulations that test the boundaries of our method in extreme settings. We also showed that our method works well in real world scenarios with highly correlated grouping factors. 

We leave the extension of our current framework to other models which do not belong to the exponential family for future work. In such cases, the KL minimization in Equation (1) does not coincide with maximum likelihood estimates anymore. 

## **Acknowledgements** 

We would like to thank Akash Dhaka, Kunal Gosh, Charles Margossian and Topi Paananen for helpful comments and discussions. We also acknowledge the computational resources provided by the Aalto Science-IT project. 

15 

Catalina, Bürkner and Vehtari 



<!-- Start of picture text -->
1.00 1.00<br>0.75 Sparsity 0.75<br>0<br>0.11 Levels<br>0.22<br>5<br>0.50 0.33 0.50<br>10<br>0.44<br>20<br>0.56<br>50<br>0.67<br>0.78<br>0.25 0.89 0.25<br>0.00 0.00<br>0.0 0.5 1.0 0.0 0.5 1.0<br>False positive rate False positive rate<br>True positive rate True positive rate<br><!-- End of picture text -->

(a) False against true positive rate in a Gaussian model (b) False against true positive rate in a Gaussian model for varying sparsity thresholds. We include 95% unfor varying number of levels. We include 95% uncercertainty interval for both true and false positive rates.tainty interval for both true and false positive rates. Chance selection in dashed black lines. Chance selection in dashed black lines. 

Figure 7: Additional results for more sparsity factors and number of levels per grouping factor. 

## **Appendix A. Further results for more sparisty thresholds** 

In this section we provide more results for Gaussian simulated data with group sparsity thresholds _𝑠_ = {0 _,_ 0 _._ 11 _, . . . ,_ 0 _._ 89}. To isolate the effect of the sparsity we fix the number of variables to _𝐷_ = 5 and _𝐾_ = 1 grouping factors. For a more complex setting, we allow all _𝐷_ = 5 variables to vary within the grouping factor. 

In Figure 7a we show the ROC curve for this experiment’s results. To trace each sparsity’s ROC curve we vary the selection threshold for relevant group effects. As we did in the main text, we decide which group effects are relevant by looking at the ELPD improvement of a projection with respect to the previous one after including a given group effect. For a selection threshold _𝑡_ , we select as relevant all group effects whose projection’s ELPD improvement is over the _𝑡_ th quantile of all ELPD improvements. This gives a curve starting at 0% true positive rate when _𝑡_ = 0, to 100% for _𝑡_ = 1 for every sparsity threshold. 

Nonetheless, the sparsity threshold inherently sets the portion of actually relevant group effects. As the sparsity increases, the number of relevant group effects gets lower, and therefore the false positives rate can only increase as we return more and more group effects as relevant. On the other hand, for low sparsity thresholds we have the opposite behaviour, as there are many actually relevant group effects, and therefore the false positive rate gets lower as we select more group effects. The most difficult setting corresponds to medium sparisty thresholds, and that is reflected in the figure with higher false positive rates. 

## **Appendix B. Further results for more number of levels** 

In this case we focus on studying the effect of larger number of levels in each grouping factor. We fix the number of variables _𝐷_ = 5 and _𝐾_ = 1 grouping factor. We allow only 0 _._ 33 portion of _𝐷_ = 5 total 

16 

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 

Table 2: Hyper parameters for the Bernoulli simulations. They are propagated to a constant vector of the corresponding value. 

|Parameter|Value|
|---|---|
|_𝜇𝑓_,_𝜎_<sup>2</sup><br>_𝑓_<br>_𝜇𝑏, 𝑓_,_𝜎_<sup>2</sup><br>_𝑏, 𝑓_<br>_𝜇𝑔_,_𝜎_<sup>2</sup><br>_𝑔_|0, 4<br>0, 2<br>0, 3|



variables to be group effects. We now vary the number of levels in {5 _,_ 10 _,_ 20 _,_ 50}. To avoid other factors to intervene, we simulate Gaussian observations. 

We show ROC curves for all choices of levels in Figure 7b. We use the same mechanism to decide relevant group effects and contrast them to the ground truth. In this case it’s clear that the number of levels is not inducing more false positives to be returned, rather affecting only the true positives rate and how quickly the method is able to get all of them right. 

## **Appendix C. Bernoulli simulations** 

Finally, we show optimal projection size and ROC curve results for Bernoulli simulated data following the same structure as in the main text. In this case we choose a logit link function. For non-Gaussian observation models there is an added challenge as the projection is computing a linear Gaussian model as an approximation to the non-Gaussian observation model. This increases the computational budget of the method and sometimes results in unstable projections, even though still resulting in good performance overall. 

On top of that, the hyper parameters we have used on the sampling procedure for Bernoulli data imply smaller coefficients (see Table 2). This is due the further complexity added by the link function, that usually causes extreme values for large effects. 

We follow the same analysis structure as in the main text. We first focus on the optimality of the projections and analyze the optimal projection size that the method suggests to achieve the reference performance. We show these results in Figure 8. 

**The projections achieve optimal predictive performance.** The results show that the optimal projection is able to discard on average 60% of the terms while achieving the reference predictive performance. This proportion of relevant terms is dependent on the sparsity threshold selected as analyzed in Section A. These results hold even for larger number of grouping factors. 

**The projections are smaller with higher correlation.** In presence of highly correlated variables the optimal projection is able to identify a smaller subset of relevant variables that achieve the reference predictive projection. As a result, the optimal size decreases as we increase the overall correlation. 

**The projections are robust.** Even as we increase the complexity of the reference models, the method is able to find optimal projections every time. The robustness of the results is indicated by 

Now, we analyze the performance of the method regarding the proper identification of the truly relevant simulated terms. We show these results in Figure 9. We employ the same method to compute true and false positive rates for these experiments as we did in the main text for Gaussian data. That 

17 

Catalina, Bürkner and Vehtari 



<!-- Start of picture text -->
rho = 0 rho = 0.33 rho = 0.67 rho = 0.9<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>1.00<br>0.75 D<br>0.50 5<br>7<br>0.25<br>10<br>0.00<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>0.33 0.67 1 0.33 0.67 1 0.33 0.67 1 0.33 0.67 1<br>Percentage of D as group effects<br>Figure 8: Optimal size for the projections to achieve the reference LOO performance (ELPD). Each<br>column shows a different correlation factor. Each row shows a different number of grouping factors.<br>We include 95% uncertainty interval for the size of the projection.<br>rho = 0 rho = 0.33 rho = 0.67 rho = 0.9<br>0.75<br>0.50<br>0.25 v<br>0.00 0.33<br>0.67<br>0.75 1<br>0.50<br>0.25<br>D<br>0.00<br>5<br>7<br>0.75<br>10<br>0.50<br>0.25<br>0.00<br>0.0 0.5 0.0 0.5 0.0 0.5 0.0 0.5<br>False positive rate<br>K = 1<br>K = 2<br>K = 3<br>Optimal size to reach reference ELPD (%)<br>K = 1<br>K = 2<br>True positive rate<br>K = 3<br><!-- End of picture text -->

Figure 8: Optimal size for the projections to achieve the reference LOO performance (ELPD). Each column shows a different correlation factor. Each row shows a different number of grouping factors. We include 95% uncertainty interval for the size of the projection. 

Figure 9: False against true positive rate in a Bernoulli model for varying selection thresholds. Each column shows a different correlation factor. Each row shows a different number of grouping factors. We include 95% uncertainty interval for both true and false positive rates. Chance selection in dashed black lines. 

18 

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 

is, for a varying threshold _𝑡_ ∈[0 _, . . . ,_ 1], we select as relevant those effects that imply an ELPD improvement over the _𝑡_ th quantile of all ELPD improvements after being included in the projection. 

**The number of variables** _𝐷_ **has a moderate effect.** Increasing the number of variables in the data has a direct effect on the complexity of the reference model. This is also reflected in our results, as the ratio of true vs false positive is better for smaller number of variables. Nonetheless, the overall performance stays quite close. 

**The number of grouping factors** _𝐾_ **is the most significant factor.** Increasing the number of grouping factors in the data multiplies the number of total parameters to estimate. As a result, the individual contribution of each parameter is diluted, which makes its identification even more opaque. In the figure we can clearly see how the ratio of true vs false positives rates gets closer to random choice as we increase the number of grouping variables. 

**The percentage of group terms** _𝑉_ **is important.** As we increase the number of terms that vary within grouping factors we expect the method to confound the relevance of each of them, as the variability of the data increases. We can see, in turn, that the method returns more false positives for higher proportions of group terms. 

**High correlation** _𝜌_ **induces more false positives.** Another important factor that induces more false positives is the correlation between terms. This adds further complexity to the identification of truly relevant terms and is clearly reflected in our results, as the ratio of true vs false positive rates worsens for increasing correlation factors. Even in the extreme unrealistic case of 0 _._ 9 correlation, the method still identifies around half of the truly relevant effects. 

In general, the method does a good job at obtaining optimal projections with the smallest possible subset of relevant terms that still achieves the reference performance. 

## **References** 

- Homayun Afrabandpey, Tomi Peltola, Juho Piironen, Aki Vehtari, and Samuel Kaski. A decisiontheoretic approach for model interpretability in Bayesian framework. _Machine Learning_ , 109 (9-10):1855–1876, Sep 2020. ISSN 1573-0565. doi: 10.1007/s10994-020-05901-8. URL http://dx.doi.org/10.1007/s10994-020-05901-8. 

- Maria Maddalena Barbieri and James O. Berger. Optimal predictive model selection. _The Annals of Statistics_ , 32(3):870–897, Jun 2004. ISSN 0090-5364. doi: 10.1214/009053604000000238. URL http://dx.doi.org/10.1214/009053604000000238. 

- Ole E. Barndorff-Nielsen and David Roxbee Cox. _Asymptotic techniques for use in statistics_ . London ; New York : Chapman and Hall, 1989. ISBN 0412314002. 

- Douglas Bates, Martin Mächler, Ben Bolker, and Steve Walker. Fitting linear mixed-effects models using lme4. _Journal of Statistical Software, Articles_ , 67(1):1–48, 2015. ISSN 1548-7660. doi: 10.18637/jss.v067.i01. URL https://www.jstatsoft.org/v067/i01. 

- Peter J Bickel and Kjell A Doksum. _Mathematical statistics: Ideas and concepts_ . San Francisco: Holden-Day, 1977. 

19 

Catalina, Bürkner and Vehtari 

- James G. Booth and James P. Hobert. Maximizing generalized linear mixed model likelihoods with an automated Monte Carlo EM algorithm. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 61(1):265–285, Feb 1999. ISSN 1467-9868. doi: 10.1111/1467-9868.00176. URL http://dx.doi.org/10.1111/1467-9868.00176. 

- Leo Breiman. Better subset regression using the nonnegative garrote. _Technometrics_ , 37(4):373–384, 1995. ISSN 00401706. URL http://www.jstor.org/stable/1269730. 

- Emmanuel Candes and Terence Tao. The dantzig selector: Statistical estimation when p is much larger than n. _The Annals of Statistics_ , 35(6):2313–2351, Dec 2007. ISSN 0090-5364. doi: 10.1214/009053606000001523. URL http://dx.doi.org/10.1214/009053606000001523. 

- Carlos M. Carvalho, Nicholas G. Polson, and James G. Scott. The horseshoe estimator for sparse signals. _Biometrika_ , 97(2):465–480, Apr 2010. ISSN 1464-3510. doi: 10.1093/biomet/asq017. URL http://dx.doi.org/10.1093/biomet/asq017. 

- Paul De Boeck and Mark Wilson. _Explanatory item response models: A generalized linear and nonlinear approach_ . Springer Science & Business Media, 2004. 

- Paul H. C. Eilers and Brian D. Marx. Flexible smoothing with B-splines and penalties. _Statistical Science_ , 11(2):89–121, May 1996. ISSN 0883-4237. doi: 10.1214/ss/1038425655. URL http://dx.doi.org/10.1214/ss/1038425655. 

- Jianqing Fan and Runze Li. Variable selection via nonconcave penalized likelihood and its oracle properties. _Journal of the American Statistical Association_ , 96(456):1348–1360, 2001. doi: 10.1198/016214501753382273. URL https://doi.org/10.1198/016214501753382273. 

- Hadi Fanaee-T and Joao Gama. Event labeling combining ensemble detectors and background knowledge. _Progress in Artificial Intelligence_ , pages 1–15, 2013. ISSN 2192-6352. doi: 10.1007/s13748-013-0040-3. URL [WebLink]. 

- Andrew Gelman and Jennifer Hill. _Data Analysis Using Regression and Multilevel/Hierarchical Models_ . Cambridge University Press, 2006. ISBN 9780511790942. doi: 10.1017/cbo9780511790942. URL http://dx.doi.org/10.1017/cbo9780511790942. 

- Andrew Gelman, John B. Carlin, Hal S. Stern, David B. Dunson, Aki Vehtari, and Donald B. Rubin. _Bayesian Data Analysis, Third Edition_ . Chapman & Hall/CRC Texts in Statistical Science. Taylor & Francis, 2013. ISBN 9781439840955. 

- Edward I. George and Robert E. McCulloch. Variable selection via Gibbs sampling. _Journal of the American Statistical Association_ , 88(423):881–889, Sep 1993. ISSN 1537-274X. doi: 10.1080/ 01621459.1993.10476353. URL http://dx.doi.org/10.1080/01621459.1993.10476353. 

- Ben Goodrich, Jonah Gabry, Imad Ali, and Sam Brilleman. rstanarm: Bayesian applied regression modeling via Stan., 2018. URL http://mc-stan.org/. R package version 2.17.4. 

- Christian P. Goutis, Constantinos Robert. Model choice in generalised linear models: A Bayesian approach via Kullback-Leibler projections. _Biometrika_ , 85(1):29–37, Mar 1998. ISSN 1464-3510. doi: 10.1093/biomet/85.1.29. URL http://dx.doi.org/10.1093/biomet/85.1.29. 

20 

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 

- Andreas Groll and Gerhard Tutz. Variable selection for generalized linear mixed models by l1penalized estimation. _Statistics and Computing_ , 24(2):137–154, Oct 2012. ISSN 1573-1375. doi: 10.1007/s11222-012-9359-z. URL http://dx.doi.org/10.1007/s11222-012-9359-z. 

- Il-Do Ha. _Maximum Likelihood Estimation Using Laplace Approximation in Poisson GLMMs_ , volume 16. The Korean Statistical Society, Korean International Statisical Society, 2009. 

- Trevor Hastie. _Statistical Learning with Sparsity_ . Chapman and Hall/CRC, May 2015. ISBN 9781498712170. doi: 10.1201/b18401. URL http://dx.doi.org/10.1201/b18401. 

- Trevor Hastie and Robert Tibshirani. Generalized additive models. _Statistical Science_ , 1(3):297–310, Aug 1986. ISSN 0883-4237. doi: 10.1214/ss/1177013604. URL http://dx.doi.org/10.1214/ ss/1177013604. 

- Hemant Ishwaran and J. Sunil Rao. Spike and slab variable selection: Frequentist and Bayesian strategies. _The Annals of Statistics_ , 33(2):730–773, Apr 2005. ISSN 0090-5364. doi: 10.1214/ 009053604000001147. URL http://dx.doi.org/10.1214/009053604000001147. 

- Valen E. Johnson and David Rossell. Bayesian model selection in high-dimensional settings. _Journal of the American Statistical Association_ , 107(498):649–660, Jun 2012. ISSN 1537-274X. doi: 10.1080/01621459.2012.682536. URL http://dx.doi.org/10.1080/01621459.2012.682536. 

- Robert E. Kass and Adrian E. Raftery. Bayes factors. _Journal of the American Statistical Association_ , 90(430):773–795, Jun 1995. ISSN 1537-274X. doi: 10.1080/01621459.1995.10476572. URL http://dx.doi.org/10.1080/01621459.1995.10476572. 

- Youngjo Lee and John A. Nelder. Hierarchical generalized linear models. _Journal of the Royal Statistical Society: Series B (Methodological)_ , 58(4):619–656, 1996. doi: 10.1111/j.2517-6161.1996. tb02105.x. URL https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/j.2517-6161. 1996.tb02105.x. 

- Youngjo Lee and John A. Nelder. Hierarchical generalised linear models: A synthesis of generalised linear models, random-effect models and structured dispersions. _Biometrika_ , 88(4):987–1006, Dec 2001. ISSN 1464-3510. doi: 10.1093/biomet/88.4.987. URL http://dx.doi.org/10.1093/ biomet/88.4.987. 

- Youngjo Lee, John A. Nelder, and Yudi Pawitan. _Generalized Linear Models with Random Effects_ . Chapman and Hall/CRC, Jul 2006. ISBN 9780429144714. doi: 10.1201/9781420011340. URL http://dx.doi.org/10.1201/9781420011340. 

- Giampiero Marra and Simon N. Wood. Practical variable selection for generalized additive models. _Computational Statistics & Data Analysis_ , 55(7):2372–2387, Jul 2011. ISSN 0167-9473. doi: 10.1016/j.csda.2011.02.004. URL http://dx.doi.org/10.1016/j.csda.2011.02.004. 

- Peter McCullagh and John A. Nelder. _Generalized Linear Models_ . Springer US, 1989. ISBN 9781489932426. doi: 10.1007/978-1-4899-3242-6. URL http://dx.doi.org/10.1007/ 978-1-4899-3242-6. 

21 

Catalina, Bürkner and Vehtari 

- Charles E. McCulloch. Maximum likelihood algorithms for generalized linear mixed models. _Journal of the American Statistical Association_ , 92(437):162–170, Mar 1997. ISSN 1537-274X. doi: 10.1080/01621459.1997.10473613. URL http://dx.doi.org/10.1080/01621459.1997. 10473613. 

- Charles E. McCulloch. Generalized linear mixed models. _NSF-CBMS Regional Conference Series in Probability and Statistics_ , 7:i–84, 2003. ISSN 19355920, 23290978. URL http: //www.jstor.org/stable/4153190. 

- Naveen Naidu Narisetty and Xuming He. Bayesian variable selection with shrinking and diffusing priors. _The Annals of Statistics_ , 42(2):789–817, Apr 2014. ISSN 0090-5364. doi: 10.1214/ 14-aos1207. URL http://dx.doi.org/10.1214/14-aos1207. 

- Helen Ogden. A sequential reduction method for inference in generalized linear mixed models. _arXiv preprint 1312.1903v2_ , 2013. 

- Federico Pavone, Juho Piironen, Paul-Christian Bürkner, and Aki Vehtari. Using reference models in variable selection. _arXiv preprint arXiv:2004.13118_ , 2020. 

- Juho Piironen and Aki Vehtari. Projection predictive model selection for Gaussian processes. In _2016 IEEE 26th International Workshop on Machine Learning for Signal Processing (MLSP)_ , pages 1–6, 2016. doi: 10.1109/MLSP.2016.7738829. 

- Juho Piironen and Aki Vehtari. Comparison of Bayesian predictive methods for model selection. _Statistics and Computing_ , 27(3):711–735, 2017a. ISSN 0960-3174, 1573-1375. doi: 10.1007/ s11222-016-9649-y. URL http://link.springer.com/10.1007/s11222-016-9649-y. 

- Juho Piironen and Aki Vehtari. Sparsity information and regularization in the horseshoe and other shrinkage priors. _Electronic Journal of Statistics_ , 11(2):5018–5051, 2017b. ISSN 1935-7524. doi: 10.1214/17-EJS1337SI. URL https://projecteuclid.org/euclid.ejs/1513306866. 

- Juho Piironen, Markus Paasiniemi, Alejandro Catalina, and Aki Vehtari. _projpred: Projection Predictive Feature Selection_ , 2020a. https://mc-stan.org/projpred, https://discourse.mc-stan.org/. 

- Juho Piironen, Markus Paasiniemi, and Aki Vehtari. Projective inference in high-dimensional problems: Prediction and feature selection. _Electronic Journal of Statistics_ , 14(1):2155–2197, 2020b. doi: 10.1214/20-EJS1711. URL https://doi.org/10.1214/20-EJS1711. 

- Adrian E. Raftery, David Madigan, and Jennifer A. Hoeting. Bayesian model averaging for linear regression models. _Journal of the American Statistical Association_ , 92(437):179–191, Mar 1997. ISSN 1537-274X. doi: 10.1080/01621459.1997.10473615. URL http://dx.doi.org/10.1080/ 01621459.1997.10473615. 

- Robert Tibshirani. Regression shrinkage and selection via the Lasso. _Journal of the Royal Statistical Society. Series B (Methodological)_ , 58(1):267–288, 1996. ISSN 00359246. URL http://www.jstor.org/stable/2346178. 

- Gerhard Tutz and Andreas Groll. Regularization for generalized additive mixed models by likelihoodbased boosting. _Methods of Information in Medicine_ , 51(02):168–177, 2012. ISSN 2511-705X. doi: 10.3414/me11-02-0021. URL http://dx.doi.org/10.3414/me11-02-0021. 

22 

Projection Predictive Inference for Generalized Linear and Additive Multilevel Models 

- Aki Vehtari, Andrew Gelman, and Jonah Gabry. Practical Bayesian model evaluation using leaveone-out cross-validation and WAIC. _Statistics and Computing_ , 27(5):1413–1432, Aug 2016. ISSN 1573-1375. doi: 10.1007/s11222-016-9696-4. URL http://dx.doi.org/10.1007/ s11222-016-9696-4. 

- Aki Vehtari, Daniel Simpson, Andrew Gelman, Yuling Yao, and Jonah Gabry. Pareto smoothed importance sampling. _arxiv preprint:1507.02646_ , 2019. 

- Arunas P. Verbyla, Brian R. Cullis, Michael G. Kenward, and Sue J. Welham. The analysis of designed experiments and longitudinal data by using smoothing splines. _Journal of the Royal Statistical Society: Series C (Applied Statistics)_ , 48(3):269–311, Aug 1999. ISSN 1467-9876. doi: 10.1111/1467-9876.00154. URL http://dx.doi.org/10.1111/1467-9876.00154. 

- Simon N. Wood. Fast stable restricted maximum likelihood and marginal likelihood estimation of semiparametric generalized linear models. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 73(1):3–36, Sep 2010. ISSN 1369-7412. doi: 10.1111/j.1467-9868. 2010.00749.x. URL http://dx.doi.org/10.1111/j.1467-9868.2010.00749.x. 

- Simon N. Wood. _Generalized Additive Models_ . Chapman and Hall/CRC, May 2017. ISBN 9781315370279. doi: 10.1201/9781315370279. URL http://dx.doi.org/10.1201/ 9781315370279. 

- Hui Zou and Trevor Hastie. Regularization and variable selection via the elastic net. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 67(2):301–320, Apr 2005. ISSN 1467-9868. doi: 10.1111/j.1467-9868.2005.00503.x. URL http://dx.doi.org/10.1111/j. 1467-9868.2005.00503.x. 

23 


