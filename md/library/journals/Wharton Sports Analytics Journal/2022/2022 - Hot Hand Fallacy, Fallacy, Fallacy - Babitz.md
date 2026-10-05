<!-- source: library/journals/Wharton Sports Analytics Journal/2022/2022 - Hot Hand Fallacy, Fallacy, Fallacy - Babitz.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/hot-hand-fallacy-fallacy-fallacy/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2022 -->
<!-- authors: Kevin Babitz -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

2022, Vol 4 wsb.wharton.upenn.edu/student-research-journal

Hot Hand Fallacy, Fallacy, Fallacy?

Kevin Babitz, W’21

The Wharton School of the University of Pennsylvania, Philadelphia PA, USA

Advisor: Abraham Wyner, PhD The Wharton School of the University of Pennsylvania, Philadelphia PA, USA

Abstract Common across many domains, and especially prevalent in basketball, the ‘hot hand’ suggests that a person who has experienced a recent period of success has a greater likelihood of future success. In basketball, the player with the hot hand who has recently made a series of baskets is more likely to continue their recent success. The seminal research on the hot hand, identifies it as a fallacy after observing 26 Cornell basketball players’ shooting sequences (Gilovich et al., 1985). The shooting percentages observed after a hot streak should be less than those after a cold streak when holding the probability of success and length of the sequence constant. This work instead looks at how much different what we observe is from what we would expect. We call this expected negative difference between the hot and marginal or cold shooting probability a bias adjustment (Miller and Sanjuro, 2018). We extend the hot hand literature in three ways: we add permutation tests and apply more robust hypothesis testing to the resulting p-values to the Cornell dataset, we demonstrate the effectiveness of a new formula to approximate the bias term in the literature, and we apply the hot hand analysis framework to PGA putting data from the 2019 season. The results suggest that the Gilovich et al. paper was close to accurate in determining if the hot hand was true, even with their failure to recognize the bias adjustment needed in the analysis. The hot hand appears to be hard to detect statistically in the Cornell basketball player dataset and PGA putting data using the simulation framework discussed in these analyses. Additionally, we have found a relatively accurate approximation of the bias term used in correctly assessing if a player is significantly hot. key words: basketball, golf, hot hand, shot

Wharton Sports Analytics Student Research Journal

## Introduction

The hot hand literature’s seminal paper calls the hot hand a fallacy after observing 26 Cornell basketball players’ shooting sequences. In this paper, they observed that many of the player’s percentage of made shots on a hot streak in a sequence of 100 shots were less than their percentage on a cold streak. They claim only one of the players is significantly hot (Gilovich et al., 1985). Later research showed that in a randomly generated sequence, we would expect see the results seen in the original paper. The shooting percentages observed after a hot streak should be less than those after a cold streak when holding the probability of success and length of the sequence constant. For that reason, we must instead look at how much different what we observe is from what we would expect. We call this expected negative difference between the hot and marginal or cold shooting probability a bias adjustment (Miller and Sanjuro, 2018).

We explore and extend the hot hand literature in three ways: we add permutation tests and apply more robust hypothesis testing to the resulting p-values to the Cornell dataset, we demonstrate the effectiveness of a new formula to approximate the bias term in the literature, and we apply the hot hand analysis framework to PGA putting data from the 2019 season.

Methods Study 1: Permutation Tests on Cornell Basketball Data

We use the same data that both the Gilovich, Vallone, and Tversky (GVT) and Miller and Sanjuro (MS) papers relied on for our analysis. The data contain shot data from 26 Cornell basketball players, 14 males and 12 females. Each player shot 100 times, from a position on the court they believed to be a 50% probability of success for themselves. From the data, marginal shooting percentages and shooting percentages on hot and cold streaks of length one to three were calculated. The data are seen in Figure 1.

To determine significance of hotness in the data, we formally state the null hypothesis saying that all shots are independent from each other. To conduct significance testing in the Cornell data, we need

Figure 1: Cornell Basketball Player Data from GVT Paper (1985)

Babitz

Wharton Sports Analytics Student Research Journal independently generated sequences to compare to the observed data. We use permutations of the observed Cornell data to do this.

Specifically, we create a sequence of 100 shots (represented as 0’s and 1’s for failure and successrespectively) with an underlying probability of success of the observed probability of success, named P(hit) in Figure 1. We then permute each of these sequences 10,000 times. Permutations were used as they allowed us to assume that the player’s “true” shooting percentage is the one we observe in the study. We can then observe sequences with independence between each shot while making minimal changes to the underlying data.

Figure 2: Male 6's distribution of differences between hot and cold success rates in 10,000 permutations

From these permuted sequences, we can create a distribution of expected differences between hotand cold and hot and marginal shooting probabilities under the null hypothesis. We then comparethese distributions to the observed values to calculate p-values. An example of one of these distributions and comparison of the observed difference can be seen in Figure 2.

From these distributions, we calculate p-values to test for significance in hot handedness when comparing hot and cold shooting success rates (seen in Figure 3) and hot and marginal shooting success rates (seen in Figure 4).

We observe, when using a significance level of 0.05, that five of the players exhibit a significantly hot hand when comparing the hot and cold shooting success rates and just three of the players is significantly hot when comparing hot and marginal shooting success rates. If we use a Bonferroni correction to adjust the false discovery rate for multiple hypotheses, we observe that just one of the players is significantly hot at a significance level of 0.002 (Male number 9).

To calculate significance in the overall data, we use a permuted t-distribution and two methods for combining multiple p-values. To generate the t-distribution, we permute each player’s

Babitz

Wharton Sports Analytics Student Research Journal sequence once, sum the bias adjusted differences between hot and cold or hot and marginal success rates, and do this 10,000 times. We then compare the observed sum of bias adjusted differences to this simulated distribution.

Figure 3 (left) and 4 (right): p-values for each player comparing hot and cold success rates(left) and hot and marginal success rates (right)

When comparing hot and cold success rates, we observe p-values of 0.0115, 0.002, and 0.0008 using our t-test, Stouffer’s Method, and Fisher’s Method, respectively. When comparing hot shooting success rates to marginal shooting success rates, we observe p-values of 0.0377, 0.0165, and 0.0209 using the same methods above.

Finally, we observe that removing the extremely significant player from the data gives us a large change in significance of the hot hand in the overall data. Using hot and cold probabilities, we observe p-values of 0.0101, 0.0115, and 0.0109 using our t-test, Stouffer’s Method, and Fisher’s Method, respectively. When using marginal and hot shooting percentages, we observe p-values of 0.0329, 0.0619, and 0.1456 for the same methods above.

Overall, we observe that only a few players potentially demonstrate a hot hand in the Cornell data. This is similar to the finding in the original GVT paper in 1985 and conflicts with findings from the MS paper from 2018. We observe much of the overall significance is driven by the 9th male player and the significance is magnified by comparing hot and cold shooting percentages rather than hot and marginal shooting percentages.

Babitz

Wharton Sports Analytics Student Research Journal

Study 2: Bias Adjustment Value Formula

We use a similar simulation approach to demonstrate the strength of a formula that does a relatively good job of approximating the bias adjustment value that is necessary for understanding if a player is hot.

We claim the following formula,

(1) 𝑝 ≈ $1 + E (! | 𝐾 > 0- . ∗ Cond − p̂ (L),

" where E (! | 𝐾 > 0- is the expected value of 1 over the number of hot streaks of length L

" observed given that a hot streak occurs in the sequence,

Cond − p̂ (L) is the probability of a successful shot being observedafter a streak of length L given a hot streak occurs in the sequence, and p is the underlying probability of a success for the sequence.

To test the success of this formula, we generate permuted sequences of lengths 50, 100, and 200 with probabilities ranging from 0.3 to 0.7 in increments of 0.05. We generate 10,000 permuted sequences for each length and probability combination and calculate the values in the formula above. We observe the results in figures 5, 6, and 7 below.

Figure 5: Bias Adjustment formula calculations for sequences of length 50

Babitz

Wharton Sports Analytics Student Research Journal

Figure 6: Bias Adjustment formula calculations for sequences of length 100

Figure 7: Bias Adjustment formula calculations for sequences of length 200

In comparing the right-most column to the left-most column, we observe that the hypothesized formula does very well in approximating the underlying probability of the sequences for longer sequences and does relatively well with shorter sequences.

The success of this formula suggests that if we are confident about a player’s true shotting percentage and have a good approximation for one over the expected value of the number of shots taken on a hot streak, we can accurately estimate the player’s expected probability of success on a hot streak and the bias adjustment value.

Study 3: Applying Hot Hand Analysis to PGA Putting Data

We conclude this analysis with an application to professional sports data. It is interesting to apply the framework used to analyze the Cornell basketball shooting dataset to a professional sports context. For this analysis, we use putting data from all PGA tournaments in 2019 tracked on PGA’s ShotLink tracker. We rely on the Strokes Gained statistic, a measure of how good a shot is compared to what the average golfer’s expected outcome would be. Strokes gained is calculated by comparing the number of strokes expected to get the ball in the hole from an old position to the position after the ball is hit and then by subtracting 1 from that difference. These

Babitz

Wharton Sports Analytics Student Research Journal expectations are computed separately for each location on the golf course (fairway, rough, green, etc.) in binned distances of either yards for non-green shots or inches for shots on the green.

For the hot hand analysis, we make three assumptions: a successful putt has a positive or 0 value for strokes gained, all putts in a single round make up a sequence of putts that can be used to consider if a player is “hot” and all rounds are separate from each other, and all players have the same expected strokes from each distance bin and location on a green regardless of the player. Strokes gained is a widely used metric for measuring success of a stroke in golf and these are reasonable assumptions when using this metric.

To calculate hotness in the data, we begin by creating success and failure sequences for each player and for each round using strokes gained (the putt is successful if it has a zero or larger strokes gained value for a particular putt). We then calculate hot and marginal probability of success in each of these sequences where a hot streak is defined as three or more successes in a row. 20,000 permutations are then created for each unique combination of probability and sequence length. Again, hot probabilities and marginal probabilities are calculated for each permuted sequence and sequences with no hot streaks are removed. Finally, we compare the permuted distributions to the observed values for each round to determine statistically significant hot rounds in the data.

From this analysis, we end up with 4425 total rounds from the 2019 season that had at least one hot streak in them. From these rounds, only 72 of them (1.63%) are determined to be significantly hot using the above procedure. No individual player had more than 3 hot rounds in the 2019 season and a majority did not have any hot rounds.

## Conclusion

The results in studies 1 and 2 suggest that the GVT paper was very close to accurate in determining if the hot hand was true, even with their failure to recognize the bias adjustment needed in the analysis. The hot hand appears to be hard to detect statistically in the Cornell basketball player dataset and PGA putting data using the simulation framework discussed in these analyses.

Additionally, we have found a relatively accurate approximation of the bias term used in correctly assessing if a player is significantly hot. We note that the approximation is significantly more accurate as the length of the sequence being analyzed increases but performs relatively well on shorter sequences.

Babitz
