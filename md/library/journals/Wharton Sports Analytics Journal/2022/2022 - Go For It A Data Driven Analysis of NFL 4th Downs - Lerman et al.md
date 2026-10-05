<!-- source: library/journals/Wharton Sports Analytics Journal/2022/2022 - Go For It A Data Driven Analysis of NFL 4th Downs - Lerman et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/go-for-it-a-data-driven-analysis-of-nfl-4th-downs/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2022 -->
<!-- authors: Solomon Lerman; Bennett Stein; Nakul Solai; Ricky Martin -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Go For It?

Solomon Lerman, Bennett Stein, Nakul Solai, and Ricky Martin

Question/Intro

While a number of forward thinking NFL coaches such as Doug Peterson and John Harbaugh have adopted an analytical approach regarding their fourth down decision making, many have ignored such data.

Most NFL coach still base their decisions off of biased emotional matters such as “feel” and “momentum”. This inhibits them from making consistent fact based fourth down calls.

Other factors that contribute to this poor decision making are personal image and job security. Coaches tend to be over conservative in order to avoid possible criticism.

This leads us to the following questions:

● At what point is it beneﬁcial for an NFL team to go for it on fourth down rather than settling for a ﬁeld goal? ● Do NFL coaches need to be more aggressive in going for it on fourth down in plus territory in order to maximize points scored?

The Process

● We started by importing NFL play by play data from 2009-2019 ● Filtered the data to take out all non fourth down plays, and took out all penalties, ﬁeld goals, and punts ● This left us with all of the plays in which a team went for it on fourth down. ● We then sorted by yards to go and found the mean fourth down conversion percentage for each distance and plotted the result.

The Process (Continued)

● After compiling the fourth down conversion percentage data, we used a formula online to get the expected points for a ﬁrst and ten starting at each yardline.

● We then proceeded to plot the data.

The Process (Continued)

● We then set out to ﬁnd the expected points if you kick a ﬁeld goal from any given yardline

● To do this we found the overall percentage from each two yard bin over the last 10 years and multiplied each value by three (the value of a ﬁeld goal)

The Final Process

● To ﬁnd the expected points on fourth down, we multiplied the ﬁrst and ten expected points for each speciﬁc yardline by the conversion percentage of each fourth down distance. ○ For example, if it was a fourth and 3 at the 35 yard line, we multiplied the ﬁrst and ten expected points at the 32 yard line by the chance of converting a fourth and 3.

● With all of these graphs, we then made a ﬁnal model with the ﬁeld goal expected points along with the expected points of each fourth down distance from 1 to 10 yards.

● The model displays both the ﬁeld goal expected points and the fourth down expected points for each yardline 40 yards and in. sition

Note: This model is a baseline prediction on whether or not go for it on fourth down. It is based on the average statistics of all NFL teams. It is not intended to be used explicitly or situationally.

● Each blue line on the graph represents the expected points of each fourth down from within 40 yards of the goalline.

● The red line represents the expected points of a ﬁeld goal attempt from the 40 yard line and in.

What we found

● For an average NFL offense, we can conclude that at any yardline within the opponents 40, and you have a 4th and 3 or shorter, you are predicted to have more expected points if you go for it rather than kicking a ﬁeld goal

● With a 4th and 5 or farther, the expected points is higher if you kick a ﬁeld goal at any point within the 40 yard line of your opponent

● When tasked with a 4th and 4, it is the better option to go for it if you are within the 10 yard line or beyond the 35 yard line, at all other yard lines, the line overlaps with the ﬁeld goal line

● We can then conclude that teams need to be more aggressive on fourth down in plus territory
