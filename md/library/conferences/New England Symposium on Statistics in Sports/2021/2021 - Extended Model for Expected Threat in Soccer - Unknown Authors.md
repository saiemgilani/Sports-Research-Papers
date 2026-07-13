<!-- source: library/conferences/New England Symposium on Statistics in Sports/2021/2021 - Extended Model for Expected Threat in Soccer - Unknown Authors.pdf -->



# Extended Model for Expected Threat in Soccer Jirka Poropudas (SportIQ) and Ville-Pekka Inkilä (Football Assocation of Finland) NESSIS 2021 

## What is the value of ball possession? 

In other words, what is the probability of scoring when a team has the ball at a given location? 





## Expected Threat (xT) 

Originally introduced by Karun Singh in a blog post in 2018. 

- Based on simple Markov chain 

- Only ball event data 

   - No locations for other players 

- Offensive model 

   - Goals for 

- Short time scope 

   - Next 5 events 

https://karun.in/blog/expected-threat.html 

## Expected threat (xT) 

- “Probability of scoring a goal in next 5 events, when in possession of the ball at the given location” 

- Model considers two types of events 

   - Shot at goal from the current location 

      - Scoring probability from a suitable expected goals (xG) model 

   - Movement to another location 

- The field is divided into a grid of locations 

- Event probabilities are calculated from real-life event data 

## Expected Threat (xT) 

∙ ∙ 𝑥𝑇= 𝑆 𝑥𝐺 + 𝑀 𝑃 ∙𝑥𝑇 𝑀 

Definition of expected threat: 

Decision model: 

Dynamics: 

- Shoot or Move 

   - xG 

- Probabilities depend on location 

- Scoring probability 

- Expected goals model! 



• 𝑃 𝑀 

- Move to new location 

- Transition probabilities 

The numerical value of 𝑥𝑇 is solved by iteration. That is, by repeating the equation five times. 

https://karun.in/blog/expected-threat.html 

## Expected Threat (xT) 





https://karun.in/blog/expected-threat.html 

## Two-way xT model 

∙ ∙ ∙ − Definition: 𝑥𝑇= 𝑆 𝑥𝐺 + 𝑀 𝑃 ∙𝑥𝑇+ 𝑇 𝑃 𝑀 𝑇𝑂 ∙( 𝑥𝑇) 



“Decision model”: 

- Shoot 

- Move 

- Turnover 

   - Probabilities depend on location 

Dynamics: 

- xG 

   - Scoring probability 

• 𝑃 𝑀 

- Move to new location 

• 𝑃 𝑇𝑂 

- Move to new location following a turnover 

The minus sign in last term denotes loss of possession! 

## Extended events for xT model 



∙ ∙ ∙ ∙ − ∙ − 𝑥𝑇= 𝑆 𝑥𝐺 + 𝑀 𝑃 ∙𝑥𝑇+ 𝑀 𝑃 ∙𝑥𝑇+ 𝑇 𝑃 +𝑇 𝑃 𝑆 𝑀𝑆 𝐿 𝑀𝐿 𝑆 𝑇𝑂𝑆 ∙( 𝑥𝑇) 𝐿 𝑇𝑂𝐿 ∙( 𝑥𝑇) 

“Decision model”: 

- Shoot 

- Short or Long move 

- Short or Long turnover 

Dynamics: 

- xG 

   - Scoring probability 

- 𝑃 and 𝑃 𝑀𝑆 𝑀𝐿 

   - Move to new location 

- 𝑃 or 𝑃 𝑇𝑂𝑆 𝑇𝑂𝐿 

   - Move to new location following a turnover 

The minus sign in last two terms denotes loss of possession! 

## Move probability 





## Transition probabilities for move events 





## Turnover probability 





## Transition probabilities for turnovers 





## Shot probability and xG model 





## Extended xT 



## Expected value of movement 





## Expected cost of turnovers 





## Expected value of shot 



## Discussion 

- Extended xT model gives a better representation of soccer dynamics 

   - Two-way model includes also opponent’s scoring 

      - Time horizon up to the next shot 

   - More detailed state transitions 

      - Expected value/cost of events 

- Future work 

   - Rewarding players properly for their actions 

      - “xT added” models should consider the expected value of actions? 

   - Include player locations into xT models’ state space? 

      - For example, StatsBomb 360 data 



# Any questions or comments? 

Jirka Poropudas @hamahakkimies jirka.poropudas@gmail.com 


