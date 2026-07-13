<!-- source: library/conferences/New England Symposium on Statistics in Sports/2015/2015 - Sampling from the 9,223,372,036,854,775,808 possible brackets in the NCAA men's basketball tournament using the power model - Unknown Authors.pdf -->

# Sampling from the 9,223,372,036,854,775,808 Possible Brackets in the NCAA Men’s Basketball Tournament using the Power Model **Sheldon H. Jacobson, Arash Khatibi, Douglas M. King** 

**Department of Computer Science, University of Illinois at Urbana-Champaign** 

## **Introduction** 

## **Alpha Values** 

## **Evaluation** 

## **Discussion** 

###  ESPN scoring system 

- The NCAA D1 Men’s Basketball Tournament is an  Round of 64 annual single-elimination competition that attracts widespread attention in the United States. 

- 64 teams (after the First Four) compete in four regions, each team assigned a seed number (1 to 16).  Smaller seed numbers represent stronger teams: Seed 1 is the strongest in each region. 

- Generating a bracket is the process of picking the winners of all 63 games. 

- Number of possible brackets: 9,223,372,036,854,775,808 

   - A two-peak distribution of scores 

- 10 points for each correct pick in Round of 64. 

- Value of correct picks in later rounds 



   - One-peak for 2014, where a seed 7 won the championship for the first time 

- Each correct pick worth twice its prior round: correct pick for National Champion is 320 points. 



- Results based on one million generated brackets 



###  Objectives 

- Design a model to capture the probability mass function for all possible brackets. 

- Use the model to sample from this pool of brackets. 





- Round of 32 

- **Power Model**  Models the relative strength of the two teams as a power function of their seed numbers. 

- Estimates the associated parameters using historical **Conclusions** tournament results since 1985 (the modern era). 

- Let p denote the proportion of times seed s1 defeated seed s2 since 1985  The Power Model is an intuitive model to sample from the large pool of possible brackets in the NCAA D1 Men’s Basketball Tournament. 

- The Alpha values summarize the performance history 

- _Distribution of scores in the first three rounds of 2015_ of each seed match up in a round. 

- The Alpha value of seeds s1 and s2 in Round j is _._  Generating a good bracket is more difficult for tournaments with many upsets or two few upsets in the early rounds. 

- computed as  The results show a bell-shaped figure for each round and a two-peak distribution for the whole tournament 

- _Alpha values of Round 3_ 

- _._ 

- Remaining Rounds 

- Probability that s1 defeats s2 in Round j  One Alpha value is used for all match ups, computed as the weighted average of different _Proportion of correct picks in Final Four_ **Acknowledgments** pairs of Alpha values _._ We would like to thank Bleacher Report for featuring our work in 2014.  The Power Model is available at bracketodds.cs.illinois.edu 

- Positive Alpha value: Larger winning probability for stronger seed. 

- Negative Alpha value: Smaller winning probability for stronger seed. 

- Alpha value of zero: Random pick.  Alpha value of infinity: Always pick the stronger seed.  Alpha value of one:  Seeds provide a linear proportion _Proportion of correct picks in Rounds 6 and 7_ of probability of winning (neutral). _._ 

   - The Power Model is an intuitive model to sample from the large pool of possible brackets in the NCAA D1 Men’s Basketball Tournament. 

   - The Alpha values summarize the performance history of each seed match up in a round. 

   - The results show a bell-shaped figure for each round and a two-peak distribution for the whole tournament 

We would like to thank Bleacher Report for featuring our work in 2014.  The Power Model is available at bracketodds.cs.illinois.edu 


