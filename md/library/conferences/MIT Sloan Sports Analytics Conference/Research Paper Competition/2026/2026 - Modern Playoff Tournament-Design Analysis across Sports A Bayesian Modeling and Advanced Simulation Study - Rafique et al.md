<!-- source: library/conferences/MIT Sloan Sports Analytics Conference/Research Paper Competition/2026/2026 - Modern Playoff Tournament-Design Analysis across Sports A Bayesian Modeling and Advanced Simulation Study - Rafique et al.pdf -->

# **Modern Playoff Tournament-Design Analysis across Sports: A Bayesian Modeling and Advanced Simulation Study** 

Hassan Rafique and Shane Sanders Department of Sport Analytics, Falk College of Sport, Syracuse University 

## **1. Introduction** 

The global spectator sports market was valued at $178.74 billion in 2024, following robust annual growth in recent years (Yahoo Finance, 2025). Buoyed by the digital age and recent competition format experimentation, e.g., in the Summer Olympics, Major League Baseball, Indian Premier League (IPL) Cricket, Pakistan Super League (PSL) Cricket, the FIFA World Cup, the NBA Playoffs, and College Football, sports viewership increases have supported these revenue gains. The 2020 Summer Olympics attracted approximately 3 billion viewers, the World Series approximately 238 million total unique viewers, the IPL final more than 1 billion digital and television viewers, the 2022 FIFA World Cup Final approximately 1.5 billion viewers, and the 2025 Super Bowl a record 127.7 million U.S. viewers. 

Rules are fundamental to sport’s functioning. Moreover, the sport business and sport management literatures have identified tournament and competition design, an increasingly important function of sport operations and analytics groups within leagues, as a vital aspect of continued growth in sport attendance [1,2]. Tournament design refers to the set of rules governing tournament structure, encompassing the group of contestants, competitive format, schedule, and ranking [3]. Thus, “designing an optimal contest is both a matter of significant financial concern for the organizers, participating individuals, and teams, and a matter of consuming personal interest for millions of fans” (Szymanski 2003)[4]. 

Ostensibly, this level of importance helps to explain several recent, high-profile cases of tournament design experimentation. Even before such experimentation, however, new tournament designs can be optimized vis-à-vis key, established axioms of tournament viability. Within such an approach, axioms are specified from the literature and designs pre-tested using simulation, advanced modeling, and optimization approaches. This model-based approach is much less opportunity costly than the approach of real-world trial and error. For example, the College Football Playoff (CFP) has undertaken several modifications to varying success in recent years. Some of these stepping-stone tournament design iterations may have been circumvented through the proactive use of a design approach that optimizes key desired tournament features. In the traditional tournament design literature, these axiomatic features include: 1) **<u>Efficacy</u>** : revelation of true teamranking, in expectation, via a play of the tournament; 2) **<u>Fairness</u>** <u>: Team win likelihoods increase in</u> true (perhaps unknown but to the modeler) team strengths; 3) **<u>Attractiveness</u>** <u>: The tournament</u> generates excitement, exposure, and financial viability to the League. 

Herein, we evaluate newly-adopted hybrid tournament designs from IPL, PSL, and BPL Cricket, as well as the NBA Conference-level Play-In Tournaments and the current NCAA CFP, against classical 



1 

designs from post-group play in certain Olympic tournaments, the original CFP format from 20142023, and NCAA Basketball. This analysis will first evaluate optimal Final 4 tournament designs, and expansions therefrom. In the traditional tournament design literature, the [1 versus 4, 2 versus 3] Final 4 format, as used in post-group play for certain Summer Olympic sports, the original CFP from 2014-2023, and the NCAA Women’s and Men’s Basketball Tournaments should the expected, or top-bracketed, Final Four emerge. This format is found to dominate all other single-elimination tournament designs in terms of efficacy and fairness [5]. As is often stated in economics, there is no easy _a priori_ accounting for preferences (i.e., the attractiveness axiom). However, there is a clear accounting for the axioms of efficacy and fairness, and we will do so to compare classic and alternative tournament formats using discrete mathematical derivation, and optimization-based modeling techniques. 

Namely, we pit the optimized, classic single-elimination format of [1 versus 4, 2 versus 3] against an increasingly high-profile hybrid format, the Page Playoff System (PPS), to determine if top-bracket double-elimination concessions can improve efficacy and fairness against the best-in-class singleelimination format. This remains an open, but increasingly important, question in the literature. In recent years, the PPS has been implemented in prominent sports leagues around the world, including the IPL, PSL, and BPL cricket playoffs and the NBA Play-In Tournament. The PPS may improve upon classic single-elimination formats by providing a top-bracket concession. We further consider the role of top-bracket concessions when used to expand a tournament, the CFP, from 4 to 12 teams. The CFP tournament design expanded to a non-binary number, necessitating that some teams–the top 4 teams in this case–receive a bye. Does this alternative top-bracket concession preserve or deteriorate efficacy and fairness? 

By evaluating evolving tournament designs against their predecessors in this manner, we can help teams streamline efforts to create stable tournament designs that provide dynamic, meritorious incentives for teams to field the best teams possible. 

## **2. Methods and Results** 

**2.1 Four-team Knockout Playoffs** We first consider the 4-team single-elimination knockout playoff-design. Let [(1,2), (3,4)], and be the distinct possible draws, where is treated in the literature as the best classical, single-elimination draw with respect to the key tournament design 𝐴𝐴= [(1,4], (2,3)], 𝐵𝐵= criteria from the literature, as defined in the introduction.   𝐶𝐶= [(1,3), (2,4)] 𝐴𝐴 

The PPS (see Figure 1) is an alternative 4-team hybrid knockout playoff-design, used in professional cricket (Indian Premier League, Pakistan Super League, Bangladesh Premier League, NBA Play-In Tournament), curling, and softball. It provides an advantage to the top-two seeds in a Final 4 by providing them with a double-elimination safety net. The performance of the PPS relative to the optimized single-elimination format and with respect to key design criteria is heretofore unknown. 



2 



_Figure 1: Page playoff system with double elimination for top bracket vs the famous 4 team single elimination design._ 

PPS is an elaboration of Draw B with a top-bracket double-elimination provision. PPS increases the chance of top-team(s) winning in four-team playoffs and therefore may overcome the design shortcomings of a standard Draw B format, as shown in the previous literature and extended herein. 

**2.1.1 Knockout Playoffs Analysis Methodology** Assume teams can be ranked best-to-worst and are numbered accordingly . Let 𝑖 ) denote the probability-matrix, where 𝑖 represents the probability team i beats team j, The matrix 𝑖 ) specifies the relative strength of the teams. We make the 1,2, . . . , 𝑛𝑛 𝑃𝑃= (𝑝𝑝 following assumptions of . 𝑝𝑝 1 ≤ 𝑖𝑖 < 𝑗𝑗 ≤ 𝑛𝑛. 𝑛𝑛 × 𝑛𝑛 𝑃𝑃= (𝑝𝑝 𝑛𝑛 _A1._ 𝑖 ≤ 1 for 𝑃𝑃 and 𝑖 ≤ 0.5 for [ The better team has a higher chance of winning a match between two teams.] 0.5 ≤𝑝𝑝 𝑖𝑖 ≤ 𝑗𝑗 , 0 ≤𝑝𝑝 𝑖𝑖 ≥ 𝑗𝑗 . _A2_ . = 1 [ No Draws] 𝑖𝑖,𝑖𝑖 𝑖𝑖,𝑖𝑖 _A3._ 𝑝𝑝 is non-decreasing in + 𝑝𝑝 , i.e., is non-decreasing along each row. [If team is stronger than ’, then any third team can more easily defeat ’ than ]. 𝑖𝑖,𝑖𝑖 𝑝𝑝 𝑗𝑗 𝑃𝑃 𝑗𝑗 𝑗𝑗 For a given probability matrix 𝑖𝑖 , let denote the probability that team 𝑗𝑗 𝑗𝑗 wins under Draw . For example, 𝑖𝑖 𝑃𝑃 𝑞𝑞 (𝑋𝑋) 𝑗𝑗 𝑋𝑋 1 14 23 12 32 13 ) We consider fairness in the sense that the better a team is , the better chance it has of winning the 𝑞𝑞 (𝐴𝐴) = 𝑝𝑝 ( 𝑝𝑝 𝑝𝑝 + 𝑝𝑝 𝑝𝑝 tournament. Under this fairness definition, Draw is fair if 1 2 3 4 𝑋𝑋 𝑞𝑞 (𝑋𝑋) ≥ 𝑞𝑞 (𝑋𝑋) ≥ 𝑞𝑞 (𝑋𝑋) ≥ 𝑞𝑞 (𝑋𝑋). 

**Theorem** : Assume _A1_ , _A2_ , and _A3_ . Then among Draws A, B, C, and PPS: 

(X1) PPS maximizes the probability of the best team winning the tournament, where A maximizes among classical designs A, B, and C. 

(X2) A and PPS are fair (chance of winning tournament proportional to team strength). 



3 

[Proof is derived in the Appendix]. 

**2.1.1 Knockout Playoff Design Simulation Results** Without loss of generality, let be team ’s true  strength, where 1 2 > 0. Using a Bradley-Terry statistical learning model, we define 𝑖 ) . This satisfies the 𝑖𝑖 𝑛𝑛 assumptions A1-3. Monte-Carlo simulations verify the Theorem's results by simulating 1 million 𝑠𝑠 𝑖𝑖 𝑠𝑠 ≥ 𝑠𝑠 ≥ ⋯ ≥ 𝑠𝑠 𝑖𝑖 𝑖𝑖 𝑖𝑖 tournaments. We considered ) , where 𝑝𝑝 = 𝑠𝑠) were chosen suitably to a) avoid overlap  / (𝑠𝑠 + 𝑠𝑠 𝑃𝑃 and have strictly different strengths (Figure 2) or b) to have some overlap to show robustness of 𝑖𝑖 𝑖𝑖 𝑖𝑖 𝑖𝑖 𝑖𝑖 the Theorem result (Figure 3). Figures 2 and 3 evaluate the likelihoods that teams win the 𝑠𝑠 ∼𝑈𝑈(𝑎𝑎 , 𝑏𝑏 (𝑎𝑎 , 𝑏𝑏 tournament as a function of their team strength under PPS and Draw A, respectively. In Figure 2, we consider team strengths sampled from distinct, spaced-out uniform distributions, which means that the rank (seed) of the team has the same ordering as their team strength and the theorem conditions are satisfied. 



_Figure 2: PPS and Draw A are fair and show high efficacy. Team strengths were sampled from distinct spaced out uniform distributions: U(a1= 0.9, b1 = 1), U (a2= 0.85, b2 = 0.75), U(a3= 0.7, b3 = 0.6), and U(a4= 0.575, b4 = 0.5)._ 

Figure 2 shows that both PPS and Draw A are ordinally fair. That is, the probability of a team winning is directly ordinal to its rank or team strength. PPS shows much high efficacy than Draw A, however, by maximizing the chance of the top team(s) winning. Note that top teams are pulled sharply right, and bottom teams sharply left, for the same team strength draws from Draw A to PPS in Figure 2. Whereas every dog may have their day, it is difficult for bottom bracket dogs to repeatedly have their day when top bracket teams are provided double elimination. Therefore, topbracket concessions raise efficacy even over the most efficacious single elimination Final 4 design. 



4 

Double elimination for the top 2 teams in PPS explains this shift. For example, a standard singleelimination Draw B is shown to be less efficacious than Draw A even. When Draw B is elaborated upon with top-bracket concessions, however, efficacy rises well above Draw A. In tournaments with longer initial rounds, such as round-robins, it is crucial to account for the performance of topseeded teams, and PPS is a great choice for the playoff portion of such tournaments. 

In the big-data simulation exercise of Figure 3, we let team strength source distributions overlap, which means the rank (seed) of the team isn’t always the same as the order of teams based on strength (i.e., the possibility of inefficient seeding). Even under these inefficient seeding conditions, PPS demonstrates a markedly high level of efficacy relative to Draw A, with no distributional overlap between the probability of tournament victory for either of the top 2 teams by strength with either of the bottom 2 teams by strength. This shows that, under PPS, strong teams can retain a high chance of winning the tournament even if they are seeded (ranked) lower in the tournament bracket. That is, the PPS is compensatory of small-to-moderate seeding inefficiencies in a manner that Draw A, or any single-elimination draw, is not. For Draw A, it is interesting to note that, with overlapping team strengths, the win probability distributions shift closer to one another. This can potentially lead to relatively more upsets (lower ranked teams winning the tournament), which may relate to attractiveness for some fan bases. Additional data that links tournament upsets to viewership changes is needed to make this potential connection definitive. 



_Figure 3: Overlapping team strengths show the robustness of PPS. Teams with higher strength but lower rank (seed) can still win.  Uniform distributions: U(a1= 0.9, b1 = 1), U (a2= 0.83, b2 = 0.93), U(a3= 0.75, b3 = 0.85), and U(a4= 0.68, b4 = 0.78)._ 

### **2.2 College Football Playoffs** 

The NCAA FBS football playoffs are among the main topics of discussion in U.S. collegiate athletics. The College Football Playoff (CFP) was established in the 2014 season to replace the Bowl Championship Series, aiming to provide a more definitive and equitable method for crowning a 



5 

national champion. Over its first decade (2014–2023), the format consisted of a four-team bracket selected by a committee. This design model often drew criticism for limiting tournament access to only a few dominant programs. Motivated by the need for broader inclusivity and increased engagement, the playoff expanded to a 12-team format beginning in the 2024 season. The expansion introduced on-campus, first-round games hosted by seeds 5–8, and granted first-round byes to the top-four seeds. The format has continued to evolve rapidly; while the 2024 model awarded byes to the top-four conference champions, the 2025 format is set to transition to straight seeding, where the top-four _ranked_ teams receive byes regardless of conference championship status, further prioritizing team strength over conference affiliation. We will show that this was indeed the correct decision by the CFP. 

Fan interest in the College Football Playoff (CFP) has remained high through these design iterations, with some ups-and-downs. Viewership peaked immediately with the inaugural 2015 Championship game between Ohio State and Oregon, which drew a record 34.1 million viewers. While ratings dipped to a low of 17.2 million for the uncompetitive 2023 Georgia-TCU blowout, they rebounded to 25 million for the 2024 final. The transition to the 12-team format in the 202425 season maintained strong engagement, with the Championship game drawing 22.1 million viewers despite scheduling challenges, while early-round, on-campus games generated significant local digital engagement lifts for participating schools. This devotion is perhaps best measured by the exorbitant costs fans are willing to absorb; average ticket prices for the National Championship have frequently topped $2,000, with the 2025 Championship game shattering records at an average purchase price of approximately $2,637. Beyond tickets, the expanded playoff format has intensified the travel burden, as fans making a deep postseason run now face cumulative travel costs that can exceed thousands of dollars for flights and lodging across multiple rounds. 

### **2.2.1 12-Team Playoff Format** 

We analyze the new 12-team College football playoff format and consider changes from 2024-25to-2025-26, particularly focusing on the conference champs getting a bye in the 2024 season. The 2024 season gave byes to the top 4 conference champions and a playoff spot for all power-5 conference champions, creating a scenario in which ASU, ranked 12, received a bye and the fourth seed. Also, Clemson, ranked 16, made the playoffs with the twelfth seed. The team rankings are announced by the CFP and, for our next simulation analysis of Figure 4, we assume they reflect the true strength of teams. Note that the CFP ranking may not always be based on true team strengths, and there are other objective methods to rank FBS teams, as we will show later. 

Considering the nature of the sport and existing modeling literature [6], we assume a _ThurstoneMosteller_ stochastic-transitivity model, 𝑖 , where is team i’s strength parameter, accounts for home-advantage, and 𝑖𝑖 represents a standard normal CDF. We assume 𝑖𝑖 𝑖𝑖 𝑝𝑝 = 𝛷𝛷�𝜃𝜃 −𝜃𝜃 + 𝜂𝜂� 𝜃𝜃 1 2 ) follows a multivariate normal distribution. Strength parameter values can 𝜂𝜂 𝛷𝛷 be estimated using historical data and a Bayesian state-space model. However, we sampled these 𝑛𝑛 𝑖𝑖 𝜃𝜃 = (𝜃𝜃 , 𝜃𝜃 , ⋯, 𝜃𝜃 𝜃𝜃 values from a multivariate normal distribution for this simulation. We simulate College Football Playoff iterations under 2025-26 rules, with and without home advantage, for Round 1 games, and under 2024-25 playoff-rules, where the four highest ranked conference champions received a firstround bye. To simulate the 2024-25 scenario, we randomly selected 4 teams from the 12 playoff teams. 



6 



_Figure 4: Note the degree to which the rule whereby conference champions received a bye and playoff spot affected the tournament win probabilities for the 2024 season simulation iterations. Some better teams, by strength, were pushed lower in seeding, and it shows. Results are from 50,000 simulated tournaments._ 

Figure 4 cell values are probability estimates (as percentages) of winning the tournament for given seed and tournament design, from 50,000 simulated tournaments. The tournament game outcomes are generated conditional on the simulated team strengths, , with equally-spaced strengths and equal (moderate) uncertainty. As expected, the top 4 seeds have a significantly higher chance of 𝑖𝑖 winning the tournament, which makes winning one’s conference a high priority in the 12-team 𝜃𝜃 playoff. An interesting bi-modal pattern emerges for the 24-25 season, in which conference champions are seeded higher. Since conference champions could have been ranked lower but were moved to a higher seed, this seeding shift disrupts the probability distribution of the winner with respect to seed and lowers the efficacy and fairness of the tournament. The CFP made the correct decision to change the bye rule and award it to the top 4 ranked teams, regardless of conference champion status, in the 2025 season. This clearly and substantially raised efficacy and fairness according to the simulation results. With proactive tournament design optimization, the CFP may have avoided this inefficacious feature altogether. 

### **2.2.2 College Football Rating System** 



7 

Glickman and Stern [7] developed a Bayesian state-space model to estimate NFL team scores and game outcomes. The critical element of their approach is the estimation of team strengths, which are expected to vary over time. Their model accounts for this source of variability by modeling football game outcomes with a state-space model that assumes team-strength parameters follow a first-order autoregressive process. The model accounts for season-to-season changes driven by personnel shifts and other longer-term factors. Their model also incorporates a home-field advantage, while allowing for the possibility that its magnitude may vary across teams. The aim of the analysis is to obtain plausible inferences concerning team strengths and other model parameters, and to predict future game outcomes.  The model details are presented in Figure 5. 

The Glickman and Stern model approach provides a natural solution for estimating team strengths in College Football, as they rely on game-score differentials, account for home field advantage, and allow the team strength parameters to vary across years. Also, their framework provides a methodology to simulate game outcomes, which we will utilize later in the analysis. 



_Figure 5: Glickman and Stern model for team strength and game outcomes._ 

We use FBS regular season data from 2014 - 24 to model the Glickman team ratings (strength). Figure 6 shows the distribution of team rating (strength) grouped by conference over the years. SEC teams have dominated FBS for a decade. Figure 7 shows the top 12 teams by Glickman Rating for 2024. The Glickman ratings come with uncertainty estimates; ratings for different conferences with credible interval bands are presented in Figure 8. 



8 



_Figure 6: FBS team strengths grouped by conference over a decade. SEC, Big Ten and Big 12 teams have dominated the FBS since 2015._ 



_Figure 7: Top 12 teams based on Glickman rating, from 2024, are shown._ 



9 



_Figure 8: Glickman ratings for different conferences, evolution of ratings for the top 5 teams from 24 season._ 

Top teams, from the 2024 season, based on Glickman ratings are presented in Figure 7. Nine of those teams were in the playoffs, while the three teams that didn’t make the playoffs were South Carolina, Mississippi and Miami. None of these three teams were Conference champions, which made it very difficult to reach the playoffs at that time. Note that Mississippi and South Carolina are from a very competitive SEC Conference. 

In Figure 9, we compare the final 2024 CFP Top 25 rankings with the top 25 teams based on the Glickman Bayesian ratings for team strength. Note that the Glickman Bayesian model uses only score differential and home field advantage for the within conference regular season games. Also, these ratings are not adjusted to consider conference championship tickets to reach the playoffs. There is a strong harmony at the top of the CFP rankings, and 9 teams share the top 12 rank in both ranking systems. Clemson, ranked 16 in CFP and 15 in Glickman, reached the playoffs by virtue of a Conference Championship. Arizona State was also a Conference Champion. 



10 



_Figure 9: The table compares CFP and Glickman rankings, 2024 season . Interesting to note the harmony in selecting the top 12 teams._ 



11 





12 



_Figure 10: We further back-test the CFP top 4 rankings against the Glickman model ratings. 64% of instances match up, where both committee and model pick the same teams for top 4._ 



13 

Figure 10 shows the degree to which the model and CFP Committee matched up in selecting the top 4 (playoff) teams from 2015 - 23, 64% of teams matched. The conference championships could have impacted the Committee’s decision in some cases, since in quite a few mis-matched cases the CFP and model rank are close. E.g. 2016 Clemson (CFP-2 vs Model-5), 2017 Georgia (CFP-3 vs Model-5), 2018 Oklahoma (CFP-4 vs Model-5), 2023 Texas (CFP-3 vs Model-5). To further validate the effectiveness of the Glickman model, we simulate the 2024 playoff using the model outputs. We supplied the bracket (teams) to the model, and the model used the team rating estimates to predict the outcome of each game along with the simulated scoreline and model confidence (probability) estimate. The model predicts all the outcomes correctly, meaning the actual outcome of games matched the predicted outcomes. Hence, the model correctly predicted the winner, OSU, with a simulated score of  26-25 (actual was 34-23) with model confidence of 53%. The Appendix contains the Glickman model’s predictions for the 2025 playoff (Figure 12). 



_Figure 11: Glickman model predictions 100% match the actual outcomes of the 2024 playoffs, correctly predicting the winner. Sim represents the simulation predicted score with model confidence in % next to it. Act shows the actual score. See Appendix for 2025 playoff predictions, the brackets came out the day of submission deadline._ 

The Glickman model  provides a comprehensive framework to estimate team performances in College Football. The model predictions align well with outcomes, making the model an excellent candidate for analysis support to CFP’s decision making. The NCAA Soccer committee is known to use Ratings Percentage Index (RPI), along with other factors to inform their playoff selection 



14 

process. The NCAA Basketball Tournament Selection Committee uses Google’s NET rating model. The CFP can effectively use an open source model, such as Glickman ratings, to assist their decision making and objectively decide edge cases. 

## **3. Conclusion** 

This study demonstrates that tournament design can be optimized along impactful criteria or axioms using simulation and discrete mathematical analysis. In some cases, such optimization can explain unsatisfactory tournament designs that required years to correct, as in the case of the College Football Playoffs. Further, effective tournament design can provide teams with stronger incentives to field strong rosters toward playoff success. In turn, stronger play in a league can dynamically shift out demand in its own right. Indeed, tournament and competition format design are chief analytic functions of leagues. 

We also find in our study that other recently mainstream hybrid tournament designs eclipse the optimized, classic, single-elimination designs in terms of efficacy and fairness. A comparison of alternative designs illuminates the trade-offs between fairness and efficacy. We prove a theorem showing the fairness and high efficacy properties of the Page Playoff System. When contrasting the Page Playoff System with the standard Draw A bracket, distinct structural incentives emerge. The Page Playoff System minimizes the risk of premature elimination for top seeds by offering a “double chance” mechanism, thereby strongly rewarding consistent, season-long excellence. The specification of a Page Playoff System by the NBA (Play-In Tournament) and leading professional cricket leagues improves the meritorious nature of playoff outcomes in those leagues. The Page Playoff System is particularly well-suited to tournaments with longer initial rounds (such as round robins). The traditional Draw A is fair and is still a viable alternative when extra games are not feasible in the playoffs. 

Our analysis demonstrates that the College Football Playoff’s 2025 transition to “straight seeding” corrects a critical inefficiency in the 2024 CFP format. The 2024 model’s prioritization of Conference Champions created a bimodal distortion that effectively penalized high-performing non-champions. By removing these constraints, the 2025 format restores a meritocratic distribution of success probabilities. Additionally, our analysis confirms that the vast advantage of winning one’s Conference is ascending to the playoffs and receiving a first-round bye. Furthermore, we demonstrate the effectiveness of modeling frameworks, such as the Glickman model, for analyzing team performance and appropriately rating teams for playoff consideration. In the future, the CFP would be well-served to follow NCAA Basketball and Soccer Selection Committees by seeking structured statistical model support. This would allow the CFP to minimize the design pitfalls and growing pains it has experienced throughout its existence. 

Ultimately, as postseason formats grow in complexity and financial scale, structural decisions should no longer rely solely on intuition or tradition. This research underscores the need to integrate rigorous probabilistic modeling into the design process. By conducting appropriate simulation analyses that vary constraints, administrators can empirically balance the competing demands of entertainment value, revenue, and competitive equity, ensuring that the tournament's architecture honors the integrity of the sport and the demands of fans. 



15 

## **References** 

[1] Solntsev, Ilya & Kurov, Andrey. (2024). Sports Tournament Design as a Source of Economic Impact (Through the Example of Russian Premier League). Journal of Applied Economic Research. 23. 304-340. 10.15826/vestnik.2024.23.2.013. 

[2] <mark>Reilly, B., & Witt, R. (2021). The Effect of League Design on Spectator Attendance: A Regression Discontinuity Design Approach.</mark> _<mark>Journal of Sports Economics</mark>_ <mark>,</mark> _<mark>22</mark>_ <mark>(5), 514-545.</mark> <u><mark>https://doi.org/10.1177/1527002521989393</mark></u> <mark>[3] Devriesere, K., Csat'o, L., & Goossens, D.R. (2024). Tournament design: A review from an operational research perspective.</mark> _<mark>Eur. J. Oper. Res., 324</mark>_ <mark>, 1-21.</mark> 

<mark>[4] Szymanski, S. (2003). The economic design of sporting contests. Journal of Economic Literature, 41(4):1137–1187.</mark> 

[5]  Horen, J., & Riezman, R. (1985). Comparing draws for single elimination tournaments. _Operations Research_ , _33_ (2), 249–262. 

<mark>[6] Hennessy, J.P., & Glickman, M.E. (2015). Bayesian optimal design of fixed knockout tournament brackets.</mark> _<mark>Journal of Quantitative Analysis in Sports, 12</mark>_ <mark>, 1 - 15.</mark> 

[7] <mark>Glickman, M. E., & Stern, H. S. (1998). A State-Space Model for National Football League Scores.</mark> _<mark>Journal of the American Statistical Association</mark>_ <mark>,</mark> _<mark>93</mark>_ <mark>(441), 25–35.</mark> <u><mark>https://doi.org/10.1080/01621459.1998.10474084</mark></u> 

## **Appendix** 

Check next page for 2025 playoff predictions and theorem proof. 



16 



_Figure 12: The Glickman model’s 2025 playoff prediction. Indiana winning against Ohio State, with a prediction for a close game. The simulation was conducted on Dec 7th, the day CFP announces the playoff bracket and the paper submission deadline._ 

Theorem Proof: Draw A maximizes the probability of best team winning among draws A, B, and C. See [1]. To show PPS maximizes the probability of best team winning, we just need to show that q1(PPS) ≥ q1(A), which is same as  q1(PPS) - q1(A) ≥ 0. 

### q1(PPS) - q1(A) = 

(p_12p_34p_23p_12+p_12p_34p_32p_13+p_12p_43p_24p_12+p_12p_43p_42p_14+p_21p_3 4p_13p_12+p_21p_43p_14p_12) - (p_12 p_14 p_23 + p_13 p_14 p_32). Below we will show that this difference is non-negative. 

The proof for fairness is excluded for brevity. But the arguments are the same as for the best team winning (efficacy). 



17 





18 


