<!-- source: arXiv preprint 2609.06739, submitted 2026-09-06. Open access under arXiv's non-exclusive licence. -->
<!-- text source: PDF extracted with pypdf from https://arxiv.org/pdf/2609.06739 on 2026-09-09. Layout/columns are flattened to reading order; equations and figures may be imperfectly rendered. Consult the PDF for exact formatting. -->
<!-- arxiv: 2609.06739 · subjects: Applications (stat.AP); General Economics (econ.GN) · Archived from the weekly sports-analytics roundup (2026-09-09). -->

# The profit-bias identity in sports betting: bookmaker profit as the public's prediction error

**Dmochowski, Jacek P.**

*arXiv:2609.06739* (Applications (stat.AP); General Economics (econ.GN)), submitted 2026-09-06. [Abstract](https://arxiv.org/abs/2609.06739) · [PDF](https://arxiv.org/pdf/2609.06739). Open access.

## Abstract
Sports betting moves money continuously from a large public to a small number of firms. The most influential account of that flow, due to Levitt (2004), holds that books price away from the market-clearing point to exploit predictable public biases. It computes profit from two numbers (the probability that a side wins the proposition and the fraction of handle it attracts), treating the share on a side as independent of the outcome. Here we relax that assumption and derive a profit-bias identity: profit is affine and increasing in the expected share of handle on the losing side, with Levitt's expression as the special case of independence. The identity resolves the book's margin into exactly three channels: its hold, the product of its price shading and the public's lean, and the covariance between bet share and outcome. A lean is thus worthless without shading, and shading is worthless without a lean. Under a public-belief model, the profit driver is the public's Bayes error: the probability of a representative bettor selecting the losing side. We provide necessary and sufficient conditions for a &#34;Goldilocks Zone&#34;: prices at which book and bettor both profit. Testing these predictions on 1,139 Major League Baseball games, we find that the apparent dependence between bet share and outcome is a Simpson's paradox: present when games are pooled, but absent once they are separated by which side the book favored. The public leans heavily toward favorites, but we detect no matching shading, and the realized margin is indistinguishable from the hold.

## Full text (extracted)

THE PROFIT–BIAS IDENTITY IN SPORTS BETTING:BOOKMAKER
PROFIT AS THE PUBLIC’S PREDICTION ERROR
Jacek P. Dmochowski
Department of Biomedical Engineering
City College of New York
New York, NY 10031
jdmochowski@ccny.cuny.edu
September 9, 2026
ABSTRACT
Sports betting moves money continuously from a large public to a small number of firms. The
most influential account of that flow, due to Levitt (2004), holds that books price away from the
market-clearing point to exploit predictable public biases. It computes profit from two numbers (the
probability that a side wins the proposition and the fraction of handle it attracts), treating the share
on a side as independent of the outcome. Here we relax that assumption and derive aprofit–bias
identity: profit is affine and increasing in the expected share of handle on the losing side, with
Levitt’s expression as the special case of independence. The identity resolves the book’s margin
into exactly three channels: its hold, the product of its price shading and the public’s lean, and the
covariance between bet share and outcome. A lean is thus worthless without shading, and shading
is worthless without a lean. Under a public-belief model, the profit driver is the public’s Bayes
error: the probability of a representative bettor selecting the losing side. We provide necessary and
sufficient conditions for a “Goldilocks Zone”: prices at which bookandbettor both profit. Testing
these predictions on 1,139 Major League Baseball games, we find that the apparent dependence
between bet share and outcome is a Simpson’s paradox: present when games are pooled, but absent
once they are separated by which side the book favored. The public leans heavily toward favorites,
but we detect no matching shading, and the realized margin is indistinguishable from the hold.
Introduction
Every account of how a sportsbook makes money rests on a claim about where the betting public’s money goes relative
to the price at which it was offered. The most influential, due to Levitt [2004], posits that books deliberately price away
from the market-clearing value to exploit predictable biases in public betting as opposed to balancing their exposure.
That model, and the substantial literature testing it [Paul and Weinbach, 2007, 2008, 2009, 2011, 2012, Humphreys,
2010, 2011], computes the book’s expected profit from two numbers: the probability that the favorite covers, and the
fraction of the handle it attracts. Two numbers suffice, as we show, only if the money and the outcome are statistically
independent—only if the side drawing the handle is neither more nor less likely to cover than its posted price implies.
To the best of our knowledge, this assumption has gone unexamined.
Treating the public’s money as unconnected to the outcome discards precisely the information that separates an informed
betting public from an uninformed one, namely whether the side that attracts the money is more or less likely to win.
This distinction is not incidental: a competing account attributes the bookmaker’s margin not to public bias but to
adverse selection against privately informed bettors [Shin, 1991, 1992, 1993], a mechanism recently re-examined and
weighed against ordinary bettor disagreement [Whelan, 2024, 2025]. By assuming independence between bet share and
outcome, Levitt’s model cannot distinguish asharppublic, whose money follows the eventual winner (as the insider
account would predict), from asquareone, whose money follows the eventual loser.
arXiv:2609.06739v1  [stat.AP]  6 Sep 2026

APREPRINT- SEPTEMBER9, 2026
Here we revise the Levitt model to allow a statistical dependence between betting behavior and match outcomes.
Relaxing the independence restriction yields aprofit–bias identity: the sportsbook’s expected profit is an affine function
of the expected share of handle on thelosingside, and it reduces to Levitt’s expression when bet shares are independent
of the outcome. Because the identity presumes neither account, the sharp and square cases can be distinguished
empirically rather than assumed away [Woodland and Woodland, 1994, Gandar et al., 2002, Ottaviani and Sørensen,
2008]. The identity further separates the book’s expected margin into three parts: the hold that a balanced book collects,
a term in which the book’s price shading multiplies the public’s lean, and the covariance between bet share and outcome.
Because the second term is the product of shading and lean, neither factor generates profit on its own: a lean earns
nothing for a book that does not shade, and shading earns nothing when the public does not lean. Under a public-belief
model in which bettors act on a noisy, biased signal of the game [Snowberg and Wolfers, 2010, Jullien and Salanié,
2000, Avery and Chevalier, 1999], the profit-driving quantity is the probability that the public selects the losing side, a
misclassification (Bayes-error) probability. The same formulation characterizes a “Goldilocks Zone” of prices at which
the sportsbook and an infinitesimal bettor can simultaneously profit [Shleifer and Vishny, 1997, Hubáˇcek et al., 2019].
We tested these predictions with data from 1,139 Major League Baseball (MLB) games, finding that the apparent bias
of public money onto the eventual losing side is a Simpson’s paradox: present when games are pooled, and absent once
they are separated by which side the book has designated as the favorite. The public is square in the aggregate but not in
either of its halves. The data do exhibit a strong favorite bias in public betting, butwithoutan accompanying increase in
book profit over its hold, which we connect to the absence of detectable price shading.
Results
Terminology
The forthcoming treatment employs the terminology of sports betting, which is reviewed in Table 1. Of note, the terms
leanandshadingrefer to skews in public betting and sportsbook pricing, respectively, and are often conflated.
Setup and notation
We consider a generic two-sided sportsbook proposition, encompassing point spreads, totals, and player props. Let
the realized outcome be a real-valued random variableM∈R . For spreads,M can be the realized margin of victory
(home score minus visitor score); for totals,M can be total points; for props,M can be a player performance statistic.
The sportsbook posts a lines∈R. Relative tos, we write the possible outcomes as:
home loses⇐⇒M <s,visitor loses⇐⇒M >s,push⇐⇒M=s.
The outcome CDF atsand push probability are given by:
Fm(s)≡Pr(M <s), π push(s)≡Pr(M=s),(1)
such that the complementary CDF is ¯Fm(s)≡Pr(M >s) = 1−F m(s)−π push(s).
Let the (random) fraction of total stake placed on the home side at prices beBh(s)∈[0,1] , and let the fraction placed
on the visitor side beBv(s)≡1−B h(s). We explicitly allow statistical dependence between betting behavior and
the realized outcome (i.e.,Bh(s) may be informative aboutM). We define the conditional expected bet shares on the
eventual losing sideby:
bh,L(s)≡E[B h(s)|M <s], b v,L(s)≡E[B v(s)|M >s].(2)
These quantities capture the fraction of the handle that (in expectation) ends up on the losing side, conditional on which
side actually loses.
The profit–bias identity
We derive the per-game expected profit in the symmetric-vig (ϕh =ϕ v =ϕ ), no-push case (πpush(s) = 0); the general
treatment allowing asymmetric vigsϕh,ϕv∈[0,1] and pushes is deferred to the SI (Sec. S1). Throughout, total stake
is normalized toBh(s) +Bv(s) = 1. The book’s single-game profit isπ(s) =B h(s)−ϕB v(s) when the home side
loses,π(s) =B v(s)−ϕB h(s) when the visitor loses, and π(s) = 0 in the event of a push. Conditioning on the
realized outcome and taking total expectation gives:
E[π(s)] =F m(s)E[Bh(s)−ϕB v(s)|M <s] + ¯Fm(s)E[Bv(s)−ϕB h(s)|M >s].(3)
2

APREPRINT- SEPTEMBER9, 2026
Table 1:Betting terminology.The terms are defined in the point-spread setting, where M is the realized outcome,bh
the public’s home share of handle,p∗ the price-implied probability that the home side wins the bet (with the book’s
commission removed), and ¯Fm = Pr(M >s)is the corresponding true probability.
Term Symbol Meaning
Spreads A number posted by the book. The spread is a handicap applied to one side’s score so
that a wager on either is closer to a 50/50 proposition. The bettor’s task is to predict
whether the outcome will exceed the spread:M >s.
Priceϕ h,ϕ v The profit on a winning unit wager on the home and away sides, respectively. At the
standard−110 priceϕh =ϕ v = 100/110 = 0.909 : the bettor risks 1.10 to win 1.
The special caseϕ h =ϕ v≡ϕis referred to herein assymmetric vig.
CoverM >s A side “covers” when it wins the match taking into account the spread – also called
“beating the spread”. We take the home side to cover whenM >s and to lose the bet
whenM <s.
PushM=s A “push” occurs when the realized outcome is equal to the spread. In this event, all
wagers are returned.
Handle — The total amount staked. Book profit is reported per unit of handle, such that a margin
of4%is four cents kept per dollar wagered.
Vig — The book’s commission, embedded in the prices rather than charged separately. The
vig is the amount by which the sum of the two price-implied probabilities exceeds one:
(1 +ϕ h)−1 + (1 +ϕv)−1−1 . Forϕh =ϕ v =ϕ , the vig is (1−ϕ)/(1 +ϕ) , or 4.8%
at−110. Note that “the vig” is often used inconsistently in practice: sometimes as this
excess, sometimes as the 10% surcharge on the stake, or sometimes as the hold below.
Holdh The share of handle that the book keeps when its liabilities are balanced: its return from
the vig alone,h= (1−ϕ hϕv)/(2 +ϕ h +ϕ v), or (1−ϕ)/2 under a symmetric vig,
giving4.5%at−110.
Shadingθ The deviation of the book’s posted price from the truth,θ=p ∗− ¯Fm. Positive when
the home side is priced as more likely to win than it truly is.
Leanλ The public’s displacement from balanced betting:λ=b h−p ∗. Positive when public
betting favors the home side beyond what is implied by the book price.
Squareδ >0 A public whose money tends to be wagered on the eventualloser, so that the book
profits beyond its hold.
Sharpδ <0 A public whose money tends to be wagered on the eventualwinner(book profits less
than the hold, or takes a loss).
We note also that the term “line” is the generalization of the spreads to markets such as the point total or player props. In
all cases it is a number set by the book that dictates the threshold determining which side wins the wager.
UsingBv = 1−Bh and the conditional losing-side shares(2), the two conditional expectations equal(1+ϕ)b h,L(s)−ϕ
and(1 +ϕ)b v,L(s)−ϕ, respectively, so that:
E[π(s)] =F m(s)

(1 +ϕ)b h,L(s)−ϕ

+ ¯Fm(s)

(1 +ϕ)b v,L(s)−ϕ

.(4)
Collecting the(1 +ϕ)terms and usingF m(s) + ¯Fm(s) = 1in the no-push case yields theprofit–bias identity:
E[π(s)] = (1 +ϕ)Q(s)−ϕ, (5)
where:
Q(s)≡b h,L(s) Pr(M <s) +bv,L(s) Pr(M >s)(6)
is the expected fraction of handle wagered on the losing side. Becausebh,L(s) andbv,L(s) are conditional losing-side
shares,Q(s) admits arbitrary dependence between betting and outcome, and the book’s expected profit is affine and
strictly increasing in it.
The profit-bias identity generalizes the bookmaker-profit expression of Levitt [2004]. Namely, when bet shares are
independent of the outcome, the two coincide. However, whenever public betting covaries with the realized outcome,
the expressions deviate. Levitt’s book profit underestimates the true value whenever the public allocates a larger stake
on the eventual losing side, while overestimating when the stake favors the winning side. The mathematical relationship
between the profit-bias identity and Levitt’s bookmaker profit is detailed in SI, Sec. S2.
Independence of bet shares from the outcome is the pair of conditions: bh,L(s) =b h(s) and bv,L(s) =b v(s),
where bh(s)≡E[B h(s)] and bv(s)≡1−b h(s) are the unconditional shares. Denoting the winning-side home
3

APREPRINT- SEPTEMBER9, 2026
share by bh,W (s)≡E[B h(s)|M > s] , the unconditional share is a convex combination of the two: bh(s) =
Fm(s)bh,L(s) + ¯Fm(s)bh,W (s). Note thatbh,L(s) =b h(s) can only be satisfied whenbh,L(s) =b h,W (s). Similarly,
bv,L(s) =b v(s)requiresb v,L(s) =b V,W (s). The two conditions therefore collapse to:
δ(s)≡b h,L(s)−b h,W (s) = 0, (7)
which is the discrepancy between the expected home stake share in games the home side loses versus wins. Thus, in
order to test whether bet shares covary with realized outcomes, one evaluatesδ(s)against zero.
The identity (5) attributes the book’s entire margin toQ(s), but does not afford insight into the sources of its variation.
To that end, we write the book’sshadingand the public’sleanas signed deviations:
θ(s)≡F m(s)− 1
2, λ(s)≡b h(s)− 1
2,(8)
such thatθ(s)>0 when the spread exceeds the median outcome andλ(s)>0 when public betting favors the home
side. This allows us to decompose the losing-side share into three distinct and interpretable components.
Proposition 1(Anatomy of the book’s margin).Under a symmetric vigϕand no pushes:
Q(s) = 1
2 + 2θ(s)λ(s) + 2Fm(s) ¯Fm(s)δ(s),(9)
and therefore:
E[π(s)] = 1−ϕ
2|{z}
hold
+ 2(1 +ϕ)
h
θ(s)λ(s)| {z }
shading×lean
+F m(s) ¯Fm(s)δ(s)| {z }
outcome covariance
i
.(10)
The book’s expected margin exceeds its hold if and only if the bracket is strictly positive.
The general expression allowing asymmetric vigs and pushes is developed in the SI Sec. S1. Two consequences follow
from (10).
Corollary 2(Public lean only increases book profit if matched with a shaded line.).If the book prices at the median,
thenFm(s) = ¯Fm(s) = 1
2 andθ(s) = 0, yielding:
Q(s) = 1
2
 
1 +δ(s)

,E[π(s)] = 1−ϕ
2 + 1 +ϕ
2 δ(s),
regardless of the public’s leanλ(s). Thus, when pricing accurately, the book exceeds its hold if and only ifδ(s)>0.
Corollary 3(Price shading only increases book profit if paired with a public lean.).If bet shares are independent of the
outcome,δ(s) = 0, then E[π(s)] = (1−ϕ)/2 + 2(1 +ϕ)θ(s)λ(s) , which exceeds the hold if and only ifθ(s) andλ(s)
are non-zero and have the same sign. If public betting is balanced, price shading does not increase book profit.
By making use of the identitybh(s) =F m(s)bh,L(s) + ¯Fm(s)bh,W (s), one can show that Cov(Bh(s),1{M <s}) =
Fm(s) ¯Fm(s)δ(s) , meaning that the third term in 9 is equal (up to a constant) to the covariance between the home bet
share and whether the home side loses:
Q(s) = 1
2 + 2θ(s)λ(s) + 2 Cov
 
Bh(s),1{M <s}

.(11)
Note that the second term of the right-hand side is a product of marginal expectations while the third term is a covariance.
In other words, the book profit’s excess factors into a product of marginals and a covariance term, which is standard
for a joint expectation of random variables. Although both terms may be viewed as “public bias”, the two terms have
very distinct interpretations:θ(s)λ(s) is a directional bias that is theoretically observable before the match takes place,
whileCov(Bh(s),1{M <s})is outcome-covariant and can only be resolved after.
It is also instructive is to consider the extreme case of a public that always backs the home side. Here the home bet
share is clearly independent of the outcome, andbh(s) =b h,L(s) =b h,W (s) = 1. Despite the fact thatδ(s) = 0, the
book can still profit above its hold ifFm(s)> 1
2. This is precisely the mechanism presented by Levitt [2004] and the
second term of 11. Because Levitt implicitly assumes independence between bet shares and outcomes,δ(s) = 0 and
the productθλis the only mechanism by which the book can profit above its hold in his account.
The profit driver as a misclassification probability
Note that the profit-bias identity (5) makes no assumptions about how the public chooses sides beyond the existence of
the conditional expectations in (2). All market- and behavior-specific structure enters throughQ(s), which depends
on the joint distribution of (Bh(s),M) . Here we employ a simple public-belief model and show that it leads to a
decision-theoretic interpretation ofQ(s).
4

APREPRINT- SEPTEMBER9, 2026
Consider the point spread setting whereM models the difference between home and away score,s is the sportsbook’s
posted spread, and assume that the public forms a noisy, biased beliefYabout the (latent) expected outcomeX:
Y=X+ε+V, M=X+U,(12)
whereε is the public’s systematic bias,V is belief noise, andU captures noise on the outcome that is assumed to be
independent ofV . We further assume that the public backs the home side wheneverY >s , such that the home team’s
bet share is captured by a representative agent:Bh(s) =1{Y >s} . In other words, the public acts on the aggregate
signalY and places its stake on one side –Bh(s)∈{0,1} . With this selection rule, the conditional losing-side shares
bh,L(s) andbv,L(s) of (2) become conditional misclassification probabilities, andQ(s) takes on a decision-theoretic
interpretation.
Proposition 4(Profit driver as a misclassification probability).Under the public-belief model with selection rule
Bh(s) =1{Y >s}, the profit driver of the profit–bias identity satisfies:
Q(s) = Pr
 
public backs the losing side

.
Q(s) is thus the misclassification probability of the binary predictor 1{Y >s} for the eventM >s. As a result, the
sportsbook’s expected profit is an affine, strictly increasing function of the public’s classification error in predicting the
sign ofM−s.
Consequently, the book profits to the extent that the public’s belief signal fails to classify the outcome. The proof of
Proposition 4, as well as a closed-form evaluation ofQ(s) in terms of the belief and outcome distributions, are given in
the SI (Sec. S4).
Conditions for the Existence of a “Goldilocks Zone”
We ask when a posted spreads is simultaneously attractive to the sportsbook and to a small bettor: that is, when the
book earns a profit in expectationandan individual bettor (whose wager is negligible relative to the public aggregate)
can find at least one side with positive expected value at the posted price. We assume fractional spreads (πpush(s) = 0)
and symmetric vigs (ϕh =ϕ v =ϕwithϕ∈(0,1)). For notational convenience, we define:
τ≡ ϕ
1 +ϕ ∈
 
0, 1
2

,(13)
such thatτand1−τ= 1
1+ϕ are symmetric about 1
2.
From (5), the sportsbook’s expected profit is positive if and only if:
Q(s)>τ.(14)
Note from (6) thatQ(s) is a convex combination of the two conditional losing-side shares, weighted by the outcome
CDF:
Q(s) =
 
1−F m(s)

bv,L(s) +F m(s)bh,L(s).(15)
BecauseFm(s)∈[0,1], it follows thatQ(s)is bounded between the two losing bet shares:
min
 
bh,L(s),bv,L(s)

≤Q(s)≤max
 
bh,L(s),bv,L(s)

. (16)
Thus, whether the book profits depends on where the thresholdτis situated relative tob h,L(s)andb v,L(s).
Proposition 5(Book-profit regimes).Fix a spread s and letbmin(s) = min(bh,L,bv,L) andbmax(s) = max(bh,L,bv,L).
The book-profit condition(14)obeys exactly one of three regimes:
(i)Always(b min(s)>τ):Q(s)>τfor every value ofF m(s).
(ii)Never(b max(s)≤τ):Q(s)≤τfor every value ofF m(s).
(iii) Threshold(bmin(s)≤τ <b max(s)): asFm(s) varies from 0 to 1,Q(s) increases monotonically frombv,L(s)
tobh,L(s), crossingτonly once at:
F∗(s) = τ−b v,L(s)
bh,L(s)−b v,L(s) ∈[0,1].
The book profits on whichever side of this crossing puts more of the weight on the larger of the two shares:
Q(s)>τ⇐⇒
(
Fm(s)>F ∗(s),ifb h,L(s)>b v,L(s),
Fm(s)<F ∗(s),ifb h,L(s)<b v,L(s).
5

APREPRINT- SEPTEMBER9, 2026
In particular,b min(s)>τissufficientandb max(s)>τisnecessaryfor the book to profit ats.
The proof of Proposition 5 is in the SI (Sec. S5). The key idea is that book profitability is governed by the values of the
conditional losing-side shares relative to the thresholdτ: the book always profits whenever the public’s losing-side
stake exceedsτ onbothoutcomes ( bmin >τ ), while never profiting when it fails to exceedτ oneither( bmax≤τ ). In
the remaining case, book profitability is determined by the value ofFm relative toF∗ at the posted spreads.
We define the “Goldilocks Zone” as the set of spreads at which the bookanda small bettor can profit:
G ≡

s:Q(s)>τ
	
∩ B,B ≡

s:a negligible bettor has a positive expected value wager ats
	
.(17)
The conditions under which a bettor may find a profitable wager have been previously derived [Dmochowski, 2023].
Briefly, a unit wager netsϕ on a win and−1 on a loss, such that a bet has positive expected profit only when its win
probability exceeds 1/(1 +ϕ) = 1−τ . The win probabilities of the home and away sides are given by ¯Fm(s) and
Fm(s), respectively, leading to:
E[home bet]>0⇐⇒F m(s)<τ,E[visitor bet]>0⇐⇒F m(s)>1−τ.(18)
These conditions amount tos lying in atailof the outcome distribution Fm. In other words, the bettor may profit only
when the outcome is extreme enough to overcome the vig:
B=

s:F m(s)<τ
	
∪

s:F m(s)>1−τ
	
.(19)
Existence of a Goldilocks Zone.Combining the book profitability condtions of Proposition 5 with (19) yields the
following (distribution-free) conditions on the existence of a non-empty Goldilocks Zone:
• Sufficient.If, for at least one s, the bet shares satisfy bmin(s)> τ andFm(s) lies in a tail (Fm(s)< τ or
Fm(s)>1−τ), thens∈Gand the Goldilocks Zone is non-empty.
• Necessary.Any s∈G must satisfybmax(s)>τ andFm(s) in a tail; wherebmax(s)≤τ , the book cannot
profit andGis empty regardless ofF m.
For the threshold regimebmin(s)≤τ <b max(s), non-emptiness ofG requires that the tail constraint onFm(s) and
the “crossover” constraint (Fm(s) vs.F∗(s)) hold at thesamespread. Importantly, the quantities Fm(s),bh,L(s), and
bv,L(s) all covary withs, such that existence is determined by the joint trajectorys7→
 
Fm(s),bh,L(s),bv,L(s)

, the
object that we estimate in the forthcoming empirical section.
Visualizing the profit driver and the Goldilocks Zone
To visualize the theoretical results, we modeled the outcome distributionFm(s) and the public’s home bet sharebh(s)
with toy Gaussian models (seeMethodsfor details). In the schematics of Fig. 1, the horizontal axis is acandidatepoint
spread that the sportsbook may post for a match whose median outcome is taken to be zero (without loss of generality);
moving the spread to the right (left) increases the handicap on the home (away) team. The vertical axis is the profit
driverQ(s) – the expected share of money on the eventual losing side – and the book profits whenQ(s) exceeds the
vig-defined thresholdτ. We examine how book profit responds to four types of public betting behaviors: acalibrated
public whose beliefs are aligned with the outcome distribution (panel a); afavorite-leaningpublic whose bias toward
the stronger team (the side the sportsbook favors) places a preponderance of money on the favorite (panel b); asquare
public that allocates a higher bet share to the eventual losing side (panel c); and asharppublic that allocates a higher
bet share to the eventual winning side (panel d). It is important to note that the first two behaviors are independent of
the realized outcome, whereas the last two convey a statistical dependence between betting and outcome.
A calibrated public confines the book’s profitable region (i.e., the region of the curve where Q(s) exceedsτ) to an
interior band around the median (|s|<ϵ ; Fig. 1a). Here the book profitsonly by pricing accurately: its profitability
requires that the posted spread be near the true median. The corresponding Goldilocks regions (green bands) are situated
on either side of the median, where the posted spread differs from the median by a minimum amount without exceeding
ϵ.
A favorite-leaning public – one that backs the favorite in excess of its fair probability – produces a qualitative change
in book profit (Fig. 1b): the book now profits at the tails of the candidate spread where the public’s bias is largest.
Note that here the profit curve opens upward (U-shaped). This arises without dependence between betting and realized
outcome: it is a structural phenomenon, rooted in the the public’s tendency to overvalue favorites. The Goldilocks
region widens correspondingly, extending across the tails.
Introducing a dependence between betting and outcome produces vertical shifts of the profit curve; we model it with a
constantδ between the conditional bet shares (solid line, home loses; dashed line, home wins). Asquarepublic, whose
6

APREPRINT- SEPTEMBER9, 2026
posted spread s
0
0.5
1
Q (book profit driver)
Fm
1 Fm
book profits
above 
home underdog home favorite
a Calibrated
bh, L = bh = P(home wins)
bv, L = 1 bh
Q = 2Fm(1 Fm)
posted spread s
0
0.5
1
Q (book profit driver)
Q > 1
2  with = 0
(structural profit)
home underdog home favorite
b Favorite-leaning
P(home wins) (fair)
bh (backs favorites)
Q calibrated
Q favorite-leaning
posted spread s
0
0.5
1
Q (book profit driver)
 Goldilocks Zone
home underdog home favorite
c Square ( > 0)
bh, L (home loses)
bh, W (home wins)
Qindep
Q
posted spread s
0
0.5
1
Q (book profit driver)
home underdog home favorite
d Sharp ( < 0)
bh, L (home loses)
bh, W (home wins)
Qindep
Q
Figure 1:The sportsbook profit driver Q(s) across four public behaviours. In every panelQ(s) =F m(s)bh,L(s) +
¯Fm(s)bv,L(s) is the Fm-weighted average of the home losing-side share bh,L =E[B h|M < s] and the visitor
losing-side sharebv,L =E[B v|M >s] ; the dotted line marks the thresholdτ, above which the book profits.(a)A
calibratedpublic bets each side at its actual win probability. The bracketed connector showsQ dividing the gap between
the two shares at a ratio of Fm : (1−F m). The inverted-U curve is upper bounded by 1
2 and falls below the profit
threshold at the tails of the posted spread.(b)Afavorite-leaningpublic backs favorites in excess of their fair cover
probability. Even with the betting fully independent of outcome (δ= 0 ),Q now opens up and is markedly increased at
the tails of the candidate spread.(c)Asquarebetting public systematically allocates a larger bet share on the eventual
losing side (δ=b h,L−bh,W >0 ), increasing book profit above a purely favorite-leaning public.(d)Asharpbetting
public allocates a greater bet share on the eventual winning outcome ( δ <0 ), driving the book profit towards the
thresholdτ. In all panels, theGoldilocksregion (green) marks the set of candidate spreads where both an individual
bettor and the book profit. For a calibrated public (a), it is limited to two interior bands; a favorite-leaning public (b)
yieldsQ aboveτ across the distribution tails and thus widens the Goldilocks Zone. Square dependence (c) increases the
magnitude of the book’s profit without altering the extent of the Goldilocks Zone; with a sharp betting public (d), the
zone is relegated to more extreme spreads. All curves are schematics generated with Gaussian models for both outcome
and public belief.
money skews toward the eventual loser (Fig. 1c), quantitatively increases the magnitude of the book’s profit without
greatly changing the extent of the Goldilocks Zone. Conversely, asharppublic reduces book profit across the range of
spreads, and in the schematic shown drives the book to a loss over a substantial interior region (Fig. 1d); the Goldilocks
region is correspondingly limited to the extreme tails of the candidate spread.
Taken together, these panels relate book profitability to three mechanisms: (i) accurate forecasting of the outcome
distribution; (ii) structural biases in public betting, such as over-valuing favorites; and (iii) any conditional dependencies
between betting and outcome. The empirical section below attempts to shed light onto which of these mechanisms may
manifest in real betting markets.
7

APREPRINT- SEPTEMBER9, 2026
Empirical results
To investigate the relationship between sportsbook profit, public betting, and game outcomes, we collected Major
League Baseball (MLB) market prices and bet shares at a major North American sportsbook over an eleven-week
duration. The specific market analyzed here, termed the “run line,” fixes the favorite’s handicap at 1.5 runs and instead
expresses the teams’ relative strength through the payoutsϕh andϕv. Note that this is unlike a standard point spread
market where payouts on the two sides are approximately equal. The bettor’s task is thus to predict whether the
home team will win by more than (or lose by less than) 1.5 runs at a price reflecting the perceived difference in team
strengths. Prior tests of Levitt’s model have employed empirical bet shares (sometimes termed betting “splits”) [Paul
and Weinbach, 2007, 2008, 2012, Humphreys et al., 2013]. Here we add a temporal dimension, observing each line
and its associated bet shares from posting to game onset, as in previous high-frequency line-movement studies [Simon,
2024, Gandar et al., 1998].
We asked the following questions: (i) Do bet shares covary with realized outcomes? (ii) Does the bet share-outcome
covariance evolve across time? (iii) Do bet shares drive prices, or do prices drive bet shares, or both? (iv) What are the
contributions of price shading, public lean, and outcome covariance to the book’s profit?
Bet share-outcome dependence in MLB run lines: a Simpson’s paradoxAcross n= 1,139 games, the betting
public displayed a striking preference for the match favorite: the home bet share varies sigmoidally with the sportsbook’s
implied win probability (Fig. 2a), increasing from below 25% when the away team is strongly favored to above80%
when the home team is. In contrast, the sportsbook’s implied home win probabilities span a compressed central range
(0.39–0.67).
We computed the home team’s bet share separately for games that the home team won versus lost against the spread.
This revealed an apparent discrepancy: in games where the home side lost the proposition, the home bet share was
5.8 percentage points higher (56.4% versus 50.6%; game-level bootstrapp= 0.0004 ;nL = 584,nW = 555). This
finding may be interpreted as evidence for a square betting public. However, stratifying the analysis by the identity of
the favorite (home versus away favorite) removed the effect: the home bet share showed no significant dependence on
the realized outcome in either stratum, and both point estimates were small (home favorites,bδ=−1.5 pp,p= 0.51 ,
n= 608; away favorites, bδ= +0.6pp,p= 0.79,n= 531).
The apparent dependence is thus a Simpson’s paradox: a correlation in pooled data that is removed upon conditioning
on a confounding variable. Here the confounder is the identity of the favorite: when the sportsbook designates the home
team as the favorite, both the home bet sharebh andthe probability of the home team losing against the spread Fm(s)
are increased. The latter is due to the fraction of home team losses being slightly larger than that implied by book prices.
We elaborate on the implications of this structural form of book profit in theDiscussion.
Dynamics of book profit and public beliefPublic betting and sportsbook price setting operate as a closed loop,
producing fluctuations in both quantities prior to the start of the game. Focusing on the MLB run line market, we
collected hourly samples of the point spreads, payouts (ϕh,ϕv), and bet shares (bh,bv) in the 24 hours leading up to
game onset. Within each stratum (home favorite versus home underdog), we calculated the book’s profit driverQ(s) as
well as the public’s outcome dependencyδ(s)in non-overlapping 6 hour windows.
The book’s profit driver evolves distinctly across the two strata. For matches with a home underdog,bQ increases from
46.9%±2.6 at posting to 52.0%±2.1 at game onset – the initial “sharp” betting is not sustained. In matches with a
home favorite, the losing side share is reliably above 50% throughout (54.4%±2.4to53.8%±2.0, mean±SEM).
We asked whether the outcome-conditioned biasδ exhibits significant movement across time, employing a linear mixed
model with time and outcome as factors and the home bet share as the dependent variable. A significant interaction
between time and outcome indicates that public belief carries information about the eventual outcome that is not
constant over the pre-game window – a dynamic departure from Levitt’s implicit independence. For home underdogs,
we found a significant decreasing slope, indicating that the home bet share decreases for games in which the home
team subsequently wins against the spread (bbh,W falling from≈44% a day out to≈36% at first pitch; game-clustered
bootstrap p= 0.038 , cluster-robust p= 0.038 , n= 256 games). This finding is suggestive of a square betting
pattern that emerges closer to the start of the game. The corresponding test for home favorites was non-significant
(game-clustered bootstrap p= 0.85 , n= 288 games). We note the two strata’s slopes do not significantly differ
(three-way outcome× time× stratum interaction, game-clustered bootstrapp= 0.12 ) – the dynamic departure from
independence is specific to home underdogs.
Feedback between book pricing and public bettingThe public-belief model treats the posted price as an input to
the public’s wager rather than a response to it – this ordering can be tested directly. We estimated Jordà local projections
8

APREPRINT- SEPTEMBER9, 2026
0.3 0.4 0.5 0.6 0.7
Devigged home win probability
20
30
40
50
60
70
80
90Home run-line handle share (%)
a
Pooled
(all games)
 = +5.8
p = 0.00
b
Home +1.5
(underdog)
Home 1.5
(favorite)
 = +0.6  (n.s.)
 = -1.5  (n.s.)
c
Home lost the bet
Home won the bet
Figure 2:A Simpson’s paradox explains the apparent bet share-outcome covariance in the MLB run line market.
We collected market prices and bet shares from the MLB run line market acrossN= 1,139 games.(a)The public shows
a striking preference for favorites: the home bet share varies sigmoidally with the price-implied home win probability;
light grey markers denote individual games, while the curve shows the binned mean with 95% confidence band.
(b)Computed over all games, the home bet share appears to covary with the realized outcome: bδ= bbh,L−bbh,W = 5.8
points (p= 0.0004 ): more money is wagered on the home side in games that the home team eventually lost (bbh,L, red)
than won (bbh,W , blue).(c)However, stratifying the analysis by the identity of the favorite eliminates the effect: bδ is
−1.5 for home favorites and +0.6 for home underdogs (both n.s.). Because a home favorite attracts a majority of the
bet shareandwins the proposition less often than the price-implied win probability, the pooled bet share-outcome
covariance is spurious.
[Jordà, 2005] of each series on a one-step innovation in the other ((22); seeMethods). A local projection regresses the
level of one variable at horizonh on an innovation in the other, yielding the impulse response horizon by horizon rather
than extrapolating it from a fitted dynamic model. A game fixed effect absorbs the latent state that sets both the opening
price and the public’s prior, and a pre-move momentum control blocks the reverse channel, so that under sequential
ignorability the horizon-hcoefficient is the response to the move itself.
On the present dataset, the two directions were markedly asymmetric. A move in the book’s line was followed by a
small “fade” of the public: a one-percentage-point increase in the devigged home win probability lowered the home bet
share by roughly0.2points, significant at horizons of one to five hours and peaking ath= 4( bβ=−0.20,t=−3.11,
p= 0.002 ,n= 1090 games; Fig. 4a). As expected, when wagering on the home side becomes more expensive, the
public’s tendency to do so lowers. The converse channel, however, was absent: the line’s response to a one-point move
in the home share was flat at zero and insignificant at every horizon (|bβ|≤0.010 points, allp>0.27 ,n= 1103 games;
Fig. 4b). The price thus leads the money rather than the reverse, matching the ordering assumed by the belief model.
The book’s profit margin is indistinguishable from its hold.Propositions 1 and S1 dictate that a book profits
beyond its hold if public betting favors a side that is overpriced, or if bet shares covary negatively with the realized
outcome. We asked whether either of these two conditions may be present in our dataset. The book earned a mean
profit 5.20% of handle per game (95% CI [0.88,9.35] ,N= 1,139 ; Fig. 5a), compared to the 4.39% hold that even
a perfectly balanced book would collect – on this sample, the book’s profit is thus indistinguishable from the hold.
Moreover, as is evident in the figure, the per-game profit exhibits very high dispersion (s.d.73.8%of handle).
Stratifying games by the identity of the favorite, the bet share on the favored side is+29.6 pp higher when the home
side is the favorite and−24.5 pp higher when the visitor is favored (Fig. 5b). Public betting on the favorite thus exceeds
the book’s implied price by 24–30 percentage points, reflecting a bias that has been previously well documented [Levitt,
2004, Paul and Weinbach, 2007, Franck et al., 2011]. Note from Corollary 3 that a public lean requires a corresponding
9

APREPRINT- SEPTEMBER9, 2026
05101520
Hours to game start
42.5
45.0
47.5
50.0
52.5
55.0
57.5
60.0Losing side bet share  Q (%)
a
Home 1.5 (favorite)
Home +1.5 (underdog)
05101520
Hours to game start
30
40
50
60
70
80Home bet share bh (%)
b
Home favorites ( 1.5)
Home lost the bet
Home won the bet
05101520
Hours to game start
c
Home underdogs (+1.5)
Figure 3:Temporal evolution of public bias and book profit during the pre-game window.We collected hourly
samples of public bet shares and prices for the MLB run line market. To gain insight into the temporal dynamics of
book profit and public belief, we then estimated the fraction of share on the losing-side bQ in non-overlapping six hour
windows terminating at game onset. The analysis was stratified into home-favorite (N= 288 ) and home-underdog
(N= 256 ) games.(a)The share of money on the eventual losing side bQ(t) by stratum: for home underdogs (green),
the losing share increases from 46.9%±2.6 to 52.0%±2.1 , while for home favorites (orange) it remains stable and
above 50% (54.4%±2.4 to 53.8%±2.0 ).(b,c)The home bet share in games that the home side eventuallylost( bbh,L,
red) versuswon( bbh,W , blue) the closing bet, for home favorites (b) and home underdogs (c); the gap between the
two curves is the outcome-conditioned biasbδ(t). For games with a home underdog, the home bet share separates by
outcome early (t=−24 tot=−18 h:bδ=−8.9 points; more home money on the eventual winner) but converges by
the start of the game. The observed change inbδ is significant (linear mixed model with time and outcome as factors,
time× outcome interaction: bootstrapp= 0.038 ,n= 256 ), suggesting an increase in square betting leading up to the
start of the game. Games with a home favorite show little separation at any time (p= 0.85 ); the difference between the
two strata’s slopes is itself not significant (p= 0.12).
book shading to yield excess profit. Thus, the empirical finding that the book does not profit above its hold despite the
strong favorite-bias suggests that the book’s prices are calibrated.
To test this, we estimated the book’s mispricing ˆθ=p ∗− ¯Fm across the price range and contrasted it with the case
of a perfectly calibrated book. We found no departure from calibration: the average mispricing is +0.48 pp (95% CI
[−2.42,+3.38] ), and the largest local departure, 5.8 pp, is within the 9.4 pp that a calibrated book would produce
by chance at this sample size (p= 0.54 ). The posted prices are indeed consistent with being calibrated (but see the
Discussion for limitations).
For each excess-profit-generating mechanism (shading× lean, outcome covariance), we asked what the largest level of
that mechanism is that remains consistent with the observed data. For shading, we assumed that the book shades in the
maximally profitable direction – the side that the public backs is priced as more likely to cover than it truly is – and
calculated the largest shading whose implied profit margin still falls inside the book profit confidence interval. Because
the public’s lean is large, (counterfactual) shading would be highly profitable: 1.35% of handle per percentage point.
Consequently, the upper bound on price shading is tight: at most 3.7 pp (Fig. 5c), meaning that the devigged book price
departs from the true cover probability by no more than0.037in the direction of the public lean.
We repeated the analysis for outcome-covariance, calculating the largestδ compatible with the observed book profit.
The bound is again modest: 5.2 pp (Fig. 5d), implying that the public’s home bet share differs by at most5.2 percentage
points between games won versus lost by the home side.
10

APREPRINT- SEPTEMBER9, 2026
0 2 4 6 8 10 12
Horizon h (hours after move)
0.2
0.0
0.2
Share response per 1pp line move (pts)
Line  Share
p < 0.05
0 2 4 6 8 10 12
Horizon h (hours after move)
0.02
0.00
0.02
Line response per 1pp share move (pts)
Share  Line
Figure 4:Book pricing drives public betting, but not the reverse.To investigate causal coupling between sportsbook
pricing and public betting, we computed Jordà local projections of the book price and bet share time series across on
an hourly grid (n= 1103 games; game fixed effect, pre-move momentum control). The response of each series at
horizonh (number hours after the change in the other signal) is shown with 95% CI, and the shaded strip indicates
the contemporaneoush= 0 .(a)Line → share:a 1-percentage-point increase in the devigged home win probability
is followed by a small but significant reduction of the home bet share ( bβ≈−0.20 points,t=−3.11 ,p= 0.002 ,
n= 1090 at theh= 4 peak; significant at h= 1 –5; dark-ringed markers).(b)Share → line:in contrast, the line
does not significantly respond to a 1-point change in home bet share (|bβ|≤0.010 points,p>0.27 at every horizon,
n= 1103 ). Thus, at least in the present data, the book does not reprice to changes in observed bet shares; the price
drives the public’s belief, not the reverse.
Discussion
We argue that Levitt’s influential model of bookmaker profit [Levitt, 2004] assumes that public betting is independent
of the realized outcome, and then generalize the model of sportsbook profit to allow betting-outcome dependence.
Importantly, this leads to an expression for bookmaker profit that is affine in the public’s bet share on the eventual
losing side: the profit-bias identity. That central object of the identity may be understood in the framework of decision
theory, such that bookmaker profit is synonymous with the public’s misclassification error of the outcome relative to
the book’s line. This places the book’s accounting and the bettor’s estimation problem on a common footing, since
the same quantiles of the outcome distribution that govern one govern the other [Dmochowski, 2023]. There is thus a
direct link between how much the book profits and how biased the public’s belief of the outcome is – at the posted
spread. A profit-maximizing book seeks to identify the price which maximizes the share of betting on the losing side
but weighted by the outcomes of the corresponding loss. This is inherently a three-dimensional optimization problem
– for each candidate point spread, the profit-optimizing book must forecast (i) the share of bets on the losing side if
home wins, (ii) the share of bets on the losing side if visitor wins, and (iii) the probability of the home side covering.
Critically, (i) and (ii) donotgenerally sum to one: their sum is 1 +δ(s) , and equals one precisely when the public’s
money is statistically independent of the outcome. That independence is the scenario treated by Levitt, whose profit
expression follows as a special case of the profit-bias identity. Generalizing the model does not, however, overturn his
conclusion: that books shade prices to exploit predictable public bias remains consistent with the profit-maximizing
view of fixed-odds pricing [Kuypers, 2000] and with evidence that books do not move lines to equalize the money on
the two sides [Paul and Weinbach, 2007]. What the present work adds is that the proximate driver of book profit is the
public’s misclassification error of the outcome relative to the posted line.
A surprising finding is that the book can profit above its hold even in the absence of statistical dependence between
outcomes and betting. The bookmaker profit decomposes into three "channels": (i) its hold, (ii) a structural profit term
that is positive when the public leans towards the same side that the book’s prices are shaded, and (iii) the covariance
between betting and outcomes. Perhaps counterintuitively, we show that public lean and book shading may align even
if the public has no information pertaining to the realized outcome. As long as the side with the higher bet share has a
lower probability of winning than that implied by its price, the book earns a structural profit in addition to the hold.
The lean that drives this channel is itself well documented, and is usually attributed to the loyalties and sentiment
11

APREPRINT- SEPTEMBER9, 2026
150
 100
 50
 0 50 100
Book profit per game (% of handle)
0
10
20
30
40
50
60
70Number of games
hold 4.39%
mean 5.20%
[0.88, 9.35]
sd = 73.8%
n = 1139
a
80
 60
 40
 20
 0 20 40 60 80
Public lean  = bh p*  (pp)
0
20
40
60
80
100
120Number of games
+30-25
b
home favorite, 1.5
away favorite, +1.5
0 1 2 3 4 5 6 7
Shading  | |  (pp)
2
0
2
4
6
8
10
12
14Book profit (% of handle)
3.7 pp
upper 95% CI
hold 4.39%
c
slope 1.35%/pp
bootstrap
mean profit
0 1 2 3 4 5 6 7
Outcome covariance    (pp)
2
0
2
4
6
8
10
12
14Book profit (% of handle)
5.2 pp
d
slope 0.96%/pp
bootstrap
mean profit
Figure 5:The book’s profit margin is indistinguishable from its hold, despite a large public lean toward favorites.
(a)Reconstructed book margin per game, shown as a percentage of that game’s handle (N= 1,139 ). The mean profit
margin of 5.20% (95% CI [0.88,9.35] , orange) is statistically indistinguishable from the 4.39% margin that a perfectly
balanced book would collect from the hold alone (green), though individual games are widely dispersed (s.d. 73.8%).
(b)The public lean λ=b h−p∗, split by the identity of the favored side. Betting is highly skewed to the favorite:
+29.6 pp where the home side is the favorite,−24.5 pp where the visitor is favored.(c,d)Upper bounds on the two
mechanisms that the book may exploit to profit beyond the hold. The grey density is the bootstrap distribution of the
mean profit margin, with its 95% CI interval marked; the sloped line denotes the excess profit margin that the book
earns as a function of the level of the corresponding mechanism (either price shading or outcome-covariance). The
largest values of shading and outcome covariance that are compatible with the empirical sample are thus marked by the
lines’ crossing of the upper CI:3.7pp of shading aligned with the lean, and5.2pp of outcome covariance.
of a recreational public rather than to information [Avery and Chevalier, 1999, Franck et al., 2011, Stan ˇek, 2017].
The mechanism is complementary to the classical account of bookmaker margins, in which both the margin and the
favorite–longshot bias arise from the threat of privately informed insiders [Shin, 1991, 1992]; here no informed trader is
required, only a marginal taste for favorites meeting a handicap that makes that taste costly. That bias takes the opposite
sign in parimutuel racetrack betting, where longshots are overbet [Thaler and Ziemba, 1988, Snowberg and Wolfers,
2010, Ottaviani and Sørensen, 2008]; the favorite preference we observe is its fixed-odds, team-sport counterpart, of a
piece with earlier study of the baseball betting market [Woodland and Woodland, 1994]. Note that the conditions for this
second channel of book profit are known before the actual outcome is observed: the collected bet shares and likelihood
of each side winning the bet. In order for the book to profit from the third channel, it must elicit a preponderance of
money on the side that loses the match (presumably by identifying a price at which this occurs systematically). This
third channel cannot be resolved until after the game has concluded.
Another surprising aspect of our work pertains to our empirical investigation of the MLB run-line market at a major
North American sportsbook, where we discovered that a Simpson’s paradox can spuriously indicate betting-outcome
dependence. When pooling all matches, we observed a significant majority of the public’s money on the eventual losing
side (Fig. 2b). However, this effect is completely eliminated once stratifying the data by the identity of the favorite: in
12

APREPRINT- SEPTEMBER9, 2026
games with a home underdog, there was no significant difference between the bet share on the losing versus winning
side (Fig. 2c). The same finding was observed in matches where the home side was favored (Fig. 2c). Yet when pooling
the two strata, a seeming “square” public betting pattern emerges. The resolution to this Simpson’s paradox is that
the identity of the favorite drives both public betting tendencies (because the public prefers favorites)andthe eventual
outcome (because the favorites win less often than implied by the book’s prices). The finding of more money on the
eventual losing side when aggregating all games is thus a composition artifact. Importantly, this result is a caution
to tests of market efficiency and betting-outcome dependence, which are often performed on pooled samples [Paul
and Weinbach, 2002, 2011, Humphreys et al., 2013]. The excess-share term 2Fm ¯Fmδ of (S15) makes the separation
explicit: what a pooled test reads as behavioral dependence is the sum of a within-stratum term and a composition term,
and only the former carries the interpretation usually assigned to it. Our findings point to the importance of conditioning
such analyses on match attributes.
Our empirical analysis reconstructed book profit over 1,139 games and found that the resulting profit margin does not
vary from that of the book’s guaranteed hold (Fig. 5a). This is despite very strong evidence for the public’s bias towards
the match favorite (Fig. 5b). From the second channel of book profit (10), a margin no larger than the hold despite
so pronounced a lean implies that the book’s price shading must be small: the data bound it to at most 3.7 pp in the
direction of the lean, and a direct check of the posted prices shows no detectable departure from calibration. We read
this as a null on shading rather than as a demonstration of accurate pricing. Expected profit depends on the mispricing
only through its product with the lean, so a margin test carries power only against mispricing that aligns with where the
money sits: in simulation on our own design, 5 pp of aligned mispricing is detected 88% of the time, against 6% when
the same mispricing is oriented independently of the lean. The direct check is limited in a complementary way, since at
this sample size a perfectly calibrated book would itself generate local departures of up to 9.4 pp by chance. What
we bound is therefore Levitt’s mechanism specifically; a book could misprice substantially in ways unrelated to the
public’s lean and leave no trace in its margin. Because the book can only profit from a public lean towards favorites if
the prices are also shaded towards favorites (Cor. 3), the absence of detectable shading nullifies the potential additional
profit. Interestingly, this scenario finds the book taking on additional risk – the variability in profit margin is enormously
higher than that of the hold itself – without “reward”. The expected profit is no larger than the risk-free hold, but comes
with a much wider confidence interval.
One limitation of the present study is that the treatment is limited to two-outcome markets, whereas several prominent
markets are three-way (e.g. European football home-draw-away). As such, extending our framework to multi-way
markets such that the profit-bias relationship can be quantified represents an avenue for future research. Our empirical
results are best understood as demonstrations of the proposed theoretical framework rather than inferential claims about
the economics of modern-day sportsbooks. We analyzed data from one sport and one market (albeit both major) and
the empirical findings serve to demonstrate that key objects such asQ(s),δ may be estimated from data and that they
convey insight into that specific market. The number and size of sports betting markets is vast, and we do not aim
to characterize how those objects vary across the spectrum of sports and bet types. Relatedly, public bet-share data
are scarce. Here we collected hourly data from a single book over several months, but quantities such as the extent
of the Goldilocks Zone require the joint distribution of bet share and outcome over many games and remain hard to
estimate. Prediction markets – whose order books are an analogue of the bet share – may generate richer data [Wolfers
and Zitzewitz, 2004, Snowberg et al., 2013], but it is unclear how neatly this may map to sportsbook markets. A further
caveat is that the book’s margin is reconstructed rather than observed: the splits record shares rather than dollars, so
each game enters per unit of its own handle, and the aggregate depends on a volume distribution we do not see. Finally,
with the exception of the local-projection analysis (Fig. 4), our treatment is non-causal. Whether pre-game movement
of the kind we observe reflects the arrival of informed money is the subject of an extensive line-movement literature
[Gandar et al., 1998, Krieger and Fodor, 2013, Simon, 2024, Croxson and Reade, 2014].On the other hand, betting
markets likely exhibit a deep causal structure linking information arrival, book prices, and public betting tendencies; as
such, a causal account of how book prices and public beliefs evolve is an important direction for future work.
The profit-bias identity naturally organizes betting markets by the properties of the conditional losing shares. In
particular, we define the Goldilocks Zone as the set of prices at which the sportsbookanda negligible bettor are
simultaneously positive in expectation. This requires that the public’s losing-side share exceeds the book’s break-even
threshold while the outcome distribution is sufficiently removed from the median. A Goldilocks Zone represents an
inefficiency that still allows the book to profit, and thus connects the present work to the long-standing debate over
betting market efficiency [Sauer, 1998, Gray and Gray, 1997, Vandenbruaene et al., 2022]. Whether such a zone can be
exploited in practice depends on the same constraints that limit arbitrage in financial markets [Shleifer and Vishny,
1997, Moskowitz, 2021]: betting limits, transaction costs, and the difficulty of consistently identifying the profitable
side.
The view that sportsbooks profit by exploiting a predictably biased public has organized the literature for two decades.
Legalized online betting is now expanding that market and shifting the composition of the betting population. It remains
13

APREPRINT- SEPTEMBER9, 2026
to be seen whether the prevalent view outlasts this change; the profit-bias identity provides the means to answer that
question empirically.
Methods
Construction of schematic figure (Fig. 1)
Figure 1 is an illustrative schematic; as such, its parameters are chosen for clarity rather real-world plausibility.
Outcomes follow a Gaussian model where the median outcome (home score - away score) is assumed to be 0 (center
of the horizontal axis) and the horizontal axis represents the sportsbook’s posted point spread, which may be viewed
as their estimate of the outcome. We definez(s) = 2Φ(s/2)−1, z∈(−1,1) , where Φ is the standard normal CDF,
to capture the strength of the implied favorite. The outcome distribution is then modeled asFm(s) = 1
2 + 0.24z(s) ,
such that favorites (larger|s|) win the proposition less than half the time. The sportsbook’s break-even threshold is set
to a realistic vig,ϕ= 100/120 (−120 American odds), yieldingτ=ϕ/(1 +ϕ)≈0.45 . The four public behaviours
differ only in the home bet sharebh(s) and the outcome-covarianceδ(s):(a)calibrated, bh = ¯Fm (each side backed
at its actual win probability), so that Q= 2F m(1−F m);(b)favorite-leaning, bh = 1
2 + 0.32z (favorites backed
beyond their actual win probability) with δ= 0 , such thatQ= 1
2 + 2(Fm− 1
2)(bh− 1
2); and(c)square-(d)sharp,
which add a constant δ=±0.28 such that Q= 1
2 + 2(Fm− 1
2)(bh− 1
2) + 2Fm ¯Fmδ. We clip δ to the range
min
 
bh/Fm,(1−b h)/ ¯Fm

to ensure that the conditional sharesbh,L =b h + ¯Fmδandb h,W =b h−Fmδremain in
[0,1] . The shaded Goldilocks region shows the set of candidate spreads where the book profits ( Q > τ) while still
allowing a negligible bettor to find a profitable wager (Fm <τorF m >1−τ).
Data collection
We obtain public betting data from the DraftKings Network betting-splits website [DraftKings Network, 2026], which
reports, for each upcoming event and market, the percentage of handle and tickets wagered on each side. The splits are
collected each hour, yielding a series of samples from posting to game start: we record the event, market, selection,
posted odds, and the handle and ticket shares. We focus on the two-sided market to which (5) most directly applies: the
baseballrun line. The run line is a variant of conventional point spread but with an important modification: whereas a
standard point spread varies the handicap and holds the payouts (ϕh,ϕv) roughly symmetric (e.g.ϕh =ϕ v = 0.91),
the run line fixes the handicap at ±1.5 and expresses the teams’ relative strength through (generally asymmetric)
payouts. As an example, a home favorite with a −1.5 handicap may payϕh = 1.5 with the corresponding visiting
underdog (+1.5) payingϕv = 0.56. The book thus moves the price (i.e., not the magnitude of the handicap) and it is
the combination of the payouts and identity of the handicapped side that conveys the favored side.
We obtain final scores from the public ESPN scoreboard API [ESPN, 2026]. For each event, we determine whether it
won, lost, or pushed against the linein effect at that snapshot. A run-line wager wins when the sum of the selected team’s
score and its±1.5 handicap exceeds that of its opponent’s. The dataset analysed here spans games from 2026-05-31
through 2026-08-28
Empirical testing of the bet share-outcome dependence (Fig. 2)
To empirically probe the statistical dependence between public betting and realized outcomes, we analyzed MLB
run-line bet shares measured at game onset. Specifically, we calculated the sample estimatebδ= bbh,L andbbh,W – the
difference in home bet share between matches where the home team won versus lost against the spread. The quantitybδ
was first computed over all games, and then on two individual strata – the set of games with a home favorite, and those
with a home underdog. The rationale for stratifying the data (i.e., conditioning on the identity of the favorite) was to
control for hidden variables that produce spurious dependencies between bet share and realized outcome.
Figure 2(a) plots the home bet share against the home win probability, which we computed from the sportsbook’s
“moneyline” payouts (the moneyline is a bet on which team wins the contest, regardless of margin). The reason for
this choice, which affects only the display item, was to allow for sorting the matches along the “strength of favorite”
dimension. For home and visiting moneyline payouts ofϕh andϕv, respectively, we remove the book’s vig (“devig”)
by normalizing the corresponding implied win probabilities1/(1 +ϕ h)and1/(1 +ϕ v)to sum to one:
dv(ϕh,ϕv) = 1/(1 +ϕh)
1/(1 +ϕh) + 1/(1 +ϕv).(20)
We use the resulting devigged home-win probability dv(ϕh,ϕv) to order games by favorite strength. In the figure,
games are grouped into deciles, markers are decile means, and the band denotes bootstrapped95% CI. Panels (b) and (c)
14

APREPRINT- SEPTEMBER9, 2026
reportbbh,L (home lost the bet) andbbh,W (home won), pooled and within strata respectively, along withbδ= bbh,L−bbh,W
and its two-sided bootstrappedp-value.
Dynamics of book profit and bet share-outcome dependence (Fig. 3)
To study the temporal dynamics of book profit and associated bet share-outcome dependence, we measured the losing-
side share bQ and the home bet share Bg,t across four, non-overlapping 6-hour windows terminating at game onset.
Only games with at least one sample in each window were included. Within each game, we averaged all samples from
the same window. We then fit, separately for home favorites and home underdogs, the following mixed model:
Bg,t =β 0 +βhhg,t +βWWg +βhW (hg,t×Wg) +ug +εg,t, u g∼N(0,σ 2
u),(21)
whereBg,t is the observed home bet share at sample t of gameg,hg,t is the number of hours before onset of game
g,Wg∈{0,1} is a binary indicator of whether the home side won the closing bet, and ug is a per-game random
intercept. Sinceδ(h) =b h,L(h)−b h,W (h) =−β W−βhWh, statistical significance of the closing share is assessed
with the regression coefficientβW (ath= 0 ). Themovementof the dependence is assessed by the outcome ×time
interactionβhW . The reported p-values were obtained with a game-level cluster bootstrap (resampling whole games
with replacement and refitting the model). Figure 3 displays, for each stratum, the losing-side share bQ(h) and the
conditional bet sharesbbh,L(h) andbbh,W (h). The shares are first averaged within each game (across samples in a 6-hour
bin) and then across games. Shading denotes across-game SEM.
Line–share feedback (Fig. 4)
We investigate the direction of the line–share feedback: whether the book’s price drives the public’s share, the reverse,
or both. Since the run-line handicap is fixed to ±1.5, line movement is reflected in the payouts. We represent the
momentary line byℓg,t = dv(ϕh,g,t,ϕv,g,t), obtained by applying the devig transform (20) to therun-linepayouts at
samplet. In other words, we operationalize “line” to the devigged probability that the home side covers±1.5. We then
fit Jordà local projections in both directions, for horizonsh= 0,...,12hours:
Bg,t+h−Bg,t−1 =β ℓ→B
h ∆ℓg,t +γh ∆Bg,t−1 +ag +εg,t,(22)
ℓg,t+h−ℓg,t−1 =β B→ℓ
h ∆Bg,t +γ′
h ∆ℓg,t−1 +a′
g +ε′
g,t,
where ∆ℓg,t =ℓ g,t−ℓg,t−1 and ∆Bg,t =B g,t−Bg,t−1 are the one-step line and share deviations, the outcome is
measured from the pre-move levelt−1 , the game fixed effectag absorbs the latent state, and the lagged one-step move
of the responding series (i.e., ∆Bg,t−1 and ∆ℓg,t−1, which we term thepre-move momentum) prevents the book from
“chasing” the money already wagered. Standard errors are clustered by game. Under sequential ignorability (i.e., the
current move is as-good-as-random given the game state and the money so far),βh is the impulse response of one series
to a move in the other. We denoise the integer-rounded bet shares with a3-hour moving average.
The book’s profit margin is indistinguishable from its hold. (Fig. 5).For each game (indexed here by i), we
reconstruct the book’s profit margin per unit of that game’s handle from three observables: the closing home bet share
bh,i, the home and away payoutsϕh,i,ϕv,i, and the realized outcomeCi∈{0,1} representing whether the home side
covered:
πi =C i

(1−b h,i)−ϕ h,ibh,i

+ (1−C i)

bh,i−ϕv,i(1−b h,i)

.(23)
Hereπi is a profit margin per unit of betting volume, which we have assumed to be equivalent for all games in the
dataset. Denoting the raw implied win probability witha= 1/(1 +ϕ) , the correspondingdeviggedwin probability is
calculated asp∗
i =a h,i/(ah,i +av,i). We then tabulateDi = 2+ϕh,i +ϕv,i, the per-game holdhi = (1−ϕh,iϕv,i)/Di,
and the public lean λi =b h,i−p∗
i . Evaluating Prop. S1 at the realized outcome (rather than the cover probability)
yields the following expression for per-game profit:
πi =h i +Diλi (p∗
i−Ci).(24)
Confidence intervals for the mean across-game profit margin¯π= 1
N
P
iπi are percentile intervals from a nonparametric
bootstrap over games (4,000resamples).
To upper bound the level of price shading or outcome-covariance that is consistent with the observed data, we calculated
the largest levels that yield profit margins within the observed confidence intervals. For price shading that is maximally
aligned with the public lean,θ=csgn(λ) , wherec>0 is the magnitude of price shading in probability units. Assuming
δ= 0 , the expected profit margin follows as h+cE[D|λ|] . For a constant outcome covariance δ withθ= 0 and
¯Fm =p∗, the profit margin ish+δE[Dp ∗(1−p ∗)]. In both cases, the profit margins are linear in the level and have a
15

APREPRINT- SEPTEMBER9, 2026
slope fixed by the observed lean and price distribution; the largest compatible value is thus given by where line crosses
the upper limit of the bootstrap interval.
To assess overall calibration of book prices, we pool games and calculate the mean deviation between devigged
price and realized cover rate, employing a binomial standard error. To assess calibration across the price range,
we employed Gaussian kernel regression: on a grid of 200 points spanning the observed range of p∗, we estimate
Pr(cover|p ∗) as a Gaussian-weighted average of the realized cover indicatorsCi, each game weighted by its distance
in price from that point (Nadaraya–Watson regression, bandwidth 0.05). We then form the miscalibration curve as
ˆθ(p∗) =p∗−cPr(cover|p ∗), which we summarize with its largest absolute valuesup| ˆθ|.
To generate a null distribution forsup| ˆθ|, we hold the observed prices fixed and draw counterfactual outcomes according
to the book’s implied probabilities:Ci∼Bernoulli(p∗
i ). We then recompute the supremum over 4,000 draws – the
p-value is the fraction of simulated suprema that reach the observed one.
References
Christopher Avery and Judith Chevalier. Identifying investor sentiment from price paths: The case of football betting.
The Journal of Business, 72(4):493–521, 1999. doi: 10.1086/209625.
Karen Croxson and J. James Reade. Information and efficiency: Goal arrival in soccer betting.The Economic Journal,
124(575):62–91, 2014. doi: 10.1111/ecoj.12033.
Jacek P Dmochowski. A statistical theory of optimal decision-making in sports betting.Plos one, 18(6):e0287601,
2023.
DraftKings Network. Betting splits. https://dknetwork.draftkings.com/
draftkings-sportsbook-betting-splits/ , 2026. Public handle and ticket percentages by market;
accessed 2026.
ESPN. Scoreboard api. https://site.api.espn.com/apis/site/v2/sports/, 2026. Final scores and game
status; accessed 2026.
Egon P. Franck, Erwin Verbeek, and Stephan Nüesch. Sentimental preferences and the organizational regime of betting
markets.Southern Economic Journal, 78(2):502–518, 2011. doi: 10.4284/0038-4038-78.2.502.
John M. Gandar, William H. Dare, Craig R. Brown, and Richard A. Zuber. Informed traders and price variations
in the betting market for professional basketball games.The Journal of Finance, 53(1):385–401, 1998. doi:
10.1111/0022-1082.155346.
John M. Gandar, Richard A. Zuber, R. Stafford Johnson, and William Dare. Re-examining the betting market on major
league baseball games: Is there a reverse favourite-longshot bias?Applied Economics, 34(10):1309–1317, 2002. doi:
10.1080/00036840110095427.
Philip K. Gray and Stephen F. Gray. Testing market efficiency: Evidence from the NFL sports betting market.The
Journal of Finance, 52(4):1725–1737, 1997. doi: 10.1111/j.1540-6261.1997.tb01129.x.
Ondˇrej Hubáˇcek, Gustav Šourek, and Filip Železný. Exploiting sports-betting market using machine learning.Interna-
tional Journal of Forecasting, 35(2):783–796, 2019. doi: 10.1016/j.ijforecast.2019.01.001.
Brad R. Humphreys. Point spread shading and behavioral biases in NBA betting markets.Rivista di Diritto ed Economia
dello Sport, 6(1):13–26, 2010.
Brad R. Humphreys. The financial consequences of unbalanced betting on NFL games.International Journal of Sport
Finance, 6(1):60–71, 2011.
Brad R. Humphreys, Rodney J. Paul, and Andrew P. Weinbach. Bettor biases and the “home-underdog” bias in the
NFL.International Journal of Sport Finance, 8(4):294–311, 2013.
Òscar Jordà. Estimation and inference of impulse responses by local projections.American Economic Review, 95(1):
161–182, 2005.
Bruno Jullien and Bernard Salanié. Estimating preferences under risk: The case of racetrack bettors.Journal of Political
Economy, 108(3):503–530, 2000. doi: 10.1086/262127.
Kevin Krieger and Andy Fodor. Price movements and the prevalence of informed traders: The case of line movement in
college basketball.Journal of Economics and Business, 68:70–82, 2013. doi: 10.1016/j.jeconbus.2013.04.001.
Tim Kuypers. Information and efficiency: An empirical study of a fixed odds betting market.Applied Economics, 32
(11):1353–1363, 2000. doi: 10.1080/00036840050151449.
16

APREPRINT- SEPTEMBER9, 2026
Steven D. Levitt. Why are gambling markets organised so differently from financial markets?The Economic Journal,
114(495):223–246, 2004. doi: 10.1111/j.1468-0297.2004.00207.x. URL https://pricetheory.uchicago.edu/
levitt/Papers/LevittWhyAreGamblingMarkets2004.pdf.
Tobias J. Moskowitz. Asset pricing and sports betting.The Journal of Finance, 76(6):3153–3209, 2021. doi:
10.1111/jofi.13082.
Marco Ottaviani and Peter Norman Sørensen. The favorite-longshot bias: An overview of the main explanations.
In Donald B. Hausch and William T. Ziemba, editors,Handbook of Sports and Lottery Markets, pages 83–101.
North-Holland, 2008.
Rodney J. Paul and Andrew P. Weinbach. Market efficiency and a profitable betting rule: Evidence from totals on
professional football.Journal of Sports Economics, 3(3):256–263, 2002. doi: 10.1177/1527002502003003003.
Rodney J. Paul and Andrew P. Weinbach. Does sportsbook.com set pointspreads to maximize profits? tests of the levitt
model of sportsbook behavior.Journal of Prediction Markets, 1(3):209–218, 2007. URL https://www.ubplj.
org/index.php/jpm/article/download/429/461.
Rodney J. Paul and Andrew P. Weinbach. Price setting in the nba gambling mar-
ket: Tests of the levitt model of sportsbook behavior.International Journal of
Sport Finance, 3(3):137–145, 2008. URL https://fitpublishing.com/content/
price-setting-nba-gambling-market-tests-levitt-model-sportsbook-behavior-pp-137-145.
Rodney J. Paul and Andrew P. Weinbach. Sportsbook behavior in the NCAA football betting market: Tests of the
traditional and Levitt models of sportsbook behavior.The Journal of Prediction Markets, 3(2):21–37, 2009.
Rodney J. Paul and Andrew P. Weinbach. NFL bettor biases and price setting: Further tests of the Levitt hypothesis of
sportsbook behaviour.Applied Economics Letters, 18(2):193–197, 2011. doi: 10.1080/13504850903508242.
Rodney J. Paul and Andrew P. Weinbach. Sportsbook pricing and the behavioral biases of bettors in the NHL.Journal
of Economics and Finance, 36(1):123–135, 2012. doi: 10.1007/s12197-009-9112-4.
Raymond D. Sauer. The economics of wagering markets.Journal of Economic Literature, 36(4):2021–2064, 1998.
Hyun Song Shin. Optimal betting odds against insider traders.The Economic Journal, 101(408):1179–1185, 1991. doi:
10.2307/2234434.
Hyun Song Shin. Prices of state contingent claims with insider traders, and the favourite-longshot bias.The Economic
Journal, 102(411):426–435, 1992. doi: 10.2307/2234526.
Hyun Song Shin. Measuring the incidence of insider trading in a market for state-contingent claims.The Economic
Journal, 103(420):1141–1153, 1993. doi: 10.2307/2234240.
Andrei Shleifer and Robert W. Vishny. The limits of arbitrage.The Journal of Finance, 52(1):35–55, 1997. doi:
10.1111/j.1540-6261.1997.tb03807.x.
Jay Simon. Inefficient forecasts at the sportsbook: An analysis of real-time betting line movement.Management
Science, 70(12):8583–8611, 2024. doi: 10.1287/mnsc.2022.00456.
Erik Snowberg and Justin Wolfers. Explaining the favorite-long shot bias: Is it risk-love or misperceptions?Journal of
Political Economy, 118(4):723–746, 2010. doi: 10.1086/655844.
Erik Snowberg, Justin Wolfers, and Eric Zitzewitz. Prediction markets for economic forecasting. In Graham Elliott and
Allan Timmermann, editors,Handbook of Economic Forecasting, volume 2, pages 657–687. Elsevier, 2013.
Rostislav Stanˇek. Home bias in sport betting: Evidence from Czech betting market.Judgment and Decision Making, 12
(2):168–172, 2017.
Richard H. Thaler and William T. Ziemba. Anomalies: Parimutuel betting markets: Racetracks and lotteries.Journal of
Economic Perspectives, 2(2):161–174, 1988. doi: 10.1257/jep.2.2.161.
Jonas Vandenbruaene, Marc De Ceuster, and Jan Annaert. Efficient spread betting markets: A literature review.Journal
of Sports Economics, 23(7):907–949, 2022. doi: 10.1177/15270025211071042.
Karl Whelan. Risk aversion and favourite–longshot bias in a competitive fixed-odds betting market.Economica, 91
(361):188–209, 2024. doi: 10.1111/ecca.12500.
Karl Whelan. On estimates of insider trading in sports betting.The Manchester School, 2025. doi: 10.1111/manc.12505.
Justin Wolfers and Eric Zitzewitz. Prediction markets.Journal of Economic Perspectives, 18(2):107–126, 2004. doi:
10.1257/0895330041371321.
Linda M. Woodland and Bill M. Woodland. Market efficiency and the favorite-longshot bias: The baseball betting
market.The Journal of Finance, 49(1):269–279, 1994. doi: 10.1111/j.1540-6261.1994.tb04429.x.
17

APREPRINT- SEPTEMBER9, 2026
Supplementary Information
Notation
Table 2 defines all symbols used in the paper, where we indicate the section in which each variable first appears.
Table 2:Symbols used in the paper.All bet shares are fractions of the total handle (i.e., normalized to 1).
Symbol Meaning Defined
Outcome and line
MRealized outcome: margin of victory, total, or player statistic Setup
sSportsbook’s posted line (e.g. point spread) Setup
Fm(s) Pr(M <s), the outcome CDF at the line (1)
¯Fm(s) Pr(M >s); the home side wins the proposition (1)
πpush(s) Pr(M=s), the probability of a “push’ where all bets are cancelled (1)
Bet shares
Bh(s), Bv(s)Public’s random bet share on the home / visitor side,B v = 1−B h Setup
bh(s), bv(s)Unconditional expected bet shares,b h =E[B h](7)
bh,L(s)E[B h|M <s]: home bet share when the home side loses (2)
bv,L(s)E[B v|M >s]: visitor bet share when the visitor loses (2)
bh,W (s)E[B h|M >s]: home bet share when the home side wins (7)
bmin, bmax minandmaxofb h,L andb v,L Prop. 5
Prices and the vig
ϕNet payout per unit wager on a winner (symmetric vig) (13)
ϕh, ϕv Net payouts on the home / visitor side (asymmetric vig) S1
τ ϕ/(1 +ϕ), the book’s break-even losing-side share (13)
p∗ Devigged (overround-removed) price of the home side Prop. S1
OOverround: the two raw implied probabilities summed Prop. S1
hHold: share of handle that a balanced book keeps,h= 1−1/OProp. S1
D2 +ϕ h +ϕ v Prop. S1
Profit and its drivers
π(s)Book profit per unit of handle (5)
Q(s)Expected share of handle on the losing side (6)
Qindep(s)Value ofQunder Levitt independence (S12)
δ(s)b h,L−b h,W : outcome covariance of the bet share (7)
θ(s)Shading: deviation of the posted price from the truth (8)
λ(s)Lean: deviation of the public’s bet share from balance (8)
GThe Goldilocks Zone (17)
Public-belief model
XLatent expected outcome (12)
YPublic’s noisy, biased belief aboutX(12)
εSystematic bias in the public’s belief (12)
V, UBelief noise and game randomness (12)
Estimation
Ci Realized outcome:1if the home side won covered in gamei(23)
πi Book’s profit margin for gamei(23)
S1. Asymmetric vigs, pushes, and the general profit–bias identity
We allow for asymmetric vigs: if a unit stake is placed on the winning home side, the bettor receives a gross return
of 1 +ϕh, and if a unit stake is placed on the winning visitor side, the bettor receives a gross return of 1 +ϕv, where
ϕh,ϕv >0 represent the bettor’s profit on a winning unit bet and satisfyϕhϕv≤1 . The latter indicates that the book’s
overroundO≡(1 +ϕ h)−1 + (1 +ϕv)−1 is at least one, and is exactly one only for a fair book. If the outcome is a
push (M=s ), all bets are returned. With total stake normalized so thatBh(s) +Bv(s) = 1, the sportsbook profit for a
single game is:
π(M;s) =



Bv(s)−ϕ hBh(s), M >s,
Bh(s)−ϕ vBv(s), M <s,
0, M=s.
(S1)
18

APREPRINT- SEPTEMBER9, 2026
Expected profit is computed by conditioning on the three outcomes{M <s},{M >s},{M=s} . IfM <s (home
loses), then using (S1) and the definition ofbh,L(s):
E[π(M;s)|M <s] =E[B h(s)−ϕ v(1−B h(s))|M <s] = (1 +ϕ v)bh,L(s)−ϕ v.
Similarly, ifM >s, E[π(M;s)|M >s] = (1 +ϕ h)bv,L(s)−ϕ h. IfM=s ,π= 0 . Taking expectations over the
three cases yields:
E[π(M;s)] =F m(s)

(1 +ϕv)bh,L(s)−ϕ v

+ ¯Fm(s)

(1 +ϕh)bv,L(s)−ϕ h

.(S2)
DefineQh(s)≡F m(s)bh,L(s),Qv(s)≡ ¯Fm(s)bv,L(s),Q(s)≡Q h(s) +Qv(s), and ∆ϕ≡ϕ v−ϕh. Substituting
into (S2) gives:
E[π(M;s)] = (1 +ϕ h)Q(s) + ∆ϕQh(s)−ϕ vFm(s)−ϕ h ¯Fm(s).
UsingFm(s) +π push(s) + ¯Fm(s) = 1 andϕvFm(s) +ϕh ¯Fm(s) =ϕ h(1−π push(s)) + ∆ϕFm(s), we obtain the
decomposition:
E[π(M;s)] = (1 +ϕ h)Q(s) + ∆ϕ
 
Qh(s)−F m(s)

−ϕh
 
1−π push(s)

.(S3)
Special cases.Ifϕ h =ϕ v =ϕthen∆ϕ= 0and (S3) simplifies to:
E[π(M;s)] = (1 +ϕ)Q(s)−ϕ
 
1−π push(s)

,(S4)
which implies the uniform bound E[π(M;s)]≤(1 +ϕ)Q(s) . Settingπpush(s) = 0 in (S4) recovers the profit–bias
identity (5) of the main text.
Anatomy of the book’s margin with asymmetric vigs.The three-term decomposition of the main text (Prop. 1)
can be generalized to asymmetric vigs by replacing the balanced-book reference 1
2 with the devigged price, and the
symmetric hold(1−ϕ)/2by the overround-implied hold.
Proposition S1(Anatomy of the book’s margin, asymmetric vigs).Assume πpush(s)≡0 and letD≡2 +ϕ h +ϕv.
Define:
p∗≡ 1 +ϕv
D , h≡ 1−ϕ hϕv
D , θ(s)≡p ∗− ¯Fm(s), λ(s)≡b h(s)−p ∗,
wherep∗ is the devigged implied win probability of the home side andhis the book’s hold. Then:
E[π(s)] =h+Dθ(s)λ(s) +DF m(s) ¯Fm(s)δ(s).(S5)
Settingϕh =ϕ v =ϕgivesp ∗ = 1
2,h= (1−ϕ)/2andD= 2(1 +ϕ), recovering(10).
Proof. Start from (S2) withπpush(s)≡0 . By the law of total expectation,bh(s) =F m(s)bh,L(s) + ¯Fm(s)bh,W (s);
together withδ(s) =b h,L(s)−b h,W (s), this yields:
bh,L(s) =b h(s) + ¯Fm(s)δ(s), b h,W (s) =b h(s)−F m(s)δ(s),
and sinceBv = 1−Bh,bv,L(s) = 1−bh,W (s) =
 
1−bh(s)

+Fm(s)δ(s) . Substituting both into (S2) and collecting
theδterms, whose coefficient isF m ¯Fm

(1 +ϕv) + (1 +ϕh)

=DF m ¯Fm, leads to:
E[π(s)] =F m

(1 +ϕv)bh−ϕv

+ ¯Fm

(1 +ϕh)(1−b h)−ϕ h

+DF m ¯Fmδ.
Expanding the first two terms and factoringbh yields:
E[π(s)] =

Fm(1 +ϕv)− ¯Fm(1 +ϕh)

bh +
 ¯Fm−Fmϕv

+DF m ¯Fmδ.
We evaluate the two brackets in turn. SubstitutingFm = 1− ¯Fm into the first and using (1 +ϕv) + (1 +ϕh) =D and
(1 +ϕv) =Dp∗:
Fm(1 +ϕv)− ¯Fm(1 +ϕh) = (1 +ϕv)− ¯Fm

(1 +ϕv) + (1 +ϕh)

=Dp ∗−D ¯Fm =Dθ.
Performing the same substitution in the second bracket gives ¯Fm−Fmϕv = ¯Fm(1 +ϕv)−ϕ v. Writing ¯Fm =p∗−θ ,
we have:
¯Fm(1 +ϕv)−ϕ v =

p∗(1 +ϕv)−ϕ v

−θ(1 +ϕ v) =

p∗(1 +ϕv)−ϕ v

−Dθp ∗.
The bracketed constant evaluates to:
p∗(1 +ϕv)−ϕ v = (1 +ϕv)2
D −ϕv = (1 +ϕv)2−ϕvD
D = 1−ϕ hϕv
D ,
19

APREPRINT- SEPTEMBER9, 2026
because(1 +ϕ v)2−ϕv(2 +ϕh +ϕv) = 1−ϕ hϕv. Substituting both brackets back:
E[π(s)] =Dθ(s)b h(s) + 1−ϕ hϕv
D −Dθ(s)p ∗ +DF m(s) ¯Fm(s)δ(s),
and collecting the twoθterms throughλ(s) =b h(s)−p ∗:
E[π(s)] = 1−ϕ hϕv
D +Dθ(s)λ(s) +DF m(s) ¯Fm(s)δ(s).
It remains to show that the constant 1−ϕhϕv
D is equivalent to the book’s holdh. Putting the two raw implied probabilities
in the definitionO≡(1+ϕ h)−1+(1+ϕv)−1 over a common denominator results in the numerator(1+ϕv)+(1+ϕh) =
D, such that:
O= D
(1 +ϕh)(1 +ϕv),
and hence:
1− 1
O = D−(1 +ϕ h)(1 +ϕv)
D = 1−ϕ hϕv
D =h,
where we have usedD−(1 +ϕ h)(1 +ϕv) = (2 +ϕh +ϕv)−(1 +ϕ h +ϕv +ϕhϕv) = 1−ϕ hϕv. The constant
term is therefore the share of handle that a balanced book keeps (i.e.,h), giving (S5).
S2. Recovering Levitt (2004) under independence
The profit-bias identity (5) is a strict generalization of the bookmaker-profit expression in Levitt [2004]. In Levitt’s
notation,p is the probability that the favorite wins,f is the fraction of total dollars wagered on the favorite, andv is the
vig; his expected gross profit per unit bet is:
E[πLevitt] =

(1−p)f+p(1−f)

(1 +v)−

(1−p)(1−f) +pf

.(S6)
The first bracketed term is the expected fraction wagered on the eventuallosingside, from which the book collects
1 +vper unit; the second bracketed term is the expected fraction on the eventualwinningside, on which it pays out1
per unit. Levitt’s expression is therefore of the formlosing share×(1 +v)−winning share, which follows as:
E[πLevitt] =

(1−p)f+p(1−f)

(1 +v)−

1−

(1−p)f+p(1−f)

= (2 +v)
 
f+p−2pf

−1,
which is his Eq. (2). His profit is thus already an affine, increasing function of a single losing-side share — the same
structural form as (5).
An important distinction between Levitt’s and our expressions pertains to the composition of the losing-side share.
In (S6),f is a singleunconditionalnumber, such that forming (1−p)f implicitly treats the favorite’s bet share as
statistically independent of the realized outcome. Identifying the favorite with the home side gives p= ¯Fm(s) and
1−p=F m(s), and imposing that independence gives:
bh,L(s) =b h(s) =f, b v,L(s) =b v(s) = 1−f,
such that our outcome-conditioned share (6) equates to Levitt’s bracket:
Q(s) =F m(s)f+ ¯Fm(s) (1−f) = (1−p)f+p(1−f) =f+p−2pf≡Q indep.
This shows alignment of bet shares, but not yet of profits. The two profit expressions are denominated in different
units and use different vig conventions – we reconcile the different conventions next, and then verify that the identity
reproduces Levitt’s Eq. (2) exactly. We note also that Levitt’s later step of writingf=f(p) with∂f/∂p>0 does not
affect his independence assumption: it describes how aggregate betting responds to thepostedline, not how bet shares
covary with therealizedoutcome.
Reconciling the two conventions.To allow a direct comparison between (5) and (S6), one must first reconcile two
bookkeeping conventions relating to (i) the vig and (ii) the unit of measurement of profit.
(i) The vig.Levitt’s v is defined relative to thewinamount: a losing bettor pays 1 +v and a winning bettor collects 1 (at
the standard−110 price, 110 is risked and 100 is earned, sov= 1/10 ). Ourϕ is the net payout per unitwagered: a
bettor risks1to earnϕ. The relationship between Levitt’svand ourϕis thus given by:
ϕ= 1
1 +v.(S7)
20

APREPRINT- SEPTEMBER9, 2026
For example,−110in American odds corresponds toϕ= 10/11andv= 1/10.
(ii) Normalization of profit.Our π(s) is the profit per unit ofhandle: total stake is normalized to Bh(s) +Bv(s) = 1.
Levitt’s “gross profit per unit bet” is denominated in the win amount, such that a single unit bet in his accounting puts
1 +vof handle at risk. One Levitt unit therefore carries1 +v= 1/ϕunits of handle, and the two profit measures are
related by:
E[πLevitt] = (1 +v)E[π(s)] = E[π(s)]
ϕ .(S8)
Exact recovery of Levitt’s Eq. (2).Applying (S7) and (S8) to the identity (5) yields:
E[π(s)]
ϕ = (1 +ϕ)Q(s)−ϕ
ϕ =

1 + 1
ϕ

Q(s)−1 = (2 +v)Q(s)−1.(S9)
If we assume Levitt’s independence and designate the favorite as the home side, (S9) follows as:
E[πLevitt] = (2 +v) (f+p−2pf)−1,
which is Levitt’s Eq. (2) exactly.
As will be derived in the next section, the difference between Levitt’s f+p−2pf and our Q(s) is precisely the
covariance between bet shares and realized outcomes. Levitt’s expression thus understates (or overstates) the book’s
margin whenever the public’s money tends toward the eventual loser (winner).
S3. Derivation of the independence test
Here we derive the statistical test of bet share–outcome independence (7), which implies equality between conditional
and unconditional bet shares:
bh,L(s) =b h(s), b v,L(s) =b v(s).(S10)
We show below that these two conditions collapse into a single equality, and thus bet share–outcome independence may
be assayed with a single test.
Consider the home condition first. Excluding pushes, the law of total expectation gives:
bh(s) =F m(s)bh,L(s) + ¯Fm(s)bh,W (s).(S11)
The unconditional share is therefore a weighted average of two conditional shares, with the weights given by the
probabilities of the two outcomes. Enforcingb h,L(s) =b h(s)leads to:
¯Fm(s)

bh,L(s)−b h,W (s)

= 0.
Assuming that ¯Fm(s)>0, this implies:
bh,L(s) =b h,W (s).
Note that the visitor loses the proposition precisely when the home side wins, such that:
bv,L(s) = 1−b h,W (s).
Combined with bv(s) = 1−b h(s), the requirement bv,L(s) =b v(s) is identical to bh,W (s) =b h(s). In turn,
bh,W (s) =b h(s)implies:
Fm(s)

bh,L(s)−b h,W (s)

= 0.
Both conditions in (S10) thus reduce to:
δ(s) =b h,L(s)−b h,W (s) = 0.
which is (7).
Excess profit from bet-share outcome dependenceHere we derive an expression for the change in the book profit
that is brought about by a non-zeroδ. Substituting (S10) into (6) yields the profit driver under Levitt’s independence:
Qindep(s)≡F m(s)bh(s) + ¯Fm(s)bv(s).(S12)
To relateQ indep(s)to the realized losing-side shareQ(s), it is helpful to write both in terms of home bet shares:
Q(s) =F m(s)bh,L(s) + ¯Fm(s)
 
1−b h,W (s)

, Q indep(s) =F m(s)bh(s) + ¯Fm(s)
 
1−b h(s)

.
21

APREPRINT- SEPTEMBER9, 2026
SubtractingQ indep fromQ(s), one obtains:
Q(s)−Q indep(s) =F m(s)

bh,L(s)−b h(s)

+ ¯Fm(s)

bh(s)−b h,W (s)

.(S13)
Employing (S11), the two bracketed expressions above may be written as:
bh,L(s)−b h(s) = ¯Fm(s)δ(s), b h(s)−b h,W (s) =F m(s)δ(s).(S14)
Substituting (S14) back into (S13) leads to:
Q(s)−Q indep(s) = 2Fm(s) ¯Fm(s)δ(s).
To connect the excess profit to the covariance between bet shares and realized outcomes, letI=1{M <s} represent the
indicator that the home side fails to cover, such that E[I] =F m(s). Note that one can write E[BhI] =F m(s)bh,L(s).
The covariance betweenBh andIis then given by:
Cov
 
Bh(s),I

=E[B hI]−E[B h]E[I] =F m(s)

bh,L(s)−b h(s)

=F m(s) ¯Fm(s)δ(s),
where in the last step we have used (S14). Putting all of this together, the excess profit can be written in two equivalent
forms:
Q(s)−Q indep(s) = 2Fm(s) ¯Fm(s)δ(s) = 2 Cov
 
Bh(s),1{M <s}

.(S15)
The significance of (S15) is that the deviation of our profit driverQ from Levitt’sQindep is twice the covariance between
bet shares and realized outcomes.
S4. Public-belief model:Qas a misclassification probability
Here we provide the proof of Proposition 4 in the no-push case where Pr(M=s) = 0 . We model the public’s belief
about the latent expected marginXwith:
Y=X+ε+V, M=X+U,(S16)
whereε is a systematic bias andU (game randomness) is independent ofV (belief noise). LetFU denote the CDF ofU
and letFV denote the CDF ofV.
Let the public bet the home side wheneverY >s. Define the Bernoulli indicator:
Bh(s)≡1{Y >s}, B v(s)≡1−B h(s) =1{Y≤s}.
This constrains the public’s bet share to the two extrema{0,1} , such that the public acts on the signalY and stakes
one side exclusively. This “specialization” converts the losing-side shares into misclassification probabilities but is not
restrictive forQ(s): with a continuum of bettors holding independent signals Yi =X+ε+V i, the home bet share
Bh(s) = Pr(Yi >s|X) = 1−F V (s−X−ε)∈(0,1) yields the sameQ(s) derived below, since integrating the
fraction overXreproduces (S20) term by term.
Recall the definition ofbh,L(s)andb v,L(s)as conditional expected bet shares on the losing side:
bh,L(s)≡E[B h(s)|M <s], b v,L(s)≡E[B v(s)|M >s].(S17)
BecauseBh(s)andB v(s)are Bernoulli, their conditional expectations may be written as conditional probabilities:
bh,L(s) = Pr(Y >s|M <s), b v,L(s) = Pr(Y≤s|M >s).(S18)
Substituting (S18) into the profit-bias identity (6) yields:
Q(s) = Pr(Y >s, M <s) + Pr(Y≤s, M >s).(S19)
Proof of Proposition 4. The claim follows immediately from (S19): the two events{Y > s, M < s}(public backs
home, home loses) and{Y≤s, M >s} (public backs visitor, visitor loses) are exactly the two ways that the public’s
signalY misorders the realized margin of victory M relative to the lines. The union of these disjoint events is the
event that the public backs the losing side, such thatQ(s) = Pr(public backs the losing side), which is the probability
of misclassifying the targetM >susing the predictor1{Y >s}.
22

APREPRINT- SEPTEMBER9, 2026
EvaluatingQ(s) under the public-belief model.From (S16), the dependence betweenY andM stems from the
shared latent variableX. Even ifU⊥V , the events{Y >s} and{M <s} are not generally independent; however,
they are independent conditional onX becauseY depends on (X,V) andM depends on (X,U) withU⊥V . We can
therefore write:
Pr(Y >s, M <s) =EX[Pr(Y >s|X) Pr(M <s|X)],
and similarly forPr(Y≤s, M >s). Conditioning onXgives:
Pr(Y >s|X) = Pr(V >s−X−ε) = 1−F V (s−X−ε),
and:
Pr(M <s|X) = Pr(U <s−X) =F U(s−X).
Therefore, combining with (S19):
Q(s) =E X[(1−F V (s−X−ε))F U(s−X)] +E X[FV (s−X−ε) (1−F U(s−X))].(S20)
Equation (S20) is the expression forQ(s)under the public-belief model.
To connect this to the losing-side bet shares, we write (S18) as:
bh,L(s) = Pr(Y >s|M <s) = Pr(Y >s,M <s)
Pr(M <s) = EX[(1−F V (s−X−ε))F U(s−X)]
Fm(s) ,(S21)
and
bv,L(s) = Pr(Y≤s|M >s) = Pr(Y≤s,M >s)
Pr(M >s) = EX[FV (s−X−ε) (1−F U(s−X))]
1−F m(s) .(S22)
Substituting (S21) and (S22) intoQ(s) =b h,L(s)Fm(s) +bv,L(s)(1−F m(s)), we recover (S20) identically.
S5. The Goldilocks book-profit region
We defineτ≡ϕ/(1 +ϕ). The book is profitable if (14) isQ(s)>τ, andQ(s)is affine inF m(s):
Q(s) =F m(s)bh,L(s) + ¯Fm(s)bv,L(s) =b v,L(s) +Fm(s)
 
bh,L(s)−b v,L(s)

,(S23)
such that (14) is the linear inequality:
Fm(s)
 
bh,L(s)−b v,L(s)

>τ−b v,L(s).(S24)
Below we prove Proposition 5.
Proof of Proposition 5. Writea=b h,L(s),b=b v,L(s),F=F m(s)∈[0,1] , so thatQ= (1−F)b+Fa is a convex
combination ofaandb; consequently,min(a,b)≤Q≤max(a,b), which is (16).
(i) Always.Ifb min(s) = min(a,b)>τ, thenQ≥min(a,b)>τfor everyF∈[0,1].
(ii) Never.Ifb max(s) = max(a,b)≤τ, thenQ≤max(a,b)≤τfor everyF∈[0,1], so (14) fails.
(iii) Threshold.Suppose min(a,b)≤τ <max(a,b) , such thata̸=b andF∗≡(τ−b)/(a−b) is well defined. If
a>b , thenb= min(a,b)≤τ <a= max(a,b) , so that 0≤τ−b<a−b ; dividing bya−b>0 givesF∗∈[0,1)
and (S24) becomes the condition F > F∗. If instead a < b, thena≤τ < b , so that a−b≤τ−b <0 ; dividing
bya−b<0 givesF∗∈(0,1] , and the direction of the inequality (S24) is reversed to yieldF <F∗. In both cases,
F∗∈[0,1]and (S24) placesF m(s)on the side ofF ∗ that assigns greater weight tob max(s).
The sufficiency ofb min(s)>τis case (i); the necessity ofb max(s)>τfollows from case (ii).
When the shares coincide (a=b=b L), (S23) reduces toQ(s) =b L(s) and the book profit is positive ifbL(s)>τ .
Intersecting the book-profit region with the bettor setB gives the Goldilocks ZoneG={s:Q(s)>τ}∩B , withQ(s)
given by (S23). IfF m is strictly increasing, bettor profitability (19) may be written in terms of quantiles:
B=

−∞, F−1
m (τ)

∪

F−1
m (1−τ),∞

.(S25)
The sufficient and necessary conditions of the main text follow by intersecting cases (i) and (ii) with membership of
Fm(s) in one of these tails; only the Threshold regime (iii) requires the joint values ofFm,bh,L, andbv,L at the sames,
and is therefore evaluated empirically.
23
