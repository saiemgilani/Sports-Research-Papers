<!-- source: library/conferences/New England Symposium on Statistics in Sports/2023/2023 - Contextualized Generative Ghosting Model as Benchmark for Evaluating Player Movement in Football - Unknown Authors.pdf -->



Contextualized Generative Ghosting Model as Benchmark for Evaluating Player Movement in Football 

Presenter: Chaoyi Gu (Aaron) 

Authors: Chaoyi Gu, Varuna De Silva, Mike Caine, Ben Smith 



Loughborough University Institute for Digital Technologies Machine Learning Lab 







## About Me 





<!-- Start of picture text -->
<br>Bio:<br><!-- End of picture text -->

 I am a Ph.D. student at Loughborough University. My research is mainly about how to use machine learning methods to analyze big data in soccer to gain insights that can be used to help coaching staff make better tactical decisions. 

Bio: https://www.lborolondon.ac.uk/about/doctoral-researchers/chaoyi-gu/ 

Linkedin: https://www.linkedin.com/in/aaron-gu-226027129/ 





## Introduction 

- Current analytical models in soccer: 



<!-- Start of picture text -->
 Xg mode (Rathke, 2017)<br><br><br><br><!-- End of picture text -->

- Xg mode (Rathke, 2017) 

- Expected Possession Value model 

(Fernández, Bornn, and Cervone, 2019) 

   - VAEP model (Decroos et al., 2021) 

- Generative Ghosting model: 







###  Features: 

- Supervised learning with defined input and output 

- Model performance heavily relies on the distribution of training data 

- Cannot answer what-if questions in given context 

###  Features: 

- Combination of unsupervised learning and supervised learning 

- More likely to capture the generative patterns within the data 



- Can answer what-if questions in given context 







## Background 



<!-- Start of picture text -->
Keep walking<br>Starts jogging<br><!-- End of picture text -->

 Deep Generative Model on Time Series Data (Chung et al., 2015) 



<!-- Start of picture text -->
[0.1,..<br>……<br>……<br>..,0.6]<br><!-- End of picture text -->





[0.1,.. [0.2,.. …… Latent Space …… …… …… ..,0.6] ..,0.3] 













## Background 



 Pitch Control (Spearman W, 2018) 





## Data 









<!-- Start of picture text -->
Event Data<br><!-- End of picture text -->





<!-- Start of picture text -->
Professional<br>Soccer Matches<br><!-- End of picture text -->





<!-- Start of picture text -->
… …<br><!-- End of picture text -->











## Data Processing 



- Change data representation 



Instead of directly analyzing tracking and event data, we convert them to another form of representation – pitch control frames 





Event Data Tracking Data 









## Framework of Generative Ghosting 



<!-- Start of picture text -->
Players' Positions<br><!-- End of picture text -->







<!-- Start of picture text -->
Part 1 Part 2<br>Players' Positions<br>Trained<br>Trained<br>Contextualized<br>Generative<br>CNN<br>Model<br>(C Gu and V De Silva, 2023)(https://arxiv.org/abs/2303.13323)<br><!-- End of picture text -->

















Results 









## Conclusion 



- Contributions 



<!-- Start of picture text -->
<br><!-- End of picture text -->

Our deep generative ghosting model can be used as a benchmark for evaluating soccer players’ performance on the pitch. 

This model can be applied in analyzing team movement and individual player’s ability of utilizing open space. 

 Future Direction 

The future research direction can be combining our method with expected goal model to quantify the value of each decision made within the game 









## References 



- Gu, C., & De Silva, V. (2023). Deep Generative Multi-Agent Imitation Model as a Computational Benchmark for Evaluating Human Performance in Complex Interactive Tasks: A Case Study in Football. arXiv preprint arXiv:2303.13323. 



<!-- Start of picture text -->
<br><br><br>Conference.<br><!-- End of picture text -->

- Chung, J., Kastner, K., Dinh, L., Goel, K., Courville, A. C., & Bengio, Y. (2015). A recurrent latent variable model for sequential data. Advances in neural information processing systems, 28. 

- Decroos, T., Bransen, L., Van Haaren, J., & Davis, J. (2021, January). VAEP: an objective approach to valuing on-the-ball actions in soccer. In Proceedings of the Twenty-Ninth International Conference on International Joint Conferences on Artificial Intelligence (pp. 4696-4700). 

- Fernández, J., Bornn, L., & Cervone, D. (2019, March). Decomposing the immeasurable sport: A deep learning expected possession value framework for soccer. In 13th MIT Sloan Sports Analytics Conference. 

- Rathke, A. (2017). An examination of expected goals and shot efficiency in soccer. Journal of Human Sport and Exercise, 12(2), 514-529. 



- Spearman, W. (2018, February). Beyond expected goals. In Proceedings of the 12th MIT sloan sports analytics conference (pp. 1-17). 



End 









# Thanks for listening！ 

**_Any question is welcomed Further discussion can be made via email My email address: C.Gu@lboro.ac.uk_** 




