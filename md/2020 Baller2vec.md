<!-- source: 2020 Baller2vec.pdf -->

# **baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 

**Michael A. Alcorn**<sup>1</sup> **Anh Nguyen**<sup>1</sup> 

## **Abstract** 

Multi-agent spatiotemporal modeling is a challenging task from both an algorithmic design and computational complexity perspective. Recent work has explored the efficacy of traditional deep sequential models in this domain, but these architectures are slow and cumbersome to train, particularly as model size increases. Further, prior attempts to model interactions between agents across time have limitations, such as imposing an order on the agents, or making assumptions about their relationships. In this paper, we introduce baller2vec, a multi-entity generalization of the standard Transformer that, with minimal assumptions, can _simultaneously and efficiently_ integrate information across entities and time. We test the effectiveness of baller2vec for multiagent spatiotemporal modeling by training it to perform two different basketball-related tasks: (1) simultaneously forecasting the trajectories of all players on the court and (2) forecasting the trajectory of the ball. Not only does baller2vec learn to perform these tasks well, it also appears to “understand” the game of basketball, encoding idiosyncratic qualities of players in its embeddings, and performing basketball-relevant functions with its attention heads. 

## **1. Introduction** 

In a variety of settings, individuals attempt to predict phenomena that arise from multiple entities interacting through time, whether that is a defender anticipating where the point guard will make a pass in a basketball game, a marketing professional guessing the next trending topic on a social network, or a theme park manager forecasting the flow of visitor traffic. Researchers designing algorithms to perform 

> 1 Department of Computer Science and Software Engineering, Auburn University, Auburn, Alabama, USA. Correspondence to: Michael A. Alcorn _<_ alcorma@auburn.edu _>_ and Anh Nguyen _<_ anh.ng8@gmail.com _>_ . 

Preprint. Work in progress. Copyright 2021 by the author(s). 







_Figure 1._ After solely being trained to predict the trajectory of the ball ( ) given the locations of the players and the ball on the court through time, a self-attention (SA) head in baller2vec learned to anticipate passes. When the ball handler ( ) is driving towards the basket at _t_ = 3, SA assigns near-zero weights (black) to all players, suggesting no passes will be made. Interestingly, the ball handler indeed did not pass and dribbled into the lane. At _t_ = 7, SA assigns a high weight (white) to a teammate ( ), which correctly identifies the recipient of the pass at _t_ = 12. 

such tasks face two main challenges: 

1. Given that entities lack a natural ordering, how do you effectively model interactions between entities across time? 

2. How do you _efficiently_ learn from the large, highdimensional inputs inherent to such sequential data? 

Prior work in athlete trajectory forecasting, a widely studied application of multi-agent spatiotemporal modeling (MASM; where entities are agents moving through space), has attempted to model player interactions through “rolealignment” preprocessing steps (i.e., imposing an order on the players) (Felsen et al., 2018; Zhan et al., 2019) or graph neural networks (Yeh et al., 2019), but these approaches may destroy identity information in the former case (see Section 4.2) or limit personalization in the latter case (see Section 5.1). Recently, researchers have experimented with variational recurrent neural networks (VRNNs) (Chung et al., 2015) to model the temporal aspects of player trajectory data (Yeh et al., 2019; Zhan et al., 2019), but the inherently sequential design of this architecture limits the size of models that can feasibly be trained in experiments. 

Transformers (Vaswani et al., 2017) were designed to circumvent the computational constraints imposed by other sequential models, and they have achieved state-of-the-art results in a wide variety of sequence learning tasks, both 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 

in natural language processing (NLP), e.g., GPT-3 (Brown et al., 2020), and computer vision, e.g., Vision Transformers (Dosovitskiy et al., 2021). While Transformers have successfully been applied to _static_ multi-entity data, e.g., graphs (Velickoviˇ c et al.´ , 2018), the only published work we are aware of that attempts to model multi-entity _sequential_ data with Transformers uses four different Transformers to _separately_ process information temporally and spatially before merging the sub-Transformer outputs (Yu et al., 2020). 

In this paper, we introduce a _multi-entity_ Transformer that, with minimal assumptions, is capable of _simultaneously_ integrating information across agents and time, which gives it powerful representational capabilities. We adapt the original Transformer architecture to suit multi-entity sequential data by converting the standard self-attention matrix used in NLP tasks into a novel self-attention _tensor_ . To test the effectiveness of our multi-entity Transformer for MASM, we train it to perform two different basketball-related tasks (hence the name baller2vec): (1) simultaneously forecasting the trajectories of all players on the court ( **Task P** ) and (2) forecasting the trajectory of the ball ( **Task B** ). Further, we convert these tasks into classification problems by discretizing the trajectory space, which allows baller2vec to learn complex, multimodal trajectory distributions via strictly maximizing the likelihood of the data (in contrast to variational approaches, which maximize the evidence lower bound and thus require priors over the latent variables). We 

1. baller2vec is an effective algorithm for MASM, obtaining a perplexity of 1.68 on **Task P** (compared to 16.90 when simply using the label distribution from the training set) and 14.57 on **Task B** (vs. 322.40) (Section 4.1). 

2. baller2vec demonstrably integrates information across _both_ agents and time to achieve these results, as evidenced by ablation experiments (Section 4.2). 

3. The identity embeddings learned by baller2vec capture idiosyncratic qualities of players, indicative of the model’s deep personalization capabilities (Section 4.3). 

4. baller2vec’s trajectory forecast distributions depend on both the historical and current context (Section 4.4), and several attention heads appear to perform different basketball-relevant functions (Figure 1; Section 4.5), which suggests the model learned to “understand” the sport. 

## **2. Methods** 

### **2.1. Multi-entity sequences** 

Let _A_ = _{_ 1 _,_ 2 _, . . . , B}_ be a set indexing _B_ entities and _P_ = _{p_ 1 _, p_ 2 _, . . . , pK} ⊂ A_ be the _K_ entities involved in a particular sequence. Further, let _Zt_ = _{zt,_ 1 _, zt,_ 2 _, . . . , zt,K}_ 

be an _unordered_ set of _K_ feature vectors such that _zt,k_ is the feature vector at time step _t_ for entity _pk_ . _Z_ = ( _Z_ 1 _, Z_ 2 _, . . . , ZT_ ) is thus an _ordered_ sequence of sets of feature vectors over _T_ time steps. When _K_ = 1, _Z_ is a sequence of individual feature vectors, which is the underlying data structure for many NLP problems. 

We now consider two different tasks: (1) sequential entity labeling, where each entity has its own label at each time step (which is conceptually similar to word-level language modeling), and (2) sequential labeling, where each time step has a single label (see Figure 3). For (1), let _V_ = ( _V_ 1 _, V_ 2 _, . . . , VT_ ) be a sequence of sets of labels corresponding to _Z_ such that _Vt_ = _{vt,_ 1 _, vt,_ 2 _, . . . , vt,K}_ and _vt,k_ is the label at time step _t_ for the entity indexed by _k_ . For (2), let _W_ = ( _w_ 1 _, w_ 2 _, . . . , wT_ ) be a sequence of labels corresponding to _Z_ where _wt_ is the label at time step _t_ . The goal is then to learn a function _f_ ( _Z_ ) that maps a set of entities and their time-dependent feature vectors to a probability distribution over either (1) the entities’ time-dependent labels or (2) the sequence of labels. Here, we use a multi-entity Transformer (described in Section 2.3) for our _f_ . 

### **2.2. Multi-agent spatiotemporal modeling** 

In the MASM setting, _P_ is a set of _K_ different agents and _Ct_ = _{_ ( _xt,_ 1 _, yt,_ 1) _,_ ( _xt,_ 2 _, yt,_ 2) _, . . . ,_ ( _xt,K, yt,K_ ) _}_ is an unordered set of _K_ coordinate pairs such that ( _xt,k, yt,k_ ) are the coordinates for agent _pk_ at time step _t_ . The ordered sequence of sets of coordinates _C_ = ( _C_ 1 _, C_ 2 _, . . . , CT_ ), together with _P_ , thus defines the trajectories for the _K_ agents over _T_ time steps. We then define _zt,k_ as: 



where _g_ is a multilayer perceptron (MLP), _ea_ is an agent embedding layer, and _ht,k_ is a vector of optional contextual features for agent _pk_ at time step _t_ . The trajectory for agent _pk_ at time step _t_ is defined as ( _xt_ +1 _,k − xt,k, yt_ +1 _,k − yt,k_ ). Similar to Zheng et al. (2016), to fully capture the multimodal nature of the trajectory distributions, we discretize the 2D Euclidean space into an _n × n_ grid (Figure 2) and treat the problem as a classification task. Therefore, _Z_ has a corresponding sequence of sets of trajectory labels (i.e., _vt,k_ is an integer from one to _n_<sup>2</sup> ), and the loss for each sample in **Task P** is: 



where _H_ is sequence of sets of contextual vectors corresponding to _C_ and _f_ ( _P, C_ 1: _t, H_ 1: _t_ )[ _vt,k_ ] is the probability assigned to agent _pk_ ’s trajectory label at time step _t_ by _f_ , i.e., (2) is the negative log-likelihood (NLL) of the data according to the model. 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 



_Figure 2._ An example of a discretized trajectory. The agent’s starting position is in the center cell, and the cell containing the agent’s ending position is used as the label (of which there are _n_<sup>2</sup> possibilities). 

For **Task B** , we optimize the following loss for each sample: 



where _f_ ( _P, C_ 1: _t, H_ 1: _t_ )[ _wt_ ] is the probability assigned to the ball’s trajectory label at time step _t_ by _f_ , and the labels correspond to a discretized 3D Euclidean space (i.e., _wt_ is an integer from one to _n_<sup>3</sup> ). 

### **2.3. The multi-entity Transformer** 

We now describe our multi-entity Transformer, baller2vec (Figure 3). For NLP tasks, the Transformer self-attention mask _M_ takes the form of a _T × T_ matrix (Figure 4) where _T_ is the length of the sequence. The element at _Mt_ 1 _,t_ 2 thus indicates whether or not the model can “look” at time step _t_ 2 when processing time step _t_ 1. We generalize the standard Transformer to the multi-entity setting by employing a _T × K × T × K_ mask _tensor_ where element _Mt_ 1 _,k_ 1 _,t_ 2 _,k_ 2 indicates whether or not the model can “look” at agent _pk_ 2 at time step _t_ 2 when processing agent _pk_ 1 at time step _t_ 1. In practice, we reshape _M_ into a _TK × TK_ matrix (Figure 4) to be compatible with typical Transformer implementations, and the input to the Transformer is a matrix with shape _TK × F_ where _F_ is the dimension of each _zt,k_ . Similar to Vaswani et al. (2017), to encode temporal position, we add _the same_ position embedding _et_ to the feature vector for _each_ entity at each time step, i.e.: 



The remaining computations are identical to the standard Transformer (see implementation in Section S1). 

## **3. Experiments** 

All data and code for the paper are available at https: //github.com/airalcorn2/baller2vec. 

### **3.1. Dataset** 

We trained baller2vec on a publicly available dataset of player and ball trajectories recorded during 631 National Basketball Association (NBA) games from the 2015-2016 season. All 30 NBA teams and 450 different players were represented. Because transition sequences are a strategically important part of basketball, unlike prior work, e.g., (Felsen et al., 2018; Yeh et al., 2019; Zhan et al., 2019), we did not terminate sequences on a change of possession, nor did we constrain ourselves to a fixed subset of sequences. Instead, each training sample was generated on the fly by first randomly sampling a game, and then randomly sampling a time point from that game. The following four seconds of data were downsampled to 5 Hz from the original 25 Hz and used as the input. 

Because we did not terminate sequences on a change of possession, we could not “normalize” the direction of the court as was done in prior work (Felsen et al., 2018; Yeh et al., 2019; Zhan et al., 2019). Instead, for each sampled sequence, we randomly (with a probability of 0.5) rotated the court 180<sup>_◦_</sup> (because the court’s direction is arbitrary), effectively doubling the size of the dataset (we used a binary variable to indicate the side of the frontcourt for each player). As a result, we had access to _∼_ 82 million different (albeit overlapping) training sequences (2 rotations _×_ 569 games _×_ 4 periods per game _×_ 12 minutes per period _×_ 60 seconds per minute _×_ 25 Hz). We used a training/validation/test split of 569/30/32 games, respectively (i.e., 5% of the games were used for testing, and 5% of the remaining 95% of games were used for validation). For both the validation and test sets, _∼_ 1,000 different, _non-overlapping_ sequences were selected for evaluation by dividing each game into _⌊_<sup>1</sup><sup>_<u>,</u>_</sup> _N_<sup>000</sup><sup>_⌋_</sup> non-overlapping chunks (where _N_ is the number of games), and using the starting four seconds from each chunk as the evaluation sequence. 

### **3.2. Model** 

We trained separate models for **Task P** and **Task B** . For all experiments, we used a single Transformer architecture that was nearly identical to the original model described in Vaswani et al. (2017), with _d_ model = 512 (the dimension of the input and output of each Transformer layer), eight attention heads, _d_ ff = 2048 (the dimension of the inner feedforward layer), and six layers, although we did not use dropout, and we used learned embeddings to encode position instead of sine/cosine vector functions. For _both_ **Task P** and **Task B** , the model was provided the players _and_ the ball as input. Both the players and the ball were embedded to 20-dimensional vectors. The input features for each player consisted of his identity, ( _x, y_ ) coordinates on the court at each time step in the sequence, and a binary variable indicating the side of his frontcourt. The input 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 





_Figure 3._ An overview of the multi-entity Transformer. Each time step _t_ consists of an _unordered_ set of feature vectors _Zt_ (colored circles) with either (left) a corresponding set of entity labels _Vt_ (colored diamonds) or (right) a single label _wt_ . Here, each circle represents the input features for a different entity (in our experiments, a basketball player) at a specific time step, and matching colored circles/diamonds across time steps correspond to the same entity. 



_Figure 4._ Left: the standard self-attention mask matrix _M_ . The element at _Mt_ 1 _,t_ 2 indicates whether or not the model can “look” at time step _t_ 2 when processing time step _t_ 1. Right: the matrix form of our multi-entity self-attention mask tensor. In tensor form, element _Mt_ 1 _,k_ 1 _,t_ 2 _,k_ 2 indicates whether or not the model can “look” at agent _pk_ 2 at time step _t_ 2 when processing agent _pk_ 1 at time step _t_ 1. In matrix form, this corresponds to element _Mt_ 1 _K_ + _k_ 1 _,t_ 2 _K_ + _k_ 2 when using zero-based indexing. The _M_ shown here is for a static, fully connected graph, but other, potentially evolving network structures can be encoded in the attention tensor. 

features for the ball were its ( _x, y, z_ ) coordinates at each time step. 

The input features for the players and the ball were processed by separate, three layer MLPs before being fed into the Transformer. Each MLP had 128, 256, and 512 nodes in its three layers, respectively, and a ReLU nonlinearity following each of the first two layers. Similarly, separate positional embeddings were used to encode the temporal order of the player and ball Transformer inputs. A single linear layer on top of the Transformer output followed by a softmax was used for classification. For players, we discretized an 11 ft _×_ 11 ft 2D Euclidean trajectory space into an 11 _×_ 11 grid of 1 ft _×_ 1 ft squares for a total of 121 player trajectory labels (Figure 5 shows the distribution of the labels for the entire dataset). Similarly, for the ball, we discretized a 19 ft _×_ 19 ft _×_ 19 ft 3D Euclidean trajectory space into an 19 _×_ 19 _×_ 19 grid of 1 ft _×_ 1 ft _×_ 1 ft cubes 

for a total of 6,859 ball trajectory labels. 



_Figure 5._ A log-normalized heat map of the discretized player trajectory labels in the full NBA dataset. The center cell corresponds to the “stationary” trajectory (i.e., the player did not move further than 0.5 ft in either the _x_ or _y_ direction). The elongated shape of the distribution reflects the rectangular shape of the court. 

We used the Adam optimizer (Kingma & Ba, 2015) with a learning rate of 10<sup>_−_6</sup> , _β_ 1 = 0 _._ 9, _β_ 2 = 0 _._ 999, and _ϵ_ = 10<sup>_−_9</sup> to update the model’s parameters, of which there were _∼_ 23 million. Models were implemented in PyTorch and trained on a single NVIDIA GTX 1080 Ti GPU for _∼_ 250 epochs where each epoch consisted of 20,000 training samples, and the validation set was used for early stopping. 

### **3.3. Ablation studies** 

To assess the impact of the multi-entity design of baller2vec and the inclusion of player identity on model performance, we trained three variations of our player trajectory forecasting model: (1) one player as input without player identity, (2) all 10 players as input without player identities, and (3) all 10 players as input with player identities. In experiments where player identity was not used, a single generic player embedding was used in place of the player identity embeddings. We also trained two variations of our ball trajectory forecasting model: one with player 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 

identity and one without. Lastly, to determine the extent to which baller2vec uses historical information in its forecasts, we compared the model’s average NLL for the full sequence test set on **Task P** to the model’s average NLL for the test set when only predicting the trajectories for the 

## **4. Results** 

### **4.1. baller2vec is an effective algorithm for multi-agent spatiotemporal modeling.** 

The average NLL on the test set for our best **Task P** model was 0.519, while the average NLL for our best **Task B** model was 2.717. In NLP, model performance is often expressed in terms of the “perplexity” per word, which, intuitively, is the number of faces on a fair die that has the same amount of uncertainty as the model per word (i.e., a uniform distribution over _M_ labels has a perplexity of _M_ , so a model with a per word perplexity of six has the same amount of uncertainty as rolling a fair six-sided die). In our case, we consider the perplexity per trajectory, defined as: 



where _N_ is the number of sequences. Our best **Task P** model achieved a perplexity per trajectory of 1.68, i.e., baller2vec was, on average, as uncertain as rolling a 1.68-sided fair die (better than a coin flip) when predicting player trajectories. For comparison, when using the distribution of the player trajectory labels in the training set as the predicted probabilities, the perplexity on the test set was 16.90. Our best **Task B** model achieved a perplexity per trajectory of 14.57 (compared to 322.40 when using the training set distribution). 

### **4.2. baller2vec uses information about all players on the court through time, in addition to player identity, to model spatiotemporal dynamics.** 

Results for our ablation experiments can be seen in Table 1. Including all 10 players as input dramatically improved the performance of our **Task P** model by 12.1% over only using a single player. Including player identity improved the model’s performance a further 3.8%. This stands in contrast to Felsen et al. (2018) where the inclusion of player identities led to slightly _worse_ model performance, a counterintuitive result given the range of skills among NBA players, but possibly a side effect of their role-alignment procedure. Interestingly, including player identity as input for **Task B** only improved the model’s performance by 1.1%. Lastly, the model’s average NLL on **Task P** for the full sequence test set (0.519) was 71% lower than its average NLL for the single frame test set (1.78), i.e., baller2vec is clearly using historical information to model the spatiotemporal 

dynamics of basketball. 

_Table 1._ The average NLL on the test set for each of the models in our ablation experiments (lower is better). For **Task P** , using all 10 players improved model performance by 12.1%, while using player identity improved model performance by an additional 3.8%. For **Task B** , using player identity improved model performance by 1.1%. 1/10 indicates whether one or 10 players were used as input, respectively, while I/NI indicates whether or not player identities were used, respectively. 

|Task|1-NI|10-NI|10-I|
|---|---|---|---|
|**Task P**|0.613|0.539|0.519|
|**Task B**|N/A|2.709|2.679|



### **4.3. Player embeddings encode individual attributes.** 

Neural language models are widely known for their ability to encode semantic relationships between words and phrases as geometric relationships between embeddings—see, e.g., (Mikolov et al., 2013b;a; Le & Mikolov, 2014; Sutskever et al., 2014). Alcorn (2018) observed a similar phenomenon in a baseball setting, where batters and pitchers with similar skills were found next to each other in the embedding space learned by a neural network trained to predict the outcome of an at-bat. Figure 6 displays a 2D UMAP (McInnes et al., 2018) generated from the player embeddings learned by baller2vec for **Task B** . Like (batter|pitcher)2vec (Alcorn, 2018), baller2vec seems to encode skills and physical attributes in its player embeddings. 

Querying the nearest neighbors for individual players reveals further insights about the baller2vec embeddings. For example, the nearest neighbor for Russell Westbrook, an extremely athletic 6’3” point guard, is Derrick Rose, a 6’2” point guard also known for his athleticism (Figure 7). Amusingly, the nearest neighbor for Pau Gasol, a 7’1” center with a respectable shooting range, is his younger brother Marc Gasol, a 6’11” center, also with a respectable shooting range. 

### **4.4. baller2vec’s trajectory forecast distributions depend on both the historical and current context.** 

Because baller2vec _explicitly_ models the distribution of the player trajectories (unlike variational methods), we can easily visualize how its trajectory forecast distributions shift in different situations. As can be seen in Figure 8, baller2vec’s trajectory forecast distributions depend on both the historical and current context. When provided with limited historical information, baller2vec tends to be less certain about where the players might go. baller2vec also tends to be more certain when forecasting “easy” trajectories (e.g., a player moving into open 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 



_Figure 6._ By exclusively learning to predict the trajectory of the ball, baller2vec was able to infer idiosyncratic player attributes (as can be seen in this 2D UMAP of the player embeddings). The left-hand side of the plot contains tall post players ( , ), e.g., Serge Ibaka, while the right-hand side of the plot contains shorter shooting guards (�) and point guards (+), e.g., Stephen Curry. The connecting transition region contains forwards ( , ) and other “hybrid” players, i.e., individuals possessing both guard and post skills, e.g., LeBron James. Further, players with similar defensive abilities, measured here by the cube root of the players’ blocks per minute in the 2015-2016 season (Basketball-Reference.com, 2021), cluster together. 



_Figure 7._ Nearest neighbors in baller2vec’s embedding space are plausible doppelgangers, such as the explosive point guards¨ Russell Westbrook and Derrick Rose, and seven-foot tall brothers Pau and Marc Gasol. Images credits can be found in Table S1. 

space) vs. “hard” trajectories (e.g., an offensive player choosing which direction to move around a defender). Similarly, as can be seen in Figure 9, player trajectories _generated_ by baller2vec are noisier when conditioned on less historical context. 

ten seem to reveal how a model is “thinking”. For example, Vaswani et al. (2017) discovered examples of attention heads in their Transformer that appear to be performing various language understanding subtasks, such as anaphora resolution. As can be seen in Figure 10, some of the attention heads in baller2vec seem to be performing basketball understanding subtasks, such as keeping track of the ball handler’s teammates, and anticipating who the ball handler will pass to, which, intuitively, helps with our task of predicting the ball’s trajectory. 

## **5. Related Work** 

### **5.1. Trajectory modeling in sports** 

There is a rich literature on MASM, particularly in the context of sports, e.g., (Kim et al., 2010; Zheng et al., 2016; Le et al., 2017b;a; Qi et al., 2020; Zhan et al., 2020). Most relevant to our work is Yeh et al. (2019), which used a variational recurrent neural network combined with a graph neural network to forecast trajectories in a multi-agent setting. Like their approach, our model is permutation invariant with regard to the ordering of the agents; however, we use a multi-head attention mechanism to achieve this permutation invariance while the permutation invariance in Yeh et al. (2019) is provided by the graph neural network. Specifically, Yeh et al. (2019) define: 



### **4.5. Different attention heads in baller2vec appear to perform different basketball-relevant functions.** 

One intriguing property of the attention mechanism (Graves, 2013; Graves et al., 2014; Weston et al., 2015; Bahdanau et al., 2015) is how, when visualized, the attention scores of- 



where **v** _i_ is the initial state of agent _i_ , **t** _i,j_ is an embedding for the edge between agents _i_ and _j_ , **e** _i,j_ is the representation 



<!-- Start of picture text -->
t  = 0 t  = 2 t  = 8<br>v 0 , 5 f 0 , 5 v 2 , 5 f 2 , 5 v 8 , 5 f 8 , 5<br>’s trajectory forecast distributions are affected by both the historical and current context. At  t  = 0, baller2vec, baller2vec baller2vec<br>;  k = 5) future trajectory (left grid and dotted red line; the blue bordered center cell is) future trajectory (left grid and dotted red line; the blue bordered center cell is<br>the “stationary” trajectory), with most of the probability mass (right grid; black = 1.0; white = 0.0) divided between trajectories moving<br>towards the opponent’s basket and where the ball handler appears to be headed. After observing a portion of the sequence ( t =<br> becomes very certain about the target player’s trajectory ( f 2 , 5), but when the ball handler makes a move past his defender), but when the ball handler makes a move past his defender<br> becomes split between trajectories (committing to the ball handler or staying in position for the trailing man).<br> S1.. = ball, = offense, = defense, and  ft,kt,k =  f ( P, C C 1: t, H, H H 1: t ) t,k .<br>(a) Ground truth. (b) 2 s observed. (c) 1 s observed. (d) 0 s observed.<br><!-- End of picture text -->



_Figure 8._ baller2vec’s trajectory forecast distributions are affected by both the historical and current context. At _t_ = 0, baller2vec, baller2vec baller2vec is fairly uncertain about the target player’s ( ; _k_ = 5) future trajectory (left grid and dotted red line; the blue bordered center cell is) future trajectory (left grid and dotted red line; the blue bordered center cell is the “stationary” trajectory), with most of the probability mass (right grid; black = 1.0; white = 0.0) divided between trajectories moving towards the opponent’s basket and where the ball handler appears to be headed. After observing a portion of the sequence ( _t_ = 2), baller2vec becomes very certain about the target player’s trajectory ( _f_ 2 _,_ 5), but when the ball handler makes a move past his defender), but when the ball handler makes a move past his defender ( _t_ = 8), baller2vec becomes split between trajectories (committing to the ball handler or staying in position for the trailing man). Additional examples can be found in Figure S1.. = ball, = offense, = defense, and _ft,kt,k_ = _f_ ( _P, C C_ 1: _t, H, H H_ 1: _t_ ) _t,k_ . 



_Figure 9._ With less historical information (solid lines), baller2vec’s generated trajectories (dotted lines) tend to be noisier. Each player is a different color, and the colored lines are their corresponding trajectories. The shapes are in the _starting_ positions for the trajectories, and the ground truth location of the ball is used as input at each time step (i.e., the ball trajectories are not generated). = offense, = defense, and = ball. 







(a) Attention head 2-7 (layer-head) ap(b) Attention head 6-2 seems to predict (c) In this frame, the highlighted player pears to focus on teammates of the ball who the ball handler will be in future in (b) receives a pass from the previous handler ( ). frames ( ); see (c). ball handler. 

_Figure 10._ The attention outputs from baller2vec suggest it learned basketball-relevant functions. Players are shaded according to the _sum_ of the attention scores assigned to the players _through time_ with reference to the ball in the current frame (recall that each player occurs multiple times in the input). Higher attention scores are lighter. For both of these attention heads, the sum of the attention scores assigned to the ball through time was small (0.01 for both the left and middle frames where the maximum is 1.00). Additional examples can be found in Figures S2 and S3. 

for edge ( _i, j_ ), _Ni_ is the neighborhood for agent _i_ , **t** _i_ is a node embedding for agent _i_ , **o** _i_ is the output state for agent _i_ , and _fe_ and _fv_ are deep neural networks. 

Assuming _each individual player_ is a different “type” in (6) (i.e., attempting to maximize the level of personalization) would require 450<sup>2</sup> = 202,500 (i.e., _B_<sup>2</sup> ) different _ti,j_ edge embeddings, many of which would never be used dur- 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 

ing training and thus inevitably lead to poor out-of-sample performance. Reducing the number of type embeddings requires making assumptions about the nature of the relationships between nodes. By using a multi-head attention mechanism, our model learns to integrate information about different agents in a highly flexible manner that is both agent and time-dependent, and can generalize to unseen agent combinations. 

Additionally, unlike recent works that use variational methods to train their generative models (Yeh et al., 2019; Felsen et al., 2018; Zhan et al., 2019), we translate the multi-agent trajectory forecasting problem into a classification task, which allows us to train our model by strictly maximizing the likelihood of the data. As a result, we do not make any assumptions about the distributions of the trajectories nor do we need to set any priors over latent variables. Zheng et al. (2016) also predicted discretized trajectories, but they included “macro-goals” (i.e., the approximate destination of the player) as input to their model. 

### **5.2. Transformers for multi-agent spatiotemporal modeling** 

Giuliari et al. (2020) used a Transformer to forecast the trajectories of _individual_ pedestrians, i.e., the model does not consider interactions between individuals. Yu et al. (2020) used _separate_ temporal and spatial Transformers to forecast the trajectories of multiple, interacting pedestrians. Specifically, the temporal Transformer processes the coordinates of each pedestrian _independently_ (i.e., it does not model interactions), while the spatial Transformer, which is inspired by Graph Attention Networks (Velickoviˇ c et al.´ , 2018), processes the pedestrians _independently at each time step_ . Sanford et al. (2020) used a Transformer to classify on-the-ball events from sequences in soccer games; however, only the coordinates of the _K_ -nearest players to the ball were included in the input (along with the ball’s coordinates). Further, the _order_ of the included players was based on their average distance from the ball for a given temporal window, which can lead to specific players changing position in the input between temporal windows. As far as we are aware, baller2vec is the **first** Transformer capable of processing all agents _simultaneously across time_ without imposing an arbitrary order on the agents. 

## **6. Limitations** 

At least two different factors may explain why including player identity as an input to baller2vec only leads to relatively small performance improvements. First, both player and ball trajectories are fairly generic—players tend to move into open space, defenders tend to move towards their man or the ball, point guards tend to pass to their teammates, and so on. Further, the location of a player on the 

court is often indicative of their position, and players playing the same position tend to have similar skills and physical attributes. As a result, we might expect baller2vec to be able to make reasonable guesses about a player’s/ball’s trajectory just given the location of the players and the ball on the court. 

Second, baller2vec may be able to _infer_ the identity of the players directly from the spatiotemporal data. Unlike (batter|pitcher)2vec (Alcorn, 2018), which was trained on several seasons of Major League Baseball data, baller2vec only had access to one half of one season’s worth of NBA data for training. As a result, player identity may be entangled with season-specific factors (e.g., certain rosters or coaches) that are actually exogenous to the player’s intrinsic qualities, i.e., baller2vec may be overfitting to the season. To provide an example, the Golden State Warriors ran a very specific kind of offense in the 2015-2016 season (breaking the previous record for most three-pointers made in the regular season by 15.4%), and many basketball fans could probably recognize them from a bird’s eye view (i.e., without access to any identifying information). Given additional seasons of data, baller2vec would no longer be able to exploit the implicit identifying information contained in static lineups and coaching strategies, so including player identity in the input would likely 

## **7. Conclusion** 

In this paper, we introduced baller2vec, a generalization of the standard Transformer that can model sequential data consisting of multiple, unordered entities at each time step. As an architecture that both is computationally efficient and has powerful representational capabilities, we believe baller2vec represents an exciting new direction for MASM. As discussed in Section 6, training baller2vec on more training data may allow the model to more accurately factor players away from season-specific patterns. With additional data, more contextual information about agents (e.g., a player’s age, injury history, or minutes played in the game) and the game (e.g., the time left in the period or the score difference) could be included as input, which might allow baller2vec to learn an even more complete model of the game of basketball. Although we only experimented with static, fully connected graphs here, baller2vec can be easily applied to more complex inputs—for example, a sequence of graphs with changing nodes and edges—by simply adapting the attention tensor as appropriate. Lastly, as a generative model, baller2vec could be used for counterfactual simulations (e.g., assessing the impact of different rosters), or combined with a controller to discover optimal play calling strategies through reinforcement learning. 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 

## **Acknowledgements** 

We would like to thank Sudha Lakshmi, Katherine Silliman, Jan Van Haaren, Hans-Werner Van Wyk, and Eric Winsberg for their helpful suggestions on how to improve the manuscript. 

## **References** 

- Alcorn, M. A. (batter|pitcher)2vec: Statistic-free talent modeling with neural player embeddings. In _MIT Sloan Sports Analytics Conference_ , 2018. 

- Bahdanau, D., Cho, K., and Bengio, Y. Neural machine translation by jointly learning to align and translate. In _International Conference on Learning Representations_ , 2015. 

- Basketball-Reference.com. 2015-16 nba player stats: Totals, February 2021. URL https: //www.basketball-reference.com/ leagues/NBA_2016_totals.html. 

- Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. Language models are few-shot learners. _arXiv preprint arXiv:2005.14165_ , 2020. 

- Chung, J., Kastner, K., Dinh, L., Goel, K., Courville, A., and Bengio, Y. A recurrent latent variable model for sequential data. In _Advances in Neural Information Processing Systems_ , 2015. 

- Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., and Houlsby, N. An image is worth 16x16 words: Transformers for image recognition at scale. In _International Conference on Learning Representations_ , 2021. URL https:// openreview.net/forum?id=YicbFdNTTy. 

- Felsen, P., Lucey, P., and Ganguly, S. Where will they go? predicting fine-grained adversarial multi-agent motion using conditional variational autoencoders. In _Proceedings of the European Conference on Computer Vision (ECCV)_ , pp. 732–747, 2018. 

- Giuliari, F., Hasan, I., Cristani, M., and Galasso, F. Transformer networks for trajectory forecasting. In _International Conference on Pattern Recognition_ , 2020. 

- Graves, A. Generating sequences with recurrent neural networks. _arXiv preprint arXiv:1308.0850_ , 2013. 

- Graves, A., Wayne, G., and Danihelka, I. Neural turing machines. _arXiv preprint arXiv:1410.5401_ , 2014. 

- Kim, K., Grundmann, M., Shamir, A., Matthews, I., Hodgins, J., and Essa, I. Motion fields to predict play evolution in dynamic sport scenes. In _2010 IEEE Computer Society Conference on Computer Vision and Pattern Recognition_ , pp. 840–847. IEEE, 2010. 

- Kingma, D. P. and Ba, J. Adam: A method for stochastic optimization. In _International Conference on Learning Representations_ , 2015. 

- Le, H. M., Carr, P., Yue, Y., and Lucey, P. Data-driven ghosting using deep imitation learning. In _MIT Sloan Sports Analytics Conference_ , 2017a. 

- Le, H. M., Yue, Y., Carr, P., and Lucey, P. Coordinated multiagent imitation learning. In _International Conference on Machine Learning_ , volume 70, pp. 1995–2003, 2017b. 

- Le, Q. and Mikolov, T. Distributed representations of sentences and documents. In _International conference on machine learning_ , pp. 1188–1196. PMLR, 2014. 

- McInnes, L., Healy, J., and Melville, J. Umap: Uniform manifold approximation and projection for dimension reduction. _arXiv preprint arXiv:1802.03426_ , 2018. 

- Mikolov, T., Chen, K., Corrado, G., and Dean, J. Efficient estimation of word representations in vector space. _arXiv preprint arXiv:1301.3781_ , 2013a. 

- Mikolov, T., Sutskever, I., Chen, K., Corrado, G., and Dean, J. Distributed representations of words and phrases and their compositionality. In _Advances in Neural Information Processing Systems_ , 2013b. 

- Qi, M., Qin, J., Wu, Y., and Yang, Y. Imitative nonautoregressive modeling for trajectory forecasting and imputation. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pp. 12736–12745, 2020. 

- Sanford, R., Gorji, S., Hafemann, L. G., Pourbabaee, B., and Javan, M. Group activity detection from trajectory and video data in soccer. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops_ , pp. 898–899, 2020. 

- Sutskever, I., Vinyals, O., and Le, Q. V. Sequence to sequence learning with neural networks. In _Advances in Neural Information Processing Systems_ , 2014. 

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., and Polosukhin, I. Attention is all you need. In _Advances in Neural Information Processing Systems_ , pp. 5998–6008, 2017. 

- Velickoviˇ c,´ P., Cucurull, G., Casanova, A., Romero, A., Lio, P., and Bengio, Y. Graph attention networks. In 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 

- _International Conference on Learning Representations_ , 2018. 

- Weston, J., Chopra, S., and Bordes, A. Memory networks. In _International Conference on Learning Representations_ , 2015. 

- Yeh, R. A., Schwing, A. G., Huang, J., and Murphy, K. Diverse generation for multi-agent sports games. In _Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition_ , pp. 4610–4619, 2019. 

- Yu, C., Ma, X., Ren, J., Zhao, H., and Yi, S. Spatio-temporal graph transformer networks for pedestrian trajectory prediction. In _Proceedings of the European Conference on Computer Vision (ECCV)_ , August 2020. 

- Zhan, E., Zheng, S., Yue, Y., Sha, L., and Lucey, P. Generating multi-agent trajectories using programmatic weak supervision. In _International Conference on Learning Representations_ , 2019. URL https://openreview. net/forum?id=rkxw-hAcFQ. 

- Zhan, E., Tseng, A., Yue, Y., Swaminathan, A., and Hausknecht, M. Learning calibratable policies using programmatic style-consistency. In _International Conference on Machine Learning_ , pp. 11001–11011. PMLR, 2020. 

- Zheng, S., Yue, Y., and Hobbs, J. Generating long-term trajectories using deep hierarchical networks. _Advances in Neural Information Processing Systems_ , 29:1543–1551, 2016. 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 

# **Supplementary Materials** 

# **baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 



















_Figure S1._ Additional examples of player trajectory forecasts in different contexts. Each row contains a different sequence, and the first column always contains the first frame from the sequence. 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 







_Figure S2._ Additional examples of attention outputs for the head that focuses on the ball handler’s teammates. 













_Figure S3._ Additional examples of attention outputs for the head that anticipates passes. Each column contains a different sequence, and the top frame precedes the bottom frame in time. 

_Table S1._ Image credits for Figure 7. 

|Image|Source|URL|
|---|---|---|
|Russell Westbrook|Erik Drost|htt|
|Pau Gasol|Keith Allison|htt|
|Kawhi Leonard|Jose Garcia|htt|
|Derrick Rose|Keith Allison|htt|
|Marc Gasol|Verse Photography|htt|
|Jimmy Butler|Joe Gorioso|htt|



**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 

## **S1. baller2vec implementation.** 

# Adapted from: https://pytorch.org/tutorials/beginner/transformer_tutorial.html 

import math import torch 

from torch import nn 

class TimeEncoder(nn.Module): def __init__(self, seq_len, d_model, dropout): super().__init__() self.dropout = nn.Dropout(p=dropout) self.time_embeddings = nn.Parameter(torch.Tensor(seq_len, d_model)) nn.init.normal_(self.time_embeddings) 

def forward(self, x, repeat): repeated = self.time_embeddings.repeat(repeat, 1) x = x + repeated return self.dropout(x) 

class Baller2Vec(nn.Module): def __init__( self, n_player_ids, embedding_dim, sigmoid, seq_len, mlp_layers, n_players, n_player_labels, n_ball_labels, n_seq_labels, nhead, dim_feedforward, num_layers, dropout, use_cls, embed_before_mlp, ): super().__init__() self.sigmoid = sigmoid self.seq_len = seq_len self.use_cls = use_cls self.n_players = n_players self.embed_before_mlp = embed_before_mlp 

# Initialize players, ball, and CLS (if used) embeddings. initrange = 0.1 self.player_embedding = nn.Embedding(n_player_ids, embedding_dim) self.player_embedding.weight.data.uniform_(-initrange, initrange) 

self.ball_embedding = nn.Parameter(torch.Tensor(embedding_dim)) nn.init.uniform_(self.ball_embedding, -initrange, initrange) if use_cls: self.cls_embedding = nn.Parameter(torch.Tensor(mlp_layers[-1])) nn.init.uniform_(self.cls_embedding, -initrange, initrange) # Initialize preprocessing MLPs. player_mlp = nn.Sequential() ball_mlp = nn.Sequential() # Extra dimensions for (x, y) coordinates and hoop side (for players) or z # coordinate (for ball). 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 

in_feats = embedding_dim + 3 if embed_before_mlp else 3 for (layer_idx, out_feats) in enumerate(mlp_layers): if (not embed_before_mlp) and (layer_idx == len(mlp_layers) - 1): out_feats = out_feats - embedding_dim 

player_mlp.add_module(f"layer{layer_idx}", nn.Linear(in_feats, out_feats)) ball_mlp.add_module(f"layer{layer_idx}", nn.Linear(in_feats, out_feats)) 

if layer_idx < len(mlp_layers) - 1: player_mlp.add_module(f"relu{layer_idx}", nn.ReLU()) ball_mlp.add_module(f"relu{layer_idx}", nn.ReLU()) in_feats = out_feats self.player_mlp = player_mlp self.ball_mlp = ball_mlp # Initialize time encoders. d_model = mlp_layers[-1] self.d_model = d_model self.player_time_encoder = TimeEncoder(seq_len, d_model, dropout) self.ball_time_encoder = TimeEncoder(seq_len, d_model, dropout) if use_cls: self.cls_time_encoder = TimeEncoder(seq_len, d_model, dropout) 

# Initialize Transformer. encoder_layer = nn.TransformerEncoderLayer( d_model, nhead, dim_feedforward, dropout ) self.transformer = nn.TransformerEncoder(encoder_layer, num_layers) 

# Initialize classification layers. self.player_classifier = nn.Linear(d_model, n_player_labels) self.player_classifier.weight.data.uniform_(-initrange, initrange) self.player_classifier.bias.data.zero_() 

self.ball_classifier = nn.Linear(d_model, n_ball_labels) self.ball_classifier.weight.data.uniform_(-initrange, initrange) self.ball_classifier.bias.data.zero_() 

if use_cls: self.event_classifier = nn.Linear(d_model, n_seq_labels) self.event_classifier.weight.data.uniform_(-initrange, initrange) self.event_classifier.bias.data.zero_() 

# Initialize mask. self.register_buffer("mask", self.generate_square_subsequent_mask()) 

def generate_square_subsequent_mask(self): # n players plus the ball and the CLS entity (if used). if self.use_cls: sz = (self.n_players + 2) * self.seq_len else: sz = (self.n_players + 1) * self.seq_len mask = torch.zeros(sz, sz) ball_start = self.n_players * self.seq_len if self.use_cls: cls_start = ball_start + self.seq_len for step in range(self.seq_len): start = self.n_players * step stop = start + self.n_players ball_stop = ball_start + step + 1 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 

# The players can look at the players. mask[start:stop, :stop] = 1 # The players can look at the ball. mask[start:stop, ball_start:ball_stop] = 1 # The ball can look at the players. mask[ball_start + step, :stop] = 1 # The ball can look at the ball. mask[ball_start + step, ball_start:ball_stop] = 1 if self.use_cls: cls_stop = cls_start + step + 1 # The players can look at the CLS. mask[start:stop, cls_start:cls_stop] = 1 # The ball can look at the CLS. mask[ball_start + step, cls_start:cls_stop] = 1 # The CLS can look at the players. mask[cls_start + step, :stop] = 1 # The CLS can look at the ball. mask[cls_start + step, ball_start:ball_stop] = 1 # The CLS can look at the CLS. mask[cls_start + step, cls_start:cls_stop] = 1 mask = mask.masked_fill(mask == 0, float("-inf")) mask = mask.masked_fill(mask == 1, float(0.0)) return mask def forward(self, tensors): device = list(self.player_mlp.parameters())[0].device # Get player position/time features. player_embeddings = self.player_embedding( tensors["player_idxs"].flatten().to(device) ) if self.sigmoid == "logistic": player_embeddings = torch.sigmoid(player_embeddings) elif self.sigmoid == "tanh": player_embeddings = torch.tanh(player_embeddings) player_xs = tensors["player_xs"].flatten().unsqueeze(1).to(device) player_ys = tensors["player_ys"].flatten().unsqueeze(1).to(device) player_hoop_sides = ( tensors["player_hoop_sides"].flatten().unsqueeze(1).to(device) ) if self.embed_before_mlp: player_pos = torch.cat( [ player_embeddings, player_xs, player_ys, player_hoop_sides, ], dim=1, ) player_pos_feats = self.player_mlp(player_pos) * math.sqrt(self.d_model) else: player_pos = torch.cat( [ player_xs, player_ys, player_hoop_sides, ], dim=1, ) player_pos_feats = self.player_mlp(player_pos) * math.sqrt(self.d_model) player_pos_feats = torch.cat([player_embeddings, player_pos_feats], dim=1) 

**baller2vec: A Multi-Entity Transformer For Multi-Agent Spatiotemporal Modeling** 

player_pos_time_feats = self.player_time_encoder( player_pos_feats, self.n_players ) # Get ball position/time features. ball_embeddings = self.ball_embedding.repeat(self.seq_len, 1) ball_xs = tensors["ball_xs"].unsqueeze(1).to(device) ball_ys = tensors["ball_ys"].unsqueeze(1).to(device) ball_zs = tensors["ball_zs"].unsqueeze(1).to(device) if self.embed_before_mlp: ball_pos = torch.cat( [ ball_embeddings, ball_xs, ball_ys, ball_zs, ], dim=1, ) ball_pos_feats = self.ball_mlp(ball_pos) * math.sqrt(self.d_model) else: ball_pos = torch.cat( [ ball_xs, ball_ys, ball_zs, ], dim=1, ) ball_pos_feats = self.player_mlp(ball_pos) * math.sqrt(self.d_model) ball_pos_feats = torch.cat([ball_embeddings, ball_pos_feats], dim=1) ball_pos_time_feats = self.ball_time_encoder(ball_pos_feats, 1) # Combine players and ball features. combined = torch.cat([player_pos_time_feats, ball_pos_time_feats], dim=0) if self.use_cls: # Get CLS time features. cls_feats = self.cls_embedding.repeat(self.seq_len, 1) cls_time_feats = self.cls_time_encoder(cls_feats, 1) # Combine with CLS features. combined = torch.cat([combined, cls_time_feats], dim=0) output = self.transformer(combined.unsqueeze(1), self.mask) preds = { "player": self.player_classifier(output).squeeze(1), "ball": self.ball_classifier(output).squeeze(1), } if self.use_cls: preds["seq_label"] = self.event_classifier(output).squeeze(1) return preds 


