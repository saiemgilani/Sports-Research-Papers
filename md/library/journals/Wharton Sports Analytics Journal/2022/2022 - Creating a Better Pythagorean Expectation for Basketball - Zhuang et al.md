<!-- source: library/journals/Wharton Sports Analytics Journal/2022/2022 - Creating a Better Pythagorean Expectation for Basketball - Zhuang et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/creating-a-better-pythagorean-expectation-for-basketball/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2022 -->
<!-- authors: Richard Zhuang; Baillie Weil; Andrew Hyde -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Can we make a “better” Pythagorean Expectation for Basketball?

By: Richard Zhuang, Baillie Weil, and Andrew Hyde

Points Per 100 Possessions vs. Per Game r2=.09 r2=.43

Points per Possession

Pythagorean Expectation for Basketball

This is the currently used formula for Pythag in basketball right now:

Pythag =

PF13.91 (PF13.91+PA13.91)

Our improved formula:

Pythag =

ORtg2 (ORtg2+DRtg2)

Our next thought:

Was the league tougher in some years than others? And if so, how can we adjust for that and ﬁnd a way to make all teams equal? So how do we do this?

This is what we came up with for Strength of Schedule per Possession: SOSPP= (ORtg) - (Average DRtg for the rest of the league in that year)

Final Product: SOSwPYTH= SOSPP x PythPP

Which Pythagorean expectation is better?

Theirs

Ours r2=.49 r2=.94

What can we do with this?

● Because we standardized for both competition between seasons and home-ﬁeld advantage ○ All-time teams? ○ NBA Coronavirus Bubble?

● Let’s do both!

Who are the best and worst teams of all time?

The Best: Most of the best teams have a SOSwPYTH > .6

The Worst: Most of the worst teams have a SOSwPYTH < .4

Playoﬀ Seedings after the simulated regular season games and play-ins

East

1. Bucks 2. Raptors 3. Celtics 4. Heat 5. 76ers 6. Pacers 7. Magic 8. Nets

Playoﬀ Bracket vs.

## Conclusion

● Per possession is better measure/predictor for success than per game ● We found a better pythagorean expectation for basketball ● Standardize for seasons and home-ﬁeld advantage through measure strength of schedule using per possession numbers ● Combine the new pythagorean expectation and the new strength of schedule ● Find the greatest/worst teams of all time ● Simulate the NBA bubble championship

Thanks for Listening

Questions?
