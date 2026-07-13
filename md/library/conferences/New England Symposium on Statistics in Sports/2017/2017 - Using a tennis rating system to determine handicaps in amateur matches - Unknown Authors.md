<!-- source: library/conferences/New England Symposium on Statistics in Sports/2017/2017 - Using a tennis rating system to determine handicaps in amateur matches - Unknown Authors.pdf -->



# **Using a tennis rating system to determine handicaps in amateur matches Chan**<sup>2</sup> **Raghav Singal**<sup>1</sup> **Timothy** 

1 2 IEOR, Columbia University, MIE, University of Toronto 



## **Introduction** 



- Handicap systems are used in sports to improve competitive balance 

- Tennis does not have an official handicap system 

- a for tennis 

- [1] propose handicap system 

   - The stronger player gives the weaker player _h_ credits 

   - The weaker player can use a credit at any time during the match 

   - Whenever the weaker player uses one credit, she wins the point outright 

   - The underlying mathematical model is a Markov Decision Process (MDP) 

- to **_h_** 

- [1] map server-specific point-win probabilities **(** **_ps_** _,_ **_pr_ )** handicap 



- However, determining point-win probabilities is challenging 

- On the other hand, rating systems are used widely in tennis 

- **Question** : Can we map a rating difference **_d_** to a handicap **_h_** ? 

## **High-level idea of our solution** 



- **Final goal** : Achieve a linear mapping of the form **_h_** = **_γd_** 

- Will use a of mathematical models to achieve this sequence mapping 

- For amateurs, point-level data is sparse 

- Hence, we start with the match scores and the ratings differences **_d_** 



<!-- Start of picture text -->
match score<br>model 1 chain in<br>(Markov reverse)<br>server-independent point-win probability p<br>model 2 (Bayesian model with logistic link)<br>server-specific point-win probabilities ( ps , pr )<br>model 3 model of<br>(MDP [1])<br>handicap h<br><!-- End of picture text -->

## **Model 1: Markov chain** 



- **Goal** : match-score to Map **_p_** 

- **Step 1** : Map match-score to game-win probability **_q_** 

   - Suppose match-score is 3-6, 4-6 

   - We estimate as 19 **_q_** (3 + 4) _/_ (6 + 6 + 3 + 4) = 7 _/_ 

- **Step 2** : Map **_q_** to **_p_** 

   - Use the Markov chain model for a single game of tennis 

   - Can use the absorption probability equations to solve for **_p_** given **_q_** 

- **Validation** : Validated on real data from 4131 ATP / WTA matches 



<!-- Start of picture text -->
p p p<br>00-00 15-00 30-00 40-00<br>p<br>− − − −<br>1 p 1 p 1 p 1 p<br>Counts<br>p p p p<br>0.7<br>00-15 15-15 30-15 40-15 W 1<br>343<br>p 322<br>− − − −<br>1 p 1 p 1 p 1 p 300<br>p 0.6<br>279<br>p p 258<br>00-30 15-30 30-30 − 40-30<br>1 p 236<br>215<br>0.5<br>− − − 193<br>1 p 1 p 1 p p<br>172<br>p p 151<br>00-40 15-40 30-40 129<br>0.4<br>108<br>86<br>−<br>1 p 65<br>− −<br>1 p 1 p<br>44<br>0.3<br>L 22<br>1<br>0.2 0.3 0.4 0.5 0.6 0.7 0.8<br>1 Point−win probability implied by point−level data<br>Figure : (a) Markov chain model for a single game of tennis, (b) validation<br>Model 2: Bayesian model with logistic link<br>•  Goal : to<br>Map p ( pss , prr )<br>•<br>1 : to the model<br> Step Map p pss using following Bayesian<br> <br> e α + βp <br> <br> <br> <br>ps ∼N [0 , 1]  <br>1 +  e α + βp , σ <br> <br>Need to infer the three α and σ<br>parameters , β ,<br>•<br>2 : Infer to the match-win<br> Step pr by calibrating probability<br>•  Estimation : Estimated using real data from 2465 WTA matches<br>1<br>p s<br>0.9 p r<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>0.2 0.25 0.3 0.35 0.4 0.45 0.5<br>p<br>Figure : “True” data compared against Bayesian predictions<br>Model 3: MDP model<br>Point−win probability from the Markov chain model<br>r<br> or p<br>s<br>p<br><!-- End of picture text -->



- **Goal** : to Map **_p_ (** **_pss_** _,_ **_prr_ )** 

- **1** : to the model 

- **Step** Map **_p pss_** using following Bayesian 



- **Estimation** : Estimated using real data from 2465 WTA matches 



## **Mapping ratings difference to handicap** 



• **Goal** : Map **_d_** to **_h_** 

- We have already mapped match scores to handicap **_h_** 

- Each match score has a corresponding ratings difference **_d_** 

- **Model** : **_h_** = **_γd_** fitted in a Bayesian fashion 

**_h_** _∼N_ **_τ_** ( **_γd_** _,_ ) 

- **Result** : **_h_** _≈_ **11** **_d_** (using data from 3686 amateur matches) 



<!-- Start of picture text -->
Counts 45<br>1 set<br>10 2 sets<br>636<br>40 3 sets<br>596<br>557 35.13<br>35<br>517<br>477<br>0 30<br>438<br>398<br>25 24.52<br>358 23.36<br>318<br>279 20<br>−10<br>239 16.11  16.3<br>199 15<br>160 11.75<br>10.48<br>120 10  9.86<br> 8.19   8.2<br>80<br>−20  6.23<br>41  5.42  5.16<br>5<br> 3.29  3.73<br>1  2.75<br> 2.34<br> 1.26<br>−1 −0.5 0 0.5 1 0<br>6-1 6-2 6-3 6-4 7-5 7-6<br>Ratings difference Score<br>Figure : (a) Handicap against ratings difference, (b) handicaps via heuristic<br>Handicap<br>Handicap<br><!-- End of picture text -->

## **Heuristic** 



- Some players might not have a rating but know the expected set score 

• **Idea** : Map set scores to handicaps 

## **Implementation considerations** 



- a tennis can a 

- Multiple ways organization implement handicap system 

- **1** : Track data to estimate and to **_h_** 

- **Way** **_p_** map using [1] 

- **Way 2** : Use the heuristic presented above 

- **Way 3** : Adopt a rating system and use the models presented here 

## **Conclusion** 



- a novel to match scores to to 

- Developed approach map **_p_ (** **_ps_ ,** **_pr_ )** 

- Rigorously mapped a tennis rating system to handicaps for amateurs 

- Validated models on real data from thousands of matches 

> • Designed an easy to remember heuristic for handicaps • Suggested ways to implement a handicap system in real life **References** [1] Timothy CY Chan and Raghav Singal. A Markov Decision Processbased handicap system for tennis. _Journal of Quantitative Analysis in Sports_ , 12(4):179–188, 2016. 



> • = Finally, regress **_h_** against **_d_** to obtain the linear mapping **_h γd_** 

to **_h_** the MDP model Map **(** **_ps_** _,_ **_pr_ )** using proposed by [1] 


