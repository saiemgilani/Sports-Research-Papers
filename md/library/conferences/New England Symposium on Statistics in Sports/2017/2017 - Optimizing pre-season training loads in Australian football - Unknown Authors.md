<!-- source: library/conferences/New England Symposium on Statistics in Sports/2017/2017 - Optimizing pre-season training loads in Australian football - Unknown Authors.pdf -->







**Optimising Pre-Season Training Loads in Australian Football** David L. Carey<sup>a,b</sup> , Justin Crow<sup>b,a</sup> , Kok-Leong Ong<sup>c</sup> , Peter Blanch<sup>d</sup> , Meg E. Morris<sup>a</sup> , Ben J. Dascombe<sup>a</sup> , and Kay M. Crossley<sup>a</sup> See the _a b c d_ animation _La Trobe Sport and Exercise Medicine Research Centre, La Trobe University, Australia; Essendon Football Club; SAS Analytics Innovation Lab, La Trobe University; School of Allied Health Sciences, Griffith University_ @dlcarey88 **<mark>Background Practical Applications</mark>** • **<mark>Methods</mark>** Provides an adaptable framework for physical preparation staff to quickly • create training plans that: 





See the publication 

**<mark>Background</mark>** • Pre-season training is considered crucial in Australian football • It can influence player injury risk and competitive performance • Training load prescription in team sport athletes is a balance between performance improvement and injury risk reduction 

• Training plans were initialised by random sampling from a normal distribution: 

- Satisfy injury risk constraints 

- Optimise training goals 

= 𝜇, 𝜎 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒 3 km, 1 km 

- Are not exposed to subjective biases 

𝜇, 𝜎 = 30 m, 10 m 𝑠𝑝𝑟𝑖𝑛𝑡 

- **Training load – injury relationship** • Relationships have been found between injury rates in Australian football and: • High cumulative running loads (3-4 weeks) (Colby 2014) • High and low relative training loads (Gabbett 2016, Carey 2016) • Commonly quantified using the _acute:chronic workload ratio._ 

- • Ratio of short term (acute) to long term (chronic) loads 

- Optimisation was performed using the MATLAB software package: 

Individualised training plan design 

   - 

- Constrained nonlinear solver (fmincon) 

   - Parameters could be modified for: 

- Sequential quadratic programming algorithm (SQP) 

   - New recruits 

- Default step and function convergence tolerances (10<sup>-6</sup> ) 

- Players returning from injury 

- Different athletic profiles 

# **<mark>Results</mark>** 

Ability to adapt to changing training objectives 

- Able to generate training plans that satisfied relative and absolute 

- 

**Aim** 

- E.g. peaking for multiple important games 

workload constraints (Fig. 1-2) 

• To investigate whether an optimisation approach could generate preseason training plans based on injury risk and performance objectives **<mark>Optimisation approach</mark>** 

- Comparable to those previously reported in professional AFL teams: = 314 −411 km & = 2.7 −8.9 km km 

- 𝜇𝑡𝑜𝑡𝑎𝑙𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒 𝜇 

   - Theoretical framework for testing training strategies and assumptions: 

   - • Can match fitness levels be reached if off-season loads are reduced? 

   - • How much more training can we do if accept higher injury risk? 

- = 2.7 −8.9 km km 

- 𝜇 𝑠𝑝𝑟𝑖𝑛𝑡𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒 

      - 

- Increasing the off-season chronic training loads (Fig 1): 

   - ↑ amounts of ‘safe’ training 



**Decision Variables** 𝑤 𝑖 = 𝑡𝑟𝑎𝑖𝑛𝑖𝑛𝑔𝑙𝑜𝑎𝑑𝑜𝑛𝑑𝑎𝑦𝑖; 𝑖∈{1, 2, … , 125} We considered total training distance and sprint running distance. **Constraints** 1. Daily maximum and minimum: 0 ≤𝑤𝑖 ≤50,000 2. Bounded acute:chronic workload ratio (relative load progression): 𝑖−1 𝑖−1 𝑤 𝑤 𝑗 𝑗 𝑟 = 𝑖 ෍ 6 ෍ 24 ൙ 𝑗=𝑖−6 𝑗=𝑖−24 0.6 < 𝑟 < 1.3 𝑖 (Gabbett 2016, Carey 2016) 3. Maximum cumulative workload (rolling 21 days): 𝑖−1 = 𝐶 𝑤 𝑖 𝑗 ෍ 𝑗=𝑖−21 𝐶𝑖 < 73,721 (Colby 2014) **Objective** _A: Maximise total ‘safe’ training volume_ • Simple objective • Desirable for coaches (want as much time as possible to coach) 125 𝑤 𝑓𝐴 𝑖 𝒘= ෍ 𝑖=1 _B: Maximise projected performance level_ • Banister impulse-response model (Banister 1975) • Reach peak projected performance levels on day of first match 𝑖−1 𝑖−1 − −(𝑖−𝑗) 𝑖−𝑗 𝑡 𝑡 𝑤 𝑒 1 −𝑘 𝑤 𝑒 2 𝑝𝑖 = 𝑝0 + 𝑘1 𝑗 2 𝑗 ෍ ෍ 𝑗=1 𝑗=1 𝑘1 = 1, 𝑘2 = 2, 𝑡1 = 45, 𝑡2 = 11 (Morton 1990) 𝑓𝐵 𝒘= 𝑝 125 

   - ↑projected performance levels 

- : 

- _Objective A_ 

- • Prescribed frequent, moderate intensity training (Fig 2a,c) 

- • : _Objective B_ 

   - Plans included a taper prior to competition 

   - Favoured more variation in daily training loads (Fig 2b,d) 

   - Gives consideration to fatigue accumulation 



Figure 2: Computer generated optimal pre-season training plans for: (a) distance under objective A, (b) distance under objective B, (c) SD under objective A and (d) SD under objective B.(off-season chronic loads: 14km/week distance and 150m/week SD). **<mark>References</mark>** 1. Banister E, Calvert T, Savage M, Bach T. A systems model of training for athletic performance. _Aust J Sports Med._ 1975. 2. Colby MJ, Dawson B, Heasman J, Rogalski B, Gabbett TJ. Accelerometer and GPS-derived running loads and injury risk in elite Australian footballers. _J Strength Cond Res._ 2014. 3. Soligard T, Schwellnus M, Alonso J-M, et al. How much is too much?(Part 1) International Olympic Committee consensus statement on load in sport and risk of injury. _Br J Sports Med._ 2016. 4. Gabbett TJ. The training—injury prevention paradox: should athletes be training smarter and harder? _Br J Sports Med._ 2016. 5. Drew MK, Finch CF. The Relationship Between Training Load and Injury, Illness and Soreness: A Systematic and Literature Review. _Sports Med._ 2016. 6. Borresen J, Lambert MI. The quantification of training load, the training response and the effect on performance. _Sports Med._ 2009. 7. Fitz-Clarke JR, Morton RH, Banister EW. Optimizing athletic performance by influence curves. _J Appl Physiol._ 1991. 8. Hellard P, Avalos M, Lacoste L, Barale F, Chatard JC, Millet GP. Assessing the limitations of the Banister model in monitoring training. _J Sport Sci._ 2006. 9. Carey DL, Blanch P, Ong KL, Crossley KM, Crow J, Morris ME. Training loads and injury risk in Australian football-differing acute: chronic workload ratios influence match injury risk. _Br J Sports Med._ 2016. 10. Malone S, Roe M, Doran DA, Gabbett TJ, Collins K. High chronic training loads and exposure to bouts of maximal velocity running reduce injury risk in elite Gaelic football. _J Sci Med Sport._ 2016. 11. Akenhead R, Nassis GP. Training load and player monitoring in high-level football: current practice and perceptions. _IJSPP._ 2016. 12. Schaefer D, Asteroth A, Ludwig M. Training plan evolution based on training models. Innovations in Intelligent SysTems and Applications (INISTA). 2015. 13. Wisbey B, Montgomery PG. _Quantifying AFL Player Demands Using GPS Tracking – 2015 Season._ AFL Research Board Report 2015. 14. Morton RH, Fitz-Clarke JR, Banister EW. Modeling human performance in running. _Journal of applied physiology._ 1990. 15. https://www.strongerbyscience.com/periodization-history-theory/ (2017) 



Figure 1: Convergence of 20 simulated pre-season training plans for: (a) distance under objective A, (b) distance under objective B, (c) SD under objective A and (d) SD under objective B. 


