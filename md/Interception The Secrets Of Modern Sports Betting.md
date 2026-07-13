<!-- source: Interception The Secrets Of Modern Sports Betting.pdf -->

# Interception 

The Secrets of Modern Sports Betting 

# Ed Miller Matthew Davidow 

******ebook converter DEMO Watermarks******* 

Copyright © 2023 by Ed Miller and Matthew Davidow ALL RIGHTS RESERVED 

No part of this document or the related files may be reproduced or transmitted in any form, by any means (electronic, photocopying, recording, or otherwise) without the prior written permission of the author. 

For information about permission to reproduce selections from this book, write to 

Ed Miller 10624 South Eastern Avenue Suite A-995 Henderson, NV 89052 United States of America. 

##### <u>TheLogicOfSportsBetting.com</u> 

ISBN-13: 979-8-8636-1652-0 

Limit of Liability and Disclaimer of Warranty: The author has used his best efforts in preparing this book, and the information provided herein is provided “as is.” The author makes no representation or warranties with respect to the accuracy or completeness of the contents of this book and specifically disclaims any implied warranties of merchantability or fitness for any particular purpose and shall in no event be liable for any loss of profit or any other commercial damage, including but not limited to special, incidental, consequential, or other damages. Betting comes with an inherent element of risk, and the author specifically disclaims liability for any financial losses sustained in connection to the contents of this book. 

Trademarks: This book identifies product names and services known to be trademarks, registered trademarks, or service marks of their respective holders. They are used throughout this book in an editorial fashion only. In addition, terms suspected of being trademarks, registered trademarks, or service marks have been appropriately capitalized, although the publisher cannot attest to the accuracy of this information. Use of a term in this book should not be regarded as affecting the validity of any trademark, registered trademark, or service mark. 

******ebook converter DEMO Watermarks******* 

## For Carol and Mimi 

******ebook converter DEMO Watermarks******* 

# INTRODUCTION 

In our previous book, _The Logic Of Sports Betting_ ,[1] we introduced the paradigm of profitable sports betting as an information security problem. Infosec. As in hacking. That your goal as a sports bettor who is serious about trying to win is to find the flaws in the system, the glitches in the Matrix, the chinks in the armor. And, much as a hacker might, to then exploit those flaws to get what you want from the system. In the case of sports betting, the goal is to win money. 

This is essentially a book-length expansion of that concept. The modern sportsbook—really the entire modern sportsbook industry—is the system. The moment you open an account with any modern sportsbook brand, you are engaging the system. You have started the game. The assumption we make in this book about you, dear reader, is that from that point on, you are playing to win. 

That is to say, this book is not for the casual bettor. Casual bettors bet for fun and entertainment. Casual bettors want to win, of course. But the main reason they bet is because they enjoy the sweat, and because betting generally enhances their sports watching experience. They also value their ability to continue betting as long as they please without restriction long into the future. 

Casual betting is a completely valid way to engage with sports betting. It’s the way most people do engage with sports betting. It’s great. It’s just not what this book is about. 

We assume in this book that your goal in sports betting is to win as much money as you can (while staying quite clearly on the “right” side of things both legally and ethically). And, in doing so, you know that your experience with the modern sports betting industry will eventually end when you’ve been effectively kicked out of every major sportsbook brand. And you’re 

******ebook converter DEMO Watermarks******* 

totally fine with that. Because your goal is to beat the system—to play the game and to win it—not to avail yourself of entertainment. 

To do this, you will have to learn to look at a large sports betting menu and find the good bets. A “good” bet being one that will return a positive amount of money on average to the bettor. (Most sports bets, by virtue of the hold that sportsbooks place on their betting markets, return negative money on average to the bettor. The house does not always, but does usually, win.) 

If you’re conversant enough with gambling theory to know the term “expected value,” then when we say good bets, we mean bets with a positive expected value (+EV). If you aren’t familiar with that term, Google “expected value” right now and read up for half an hour. 

Towards this goal of identifying good sports bets, one may reasonably expect us in this book to go in-depth on the sports themselves, talking about statistical analysis and modeling. Data-driven this and that. _Moneyball_ shit. 

There is a little of that, but mostly no. This book is mostly about the system itself. The modern sportsbook. How it’s assembled. How it keeps prices updated second-by-second. Also, the businesses behind the brands. How the people who run them tend to think. How they build the technology to serve you with so many sports betting options and keep them available to you 24/7. And also the shortcuts they take along the way. 

A hacker’s greatest weapon is knowledge. Technical knowledge about computer systems. Social knowledge about how businesses are constructed —org charts, protocols, cultures. Once a hacker acquires enough knowledge about a system, the task of getting what they want out of the system becomes much easier. 

That is the philosophy behind this book. Armed with enough technical knowledge about how modern sportsbooks are put together and operate— and also how the people who work in the industry think and behave— getting what you want from the system will, we hope, also become easier. 

After years of experience on the betting side of things, in 2018, we (the co-authors) decided to found a business on the industry side. It’s a businessto-business odds feed provider. In the vernacular of this book, it’s a “sports betting content provider.” If that sounds like Greek to you now, it will make sense soon. 

In the ensuing five years, we’ve learned a ton about how this industry works—and doesn’t work—and the goal of this book is to share that 

******ebook converter DEMO Watermarks******* 

information with you, the bettor. At least to share the general industry, nonproprietary, non-trade secret part of that knowledge with you. 

We’ll elaborate more on our personal goals for the book in the conclusion, but up front we want to give what we hope is at least a provisionally satisfactory answer to the question, “If you work for the industry, why are you telling us how to break it?” Basically, it’s two things. One, we think that in some important ways we did things better in our company than the rest of the industry does it. So part of the equation is, we’re saying, “Here’s what everyone else gets wrong that we did right.” Our humility knows no bounds, you can see. 

But the bigger reason is that we think a lot of what’s fragile about the system—a lot of what a savvy bettor can take advantage of to win (which, by the way, you aren’t supposed to be able to do)—can and should be fixed. We think this book will get a lot of people up to speed quickly on how the modern sports betting industry works. And where it’s broken. We hope the book will give some smart readers perhaps the insight and personal motivation needed to do the work needed to fix the broken bits of this industry that we genuinely love. 

This isn’t a cookbook where you follow the recipe and money comes pouring out of the oven. It’s more of a scouting report. Sun Tzu said, “If you know the enemy and know yourself, you need not fear the result of a hundred battles. If you know yourself but not the enemy, for every victory gained you will also suffer a defeat. If you know neither the enemy nor yourself, you will succumb in every battle.” 

Once you read this book, you will know the enemy. What you do with that knowledge will be up to you. 

******ebook converter DEMO Watermarks******* 

# ANATOMY OF A MODERN SPORTSBOOK 

We’re going to start by looking at the anatomy of a modern sportsbook. The component parts, how they work together, some of the business considerations, and so on. 

Modern sportsbooks are technology businesses. Everything is software and data. Data and software. The problems we solved in our day-to-day work at our business are the same sorts of problems you would solve getting a university computer science degree. 

It was not always this way. In fact, until quite recently it wasn’t really this way at all. Not so long ago, sportsbooks were mostly human businesses —for lack of a better way of describing it at least. Vinnie at the bodega read lines from the morning newspaper and kept a notebook with all his customers bets. 

Even in Vegas where they kept track of the bets on computers, it was still mostly a human business. If you wanted to make a bet, you talked to a person at the counter, while another person made lines, yet another person approved large bets, and yet another person asked you if you wanted to make any new bets before paying you out in cash. 

Within the span of about twenty years, countries like the United Kingdom, with its relatively liberal rules (at least compared to pre-2018 rules in the United States) about sports betting, saw this change. Little by little, the companies that ran the sportsbooks built software to do the jobs the humans once did. Instead of placing your bet at a counter, increasingly you placed it on a website or app. Instead of a human approving each individual bet, algorithms started doing most of that. Instead of a human setting the odds and lines, this process too became increasingly automated. 

If you are an American, then you’ve seen this change happen not over twenty years, but over just one or two. Due to the pre-2018 prohibitions 

******ebook converter DEMO Watermarks******* 

(and due to quite stringent regulation, along with a little inertia, in Nevada) the old human-centric business model persisted here much longer than it did in Europe. And then, all at once, when the prohibitions were lifted, the modern sportsbooks rushed into the United States with their deposit bonuses and bet boosts and—more to the point here—their technology. Technology that was already two decades in development and usage in other locales. 

This quick change caught many experienced American bettors (and American industry folk) by surprise. Their decades of knowledge and lived experience had, in the blink of an eye, in many cases become obsolete. Oftentimes they didn’t notice or appreciate how profoundly things were changing. 

The industry in America has changed so much, so quickly, and is today so sufficiently complex that there’s an excellent chance that whatever you think you know about how it works is wrong. 

Let’s fix that, shall we? 

A great way to explore this topic is to walk through all the steps you’d need to go through to build a modern sportsbook from scratch. Just follow this here recipe, and soon all the drooling suckers of the world will be losing their gambling dollars to you instead of those corrupt, faceless corporations run by idiots. Right? Right?? (Hope you caught the sarcasm there.) 

“Mobile” is the way most bettors interact with sportsbooks these days. That is, they place bets on phone apps or websites instead of in person at counters or kiosks. If you want to launch a sportsbook, you need an app and a website. 

But slow down. First you need software that takes and settles bets. This bit of software is called the betting platform, and you can think of it as the engine that runs your operation. This is the software that keeps track of what bets are on offer and the current odds of each bet. It’s also the software that processes customer bets and keeps track of them. It’s also the software that allows you, the modern sportsbook operator, to settle the bets correctly. 

In the industry, this bit of software is usually discussed separately from a related and equally critical piece of software called the player account manager. The PAM, as goes the industry lingo, maintains the information about the bettors themselves. Account balances, personal information, all 

******ebook converter DEMO Watermarks******* 

sorts of regulatory thises and thats such as know-your-customer (KYC) information, and so forth. 

You need both. You need a platform to know about and manage the bets you offer, and you need a PAM to know about and manage your customers. And you need these two pieces of software to talk to each other, because the PAM has to tell the platform if a customer has enough money in their account to place a given bet, and the platform has to tell the PAM what the result of that bet was and how much to credit or debit the account for. And so forth. 

Okay, no problem. You just license some platform software, license some PAM software, hook them up, and you’re ready to go. 

Nope. If you actually go out and try to do this, you’ll quickly find out that it’s surprisingly hard to find anyone who will let you use their platform and PAM software, even for a fee. This software is scarce, and a big reason why is that these two pieces are heavily regulated in every jurisdiction. Which, if you think about it, is fair, because these are the bits of software that handle the money—who deposited, who withdrew, who bet what, how much they’re owed, and so on. And sports betting can get complicated— you’ve got straight bets, parlays, teasers, in-play bets, props, single game parlays, so on and so forth. And many of these bets (particularly the multibets) come with sometimes arcane rules about who wins how much in what circumstances and when. 

Your platform and PAM software have to handle all this perfectly. No bugs. No screw ups. A lot of what’s out there is software that has been in development already for decades. The folks who work in sports betting know well what software packages are out there, how they work, who owns them—and because they’re scarce, the who owns them part is often a <u>[2]</u> ~~.~~ source of industry intrigue 

Another problem is that it’s often the case that one company owns the platform software while another owns the PAM. And both of these companies are separate from yours—the one you started to run your sportsbook. Each of these companies has their own corporate goals and profit incentives. If you, the sportsbook operator, want to offer your customers some brand-new fancy-do bet type, you may have to get both the platform company as well as the PAM company to implement some new features to enable your vision. And they may well decide that your feature 

******ebook converter DEMO Watermarks******* 

goes very nicely on their ten-year roadmap. At the very end of their tenyear roadmap. 

Okay, so let’s say you’ve managed to work a small miracle and sign deals with people to use their platform and PAM software. And those people have agreed to do some work on their end to get your sportsbook up and running. Your customers can log in, they can deposit money, and they see—nothing. There are no bets. 

All the “what to bet on” content is a third, separate thing. You could solve this problem by hiring some people to type in betting markets manually. “Okay, the Bears play the Lions on October 26, and the line is ‑6.5, and the total is 52.5.” Done. 

The Vegas sportsbooks all used to do it this way—hiring linesmakers to type in and maintain the lines manually in the platform software. 

Unfortunately, manual data entry is obsolete these days. A modern sportsbook doesn’t just have a spread and a total and a moneyline and a prop or two. It has—on just one single game—dozens of spreads and totals, props on every relevant player, team props, bets on halves and quarters, the ability to parlay all of the above together with dynamic pricing, and in-play versions of all of the above. And micromarkets. It ain’t a manual job anymore. 

And modern sportsbooks don’t just offer NFL. They offer Nicaraguan netball and Hungarian hurley and Third Division Danish darts. 

It’s an absolute firehose of betting content—and if you want to offer it to your customers (and you do want to offer it if you intend to run a competitive modern sportsbook), you have to contract with content provider companies to provide it to you. 

We founded such a company, and while we can’t reveal too many particulars, know that generating this content and keeping it error-free and available second-by-second is a genuine problem for modern technology. 

As the aspirant operator of a modern sportsbook, you really have no hope of generating all this betting “product” (as the industry lingo calls it) it on your own. You have to buy it—from our company, from another company—realistically from multiple companies simultaneously to fill out your menu. Polish pole vault from one company and Cornish cornhole from another. Player props from one company and single game parlays from another. 

******ebook converter DEMO Watermarks******* 

That’s a handful more technology companies you have to deal with to stand up your sportsbook, and maddeningly, they all must play nicely with one another. The content companies with the platform company. The platform with the PAM. Sometimes the content companies with one another (even sometimes their direct competitors). 

Okay enough. What’s the point? The point is that it’s a damn miracle anyone makes this work at all. Modern sportsbooks are very sophisticated technology products that are held together with duct tape and crazy glue under the hood. The top three business priorities of the people who run them are, 

1. That they work at all, 

2. That they work at all, and, 

3. That they work at all. 

Everything after that is a secondary concern. Sportsbook operators want a product that offers bets, accepts bets, and pays out those bets correctly every time. A product that is up and available all the time (even—especially —ten minutes before the Super Bowl when millions of Americans are simultaneously trying to bet on Refrigerator Perry to somehow parachute onto the field mid-play, take a handoff, and rumble into the end zone). They want a product that meticulously follows all the myriad laws and regulations in all the various jurisdictions they operate in. They want to stay out of trouble. Those are the primary concerns. 

If you’ve ever used a modern sportsbook and had a thought, “This is dumb why do they do it this way? It would make more sense to do it that way…” the answer to your question will nearly always be, “It’s this way because the software components (platform, PAM, content feeds, other) that power the sportsbook work that way and those software components are inflexible for a number of reasons (regulatory, technical debt, political, inertia, other) and whoever runs the actual sportsbook company has no ability to make things work the way you think they should work even if they really wanted to.” 

Okay. Running a modern sportsbook is largely an exercise in piecing together a Frankenstein of technology components and then praying the monster comes to life when you power it on. This is the rule in the industry, but there are exceptions. The biggest, most successful modern sportsbook brands are a bit of an exception. We aren’t naming real life brand names in 

******ebook converter DEMO Watermarks******* 

this book for two reasons, one duuuh, and two whenever you happen to be reading this, the leading brands may be different from what they are when we’re writing it. But here we’re talking about the two or maybe three market leaders—you’ll know them when you see them. 

In general (and again, there are exceptions—exceptions always, naturally), the market leaders became the market leaders through successful repeated application of the following positive feedback loop. 

Step 1. Have some early success. (Due to marketing, product innovation, regulatory capture, right place/right time, many possibilities here.) 

**Step 2. Invest that success in technology.** As an example, perhaps building out their own player account management system to replace the one they were licensing from a third party. 

**Step 3. Don’t suck at building technology.** The thing built should improve upon the thing replaced. The newly built PAM is an improvement, and it passes regulatory scrutiny. Hooray. Use that improvement to build upon early success. 

**Step 4. Invest.** Use that now-built-upon success in further technology. **Step 5. Don’t screw that up.** Then use further improved technology to build more success. 

And so on. (Note the “don’t screw ups” in there. That’s the hardest part of all.) 

As a result of this process, the leading brands (and this is very much a count-them-on-one-hand sort of thing) often are not reliant on the ducttape-and-crazy-glue style technical infrastructure. Instead, they have a mostly in-house built technical infrastructure—at least for the most important software components. Because they own their most important technology pieces in-house—and because the in-house technology is mostly of high quality because it had to be at each step to perpetuate the positive feedback loop described above (foreshadowing here—this point becomes important a few paragraphs down)—these brands have more flexibility. They can bring new betting markets or products to their customers, for example, because they can design, implement, and release entirely in-house. This technical flexibility tends to entrench their already entrenched advantages over the rest of the pack. 

When PASPA was repealed in 2018 (if you didn’t know, this is the event that allowed modern sportsbooks to proliferate in the United States), there was a rush of would-be entrants to the new US market. Many such would- 

******ebook converter DEMO Watermarks******* 

be entrants seemed, how shall we put this, somewhat naïve to the technical realities we have just outlined. 

Soon they would realize the limitations of their duct-taped and crazyglued setups, and they looked at the market leaders for inspiration. They said, “Aha! I see it now. The market leaders all own their technology inhouse! We must also own our technology in-house and we shall compete with them!” 

There’s a fatal flaw in this logic, however (duly foreshadowed). The power of in-house technology is not merely that it is owned in-house, but also that it is well-built enough to have supported the organic growth of the business in the positive feedback manner outlined above. If you bring poorly built software in-house, you’ve only just created new problems for yourself. 

This logical flaw escaped many decisionmakers at the time, and in the name of “in-housing” they set about buying out the owners of component infrastructure pieces. If you owned a company that, say, developed licensable betting platform software in 2020, there’s an excellent chance that no matter the quality of your software, you were fielding acquisition offers. Numerous acquisitions occurred. Some later regretted. 

Okay again we return to the point. Modern sportsbooks can roughly be divided into two categories. The market leading brands, and all the rest. Understand that, if you download any sportsbook’s app to your phone, superficially, all the brands might look roughly the same. Markets on the left, prices in the middle, betting ticket on the right. 

Under the hood, they are not the same. Many of the also-ran brands are in “just hope it works at all” mode—and this attitude will permeate through to the customer experience. (That’s you.) 

Beating modern sportsbooks is about combining some (often fairly basic) sports-specific knowledge with fairly deep insight into the systems and technology that the sportsbooks use to deliver their product to you. Your goal is to exploit the flaws in their systems and technology. Knowing about sports often helps you to do that. 

This book is a primer on how modern sportsbooks deliver their product to you. What are you looking at? How does it get there? What are the hard problems they have to solve to get it to you? And where should you look for flaws? If you learn these concepts, then finding good bets on a modern sportsbook’s betting menu will be as easy as finding candy in a candy store. 

******ebook converter DEMO Watermarks******* 

Finding the good bets, it turns out, is the easy part. Convincing the sportsbook to let you stick around long enough to place those bets is much harder. We’ll have some thoughts on that topic as well. 

What have we learned so far? Modern sportsbooks are technology companies. Most brands are forced to build their technology stack by stitching together component parts owned and licensed by third party companies. While this strategy mostly “works,” in that it’s possible to bring a product to market this way, it tends to be creaky and inflexible. As a result, these brands have very limited ability to innovate their product offering. These brands will also tend to have a “just keep the lights on” mindset which bleeds over into their approach to customer experience and service. 

Leading brands often have gotten to that position by reinvesting successes over time into homegrown technology. As a result, they often have in-house options for the components other brands have to outsource. This gives them more flexibility to experiment with new products, markets, and so forth. In practice, this all means that some of their offering will be more polished (i.e., harder to beat), but that they’ll push the limits by offering bets other brands don’t (i.e., more betting options to find advantages in), and they’ll sometimes be at least a bit more tolerant of customers that are beating them. 

### The Betting Menu 

When you open a modern sportsbook on a web browser or mobile app, you’ll see a long list of bets you can make. This is the betting menu. This menu is what the industry refers to sometimes as “product.” Or you can think of it as the content (as in “content creator,” like the guy who snorts hot sauces on TikTok) that populates the betting platform the sportsbook provides. 

Most sports betting content is provided to sportsbooks by dedicated third party content creation companies. In some cases, and again this would be mostly at leading brands, the content creation for a substantial part of the menu is owned and operated in-house. For other brands, the content creation is nearly entirely outsourced. 

******ebook converter DEMO Watermarks******* 

If we say the word “oddsmaking,” and you think of a smoky room underneath a casino bar with a few hardened industry vets chomping cigars and pouring over lists of power ratings—nope. In Vegas—yes, perhaps even still today. Vegas sportsbooks are, for various reasons, caught inside a bit of a time capsule. Outside Vegas, not anymore. 

Alas, as much romance as we have for that process, this is not the way of the modern sportsbook. 

For the bulk of this book, we will go through the various parts of the betting menu—pregame and in-play, futures, full game lines and derivatives, alternates, team props, player props, single game parlays, micromarkets—and explain from where modern sportsbooks source this content for their menu, how the companies that create the content do it, and what the difficulties are in producing this content. We will explain which markets are harder to create odds for, and therefore where to look for beatable lines. 

Let’s be clear about what we mean by a beatable line. In any form of gambling, a bet is beatable or winnable by the bettor if the odds offered on the bet surpass the chance the bet wins. On a standard, double zero roulette wheel, the chance of winning if you bet on an individual number is 1 in 38 because there are 38 possible results. The odds offered are 35‑to‑1. For every 38 bets you make, on average, you will lose 37 of them for minus one unit each, and you win one for plus 35 units. Minus 37 units plus 35 units is minus 2 units on average for every 38 spins. The house wins. 

If the casino decided to offer you 40‑to‑1 odds instead of 35‑to‑1 odds, then it would be minus 37 units plus 40 units is plus 3 units on average for every 38 spins. The house loses, and you win. 

In roulette, the house feels extremely safe offering 35‑to‑1 odds on a roulette number knowing you can never really gain an advantage. Because the rules of the game—and Newtonian physics—dictate that the 35‑to‑1 odds offered will not represent a beatable bet. The house merely has to avoid the unforced error of offering 40‑to‑1 odds, and they can just put the table out on the floor and take on all comers. 

In sports there is rarely such safety. The principle is the same. The house is offering a menu of bets that will not—or at least should not according to its best guess—offer the bettor an advantage. The key word there however is “guess.” The certainty of simple math and the laws of the universe doesn’t carry over from roulette wheels to sporting events. Sports are 

******ebook converter DEMO Watermarks******* 

complex beasts. A sportsbook is never, ever certain that any bet it offers is not beatable. 

This is a key point. You open a sportsbook betting menu. The sportsbook is never, ever certain that any one of those thousands of bets it offers is good for them and bad for you. In fact, it’s unknowable. 

“But,” you may ask, “If the sportsbook can’t know whether a bet is good or bad for them, how can I?” Well, you can’t either. You are also guessing. 

The good news for you is that you have entered the territory of their guess versus your guess. If you concentrate on parts of the betting menu where your guesses are consistently better than theirs, you can win. 

To know whether you’re in those parts or not, you need to know how good their guesses are for each part of the menu, as this varies a lot based on the specific bet type. 

### The Betting Content Ecosystem 

You open your favorite modern sportsbook app, BeaverBet. And you go to this week’s NFL football games. The Bears are ‑9.5 against the Lions. Great. You like that new rookie Lions quarterback and the Bears are the public side and… STOP. You’re thinking like a sucker. 

None of that. 

Where does that ‑9.5 number come from? How does it get to your phone? 

It gets to your phone presumably via a network connection between your phone and some server associated with BeaverBet. Due to how sports betting regulations tend to work, there is probably a server physically located within the borders of your state or jurisdiction running an instance of the sportsbook’s platform software that is serving this number to your phone. 

How does the platform software know the number ‑9.5? Or, for that matter, how does it know about the Bears-Lions game in the first place? That information is provided to the platform software via an integration with a content provider. 

There are several different tiers of sports betting content providers available to a brand like BeaverBet, and the suits at BeaverBet would have to choose which of these content providers they want to use to populate its 

******ebook converter DEMO Watermarks******* 

sportsbook platform software with betting content. We will go over these options in detail later, but for this example, BeaverBet is most likely to get these pieces of information (the existence of the football game and the game line ‑9.5) from one provider in particular. 

For major sports, the sports league itself is likely to have struck a data distribution deal with one specific content company (or perhaps a small handful of companies). This specific company may be referred to as the “official” data provider for that league, where in this case “official” just means that the league has a contract with the company. It’s most likely then that BeaverBet would have signed a deal with whichever company is the official provider for, in this example, the NFL. Both the existence of the game and the number ‑9.5 likely would be provided to BeaverBet’s server via an always-on data feed maintained by that official provider. 

Where does the content provider company get the number ‑9.5 from? There is perhaps some small bit of secret sauce in the exact way this happens, but if you read our book _The Logic Of Sports Betting_ , you know that ultimately this line originates from a sportsbook—not BeaverBet, but some other one—that specializes in making markets. 

To recap the process from _Logic_ , someone in the world has to step up and be the first to offer betting on a game. This would be a sportsbook that doesn’t depend on this content provider system to fill out its menu, and that is, for lack of a better term, a bit old school. 

Whichever sportsbook this is likely has a fairly dependable schedule they stick to for when they open betting on a game, such that their customers know when they can likely expect betting to open on any given game. 

Once it’s time, someone at that sportsbook would then type “Bears versus Lions” into their platform software and take their best guess at a fair line and type that in as well. Let’s say they guessed ‑7.5. They’d publish the event, enabling their customers to make bets at the published line. But they’d keep the betting limits low at first. 

Early bird customers would be furiously mashing the refresh button on their browsers waiting for this betting to open. The moment the line appeared, any early bird customers with an opinion would start jamming in bets. The sportsbook would then move the line based on the bets. (This movement would likely be automated in software nowadays.) 

******ebook converter DEMO Watermarks******* 

If the first four bets all came in on the Bears, the line might move automatically to ‑8 or ‑8.5. As more bets came in, these bets would continue to push the line one way or another. Eventually, a sort of “crowd consensus” line would be reached where none of the early bird bettors any longer feels they have a winning bet they can make. 

To be clear, these people doing this betting are in no way “the public.” They are a very small number of extremely invested, often professional (or aspiring professional), gamblers who spend their evenings not at the bar with friends but instead refreshing obscure sportsbook websites with the goal of getting down good $200 bets. 

Anyway, once the first flurry of betting is over and the line settles at an equilibrium point, the sportsbook raises the betting limits. This spurs another flurry of betting—from people for whom betting just the $200 opening limit is a waste of time, energy, and good information. The line moves again and then settles. 

This process of finding an equilibrium line through reacting to betting pressure is called “price discovery.” At some point, the line is considered good, and the content provider companies begin to copy it and distribute it on to their customers. When we say “copy,” this could be via a content provision deal where the originating sportsbook is also acting as a first mover content provider. Or it could be literally someone looking at a website and copying the number into their software. Or it could be an automated copying process like web scraping. 

There is a misunderstanding common among people who work in the industry about this point of the process. Industry people will sometimes refer to these market making sportsbooks as a “source of truth.” And they will sometimes refer to these lines arrived at by price discovery as “true probabilities.” 

No and no. These lines represent the collective wisdom of a small handful of Adderall-addicted nerds. Don’t get us wrong. We don’t say that to disparage in any way Adderall-addicted nerds. If you think you know better than they do, nope. You don’t. 

But at the same time there is a massive disparity in the quality of “trueness” between probabilities determined by the laws of physics and mathematics (as they are typically determined in other gambling games such as card games, roulette, dice, and slot machines) and probabilities 

******ebook converter DEMO Watermarks******* 

determined by a few socially-challenged malcontents mashing buttons on a web browser. 

This misconception is far-reaching in its significance. The modern sports betting industry always wants more. More bets. Different bets. More bet availability. Parlays. Micromarkets. You name it. All of these offerings, we shall see, must be built mathematically on top of this foundation of pricediscovered probabilities. That foundation is much shakier than many in the industry understand it to be. This creates all manner of hidden flaws in the system, begging to be exploited. 

Anyway, that’s how that ‑9.5 gets to your phone. Someone, somewhere, days or weeks or months before was brave enough to throw up a guess and take a few bets. That line gets jerked around until it finds an equilibrium and then it is copied multiple times through a network of content providers until it gets to the one selected by BeaverBet to populate its platform with NFL betting markets. 

The process is roughly the same for every market that the market making sportsbook is willing to offer. They’ll have a moneyline and a game total as well, so those too get copied through. They’ll have first half prices. Maybe some first quarter prices. Maybe even a player prop or two. All those prices are price discovered and copied through in much the same way. 

But a market making sportsbook typically won’t offer the hundreds or thousands of different individual bets on a game the way a modern sportsbook does. If you want to bet that Shohei Ohtani strikes out 15 batters and hits three home runs and that the Angels somehow figure out how to lose anyway, you simply can’t do that at a market making sportsbook. That sort of bet is only offered at your favorite modern sportsbook. 

You open BeaverBet. You fire up the single game parlay interface and key in your selections. Ohtani strikeouts, Ohtani home runs, a Trout home run too why not, and of course that big old Angels L. 

In a flash, the BeaverBet app quotes you odds. 

Where in the heck do those odds come from? There’s no market line. No price discovery. How does that work? 

### Specialized Content Providers 

******ebook converter DEMO Watermarks******* 

There’s an entire ecosystem of betting content providers, and for the most part they focus on offering either breadth or depth. You’ll know a breadthfocused content provider if you pick up their marketing materials and they promote themselves by trumpeting that they can machine gun “ten quintillion events per year” into your sportsbook. You know, approximately. 

BeaverBet wants to make sure that if you really want to bet on second division Dominican disc golf, you won’t have to go to a competing brand to do so. So they integrate one (or likely several) breadth-focused content providers into their platform to make sure you can get that differentiated BeaverBet experience for as many worldwide sporting events as possible. 

But what about the Ohtani/Angels parlay bet? It’s a different company, a depth-focused content provider, that is making those odds for BeaverBet. 

<u>[3]</u> Depth-focused content provider ~~s~~ are often smallish firms that focus on a small number of sports and leagues and build out, well, a depth of offering. 

For example, a firm might specialize in player props for major American sports. This firm would then go around to everyone and declare themselves the best source for all American sport player props content. And if they did a good enough job marketing themselves as such, they might win themselves integrations into various sportsbook brands and/or bigger content providers (i.e., the breadth-focused ones). 

In order to move the needle here as a depth-first content provider, generally customers (i.e., sportsbook brands) will expect from you a lot of depth. Will Gronk score one touchdown? Will Gronk score two touchdowns? Will Gronk score three touchdowns? Will Gronk get exactly one reception? Will Gronk get exactly two receptions? Will Gronk get exactly three receptions? Will Gronk get exactly between 1 and 5 receiving yards? Will Gronk get exactly between 6 and 9 receiving yards? 

Now do that for every skill player on the field. 

If you’re a suit at BeaverBet and you decide that you want to offer player prop markets for American sports to your customers, then you would likely look first at your main, big, breadth-first content provider and see what they offer. If you’re satisfied with that offering, then you’ll just go with that, since you already have an integration with them and adding new integrations means adding new points of failure, there are economies of scale at play, and so on. 

******ebook converter DEMO Watermarks******* 

If you’re sufficiently unhappy with their offering, or if you want to make a plentiful player prop offering a defining pillar of the BeaverBet brand, then you might search for a smaller, depth-first content provider to integrate with in order to supplement what you get from the larger, breadth-first provider. 

The depth-first content provider’s main role is to calculate odds on large numbers of markets that aren’t covered by the market making sportsbooks. They do this primarily by building and maintaining proprietary mathematical models for the sports they offer. 

For example, say a baseball-focused content provider wanted to offer bets on if a home run will or won’t be hit in the Nth inning for every inning in every game. At baseline, the provider would build a mathematical model that takes the games main pregame lines as inputs. Say the Giants are playing the Dodgers, the Dodgers are 62 percent favorites, and the total is 8.5 at the current “market prices” (the prices determined by the price discovery process outlined above). This baseball-focused content company would maintain some sort of math that maps 62 percent and 8.5 to a distribution of home run outcomes for each inning. 

How sophisticated—or not sophisticated—this math is can vary widely. It could possibly be as simple as a lookup chart in an Excel spreadsheet. One sheet per inning, the rows are moneylines from 20 to 80 percent, the columns are totals from 5.5 to 16.5, and each cell holds the percentage chance of a home run hit in that inning. 

If a betting content provider were to use an approach this simplistic, naturally their home run markets would be easily beatable. By failing to take into account factors that clearly matter for home run rates—park, weather, starting pitcher tendencies (fly ball versus ground ball pitchers for instance), hitter tendencies, and so on—the model would implicitly be assuming at all times that these factors are “league average for the total.” That is, that all MLB games with 8.5 totals are “average” games with identical expected home run rates. 

You might think, “Well obviously a company specializing in making baseball betting markets would do a much better job than an Excel lookup chart I could make in a day.” Maaaaybe. Maybe not. It really depends. 

There are a number of business incentives within the industry to not do a very good job. Not to do a poor job on purpose, of course, but also to not spend a whole lot of effort and resources on trying to do it right. Recall that 

******ebook converter DEMO Watermarks******* 

many sportsbook brands are much more worried about making sure their product works at all than they are in the minutiae of exactly how accurate their betting lines are. And they are also worried about having a “competitive product”—i.e., to have more, more, more on their betting menu. Quantity first. 

In many cases it’s also quite hard to do a good job. Modeling sports and attempting to account for all the special cases is quite a difficult problem. In the coming chapters, we will go through different parts of the betting menu, talk about what sort of content provider work is likely behind the lines you’re looking at, and offer some thoughts about how you might look for ways to exploit it. 

******ebook converter DEMO Watermarks******* 

# A NOTE ABOUT LONGEVITY 

We’ll talk about this topic more later, but it behooves us to bring it up early. Modern sportsbooks don’t like customers who beat them. They are acutely aware that many of the bets on their menus are extremely beatable. If you do choose to beat them, they will not be impressed. They will just restrict your account. This means they’ll cut your betting limits so low that it will be a complete waste of your time to ever bet there again. Like they will cut your betting limits to literal pennies. 

Depending on which sportsbook brands you choose and exactly how you bet, they may limit your account after just a few bets. They may limit it as soon as minutes after you open the account. 

No matter what you do, if you try to bet with the goal of winning, your account at a modern sportsbook will eventually get limited to nothing. What is (sort of) under your control is how long you last and how much money you can win before the ax comes down. 

We will talk later about how sportsbooks identify “undesirable” customers, and we will offer some strategies on how to stay on the desirable list as long as possible before they eventually pull the plug. You’ll likely want to read through that section completely before you even open an account at your target sportsbooks. Anything you do can and will be used against you. And chances are, if you do what makes sense to you or comes naturally, you’ll be behaving exactly like everyone else out there who is also trying to beat them. You’ll fit their “undesirable” profile quickly, and— WHACK. 

Some people see how quickly modern sportsbooks toss anyone who they think is beating them and get angry about it. They see it as an injustice. We are sympathetic. 

******ebook converter DEMO Watermarks******* 

But we are also somewhat sympathetic to the sportsbook’s viewpoint. They see it as impossible to offer a betting menu as large as today’s menus are without offering beatable bets. (Practically speaking, this is true.) And they think that most of their customers would like to enjoy the large menu. (Also likely to be true.) And they know that if they let profit-minded bettors run wild through their betting menus without limitation, they would lose hundreds of millions of dollars to these bettors annually. (Not an exaggeration.) 

So they limit. It’s lame. But it also keeps the lights on. 

Personally, we think modern sportsbooks have a responsibility to try to harden as much of their menu as possible so that they can offer large parts of it without resorting to limitation. And that they should clearly mark the parts of their menu that aren’t hardened so you, the customer, can know where you risk getting shut down. 

Modern sportsbooks, however, do not do this. They reserve the right to limit anyone for any reason. And they use that right. We don’t think it makes sense to waste energy being angry at them about it. Just learn how to dance and have as much fun as you can before the music ends. 

******ebook converter DEMO Watermarks******* 

# SINGLE GAME PARLAYS 

The modern sportsbook is a European invention. The slick front end experiences. The unbelievably large betting menus. The network of software and content providers. All created by European betting companies over the past couple of decades. Most of the large industry firms are based <u>[4]</u> ~~.~~ in Europe, and they tend to fill their C-suites with European nationals 

Much of the collected industry wisdom and know-how is also still based in Europe. The people who build the software infrastructure and who know how it works. The engineers and quants. 

The modern sportsbook was also originally designed to serve the European betting customer. Europe is an extremely diverse place with dozens of different countries whose people speak dozens of different languages and follow dozens of different sports leagues. Each country has its own very different regulatory framework for sports betting. 

This pedigree created a specific set of problems that the first modern sportsbooks had to solve. 

1. Regulatory compliance in many very different jurisdictions 

2. Broad coverage of events in many different nations 

3. Localization 

It also meant that the engineers and quants focused most of their efforts on the sports most popular with European customers: soccer and tennis. 

Over the decade preceding the repeal of PASPA in 2018, much of the work on fleshing out content depth centered around these sports. For example, single game parlays—a relatively new betting product in the United States—were developed in Europe many years ago for soccer. (They are called “bet builders” there.) 

We note this European pedigree for two reasons. First, many of the people building out the content depth for US sports today are the same 

******ebook converter DEMO Watermarks******* 

people who worked on the problem before 2018. They come from Europe (and Australia), and their background is primarily soccer and tennis. 

Second, soccer and tennis are both in their own ways fairly simple sports to model. Soccer is a strongly team-oriented sport where nothing (from a betting perspective) happens for a while until one of a relatively limited number of discrete events occurs. A goal, a shot, a foul, a corner. Then more nothing. Then an event. And so on. 

The team lineups are published well before kickoff, and substitutions are fairly strictly limited. 

Tennis is a series of individual, discrete points played between two known competitors who don’t change (i.e., no substitution) throughout the duration of a match. 

Keeping these two points in mind, let’s talk about single game parlays for US sports. 

A single game parlay is special type of betting content that allows you to select multiple legs of a parlay on one game. Typically, the single game parlay menu is somewhat restricted compared to the non-parlayable betting menu. But even with the restrictions, you’re often able to parlay game outcomes, half or period outcomes, team props, player props all together. So you could bet, for example, that the Clippers will win the first half, but that the Warriors will come back and win the game, that the Clippers will score over 112.5 points for the full game, and that Steph Curry will score 6 or more three pointers. You select each of these parlay legs from the menu and then the software thinks for a brief moment and quotes you odds. 

What is happening when it thinks? And how does it come up with the odds? 

There are several ways content companies solve this problem. One way is to maintain a correlation matrix. This is basically a big table that stores how often various outcomes co-occur with one another. To price the parlay, one would multiply the correlation factors in the appropriate cells corresponding to the selected legs. 

Another way is to develop game simulators. This approach simulates the play of the game, 10,000 times perhaps, and then counts how many of the simulations satisfy the requirements of the parlay. 

Going with the second approach as an example because it’s simpler to explain, let’s say 231 of the 10,000 simulations would have hit all four legs of your parlay. That’s a 2.31 percent win rate. 

******ebook converter DEMO Watermarks******* 

Then the software adds hold. Usually a very healthy amount of hold is added for this sort of content—unfortunately the specific amounts can vary from sportsbook to sportsbook, are not disclosed to the customer, and can be difficult to reverse engineer. You can also expect more hold the more legs you add to the parlay. But maybe the software rounds that 2.31 percent win rate up to 5 percent and quotes you 19‑to‑1 odds on your bet. 

You might naively look at this 19‑to‑1 quote and conclude that this entire product deserves a wide berth. After all, 19‑to‑1 odds on a true probability 2.31 percent win rate is a very bad deal. After ten thousand tries for $1 each, you’d lose 9,769 of them for a total loss of $9,769. And you’d win 231 of them for a total win of $4,389. The net loss would then be ‑$5,380 for every $10,000 bet which is. Well, it’s bad. 

But this logic is flawed. The naughty words in the preceding paragraph are “true probability.” There is no such thing in sports betting. 

The odds the sportsbook offers are only as accurate as the mathematical model used to calculate them. In a sport like football, a mathematical model must account for a lot of details accurately. 

Let’s say, for the sake of argument, that you are a data scientist, and you work for a depth-first content provider known for offering a popular and successful tennis product. Your bosses now want to build out a football product they plan to use as a foothold for expansion into the US market. They’ve told you that it will be your job to build the football simulator that will price your company’s single game parlay product. 

You know tennis well, but you’ve never seen a complete American football game before in your life. What are you going to do? 

First you might watch a few video recorded NFL games to familiarize yourself with the basic rules of the sport. Then you might download a large NFL dataset sourced from another company in the complex network of content providers. Okay touchdowns are worth six. Field goals are worth three. Four downs. Got it. 

The dataset you downloaded came annotated with the pregame betting lines from the most reputable market making sportsbook. You have full game spreads, moneylines, and totals as well as first and second half lines for every game. 

You settle on the simulator idea and set out to design how it will work. The main inputs to your model will be the pregame betting lines. The 

******ebook converter DEMO Watermarks******* 

simulator will then play out the game (as well as you can code it to) following the rules of football (as you understand them to be). 

You will know you’ve done a good job with the first version if what you get out matches what you put in. That is, if you input ‑9.5 and 54 as inputs to your model, then you expect half your simulated games to cover ‑9.5, half to go over 54, half to cover +9.5, and half to go under 54. 

You test it for a number of reasonable combinations of spread and total and, if it passes, you’ve got something to work with. 

Let’s say you have gotten to this stage and your model is reliably returning simulations that match the pregame betting line inputs. You then check to make sure the moneylines match as well. 

And you have a problem. Your moneylines are within a percent or two for most inputs (e.g., if the moneyline in your source data says ‑150 for the home team, the home team wins between 58 and 62 percent of your simulations for that game). But for some inputs it’s off by more than that. And in a few cases it’s off by as much as 8 percent. 

That’s not good enough, so you go through your simulation logic and try to figure out what might be wrong. But you aren’t sure. You feel like you’ve accurately followed the rules of football, and your simulated teams (to the best of your knowledge) are playing like the teams in your dataset. 

Your bosses, meanwhile, have begun to breathe down your neck because they just signed a contract with a new US-based sportsbook customer to deliver this product at the beginning of the next NFL season. Delivery deadline is now T-minus two months and counting. 

Pressed for time and unable to find the logical flaw in your simulation, you layer an “adjustment” on to the scoring rates in certain parts of the simulator to snap everything correctly into line. 

Now you have to make sure your simulator also conforms to the first and second half lines in your dataset. It doesn’t quite yet, but you’re already close. You make a few tweaks to the first half, and, done. Well not quite done. The model answers within a few percent of the first half lines for about 75 percent of your test inputs, but it’s off by four or more percent the other 25 percent of the time. 

It’s time for another “adjustment.” Oops, that broke the moneylines again. You go back and readjust that adjustment. 

Football is an incredibly complex sport that is very difficult to simulate. Teams make large strategic shifts based on the lead and how much time is 

******ebook converter DEMO Watermarks******* 

remaining. The strategic shifts can be wildly different depending on if they’re ahead by exactly 10 or 11 or 12 points with nine minutes remaining in the fourth quarter. Some head coaches may make substantially different choices from other coaches. 

Then there are the little details. A team is down 4 points midway through the fourth quarter. They’re driving for a touchdown, but they get stopped near the 20‑yard line. Will they kick a field goal to try to go down 1 point? Or will they go for it to try and score the touchdown? For some coaches, the answer is field goal. For others, the answer is go for it. For yet <u>[5]</u> ~~.~~ others, the answer is they will go for it if the mood strikes them that day 

Then there are the oddities. A team’s place kicker goes down injured in the first quarter. A starting quarterback is injured and Tim Tebow (God bless him) is the backup. 

How do you capture all of these details into your simulation model and still ship it to your company’s customer in two months? The obvious answer is you don’t. The best you can hope to do is to get the basics right, ship the product, and then improve the model slowly over time. 

That is if you’re allowed the time and resources to improve the model. Rather than, say, your bosses deciding that football is shipped and now it’s hockey time. 

The models that price single game parlays are flawed. They’re all flawed. That’s a universal. 

We can tell you from personal experience that it’s very hard to build a football model that gets even the basics right. Team scoring, quarter by quarter. Touchdown rates. Field goal rates. 

It has to be right even for the edge cases. If one team gets out to a 21‑0 lead in the first five minutes, you need to correctly simulate the strategy changes both teams will make through the rest of the game. You also need to correctly simulate the game that is 3‑0 halfway through the third quarter. 

This is where models tend to falter—around the edges. The closer an inprogress or simulated game is running to an “average” game, the more bang on most models will tend to be. There’s more data to guide the model for average games because most games in the dataset are (by definition) somewhat close to average. 

As a bettor, you can probe a model’s edge cases by choosing certain legs on your parlay. For example, say you choose a leg where one team wins the first half by 21 or more points. By doing that, you’ve removed all the 

******ebook converter DEMO Watermarks******* 

“average” first half outcomes from consideration, and as you add more legs, you’re looking only at how the model performs in your somewhat uncommon early blowout scenario. 

Let’s revisit the plight of our data scientist on a hard deadline. Your bosses ask about the status of your model, and you proudly say that it (mostly) works (most of the time) to price out all the team-based bets on the menu. The bosses say, “Great. Now add player props.” 

This simple request adds a lot of new complexity. Now your simulator not only must model team-based variables correctly, but it also has to get the nuances of player usage correct as well. Let’s say the game is a blowout with one team up 28‑0 at halftime. Are there any players who will tend to get more play than expected in that situation? Less play than expected? 

What about kicker points? Will the coach of the trailing team be willing to kick field goals down 28? Or will they go for nearly every fourth down in field goal range until they close the lead? 

And then there’s the fact that skill position players fill specialized roles. One running back plays primarily on first and second down, takes a lot of handoffs, and catches the occasional pass. Another running back plays on passing downs due to superior pass blocking skills, is a moderatelyproductive outlet receiver, but gets few carries. Another running back tends to see the field on plays near the goal line. 

Think about that goal line running back for a moment. A relatively common box score line for that player could be two carries for 1 yard and a touchdown. How will you make sure your simulation model knows how this particular running back tends to be used and model it correctly? If you’ve barely seen three football games in your life, will this usage detail even occur to you to model correctly in the first place? 

As a bettor again, you could try a parlay for the goal line running back under 2.5 carries and a touchdown. This outcome could have a real-life likelihood of over 10 percent, while the model may not know that this player will tend to get the ball only on plays that begin on the 1-yard line. It may mistakenly assume that a running back who gets under 2.5 carries has almost no chance for a touchdown. 

The more options and flexibility that the suits want to add to their single game parlay betting menus, the more of these nitty gritty details the underlying model has to get correct. 

******ebook converter DEMO Watermarks******* 

It’s likely that if you go to your favorite sportsbook today and try to key in a bet like this, you’ll find that it doesn’t offer all of these options. But over time you can expect the list of options to expand. This industry wants more. More than they had last season. More than their competitor. More bets. More availability. More flexibility. More parlays. More, more, more. 

For single game parlay, adding just a few new options to the menu can place a surprisingly large burden on the underlying model. The possible bet combinations increase exponentially. 

Basketball is a somewhat simpler sport than football to model from a team scoring perspective. But add in player props and it becomes similarly complex. If one team is up, say, 25 points at the half, how many minutes will the star players on either team see in the second half? (In basketball, handicapping player props is typically an exercise in handicapping minutes.) There’s obviously no one-size-fits-all answer—if the data scientist building the model just goes with “average” here, they’ll be wrong in nearly every specific instance. 

A notorious single game parlay failure involved Draymond Green of the Golden State Warriors. On January 9, 2022, Green was injured and slated to miss the game. But his teammate, Klay Thompson, was returning to action that night after recovering from a ruptured Achilles tendon. Green wanted to honor his teammate’s return by playing one ceremonial possession together. So Green started, played a few seconds, and then was done for the night. 

Bettors who knew about Green’s plan took advantage of single game parlays on the game by parlaying all of Draymond Green’s under props. 

Sportsbooks take a dim view of customers who take advantage of errors like this one. If you try to place a bet like this, it’s obvious what your idea was if not in the moment, certainly in retrospect. There’s an excellent chance that anyone who went through with this bet had their accounts flagged as a potentially undesirable customer. (Though it was such an obvious angle at the time, our guess is that a lot of “desirable” customers also got bets down on that one.) 

Consider the softer version of that situation, however. A key player is injured and questionable to play. They might play their normal minutes, or they might play just a few minutes, feel the injury flare up, and sit for the rest of the night. In this situation, parlaying all the under props together could be a good bet. It wouldn’t be the sure thing it was in the Draymond 

******ebook converter DEMO Watermarks******* 

Green example, but for longevity’s sake you shouldn’t be looking for sure things. A merely good bet is ideal. 

Modern sportsbooks love single game parlay products because they check two boxes. One, recreational customers love them. Two, they have very high hold percentages. Some would-be sharp bettors allow the high hold percentages to scare them away from the product entirely. 

It’s true, single game parlay products add a very healthy hold to the “true odds” that the model working behind the curtain calculates. If you play into these products without thinking carefully about how to exploit the modeling flaws, you will indeed get killed. 

But on the flip side, the modeling task is nearly impossible from the product creator’s perspective. If a sportsbook wants to offer a generous choice of betting options (and every sportsbook does), then the intrepid bettor can explore all the modeling edge cases with a few well-chosen parlay legs. 

The models will fail in some of these edge cases. If you play with these products enough, you will find outcomes that the model thinks are nearly impossible, but due to some difficult to account for factor such as player usage, injury chance, or coaching peculiarities, the real-life outcome is actually quite likely. Adding a set amount of hold (even if it’s quite a bit) in the final step isn’t enough to protect the sportsbook in these situations. 

Single game parlay products will always be vulnerable. As sportsbooks add more betting options to the menu, those options just give you more tools with which to break the machine. 

******ebook converter DEMO Watermarks******* 

# IN-PLAY BETTING 

The odds and lines posted at market making sportsbooks are “sharp” because there is a small but dedicated community of serious bettors who bet every line until a sort of community consensus is reached. 

The entire multi-billion dollar betting content ecosystem depends on the opinion of this tiny community of bettors. As we saw in the single game parlay section, the companies that build out betting product use the market makers betting lines in several ways. They use them as key data points when building their models. They also use them as model calibration north stars. The model takes the market maker lines as inputs, and it’s tuned until it successfully regurgitates those lines back out on the output end. 

The assumption underlying the entire exercise is that these lines are “true.” This assumption for the most part, most of the time, holds reasonably well (note all the qualifiers). The assumption holds well enough in most cases that the content industry gets away with treating these lines as gospel even though they aren’t. 

This tiny community of bettors, at least at the time of this writing, is mostly focused on pregame betting. If you view the lines at the market maker as an up-to-the-second price check on how the serious betting community values a game—then the continuous stream of price checks goes dark the moment the game kicks off. 

Once a game starts, information about the outcome of the game starts flooding in. Balls bounce. Points get scored. On the field strategies start working or not working. Players get injured or into foul trouble. 

But the information feed about what the serious bettors think of all this (the market makers betting line) goes almost completely silent. 

Yet if you go to your favorite modern sportsbook and pull up the betting lines for an in-progress game—particularly for a major American professional league game such as NFL, NBA, or MLB—you’ll see a ton of 

******ebook converter DEMO Watermarks******* 

betting options. If not from the market maker, if not from the collective wisdom of Adderall-addicted nerds, where do all these lines come from? 

They come from depth-focused betting content companies. Like the single game parlay, they come directly from statistical models built and maintained by these companies. 

The underlying model here could be built using one of a number of different mathematical techniques. Since its job is to price individual markets without having to worry about parlays and correlations, a simulation model isn’t as obvious a choice. It’s entirely possible you could look at the source code of a model designed to price in-play football markets and see very little obvious reference to the game of football. 

Regardless, as a bettor the exact design of the underlying model will always remain a bit of a black box to you. The key ideas though are: 

1. The prices come from a model. 

2. The model was built by a human being, and like all models, it has flaws. 

3. The prices for the most part do not come from a price discovery process, and therefore they do not represent the “wisdom of the crowd.” 

This last point holds more true during some portions of a game than it does during others. As a trivial example, say you’re watching an OriolesRed Sox game, and the Orioles were ‑140 favorites pregame. After the first pitch of the game (a ball), the Orioles are still ‑140 favorites (which is now priced ‑150 because the sportsbook adds extra hold to their in-play markets). 

These in-play odds clearly still reflect the pregame wisdom of the crowd, as nothing of too much significance has happened in the game, and so the pregame odds are still offered. 

The deeper you get into the game, the more things happen, and the less of that pregame wisdom remains in the offered odds. An exception to this trend occurs right after halftime in football and basketball. Serious bettors do create a little mini betting market during halftimes, and the in-play lines get a wisdom injection. But this post-halftime wisdom tends to dissipate quickly once the game resumes. 

******ebook converter DEMO Watermarks******* 

In a football or basketball game, lines offered roughly speaking during the second quarter and then again beginning halfway through the third quarter to the end of the game contain relatively little of that price discovery market sharpness, and instead lean heavily on the outputs of someone’s model. 

Among modern sportsbooks (for American sports) there are a small handful of independently run models that price these in-play markets. The very biggest sportsbook brands may have an in-house team that maintains and operates its own pricing models for major sports like NFL and NBA. Other brands must source their in-play betting lines from third party content companies, and there are few to choose from that price the major American sports. 

So how do these models work? 

Like the ones designed to price single game parlays, typically they will take the pregame betting lines as inputs. As additional inputs, they’ll take information about the current state of the game. The score, the time remaining, who has the ball, and so on. And the job of the model is to transform those inputs—the pregame betting pricing information plus the in-game game state information—into an array of betting lines. 

In its raw form, that’s how it works. Inputs into model, model spits out prices, prices transmitted to sportsbook brands, sportsbook brands offer bets to customers. 

Let’s say for the sake of argument that there are five independent models in the marketplace to price in-play five-a-side pickleball. And there’s also a mature pregame betting market for five-a-side pickleball. 

Each of the five companies that maintains a model starts it in the same place. They want their prices to match the price discovered pregame prices, so they use whatever inputs their model requires to get that answer out of it. 

As the game begins, the models still match one another, because nothing much has happened yet, and so the pregame prices still dominate. To be clear, we don’t mean that no points or runs or goals or wickets have been scored or whatever thing one does in five-a-side pickleball to try to win the game. These things may have happened, and the models will all have adjusted their offered prices for the score. 

It’s just if you ask a model the question, “If the Dallas Dills were 64 percent to win pregame and they score first wicket after three minutes have elapsed in the match against the Saratoga Sweet Pickles, then what is the 

******ebook converter DEMO Watermarks******* 

Dallas Dills new winning chance?” it just tends not to be particularly difficult to come up with a reasonable answer mathematically. You can expect any production-quality model to offer a price that’s in the ballpark. 

But as the game proceeds further, the models begin to diverge. More things happen, and the peculiarities of one model versus another begin to dominate. At this stage, if the five companies that maintain models all continued to publish the raw outputs of their models to their customers, then arbitrage betting opportunities would present constantly. 

As a review from _The Logic of Sports Betting_ , an arbitrage exists when the prices offered between two different sportsbooks give the bettor a negative synthetic hold. Say BeaverBet is offering the Dallas Dills at ‑220 odds or 69 percent to win, while their rival, BetBeaver ~~,~~ <u>[6]</u> uses a different content provider and model and is offering the Sweet Pickles at +300 odds or 25 percent. You could theoretically bet on both teams simultaneously at these prices and lock in a profit. If you were to bet $220 on the Dills at ‑220 and $80 on the Sweet Pickles at +300, then no matter which team won, your two bets would return $320 on a $300 investment. 

We say “theoretically” lock in a profit, because just because a price appears on your web interface or phone app does not mean you can successfully place the bet. Sportsbooks may reject your bet for any number of reasons, and in-play they often do. 

If an arbitrage exists—any arbitrage—then it means at least one of the two models involved must be wrong. It’s possible that both are wrong. But at least one must be. 

In reality it’s likely that at least four of the five models (and possibly all five) are quite flawed, and they publish “wrong” prices very regularly. Modeling sports is genuinely very difficult. Sports matches are dynamic, chaotic processes, and there are lots of factors a model needs to account for. 

Arbable pricing doesn’t create a bettable opportunity—it just makes the opportunity obvious to a casual observer. The bad model is what creates the bettable opportunity. 

Sports betting content companies do not want the warts of their models exposed, so to avoid this, they fudge the inputs of their models to close arbitrages. Whoever operates the model that feeds BeaverBet will watch the prices of the other models in the marketplace. Any time their model is offering a price that represents an arbitrage with any of their competitors, they will adjust the inputs (e.g., the pregame betting line inputs) until the 

******ebook converter DEMO Watermarks******* 

prices their model spits out no longer represent an arbitrage with any of the four other models. 

This adjustment process can be manual or it can be automated. 

Sometimes the five models have diverged so much that it’s impossible to close the arbitrage with all of them at the same time—closing one arbitrage will open another. What people do in that case is they tend to favor the prices of one of the models over the others. 

This favored “source of truth” model tends not to be chosen through any sort of objective analysis of its pricing capabilities, but rather on the general industry reputation of its operators. If ReallyGoodFootyBets, Inc. built a soccer model in 2013 that was generally well-regarded, then industry folk will assume the five-a-side pickleball model ReallyGoodFootyBets, Inc. rolled out in 2023 is also of superior quality. 

Or they’ll favor whatever model happens to be used at the market <u>[7]</u> ~~.~~ making sportbook they tend to look to for their pregame prices Despite the fact that relatively little price discovery process goes on in-play and therefore all the advantages that the market making sportsbook has in producing “sharp” pricing are gone. Industry-wide thinking often goes no deeper than “That book is sharp, let’s key off their prices.” 

Anyway, content providers hate arbitrages because if they have an arbitrage with another provider, they know that one of the two must be wrong. Content providers tend not to have conviction that their model is the correct one. 

Thus far we’ve looked at one of the two main components of the model inputs—the pregame betting line. The second main component is a game state. 

Most content providers source this game state information from what the industry tends to call a “data feed. ~~”~~ <u>[8]</u> This data feed is provided by yet another content provider company. 

This game state data is created ultimately by a human sitting in the stands at the game. If it’s a lesser-known sport or match, then the content provider company will often contract with someone local to the match to gather the data in real time. This person is called a scout. 

For example, if five-a-side pickleball is an organically growing competition that lacks a strong centralized organizing league, then one or three or five content companies might take it upon themselves to hire local 

******ebook converter DEMO Watermarks******* 

scouts to gather data. Scouts will use an app on their tablets designed to input the pickleball-related affairs quickly in real time. 

And that’s it. If the scout has to go to the bathroom, the data may just be spotty for a moment. Or if one scout just isn’t that great at their job, then the data feed for games they work also just won’t be that great. 

Nevertheless, these raw data feeds will often be used directly as an input to the models that produce betting lines. 

For large sports with centralized leagues, the league will often strike an “official data” deal with one content provider company, granting that company an effective monopoly on distributing the game state data. There’s often a bit more redundancy and error-checking that comes with such a data feed—you aren’t out of luck just because Joe the scout decided to buy a pretzel—but at the end of the day it’s created by human beings at the game recording their observations in real time. There can be delays and errors. 

As you might imagine, if bad or slow or simply wrong game state information is fed into an in-play betting model, the model is likely to publish bad betting lines. 

This happens regularly in all major American sports. 

College sports deserve a particular callout here, as the quality of available data can vary widely from game to game. One game might have very fast and accurate data, while another game has errors and up to twominute delays. This variability can be seen in both low- and high-profile games. 

On top of the obvious problems with slow and error-prone data feeds, there’s a more subtle problem with these feeds that is nearly universal. They omit important data points that are relevant to making betting lines in real time. 

Say you’re watching a football game and the offense completes a 35‑yard pass downfield. But two referees throw flags in the backfield. Depending on where and how these flags were thrown and what you saw as the play developed, you might immediately know that the play will be called back for offensive holding. 

That information is typically not in a data feed. The notification in the feed of the flag may be fast or it could be slow—sometimes much slower than seeing it on television. So you might get a “flag on the play” in the feed, and it could come quickly or not as quickly. 

******ebook converter DEMO Watermarks******* 

But no data feed will tell you that the flag is likely for offensive holding. The only way to know that before the referee announces it on the field is by inference from years of experience watching football. 

At nearly any stage of a football game, the difference between a completed 35‑yard pass and a 10‑yard penalty for 1<sup>st</sup> and 20 causes a bettable difference in betting lines. (I.e., if a model prices in the 35‑yard gain, but the play is called back for a holding penalty, then you would have a profitable bet against the penalized team.) 

This happens regularly. Models price in the result of the play, but anyone watching will know that it’s getting called back. 

Coaching challenges in any sport also create a situation where anyone watching the game will have substantial, useful, bettable information about the game that will not be present in the data feed. The challenges create long delays, and a viewer familiar with the sport will often be able to predict with high accuracy the outcomes of many challenges. The data feed makes no such predictions, and any lines the data feed-driven models make during these periods will be wrong. 

An additional recurring problem for content providers is that they’re asked to make numerous markets beyond the main ones. They can close arbitrages with competing models for the main markets like the game moneyline, the main spread, the main total, and so on by tweaking the inputs. 

But the models also spit out numerous other markets as well. Half and quarter markets. Alternate point spreads. Props. 

There is today an increased focus from the industry side (read: a rabid pursuit of without due regard to the substantial technical and mathematical challenges thereof) on expanding in-play betting menus with large numbers of props. Team props. Player props. Also fast resolving prop bets the industry terms micromarkets. 

The industry would like to offer you yardage and touchdown props on all the important players throughout an entire football game. Points, rebounds, and assists props on all the important players throughout an entire basketball game. Strike out, home run, hit, run, and RBI props on every player throughout an entire baseball game. 

They want you to be able to bet on the outcome of increasingly smaller chunks of the game. The outcome of a drive in football. The outcome of a 

******ebook converter DEMO Watermarks******* 

play. The outcome of a possession in basketball. The outcome of an at bat or even a single pitch in a baseball game. 

The industry likes to think of these sorts of bets as a collective leap forward in betting technology, but in reality all of these new markets will be produced and delivered in exactly the same way current in-play markets are produced and delivered. Content companies will maintain models for the sports and will regurgitate the model predictions as betting lines. The betting lines will only be as good as the models are and as the data feeds that supply them with game state information. 

Currently, content companies spend much of every game fuzzing the inputs of their models with the goal of avoiding the much-feared arbitrage. They’re afraid that their models are lacking compared to their competitors models ~~.~~ <u>[9]</u> 

It’s practical to fuzz inputs to close arbitrages on a few main markets. But now they plan to offer dozens if not hundreds of new markets in-game that are essentially unfuzzable. 

We don’t really have any particular callouts here—specific markets or situations to look out for and such. You can just expect the lines on any new in-game prop markets you see to be very vulnerable. These lines represent the raw, regurgitated guts of sometimes oversimplified and miscalibrated models that may have been rushed to production for business reasons and likely require years more work to make them solid. 

Sportsbooks will try to defend themselves when offering these products by slapping a (relatively) large amount of hold on these markets. But this is like raising a buckler to a bazooka. Many of these in-game prop prices will be way off, and an extra few percent of hold ain’t about to save the day. 

Perhaps this sounds unduly harsh, and we concede we used colorful language in the preceding paragraphs partially for effect. But it’s important that you understand how much more complex a problem it is to generate all these prop bets in-game than it is just to offer a few main game-long markets. 

As a simple example, consider a situation where a football team is down by 12 points on their own 25‑yard line with 15 minutes remaining. You want to offer a bet on the outcome of this drive. And you aren’t content on offering a “Will this drive end in a score, yes or no?” prop. You want submarkets for every possibility. A rushing touchdown. A passing 

******ebook converter DEMO Watermarks******* 

touchdown. A field goal attempt. A punt. An interception. Loss of possession on downs. 

Think about that interception market for a moment (or turnover or however the product designers want to word the prop). Every NFL quarterback will give you a different answer. Some are very likely to throw an interception. Some very unlikely. 

These answers also depend greatly on how aggressively the team will be going for it in any fourth down situations. Every NFL head coach will also give you different answers. 

Now consider how much the lead affects those answers. If the team is down 10 points instead of 12, you also get very different answers. 

If you don’t mind your head exploding, now imagine having to extend all this logic to college football. 

Practically speaking, the models that content companies use to generate these markets are simply not up to the task of accounting for all the important variables. It’s legitimately very hard to do so in a consistent, relatively error-free way. 

And so they will put up bad lines and let you bet them. 

It’s worth a final note that the ends of games are the hardest to model. In football, whether and in exactly what situations a trailing team is likely to get a second possession after scoring on their current possession is a tricky problem. In basketball, how successfully and in which situations the trailing team will foul. In baseball, exactly how that reliever-batter matchup stacks up. If free bases will be granted by defensive indifference. And so on. In hockey, exactly when and in what situations a trailing team will tend to pull their goalie for an extra skater. 

These answers tend to be very team and player specific, and furthermore, small modeling errors can create large—sometimes absurd— line errors. Think about how much impact a team pulling a goalie 60 seconds earlier than expected would have on a hockey puck line or total. 

In football there are end game situations where a team has the ball in field goal range with an effectively insurmountable lead. Will this team run four downs and run out the clock? Will they kick a field goal on fourth down? Will they run their normal offense for a set and therefore potentially score a touchdown? Again there’s no one-size-fits-all answer here for a modeler to rely on. It’s purely—and severely—situational. 

******ebook converter DEMO Watermarks******* 

There was a Georgia-Tennessee football game a few years back where Georgia had the ball in this situation and a major sportsbook brand had the total priced such that it implied Georgia had over an 80 percent chance of scoring. Whereas we made it more like a 25 percent chance. 

That’s a particularly large line discrepancy, but modeling errors of this sort (the error being either the sportsbook brand’s or ours or both) occur very predictably toward the end of any game. 

In summary, in-play lines are made by models. There’s not much “market” for the content companies to tether their prices to besides early in the game and immediately after the second half begins. So the model operators basically just tether their pricings to the other models as best as they can. This clustering creates a modest “wisdom of the crowd” effect, but it’s not nearly as robust as the effect you’ll see in pregame markets. It’s easy to find situations where all the models have clustered together at a bad (i.e., very beatable) price. 

Furthermore, this price tethering really only applies to the main in-play markets. But there’s substantial industry pressure these days to offer in-play prop markets. Team and player props. Micromarkets. These markets will tend to be priced from just the raw model outputs. It’s incredibly difficult for model builders to account for all the important situational factors when pricing these markets. Therefore, they won’t. And, therefore, the published prices will often be extremely beatable. Finding the bad lines mostly requires a reasonable working understanding of the sport and then just paying attention. 

Furthermore yet, the in-play models are driven by in-play data feeds of game state information. The model prices will be only as good as the quality of the data that feeds them. All sports can have data inconsistencies and errors, but in particular you can expect college sports to have inconsistent data—and you can expect a wide range of qualities from game to game. So you might, for example, be watching a game and notice that line updates for that game are particularly slow and inconsistent. It’s reasonable to expect this poor data quality to persist throughout that game. 

Especially tune in late in games—roughly the fourth quarters of football and basketball games, the second half of the third period of hockey games, and the last couple innings of baseball games. Modeling the ends of games is particularly tricky, and it’s possible if not common to find modeling 

******ebook converter DEMO Watermarks******* 

errors of 20 percent or more in these situations. (E.g., Events with roughly estimated likelihoods of 60 percent or more priced at +150 or better.) 

The industry knows that offering in-play betting is a tricky business, but the people who work in the industry tend still to come from backgrounds where they are most used to offering soccer and tennis. While offering inplay soccer and tennis are tricky problems in their own rights, the American sports (particularly football and college sports) offer some significantly harder problems that, in our opinion at least, many in the industry have profoundly underestimated. 

From the content producer side, none of these problems is easy to fix, so it’s fair to expect in-play betting lines on the major American sports to be extremely beatable for years to come. 

******ebook converter DEMO Watermarks******* 

# CASHOUT 

Cashout is a popular feature with bettors, and it’s a major profit center for sportsbooks, so you can expect any modern sportsbook to try to offer it on as many bets as possible. 

The key idea with cashout is to understand that it’s just another bet. People think of it as “undoing” a bet. But that’s not what it is. Whenever you click that cashout button, you’ve simply made another new bet. 

For example, say in a Bears-Lions game that you’ve bet Bears ‑9.5 at ‑110 odds pregame for $110. The bet would return $210 to your wallet on a win and obviously $0 on a loss. 

During the game you look at the cashout quote for that bet and it’s $150. If you click that button, you have not undone your original bet. 

Instead, you’ve placed a new bet on Lions +9.5 for $60 at +150 odds. Let’s look at how this works. 

If Bears ‑9.5 covers, then the original bet returns $210, but the new cashout “bet” costs you $60, and you end up with $150 in your wallet. 

If Lions +9.5 covers, then the original bet returns $0, but the new cashout “bet” returns $150, and you end up with $150 in your wallet. 

Every cashout offer works this way. It’s designed to make you feel like you are “undoing” a bet or “taking money off the table,” but it’s more correct to think of it as placing yet another new bet. 

Why is this distinction important to understand? Because the cashout offers have added hold from the sportsbook just like any other bet they offer. Indeed, they usually have more hold than the standard market for the same bet. 

For example, if you were to look at the regular old betting menu at precisely the same time you see your cashout offer of $150, you might see these odds posted: 

Bears ‑9.5 ‑230 Lions +9.5 +170 

******ebook converter DEMO Watermarks******* 

If you click your cashout, you’re making a bet on Lions +9.5 +150, but just one tab over, the very same sportsbook is offering Lions +9.5 +170. 

“Okay,” you say, “So you’re telling me that cashout offers are a sucker’s bet then?” 

Often they are, yes. 

However, not necessarily. Let’s go back to the first sentence of this chapter. Cashout is a popular feature among bettors and a major profit center for sportsbooks (you now understand why this second part is true— it’s a way for the sportsbook to get their customers to make additional bets into betting lines with extra hold attached to them). Therefore, sportsbooks want to offer cashout as much as possible. 

That’s the key idea. There’s business pressure on sportsbooks to offer cashout on as many bets as possible and to offer it as much as possible—up to an ideal of 100 percent available cashout offers on 100 percent of bets pending on their platform. 

That means that when you place a Bears ‑9.5 bet, the sportsbook wants to offer you a price on Lions +9.5 at all times, from the moment you bet through the very end of the game. 

They want to offer _you_ a price on Lions +9.5, because they place a business emphasis on offering cashout options. But they might not, for various reasons, particularly want to offer anyone else a price on Lions +9.5. 

Consider a situation where the Lions are down by 16 points at the 50‑yard line near the beginning of the fourth quarter. If the Lions score a touchdown on this drive, will they go for two? If they go for two and fail, they’ll be down 10 points and poised not to cover +9.5. If they instead kick the extra point, they’ll be down by 9 points and therefore be likely to cover +9.5. 

The correct odds to offer on Lions +9.5 depend heavily on how likely the Lions coach is to go for two assuming they score a touchdown on this drive. And this can range, depending on who happens to be the Lions coach, from always to never. 

From a content company’s perspective, details like this one are maddening to try to keep track of and account for. Their solution likely would be simply not to offer the +9.5 line. They might offer +10.5 instead and mostly eliminate the impact of the two-point decision on the outcome. 

******ebook converter DEMO Watermarks******* 

But because you placed a bet on Bears ‑9.5 four days ago, and because the sportsbook _always_ wants to offer cashout, they may offer a price on Lions +9.5 to you (but not to the general public on their menu) as cashout. 

This price could be wildly wrong. Maybe you know that the Lions coach will never go for two, but the model has them priced as always going for two. So you know that the Lions will often lose by exactly 9 whereas the model thinks it’ll likely be either 10 or 8. 

Yeah, maybe the sportsbook is getting you for a couple extra percent of hold when you’re on the cashout tab versus on the main menu. But if the cashout tab is offering you a bet you can’t get on the menu, and that bet is particularly tricky for the content company to price, you can find opportunities in cashout that you can’t get elsewhere. 

(Cashing out a bet during the game like this has the added advantage of looking like a sucker play from the sportsbook’s perspective.) 

While sportsbooks feel business pressure to offer cashout as much as possible, you won’t always see cashout offers on all your bets. Sportsbooks and content companies understand the difficulties of offering cashout, and they restrict its availability to protect themselves. 

Similarly, you’ll often see limited (sometimes very limited) single game parlay menus and in-play betting menus. Again, these options are restricted because sportsbooks and content companies understand that these products are vulnerable to a bettor willing to put in the effort to pick them apart. 

But know that there are strong competitive and business pressures to offer more, more, more over time. If you’re in charge of product at BeaverBet, and you see your competitors over at BetBeaver advertising that they have universal cashout, then you immediately feel like you have to offer it also. 

That doesn’t mean that you just throw caution to the wind and flip the switch the next day to turn cashout on for everything. But you do prioritize “universal cashout” in your product roadmap, and in six months or a year maybe you find yourself rushing a beta version of it into your live product before all the kinks are worked out. Because you worry (probably correctly) that if you don’t keep up with your competitors products, you’ll bleed market share to them. 

The same logic goes for every product we’ve covered so far. Maybe your modern sportsbook doesn’t have it today, but there will be pressure to 

******ebook converter DEMO Watermarks******* 

add, add, add over time. The best time for a bettor to probe a betting market or product for vulnerabilities is when it’s just been added. 

We will end this section by outlining a tactic that we’ve not tried personally, but that should theoretically take advantage of an overly generous cashout. 

Say you find a sportsbook that genuinely does offer that otherwise elusive “universal cashout” product. Cashout any bet. Any time. 

Remember that cashing out is just making another bet. So any time you place a regular bet (i.e., not a cashout), you can think of making that bet as purchasing an option. Like a stock option. Placing the original bet gives you not just that bet (and whatever value it has), but it also grants you an option to make the corresponding cancelling bet at any time. 

You might never find a good opportunity to place the cancelling bet, and your option would expire worth zero. Or you might find a great spot to use it, and then option pays off. But either way, that option represents some non-zero bonus value to placing a bet in addition to whatever intrinsic value it has as a bet. 

For example, say you make a run of the mill NBA pregame bet of over 222.5 points in the Nets-Hawks game. You bet $110 to win $100. Assuming you have no (valid) opinion on which side of that bet is more likely to win, then you can expect to win half the time. Since you get $210 returned to you if you win, the bet is worth half of that, or $105. 

You paid $110 to place a bet now worth $105, so it cost you $5. But since this sportsbook lets you cashout your NBA totals bets at any point during the game, in addition to your $105 of value you get on the original bet, you also receive an option to place an under 222.5 bet. You can place this bet at any point during the game that you like. Or choose not to place it, if you never see a good bet. 

It’s entirely possible that this option, due to flaws in the pricing model the sportsbook uses for their cashout, will be worth more than the $5 you spent making the bet. And, therefore, that you can fire blindly into sharp, thoroughly price discovered pregame lines on major sports with the goal of making the losses back by intelligently exercising those cashout options when the pricing is bad. 

******ebook converter DEMO Watermarks******* 

# FUTURES 

Futures are the long-term bets with lots of options. Team to win the league championship. Team to win the pennant. Player to finish the season with the most home runs. Player to win the MVP award. 

In the old school Vegas days, books often hung futures menus preseason and then, once the season started, you rarely saw them offered again. Why? They’re a big pain in the ass for the book to keep track of. There are thirty different teams that can win the championship or a hundred different players who could win the Heisman. Every game played shifts these odds by small or very large amounts. The later you get into the season, the more wildly these odds move. One mid-game injury can completely change an entire single player futures market in a moment. Playoff pictures can shift dramatically on individual scores during late-season games. 

Also, the odds changing on any one team or player imply odds changes to all the other options, sometimes in subtle ways. The best team in the league can lose a game late in a season dropping them from a playoff one seed to a two seed. Perhaps this loss doesn’t affect that team’s championship chances much, but it might change the likely five seed’s odds a lot because of a change in a probable playoff matchup in the second round. If you’re the book, you have to keep track of all this stuff in realtime if you want to offer always-up futures markets. This was too much work for too little reward for the old school Vegas shops, so they didn’t do it. 

But little by little over the years, Vegas sportsbooks began to offer their futures menus during the season. Is it because these bets are a big money maker for the book, so they wanted to get them up more? 

Nope. 

But they’re amazing for marketing. Think of all the times you see sports betting in the news media. As often as not, those stories reference a big futures bet made or long odds offered as a key interest point in the story. “Meet Gold Chainz Galindo. He bet three million bones on the Sacramento 

******ebook converter DEMO Watermarks******* 

Kings to win the championship. And can you believe it? The Kings actually made the playoffs this year! Will Chainz win his bet? Only time will tell.” (Spoiler: No gold chainz for Galindo this season.) 

We barely watch English soccer, but we can tell you that Leicester City were offered at 5,000‑to‑1 at one point during the season they won the Premier League. We can’t remember which season that was, mind you. But we can tell you the odds offered. Because approximately five thousand to one news articles were written that season quoting those odds. 

To be clear, we aren’t knocking the betting journalists. They’re doing their job, and they tend to do it well. They’re just trying to do the impossible. Make us care about whether someone else’s sports bet wins. 

The point is that futures markets are still just as huge a pain in the ass for sportsbooks to offer today as they ever were. There are tons of options. The odds on any one option all depend on things that happen (good and bad) to the competing options. Casual bettors like to bet futures, but it’s not like the recreational money comes pouring in on NBA to-win-the-conference markets in early December. 

Futures markets are up all the time now at modern sportsbooks, and they’re there to provide easy talking points in advertising and the media as much as anything else. This fact also creates some competitive pressure for books to offer fairly good odds on these markets. Let’s say you’re a book and you want to play it safe in these markets. You might make a rule that you never offer longer than 100‑to‑1 odds on anything. 

Well, guess what. When that journalist comes around to write the story on Leicester City and asks you what odds you were offering at their lowest point of the season and you say 100‑to‑1, your sportsbook brand ain’t getting the shout out. The one that stuck their neck out and offered 5,000‑to‑1 (that exactly one person bet for exactly two pounds sterling) gets all the press. 

This phenomenon creates some incentive for the traders managing the odds in these markets to keep things reasonable. If they offer a few good prices then when a player or team draws media interest, they might happen to have the highest odds around and get some free publicity. 

Having the odds managed by traders is another key aspect of futures markets. Market making sportsbooks tend not to focus much on these types of bets. The more sophisticated betting groups tend not to bother themselves much with them either. The price discovery process that shapes 

******ebook converter DEMO Watermarks******* 

the worldwide pricing of major markets like point spreads and totals for individual games doesn’t work the same way on futures markets. 

Content provider companies will provide odds on futures markets as part of their larger offering, but there’s no particular “sharpness” to this pricing. No whizzbang algorithmic models are burning CPU cycles simulating hundreds of millions of college football seasons to determine who wins the Heisman trophy. It falls mainly to the trading teams at modern sportsbooks to maintain the odds on these markets. They do it the old-fashioned way— someone takes a guess, and then the traders move odds around as bets (and information like injuries or game results) come in to try to balance risk and avoid too much exposure on any given option. 

It's a whole lot of work to do it “right.” By “right,” we mean to maintain perfectly internally consistent sets of odds available on a 24/7 basis including even as games are being played. If the Orioles win ten games in a row, obviously their championship odds should go up (i.e., pay out shorter odds due to increased winning chances). The other American League teams should collectively see their odds decrease to compensate. But this decrease isn’t equally distributed. Certain AL East teams might see a lot of decrease. Teams in other divisions could also decrease—but it’s theoretically possible for some of these teams to see increased chances if, for example, the Orioles might displace an objectively better Rays or Blue Jays team in the playoffs. 

This is tricky, and it’s way more work on the sportsbook’s side than it’s worth to try to nail it. The upshot is that the pricing on these markets will be different (sometimes substantially so) from sportsbook to sportsbook, there is no trusted, centralized pricing, there’s sometimes a marketing-based incentive to keep the odds long, and no one is trying to make sure the pricing is “right” on these. 

Thus, there are almost always good bets somewhere among the options on any given futures offering. 

A quick story. A number of years ago, one of our friends specialized in picking off the futures markets all around Vegas. Recognizing the marketing value of keeping them up, most Vegas books by this time offered pennant and championship odds on all the MLB teams throughout the season. But as we explained above, trying to keep these markets updated with “correct” odds day-after-day was a lot of work. A given book might see just a couple bets on these markets in a normal day—with most of these 

******ebook converter DEMO Watermarks******* 

bets coming from tourists betting on their favorite team. The work-toreward ratio to keep these odds updated all the time was unfavorable. 

So sportsbooks didn’t. They’d update the odds maybe once a week. Our friend knew the update schedules and, a day before the update, he would drive around town picking off stale lines on any team that had gone on a winning streak over the past few days. 

By the end of the regular season, he’d have a shoebox full of tickets and already a guaranteed winner on most of the playoff teams. He’d hedge out the remaining risk by betting on the teams he didn’t have enough exposure <u>[10]</u> ~~.~~ to and lock in a profit 

This strategy would be somewhat less lucrative if tried today at modern sportsbooks than it was back then in Vegas. Modern sportsbooks have more resources—traders and software—to keep these markets up to date. But, on the flip side, they tend to use that extra bandwidth to put up more markets than the old Vegas books would. 

The basic principle behind this play still holds today and likely will hold well into the future. These markets are hard for sportsbooks to keep tight, and you should be able to build a nice, profitable portfolio of futures bets if you focus on these markets and look for the off numbers. 

The best approach to finding good bets in these markets is to build a simulator. If you have the basic programming skillset, it isn’t too difficult a task. You can infer the relative strength of all the teams from the pricing of the single game markets and then play out the remainder of the season. 

If you can do that, great. But this book is aimed more at answering the question “How can you find good bets with a bit of sports sense and then just by paying attention?” In that vein, you can price out your target market at a few different books that will accept your action. 

Say you’re looking at the NFL division winners markets. Record the price at a few books and then convert the odds to a break-even percentage for each option (e.g., +400 becomes 20 percent). Find the best price on each team among the various books you are using. Add up the break-even percentages—if they total less than 100 for the entire market, then you’re sure to have a good bet somewhere in there. If they total a bit more than 100, then it’s still fairly likely at least one of the options is good, since it’s hard to nail the pricing on these types of markets. 

Next step once you’ve identified a market with a likely good bet is to try to figure out which option (or options, plural) is the good one. Look for 

******ebook converter DEMO Watermarks******* 

outliers among the books. If most of the books have a team priced around 20 percent, but one book is at 12 percent, consider if that might be the good bet. 

Try to reverse engineer the discrepancy. Did something happen recently with that team? Could it be that most of the books have reacted to that information, but one perhaps is lagging in updating their odds? Maybe the team went on a winning streak recently. Or there was a meaningful trade or injury that would directly impact that team’s odds. 

If the market is good (i.e., the best price break-even percentages sum to just a bit more than 100 or lower), but none of the bets jump out as the likely good one using the preceding logic, then you can compare the pricing to parallel markets. In this case, parallel markets are different markets that have an obvious pricing correlation with the target market. 

If you’re looking at NFL division winner markets, then parallel markets would be conference and championship winner markets, as well as team by team “To make the playoffs, yes or no” markets. The pricing among all these parallel markets should have a shared logic. If you can find a price in your target market that is not compatible (and better, obviously) with pricing in these other markets, there’s a good chance that’s your bet. 

As an example, consider a hypothetical situation where you’re looking at two futures markets in MLB about halfway through the season: the National League pennant market and the MLB championship market. There are four large online sportsbooks in your jurisdiction. You copy the prices from all four sportsbooks for these two markets into a spreadsheet and you convert all the odds to break-even percentages. 

Using the best-available price on each team, you see that both markets have break-even percentages that sum to 99 percent. It’s a mathematical certainty that there’s at least one good bet in each of these markets. 

One team that pops out at you is the Pirates. One of the books has substantially better prices on the Pirates than the others do. The Pirates have also recently gone on a seven-game win streak. This is probably enough information by itself to justify a bet. But you go the next step and compare the prices between the two markets. The best-available championship price on the Pirates is +2400, a 4 percent break-even. And the best-available pennant price is +1900, a 5 percent break-even. 

These two prices are logically inconsistent—together they imply that 4 out of every 5 times that the Pirates win the pennant, they also win the 

******ebook converter DEMO Watermarks******* 

championship. Could the Pirates really be an 80 percent favorite over whichever team wins the AL? Of course not. 

So either the championship percentage is too high or the pennant percentage is too low. Because we’re already on the lookout for a percentage that’s too low (due to the low 99 percent sum for the entire market) it’s entirely reasonable to assume that 5 percent is probably too low and therefore to bet the Pirates to win the NL pennant at +1900. 

Since the championship market also adds up to 99 percent, there’s a good bet in that group as well, but it’s less likely that Pirates +2400 is a good bet—so keep looking. 

Individual player futures markets can often be extremely soft with some very good bets indeed sometimes to be found. These are markets like the player to win an end of season award (MVP, Cy Young, Heisman, Rookie of the Year, and so on). Or the player to lead the league in a certain stat (home runs, rushing yards, point scored, and so on). 

Remember that the posted odds in markets like these are essentially guesses from whichever employee from the trading team is assigned to maintain the market. Perhaps the prices are seeded by a content provider company, but in that case it’s an employee at the content company who is guessing. There’s no serious modeling work here, no market making, no “sharp money.” 

As a result, these markets tend to be full of errors. 

Sometimes the errors are systematic. A common systematic error is to underestimate how much variance there is in any individual player’s future performance. For example, if an NBA team is in first place about two thirds of the way through the season, it’s quite unlikely that the team will tank the remainder of the season so badly that it misses the playoffs. Even if a star player gets injured, other players on the team can typically step in to get the team to the next stage. 

Whereas the obvious frontrunner for MVP or most home runs or rushing yards or what have you can get injured at any moment and—poof—their chances to win are instantly gone. This is no brilliant insight of course, and the people who make the odds surely know this as well. Nevertheless, it seems a human bias often steps in here and you’ll see frontrunners for these individual awards sometimes offered at too short odds while “dark horse,” but still quite viable, candidates are sometimes offered at extremely good odds like 50‑to‑1 or better. 

******ebook converter DEMO Watermarks******* 

The MLB Rookie of the Year award earns special mention here. Major League Baseball is unique among the major American sports leagues with its extremely deep minor league system and convoluted roster and unionnegotiated service time rules. The most talented rookie players often break camp playing in the minors and can stay down through April and sometimes well into May. 

Because this is so common in baseball, the writers who vote on the award at the end of the season often will not hold this time not yet in the league against a candidate. A strong June through September can be enough to win the ROY award. 

But the oddsmakers do not necessarily know the ins and outs of all the MLB farm systems, and they often list rookie players not yet in the league at very long odds (like 100‑to‑1 or higher). Occasionally they’ll price a blue chip, marquee prospect this way. This is a player who is breaking camp in the minors often only for some procedural reason, and who is nearly guaranteed to be promoted to the Majors relatively early in the season. 

It's not too uncommon to see a player like this available for 75‑to‑1 a couple weeks prior to his promotion, but priced at 7‑to‑1 a couple weeks afterwards. Every MLB season, it’s worth learning a few names that fit this profile and checking the prices on these players until they get promoted. 

******ebook converter DEMO Watermarks******* 

# DISPELLING A FEW BETTING MYTHS 

Two things are true. The overwhelming majority of sports bettors lose. The sportsbooks those bettors bet at and lose to offer hundreds if not thousands of good (for the bettor) bets every day. 

Somehow people manage to lose despite being showered every day with good betting opportunities. 

Why is this? It’s because most people have absolutely no idea what they’re doing. Perhaps worse than that, a good portion of them think they do know what they’re doing. They aren’t just throwing down a $5 parlay every so often to make watching the game more fun. They have a whole strategy. They’re fading public sides and grabbing better odds live and locking in middles and hedging and yada, yada, yada. 

They’re sure all this makes sense. Never mind that at the end of the month they’re depositing rather than withdrawing, just like they do every other month. Chronically unlucky, perhaps. 

The goal of this section is to keep you out of that trap. Good bets are everywhere at a modern sportsbook. Yes, it’s very difficult to beat modern sportsbooks out of a lot of money (for reasons we will cover shortly). But please, for heaven’s sake, don’t lose. No, they won’t let you win a ton. Yes, they’ll limit your accounts. But, like, don’t actually lose to them, okay? 

You win at betting by making winning bets 

This one is so simple and yet also apparently counterintuitive to people. Any bet has an expected win or loss associated with it. If you bet $110 on a coin flip at ‑110 odds, your expected loss is $5 (as calculated in an earlier chapter). 

******ebook converter DEMO Watermarks******* 

That’s a losing bet. It loses $5 for every $110 you place on it. 

There is no way to sequence those coin flips, to manage your bankroll, to create middles or hedges or cashouts or buy backs or any such thing to turn that bet into one that will win you money over time. It’s a bad bet. It costs you money every time you make it. It loses. 

If you bet $100 on a coin flip at +110 odds, your expected win is $5 (calculated the same way—it pays $210 if you win and you win half the time, so it’s worth $105 on average while you paid only $100 for it). 

That’s a winning bet. It wins $5 for every $100 you place on it. 

The moment you click “Bet,” it’s done. You’ve earned $5 by making the good bet. Or you’ve spent $5 making the bad bet. You win at betting by clicking Bet on good bets that make you money and by not clicking Bet on bad bets that cost you money. 

Full stop. 

Yes, obviously there’s risk involved. Good bets can lose and bad bets can win. But this is what trips people up and gets them thinking that they should start clicking Bet on bad bets. Because they start to think that other things matter besides—in fact are more important than—clicking Bet on good bets and not clicking Bet on bad bets. 

But we absolutely promise you that clicking Bet on good bets and not clicking Bet on bad bets is by far the most important skill you can have to win at gambling. It trumps everything by a lot. Any time you hear someone use the word “bankroll,” you’re in the danger zone. 

Yes, it’s possible to go broke by overbetting a bankroll on good bets. 

But it’s only possible to do that if you first make good bets. If you go broke by betting your bankroll on bad bets, then you did not go broke because you overbet your bankroll. You went broke because you suck at gambling. 

Most people who make bets because they’re worried about their bankroll are making bad bets as a result. They’re no longer making good bets and avoiding bad bets. They’re intentionally making bad bets. Because “bankroll.” 

#### This is not the way. 

Cashout is the perfect example of how this psychological trick works. It’s just another bet. If you click “Cashout” you’ve made a bet. Maybe it’s a good bet. Maybe it’s a bad bet. (If you haven’t done the work to determine that it’s a good bet, then let’s go with bad.) 

******ebook converter DEMO Watermarks******* 

But it’s a bet, just like any other bet. The sportsbook certainly looks at cashouts like they do any other bet. They calculate a betting volume and a hold percentage on cashouts same as they do any other bet type. (And those volumes and hold percentages tend to look very good to the sportsbook, which is why they love offering you cashouts.) 

If you are about to click “Bet,” picture us sitting on your shoulder asking, “Why are you making this bet?” 

If your answer involves a reference to any previous bet you’ve made— GAME SHOW BUZZER. Here comes the whammy. 

“Well, I bet +4.5 pregame and now this is a middle…”—SIRENS FLASHING. 

“Well, I’ve got a future bet on…”—THOSE ANNOYING SOUNDS CAR ALARMS MAKE THAT EVERYONE JUST IGNORES. 

The only good answer is, “I believe this is a good bet that offers a positive expected value.” 

If you get good at identifying those, and if you stick to only clicking Bet on those bets, then you will win. Then—and only then—you can start thinking in terms of “risk management.” 

### Your vibes ain’t beating price discovered pregame markets 

A lot of people claim they can beat major pregame markets in major American sports. NFL, NBA, or MLB full game or first half sides or totals. They can’t. You can’t. If you think you can, you’re deluding yourself. 

We aren’t saying that it’s impossible to do. It’s kind of like bench pressing 315 pounds. It’s well within the bounds of possible human achievement. 

But it also requires years of systematic work and preparation. If you’ve never set foot in a gym before and you walk up to a bench and throw on three plates and think you’re about to press it. Hard no. We’d guess that’s a no for almost every human in the world. 

And even with years of systematic work and preparation, most people still fall short of 315. Yes, it’s possible. You just have to be naturally gifted and also willing to work your ass off for it. 

******ebook converter DEMO Watermarks******* 

You also know if you’re close. Like if you’ve already benched 295, then you’re a reasonable person if you think you can stretch that to 315. If you’ve never even benched the bar before—stop clowning yourself. 

There’s something about gambling that gives people a ridiculously outsized sense of their own capabilities. We’ve known people who just started playing poker who were convinced—absolutely convinced—they could study for a few months and become one of the best players in the world. 

Poker is a wildly complex strategic and mathematical game on par with chess. The actual best players study all day every day and have done for years. 

Can a smart person learn to beat their local low-limit poker game within a few months? Of course. Can you learn to identify and pick off soft sports betting lines at a modern sportsbook within a few months? If we didn’t think so, we wouldn’t have written this book. Absolutely we think you can. 

But at any given moment, the major market sides and totals for major American sports represent the collective wisdom of a bunch of smart people, many of whom work all day every day to beat these lines and have done for years. Whatever angle you think you have, you don’t. 

Fading public betting (we debunk that one in _Logic_ ), favorite/underdog bias, travel, motivation, applying Sabermetrics in baseball (sorry, but everyone knows about Fangraphs), matchups, weather for totals, we’re trying to think of more here. The point is none of it will get you an edge. 

This isn’t to say that these things don’t matter. They absolutely do. Obviously the weather matters for totals. Travel and motivation matter. Even public betting patterns sometimes matter. 

The problem is that the smart people who shape the price discovery process also know they matter. At least some of the smart people do— enough of them that the collective part of collective wisdom kicks in and makes it very hard to find an edge on any of these factors alone. 

It’s not enough to know that motivation factors favor one team over another in a specific game. You don’t know if the line already accounts for those factors. The only way to know that (well to make an educated guess at that—you never _know_ anything) is to maintain a complex statistical model that handicaps all the relevant factors and then to use that model to tease out and quantify specifically the motivation factor. 

******ebook converter DEMO Watermarks******* 

The bottom line is trying to beat these markets is among the hardest things to do in sports betting. If you don’t already have a long, strong track record of success doing the easier things—just trust us, you can’t do this one. Maybe one day. But build up to it and don’t delude yourself. 

### Your vibes ain’t beating the easy-tomodel modeled markets 

We’ve just spent the first half of the book explaining how difficult it is for content companies to produce all these lines that modern sportsbooks offer. The single game parlays and the in-play lines and the cashout lines and the in-game props and micromarkets. 

It is difficult. Think about the problem from the sportsbook’s perspective. During the course of a single game, they’re expected to post thousands of different in-play lines for their customers to bet. And they’re expected to estimate the probability of the events underlying each of those thousands of lines to within about five percent each. 

And never be wrong. 

And do it with game state data that’s sometimes slow, inconsistent, or error-prone. And cover every possible wacky situation that can happen during a sporting event. And get new lines up within seconds of major game-changing events. 

It’s just hard. Content companies will make mistakes. Sportsbooks will copy these mistakes and offer them to customers. As the bettor, your job is just to sit back, watch the game, and wait for someone trying to do something extremely difficult to screw up. 

But just because mistakes are quite common doesn’t mean every line is bad. Most of the lines aren’t bad. That is, most of the lines correctly estimate the underlying probability of the event to within five percent and therefore offer no good bets to the bettor. 

It’s common for people to think they can pick off the poorly modeled lines purely with intuition. “You’re telling me the Chiefs score two TDs in the first quarter and now the full game line is still just ‑16.5?” 

Yup. That’s what they’re telling you. And they’re almost certainly right. Because that’s an easy one to model. It’s still early in the game, so the information from the pregame markets hasn’t gotten stale yet. And this is a 

******ebook converter DEMO Watermarks******* 

common game situation, so there’s plenty of data from which to build a model. So yeah, the people with the computer science degrees and the mountains of data and the ability to harness modern computing power in real time probably got this one. Maybe your vibes are off. 

What’s easy to model then? Longer-term (i.e., full game) team-based markets mostly, especially in games where nothing particularly out of the ordinary has happened yet. That ‑16.5 point spread after a couple quick Patrick Mahomes TD passes. This is just a normal beginning to a Chiefs game. 

Game moneylines and totals in the first few innings of a baseball game where the starters are still in. Team-based props in these games like team strikeouts or home runs. “Race to” markets in basketball when the number they’re racing to isn’t too close yet for either team. 

Also any game rules-based prop, especially when it’s longer term. Like “Will the game go to overtime?” while it’s still the first half. This stuff is mostly either just math or relatively simple combinations of pregame market information and math. 

Anything short term will generally be harder to model. “What is the outcome of this at bat?” in baseball. Hard, because the answer depends on the idiosyncrasies of a specific pitcher, a specific batter, and how those idiosyncrasies interact. Sportsbooks will place a lot of hold on a market like this to compensate for the modeling difficulty, but that doesn’t change that this is a hard modeling problem. 

“Current drive outcome” in football is another one that’s tricky. Everything also gets trickier the more situational factors matter. Current drive outcome is much easier to model when it’s halfway through the first quarter versus at the beginning of the fourth quarter. 

Full game spreads, moneylines, and totals get harder to model (and therefore easier to beat) in the second half of games. This is when situational factors begin to predominate. Will the coach go for it on close fourth down decisions? Will they let the position player pitch? Will the coach call for fouling down ten at the end of a basketball game? When will they pull the goalie? The more this situational stuff looms large, the harder a time anyone making lines will have of modeling the situation well. 

There are indeed plenty of in-game lines you can beat with your intuition alone. But before you pull the trigger on those, think about how 

******ebook converter DEMO Watermarks******* 

easy or hard the modeling problem is likely to be. If you try to beat someone else’s easy math problem with your intuition, you’re going to lose. 

******ebook converter DEMO Watermarks******* 

# LONGEVITY 

Modern sportsbooks don’t want winning customers. This is almost <u>[11]</u> ~~.~~ universally true 

If a modern sportsbook allows you to bet with them, it’s because they have not yet identified you as a winning customer. All modern sportsbooks have a player profiling system, and all of them attempt to identify and restrict or exclude winning customers. 

There is substantial variation among them in exactly how they identify winning customers, where they set the bar as to when a winning customer becomes undesirable, and how harshly they will restrict you once they’ve so identified you. But they all profile, identify, and restrict. 

This practice rubs many people the wrong way, and with good reason. “If I can beat you fair and square, then I should be allowed to,” is roughly the reasoning. We are sympathetic. 

But look at it from the other side. It’s impossible within the constraints of contemporary technology to offer the extensive betting menus these sportsbooks offer without listing many beatable bets. The modeling problem is way, way too difficult to get everything right all the time. 

Also consider that if there were no constraints on a winning bettor, a single bettor starting from as little as a $10 deposit could use the power of exponential growth to beat a given sportsbook out of millions of dollars within a relatively short period of time. 

And as soon as it became clear to people that it was possible to turn $10 into a million or more this way, more people would try. The winning bettors would quickly bankrupt a modern sportsbook of any size. 

There are two options to avoid this problem. Option 1, restrict your betting menu only to those markets for which you have enough liquidity to offer an actual “market” with buyers and sellers, and rely on the magic of price discovery to protect you. This is the option market making sportsbooks have chosen. 

******ebook converter DEMO Watermarks******* 

Option 2, you go ahead and offer the big betting menu and toss anyone who shows the ability to beat you. That’s the modern sportsbook. 

You don’t have to like it, but if you create an account with a modern sportsbook, know that those are the rules of the game. You’ll be allowed to play until they figure out you’re beating them, and then it’s over. 

So how do you stay in action the longest? 

Well, back up a little bit. Think about what your goals are. Why are you reading this book? What are you trying to accomplish? Are you just trying to pick up a bit of free money on offer? Are you trying to place the most bets because you have fun betting? Are you trying to keep your account unrestricted as long as possible? Are you trying to maximize your lifetime winnings at the sportsbook? 

We can’t answer these questions for you, but do think about them, as your goals will inform your choices, behaviors, and strategies. 

All modern sportsbooks profile, identify, and restrict. But their approaches to it vary and, for the most part, in ways that make sense if you understand their business incentives. 

Let’s say you’re in a state that has twenty licensed modern sportsbook brands operating. The classic Pareto principle (80/20 rule) applies to this situation. You’ll see 80 percent of the market share go to 20 percent of the brands. (Sometimes it’s even more extreme than this.) You can divide the 20 sportsbook brands operating in your state roughly into a “top 4” and a “bottom 16.” The business incentives are quite different between these two groups. 

Simply put, none of the bottom 16 brands does a whole lot of business. They don’t have many customers. They don’t do much betting volume. They don’t win very much off of the bets they do get. 

Yet all 16 of these companies decided it was worth the considerable investment to cobble together a modern sportsbook technology stack, pay the typically quite significant fees to get licensed in your state, and hire a number of employees to operate the business. If they aren’t doing much betting business, why did they invest so much? 

That answer will vary from brand to brand. It could be because the company owns (or is developing) some unique piece of the sports betting technology stack and they want a “shop window” to demo it to the industry. 

It could be because there’s a mega brand behind the sportsbook, and they’re testing the waters to see how the general brand value converts to the 

******ebook converter DEMO Watermarks******* 

sports betting business. 

It could be a regulatory capture play. They’re acquiring licenses or other exclusive agreements in jurisdictions where these relationships are scarce or hard to acquire with the general hope of flipping these licenses or relationships in the future for a profit. 

It could be a little of all three. Or something else. Regardless, the amount of cash flow generated (or not generated) by the betting business contributes only a small amount to the overall valuation of the venture. And it’s not the yardstick by which anyone involved will judge the success or failure of the venture. 

In other words, it ain’t the day-to-day betting revenue that’s keeping these brands going. And that’s good because there ain’t much of it. 

If you’re running one of these “bottom 16” brands, think about the risk profile on a new betting customer signup. Maybe it’s a “desirable” recreational customer, who can be expected to lose a few bucks a month, contributing roughly jack and squat to the overall top line valuation. 

Or maybe it’s an “undesirable” customer, who is a risk to take millions of dollars off the bottom line if their activities aren’t nipped in the bud. 

This high risk/low reward new customer dynamic tends to make these “bottom 16” brands extremely risk averse with their customer profiling. You breathe wrong on their platform, and they’ll restrict you. 

You might think it’s an overreaction. After all, “desirable” recreational customers far, far outnumber the winning “undesirables.” 

Yup, that’s true. For the top 4 that is. 

It’s decidedly not true for the bottom 16. Most recreational customers open accounts at just one or two sportsbooks. If a recreational customer has just one or two accounts, it will almost always be at one of the top 4. That’s the defining characteristic that differentiates the top 4 sportsbooks from the bottom 16 sportsbooks. The top 4 are where recreational people open accounts and play. 

On the other hand, consider someone who opens an account at every single one of the 20 sportsbook brands in your state. What do you think that person is likely up to? 

If you answered, “They’re trying to scoop up as much bonus money as possible and then win what they can until they get kicked out,” you win the prize. Which is nothing. You win nothing. 

******ebook converter DEMO Watermarks******* 

If you’re looking at new signups at the top sportsbook in your state, for every 100 signups, maybe 99 are “desirable” recreational customers who intend to play the game as designed, while one is there to try to take the sportsbook’s money. If you’re looking at new signups at the 13<sup>th</sup> ranked sportsbook in your state, for every 100 signups, it could be that 50 or more are there to try to milk the bonus offer and then win a few more bucks out of the place before they get shut down. 

We made those numbers up, but you get the picture. “Undesirable” customers trying to win the money is in no way a small problem for bottom 16 sportsbooks. It’s almost the rule rather than the exception for these brands. 

These brands are restricting people left and right because they rightly perceive every new signup as a potential threat, and they also don’t rely on (short term) betting revenue to derive their corporate value. If you smell even slightly funny, you’re out. It is what it is. 

Top 4 brands have different incentives. Their betting business is significant, and the revenue they derive from it has a more direct impact on their corporate value. If they grow their customer base or if they change in some way to derive more revenue from their existing customer base, the value of their company is likely to improve. 

Most of their customers are the desirable recreational customers, and they want to keep those customers happy and make it as easy as possible for them to bet. 

“Undesirable” customers are still potentially a major threat to their bottom line, but these brands have to walk a fine line. They want to make it <u>[12]</u> ~~.~~ hard for the “undesirables” to bet, but easy for everyone else 

Top 4 sportsbooks also want to court high rolling so-called VIP customers. For the most part, bottom 16 sportsbooks don’t make much attempt to accommodate this sort of business. They would (again correctly) be on high alert that this customer relationship would turn sour for them. 

We’ve personally seen genuine, well-known-to-be VIP customers severely limited at bottom 16 brands. Not advantage bettors—genuine whales. Why would anyone turn away a dream customer like this? 

Variance. Perhaps ironically, many small sportsbook brands simply can’t stomach the swings that even a single fairly high roller bettor can put them through. 

******ebook converter DEMO Watermarks******* 

Imagine being the CEO of one of these brands, it’s 1am on a Sunday morning, and you’re glued to the TV praying some college kid slips as he tries to kick the game-winning field goal for his Rainbow Warriors. Because if he makes it, your one-and-only genuine VIP customer will win a multimillion dollar parlay, which will throw your entire quarter’s betting revenues into the red and may scuttle the eight-figure acquisition deal you’ve been working on for months. Many small brands want to avoid this scenario entirely. 

Bottom line, while smaller brands often have other business incentives, top 4 sportsbooks want their customers to be able to bet, and they want where appropriate for their wealthy customers to be able to bet big. They also want to identify and restrict customers who beat them. But it’s not always easy for them to identify when they’re getting beaten. 

### Profiling Basics 

Sportsbooks are notorious for restricting bettors after just a small handful of bets. “What the heck happened? I just made two bets and—BAM—all my limits were whacked down to pennies! How could they possibly have decided they didn’t want my action so fast?” 

Sportsbooks put a lot of resources into their player profiling. Even if there were no such thing as advantage gamblers, they’d still have to do this because of the existence of the other classes of undesirable customers. Failing to exclude any of the other classes of undesirable customers can land a sportsbook in very substantial political or legal jeopardy. 

As a result, sportsbooks (especially top 4 brands that get lots of new customers) are pretty good at getting a read on a new customer quickly. They use not just your betting history to make decisions about you, but also the personal and financial information you share with them when you open your account. (This usage is subject to privacy regulations that vary by jurisdiction.) 

Think about how much you can often deduce about a stranger even if you’ve never spoken a word to them. Just by how they dress, how they carry themselves, how they groom themselves, who they are associating with, and so on. And then on the first word, their accent, how they greet you, their body language, and so on. 

******ebook converter DEMO Watermarks******* 

Now think about what one might conclude about you (rightly or wrongly) from the following information. Your age. Your gender. Where you live. Your name (particularly if it’s identifiable with a particular nationality or ethic group). Where you bank. What operating system you used to create your account. (Did you open your account from a Chromiumbased browser on Ubuntu Linux? Nerd.) How you arrived at their website to create your account. The size of your initial deposit. 

Sportsbooks collect and analyze this sort of information. In fact, they’re often required to do so by law to comply with anti-financial crime and antimoney laundering regulations. Especially if you want to play for significant money, they’re required to verify your source of funds (i.e., that you indeed have the money you are planning to gamble and that you acquired that money through legally compliant affairs). They’re also required to “know their customer.” The days of bringing a duffle bag of cash into a casino and throwing on a cowboy hat and a fake moustache and pretending to be oil money are long over. If you want to bet, they’re gonna know all about your (actual) business whether you want them to or not. 

The most common question people ask about profiling is, “Is it possible to fly under the radar by betting small?” 

Yes and no. It’s certainly true that individual customers who deposit and bet small will get less scrutiny than an individual high roller. But small bettors as a group are being profiled more than perhaps they suspect. At a bottom 16 sportsbook, there simply aren’t that many customers, and there’s not really any such thing as flying under the radar. If you win at all, your account will appear on winners lists that humans will review. Appear often enough, and you can expect your play to be investigated. 

At a top 4 sportsbook, there may be too many winners to make it practical to compile lists for manual review. But these brands often have automated profiling systems that will classify you based on your betting patterns. You can be flagged for review fairly easily, especially if you bet like a typical “undesirable.” (More on this in a bit.) 

The other thing betting small does is it puts you, by definition, in the low roller category. Once you’ve established yourself as a small bettor, you’re very likely to get flagged if you start depositing or betting much larger amounts than your established behavior. This flagging is likely required by regulation, and your larger deposits may trigger know-your-customer and source-of-funds checks. 

******ebook converter DEMO Watermarks******* 

Modern sportsbooks view their business as selling an entertainment product. From their viewpoint, you as the bettor are receiving an entertainment experience from them, and you are paying for that experience with the losses on your bets. 

This viewpoint is distinctly at odds with how many would-be winning bettors see sports betting. Some bettors might instead see sports betting as a game of skill—where the goal is to use your wits to try to gain an advantage over your opponent, the sportsbook. Or they see it as a trading game, the “sports betting as toy stock market” paradigm. Where your goal as the bettor is to buy low on undervalued bets and sell high on overvalued ones. 

You will find that modern sportsbooks are not at all sympathetic with the latter two conceptions of sports betting. To them, the sportsbook offers an entertainment product, full stop. And any bettor who tries to engage with their product from any other angle is potentially abusing their offering. 

Perhaps this view from the sportsbook doesn’t surprise you, but what may surprise you is that most other industry-associated people hold this view as well. This includes people like sports league executives, legislators, and, of particular note, gaming regulators. 

So, theoretically speaking, say you were to find some systematic pricing error on a modern sportsbook’s betting menu, and you were to exploit said error. And then you were to get into a dispute with said modern sportsbook after they caught on to your angle, and they didn’t want to pay you. And you decided you would escalate said dispute to the state gaming regulatory board—you should not necessarily assume that the regulator will be sympathetic to your view of things. The regulator may well view your betting behavior as “abusive” because it does not fit the “sports betting as entertainment product” paradigm. 

If you want to make the most from your interactions with modern sportsbooks, it’s best to do so as much as possible on their terms. Entering into direct conflict with them is unlikely to turn out the way you want it to. 

They want to offer an entertainment product, so you should behave as if you are buying an entertainment product from them. Act like a recreational gambler in all ways except one—don’t make the losing bets. 

### How Do Recreational Gamblers Behave? 

******ebook converter DEMO Watermarks******* 

I (Ed) have been writing gambling books for twenty years now, and over that time I’ve come to know hundreds of readers personally. I feel like I have a reasonably good read on what types of people tend to read my books. For the most part, my readers are smart. (Allow me, dear reader, to flatter you for a moment.) My readers are analytical. My readers are also looking for an edge. They’re looking to do whatever it is they do a little better than the next person. 

My readers also have a tendency to be risk-averse. 

My readers are exactly the types of people to look at sports betting not as entertainment, but instead as a game of skill or a little mini financial market. They look at it as a challenge to be conquered. 

My readers are the type of people who will read all the fine print on a specific bet type or promotion and then happily fire off an email to sportsbook customer service quoting paragraph 3 subparagraph H to some hapless customer service agent when the expected bonus payout is not quite correctly awarded. 

In other words, dear reader, you ain’t a recreational gambler. You don’t smell like one. You don’t look like one. You don’t behave like one. You stick out like a sore thumb. 

If you want longevity at modern sportsbooks, you may have to unlearn some of your natural behaviors and learn some new ones. Again, the goal is to behave exactly like a recreational gambler in all ways except one—don’t make the losing bets. 

So how do recreational gamblers behave? 

They gamble. They aren’t trying to arbitrage everything or hedge away all their risk. For example, they do not bet both sides of the same game in order to satisfy some bonus’s betting requirements without putting any money as risk. They’re on the sportsbook in the first place so they can feel that rush of putting money at risk. 

Yes, they love cashout, but only after they have a nice win (or freeroll) to “lock in.” They are less likely to cashout a losing bet or lock in a negative freeroll. For example, say they bet a parlay for $100 to win $2,000. They might cash it out at $500, but they’d be unlikely to cash it out at $20. They want the feeling of having won more than the avoidance of risk. 

They don’t min-max things. If they have to bet $1,000 to earn out a bonus, they don’t bet exactly $1,000 and not one penny more. They don’t find the mathematically optimal thing to bet that $1,000 on to meet the 

******ebook converter DEMO Watermarks******* 

withdrawal requirements. Yes, they take advantage of bonuses and promotions. But they do not optimize. 

They use “human” bet sizes. They don’t size down to the penny based on mathematical formulas like Kelly fractions or arbitrage calculators. 

They don’t “nurse” their deposits. If they deposit money in a sportsbook, it’s with the expectation that they will bet it. For example, they aren’t depositing $1,000 and then making $10 their “betting unit.” They’re betting in a way such that a modest bad run will bust the account. 

They bet on things to happen, not against things happening. Steph Curry points prop? Over. Patrick Mahomes passing yards? Over. Tiger Woods to win the Masters at age 63? Sure, put me down for $100. 

They like betting favorites, but they hate laying big money. Bet Duke at ‑1400 to beat Richmond? Nah. But parlay that with a few other big favorites to get the odds down close to even? Yup, let’s do that. 

The main point here is that there are so many good bets on offer at modern sportsbooks, you don’t have to behave like a value-seeking robot to get the money. Being “contrarian” is not the right idea. Robot behaviors will sooner or later get you flagged and limited. 

### VIP Programs 

Perhaps the most famous form of advantage gambling is card counting in blackjack. Introduced to the public in the 1962 book _Beat The Dealer_ by Edward Thorp, this method allows the player to beat the game not by cheating but with some clever observations about the math of the game itself. 

Indeed, card counting works. But the reason we gamblers aren’t all billionaires by now at the casino’s expense is because it also has a fatal flaw. Card counting requires the player to vary their bet sizes, sometimes quite dramatically depending on the specific rules of the game. The advantage comes from betting larger amounts when the odds are in the player’s favor and small amounts when the odds are against the player. Make good bets. Avoid bad bets. 

These ever-present bet size fluctuations are the telltale signature that betrays the card counter to any well-informed casino employee. A card 

******ebook converter DEMO Watermarks******* 

counter is always playing on borrowed time—eventually a pit boss will figure out the play and kick them out. 

There is another form of advantage gambling that’s less well known, but arguably has produced the biggest advantage gambling scores over the past few decades. Not only has it produced some eye-popping short-term wins, but it’s also allowed some gamblers to win consistently over very long periods of time. 

This involves manipulation of the VIP programs offered by casinos. Obviously, every casino will have a slightly different way they run their VIP programs, but the general idea is fairly universal and has remained the same for many years. The casino watches your gambling action and attempts to quantify how much they expect to have won from you based on your play (called your theoretical loss or “theo” for short). They then set aside some fraction of your theo and return that money to you in various ways. Food and drink. Event tickets. Gifts. Travel. Free play. Straight cash back. And so on. 

At lower levels of play, the casino has a set program usually divided into tiers, and you get whatever the casino offers for the tier that you’ve qualified for. 

At higher levels, you get assigned a person, called a host, whose job it is to keep you happy and coming back for more. You have a personal relationship with this host, and you can ask for things. The host is still bound by the general rules of the relationship (i.e., you are only to be returned a fraction of what the casino thinks you should have lost to them), but this two-way host relationship gives the savvy advantage gambler more opportunities to get what they want from the VIP program. 

In 1994, advantage gambler Max Rubin published a book called _Comp City_ which fleshed out the general idea. You use various tricks when you gamble to encourage the casino to vastly overestimate your theoretical loss. Then you ask for the maximum amount in return for your theo. If you’ve done it correctly, you end up getting more back from the casino in perks than you’ve lost to them from your actual gambling. 

Thirty years ago, when the book was published, it was much easier to get one over on casinos. Among the tricks Rubin suggests are things like making large bets when the pit boss is watching and then making small bets when the boss isn’t watching. Playing craps and making extreme use of the “odds” bet. (The “odds” bet in craps is a genuinely break-even bet that you 

******ebook converter DEMO Watermarks******* 

are permitted to make after first making a smaller bet that has the typical house advantage.) 

The result of all this chicanery would have been that the casino might have you rated as betting $10,000 per hour at a three percent house edge (for a $300 per hour expected loss to the casino) when in reality you are betting only $3,000 per hour at a one percent house advantage (for an actual $30 per hour expected loss to the casino). If you can then convince the casino to pay you back more than ten percent of your theoretical loss in freebies, you come out ahead. 

Not only do you come out ahead, but at the end of your trip the casino is practically begging you to return for your next trip when you leave. Maybe you can use that enthusiasm to score some free travel, food, drink, and hotel rooms from your host as an enticement for you to come back and beat them all over again. 

Unfortunately, this doesn’t work as well anymore. Thirty years ago, the casinos relied on their pit bosses to observe you and determine how much you were betting. Today, computers do the job. The computers are much better at estimating your theoretical losses at games like blackjack and craps <u>[13]</u> ~~.~~ than the overworked casino employees were back in the old days 

In sports betting, however, it’s impossible for anyone to know your actual theoretical loss on any given bet. But modern sportsbooks often pretend that they know the “true probabilities” of every bet on their menus, and they then go on to do the same theo math on their customers to estimate theoretical losses for, among other things, their marketing and VIP programs. Perhaps you already see where this is headed. 

In general, a sportsbook will consider your theoretical loss on a bet to be proportional to the hold they apply to a market. On a simple point spread bet, if you bet $1,100 at -110 on a point spread, then after two bets you would have bet $2,200 and on average you would have won one of them for a $2,100 return. The sportsbook rates this as a $100 theoretical loss over two bets or a $50 loss per $1,100 bet. 

The sportsbook may modify this rating using a concept called “closing line value” or CLV. Say instead of betting your point spread bet at -110 you bet it at even money (with the other side of the bet therefore listed at -120). After you bet, the prices then move, and when the game goes off the sportsbook has the market listed at -110 on either side. According to the “true probability” theory of sports betting, the closing line suggests that the 

******ebook converter DEMO Watermarks******* 

true odds of winning your bet are 50 percent. Since you made your bet at even money and you have a 50 percent chance to win, your theoretical loss is not $50 but zero. 

Sportsbooks will sometimes use this CLV calculation not just to adjust your theoretical loss, but to decide whether they want you as a customer at all. If you consistently get CLV on your bets, the book may conclude that you’re trying to win and restrict your account. 

This CLV calculation can’t really be done on many sorts of bets that a modern sportsbook offers, however. It relies on comparing the price you got on a bet versus the price they offered on the exact same bet at a (substantially) later time. So, for example, any in-game bet you make can’t really have CLV calculated for it, as the moment a new event happens in the game, they no longer offer the same bet. Trying to calculate CLV on single game parlay bets would also often become absurd. 

Having said all this, top 4 sportsbooks must compete with one another for the relatively small pool of high roller customers. They have substantial business incentives to be accommodating to VIP players. If you don’t shove it in their faces that you’re beating them, you’ll find they may give you a lot of leeway to bet with them and rack up the theo. 

As of the time of this writing, here are the sorts of perks available when participating in a representative VIP program. 

Personalized host service. A host is a customer service sportsbook employee whose job it is to be in regular contact with you and basically find out what you want. This is similar to how it works at an old school brick and mortar casino. You can ask the host for all sorts of things. A deposit bonus should you bust your account. Tickets to sporting events. Free entries to contests like survivor pools or March Madness bracket contests. And many other sorts of things. 

The host is constrained by the rules of the loyalty program, which will typically be a tiered system. So if for example your betting just barely qualifies you to participate in the VIP program, you can’t ask for Super Bowl tickets for you and one hundred of your closest friends. I mean you can ask, but… 

The more you bet, the higher the tier you qualify for. Higher tiers generally earn more points per dollar bet—a point just being a proxy for a cash back percentage. The highest tiers in a program can earn, just as a ballpark figure, something in the range of 1.5 percent cash back. That is, at 

******ebook converter DEMO Watermarks******* 

the highest tier, for a $1,100 point spread bet at -110 odds (and with a $50 theoretical loss), you can potentially earn points worth about 1.5 percent of $1,100 or $16.50. 

Maybe $16.50 doesn’t sound like a lot when you’re risking $1,100—but from the sportsbook’s perspective they’re returning $16.50 of your $50 theoretical loss or about a full one-third of your losses back. 

If you were able to selectively bet only in spots that were about break even (without betraying this fact to the sportsbook via CLV), then you would rack up those loyalty points without incurring any real expected losses. 

Typically, sportsbooks will try to avoid giving you hard cash for your points. If you earn $1,000 worth of points, they’ll rarely permit you to cash those points in for $1,000 straight into your account. Instead, you’ll be offered contest entries or free bets or bet boosts. Or you’ll be given extremely generous rakeback arrangements on, say, daily fantasy contest entries. Or you’ll be offered special bets with extremely favorable rules (e.g., you can place a moneyline bet and the moment your team takes the lead, you can no longer lose the bet—you can only win or push). Or you’ll be offered the chance to buy gifts from a catalog with your points around holiday times. 

Sportsbooks always love to offer their VIPs deposit bonuses if they happen to need a reload. 

VIP programs also qualify for “race” type contests against other VIP players. Weekly “whoever bets the most this week wins a prize” type contests. Or “bet to this dollar threshold this week and earn this bonus” type deals. Or “earn a relatively small free bet or bonus in your account every day that you log into your account.” 

Added up over a year of play, the perks these programs offer can be extremely significant. You’ll get plenty of actual cash back via the bonuses and free bets and rakeback and contest entries and so forth. And you’ll also get other things which may have more (or less) value to you depending on your personal preferences. Cruises. Other travel. Food and drink. Event tickets. “Expensive toy” type gifts. That sort of thing. 

The programs tend to be lucrative enough that as long as you can be roughly break even on your actual betting, it’s well worth pursuing the highest tier you can qualify for at any sportsbook. 

******ebook converter DEMO Watermarks******* 

But there we’ve just said a mouthful. The entire program is designed around theoretical losses—you’re expected to lose on the betting. You aren’t supposed to break even on your betting. Nevertheless, being able to “win” by being break even gives you a lot of flexibility. You don’t need every bet you make to be a good one. You just need to be able to offset any bad bets you happen to make with good ones of equal value. 

This flexibility is useful as you’ll soon see, as if you want to stay welcome to bet for a long period of time, you’ll have to use a lot of discretion with which (good) bets you allow yourself to make. 

### How Not To Get Kicked Out 

The following guidelines are in no way ironclad. If you’re trying to win money from your sportsbook (and if you’re any good at it), then you are an undesirable customer to them. There’s no way around that. 

Eventually, if you win consistently (whether from the bets themselves or from the VIP program perks), some key sportsbook employee is going to see that big negative number next to your account and decide enough is enough. That’s just how it goes when you deal with modern sportsbooks. 

But if you keep these guidelines in mind as you bet, you have a much better chance of lasting for a while compared to someone who is ignorant of these things. 

**Rule 1. Don’t show up the trader.** The trader is the sportsbook employee who is responsible for managing the odds offered by the sportsbook. “But,” you protest, “Didn’t you just say that the odds come into the sportsbook platform software from third party content provider services?” They do indeed. But sportsbooks typically add a management layer between the raw odds from the content provider and the offered odds. 

Basically, they employ a room full of people who sit in front of computers and televisions whose job it is to tweak the odds. Sometimes they tweak the odds just to fix errors in the odds feeds. Sometimes they tweak the odds to bias the prices slightly against anticipated action. (A very large sportsbook will have operations in many states. If Ohio State is playing Michigan, the traders may make the Buckeyes slightly more expensive to customers in Ohio while they make the Wolverines slightly more expensive to customers in Michigan.) Sometimes they tweak the odds 

******ebook converter DEMO Watermarks******* 

to discourage further action on a side they’ve already taken lots of action on. Sometimes they tweak the odds just because they’re old-fashioned and have an opinion about what the price should be. 

The key idea here is that while the sportsbook offers thousands of bets at any given time, and for the most part those prices are provided by content providers, there’s likely also a sportsbook employee called a trader who “owns” any particular bet on the menu. 

So if you see Ohio State ‑9.5 ‑120, that price indeed comes from an odds feed. And the trader assigned to that game doesn’t (or shouldn’t) have the ability to change that ‑9.5 to ‑2.5 or ‑14.5 or something drastically different from the feed price. But they can tweak it a little. Perhaps the price came in from the feed at ‑9.5 ‑110 and the trader moved it to ‑120. For some reason. 

If the trader’s choice to move it to ‑120 was a bad one, and you take advantage of that choice, you are potentially showing that trader up. The trader might have to answer to their boss for losses on the market. 

Or, possibly more likely, they may just find your betting behavior to be annoying to them. The same way you’d find it annoying if you spent dinner with someone who interrupted the flow of conversation constantly to correct you on every error you may have made whether large or small. You may just piss them off. 

But this advice gets a little tricky. Every line you bet you should think is an error. So how do you know if you’re “showing up” the trader or not? To really understand that, you have to put yourself best as you can in the shoes of the trader. What behaviors would annoy you? 

Let’s go with some obvious ones. If you bet injury news the millisecond it comes out, you’re showing up the trader. Why? Think about if it was your job. You work eight hours a day managing lines. You’re responsible for dozens of lines at a time. And here you’ve got some customer who you can tell is refreshing Twitter 24/7 just so they can shove in a few $500 Dallas Dills first half bets every time you take a bathroom break. 

And then, instead of backing you up, your boss calls you in after the game and asks you to explain why you gave the bets. Wouldn’t take more than a couple of these until you were ready to press the big red “nuke account” button on that customer, right? 

In general, any betting opportunity that relies on jamming the bet in before the line corrects is prone to get you in hot water with the trading team. 

******ebook converter DEMO Watermarks******* 

What isn’t showing up the trader? Any bet on a widely available line that’s had time to settle into place. Bets into third party “products”—for example, the single game parlay product. This isn’t a simple line that a trader can manage. Therefore, if you find a good bet here, it’s not the trader’s fault. You aren’t showing anyone up. Many in-play bets, particularly any bets on derivatives (i.e., not the main game spread, moneyline, or total). The sportsbook will be heavily reliant on content provider services to offer these lines, and it’s less likely a trader will “own” any errors here. 

**Rule 2. Don’t bet things recreational bettors don’t bet.** Modern sportsbooks are designed to cater to recreational bettors. You might assume that every bet on the menu is there because recreationals like to bet it. 

That’s not how it works. Recreationals tend to like to bet certain things and not others. Many bets on the menu will go almost entirely ignored by recreational customers. 

This is, perhaps, an inefficiency of the present modern sportsbook model. Why are they filling their menus with bets that their target customers don’t want to make? We don’t have a good answer for that one. Nevertheless, that’s what they do. 

There are no hard and fast rules about what recreationals do and don’t bet, but again, if you try to put yourself in the shoes of a recreational bettor, it will give you some insight. 

They prefer overs to unders. This is largely about the sweating experience. If you bet an over, you can lock in a win early. You also usually always feel like you have a shot to win even if you need a miracle. Betting an under offers the opposite experience—if the result of your bet is locked in during the third quarter, you’ve lost. And even when you’re on the path to winning, you’re worried until the very end that a miracle might kill you. That sort of “negative” sweat is generally less fun. Recreationals bet for a good sweat. 

This tendency to avoid unders is particularly strong for star players. No recreational wants to have to sweat a Josh Allen under yardage bet in the fourth quarter.  The sick feeling will start the moment the Bills get the ball down two scores with nine minutes left, and it won’t leave until the final whistle blows. Maybe a recreational decides to fade a scrub wide receiver. But a premier player? Rarely. 

******ebook converter DEMO Watermarks******* 

They don’t like laying big money. If you look at the “Will this game go to overtime?” prop, you’ll often see something like Yes +600, No ‑1000. And if you model it out, a reasonable guess might be that six percent of games go to overtime. That is, Yes is a horrible bet, and No is a good one. 

This is not an error or oversight. Sportsbooks price this bet like this because recreationals simply don’t bet the No. The sportsbook probably shouldn’t offer the No at all, since they don’t intend anyone to bet it. Instead, they do tend to offer it, but it’s kind of there just to make the menu look a certain way. You aren’t actually intended to bet it. 

Recreationals like to bet on games they can watch. Again, this is about the sweating experience. It’s no fun to try to sweat a bet when you can’t watch the game. For sports like college football or basketball, pay attention to which games are and aren’t being televised. Non-televised games will get less recreational action. 

So, for example, betting an under in a non-televised, non-conference college basketball game is—well it’s not a very recreational sort of bet. 

Same goes for foreign sports and leagues. If you (I’m talking to you now, dear reader) are from Europe, you may not appreciate how little recreational bettors in the United States care about soccer. If you find a good price on an Italian Serie A game and you bet it, you may be surprised to hear that there’s an excellent chance that you’ll be the only person in your entire state who placed a bet on that game. Not very recreational. 

**Rule 3. Seek out major market bets on game day with small edges.** These markets are hard to beat. The sportsbook knows this, which is why these are great markets to bet if you’re looking to grind VIP status. You don’t have to win on the bets to reap the VIP rewards. You just have to roughly break even. And you have to break even on your entire body of bets, not every individual bet. The best way to get in betting volume is to bet your good bets here and there (your good props, your single game parlays that break the model, your in-play bets, and so on), and then drown those in a sea of mediocre major market bets. If you get the ratio right, you’ll have a small percentage edge on your entire body of bets taken together, but you’ll also look to the trading team like you bet like an average doofus. 

In the United States, major market sports are NFL, college football, NBA, and MLB. College basketball and other smaller sports (leagues like college baseball, WNBA, MLS, and so on) suffer from lines that move too 

******ebook converter DEMO Watermarks******* 

much even on game day. Let’s say you bet a college basketball game over 132 on game day. Consider two universes. One where the total moves to 135 before the game starts. And another where it moves to 129. 

If the total moves to 135, then your over 132 bet was likely good. This is the sort of bet the trading team will flag as possibly a sharp bet from someone trying to win. 

If the total moves to 129, then your over 132 bet was likely bad. Your bet won’t flag as “sharp,” but you also won’t get extra credit with the trading team for being a special dumbass either. 

When you bet these volatile sports (volatile because they’re not very liquid at the market making sportsbooks), you’ll end up by accident with a handful of bets that look “sharp” because you happened to beat the closing line by a good bit. This could work against you even if you don’t think it should. 

Major sports are safer for the purpose of VIP status grinding because they’re less likely to move on you. What kind of bets are you looking for? 

Look for bets where you have an angle, but you aren’t sure if the angle is strong enough to beat the hold. Say the spread on the Ravens game moved two hours ago, but your target sportsbook moved the corresponding moneyline only to ‑300 when it “should” have moved to ‑315. Bet the ‑300. 

You’re inclined to bet over in the Raiders-Chargers game because the wind is supposed to be calmer than previously expected, and your target sportsbook has 51 while you see 51.5 at other sportsbooks. 

You read on Fangraphs that the Cardinals starting pitcher’s velocity was down in his first start off the injured list, and you can bet the Cubs at +120 at your target sportsbook while the best price elsewhere is only +115. 

Recalling concepts introduced in _Logic_ , the general principle here is we’re looking for two things. One, a minor angle (an opinion on weather, injuries, coaching strategy, etc.). And two, a smaller-than-usual synthetic hold between your target sportsbook and other sportsbooks in the market. These two effects work together to get your expected losses on these “cover” bets down as low as reasonably possible. 

The astute reader may notice that if you bet this way, you’ll be betraying your “sharpness” by tending to bet only when the price offered is somewhat better than the “market” price. You’re betting ‑300 when there’s ‑315 elsewhere. Betting over 51 when there’s 51.5 elsewhere. Betting +120 when there’s +115 elsewhere. 

******ebook converter DEMO Watermarks******* 

It’s true. This will be a consistent pattern. But this price-shopping tendency alone shouldn’t get you restricted at a large top 4-type sportsbook offering a generous VIP program. 

In the listed examples, you likely aren’t betting trader errors—the traders probably know where these prices are relative to other sportsbooks, and they have hung these prices for a reason. They know that they can expect some extra “bargain shopper” action on these markets, and they’re likely okay with that. 

They’ll no doubt notice that you have a particular tendency to bargain shop, but if you don’t do other things to embarrass them or piss them off, the trading team will likely leave you alone. 

Theoretically, once the traders identify you as a consistent bargain shopper, they should notify the marketing department to stop sending you the extra nice bonus coupon books, so to speak. In practice, this rarely happens as there’s usually a lack of communication between trading and marketing. As long as you don’t get the ax from the traders, the perks from marketing tend to keep flowing. 

**Rule 4. Bet parlays.** Parlays are great. They are very popular with recreational bettors. 

They also benefit from a bit of bogus accounting. Recall from _Logic_ that parlays are a mechanism to increase betting volume. The concept behind a parlay is that if you win the first leg on your ticket, you automatically parlay all of it (the original bet plus the winnings) into the second leg. If you win that one, you automatically parlay all of that (the original bet plus the winnings from the first two bets) into the third leg. And so on. A “parlay bet” might just look like a single bet on a single ticket, but mathematically it represents a series of bets placed consecutively. 

If you bet a three-leg parlay of 50‑50 bets (e.g., three different point spreads), then there is a 50 percent chance that you’ll place a single bet (and lose it), a 25 percent chance that you’ll place two bets (winning the first and losing the second), and a 25 percent chance that you’ll place three bets (winning the first two). 

Thus if you bet $100 on such a three-legger, you’ll bet $100 total 50 percent of the time, $291 total 25 percent of the time (the initial $100 bet plus the $191 bet-plus-winnings rolled over onto a second bet), and $656 the other 25 percent of the time (the initial $100 bet plus the $191 bet-plus- 

******ebook converter DEMO Watermarks******* 

winnings rolled over plus the final $365 bet-plus-winnings rolled over a second time). 

That equates to an average effective amount bet per parlay of about $287 or close to three times the original $100 bet. (This approximate math tends to hold—the total average betting volume of a parlay of 50‑50 options will be roughly the number of legs times the original bet size. It falls slightly short due to the hold or “short pay” of each leg.) 

If such a winning parlay pays 6‑to‑1, then after eight tries, you will win one for $600 and lose seven for ‑$700 or a net loss of ‑$100 per eight plays or ‑$12.50 per play. 

There are two ways to convert this loss to a sportsbook hold. One would be to divide the average amount lost by the average betting volume ($287 in this example), for ‑$12.50 / $287 = ‑0.0436 or a 4.36 percent hold. 

This is the method we suggest you use for your own personal accounting. If you do so, you see that the sportsbook’s theoretical percentage hold on the parlay bet is roughly the same as its theoretical percentage hold on the constituent single bets. 

The second way is the way the sportsbook industry does it. They ignore the bet volume magnifying effect of the parlay and they divide the average loss by only the initial bet size ($100 in this example), or ‑$12.50 / $100 = ‑0.125 or a 12.5 percent hold. 

On top of this, the sportsbook industry tends to separate parlays from single bets in their accounting. So they might see that they hold 2 percent on single bets in a particular sport, but 18 percent on parlays. And their eyes pop out at this massive (percentage) difference, and they conclude that they want their customers to bet parlays, parlays, and more parlays. 

Because of this accounting quirk (and because recreational bettors do indeed love them), parlays have an undeserved reputation as “sucker bets.” Which means they’re great cover for the sharp bettor. 

Single game parlays are included here. Top 4-type modern sportsbooks that offer this product promote it heavily, and playing the single game parlay product should look good on your account so long as you don’t throw whatever angles you may have found in the traders faces. 

For example, let’s say your sportsbook launches an NHL single game parlay product that features single player shots, goals, and assists as parlayable options. You know that NHL skaters play in predetermined lines, which means the same skaters will tend to share the ice with one another. 

******ebook converter DEMO Watermarks******* 

One player’s goals will be correlated with another player’s assists due to this tendency to play together. 

But you also know that some groups of skaters will be more correlated with one another than others. Some skaters play not only on the same fullstrength line together, but also on the power play line. By playing with the single game parlay widget for a few hours, you sense that the underlying pricing model uses a “league average” correlation factor between skaters who play on the same full-strength line. It applies the same adjustment to all skaters in the league. That is, it seems to have a static list of who plays on full strength lines together, and it ignores power play lines. 

Also, when coaches occasionally change the line compositions for a single game or on a forward-going basis, you’ve noticed that the model often seems to use the old, stale full-strength lines to price correlation rather than the new information. Another piece of evidence for the “static list” thesis—perhaps you notice that it all gets fixed one day. Maybe behind the scenes, once a week or once every two weeks it’s some trader’s job to go back through all the NHL full-strength lines and update the list. 

These two modeling failures give you moderately good bets night after night on the same few sets of skaters who are most correlated with one another. And it occasionally gives you some very good bets in specific places where the model hasn’t caught up to the coach’s changes. 

It’s completely fine to bet these edges. Throw together single game parlays that include a goals over for one skater and an assists over for a highly correlated second one. Try to add some other legs that don’t seem to hurt the total expected value of the bet too much. 

Adding extra legs to the parlay has three benefits. One, it throws some noise in to make it slightly less obvious what your angle may be. If you have period overs or puck lines and what not in your parlays along with the player props, a trader doing a quick scan of your action may not see anything notable. 

Two, it looks more “recreational” to bet four or five leg parlays versus two leggers. 

Three, it adds variance to your results. If you’ve found a good edge and you just grind the two leg parlays, you’ll basically just win and win on them. You do not want your wins to be steady and consistent—you want to hide the positive expected value of your betting strategy amongst the noise of variance. This is an important idea that runs counter to many would-be 

******ebook converter DEMO Watermarks******* 

advantage gamblers natural inclinations. If you bet a zillion two leg parlays every night and all you do is win, the traders will notice and restrict you. If instead you spray regularly on multi-leg parlays and you happen to hit a few more big parlays than you’re “supposed” to, it’s not so obvious that you have an angle. Maybe you’re just lucky. 

So yeah, it’s totally fine to bet these model errors—even to bet them regularly. What the trading team won’t like is if you find a plum opportunity on a new first line in Philly, and you decide to push that edge by jamming in 150 different parlays each centered around goals scored (or assists) for skater one and assists (or goals scored) for skater two. 

Again, consider if you’re making someone look dumb or lazy or bad at their job with your betting behavior. It’s someone’s job somewhere to maintain that list of skaters and full-strength lines that determines the correlation applied in the single game parlay product. Obviously that person will be slow to update or will make mistakes sometimes. If you casually bet these errors when you notice them, great. If your betting behavior amounts to flashing a blinking red sign saying, “Dumbass! These skaters play together now. Didn’t you watch the press conference? You’re so bad at your job you should probably be fired!” you just might piss someone off. That’s how you get restricted. 

To be clear, if you somehow bet 150 parlays every night, and this night you just happen to bet them on this particular plum spot, it’s actually probably fine to go nuts. What’s not good is if you bet two parlays a night and then one day you see a really great spot and bet a hundred times on the same angle. 

There’s a myth that successful sports bettors really pick and choose their spots. That learning how to “lay off a game” (i.e., to not bet it at all) is somehow a valuable skill. To the contrary, the most successful sports bettors that we know tend to place a mind-bendingly enormous number of bets. Most of the bets they make have little to no edge at all. When they take stock of their action at the end of the year, they tend to end up with an aggregate return of maybe 1 or 2 percent on all their bets, but they make that on a truly massive betting volume. There are several reasons why they bet this way, but this concept of “hiding the betting signal by creating a lot of betting noise around it” is one of the key ideas. 

It’s possible that being able to find an endless supply of break-even bets might be the most valuable sports betting skill of all. 

******ebook converter DEMO Watermarks******* 

**Rule 5. Variance.** Variance is your friend. 

Your instinct, for obvious reasons, might be to try to deposit money into a sportsbook as little as possible—ideally only once. But that instinct is all wrong. At least it is if your goal is to win the most money possible from your relationships with modern sportsbooks. 

Sportsbooks absolutely love deposits. Nothing makes your account— and you—look better to the marketing folks than you depositing money. They love it so much, in fact, that once you’ve attained a certain status with them, they’ll nearly always offer you a bonus on your deposits to incentivize you. 

These bonuses are free money to you, and they can be generous. When you deposit, you win twice. You get free bonus money immediately, and you also make the marketing people happy with you so they will give you more free stuff later. 

The problem with this logic, of course, is that in order to deposit you must first bust your account. Perhaps this sounds undesirable. Consider two universes. 

In both universes, you’ve found sports bets you can make that generate for you $10,000 in total expected value. You bet these bets at your two favorite modern sportsbook brands, BeaverBet and BetBeaver. 

The first universe is the zero-variance universe. You bet your bets, and you win exactly $5,000 at each of the two sportsbook brands. The trading teams at both of these books realize you are grinding them down, and they restrict your accounts. Enjoy your winnings, because that’s all you’re getting. 

The second universe is the Yeehaw! universe. You bet your bets, and you still win exactly $10,000 between the two sportsbooks. But you do so by winning $510,000 at BeaverBet while losing $500,000 at BetBeaver. 

The trading team at BeaverBet, the ones you just beat for half a million, might or might not cry uncle. Maybe they look at your crazy, high-variance betting and think you got lucky, and they let you keep betting to give you a chance to lose it back. Or maybe they decide they’re done with you and restrict your account. 

But at BetBeaver, the ones you just lost half a million to, you’re a marketing department folk hero. You’re wild. You’re crazy. And most importantly, you’ve passed all their know-your-customer and source-of- 

******ebook converter DEMO Watermarks******* 

funds checks with flying colors. When you lose, you just deposit again. And again. 

How long you will keep it up, no one knows! But the marketing department is going to make sure that as long as you do keep depositing, you keep depositing at BetBeaver. They put you in their highest tier—the ultra-VIPs. Expect generous deposit bonus offers, freeroll tournament entries, straight cashback, and more. 

In both universes, your betting bottom line is the same. You’re up ten grand. But in the first universe, you’re done. That’s all you get. In the second, you’ve got one sportsbook potentially desperate to win their money back from you and another primed to shower you with very valuable bonuses and perks. 

On top of the extra monetary perks you receive in universe two, there’s an additional intangible benefit. Your status with the marketing department at BetBeaver may also earn you a “get out of jail free” card with the trading department. Say you find a juicy pricing error, bet it, win big, and in the process, you really embarrass the head trader. They try to slap a nasty restriction on your account. But you appeal to your friends at marketing, and they use their pull to get the restriction lifted so you can keep betting. 

To be clear, it won’t always work out this well. You can lose to a sportsbook, deposit with them several times, and still find yourself on their shit list. But regardless, the point stands. Variance is one of your greatest allies. 

### Final Thoughts 

There are various strategies to win at modern sportsbooks. There’s the bonus grab, where you try to maximize your initial deposit and signup bonuses, play them through, and call it a day. There’s the slash and burn, where you max bet every mistake line you can find until they restrict you. There’s the “under the radar” where you make small bets and try to win small amounts over a longer period without attracting attention. 

But arguably if your goal is to win the most money possible over the lifetime of your betting account, the best strategy is to go the VIP route. You don’t smash and grab, and you also don’t fly under the radar. You 

******ebook converter DEMO Watermarks******* 

actively build a long-term relationship with the sportsbook and its hosts and other employees. 

This is arguably the most lucrative, but it’s also by far the trickiest. You have to (convincingly) present yourself as one of the sportsbook’s best customers. You have to make lots of bets that are meant to appear to trained employees to be losing bets—but that actually aren’t losing bets. 

It requires a blend of several skills. You obviously have to have the math and gambling skills to tell a good bet from a bad one. Because this is sports betting, you need some sports knowledge to suss out the nuances of the sport the people building the pricing models may have overlooked. 

You also need people skills to keep your relationship with the host and other employees a positive one. You need to have a sense for the difference between winning “fair and square” in the eyes of the sportsbook employees versus pissing someone off or embarrassing someone for making a mistake. You need to stick mostly to the “fair and square” bets and avoid setting off fire alarms in the trading offices of your favorite sportsbook. 

You also need a dash of acting skills. If you’re there to win the sportsbook’s money, you can’t tell them that. You’re expected to be there for recreation, and so in your interactions with the host and other sportsbook staff you have to play the role—convincingly—of someone who is betting for betting’s sake. 

But if you do check all the boxes, there are potentially a lot of perks waiting for you. The VIP programs can be generous—and the better a customer you appear to be to the sportsbook, the more generous they can be. If the host and other employees see you as potentially a top 0.1 percent customer of theirs, you’ll get cash back, free bets, generous deposit bonuses, sports tickets, travel, special event invites, invites to lucrative VIPonly contests and tournaments, and you’ll have the ability to ask for things that you want—say 10× limits on in-play five-a-side pickleball matches— and actually get them. 

For all this, the sportsbook will expect you to lose. And you will disappoint them. But you won’t shove it in their face. You’ll place a lot of bets, most of which you have little to no edge on (or even a slight disadvantage on, though never if you can help it will you place bets where you are giving up the full theoretical hold to the house). You’ll find a handful of consistent errors in their betting products—single game parlay modeling errors, in-play data or modeling errors, deficiencies in trading 

******ebook converter DEMO Watermarks******* 

player props against information, weak futures books, and so on—and you’ll hit those errors often. Just enough to make sure that the entire body of your betting has a small but consistent edge for yourself. 

You’ll make liberal use of parlays so that your account goes (intentionally) through significant down and upswings. This swinginess will make the fact that you happen to be ahead against the house look more like luck than skill. (Losing runs also present you with opportunities. If you run bad and bust your account, you can ask your host for a redeposit bonus or a lossback percentage.) 

Oh, that’s another skill you need. You need to have the stomach to handle the swings of gambling. And the bankroll. This is a rule for winning gambling across disciplines. If you want to win at gambling, then you have to find someone to lose to you. No one, and we mean no one, wants to lose to someone who appears to want to play angles all day and never wants to take a risk. If you play poker, but refuse play any hand but pocket aces, only true newbies to the game who don’t understand your strategy will be willing to lose to you. If you try to play off your deposit bonus by betting red and black simultaneously at roulette until your playthrough requirement is met, you won’t be welcome back for another bonus. 

The more you embrace the actual gambling—the ups and the downs— the better your gambling career will go. 

If you’ve done all this right, then one day you will be watching the conference championship game completely comped, travel and all, from your favorite sportsbook’s corporate suite, and your host will slap you on the back and introduce you to the CEO by saying, “This is the luckiest asshole I’ve ever met.” 

******ebook converter DEMO Watermarks******* 

# WINNING ANGLES 

To this point, the book has mostly been about how modern sportsbooks work. Now it’s about how to find winning bets. 

The surest way to find winning bets is to operate a full-blown modeling operation. Build and maintain statistical projection systems for your sport, model the effects of rule changes, weather, travel, time changes, other scheduling effects, coaching, injuries, and so forth. 

The top betting groups in the world do this. It’s quite hard. It’s both a lot of work to build a system like this, and it can be devilishly difficult to debug it to the point where the system consistently suggests good bets. Garbage in, garbage out is an ever-present possibility—even when you’re using a system that has worked in the past. 

If you want to give building such a system a go, do it. You’ll learn a lot no matter how it turns out. 

But the perspective of the remainder of this book assumes that you, for one reason or another, do not plan to go that route. You want to find winning sports bets, but you don’t want to try to handicap one or more sports from scratch. 

This is also a reasonable choice. It avoids doing an absolute ton of work, and modern sportsbooks present many good betting opportunities that don’t require it. 

But we want to make it clear—this is not a shortcut. The people who do the full work and do it well have the chance to make a lot more at this than the people who skip the full work. 

Okay, having said all that, we’re going to list a number of types of betting angles. We will explain how you find the good bets. Then we will analyze the angle along a few dimensions. How commonly you will find bets using it. How reliable it is (i.e., how frequently you will make mistakes trying to use the angle). How sportsbook employees are likely to view your action should you choose to use the angle. 

******ebook converter DEMO Watermarks******* 

We will start with the more commonly known angles (not coincidentally also the ones that will get your accounts restricted the fastest) and then move on to subtler plays. 

### Angle #1. Time-based arbitrage, a.k.a., steam chasing 

Modern sportsbooks get their odds from feeds provided by content companies. The content companies source their odds from other content companies. Those companies potentially from other companies yet. At some point if you go far enough back in the chain, there is an odds source— a market making sportsbook (or multiple such sportsbooks) that takes a guess at what the odds should be and permits all bettors, known winners among them, to bet. 

When a betting group sees a widely available line that they think represents a good bet, they bet it. For the sake of argument, let’s say the widely available total on the Kentucky-Duke basketball game is 136.5, and the betting group likes over. 

Representatives of the betting group may bet it at the market making sportsbook that serves as the odds source for the content chain. But they know that the moment they do so, their information (that they like over) becomes public. The market making sportsbook will have software that automatically moves the line in response to a bet from the group. So the line might move from 136.5 to 137 or 137.5 in response to the bet. 

Additionally, this market making book might have a limit as low as a few thousand dollars on the bet size permitted. 

Say the betting group, Blue Horseshoe, thinks that over 136.5 is a good bet that expects to have about a five percent edge. For every thousand dollars bet, the group expects to win $50. And say the market making book has a $3,000 limit on bet size. 

That makes one limit bet worth $150 to the betting group. Not that much money. And in order to claim that $150, the group has to give away to the world (including all those content companies and then, ultimately, the billion-dollar modern sportsbooks) the information that they think over 136.5 is a good bet. 

******ebook converter DEMO Watermarks******* 

So they don’t bet at the market making book—at least not first. Before they bet their play at the book that will propagate information quickly, they try to bet it in other places. 

Which other places? That is known only to them. The point though is that Blue Horseshoe and other serious betting groups are keenly aware of how the chain of content providers works. They bet their plays in ways designed to disrupt this flow of information—at least to disrupt it long enough so they can get all the bets down they want at the prices they like. 

But inevitably word leaks out. Every time Blue Horseshoe places a bet at a price they like, there’s someone on the other side of that bet who now knows the play. Maybe that person is a trader or some other employee of one of the sportsbooks that Blue Horseshoe uses. The trader texts a friend, “Hey I think Blue Horseshoe likes over 136.5 in the Duke game.” 

Maybe the friend tries to make a few bucks off this tip and bets over 136.5 wherever he can find that price still available. Now more people potentially know—whoever was on the other side of those bets. Maybe those people also send texts to a friend, or they bet it themselves. Eventually this wave of people betting the Blue Horseshoe information arrives at the shores of a market making sportsbook, and enough people place over 136.5 bets there that the price moves to 137 or 137.5. The moment this happens, the content provider network follows the move, and the price moves everywhere. 

This dynamic—the content provider network playing a game of telephone with odds updates, the betting groups trying to thwart that game, and bits of information about the betting groups plays working its way slowly through the system—means there is an opportunity to ride the coattails of betting groups. There is a predictable time lag between odds moves at some sportsbooks (the ones that tend to get bet into before the market maker) and when the information fully propagates through the content network. 

You can win at sports betting simply by watching for these early movers to move and then quickly betting the same side at the late movers. 

We, of course, can’t write in a book, “Watch for a move in college basketball totals at sportsbook X and then go bet it at sportsbook Y,” because it’s a dynamic market and the X and Y roles will be filled by different sportsbook brands at different times. If you want to apply this angle, you have to “learn the market.” Basically, you have to spend many 

******ebook converter DEMO Watermarks******* 

hours watching screens listing odds at many sportsbooks, and you have to learn the patterns of how information propagates through the system. 

This process—watching for early moves and then betting them at the late-to-movers—is colloquially called steam chasing. It will net you many, many bets, since markets are constantly moving and betting groups inject information into the system all the time. It’s only partially reliable, however, since you typically won’t have all the information (who bet what, where, and why). You’ll just see odds move, and you’re inferring much of the rest (that a winning betting group liked the price for some reason and that’s why the odds moved). Sometimes this inference will be wrong—and sometimes you’ll be outright tricked (i.e., someone is intentionally sending bogus information out into the market). 

The biggest strike against using this angle, however, is that sportsbook employees despise it. First of all, it’s obvious what you’re doing. You’re the person who reliably bets on stuff exactly two minutes before the odds update comes in, and miraculously you’re always on the right side. Second, it makes the traders look bad. They may have to answer to bosses, “Why are you slow on these updates?” Even if they don’t have to answer to anyone, they’ll know you’re hurting their bottom line. They’ll also know what you’re doing, and they won’t respect it. 

This angle works. You don’t have to know anything about sports to employ it—you just have to participate in the sports betting market enough to learn how information propagates through it. But using it will earn you the ire of sportsbook employees and it is likely to get your account restricted very quickly. 

### Angle #2. Information arbitrage 

This angle is similar to the first angle. Except here, the play is to watch for news or other information that would affect the betting odds. Then the moment news hits, you try to identify sportsbooks that haven’t updated odds yet. You bet the stale lines before the sportsbooks can react. 

If a star player is listed as 50‑50 to play in a game, you wait for the first hint of clarification on Twitter or in some other place. If the star plays, you bet on his team. If the star sits, you bet against them. Duh. 

******ebook converter DEMO Watermarks******* 

The moment an injury on an important player is announced, you locate sportsbooks that haven’t reacted yet and bet against the newly injured player’s team. 

You watch for baseball or soccer starting lineups to be announced, and if there are any significant surprises, you bet on or against the surprising team accordingly. 

This is also an angle that comes up all the time. Bettable news comes along quite frequently. Lineups come out every day, and surprises will come along here and there. In basketball in particular, injury information is huge, since a single player can swing bet pricing a lot. And information about whether and how much an important-but-injured player may play often comes out shortly before a game. 

It's also hard to get this wrong. If an important player isn’t playing, it’s often a slam dunk to be a good bet against that team. The main way to get it wrong is to forget that the market price before news hits often prices in a chance the player will be announced out. If you misunderstand what that implied percentage is in the pre-news line, you could be overestimating the impact of the news. 

For example, if the Lakers are priced at 65 percent to win and then LeBron James is announced out of the lineup, it’s possible the Lakers move to only 64 or 63 percent after the news because it was already assumed by the people who shape the market that James was unlikely to play. In that case, betting the Lakers’s opponents at 37 percent (not 35 percent as there is hold on the market) might end up a bad bet even if you get the jump on the news. 

But again, the main problem with this angle is not that it’s rare, nor that you’re likely to get it wrong. The problem is that it’s dead obvious what you’re doing, and it will certainly piss off the sportsbook employees if you do it even somewhat regularly. No one wants to have to explain to their bosses why they’re allowing customers to bet injury news before they update the line. No one will think you’re clever. Just annoying. 

### Angle #3. Second-order arbitrage 

Backing up for a moment, “arbitrage” as we are using it defines the class of angles where you hold no opinion about the underlying price of the market 

******ebook converter DEMO Watermarks******* 

you are betting. Instead, you are observing a logically incompatible difference in two or more prices and betting the one (or possibly more than one) price that seems most likely to be wrong. 

In other words, if you bet a Lakers moneyline at 65 percent, if you’re betting an arbitrage angle, you have no inherent opinion on the baseline correctness of the 65 percent estimate of the Lakers’s winning chances. Instead, you’re betting Lakers at 65 percent because you see the same bet offered at 70 percent or higher at some other sportsbook. 

In the first two angles, not only did you likely see the bet offered at 70 percent somewhere else (either due in the first case to betting group activity and in the second case due to news or information propagation), but your best assumption is that the sportsbook where you’re betting the 65 percent will very soon also move their price to 70. They just haven’t gotten to it yet. 

With second-order arbitrage, you are logically doing the same thing. You’re placing a bet based on a change in price you’ve seen elsewhere. And you have an expectation that the sportsbook where you are betting will eventually update their price on the bet you’re making. 

But this time you’re a little more subtle about it because you aren’t betting directly on the market that moved. Instead, you’re betting on something else that—due to the logic of the situation—will also be affected by the pricing change. 

Using the example from the previous angle, say the Lakers are listed at 65 percent, and then LeBron James is announced out of the lineup. The first-order bet would be against the Lakers, either on the moneyline or the point spread. Perhaps also (depending on the primary role of the player announced out) a bet over or under on the total. 

An under bet on LeBron’s player props would also be a first-order arbitrage as well—except that if LeBron doesn’t play, then the under bets likely won’t be graded winners. Nearly every sportsbook’s player prop rules require that the player appear in the game at some point for the bets to have action. Betting under points on a player who sits the entire game is just returned as a no bet. 

But if LeBron isn’t scoring the 17.5 points attributed to him by the player prop line, those points don’t just disappear. (If they did, then the game total would also drop by 17.5 points and the Lakers’s winning chances would drop almost to single digits. This is obviously absurd.) 

******ebook converter DEMO Watermarks******* 

Those points still get scored—at least most of them do—just by different, non-LeBron players. 

A second-order bet would be to use knowledge of the Lakers’s lineup and player usage in LeBron’s absence and a bit of logic to figure out who will likely score those missing points. And then you bet player prop overs on those players before the sportsbook has time to move the line. 

This approach has several advantages over the more direct arbitrage betting. First, it will often have you betting overs—in this case player prop overs—which is a common sort of bet for recreational players. 

Second, these second-order bets aren’t nearly as time-sensitive as the first-order bets. The moment LeBron is announced out, everyone who works on the industry side, whether they work at content providers or at sportsbooks, is scrambling to try to reprice the first-order markets. Shift those Laker prices. Make sure there’s no exposure on the LeBron props. And so on. 

From the moment that Lakers beat writer Tweets “LeBron is OUT tonight” you have seconds to maybe a minute or two to get that Lakers bet down at your modern sportsbook target before they update their price. 

On the other hand, if you know the Lakers team well and you’re fairly sure that a somewhat obscure bench player will see a lot more floor time than usual as a result, you probably have a good bit more time to get your over bets in on that player. 

The downside to this class of angle is that you can be wrong in a way you couldn’t on the first two. You theoretically can think you know which player stands to get more floor time, but in reality not actually have a clue. This class of angle requires specialized knowledge about sports and teams plus the use of logical inference on your part. Perhaps logic just ain’t your thing. 

We kid, of course, dear reader. Given the wisdom you’ve shown by choosing to read this book, you no doubt have an abundance of the sort of mental faculties required to exploit these second-order arbitrages with ease. (We aren’t wrong to assume this, are we?) 

Regardless, second-order arbitrages should be a bread-and-butter part of your betting arsenal. They’re a reliable source of good bets with opportunities arising commonly. Identifying them is not too difficult a skill to master. And they’re far more tolerable bets to a sportsbook than their more direct, first-order cousins. 

******ebook converter DEMO Watermarks******* 

### Angle #4. Mispriced derivatives 

A derivative is a market where the line is created by a model rather than by price discovery. For a typical Major League Baseball game, for example, market making sportsbooks will offer a small handful of lines for betting. The moneyline. A run line (usually the favored team ‑1.5 runs). A total. First five innings moneyline, run line, and total. Strikeout props for the starting pitchers. Maybe a prop about whether a run will be scored in the first inning. Maybe another prop or three. 

These are the markets that are subject to the price discovery process. Hang a price, let people bet, move the price based on the incoming bets. 

A modern sportsbook might have hundreds of prices on the same game. Run lines from +4.5 runs to ‑5.5 runs. Totals from 3.5 to 21.5. Individual prices for every inning. Strikeout props for the starting pitchers from 2.5 to 12.5. And so on. 

Modern sportsbooks rely on content provider companies (sometimes internally owned and operated, sometimes third parties) to fill out these many extra options on the menu. In turn, these content companies maintain and operate mathematical models that in some way use the price discovered prices from market making books as inputs and extrapolate those to fill out the menu. 

The derivative prices, therefore, will be only as good as the model that created them. Some of these prices are relatively easier for models to nail while others are more difficult. 

Going back in time a little bit, when Matt was in high school, his aunt, <u>[14]</u> ~~.~~ Aunt Eileen, taught him an angle for beating football teasers 

Teasers are an alternative point spread derivative bet. The simplest type was a two-leg parlay of point spreads where the spread was moved six points in your direction. So if the two football teams you were betting were listed at ‑14 and +6.5 on the main point spread, you would get a two leg parlay of the same teams at ‑8 (i.e., ‑14 + 6) and +12.5 (i.e.., +6.5 + 6) that paid even money. 

<u>[15]</u> The break-even percentage of each teaser leg is 70.7 percent ~~.~~ The implication is that if ‑14 will hit about 50 percent of the time, ‑8 should hit somewhat less than 70.7 percent of the time, giving the book the house edge 

******ebook converter DEMO Watermarks******* 

on the teaser. (It’s also implied that the sportsbook could also offer the single, non-parlayed bet of the first team ‑8 at odds of about ‑240.) 

It turns out that this relationship holds for nearly every football point spread. If you add six points to the spread, the bet will hit less than 70.7 percent of the time. 

But it doesn’t hold for all of them. This was Aunt Eileen’s insight. If the six points moved you across both the 3 and 7 (the most common winning margins in a football game), then the teased leg would win more than the required 70.7 percent of the time. That is, if the game spread was ‑8.5, ‑8, ‑7.5, +1.5, +2, or +2.5. (Teasing ‑8 to ‑2 moves it through the 7 and 3, and teasing +1.5 to +7.5 again moves it through the 3 and 7.) 

We, naturally, call this angle the “Eileen teaser,” but you may know them as Wong teasers, named for Stanford Wong, an advantage gambler who wrote about this angle. 

The teaser represents a very simple model for creating a derivative, the mathematical model being, “Adding six points to the point spread moves the odds from ‑110 to ‑240.” This model usually worked, but it didn’t always. The angle was to selectively bet only the situations where the model was wrong. 

Modern sportsbooks use more complex models to price their derivatives. But the way to exploit them remains the same. You’re looking for specific games or conditions where the assumptions underlying the model used to create the derivative odds is wrong. 

So how the heck do you find those? You have to do a little bit of reverse engineering. 

In the most recent college football season (as of the time of this writing), we were checking out the derivatives at a very large modern sportsbook. This sportsbook offered hundreds of pregame bets—alternate point spreads and totals, half and quarter bets, and an array of props. 

Immediately one of the props stuck out. “Will the first score of the game be?” And options were a passing touchdown, rushing touchdown, field goal, or other. 

Field goal was priced as far, far too likely. How did we know that? We’ve spent the previous decades developing pricing models. This experience may, we concede, have helped a little. Nevertheless, what we found in five seconds, we think you too could find in perhaps five minutes. 

******ebook converter DEMO Watermarks******* 

Or five hours. The point is you can find it with some logic and a willingness to check some math—you don’t need to have built models yourself. 

All the other field goal-related markets were also off. Total field goals in the game. Longest field goal. And so on. What would cause this? 

The simplest explanation is that they were using an NFL model to price the college football derivatives. This makes sense given not just what we were seeing in the pricing, but also based on our industry knowledge. NFL, while not a particularly popular betting league in Europe, does have its niche among overseas bettors and has for a while. College football, on the other hand, is completely unknown outside the United States. 

It would make sense that this modern sportsbook (owned by a corporation based in Europe long accustomed to operating in numerous countries there) would have an existing solution for NFL derivatives pricing. Perhaps they had an internal division that maintained an NFL model or a relationship with a third-party content provider. But perhaps they had no such solution for pricing college football. And so they wanted to do business in the United States and offer college football betting, but they had no model to price the derivatives. So they made what seemed like a sensible choice—just use the NFL model to price the college games. 

But college football is substantially different from NFL in a number of ways. The quality of the place kicking is one obvious way. In the NFL, all the teams have exquisitely good kickers. These players can have long careers and there’s really no reason for any NFL team to go without an NFL quality kicker for more than perhaps a one-off game. Where “NFL quality” means ridiculously, absurdly strong and accurate. 

College is a different story. There are way more teams, the players are much younger, and they are also subject to eligibility requirements that place a hard limit on their college career lengths. As a result, college kickers are of highly variable quality—the best being “NFL quality” or close to it. The worst being physically unable to kick long field goals and unreliable even on shorter tries. 

If a college team has a pretty good offense, but a terrible kicker, it’s obviously unlikely that their first score will be a field goal. And it’s also unlikely that the team will kick more than perhaps one field goal in the entire game. An NFL pricing model will ignore this reality and instead assign (implicitly) an NFL quality kicker to the team. 

******ebook converter DEMO Watermarks******* 

Once we got the idea that they were using an NFL model to price their college games, we looked for other bets where the model would get it wrong. Another major difference between college football and NFL is in the style of offenses the teams run. 

In the NFL, every team runs what would be called a “pro-style” offense in college. This is an offense that centers around exquisitely good quarterback play. Yeah, yeah, your favorite NFL team has a bum at quarterback, and it’s true that the very best NFL quarterbacks distinguish themselves from the average and not-so-good quarterbacks in the league. 

But even the worst NFL quarterback can pass the ball accurately and can hit targets downfield. They can run a two-minute offense. They’re all really good. The best are just on another level yet. 

Again, this is not so in college football. So much so that some teams don’t run their offense through the quarterback position in the same way every NFL team does. Some teams run an option offense which leans heavily on offensive line play and athleticism at the back positions. 

College football teams without a pro-style offense will perform substantially differently when playing from behind than NFL teams do. So certain alternative point spreads will be mispriced by an NFL model when applied to some college games. 

Anyway, our theory of “NFL pricing model applied to college games” was thus confirmed, as we saw the expected mispricing. From that point, finding mispriced bets in any college game at that sportsbook was trivial. We just had to look for the markets that an NFL model would misprice. 

A couple callouts from this story. First, college football is a unique opportunity for North American sports bettors. It’s a fiendishly difficult game to model because it’s football (which is tricky by itself) and because of the vast differences in team quality and style. It’s also a sport that had nearly zero attention paid to it by the sports betting industry until just a few years ago. 

While we don’t expect top sportsbook brands to continue to trot out jerry-rigged NFL models to price college games indefinitely, they will have lots of trouble modeling this sport even with built-for-purpose models. You should find mispriced derivatives opportunities in college football for years to come. Look for teams and games at the extremes. Great kickers. Terrible kickers. Great running games. Great passing games. Terrible offenses. Extremely uptempo offenses. Grindy, downtempo offenses. Think logically 

******ebook converter DEMO Watermarks******* 

about what markets these extreme factors would affect and look at the pricing to see if the model attempts to adjust for the extremes or if they’re just using a one-size-fits-all “average” college football team to price things. 

On top of this, the existing pregame markets for college football at market making sportsbooks are quite illiquid compared those for the other major American sports. That is, it don’t take much money to move the line. 

So we have a situation where potentially hundreds of millions of dollars will be bet in the United States with large modern sportsbooks on a packed college football Saturday. And the lines those sportsbooks rely on to book the action—including the basic markets like game moneyline, point spread, and total—are set by much, much smaller amounts of action in relatively more obscure corners of the sports betting world. 

The betting industry here is trying to build a skyscraper on top of a toothpick. 

Now you know. Do as you like with the knowledge. 

Second, perhaps it surprises you that a major sportsbook brand intending to take large amounts of action on college football in the United States would trot out a model with glaring problems to price things. Wouldn’t they put more work into getting it right before they took it to market? 

Simply put, no. Every business incentive in the industry prioritizes getting to market quickly and delivering large amounts of product (i.e., a big betting menu) quickly. “Are these prices good?” is an afterthought. Sometimes a neverthought. 

Customers choose which sportsbook to bet at based on, among other things, whether the sportsbook lets them make the bets they want to make. Sportsbook brands know that it’s expensive to try to reattract a customer who tried out their book, but then moved on to a competitor with a bigger menu or an otherwise better product. 

Every major sportsbook will try to get the shiny new toys out NOW and then worry about little details like the pricing quality later. 

In many cases, that later never really comes. The menus are huge. Sportsbooks do collect tons of data and compile internal metrics about how various types of bets on their menus are performing. But just because the book knows that a part of the menu—say college football derivatives—is underperforming expectations (in this case, expectations are typically measured by the realized hold percentage on bets taken, which is perhaps a 

******ebook converter DEMO Watermarks******* 

flawed metric to begin with) does not mean they can figure out why it’s underperforming. 

Sometimes people in the industry are tempted to make assumptions about why a certain portion of the menu is underperforming without considering other possibilities. In-play betting is an example. The industry is terrified of “courtsiding” on in-play betting, which is the term that describes someone attending a game or match in person and betting with a consistent speed advantage over the data feeds the books use. Many in the industry will be tempted to blame any underperformance on in-play markets on possible courtsiding without truly examining the general quality of their pricing. The pricing may be so poor that their product is just getting smashed straight up by bettors without any speed advantage. 

The upshot of this is that you should pay special attention to anything new on a betting menu. New product is very likely to have serious modeling problems present at launch. And these problems may persist far longer than you might imagine. 

### The “Palpable Error” Rule 

This is a good time to mention that modern sportsbooks write a “get out of jail free” card into their Terms and Conditions to protect themselves from modeling errors. (And other sorts of errors as well.) It’s called the Palpable Error rule or Palp for short. We don’t really want to copy-and-paste someone’s legalese here so we will just give you the jist. It says that the sportsbook reserves the right to void any bets made on markets with listed prices that are a “clear and obvious” error. Or to pay out winning bets at the “correct” odds (determined correct at the sportsbook’s sole discretion long after the fact). 

Yup. The rule is generally worded broadly and vaguely like that and left without too much further clarification. Go ahead and slog through your favorite modern sportsbook’s T&Cs until you find it. 

Theoretically, the idea is this. The sportsbook accidently offers an inplay bet on a game that has already finished and you bet on the winning team. The book reserves the right to void the bet. 

Okay. We think that’s a fairly reasonable policy (though obviously the sportsbook should do its utmost to avoid making mistakes like that in the 

******ebook converter DEMO Watermarks******* 

#### first place). 

In practice, modern sportsbooks sometimes apply this rule (to their advantage) in far more ambiguous circumstances. For example, one reader sent us screenshots from a major international sportsbook brand where the palpable error rule was used to adjust the odds on an in-play baseball run line bet (placed midway through the game) from +120 to ‑200. 

This person placed a bet at +120 odds and won. After the game, the sportsbook claimed that +120 was a “clear and obvious” error, and that the correct odds should have been ‑200 and paid out on those odds. 

We don’t intend to litigate the fairness of this practice in this book. We have personal thoughts about the relative merits (and lack thereof) surrounding this rule and how it is applied, but this book isn’t really the place for these personal thoughts. 

But we did want to call your attention to the fact that this rule will exist at nearly any modern sportsbook that you choose to play at. If you look for and bet mispriced lines, there’s every likelihood that you will eventually have it applied to one or more of your bets. 

You have the right in most jurisdictions to appeal an application of this rule to the regulatory authority. Use this right with care. If you “call the cops” on a sportsbook, you may win. Or you may not. Regulatory bodies vary significantly in how player-friendly they tend to rule on such things. But either way, you will bring negative attention to yourself with the folks who work at the book, and you can expect to have less rope with them going forward. 

Is this right? Is this wrong? Again, we have our personal opinions, but in these pages we will stick to “it just is.” If you play at modern sportsbooks, this is a thing that can happen. Be aware of it. For what it’s worth, you should be able to win plenty of money even if you do get bitten by this every so often. 

Again, just so it’s clear, sportsbooks can claim after the fact that nearly any price on nearly any bet they offered (and you took) was a “clear and obvious” error and either adjust your winnings or void the bet. Now you know. 

******ebook converter DEMO Watermarks******* 

Angle #5. Misalignment between sportsbook house rules and the model’s rules 

This angle is perhaps a subclass of “mispriced derivatives,” but it’s worth a special call out. It’s an angle that many who don’t understand how the sportsbook content industry works might not even look for. 

The pricing for most of the markets on the sportsbook’s menu comes from content services. 

The house rules on those same markets, however, are usually devised inhouse. 

In practice you’ve often got two completely different groups of people working to create just a single offering on the menu. 

It’s very possible for these two groups to miscommunicate on how a specific type of bet outcome should be graded. The people at the content service who are sending the prices think a certain outcome will be graded a loss. But the house rules state that the same outcome is graded a no bet. 

In our time running a content provider service, we ran into this problem more than once with our sportsbook customers. One instance that comes to mind is how moneyline bets (including those placed in-play) on baseball are graded in the event that a game is postponed or called early due to rain. 

Say the Phillies are leading 5‑4 in the fifth inning of a game in Atlanta. You place a moneyline bet on the Phillies. In the seventh inning, a thunderstorm comes, and the game is called with the Phillies still leading 5‑4. 

Some sportsbook house rules say this bet should be graded a win for the Phillies. 

Other sportsbook house rules say this bet should be voided because those rules state that games must go nine innings for bets to have action. 

(We had different customers with different rules for this situation.) 

If you’re a content company, how do you price this bet? To do it right, you need two separate prices—one that gives Atlanta a better chance of coming back to win (for the sportsbook that voids all bets on games that don’t go nine innings), and one that gives the Phillies a better chance to win 

******ebook converter DEMO Watermarks******* 

(for the sportsbook that grades rain outs after the fifth inning as a win for the team that’s ahead). 

On top of that, if you’re the content company, you need not only a baseball model but also a weather model to make the second price, because the moneyline you offer must price in correctly the chance the game gets rained out (and in what inning it happens). 

In reality, this pricing nuance will often go unnoticed by both the content company and the sportsbook. The content company will simply have a moneyline price for the game, and the sportsbook will uncritically offer that price to their customers. 

Any time you see rain clouds looming over a late-inning MLB game, check both the moneyline prices and the house rules at every book you use. If you see two books with roughly the same price, but different rainout rules, then one of the prices has to be wrong. In this example, it’s fairly safe to assume that whatever content company made the line is not playing Weather Channel and is just ignoring the chance of rain when they make the line. So it’s likely a good play to bet the leading team at the book where rainouts are still action. 

We learned of an even more egregious example of this sort of angle from a sharp young modeler that we know. A large, modern sportsbook was offering odds on specifically the ninth inning of MLB games. The content provider was pricing the ninth inning odds to take into account that sometimes the home team doesn’t finish batting in the ninth inning. For example, total runs markets would be listed lower for the ninth inning than for other innings because sometimes only the away team bats. 

The house rules, however, stated that all ninth inning bets were refunded if the home team didn’t bat. 

This led to absurd situations in close games. For example, consider a game where the home team is leading 4‑2 going into the ninth inning. You bet on the away team to win the ninth inning. (To be clear, the bet is “Which team will score more runs in the ninth inning?”) If the away team fails to score at least two runs, then the game ends without the home team batting, and all bets are refunded. No problem. 

Any time your bet actually gets considered for action, your team begins with at least a two run lead. Furthermore, if the away team scores two runs, then the game will usually end on the first home team run. This also means you win, since the away team will have won the ninth inning 2‑1. 

******ebook converter DEMO Watermarks******* 

The only way you can lose the bet is if the visiting team scores two runs and the home team hits a three-run home run or grand slam in the bottom of the inning. 

Eventually they fixed this one. But while it lasted, there were good and sometimes amazing ninth inning bets available on every MLB game. Angle #6. Misalignment between a sport’s rules and the model’s rules 

This category is somewhat similar to the last one, but it’s more pure modeling error than miscommunication. Leagues often tweak the rules of a game. Recently, MLB added a pitch clock and changed the size of the bases. NFL changes kickoff and overtime rules semi-regularly. College football changes the rules about when clocks run and stop. College basketball moves the three-point line. And so on. 

Furthermore, sometimes leagues switch rules up within a season. In MLB, every extra inning starts with a runner on second base. Except not in the playoffs. The NFL’s overtime rules are different in preseason, during the regular season, and in the playoffs. In the past, MLB has ended the second game of a double header after the seventh inning rather than playing a full nine. 

Content companies must build and maintain models for these sports. It’s their job to stay on top of these rule changes and adjust their models as needed. But they often miss rule changes. Especially these little ones that switch back and forth within a season. 

For example, just prior to this book’s publication, we were watching a Browns-Eagles game during the NFL preseason. The Browns led 18‑10 in the fourth quarter, and we noticed a large modern sportsbook offering a three-way line. You could bet Browns, Eagles, or tie. The book had applied <u>[16]</u> ~~.~~ an extremely heavy 30 percent overround to the market 

Despite the extreme hold the sportsbook put on the market, however, they were not safe. There was still a good bet among the three! They were offering the tie at +1400. 

This would be a terrible bet using the NFL’s regular season overtime rules, which no doubt the content company responsible for the market was using in their model. But in the NFL preseason, they play no overtime. We 

******ebook converter DEMO Watermarks******* 

priced a tie at about 9 percent, making +1400 quite a good bet. As it turned out, the Eagles scored a touchdown and two-point conversion, and the game ended 18‑18. 

The runner on second base in extra innings rule change remains today a bugaboo for models pricing baseball totals. Not only does the rule get repealed for the playoffs, but we’ve noticed that many models in use in the market today simply don’t yet fully account for it. This is because many models used to price baseball derivatives have two flaws. First, they are simply out of date—again the business incentives in this industry are always to build more, more, more. New, new, new. It’s not to go back and make sure what you’ve already built is correctly priced. (The incentive to make sure your models are correctly pricing things in the first place often doesn’t exist, let alone to update it with minor rule changes.) 

Second, even when updating models, often model builders will rely too heavily on past data. Instead of simulating a game accurately, applying all the most current rules, the model will rely instead on aggregating data from the results of past games. To the extent that models incorporate data from games before this rule was instituted, they will be inherently inaccurate. 

Concretely, say you’re a content provider in charge of making baseball totals. From the market making sportsbooks, you can source a moneyline, run line, and market total. Your job is to build a model that uses these inputs to produce prices for every possible total from 3.5 to 23.5. 

Broadly speaking, there are two approaches. One, you can just look at past games with similar moneylines and totals and then count how many games finished with each final score. You then just make your prices by assuming the percentage of games that land on each number represents the correct break-even percentage. 

Or you can try to build a game simulation that uses the current rules and players. 

It’s much easier to just count up the results of past games. (To be clear, we’re oversimplifying the modeling process here to make the point.) When you count up game results, you’re likely including data from both before and after the rule change. Thus, your answers will correspond to some hybrid rule that doesn’t exist—not quite right for either actual ruleset. 

The upshot of this is that we currently see in-play MLB models get the totals wrong in games likely to go to extra innings. It’s much more likely in games that use the runner on second rule that a given inning will end 

******ebook converter DEMO Watermarks******* 

exactly 1‑1, thereby extending the game while adding 2 runs to the game total. So the higher alternate totals are often good bets as they are priced as unlikelier than they actually are. 

In 2006, there was a seemingly small college football rule change that had a major modeling impact. In the previous season, the clock would not start after a change of possession (a punt or turnover) until the first snap of the new drive. For the new season, they would start the clock as soon as the ball was spotted. 

This likely seemed like a small change to most people, and many people likely didn’t adjust their models. But this rule change has an outsized impact in the most critical part of the game—protecting a lead late game. Under the new rules, a team leading by one score with, say, two minutes remaining could punt the ball, and the receiving team would lose precious seconds between the spot and their first snap. This made punting in these situations more strategically attractive, and therefore made playing conservatively on the previous drive more attractive as well. 

This led to lower scoring second halves as leading teams were more inclined to nurse their lead and try to bleed out the clock. Had in-play betting on college football existed at the time as it does today, this would have presented some amazing in-play betting opportunities into obsolete pricing models toward the ends of some games. 

This was before the days of ubiquitous in-play betting, however, so we were limited to halftime bets. We bet under in the second half in at least 75 percent of the games that year and won almost 60 percent of them. (No doubt we ran good along the way.) While we noticed the rule change and thought it might be important, it was our friend, Jan Suchanek (who went by perpetualczech on gambling social media and internet forums), who realized exactly how important the change would be, and who pushed us to lean into the angle to the maximum from the beginning of the season. 

Jan was particularly good over a very long time at picking up on angles like this, and he was generous in sharing his insights with us throughout the years. Unfortunately, Jan passed away recently, and we wanted to share this story here to memorialize him and his many contributions to sports modeling and betting. Our readers who believe in eternal energy will understand. 

Little rule changes like this one happen all the time, and there will always be opportunities to be one step ahead of the modelers to identify the 

******ebook converter DEMO Watermarks******* 

most critical impacts the change will have on the game and therefore exactly which bets are most likely to be affected. 

### Angle #7. Using handicapping services 

This one is a big can of worms, but we have to talk about it. Handicapping services (also known as “tout” services) have a terrible (and well-deserved) reputation. This is the “pay us money and we’ll tell you what to bet” kind of thing. 

In the past, most of these were outright scams. The few that weren’t, for the most part, weren’t profitable for the subscriber for various reasons. 

One simple and logical line of thinking put the sword to them. “If your picks are winning, why don’t you bet them instead of sell them?” 

In 99 percent of cases, the honest answer to that was, “They aren’t winning. I just make shit up.” 

The rare exceptions to this rule ran into another logical problem. “If your picks are winning, then the moment you release them, your customers will bet them, and in response the line will move until the value is gone. So only your very fastest-fingered customers will get to actually bet your picks.” 

This logic was also mostly sound. 

Together, this basically added up to “Touts? Just no.” 

With the advent of modern sportsbooks in the United States, the situation is now slightly different. The overwhelming majority of people selling sports picks are still full of shit, of course. That hasn’t changed. Anyone can pretend. 

But there now exists a genuine logical reason for winning pick sellers to exist—and for customers to buy the picks and get value for their subscription fees. Here’s how it works. 

Modern sportsbooks offer thousands of bets. At any given time, a lot of them are good bets. Once a person gets the hang of finding the good bets, that becomes the easy part. The hard part is to get your money down on the good prices. Modern sportsbooks know their menus are full of vulnerable lines, so they’re extremely cautious about letting anyone bet a lot of money. 

That’s the answer to the first logical problem above—“If your picks are wining, why don’t you bet them instead of sell them?” The answer is that 

******ebook converter DEMO Watermarks******* 

one person (or even a small group of people) really aren’t allowed to bet much at these sportsbooks. You bet these for a while, they win, then your account gets restricted, and you’re out of action. 

On the other hand, a lot of people, not working together, but who all subscribe to the same service can get much more down on the same plays. But then we run into the second logical problem from above, “The moment people bet the plays, the line will move, so only the very fastest will get down.” 

Now that you understand how the sportsbook content ecosystem works, you should see that this is not necessarily the case in the new world where modern sportsbooks book most of the action. 

In the past, the most reliable place to bet winning plays was at a market making sportsbook. These were the only ones that would not restrict. So let’s say there was a tout service that had a good reputation for selling plays that won. The moment a play was released, people would rush to get as much down as they could at market making sportsbooks, and that’s why the line would move so fast. All the subscribers were fighting over the same few clicks at one or two obscure sportsbooks. 

Now there are new, massive, obvious places to play the plays. These are not market making sportsbooks. One book might move their line, but that still leaves all the others. 

Of course, the lines will still move eventually if the plays indeed do win, but the total ability of the market to absorb the action has increased enormously. 

This is most easily explained with an example. Let’s say there’s a tout service that specializes in NFL player props. Net rushing yards, total receptions, those sorts of bets. 

Say the service releases Robert Poindexter over 25.5 rushing yards at ‑110. There are two market making sportsbooks that offer this market. The moment the service releases the play, the first customers are clicking on that over 25.5 yard bet at the $500 maximum limit at each market making sportsbook. The automove software at those books immediately moves the line to ‑120 for the next bet. And then on the next click, it moves the line to 26.5 yards. Then 27.5 yards. And so on. After just a few clicks (this all happens within seconds), the released play no longer exists. 

Other, non-market making sportsbooks that follow the market makers here might accept a few bets at the old line before they get the update. But 

******ebook converter DEMO Watermarks******* 

the total amount of money worldwide that it is possible to bet into the released line is tiny. For the sake of argument, maybe it is something like $10,000. (It’s impossible to know this sort of figure exactly.) 

Today, there are huge companies newly taking bets on this market. These books don’t automove on bets the way the market making books do. For player props, they may receive the markets and prices from a thirdparty content provider, and they may not move their price on it (regardless of the betting) until the content provider updates the line. 

It’s possible for every customer of the service to get a bet on (so long as they are reasonably quick about it). 

But why wouldn’t the owners of the service just hoard all the plays to themselves? It’s hard for one person to get a lot down at modern sportsbooks. It’s much more feasible for many people to each get a little down. The owner of the service might have the choice between getting one small-to-medium-sized position on every released play or selling the play and allowing perhaps a few hundred people to each get a small position on every play. 

The deep pockets and large customer bases of the modern sportsbook theoretically allow niche handicapping services to operate in a way that makes economic sense for both seller and buyer. 

To be clear, this is the exception, not the rule. The vast majority of people, groups, and services that sell picks are selling garbage. 

Having said that, here are three services that have a reputation for offering real value to subscribers. 

**Establish The Run.** This service specializes in player props, and they do excellent handicapping and projection work. The key to making good player prop lines (in football and basketball in particular) is to estimate how much usage each player is likely to get in the game, and ETR does a particularly great job on that. 

**Right Angle Sports.** This service has a long (predating the modern sportsbook invasion of the United States) and documented history of delivering value. Particularly look at their college basketball service. With hundreds of teams, this is a sport where just doing a good job on the information work to keep track of who is playing, who isn’t, and so on is enough to consistently stay ahead of the pack. 

**Unabated Sports.** This is a how-to site with tools that also has a concierge picks service. It’s a newer site, but the people who run it have a 

******ebook converter DEMO Watermarks******* 

good track record and reputation. 

Speed is still important when using any of these services. The lines will move after they release plays, and you won’t be able to bet them. But there is more opportunity today to get good bets down if you act quickly after a release than there has been in the past. 

You may also get yourself flagged as “undesirable” if you hop on these releases too often. With everyone clicking the same bet at the same time, traders will notice. If the traders decide that they’re being consistently beaten by a particular service, they may resort to restricting all of their bettors who are apparent service customers. The best bet for longevity is to hide the signal under a mountain of noise. Following too many service releases may be too obvious a signal and get you pinched. 

Nevertheless, the economic viability of legitimate pick services has improved due to the modern sportsbook invasion, and more legitimate ones may spring up in the future. So, while you should approach this entire industry with skepticism, also keep your mind open that some might provide value as well. 

### Angle #8. Mispriced parlay correlation 

Parlays are the modern sportsbook’s favorite bet type. Partly because recreational bettors tend to love them. Partly because of that accounting quirk where hold percentage gets calculated based on only the original bet size and not the implied (larger) betting volume of the parlay. And partly because, well putting those two ideas together, parlays increase the betting volume of recreational players. 

Classic “off the board” parlays are intended to be permitted only on logically independent bets (e.g., each leg is a bet on a different game), and the payout is calculated by multiplying the payouts of the individual legs. The math works as if you rolled over the winnings from each leg into the <u>[17]</u> ~~.~~ next leg 

Since modern sportsbooks love parlays so much, they don’t want to restrict your leg options to only logically independent bets. Their ultimate product goal is the “everything parlayable” menu—combine any set of bets at all no matter their logical relationship into a parlay. 

******ebook converter DEMO Watermarks******* 

This flexibility is incredibly player friendly. What bettor wouldn’t want to be able to parlay any set of bets on the menu? 

But it’s quite the mathematical challenge from the sportsbook’s side. They have to correctly estimate the correlation factor between any two propositions (or, acknowledging the full complexity, any open-ended set of propositions) and then present odds to the player based on this estimate. 

And, from a user experience perspective, they have to run that calculation in milliseconds, so the bettor doesn’t have to sit there and wait for some computer to crunch a bunch of numbers before being offered a price. 

This is very hard. 

To be clear, if you want to bet that Patrick Mahomes throws over 3.5 touchdowns and that the Chiefs win by more than 9.5 points, the sportsbook has to do a bunch of math in the background to offer you a reasonable price. The book may have a ready-made price on over 3.5 touchdowns and another ready-made price on winning by more than 9.5 points (perhaps they get these prices from a content feed). But there’s no simple way to combine those two prices to get the parlay price, because the two outcomes are correlated. 

If you know that the Chiefs have won by more than 9.5 points, that knowledge makes it more likely that Mahomes has thrown for more than 3.5 touchdowns than if you didn’t know that. And vice versa—if you know Mahomes has thrown for more than 3.5 touchdowns, that knowledge makes it more likely that the Chiefs have won by more than 9.5 points. 

That much is obvious. What’s not obvious is by how much more? 

To solve this problem, as we described earlier in the book, sportsbooks sometimes use simulation models. They simulate the game a number of times, and then they count in what percentage of simulations all the outcomes occurred. They use that percentage to estimate the odds, they take on some healthy amount of hold, and they offer the price to the player. 

But simulations are hard. When you’re trying to simulate, say, a football game, it’s very easy to miss some of the details. 

Anyone who plays fantasy football knows well that skill position players are used in different roles, and these different roles tend to produce divergent stat lines. Some receivers get a lot of targets every game, but nearly always on short routes. Other receivers get one or two targets a 

******ebook converter DEMO Watermarks******* 

game, but they are usually on go routes and when completed tend to produce long gains and touchdowns. 

Modern sportsbooks that want to offer single game parlays that permit you to parlay player props (and they all want to offer this) will have their hands full here. The correlation between number of receptions and number of touchdowns is different for every single player in the league. 

Say a game is over and we tell you that fourth year wide receiver Perry Snodgrass caught four passes today. Your job is to tell us the chance he scored a touchdown. 

The correct answer can vary from very low to very high depending on how the team uses Snodgrass. The single game parlay model’s job is to come up with a credible answer to this question for every relevant player in the league. 

This is a difficult modeling task—and the more flexibility the sportsbook wants to offer the bettor (e.g., they want to let you parlay exact number of receptions with exact number of touchdowns) the harder it is. 

This is the thing to remember about single game parlay products. The more flexibility they offer the bettor, the more precise the modeling job they have to do to get every single thing right. 

You can pick these products apart by asking the general form of the question we asked above about Perry Snodgrass. “If we tell you that X happened, then what is the chance that Y occurred?” Where X is any option on the menu. Look at all the extreme outcomes as possible Xs. The 130 team points scored in NBA. The 8 team goals scored in hockey. (The goalie probably gets pulled for his backup in this game, for example. Maybe there’s a goalie player prop you can parlay with this one.) 

Consider what may be correlated with a quarterback interceptions prop. Cody McBrodie is the starting quarterback for the Cardinals in their game against the Rams this week. If you select over 2.5 interceptions for Cody as one of your parlay legs, what does that say about the game script? If Cody throws three picks, likely the Cardinals are losing. Your first thought might be to parlay that leg with a Rams point spread bet. 

But there’s a decent chance the model does okay here. The single game parlay backend model may have its flaws, but it probably has “incerceptions bad” figured out. So take the logic one step further. 

If the Cardinals are turning the ball over, they aren’t kicking field goals on those drives. Check the pricing on “over 2.5 Cody interceptions” and 

******ebook converter DEMO Watermarks******* 

“under 1.5 Cardinals field goals.” Compare it to “over 2.5 Cody interceptions” and “over 1.5 Cardinals field goals.” If the model gets this correlation right, then you’ll see the under field goals price will be substantially shorter than the over field goals price. 

Let’s say the model gets this relationship reasonably correct. Take the logic another step. If the Cardinals are likely losing due to the turnovers, then they obviously aren’t likely winning. What things tend to happen when the Cardinals are winning? Robert Poindexter is their first and second down running back, and when the Cardinals are ahead they tend to hand the ball to him to chew up clock. When the Cardinals are behind, Poindexter doesn’t get much usage. 

Look at the “over 2.5 Cody interceptions” prop paired with the “under 12.5 Poindexter carries” prop. Compare that price with how it prices “over 2.5 Cody interceptions” with “over 12.5 Poindexter carries.” There is a strong logical relationship here, so the under carries price should be much shorter than the over carries price. There’s a good chance, however, we are now one step beyond the logical horizon of the pricing model. 

The great thing about these single game parlay widgets is they give you instant pricing feedback. You click legs in, and you immediately get a price. It lets you brainstorm these logical relationships, click lots of things in and out, and really play with it. 

It’s nearly impossible that whoever built the model that powers the product thought of everything. And even if they did think of everything, that “everything” also has to get maintained before every game. Even if they are modeling Poindexter’s role on the Cardinals well, maybe he gets traded and ends up in a completely different role. Someone on the content provider side has to keep track of that and update it accurately. 

It’s nearly an impossible job for them to do this without making errors and oversights. 

The other great way to use single game parlay products is to exploit the fact that parlays magnify bet volume. This allows you to get potentially large amounts down when you find either a bad price or a modeling flaw without drawing too much unwanted attention to your action. 

An example of the potential for this came up during the Mexico City MLB series in April 2023. On April 29 and 30, the Giants and Padres played a two-game series in Mexico City. 

******ebook converter DEMO Watermarks******* 

Mexico City is a high-altitude city—about 7,350 feet above sea level, or about 2,000 feet higher than Denver, which is MLB’s highest home city. Baseballs fly farther at high altitude, and the effect is non-linear. 

To compensate for this effect, they built Coors Field in Denver with deep outfield walls to prevent too many home runs from being hit there. Whereas the park where they played the series in Mexico City, Alfredo Harp Helú Stadium, has more typical MLB dimensions. 

This suggested that a lot of home runs might get hit. Exactly how many, no one really could be sure. 

In the past we’ve done some physical modeling of ballparks to predict home run rates, but in doing so we realized that there’s more to it than just altitude, temperature, and the outfield wall dimensions. It’s essentially impossible to nail down precisely how easy or hard it will be to hit home runs in a new ballpark without first gathering some data from a number of games played there. 

But it was reasonable to assume that scoring would be up, and so bettors at market making sportsbooks bet the game total up to 15.5, which is an unusually high total for an MLB game. (For comparison, the total for the game in Denver on the same day was 12.) 

Well, that game ended Giants 11‑Padres 16, and an incredible 11 home runs were hit. 

The next day, the total got bet all the way up to 19.5. Collectively, the betting community revised their estimate for the total up by four whole runs (an enormous number in baseball) based on just the one game played. 

Is 19.5 a better estimate than 15.5 was for what could be expected in this park? Maybe. Probably? But more to the point, the fact that the total moved so much after just one baseball game reiterated what we said above—no one really had a clue. Everyone, including the sharpest baseball bettors in the world, was just throwing darts. 

Enter, modeling error. 

So again, here’s the situation. There’s a baseball game being played. Everyone has the sense that a lot of runs might get scored. Absolutely no one has any clue specifically how many are likely. Massive uncertainty. 

This game is attracting lots of interest. Not just from winning bettors— the situation is well-covered in sports media. So the big modern sportsbook brands want to offer a lot of bets on the game. Not just the game total, but all the regular stuff too. Player props. Single game parlays. 

******ebook converter DEMO Watermarks******* 

The problem for them was, this game broke the models. In particular, the uncertainty broke the models. 

Every real-world prediction has to account for uncertainty—the known unknowns and the unknown unknowns about the situation. In baseball, the known unknowns are, well, well-known. You can go to Fangraphs and get six different projections for every player in the league. Each projection represents an estimate of how good that player is—and they’re all slightly different from one another. The spread in these projections is uncertainty. We don’t ever know exactly how good any player is. We just have rough estimates. But we also know that for most players, those estimates are probably correct to within some certain tolerance. 

The same with the hitting environment. The same ballparks get used year after year. Those ballparks all see roughly the same types of weather year after year. We never know exactly how a ballpark will play on any given day, but we can make reasonable guesses and expect to be correct most of the time within some certain tolerance. 

Put it all together, and on a regular old day in a regular old MLB ballpark, we can come up with an estimate of how many runs are likely to get scored that day on average. There will be uncertainty in that estimate— but the amount of uncertainty will be familiar and consistent. 

This familiar, consistent uncertainty is relied upon as a foundational assumption when content providers build their models. They’re trying to answer the question, “If the game total is 9.5, then what is the right price for under 5.5 or over 13.5?” 

To understand the role uncertainty plays, think about two scenarios. In one, we tell you that the game total is 9.5, and we’ve arrived at that number because thousands of MLB games have been played under objectively similar conditions. In those objectively similar conditions, about half the games went over 9.5 and half went under. In addition, about 20 percent of those same games went over 13.5. 

In the second, we tell you, “The game total is 9.5, but the game features the Savannah Bananas, and no one’s ever seen any of these players before nor has anyone ever played a recorded game in this stadium. The total just happens to be 9.5 because a few Adderall-addicted nerds with more money than sense decided to bet the game, and that’s where the number landed. So maybe the right answer is more like 6.5 or 12.5. Really no one knows.” 

******ebook converter DEMO Watermarks******* 

Imagine you’re a content provider for sportsbooks, and it’s your job to list a price on over 13.5 for each game. In the first game, you go with 20 percent. And because the second game has the same total as the first, you go with 20 percent for the second game also. 

Hopefully it’s clear that 20 percent may be a decent guess for the first game, but in the second game where the “correct” total could easily actually be 13.5 or even higher, 20 percent is far too low an estimate. Because there’s more uncertainty surrounding the second game, any extreme outcome will be more likely in that game than it is in the bog-standard normal old game. 

Well, content providers made exactly this modeling error for that second Mexico City game. They took that game total of 19.5 from the market makers and plugged 19.5 into their models and then published whatever percentages came out. 

What came out of those models all the way around—from alternate game totals to player hit, total base, run, RBI, and home run props—was a stream of incorrectly low probabilities listed for the extreme outcomes. With “extreme” in this case meaning any outcome that looked more or less like a normal MLB game. 

In other words, they were telling their models, “This game is going to be an absolute home run fest, and we’re pretty certain about that!” 

When they should have been telling their models, “Well, the betting market thinks this game could be a home run fest, but bettors don’t really have a clue in this case, evidenced by the fact that they’ve adjusted their estimate wildly from just the previous day. And the previous game was indeed a home run fest, but that was just one game. So shrug?” 

In the same game parlay widgets at multiple sportsbooks, you could parlay together options that corresponded to, “This is actually going to play out kinda just like a normal MLB game,” and get very long odds for it. The game ended Giants 4‑Padres 6. 

### Angle #9. In-play data errors 

Ahh, in-play. To this point all of the angles have focused mostly on pregame betting. Which is somewhat remarkable, because when you’re in charge of a betting menu, pregame is the easy part. Pregame you have a 

******ebook converter DEMO Watermarks******* 

betting market to rely on to handicap the games for you. Pregame you have plenty of time to spot errors and check your work. Pregame information comes in slowly, and you should have systems in place to gather and react quickly to it when it does come in. 

Pregame bets are also insulated from a lot of the minute, situational concerns that otherwise could plague linesmaking. Does the Chargers coach like to go for it aggressively when down by one score in the third quarter? For the most part that sort of observation just doesn’t matter to your pregame lines. 

In other words, pregame menus should, by rights, the vast majority of the time, be nearly free from errors. They aren’t—we just wrote who knows how many pages on ways to find errors in those pregame menus—but pregame is the easy part to get right. 

In-play is a much trickier problem for the companies that produce pricing. Just getting the major markets (game moneyline, spread, total) right from the beginning of a game through the end is a difficult task. Game information comes in constantly. There are fouls and penalties and injuries and challenges. The companies that produce pricing not only have to gather information about all these things accurately and extremely quickly, but they also have to digest that information and evaluate the impact on a dime. 

Oh, the Ravens quarterback is rolling around injured after a sack? How badly is he injured? How likely is he to return? Is the injury likely to affect his performance if he does return? What is the skill gap between him and his backup? Someone needs to ask and answer these questions within seconds and get up a credible new line. 

Oh, there was a challenge? What is the relative impact of the play being upheld or overturned? How likely is it to be upheld or overturned? 

Down by two goals in the third period of a hockey game. Are they going to pull the goalie? Wait, did they do it already? 

The star player on a college basketball team just picked up his third personal foul. Are they going to sit him? If so, for how long? 

Anyone who watches sports knows that these things matter—a lot. That means they affect betting lines. Often a lot. 

You might expect that sportsbook content companies producing in-play pricing would have gathering all this information and reacting to it quickly down to a science. 

******ebook converter DEMO Watermarks******* 

They absolutely do not. We’ll elaborate on that in a moment, but one quick point first. 

Modern sportsbooks of course aren’t content with just putting up major markets in-play. They want derivatives—alternate spreads and totals—first half, second half, every quarter, bets on the outcome of every drive, every <u>[18]</u> ~~.~~ possession, every at bat 

They want player props too. And while we haven’t seen much of it yet for the big American sports, sportsbooks surely want single game parlay products as well that can be used in-game. 

Every angle that applies to in-play bets in general will apply three-fold to one of these sliced-and-diced derivative bets or micromarkets. Say you’re watching a football game and you see a flag thrown. The referee hasn’t announced it yet, but you’ve watched enough football in your life to know for sure it’s going to be an offensive holding call. 

Yes, there’s broadcast latency (i.e., you’re seeing the game on some consistent multi-second delay versus real time). But there’s every chance that you can react to that flag before the content companies do, because they don’t know it’s an offensive holding penalty yet. They should—if you know it is, they should too—but they probably don’t. 

If it’s the second quarter, however, knowing that offensive holding is about to get called doesn’t have a major impact on the full game lines. It might move the moneyline by a percent or two (maybe the team with the ball was 36 percent to win the game before the call, and now they’re 34 percent). Similar impact on the total. Not really bettable, since modern sportsbooks will put 6 or even 8 percent hold on these markets. (If the favorite is priced at 68 percent to win, it doesn’t really matter if you know they’re really 66 percent instead of 64. There’s still no bet.) 

But that penalty could move a second quarter market much harder. Or a market like “Will the current drive result in a touchdown?” An offensive holding penalty can change the likelihood of one of those bets winning or losing by well more than the 6 or 8 percent hold. 

The shorter the time frame of the bet, the more vulnerable any in-play market will be to any of the angles to come. 

Okay point made. Back to how content companies source in-play data and make lines. 

Generally speaking, content companies rely heavily on what’s called the “official” data feed for all the main sports. This is a feed of raw game 

******ebook converter DEMO Watermarks******* 

information gathered either by the relevant league, cooperatively between the league and a data company, or exclusively by the data company with the league’s blessing. 

The key idea here is that this data gathering arrangement represents a quasi-monopoly. 

Say you wanted to start a business gathering and selling game data from five-a-side pickleball. You go to a game. You bring along your tablet that you plan to use to gather information. 

And then two people, one a representative of the five-a-side pickleball league and the other a representative of the already existing data company that signed a contract with the league and that now holds the “exclusive rights” to distribute data for the five-a-side pickleball league, these two friendly folks both tap you on the shoulder and politely ask you and your tablet to get lost. 

This is the general state of affairs. We are not referencing any specific leagues or companies here—every actual real-world situation is slightly different and none fits this scenario perfectly. The important idea is that data feeds tend to lack a measure of redundancy. There is one stream of officially-sanctioned game information, and that’s it. 

And the content companies that turn that raw game data into betting lines rely heavily on it to produce their lines. 

On the plus side for this arrangement, the data feeds do tend to be fast. Relevant game information will typically come through on these feeds before you see it on the screen if you’re watching the game. (More on this time latency issue in a moment.) 

On the minus side, the lack of redundancy means human error can slip into this data more easily than if there were multiple redundant sources on equal footing, each with independent error checking. 

Types of errors in the feeds include incorrect game scores and times remaining, the wrong team listed with possession of the ball, incorrect play outcomes, plays listed as completed successfully when they’re subject to being called back for a foul or penalty. In football, commonly the ball listed on the wrong team’s yard line, such as Sooners 35 when the ball is really on the Longhorns 35. Incorrect down and distances. Incorrect shot clocks on basketball inbounds. And so on. 

If you’ve ever been to a live sports event, you know the scoreboard operator sometimes leaves incorrect information on the scoreboard for a 

******ebook converter DEMO Watermarks******* 

while before it’s fixed. It’s the same vibe in some of the data feeds. 

If you’re trying to make betting lines from these data feeds, it’s a tricky business because you never know when an error might come through. Content companies will typically have some layer of error detection and correction. But an eagle-eyed observer will also see plenty of in-play lines that are clearly made with the wrong game state, and this wrong game state may have come ultimately from an error in the game’s data that didn’t get caught. 

Potentially any bit of information in any sport could be in error and cause a bad line. But if we had to call one out as something to look specifically for, it might be the “wrong team’s yard line” one in football. It’s not uncommon for that yard line to come in on the data feed with the team flipped, and it’s also a tricky one to catch. This error can move a main market like a moneyline far enough to give you a bet, but it can really create hilarious lines on the shorter-term markets like “will this drive result in a touchdown?” If you’re watching that market and you see the breakeven percentage of the line pop from 25 percent to 50 percent after a short first down in a team’s own half, this data error could be the cause. 

A tip here is that some leagues have fewer errors and more game-togame consistency than others. For the leagues with more errors, they also tend to have less game-to-game consistency. Some games in these leagues will be done well and be relatively error-free, while other games will be a mini-disaster. If you watch a game and notice, say, two weird lines already halfway through the first quarter, perhaps stay focused through the rest of that particular game. You may continue to see errors throughout. 

For the inconsistent leagues, don’t make assumptions about which games will be done well and which ones won’t. One might assume that the high-profile games will be done well while lower profile games might slip through the cracks, but we’ve seen some high-profile games with extremely troubled data feeds. It can be tempting when viewing from the outside to try to apply method to such observations when it can be just madness. 

Back to the latency issue. Video feeds tend to lag real life. This lag can vary from a few seconds at the fastest to upwards of a minute. It goes without saying that if you want to find in-play betting opportunities, it’s to your benefit to find the fastest video feeds you can. Over the air TV differs from cable TV differs from satellite TV differs from internet streaming. And the internet streaming options often differ most widely among 

******ebook converter DEMO Watermarks******* 

themselves. Some streaming is just about the fastest feeds you can find. While other streaming is delayed by a minute or more. 

This will all change over time as well, with feeds likely getting faster (lower latency). Just keep three things in mind. 

First, you want to find the fastest feeds you can. Check the buffering settings on internet streaming feeds—sometimes those are the cause of delay and you can tweak those and speed up the feed considerably. You can determine which of two feeds is faster obviously just by watching them simultaneously and choosing the one that isn’t perpetual instant replay. 

Second, you want to stopwatch it so you know exactly what the delay is (in seconds). You can do this by watching for the timing of line changes at your target sportsbook and then counting the delay between when you see the line change and when you see the line changing event on your video feed. As a simple example, say you’re watching a football game. There’s a kickoff, a touchback, and a TV timeout. The lines stay stable during the TV timeout. 

As the game comes out of timeout, watch for the first betting line adjustment. Then count—one Mississippi, two Mississippi, three Mississippi—how many seconds come between that line change and the time you see the runner get tackled at the end of the first play of the drive on your video feed. Your count will be a more accurate delay estimate if the first play of the drive is a run of the mill play, like a run up the middle for three yards. 

Then do it again a couple more times. You should get close to the same answer every time. If you do, that’s how far behind you are. Now you know. 

Third, you want to place bets only when you’re at information par with the sportsbook. That is, when nothing game-related is likely to have happened in the X seconds (what you counted above) forward in time from whatever you’re seeing on your video feed. 

In football, this is easy. Teams tend to run their offenses with predictable delays between plays. Say it’s the NFL, and the team with the ball tends to take between 28 and 32 seconds between plays. And say you know you’re about 9 seconds behind live. That gives you about 20 seconds after each play ends on your video where you can expect to be at information par with the sportsbook. 

******ebook converter DEMO Watermarks******* 

And sometimes as we mentioned above, you’ll actually be at an information advantage over the book because you’ll see something on video that won’t make it into the data feed within that 9 second latency. 

The data feeds deal in facts. The feed may or may not signal “flag thrown” the moment it is thrown in a football game. (Some game feeds will signal this relatively quickly—perhaps within the 9 second window. Some feeds will not, and you’ll have a jump on the feed. This is something you can feel out on a game-by-game basis.) 

No feeds, at least none that we are aware of, will editorialize about the flag. “Flag thrown—probable offensive holding” is not a thing. They will wait until the referee saunters to the middle of the field and announces the penalty to include the nature of the foul and its on-field ramifications in the feed. 

If you watch football regularly, you know there can be a lot more than 9 seconds between the moment the flag is thrown and the time the referee has finished announcing the nature of the foul. 

In baseball, the cadence of the play is similarly predictable. After you see a pitch land in the catchers mitt, you can probably count on some calculatable number of seconds where you will be at par with the sportsbooks. 

Basketball is the tough one. Especially the NBA. That sport is fast. Possessions are fast. The cadence is less predictable and sometimes manic. Bet in-play NBA at any point other than during a timeout at your peril. 

Hockey is also a fast sport where it’s hard for you to know that nothing has happened during your video latency period. Again, bet it while the puck is in play at your peril. 

### Angle #10. Courtsiding 

This is the angle where you continuously try to create and exploit a latency advantage over the data feed. It got its name because betting groups would place scouts at courtside for tennis matches and then, point after point, pick off the stale in-play lines for those matches since the betting group’s scouts would know the winner of the most recent point faster than the data feeds would. 

******ebook converter DEMO Watermarks******* 

For the most part, if you do this it will be extremely obvious to the sportsbook what you’re doing. And sportsbooks absolutely hate it. You’ll get your accounts restricted to nothing if you’re identified doing this faster than if you try nearly any other angle on this list. 

Look, this is the dead obvious way to try to beat in-play betting. “I’ll just go to the game and know what happened before the book does.” No shit. 

It’s not clever, and most people who do it are extremely obvious about it. Theoretically they could do it subtly and weave it gently into a more complicated betting strategy. Every once in a while you could bet smallish advantages like a medium play in football getting called back or an inningleadoff out in baseball or one two point basket in basketball and not attract attention. 

But the people who use this angle tend to get greedy and do stuff like bet every home run in a specific ballpark five seconds before it hits the feed. These bettors attract attention often after just the first bet. And after the second bet, that can be all that’s needed for a book to take action. 

This behavior may actually be considered criminal in some betting jurisdictions. 

Bottom line, don’t build your betting strategy around this angle. There are so many other good bets on the menu. This is one sportsbooks are watching for like hawks. 

### Angle #11. Situational in-play betting 

For the most part, you can assume that the content companies making inplay lines are using a fairly simple approach to their job. They’re combining three inputs to get the output lines. First, they have a model. How this works on the inside can vary, but from the outside they look the same. They take information as an input, they do some math, and they publish lines for betting markets as the output. 

Second, they have factual game information to use as an input. The score. The time remaining. The down and distance. That sort of thing. As we just described, they usually rely mainly on an externally produced data feed to provide this information. 

Third, they have “market” information. This is the squishiest category, but you can expect companies to use the lines published by competitors as 

******ebook converter DEMO Watermarks******* 

well as information from the bets they’ve already taken. They may also use risk management information here as well—if they have a lot of exposure on one of the teams, for instance, they may feed that knowledge back into the system so that future lines discourage additional action on that team. 

What they very likely won’t have is reliable, useful situational information fed into the model. This is any information about how the game is likely to turn out that isn’t factual and also likely isn’t in the “market” information yet either. 

Let’s return to one of our favorite examples—when the goalie is likely to get pulled in hockey. Say you’re watching an NHL game and the Nordiques are playing the Whalers. (You set your DeLorean to 1985 to catch this one.) The Whalers are down 4‑3. It’s the third period. You happen to know that the Whalers coach is extremely timid and almost never pulls the goalie until the very last moments of the game. 

Compared to the average NHL game, this one is substantially more likely to end exactly 4‑3. Not 5‑3. Not 4‑4 and off to overtime. 

You can fairly safely assume that whoever is making the in-play lines for this game is not accounting for this fact. Why? 

First, the model will be made with the NHL average game in mind. This is the default when building any such model. If you look at past games that are 4‑3 and count how many end 4‑3, end 5‑3, or end 4‑4 and go to overtime, and then use that to make predictions about future games, by definition you’re anchoring your prediction to the league average strategies, patterns, and behaviors. 

Second, this information about the coach is not hard, factual information. It’s an opinion or judgement about the coach. It won’t be in any data feed. 

Third, this information “might” be in the “market” information—but probably not. Why not? 

Well, for it to appear in market information, two things must be true. First, other people must be betting this same angle, and they must have done so before you. Possible. But there just aren’t that many sharp eyes glued to the final ten minutes of a random hockey game played in 1985. Nor to a random hockey game played today, for that matter. Newer bettors tend to overestimate how much sharp play there is, and how thoroughly sharp players grab all the available angles. 

******ebook converter DEMO Watermarks******* 

There just isn’t that much “sharp action” out there, especially not in a non-top tier sport like hockey (some of our best friends work in the NHL— sorry y’all!). And especially not in-play. This sort of angle, while obvious to someone who follows hockey closely, will otherwise mostly just pass unnoticed and unbet. 

Second, even if the signal appears in the market information (i.e., sharp people are betting this), the people who make the lines have to extract this signal from the noise of all the other betting and then use it to adjust the model outputs. This part of the “is this angle accounted for in the lines?” parlay is even less likely to be true than the first part. 

Bottom line is you can probably bet that under 0.5 more goals profitably for the rest of the game. And the later into the third period you can grab it, the better the bet is likely to be. And you can probably continue to bet it every time the Whalers are down in the third period for the rest of the season. 

A few years ago, the Brewers had an utterly dominant relief pitcher named Josh Hader. He was arguably the best pitcher in the league. And the Brewers used him in a very predictable way. The team would rest him almost without fail after using him on previous days, making him unavailable that day. And on days he was available to pitch, he would always be brought in if the game situation called for it. 

About halfway through a Brewers game, you knew if it was likely to be Hader time or not. You could profitably bet on the Brewers and under the total runs if it was Hader time. And against the Brewers and over the total runs if it was not. Because the model that made the lines was oblivious to the Hader time phenomenon. This angle was available over and over throughout the season, with the in-play lines never adjusting to it at any sportsbook we were aware of. 

If you’re watching a college basketball game and a team’s two best players get into foul trouble early, yes, you can bet that. It’s very unlikely the lines are accounting for it. It’s unlikely the lines will ever “catch up” to it either, so if this continues to be true or if one of those players ends up fouling out, it’s game on. 

This is particularly true in a sport like college basketball where there are a zillion teams, twenty zillion games, new players come and the old ones go every season. It’s extremely hard for a content company (whose business 

******ebook converter DEMO Watermarks******* 

incentives are pointed in all the opposite directions to this) to track the significance and availability of every player to every team. 

It behooves us at this point to mention that we have founded a content company whose strength is producing good in-play lines. We have gone to great lengths to do as good a job as practically possible to allow our models to incorporate situational factors like these into our lines. So, for example, you cannot beat our lines with the Hader time angle like you can the lines produced by many others. 

But you might get us on the college basketball one—there are just so many teams and players to keep track of. You should know that we indeed attempt to do just that. But there’s no way for us to be anywhere close to perfect during the chaos of a college basketball Saturday. 

Our company’s in-play lines, however, are just one among many in the marketplace. You should do research into your target sportsbook brands and find out where they source their lines for all of their products. 

Two other quick situational concepts. First, situational factors often tip the scales the most in late game situations on bets where the outcome of the game doesn’t hang in the balance. Late game situations are the ones where the coach’s decision-making tendencies come to the fore. If you know of a particular outlier tendency of one of the coaches, there’s a good chance you have a bet. This can be the tendency to put position players in at pitcher in baseball. The tendency to go for two down 14 points in football. The tendency to foul or not foul down 8 or 10 points in basketball. The tendency to shift to a defensive strategy when ahead by two or more goals in hockey or not. Things like that. 

If you see the examples we just listed, hopefully the second part, about the outcome of the game not hanging in the balance, makes sense. The tendency to foul or not foul down 10 points in a basketball game doesn’t really affect the outcome. The team down 10 is likely to lose no matter what they do. Perhaps the willingness to foul gives that team a fraction of a percent better chance to win. Not a big enough chance to bet on. 

But it can significantly affect the chances on a bet like +9.5 or +10.5. Or on a total bet. These are the bets you’ll often be targeting with situational angles. Not moneylines. 

In football if a team is down 14 points in the fourth quarter, they need to score two touchdowns. If they score the first touchdown, they can either kick an extra point and be down 7, or they can go for two and be down 

******ebook converter DEMO Watermarks******* 

either 6 or 8. The team has a better chance to win the game if they choose to <u>[19]</u> ~~.~~ go for two But it’s not so much better a chance that you are likely to have an angle betting the moneyline on a team that likes to go for two or against the team that doesn’t. 

Either way, down two touchdowns, they’re probably gonna lose. A 9 percent chance to win might become 9.5 percent or 10 percent with a coach making better decisions. Not bettable. 

But going for two (or not) has a drastic impact on the chance that the +6.5 or +7.5 bets will win. The coaches that kick the extra point are likely to lose the game by exactly 7 points, meaning a +7.5 bet will win and a +6.5 bet will lose. And therefore, for that coach, there should be a large price difference between those options. 

The coaches that go for two are likely to lose by either 6 or 8 with equal measure, but rarely by exactly 7. So for those coaches, the price of the +6.5 and +7.5 bets should be nearly identical. 

In either case, the +5.5 and +8.5 bets represent bets on “Will the trailing team score twice?” and “Will the trailing team not catch up by even one touchdown?” respectively. 

So this coaching tendency meaningfully affects only the price of the +6.5 and +7.5 markets, but it has a drastic effect on the correct price of those two markets. It’s probably a content company’s best policy not to offer these two specific markets (the +6.5 and +7.5 markets) at all in this situation. Because if they do want to offer these markets, they have to get the coach’s tendency correct. Many NFL coaches will go for two nearly every time in this situation. Other NFL coaches will nearly always kick the extra point. And some, at any given moment, will be in transition between one strategy and the other. 

If you study all 32 NFL coaches and know which is which, you can have a massive situational advantage should this arise in a game. (It is of course common for a football team to be down by 14 points.) 

Oh, but perhaps your sportsbook has outfoxed you by refusing to offer +6.5 or +7.5 bets during this key moment. They may not offer the bet on their menu, but have you checked the secret menu? That would be cashout. 

Modern sportsbooks want you to be able to cashout your bets at any and all times. Recall from earlier that cashout is just another in-play bet. So if you have an existing bet at ‑6.5 or ‑7.5 then cashing out those bets is functionally identical to placing a new bet at +6.5 or +7.5 on the other team. 

******ebook converter DEMO Watermarks******* 

Here’s the angle (with cashout) spelled out beginning to end. As of today, the rule in the NFL is most coaches will kick the extra point in this situation to go down 7. But that is changing over time, as more and more coaches learn the math that says going for two is preferable. But pricing models tend to use backwards-looking league averages, and the backwardslooking league average here is that a team down 14 in the fourth quarter will be likely to lose by exactly 7. 

The coach who does go for two will be the exception to the rule, and therefore will be the one more likely to produce good bets for you. Models price average. This coach is not average. 

You’re watching the Packers-Bears game. The Packers have a coach who always goes for two down 14. In the first quarter, the Packers quarterback takes a sack, and you think after watching the first instant replay that he might have a high ankle sprain and be done for the game. So you want to make a quick Bears bet. (You could be dead wrong, of course. The Packers quarterback may miss one down and then lead his team to a crushing victory. This is gambling. You’re going to be wrong sometimes. Gambling is also a skill. The better you are at playing instant replay doctor, the better you’ll be at betting in-play football.) 

The existence of this go for two down 14 angle suggests you might look to bet the Bears at specifically Bears ‑6.5 if you can find that line among the alternatives. This is true if and only if you know your sportsbook is unlikely to offer a Packers +6.5 line if they’re down 14 points in the fourth quarter and if you are familiar with your sportsbook enough to know they’ll be willing to cashout your bet at that point. 

But assuming those two things are true, then prefer the Bears ‑6.5 bet to betting the Bears on the moneyline or at other point spreads. (Again, you’re betting the Bears in the first place for a completely different reason—the perceived injury.) 

Okay, so you have your Bears ‑6.5 bet. Fast forward, and sure enough, it’s the fourth quarter and the Packers are down 14 and driving. (For what it’s worth, the Packers starting quarterback is back in the game.) 

See what the sportsbook offers you as a cashout for your Bears ‑6.5 bet. They might be overvaluing it significantly. The model that prices the cashout offer is likely based on league average behavior. And league average behavior is to kick the extra point to go down 7 points on a touchdown. 

******ebook converter DEMO Watermarks******* 

The Packers behavior will be to go for two to go down either 6 or 8. Even with the very healthy hold the sportsbook places on cashout offers, they could easily be giving you an extra five cents on the dollar or more due to this subtlety. The bonus value you can get from cashing out will grow the closer the Packers get to the end zone on that drive. If you were somehow allowed to cashout with the Packers on the 1-yard line, you’d get max value by selling back your ‑6.5 bet. Because that is the moment where the sportsbook is most incorrect about the chance the Packers lose by 7 versus 6. 

The second quick situational concept (okay that previous one didn’t end up being very quick—point conceded) is that you can sometimes let the market handicap the situational factor for you without actually understanding it yourself. 

We said before that in-play lines take “market” information into account as an input, but then went on to specify that often the content companies aren’t particularly good at using that information. This effect can be seen most easily shortly after halftime. 

Halftime is the one time during a game where those pregame price discovery market making forces take over. The bigger betting groups often bet halftimes, but not other times during a game. Market making books take halftime markets seriously. You’ll see the “markets opened, markets bet, lines moved” process happen quickly in the first minute or so of a halftime. 

Content companies follow this movement and, therefore, by definition, they are incorporating market information well into their in-play lines. 

But a funny thing happens sometimes shortly after halftime closes. The content companies sometimes “forget” about this deluge of market information from halftime, and after the first few minutes of the second half, they go back to producing lines that lack input from the halftime markets. It will be as if the halftime betting never happened. The lines never moved. It’s back to just factual game information and uncalibrated mathematical model. 

Here’s a quick example. Say it’s a college football game, and the halftime market opens giving the Horned Frogs a 64 percent chance to win. Within a minute or so, that line moves all the way down to 60 percent. 

Why did it move? It moved for the same reason pregame markets move —nerds who are good at this generally wanted to bet against the Horned Frogs at the listed price, and they mashed the bet button enough times at 

******ebook converter DEMO Watermarks******* 

market making sportsbooks that the price moved. (Again, this movement need not represent much actual money bet. The skyscraper is still built on top of a toothpick.) 

Anyway, the price moved from 64 to 60 percent and then stopped. The nerds were content with this new price. 

The marching band plays. The dance team dances. And the second half begins. A whole lot of nothing happens for the first couple of minutes. The Horned Frogs should, logically, still have about the same chance of winning the game after the couple minutes of nothing as they had at the beginning of the half. 

But the in-play lines have mysteriously popped back up to 66 percent on the Horned Frogs. Why? 

Because the content companies making the lines tossed all that juicy halftime market information into the garbage can. Why? 

Your guess is as good as ours. But this is a thing they do. 

Feel free to bet against the Horned Frogs at this inflated price. Do you know why the nerds bet the line down from 64 to 60? Nope. Do you have to? Also nope. Chances are it was some situational factor that whoever opened the halftime market hadn’t taken into account. Betting groups have a short list of these situational factors that they keep track of during the first halves, and they bet halftime lines that don’t correctly account for them. 

You don’t have to know why. You just have to know what happened. The nerds liked one side enough that the line moved significantly. The content companies dutifully followed this line movement because if they didn’t, they’d get arbitraged into oblivion. 

The moment the half started again, they forgot all about that and set their algorithms back on autopilot. You get to bet the situational angle without knowing what the angle is. Just that it must be something, and that the inplay lines now aren’t accounting for it. 

Angle #12. In-play props and micromarkets 

These are relatively new offerings for American sports. These are markets like player prop markets (yards, completions, points, rebounds, and so on) 

******ebook converter DEMO Watermarks******* 

offered in-play. They are also markets on the next drive, next play, next at bat, next pitch, next possession, next goal. 

“What will be the outcome of the current drive?” “Who will score the next touchdown?” “Will the next play be a run or pass?” “What will be the outcome of the next at bat?” “Will the next pitch be a ball or strike?” “Who will score the next goal?” 

Stuff like that. These markets are all made by content companies with models. Anything new that you see—like one day you’re browsing the betting menu and you notice a whole new set of in-play prop markets for five-a-side pickleball—is likely to be a specific product developed and operated by a single content company. That is, if you see five-a-side pickleball in-play prop markets pop up at a second book in a month’s time, chances are it’s the same content company that is providing it to both sportsbook brands. 

Any new, model-based sports betting content is likely to be, let’s say, rough around the edges. 

For example, theoretically speaking, you might see a “Will the next down be a run or a pass?” bet at your favorite sportsbook. And you might notice that the line is the same on 1<sup>st</sup> and 10 at the beginning of the second quarter as it is on 1<sup>st</sup> and 10 at the beginning of the fourth quarter even though in the second case, the team with the ball is up two scores and much more liable to run to grind clock. 

The way this new content comes to market often goes like this. The sportsbook wants to offer the market. A content company promises to provide it. The sportsbook and content company come to terms. Once the business terms are inked, the primary concern on both sides is integration— basically making sure the software works. The lines get sent, the bets are bettable, the bets get graded, the bettors get their money correctly on winning bets, and so on. No one on either side tends to be particularly worried at this point about the quality of the pricing. 

If no one on either side is particularly worried about the quality of the pricing, then you can expect it to be, well, rough around the edges. 

This is to say that if you can think of an angle to attack the pricing with, the angle probably works. Does the current pitcher happen to walk three 

******ebook converter DEMO Watermarks******* 

guys every inning? “Next pitch is a ball” is probably a good bet. Are you watching Princeton basketball do nothing but sit back and shoot threes? “Next possession ends in a three pointer” is probably a good bet. 

You have to be a little careful here, because these markets often have enormous amounts of hold placed on them. Calculate the market overround (recall from earlier—convert all odds to break-even percentages, add them up, and the amount more than 100 percent is the overround). You may see 20 or even 30 percent overrounds, which means that if you were to throw darts at the market you’d lose extremely fast. 

Fortunately, you aren’t throwing darts. You’re using your brain. If you aren’t sure if your angle is strong enough to overcome the overround, watch the prices flash by some more and do some back of the envelope math. 

You should be able to reverse engineer the model fairly easily. We hear you protest already, “Maybe you can reverse engineer a model easily…” 

Just trust us. A lot of the models that drive these new flash props type of offerings are really, truly not very polished. If you just watch games for a bit and observe it price things for a while, you can pick up on what it’s doing. 

And here’s what we mean by back of the envelope math. Say there’s a baseball hitter whom you know almost never swings at the first pitch. And a pitcher who’s new to the league and has a control problem. You look at the “ball or strike” market at your favorite sportsbook and notice that it prices the first pitch of every new at bat pretty closely to one another. So you assume this is a “league average” price. Then you calculate how far off league average this particular hitter/pitcher matchup is likely to be. 

You Google “how often does the average MLB hitter swing at the first pitch?” and some article says 30 percent. Good enough. Your hitter doesn’t literally swing at zero percent of first pitches, so let’s call it 5 percent of first pitches. If the hitter swings, it’s guaranteed to be not a ball. 

Let’s assume the not swung at pitches will be 50‑50 balls and strikes. This is not correct. And it’s complicated by the fact that MLB hitters will preferentially swing at pitches that otherwise would have been called strikes. But we’re doing back of the envelope math here—if it comes out close, then you can refine your math with such nuances. 

So the average first pitch of an at bat will be 30 percent not balls, and the remaining pitches will split 35 percent balls and 35 percent strikes. 

******ebook converter DEMO Watermarks******* 

For this batter, the first pitch will be 5 percent not balls, and the remaining pitches 47.5 percent balls and 47.5 percent strikes. So this nonswinger will get an extra 12.5 percent balls (additive) than the average MLB at bat. 

If the overround on this market is less than about double this number (25 percent) then you’re in the ballpark to autobet this situation. It helps your cause here that the pitcher has a control problem—this tendency to throw wild pitches will counteract the “MLB hitters preferentially swing at strikes” wrinkle that we didn’t account for above. 

What’s the point of this? The goal is to gauge the size of the angle compared to the amount of hold the sportsbook has placed on the market. We’re pretty sure the angle “works” because the model seems to be pricing all first pitches about the same, regardless of the first pitch swinging tendencies of the hitter. We just don’t know if the effect is large enough to overcome the overround. If the overround is 10 or 12 percent, then it’s pretty clearly fine to bet. If it’s 40 percent, then the angle is probably not good enough. If it’s 25 percent, then you might have to do some more accurate math to decide whether the bet is good or not. 

Anyway, in-play props are the Hot New Thing in the industry, and you can expect to see plenty of new offerings come to market over the next few years. Assume anything new is full of holes in the math and then set about to find them. It shouldn’t take long. 

******ebook converter DEMO Watermarks******* 

# PUTTING IT TOGETHER 

Learning to beat modern sportsbooks is a two-step process. The first step is to learn how to find the good bets on the betting menu. As you learn to do this, start with the low-hanging fruit. Look for bets using these criteria. 

**The prices are made by models not by price discovery.** It’s certainly possible to get good enough at this that you can consistently find good bets among the main pregame markets for the major sports. But that is more of an end boss goal, not a newbie goal. The bets priced by models are much easier pickings. Fortunately, most of the bets on a modern sportsbook menu are priced by models, not markets. Examples include. 

- **Nearly any in-play bet.** Halftime is the notable exception here, but otherwise, once a game starts, you’re looking at modeled prices. 

- **Any single game parlay bet.** This bet type requires an algorithm to do the correlation math. 

- **Most player props.** There is some market (which will likely grow in significance over time) for the most “core” player prop markets. Player yard totals markets for football, player points markets for basketball, starting pitcher strikeouts markets for baseball. Pretty much all other player props will be priced by someone’s model. 

- **Most team props** . These are most of the other bets on a game that aren’t the core point spread, moneyline, total, and the first half versions of these markets. Notably, this includes most alternate point spread bets, alternate total bets, any team yardage bets, bets on specific scoring types (touchdowns, field goals, three pointers, home runs, and so on). 

******ebook converter DEMO Watermarks******* 

**The pricing relies on falsifiable assumptions.** You want to be able to enumerate the assumptions that go into the price and then also determine whether that assumption is valid or invalid. Examples include. 

- **Field goal totals bets.** One assumption embedded in these is that the place kickers will perform to a certain standard. In an NFL game with a total of 51, total field goals for the game under 3.5 ‑150 could be priced well. While in a college football game with a total of 51, under 3.5 ‑150 could be an extremely good bet. Or, possibly, not—if the college place kickers are particularly good. The skill is to look at the bet and say, “Okay, that price makes an assumption about how good the place kickers are. Is that assumption correct for this game or not?” 

- **In-play college basketball second half bets.** More than in other team sports, star basketball players have outsized importance to their teams. A key assumption underpinning any in-play basketball line, therefore, is the specific number of minutes on the floor these key players will get for the remainder of the game. During your run of the mill college basketball game, you’re fairly safe to guess that the in-play model is assuming “whatever is average” for these minutes. This can be roughly correct if all the key players are available. But if an important player left the game injured or fouled out early, it can be an incorrect assumption. 

- **Baseball home run props** . There are two major assumptions that go into all bets on baseball home runs. One is the “home run environment.” This is basically “how easy (or hard) it is to hit a home run in this game.” Variables here include the architecture of the ballpark, the weather, how the baseballs themselves are manufactured, and how the balls are stored. These are, indeed, all variables, and to make a price on any home run related prop requires making assumptions along all these dimensions. Second is “how good are these hitters likely to be at hitting home runs against the expected pitchers”? Pitchers pitch sometimes very different ways, and every hitter 

******ebook converter DEMO Watermarks******* 

has strengths and weaknesses against specific styles of pitching. Implied in every home run prop price is some assumption about how well that hitter is likely to match up versus the various potential pitchers they could face. Any one of these assumptions about how easy or hard it will be for a hitter to hit home runs in a game is potentially falsifiable. 

**The pricing relies on “following the sport.”** Some bets can be priced by someone with no day-to-day knowledge of the sport. There are many examples, but alternate football totals is one. If the price discovered game total is 51.5, you can set a good price for over 61.5 without knowing any day-to-day things like who is likely to be the third-choice wide receiver for one of the teams. But pricing some bets is reliant on this sort of nitty gritty knowledge. Some examples. 

- **Most player props.** Player prop pricing is dependent on a player’s expected game usage. If a hockey forward is promoted to the first power play unit, their expected goals and assists will increase purely due to that promotion. If an WNBA player is likely to get rested for a game, some (but not all) of her teammates expected stat totals will go up based solely on that. There is no way to get this stuff right without following the sport on a daily basis. 

- **Late inning baseball markets.** Relief pitchers are available for a game or likely to be rested based on whether they’ve pitched in the past two games. A few relief pitchers are so good and used so predictably that it’s impossible to price, for example, any lines on specifically the eighth or ninth innings without knowing whether that specific pitcher is likely to pitch or not. This obviously requires the pricing model to include information gathered about all relevant pitchers and updated on a daily basis. 

**The product is new.** Anything new to the market will have bugs. It’s pretty much that simple. 

If you start looking at specifically these sorts of betting markets—and especially if you put in the work yourself to follow the sports and spend 

******ebook converter DEMO Watermarks******* 

significant time checking lines—you will begin to see all the errors. It’s a difficult job for the modelers at the content creation companies to keep all of this right, and for various reasons you can expect them to routinely fall short. 

Finding good bets is one of those skills that, once you start to get the hang of it, you begin to see more and more angles. If you’ve never picked apart a betting menu before, it feels intimidating, and you have no idea where to start. But hopefully we’ve given you enough ideas of places to look in this book that you can get your foot in the door. Once you find some bad prices, you’ll gain confidence, and your curiosity will encourage you to search more. Modern sportsbooks are a pretty soft target, and there are plenty of glitches out there to find to keep you entertained. 

The second step is substantially more difficult. You have to learn how to bet in such a way as to both win and avoid being identified as a troublemaker. Modern sportsbooks know their menus are full of pricing errors, and they don’t want people betting those errors. They all employ customer profiling systems, and one of the main tasks of those systems is to exclude “undesirable” customers. These systems are designed to detect and exclude problem gamblers, people laundering money, people who should not be betting due to personal connections with sports, governments, or other regulatory bodies, people who are located in unauthorized jurisdictions, and so forth. 

But they’re also designed to detect and exclude winners. If you’re trying to win, they don’t want you. Many bettors refuse to believe this until they get restricted for the first time. If that’s you, take our word for it. 

Your first problem if you want to achieve longevity at a modern sportsbook is that the people who work there already know what we’ve shared with you in this book. They understand the great difference in pricing strength between lines made through price discovery and lines that are produced by models. They understand that player-related bets are vulnerable because of how sensitive they are to news and how much they require following the sport closely to get right. They know their futures markets are soft, especially individual player markets like end of season award winner markets or league leader markets. 

You will attract suspicion simply by betting on the things we suggest you bet on and winning. Here are some things you can do to mitigate this problem, in increasing order of difficulty. 

******ebook converter DEMO Watermarks******* 

**Embrace variance.** Avoid betting strategies that “lock in” wins. Go the opposite direction. Parlays are your friends. Make it hard for sportsbook employees to determine whether you are skilled or just lucky. 

**Pass on betting obvious errors.** Don’t show the traders up. If the line says ‑15, but it’s obvious that ‑1.5 was intended, skip that. (This one hopefully is obsolete now—left back in a time when traders typed lines in manually.) If a preseason injury to a franchise quarterback is announced, don’t run and bet that team’s season win total under. This betting behavior is obvious, clumsy, and it pisses sportsbook employees off. 

**Avoid courtsiding.** Betting in-play on important in-game events before the data feed updates the lines will get you tossed. 

**Pass on bets that are likely to have measurable closing line value.** Recall that “closing line value” (CLV) means that the price of the bet you made becomes more expensive at a later time. If you bet the Cubs at ‑135 (57.4 percent break-even), and by the time the game starts, the price is ‑160 (61.5 percent break-even), you have gotten a four percent “bargain” on your bet. The problem with this from a stealth perspective is that it leaves behind a record. The sportsbook can easily run a script that adds up the closing line value generated by every account. If your account appears near the top of this list, that’s bad for your continued ability to bet. It’s harder for sportsbooks to calculate CLV on in-game bets and single game parlays than it is on pregame straight bets. 

**Focus on the biggest sports.** In-play NFL markets are likely a good target. The lines are made by models, lots of situational factors matter, sportsbooks can’t easily calculate your CLV, and most importantly, these are core menu offerings that any US-based modern sportsbook will encourage all customers to bet. The five-a-side pickleball in-play markets are no doubt a softer target, but if you bet those too much and win, expect the sportsbook to pull the plug on you. 

Understand that five-a-side pickleball is not seen as a profit center to the trading team. The book may offer the markets for one of several reasons— perhaps the five-a-side pickleball league signed a contract with the sportsbook brand promising to pay an annual fee to have their league included. Perhaps it’s viewed as “menu differentiation.” Maybe some higher-up at the sportsbook just loves five-a-side pickleball and thinks it’s the wave of the future. But the trading team will know those markets are 

******ebook converter DEMO Watermarks******* 

beatable, and if you beat them, they’ll not think twice about stake factoring your account. 

Whereas if you beat NFL in-play markets, because the betting volume is so much greater, you’ll just be one of a large number of customers winning on those, and the trading team will be less quick to take action because that’s what they want you betting. 

“Is this the stuff the sportsbook wants me to bet?” can be a powerful question to ask yourself if you want longevity. The more you push yourself to learn about the industry and the current landscape of business incentives and interests, the better you’ll be able to answer this question. 

**Actively define your relationship with the sportsbook.** You can go the under the radar route if you like. Bet small, talk to no one at the sportsbook, hope no one notices your activities. That’s fine. But understand that going that route caps your potential upside. You uncap your upside with some social engineering. Introduce yourself. Demand (politely) a relationship with a host. Play the part of the recreational gambler. Ask for things. Lose. Win. Lose. Ask for more things. If you’re winning, try to make it look like luck—you hit a couple big parlays perhaps. (You hit the parlays because you bet those parlays in the first place.) Play up your losing streaks. Avoid using obvious angles when you make particularly good bets. 

Some of the winningest gamblers maintain larger-than-life personas. Far from slinking in the shadows, they are extremely well-known figures to anyone who works in the gambling industry. They construct elaborate personal narratives where they expertly weave together truths with falsehoods about themselves and their activities. They’re often well known to be big net winners at gambling—and yet they also continue to find themselves welcome to bet. The story is, “Oh, he wins at poker (or sports or horses or gin rummy), but he loses it all back at X,” where X is whatever gambling game happens to be the target today. Slots. Baccarat. Golf. Sports betting. 

It’s not easy to convince an entire industry full of people that you’re some kind of weird degenerate gambling savant who wins at specific games, but who can’t control themselves from losing it all back at other games. (And then proceed to win at the games you’re supposedly bad at.) We aren’t suggesting you try to go down this road. But know that this is what gamblers who are elite at the social aspect can look like. 

******ebook converter DEMO Watermarks******* 

**Develop the ability to lay down cover bets.** This (along with the social skill) is one of the most valuable modern sportsbook skills. If you bet college football spread and moneyline parlays on Saturday morning, trading teams will give you full credit for the theo those bets generate. These are heavily price discovered lines, and sportsbook employees will assume that none of their customers can generate edge against them. 

A four-leg point spread parlay bet into 5 percent hold markets will “hold” about 20 percent, so if you bet a $1,000 parlay, your account will get full credit for $200 of theoretical loss to the book. 

If the trading team decides to review your play, a history of making many of these sorts of bets will weigh heavily in your favor. 

The skill is developing the ability to get these bets from $200 losers to break even (or close). 

Trading teams assume none of their customers can generate edge against these lines because almost no one has the skill to pick these bets. Nearly everyone who thinks they can is wrong. 

But it is not impossible to develop systems that can successfully handicap game day major market lines and find the best bets. It’s a lot of work, and it requires a team that possesses a number of distinct skillsets— sports knowledge, data engineering, statistical fluency, gambling/trading skill, among others. 

The good news is that if you wanted to bet these markets at market making sportsbooks, you’d have to get to the point where you could win at 1‑to‑2 percent. The bar is lower at modern sportsbooks, because being break even or even being able to lose at only half a percent has potentially enormous value. Because of how the math works, while it might not sound like a big difference, it’s a much easier task to learn to lose at 0.5 percent than to win at 0.5 percent. 

Once you get to the point where you can place large numbers of roughly break-even bets on major markets, you theoretically have what’s needed to hit modern sportsbooks very hard. Someone who blasts away for huge bet sizes on game day parlays can appear to a sportsbook’s VIP team to be the dream customer. If you pair that skill with a compelling enough story (i.e., you “look the part” of the dream customer as well), you can probably imagine what lengths an unsuspecting VIP team might go to attract your business. People can be blinded by dollar signs. 

******ebook converter DEMO Watermarks******* 

We expect stories to leak out over the next decade of a few select gamblers who combined these skills to net huge scores from US-based modern sportsbooks. 

******ebook converter DEMO Watermarks******* 

# CONCLUSION 

Our goal in writing this book was to pull back the curtain on the modern sports betting industry to give you a real sense of how it all comes together. And, to some extent, to show how the emperor sometimes has no clothes. 

Modern sportsbooks make a lot of promises—express and implied. The express promise is that you can have a safe experience with them. They’ll accept your deposits, and you can more or less treat your wallet there as you would a bank account. If you ask for a withdrawal, they’ll send you your money. If you win bets there, they’ll pay off. 

This is a pretty weighty promise, and for the most part we think the modern sportsbook industry follows through on this promise. Potential exceptions to this rule should feel like exceptions to you before you get involved. Maybe that sportsbook brand you’ve never heard of in your life and that you found out operates only in your state isn’t as safe a bet on this front as well-known and trusted brands like BeaverBet or BetBeaver. 

But if you stick with the major brands, we think the express promise they make—basically that you won’t get hosed by them—is on solid ground. And that’s a pretty important thing. 

Where things get murkier is with the implied promise. If you walk into a Candies R Us store and see thousands of different brands of candies on the shelves with prices on every product, there’s an implication (though, to be fair, no one specifically greets you at the entrance to the candy store and assures this to be true) that you’re welcome to browse the store, choose whichever candies you like, purchase those candies for the listed prices, enjoy your candies, and come back at any point in the future to do it again. 

One might assume when opening a modern sportsbook’s app and browsing their menu of thousands of possible sports bets, each with neatly listed prices on them, that the same implied promise is made. 

Unfortunately, it very much is not. They may or may not honor the listed price when you go to buy. They may or may not permit you to buy your 

******ebook converter DEMO Watermarks******* 

chosen bets, may or may not permit you to buy anything at all in the future, and they make these choices arbitrarily at their own discretion based on whatever information they have about you. They may even, in uncommon but not necessarily rare cases, declare that a bet already bought and paid for was done so in error and unilaterally rescind the transaction. (This is the palpable error rule.) 

This has never quite sat well with us. On one hand, we are sympathetic to the sportsbook’s reality. They want to offer a lot of fun product to their customers. We know first-hand how difficult it is to price an entire sportsbook’s betting menu well, around the clock, as with our business we tried to tackle a subset of that problem. It’s hard. It’s impossible to do it without making some mistakes from time to time. 

On the other hand, modern sportsbooks are making an implied promise to their customers that they are not fully prepared to follow through on. We think that sucks. 

There’s middle ground. The modern sportsbook industry should not lean as heavily as they do on throwing customers out to solve their pricing problems. Content companies should do a better job of hardening their pricing. If they want to offer betting on the eighth inning, they should put in the effort to account properly for the late inning relief pitchers. If they want to offer player props on third wide receivers, they should properly account for how those players get used in the games. If they want to let you bet on the outcome of every pitch, every possession, every drive, then they should get all the relevant factors right. They shouldn’t just shrug their shoulders and say, “If anyone beats it, we’ll just stake factor them.” We have heard that sentence uttered too many times in meetings with other industry people. 

We think there’s a serious disconnect between the people who sign deals and make decisions in the industry and the people who work day-to-day in the trading rooms. It’s clear that industry decisionmakers sometimes sign partnership deals with third party content providers without ever seriously inspecting the raw data—the game state or pricing information—that they’re purchasing. This failure shifts the incentives for those working at content providers away from ensuring that their existing product is always of the highest quality towards ensuring that they’re constantly promising (even overpromising) huge quantities of new product. 

******ebook converter DEMO Watermarks******* 

This creates difficulty for the employees tasked with protecting the sportsbook in the trading room. These folks are asked to defend ever larger amounts of betting territory on ballooning menus. They’re held accountable for how the book performs in each of these markets. But they’re given few tools with which to do the job. 

Say a sportsbook buys and integrates an in-play single game parlay fivea-side pickleball product from a third party. When a customer chooses a five-leg parlay, the sportsbook’s server sends the choices as an API call to the third-party company’s servers which respond with a price. If those prices just generally suck, the traders can’t really do anything about it. They have only two real knobs they can turn to do their job to protect the sportsbook in this situation. They can add more hold to the product across the board. Or they can exclude specific customers from using the product. 

Both of these actions degrade customer experience, but for the traders it’s either that or allow the sportsbook to lose essentially unlimited amounts of money to sharp bettors on five-a-side pickleball parlays. 

Over the years, we’ve encouraged dozens of industry people to “watch the lines.” Just sit there on a football Saturday or Sunday and actually look at the product. From the manic beginnings of an NFL day to the final play of Sunday Night Football. Set aside those ten hours and fully experience the product they offer alongside the products their competitors offer. Watch all those prop prices flash by. Play with the single game parlay widgets. See which sportsbook brands leave markets suspended without explanation for extended periods of time. See which content providers leave stale lines up and available for betting while the star quarterback is on TV writhing injured on the ground. See which companies habitually publish garbage, nonsense lines before they straight copy a competitor’s prices. 

The reality is that a lot of industry people refuse to take this advice. We can’t force people to spend the time to experience the product they sell. But we think there is no substitute. In sports betting, there is a lot you can understand only if you are present and you put in the hours. 

We hope in writing this book that we’ve inspired everyone who loves sports betting to up their games. We hope we’ve inspired bettors to think more deeply about the bets they make. To think critically about their betting options and to choose ones that give them a chance at better outcomes. 

We hope we’ve inspired regulators to examine the express and implied promises that modern sportsbooks make to their customers and perhaps to 

******ebook converter DEMO Watermarks******* 

ensure that sportsbooks live up to those promises more often. 

We hope we’ve inspired the people who work at betting content creation to go the extra mile and stand out from the competition in quality as well as quantity. 

And we hope we’ve inspired those who work at modern sportsbook brands to take perhaps a longer-term view on product, branding, and “differentiation.” To trust that a deeper commitment to product quality today can lay the foundation upon which to build a winner for years to come. 

******ebook converter DEMO Watermarks******* 

# ACKNOWLEDGMENTS 

A big thank you to Andrej Semnic (semnitz on 99designs.com)  for a fantastic cover design. 

Thank you to the folks who took time out of their days to read, edit, and give feedback on the book like Diana Davidow, Gina Fiore, Elihu Feustel, Joe Bunevith, and Rufus Peabody. 

Finally, thank you to Diana Davidow and Elaine Vigneault who are indispensable every day and without whom this book and likely many other things would not be possible. 

> <u>[1]</u> Yes, you should read it. No, it’s not a prerequisite to this book. But also yes, do read it—it’s good and there isn’t much overlap between what this book covers and what that one does. 

> <u>[2]</u> Incidentally, if one can get over the hump of the alluded to barrier to entry issues, there’s a lot of money waiting to be made by a small team of engineers who can put together a brand new, modern, licensable, and working version of either of these software packages. 

> <u>[3]</u> These are not industry terms, by the way. We’re just using them because they make sense to us. The industry likes talking about things like “bespoke turnkey solutions,” which we assume to be a grammatically correct phrase in the King’s English that means something, but we aren’t quite sure. 

> <u>[4]</u> Australians as well. We shall refrain from adding parenthetical Australians from here on out, but should you dear reader happen to be Australian, your nation’s accomplishments in the industry are hereby duly noted. 

> <u>[5]</u> At least that’s what it looks like to us spectators. Coaches likely have on-the-field insight into how likely their plays are to work that we don’t, and that insight likely factors into these seemingly whimsical decisions. 

> <u>[6]</u> Modern sportsbooks are famous for their original, inspired branding. 

> <u>[7]</u> Market making sportsbooks dabble in modern sportsbooking these days. These categories are not black and white. 

******ebook converter DEMO Watermarks******* 

> <u>[8]</u> “Data” is a generic term used here in a rather specific manner. If the content of the transmitted information is primarily prices or odds, then it’s a “pricing feed” or an “odds feed.” If the content of the transmitted information is instead primarily game state information, it’s not a “game state feed” but instead a “data feed.” 

> <u>[9]</u> They don’t think of it this way, of course. They just talk about “staying in line with the market line” in-game as if such a thing exists in the same way that it does pregame. Which it doesn’t. The market that is. 

> <u>[10]</u> Tsk tsk. The impulse to lock in a profit rather than to embrace the gamble is a nasty little hobgoblin. But that’s what he did. And today he’s nationally famous for his non-gambling endeavors, while we’re out here grinding in relative obscurity. So who are we to judge. 

> <u>[11]</u> It’s true by definition. We have defined the term “modern sportsbook” as one that is betting menu maximizing. Their defining trait is that they want to offer as many different possible bets and markets as they can, and they compete with other modern sportsbooks based on the quantity and quality of their betting menus. Sportsbooks that encourage winning customers to play are not menu maximizing, and we have referred to them as “market making sportsbooks.” 

> <u>[12]</u> Note that advantage gamblers trying to beat the sportsbook are just one class of undesirable customers. Other undesirable customers include people who may potentially be committing financial crimes, problem gamblers, and people who aren’t permitted to bet due to their connection to sports or political organizations. One could write an entirely different book about how sportsbooks approach these undesirable customers, but it’s beyond the scope of this book. 

> <u>[13]</u> You can still do some of this sort of VIP program gamesmanship today, using slot machines and video poker among other things, but that’s a topic for another book. 

> <u>[14]</u> This was before the internet. Yes, we’ve been at this a while. 

> <u>[15]</u> You get this number by taking the square root of 0.5. 

> <u>[16]</u> Overround is a mathematical shorthand useful for quickly estimating the sportsbook’s hold in multiway markets. You convert the odds to break-even percentages and add them up. The amount that number exceeds 100 percent is the overround. So in this case, the break-even percentages of the three options summed to 130 percent. Not good for the bettor. 

> <u>[17]</u> Sportsbooks do sometimes short pay classic parlays with particularly large numbers of legs because they can. 

> <u>[18]</u> Those latter bets are called “micromarkets” in the industry vernacular, and they are the hot new thing, so expect to see more and more of these options on menus soon. 

> <u>[19]</u> We will leave confirming this result mathematically as an exercise for the reader. 

******ebook converter DEMO Watermarks******* 


