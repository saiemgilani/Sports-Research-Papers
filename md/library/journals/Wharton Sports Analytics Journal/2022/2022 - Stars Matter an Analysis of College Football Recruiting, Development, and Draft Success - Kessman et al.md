<!-- source: library/journals/Wharton Sports Analytics Journal/2022/2022 - Stars Matter an Analysis of College Football Recruiting, Development, and Draft Success - Kessman et al.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/stars-matter-an-analysis-of-college-football-recruiting-development-and-draft-success/ -->
<!-- issue: Wharton Sports Analytics Journal, Fall 2022 -->
<!-- authors: Naya Kessman; Ellery Axel; Cotton Snoddy; Will Hoey -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

STARS MATTER: AN ANALYSIS of college football RECRUITING

& development

By Naya Kessman, Ellery Axel, Cotton Snoddy, & Will Hoey

Wharton Moneyball Academy 2022, Sports Analytics Student Research Journal background

Joe Burrow

High School

College

NFL

3.8% of NFL Draft-eligible Division I FBS football players make it to the NFL

OUR Question

Which NCAA Division 1 program is best developing their players for the NFL draft, factoring in how well they recruit? goalS

UNDERSTAND THE CONNECTION BETWEEN HOW WELL PROGRAMS RECRUIT players AND

HOW HIGHLY THeir RECRUITing CLASSES

ARE DRAFTED

IDENTIFY THE PROGRAMS WHO HAVE

DONE THE BEST AT DEVELOPing THEIR RECRUITS FOR THE

DRAFT resources

247 sports

We gathered our recruiting class rating data from 247Sports.com

CFB Data

We obtained our draft data from

CollegeFootballData.com

R

We used R to manipulate our data and create graphs

PROCEDURE

Obtaining Data

Creating Metrics

Cleaning Data

Creating Graphs

Insights

METRICS

247Sports Composite Rating: - Represents an “industry consensus” of the caliber of every school’s recruiting class in a given year

Total Draft Value: - Assigns a value from 0 to 1 to every slot of a given draft

Coefficient Of Variation: - Equivalent to standard deviation/mean; it reflects the variation in a population while also taking into account its mean - and it is unitless

Schools’ recruiting CLASS raTINGS

RECRUITING CLASSES’ TOTAL DRAFT VALUES draft value

Team

Alabama Ohio State LSU USC Georgia

BEST AVERAGE DRAFT VALUE

3.890 3.427 3.246 2.962 2.877

Team

Air Force Army New Mexico NM State UNLV

WORST AVERAGE DRAFT VALUE

0.000 0.000 0.019 0.032 0.034

Rating vs. draft value regression

USC 2003 2003

Alabama 2017 Florida St 2002

Wake Forest 2003

USC 2006 Texas 2010

RECRUITING VS. DRAFTED SUMMARY

Team

Ohio State Alabama Clemson LSU Louisville

BeST AVERAGE RESIDUAL (Z)

0.875 0.846 0.677 0.586 0.568

Team

Texas Nebraska Kansas St. FSU New Mexico

WORST AVERAGE RESIDUAL (Z)

-0.912 -0.480 -0.469 -0.403 -0.400

Consistency

Penn St Clemson

USC Oklahoma

NM State

Iowa State

RECRUITING CONSISTENCY

Team

USC Oklahoma Georgia OSU Maryland

RECRUITING CONSISTENCY

16.49 14.87 12.39 12.04 11.92

Team

Air Force Army San José NM State Troy

RECRUITING CONSISTENCY

1.610 2.010 2.369 2.535 2.677

CONSISTENCY SUMMARY TABLES

Team

USC Oklahoma Georgia OSU Maryland

RECRUITING CONSISTENCY

16.49 14.87 12.39 12.04 11.92

Team

Penn State LSU Miami Clemson Arkansas

DRAFTED CONSISTENCY

2.428 1.895 1.845 1.805 1.755

Team

Penn State Clemson Ohio State Stanford Notre Dame

BeST RESIDUAL (Z)

3.979 2.454 2.105 1.771 1.755

Team Ohio State Alabama Penn State Clemson LSU

FINAL standings

Combined Rating 89.96

85.91

85.23

Combined Rating = [(Normalized Average Residual For Recruiting Rating vs. Total Draft Value)*2 + (Normalized Residual For Consistency Regression)*1)]/3 * 100

84.43

75.99

POSSIBLE Limitations

01 NO Transfer portal We excluded players who were drafted from a different team than they committed to

03 NO COACHING CHANGES Our project was conducted based on institutional-level data and as such we could not account for coaching staff changes.

02 No Juco We only analyzed recruits who were coming straight out of high school

04 NO violations NCAA Recruiting/Academic Violations were not accounted for.

THANK YOU!
