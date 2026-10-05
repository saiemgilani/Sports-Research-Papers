<!-- source: library/journals/Wharton Sports Analytics Journal/2024/2024 - SET Spatial Edge Technique A Framework to Evaluate Edge Setters - Bhatia et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/set-spatial-edge-technique-a-framework-to-evaluate-edge-setters/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2024 -->
<!-- authors: Viren Bhatia; Smit Bajaj -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

SET: Spatial Edge Technique - A Framework to Evaluate Edge Setters¶

Smit Bajaj, Viren Bhatia - Undergraduate Track (New York University)

## I. Introduction

Defensive plays on the football field require the effort of 11 players. However, defensive statistics only credit one or two defenders for the play’s end result (sack, tackle, interception, etc.). Our project focused on the off-ball contributions of the oft-ignored nine or ten others. In particular, we focused on a vital skill to stop the run — setting the edge.

Drawing from our experience as data science interns at AlphaPlay and working with teams from the EPL, NHL, and other global leagues, we've learned that professional organizations gain a significant edge by evaluating players' off-ball/off-puck contributions. We aim to demonstrate how the NFL teams can come to a similar conclusion — off-ball contributions are just as, if not more, important than the spotlighted on-ball ones.

Let’s begin with a concrete example from the NFL dataset: Take a look at this seemingly brushed over play in the 3rd quarter of the Lions vs. Cowboys game in Week 7.

Here’s a link to the video: https://youtu.be/DxZ453_5VVU

Here’s a couple frames,

Tony Pollard receives the handoff intending to head right, only to find Aidan Hutchinson (#97) dominate control of the outside edge. Pollard, now forced to run inside towards a crowd of Lions defenders, experiences an 25% drop off in speed and a 75-degree change in direction in 0.5 seconds.

Aidan Hutchinson not only wins this rep, but he disrupts the entire play. DeShone Elliott will be credited for a tackle for loss, yet Hutchinson — the catalyst for the tackle for loss in the first place — will not receive any credit in traditional stat sheets.

This play represents a fault in the realm of football analytics. Coaches in the film room will rightfully assign credit to Hutchinson for this play, albeit in an unquantifiable form. The stat sheet will miss it entirely, instead giving all the credit to DeShone Elliott’s tackle for loss. Our project set out to speak both languages by assigning a numerical grade to Hutchinson’s off-ball contribution.

SET: Spatial Edge Technique measures a defender’s ability to set the outside edge and force the ball carrier inside. This metric expands on ESPN Analytics’ revolutionary run-stop win-rate. More specifically, SET quantifies the extent to which defenders win control of the outside edge (as opposed to ESPN’s binary measure) and includes defensive backs and outside linebackers in its evaluation. From what we can tell, there is no public model or metric that specifically focuses on edge-setting. We hope to introduce a novel framework to quantify the “prelude to the tackle” in these select situations.

II. Setting the Edge Matters

This NFL Films YouTube video acted as inspiration for our metric and featured cameos of NFL head coaches speaking to its importance. In short, setting the edge is about restricting outside space for offenses. New York Jets head coach Robert Saleh refers to the practice as “throwing up a stop sign” to runners hoping to access the outside edges of the field. Offenses aim to horizontally stretch the defense. When a defender sets the edge, however, they counter by condensing the offense.

Here’s what Bill Belichick had to say about setting the edge:

“If the ball runs outside, the nose tackle and defensive end aren’t going to chase down the running back and so they’re all out of the play. But if you can set the edge of the defense and force the ball back inside, then all of those players are in their cutback lanes and you should be able to hold them to a minimal gain.”

III. Play Filtering

First, we narrowed our analysis to rushing attempts, ending our evaluation once the runner passed the line of scrimmage or was tackled, whichever came first.

NFL FastR’s play-by-play data includes a run gap variable with end, tackle, guard, and middle as the output values. We assume all end runs require an edge setter and automatically include these plays in our investigation. If a runner’s intention was to bounce outside and they later turned inside, however, the play must also be included in our dataset.

To infer a runner's intention, we projected their velocity vectors from behind the line of scrimmage forward for 0.5 seconds, essentially asking, “Where would the runner end up if they continued at this speed and direction for half a second more?” If any of these endpoints landed outside of the extended tackle box (includes tight ends), we assume an intention to run outside and include these plays in our dataset. An example animation is provided below. Even though both plays are coded as “up the middle”, our model rightfully flags the previously referenced Pollard/Hutchinson rep on the left. Here’s the link to our animation, https://youtu.be/fODHNfpv6dY

IV. Metric Creation

We have quantified player evaluation into a simple, two-step line of questioning. It goes as follows:

Question 1: How well did the Edge Setter get into Position? In defining “correct position”, it is first necessary to understand which parts of the field are valuable for an offense. We considered developing an all-encompassing model to value each part of the field based on a runner’s position, but found this to ignore team-specific differences. Instead, we opted for a more intuitive approach. The valuable space for a runner is simply the area they are headed towards. Defenses, in turn, constantly adjust their position based on the runner’s perceived location in the future. With this framework, we built off Bornn & Fernandez (2018) and Inayatali, White, Hocevar (2023) to develop a bivariate distribution model that dynamically maps out valuable space on the football field. Using the runner’s speed and direction, we are able to use this probability density function (PDF) to model a runner’s location 0.5 seconds in the future. Our formula alongside an animation is given below:

Ultimately, the edge setter’s goal is to win field control within our probability density function. To measure spatial control, we use Voronoi regions — a geometric tool that splits the football field into sections based on proximity to the nearest player. Voronoi regions are especially effective in the context of edge setting because they inherently adjust for leverage against a blocker. The angle of the bisector between the regions (highlighted in the yellow below) represents the blocking leverage on the play. As Giants defensive back Darnay Holmes erroneously switches his leverage position, the yellow line sweeps open. As illustrated via the red-circled Voronoi region, the Jaguars visibly gain control of this outside space. We use the shoelace algorithm listed below to calculate area.

Now equipped with a runner’s projected location and each edge setter’s field control, we simply overlay the two regions. The percentage of overlap between the runner’s PDF and defender’s Voronoi region represents the extent to which an edge setting places himself in the correct position, thus answering our original question with a number between 0 and 1 for each frame.

In the animation below, Matt Judon does not appear to “win” the block, although it’s clear he's in effective position. Consider how although Judon barely moves, his contribution to the play is among the defense's most valuable and accordingly, our SET metric rewards him. Here’s a link to our video, https://youtu.be/FvgJcM6G22g

Question 2: Did the runner change direction to the inside?:

After measuring the effectiveness of the edge setter’s positioning, we move to the action phase of our investigation. Our second question has a scale of outcomes — making the tackle is the most valuable end-state while losing the edge entirely is the least valuable. A value of 1 and 0 are respectively assigned to each other. Our model records a failed attempt if the runner’s direction shifts to the outside after encountering the edge setter.

When the edge defender does force the runner inside, however, a relative value between 0 and 1 is assigned. This value represents the extent to which a runner’s angle changes in five frames, standardized by 90°. For example, if an edge setter’s presence forces a 45° inside angle displacement five frames to the future, a value of 0.5 (45/90) is earned for the frame. 90° is practically selected as a complete side-to-side change in direction will entirely disrupt a runner’s momentum, thus accomplishing the edge setter’s intended result.

SET’s Final Composition

SET is a composite of the values assigned in both of these sections. Both scores are added and divided by two to give a final frame score. At the end of the play, these frame scores are added to evaluate an edge setter’s performance on a given play. The following images illustrate a step-by-step analysis of our SET metric.

## V. Results & Player Evaluation

In our focused analysis, we explore edge setting with three key positions: Defensive Ends (DEs), Outside Linebackers (OLBs), and Cornerbacks (CBs). Our approach utilizes a two-pronged metric. The first aspect is a straightforward binary success rate, effectively showcasing whether a player successfully set the edge during a play. It's a simple yet effective way to assess a player's ability to set the edge. Notably, OLBs like Josh Allen, Preston Smith, and Khalil Mack stand out in Week 7.

Complementing this, the second aspect dives into the quality of edge setting using our SET metric, asking: "How effectively did the player set the edge?" This is for evaluating and comparing player ability. Players such as Greg Newsome and Sauce Gardner, for example, have demonstrated their skill in executing plays that dramatically force the runner inside.

These findings are through nine weeks of data that was provided by the NFL. These players were the top graded players by their SET Percentile Ranking throughout the first nine weeks of 2022.

VI. Drawbacks & Future Work

There are a few shortcomings to using our approach that present future work opportunities:

● We have focused on one side of the ball, but the outside edge is a battle between the defense and offense. Our model can easily be flipped to evaluate how well offensive linemen turn defenders to create outside rushing lanes.

● In some instances, a defender spills, a technique where edge defenders deliberately slash inside the offensive line to open outside contain for an outline linebacker. While we recognize outside linebackers in our metric, it is possible that our model erroneously flags the defensive end as the edge setter.

● A tackle probability model can be merged with our work to determine how much tackling opportunity an edge-setter passes onto his teammates, thereby creating a team metric.

VII. Why Does This Matter?

In the referenced NFL Films video, coaches got visibly excited when discussing the nuances of edge-setting. Ravens coach John Harbaugh and former Cardinals/Buccaneers coach Bruce Arians have a popular saying in their practice facilities, “no edge, no chance.” Setting the edge is vital, yet largely overlooked in analytics due to its off-ball nature.

We predict analytics-savvy teams can unlock powerful first-mover advantages in this category. For example, a team can run our model in the pre-draft process to identify talented edge setters in later rounds. From here, these players can be strategically matched up against linemen with weak SET scores (assuming an inverse model is created) in run-probable scenarios to effectively restrict an entire part of the field. Defensive edge rotations can be reimagined in run-probable scenarios with a more precise understanding of one’s ability to set the edge.

This work highlights just one technique of many related approaches that can comprehensively alter how defensive impacts are measured.

You can find our code linked here. Feel free to reach out to us with any questions!

Smit Bajaj (Linkedin | Twitter | sb7983@nyu.edu) | Viren Bhatia (Linkedin | vb2180@nyu.edu)

--

A big thank you to Tej Seth, Zac Rogers, Brian Hall, Vince Gennaro, and Matt Manocherian.
