<!-- source: randoms/Data_Mining_in_Elite_Sports_A_Review_and.pdf -->

**Measurement in Physical Education and Exercise Science** 



Data Analysis and Mining Demands in Elite Sports Journal: Measurement in Physical Education and Exercise Science Manuscript ID: Draft Manuscript Type: Original Article Keywords: Statistics, Evaluation, exploratory factor analysis < Factor Analysis 

Journal: Measurement in Physical Education and Exercise Science Manuscript ID: Draft Manuscript Type: Original Article Keywords: Statistics, Evaluation, exploratory factor analysis < Factor Analysis 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 1 of 30** 

Data Mining Demands in Sports 1 

1 2 

3 4 5 6 7 

8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

1 Running head: DATA MINING DEMANDS IN SPORTS 

Data Analysis and Mining Demands in Elite Sports – – 

2 Data Analysis and Mining Demands in Elite Sports 

3 

4 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 2 of 30** 

1 2 

Data Mining Demands in Sports 2 

3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

# **Abstract** 

5 

- 6 Sophisticated data analytical methods such as data mining, with an exploratory focus, are 

- 7 becoming increasingly useful tools in analyzing sports performance data and supporting 

- 8 decision making that is crucial to gaining success in elite sports. In this article, we 

- 9 investigate the different data mining demands of different elite sports with respect to a 

- 10 number of features that describe sport competitions. Our main aim is to more formally 

that describe sport competitions. Our main aim is to sports and data mining domains through: (a) describing a sports with respect to pre-specified features, and (b) better of different types of performance analysis. For this, we as sport categories and performance analysis requirements, that in sports data mining. mining, sport, performance analysis 

- 11 connect the sports and data mining domains through: (a) describing a framework for 

- 12 categorizing sports with respect to pre-specified features, and (b) better understanding the 13 analytical demands of different types of performance analysis. For this, we review different 

- 14 aspects such as sport categories and performance analysis requirements, that influence 15 certain stages in sports data mining. 

16 Keywords: Data mining, sport, performance analysis 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 3 of 30** 

Data Mining Demands in Sports 3 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

# **Data Analysis and Mining Demands in Elite Sports** 

17 

18 Performance analysis, as a means for creating and analyzing a valid record of athlete 19 performances using systematic observations, has gained importance in the last decade. It 20 has been facilitated by advances in information technology and digital 21 photography (Bishop, 2003). This type of analysis can be either in the form of _match_ 22 _analysis_ or _biomechanics_ . Match analysis is more concerned with analyzing important 23 attributes, events, strategies, or patterns (and their importance) in gaining success in 24 different contests whereas biomechanics is more focused around the application of 25 mechanical principles to human’s biological system and how any improvements in (any 26 element of) this system may result in desired success in sports. Performance analysis, in 27 either form, can significantly assist coaches and athletes at any level in the process of 28 decision-making during or prior to sport competitions. 29 Despite the complexity and obvious demands of sport decisions, much of the coaches’ 30 decision-making in sport has been based on tradition and emulation (Williams & Ericsson, 31 2005). Traditional coaching may, for instance, dictate that large amounts of immediate 32 feedback on learning and skills practiced in blocked fashion will lead to improvements. 33 However, research controlling the structure of practice and feedback indicates 34 otherwise (Magill, 2007). Although, in most cases, there are data pertaining to 35 performance and training, systematic analysis and sophisticated data analytical 36 approaches, which may help avoid common errors such as base-rate neglect (Fiedler, 37 Brinkmann, Betsch, & Wild, 2000), have not been applied to gaining greater insight and 38 support for these tasks in an influential way. 

_biomechanics_ . Match analysis is more concerned with analyzing strategies, or patterns (and their importance) in gaining whereas biomechanics is more focused around the application principles to human’s biological system and how any improvements system may result in desired success in sports. Performance significantly assist coaches and athletes at any level in the during or prior to sport competitions. the complexity and obvious demands of sport decisions, much in sport has been based on tradition and emulation (Williams coaching may, for instance, dictate that large amounts of learning and skills practiced in blocked fashion will lead to controlling the structure of practice and feedback indicates 2007). Although, in most cases, there are data pertaining and training, systematic analysis and sophisticated data which may help avoid common errors such as base-rate neglect Betsch, & Wild, 2000), have not been applied to gaining greater tasks in an influential way. 

39 We believe the main challenges that to date interfere with large-scale and influential 40 utilization of effective analytical approaches in the sports performance analysis include: (a) 41 the lack of a belief that the outcomes of performance analysis can practically improve 42 future athlete performances in major competitions, and (b) the lack of a well-defined data 43 analytical framework that takes into consideration the main demands of different problems 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 4 of 30** 

Data Mining Demands in Sports 4 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

44 in elite sports and sport performance analysis requirements, and (c) the lack of confidence 45 and mutual understanding between sports data analysts and professional coaches/athletes, 46 especially in cases where the two come from different knowledge backgrounds. 47 While the first and third items rely on the cultural and psychological aspects of 48 integrating sports and data analytical procedures, the second item relates to guidance for 49 appropriate methods. A domain of methods for analyzing sports data is data mining which 50 is a branch of the broader domains of computer science and artificial intelligence. 51 Data mining is a problem-solving methodology that finds a logical or mathematical 52 description, eventually of a complex nature, of patterns and regularities in a set of 53 data (Fayyad, Piatetsky-Shapiro, & Smyth, 1996). Using data mining techniques, useful 54 and previously unknown information can be extracted from archived or streaming data. 55 The extracted information may be in the form of prediction of future events, finding events 56 that co-occur and their sequence of occurrence, and grouping entities that are similar 57 according to known attributes. 

methods. A domain of methods for analyzing sports data is data the broader domains of computer science and artificial is a problem-solving methodology that finds a logical or eventually of a complex nature, of patterns and regularities in a Piatetsky-Shapiro, & Smyth, 1996). Using data mining unknown information can be extracted from archived or information may be in the form of prediction of future events, and their sequence of occurrence, and grouping entities that are known attributes. many other applications of data analysis and mining (e.g., analysis, surveillance, etc.), elite sports data analysis must be demands of the given sport or sport task. This makes the a more sophisticated area of application (than aforementioned where converted measures and numbers require special demands. of physiological studies of recovery methods, biomechanical motor learning studies of training interventions, this article 

58 Unlike many other applications of data analysis and mining (e.g., customer analysis, 59 agricultural analysis, surveillance, etc.), elite sports data analysis must be matched, case by 60 case, with the demands of the given sport or sport task. This makes the domain of sports 61 data analysis a more sophisticated area of application (than aforementioned problems) for 62 analytical methods where converted measures and numbers require special treatments 63 regarding certain demands. 

64 Regardless of physiological studies of recovery methods, biomechanical studies of 65 techniques, or motor learning studies of training interventions, this article focuses on the 66 analysis of archived performance data using data mining (i.e., pre-processing and data 67 analysis) techniques and therefore tackles the second item above with two main aims: (a) 68 to describe a framework for categorizing different sports with respect to pre-specified 69 attributes that relate to performance analysis, and (b) to better understand the analytical 70 demands of different types of research problems in elite sports in terms of performance 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 5 of 30** 

Data Mining Demands in Sports 5 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

71 analysis. 

72 In keeping with the characteristics of data mining, the major goal of this study is to 73 focus on the _exploratory_ level of data analysis. Thus, the extraction of useful information 74 from previous data is our major concern. The article, therefore, leaves aside the _explanatory_ 75 level that explains and justifies any useful information discovered from the data. 

**Data Mining in Elite Sports** the performance analysis work in sports, concerning match statistical measures. These approaches range from analyzes. The straightforward analysis is usually concerned with between a few predictor variables and a dependent context of the data that have been collected (e.g., calculating the values of two variables without considering other to certain values of the two variables). Examples of studies data analysis category include the works by Pollard and and Huberty (2009); Vezos et al. (2007). approaches, however, more in-depth analysis is carried relationships between factors that may either directly or indirectly with respect to different target variables such as overall or even physiological parameters that may lead to certain data analysis studies include the studies by Cox and Dunn Sharp, and Boreham (2005); Kline et al. (2007); Liao (2008); 

76 

77 Most of the performance analysis work in sports, concerning match analysis, has been 78 based on using statistical measures. These approaches range from straightforward to 79 sophisticated analyzes. The straightforward analysis is usually concerned with finding 80 direct relationships between a few predictor variables and a dependent variable. This may 81 ignore the overall context of the data that have been collected (e.g., calculating correlation 82 measures between the values of two variables without considering other conditions that 83 may have lead to certain values of the two variables). Examples of studies that are more in 84 the straightforward data analysis category include the works by Pollard and Pollard (2010); 85 Ransdell, Vener, and Huberty (2009); Vezos et al. (2007). 

86 In sophisticated approaches, however, more in-depth analysis is carried out to find 87 underlying relationships between factors that may either directly or indirectly influence 88 sports performances with respect to different target variables such as overall rankings, 89 finishing times, or even physiological parameters that may lead to certain performances. 90 More sophisticated data analysis studies include the studies by Cox and Dunn (2002); 91 Kenny, Sprevak, Sharp, and Boreham (2005); Kline et al. (2007); Liao (2008); Vaz, Rooyen, 92 and Sampaio (2010); Zwols and Sierksma (2009). 

93 Although the above-mentioned studies have shed light on different aspects of a 94 number of elite sports, the use of statistical analysis without an understanding of their 95 fundamental meaning (and the contextual backgrounds of variables/values) under study in 96 terms of certain sports can potentially be misleading due to impreciseness or over-emphasis 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 6 of 30** 

Data Mining Demands in Sports 6 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

97 of the statistics (Schumaker, Solieman, & Chen, 2010). Impreciseness may be the result of 98 missing/ignoring other contributing variables and over-emphasis can be due to ignoring the 99 effect of conceptually non-related coincidences. The utilization of data mining techniques is 100 a way to overcome these problems. 

101 In the sports domain, data mining methods have generally been used to model the 102 inter-relationships of performance measures and attributes and to also extract athlete 103 performance patterns from previously held competitions. These can be used in the 104 decision-making processes to support _strategic planning_ and _athlete selection_ . 

of performance measures and attributes and to also extract patterns from previously held competitions. These can be used processes to support _strategic planning_ and _athlete selection_ . _Mining Methods Used in Sports Domain_ . Clustering, also referred to as unsupervised learning in the is concerned with finding the underlying structure in a set there is no (prior) label information available for the data points. is a number of groups. The members of each group are some criteria (i.e., similarity attributes) and are most with respect to the same criteria. Unsupervised learning pattern discovery, and outlier detection. Table 1 summarizes clustering for sport data analysis. . Classification, also known as supervised learning in the is used to predict group memberships for data instances set. The output of classification is a set of data instances and existing class labels. This task relies on known structures 

105 _Major Data Mining Methods Used in Sports Domain_ 

106 _Clustering_ . Clustering, also referred to as unsupervised learning in the machine 107 learning literature, is concerned with finding the underlying structure in a set of data 108 points where there is no (prior) label information available for the data points. The result 109 of cluster analysis is a number of groups. The members of each group are similar to each 110 other regarding some criteria (i.e., similarity attributes) and are most dissimilar to those of 111 the other groups with respect to the same criteria. Unsupervised learning may be used for 112 data reduction, pattern discovery, and outlier detection. Table 1 summarizes the other 113 major uses of clustering for sport data analysis. 

114 _Classification_ . Classification, also known as supervised learning in the machine 115 learning literature, is used to predict group memberships for data instances (i.e., individual 116 cases) in a data set. The output of classification is a set of data instances that are labeled 117 with pre-defined and existing class labels. This task relies on known structures or 118 knowledge that can then be applied to unseen new data. Table 1 summarizes some of the 119 other previous studies that made use of classification techniques for sports performance 120 analysis. 

121 _Relationship modeling_ . The aim of relationship modeling in a complex environment 122 with a number of participant attributes is to find a function or model that can define the 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 7 of 30** 

Data Mining Demands in Sports 7 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

123 data and describe the inter-relationships between predictor and dependent attributes. The 124 main aim in this task is to a model that data with the least error. 

125 Regression analysis is one of the methods that has been used for fitting a line or 126 polynomial to data. A limitation of regression analysis is that, in most cases, it is not 127 appropriate for modeling data where there is a large volume of non-linearity involved in the 128 underlying relationships. To overcome this, some researchers have made use of non-linear 129 methods, such as Neural Networks, to find attribute inter-relationships. Some of the 130 previous studies that utilized relationship modeling for sports data analysis are 131 summarized in Table 1. 

relationships. To overcome this, some researchers have made use as Neural Networks, to find attribute inter-relationships. Some that utilized relationship modeling for sports data analysis Table 1. . Finding rules that represent inter-relationships between in the first half of a football game and winning the game) or down and being physically weak) has two main forms in rule mining (Agrawal, Imielinski, & Swami, 1993) and (Agrawal & Srikant, 1995). While association rule mining is events or states that co-occur, sequential pattern mining is types of rules/patterns, when used in the sports domain, can conditions, movements, decisions, positions, or events in in time, that may lead to certain positions, scores, or outcomes rules and sequential patterns have been applied in a few et al., 1997; Jing, Wenshuang, & Huiqun, 2010). 

132 _Rule mining_ . Finding rules that represent inter-relationships between series of events 133 (e.g., pressing in the first half of a football game and winning the game) or states (e.g., 134 being emotionally down and being physically weak) has two main forms in data mining, 135 namely association rule mining (Agrawal, Imielinski, & Swami, 1993) and sequential 136 pattern mining (Agrawal & Srikant, 1995). While association rule mining is only concerned 137 with finding events or states that co-occur, sequential pattern mining is focused around the 138 sequence of events that co-occur with a high frequency in a timestamp ordered set of events. 139 These two types of rules/patterns, when used in the sports domain, can potentially 140 reveal series of conditions, movements, decisions, positions, or events in general, as well as 141 their sequences in time, that may lead to certain positions, scores, or outcomes in a broad 142 sense. Association rules and sequential patterns have been applied in a few 143 studies (Bhandari et al., 1997; Jing, Wenshuang, & Huiqun, 2010). 

144 _Current Status of Sports Data Mining_ 

145 In general, the utilization of different data mining methods (i.e., clustering, 146 classification, relationship modeling, and rule mining) in the sports domain suggests that 147 sports data mining can now be recognized as a distinct area of knowledge that requires 148 more in-depth attention by researchers in both domains of sports science and computer 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 8 of 30** 

Data Mining Demands in Sports 8 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

149 science. However, to date, there has not been significant effort from either side to more 150 formally and structurally connect the two domains. Most of the previous attempts at using 151 sophisticated data mining methods and techniques for sports performance analysis have 152 only considered ad hoc problems that arise in specific sports in limited contexts. Making 153 the connection between the two domains of knowledge (i.e., sport science and computer 154 science) will help avoid common errors (e.g., see (Fiedler et al., 2000)) and more effectively 155 and efficiently handle sports performance data. 156 In the next sections, we will go beyond this boundary and provide a more general 157 structure that introduces sports categories and types of research problems that are 158 encountered in the sports performance analysis domain, which we believe will facilitate 159 future research in this domain. 

help avoid common errors (e.g., see (Fiedler et al., 2000)) and handle sports performance data. sections, we will go beyond this boundary and provide a introduces sports categories and types of research problems the sports performance analysis domain, which we believe will in this domain. **Categorization of Sports** a number of methods of classifying sports using dimensions context (i.e., open versus closed) and primary actions (e.g., goal here is to highlight the most relevant features from a Before any data analytical approaches can be utilized for it is necessary to understand the specifics of the certain most relevant questions that arise. For conducting data performances, we categorize sport competitions regarding a aspects including the number of events, number of and winning/evaluation criteria. The main motivation 

160 **Categorization of Sports** 

161 There are a number of methods of classifying sports using dimensions such as the 162 environmental context (i.e., open versus closed) and primary actions (e.g., striking versus 163 endurance). Our goal here is to highlight the most relevant features from a data mining 164 point of view. Before any data analytical approaches can be utilized for performance 165 analysis in sports, it is necessary to understand the specifics of the certain sport under 166 study, and the most relevant questions that arise. For conducting data analysis and mining 167 tasks on sport performances, we categorize sport competitions regarding a few 168 sports-related aspects including the number of events, number of players/athletes, duration 169 of the competition, and winning/evaluation criteria. The main motivation behind using 170 these features is that they imply different types and methods of data mining especially in 171 the data pre-processing step. This will be discussed later in this paper. 

# **Sport-Related Data Mining Demands** 

172 

173 When analyzing sports performance data, there are three main attributes that are of 174 interest to sport scientists and professionals: (a) rankings, (b) times, and (c) scores. This is 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 9 of 30** 

Data Mining Demands in Sports 9 

1 2 3 4 175 mainly due to the fact that, apart from referees’ discretion mentioned earlier, these three 5 6 176 measures represent performance and are used for evaluating athletes in most sport events. 7 8 177 We refer to these performance measures as RTS (ranking, time, score) measures. 9 10 178 We believe that sports performance analysis implies a mapping, as shown in 11 12 179 Figure 1(a), from the sports domain to the data analytical domain (the data mining 13 14 180 domain in this work). While the sports domain involves the main rules, regulations, 15 16 181 strategies, performances, conditions, and abilities related to specific sports, the data 17 18 182 domain includes the representative performance measures, namely RTS measures. 19 20 183 The data pre-processing and data analysis methods that can be utilized in the data 21 22 184 mining space can only interpret the available data in the form of the performance 23 24 185 A deeper understanding of (sports) domain knowledge as well as a better understanding 25 26 186 the available and appropriate data mining tools serves to minimize problems in sports 27 28 187 performance analysis due to the lack of precision, sound approach, or validity. 29 30 188 The mapping that occurs from the sports domain to the data mining domain for 31 32 189 performance analysis opens a gap between the two domains of science, namely sport 33 34 190 and computer science. To minimize the effect of this gap, the mapping has to enable the 35 36 191 possibility of inheriting required (sports) domain knowledge. This knowledge is necessary 37 38 192 for data analysts not only to evaluate the results of their analysis but also to validate 39 40 193 processes that they carry out for preparing data and extracting information from them. 41 42 43 194 _Sports Data Pre-processing_ 44 45 46 195 Sports-related data pre-processing, in the data mining space, involves preparing 47 48 196 sorting data for analysis and can take one or some of the following forms, depending on 49 50 197 format of the data and the research problem: 51 52 198 (a) **Filtering:** Filtering data records considering certain categories of competitions 53 54 199 e.g., categorizing rowing performance results in to fast, medium, and slow courses. 55 56 200 (b) **Format conversion:** Converting data into a format which can be interpreted 57 58 59 60 

175 mainly due to the fact that, apart from referees’ discretion mentioned earlier, these three 176 measures represent performance and are used for evaluating athletes in most sport events. 177 We refer to these performance measures as RTS (ranking, time, score) measures. 178 We believe that sports performance analysis implies a mapping, as shown in 179 Figure 1(a), from the sports domain to the data analytical domain (the data mining 180 domain in this work). While the sports domain involves the main rules, regulations, tactics, 181 strategies, performances, conditions, and abilities related to specific sports, the data mining 182 domain includes the representative performance measures, namely RTS measures. 183 The data pre-processing and data analysis methods that can be utilized in the data 184 mining space can only interpret the available data in the form of the performance measures. 185 A deeper understanding of (sports) domain knowledge as well as a better understanding of 186 the available and appropriate data mining tools serves to minimize problems in sports 187 performance analysis due to the lack of precision, sound approach, or validity. 188 The mapping that occurs from the sports domain to the data mining domain for 189 performance analysis opens a gap between the two domains of science, namely sport science 190 and computer science. To minimize the effect of this gap, the mapping has to enable the 191 possibility of inheriting required (sports) domain knowledge. This knowledge is necessary 192 for data analysts not only to evaluate the results of their analysis but also to validate the 193 processes that they carry out for preparing data and extracting information from them. 194 _Sports Data Pre-processing_ 195 Sports-related data pre-processing, in the data mining space, involves preparing and 

195 Sports-related data pre-processing, in the data mining space, involves preparing and 196 sorting data for analysis and can take one or some of the following forms, depending on the 197 format of the data and the research problem: 

200 (b) **Format conversion:** Converting data into a format which can be interpreted by 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 10 of 30** 

Data Mining Demands in Sports 10 

1 

2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

201 specific data analytical software and tools used when conducting actual data analysis e.g., 202 converting hh:mm:ss times into collective seconds. 

203 (c) **Extraction:** Finding new data not explicitly available based on collected data 204 e.g., extracting absolute and cumulative rankings of boats relative to different sectors of 205 2000-meter rowing races based on the times of the boats (Ofoghi, Zeleznikow, & 206 MacMahon, 2011b). 

2011b). **conversion:** Converting parts of data into a format data analytical process e.g., generalizing final standings ranging into medal winner (positions 1 to 3) and non-medal than 3) categories. **conversion:** Converting specific parts of data to a the nature of the specific sport/problem e.g., converting times that show the time differences between the lead and pre-processing tasks in _filtering_ , _format conversion_ , and sport specifics, while _structural conversion_ is usually dependent data analytical method where some data analytical methods nominal values compared to numeric data types e.g., (b) the amount of data that is available where often small specific parameters may necessitate generalization of the values values that cover a greater number of data records. _Descriptive_ hand, closely linked to understanding the sport and its 

207 (d) **Structural conversion:** Converting parts of data into a format that allows for 208 more precise data analytical process e.g., generalizing final standings ranging from 1 to the 209 number of contestants into medal winner (positions 1 to 3) and non-medal winner 210 (positions greater than 3) categories. 

211 (e) **Descriptive conversion:** Converting specific parts of data to a format that 212 better describes the nature of the specific sport/problem e.g., converting absolute times to 213 relative/differential times that show the time differences between the lead and other 214 athletes. 

215 The data pre-processing tasks in _filtering_ , _format conversion_ , and _extraction_ are not 216 affected by the sport specifics, while _structural conversion_ is usually dependent on: (a) the 217 specifics of the data analytical method where some data analytical methods can more 218 effectively handle nominal values compared to numeric data types e.g., classification 219 systems, and (b) the amount of data that is available where often small amounts of data 220 pertaining to specific parameters may necessitate generalization of the values into more 221 coarse-grained values that cover a greater number of data records. _Descriptive conversion_ 222 is, on the other hand, closely linked to understanding the sport and its features. As 223 mentioned earlier, the magnitude of the effect that the sports domain may have on this 224 type of pre-processing depends on the specifics of the sports and the sports categories. The 225 appropriate data pre-processing technique may be chosen or driven by the combination of 226 features of a sport e.g., scoring system, duration, number of events, etc. However, we will 227 address these issues individually in the next section. In the cases where there are a number 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 11 of 30** 

Data Mining Demands in Sports 11 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

228 of sport features to be considered, a combination of pre-processing tasks may be 229 appropriate. 

230 _The effect of the number of events in a competition on sports data pre-processing_ . 231 Most single-component sports (e.g., fencing and running) usually do not require or 232 influence descriptive conversion in data pre-processing. The main reason for this is, in 233 these sports, the predictor variables i.e., the RTS measures, explicitly represent the nature 234 of the sport and can therefore be utilized for modeling the underlying structure to predict 235 the variations of the dependent variable e.g., the final standings. For instance, 200-meter 236 freestyle swimming does not require any specific type of pre-processing of lap times to 237 predict finishing times. 

the predictor variables i.e., the RTS measures, explicitly can therefore be utilized for modeling the underlying of the dependent variable e.g., the final standings. For instance, does not require any specific type of pre-processing of lap times. competitions, however, may necessitate converting We argue that this depends on whether the individual events triathlon) or _independently_ (e.g., track cycling omnium). measures, RTS, in independent multiple events usually provide modeling and predicting dependent variables i.e., the overall standings. The machine learning-based analysis of the necessary track cycling omnium competitions carried out by Ofoghi, Dwyer (2010), for example, includes no further pre-processing in each individual event than generalizing the final standings of medal winners, non-medal winners ranked between 4 and ranked above 10. This is mainly due to the small amount available for this specific sport. 

238 Multiple-component competitions, however, may necessitate converting specific data 239 to other forms. We argue that this depends on whether the individual events are held 240 _successively_ (e.g., triathlon) or _independently_ (e.g., track cycling omnium). The three 241 performance measures, RTS, in independent multiple events usually provide enough 242 information for modeling and predicting dependent variables i.e., the overall times and the 243 overall final standings. The machine learning-based analysis of the necessary abilities for 244 winning the track cycling omnium competitions carried out by Ofoghi, Zeleznikow, 245 MacMahon, and Dwyer (2010), for example, includes no further pre-processing on the 246 rankings of riders in each individual event than generalizing the final standings into the 247 three categories of medal winners, non-medal winners ranked between 4 and 10, and 248 non-medal winners ranked above 10. This is mainly due to the small amount of historical 249 data which is available for this specific sport. 

250 In successive multiple-event sports, in contrast, raw RTS measures may be misleading 251 in the performance analysis task. Triathlon is an example of a successive multiple-event 252 competition where the raw rankings or raw times of athletes, pertaining to each individual 253 component, may not reveal a great deal of information as to which individual discipline 254 plays the most important role in deciding whether a triathlete can win the competition. 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 12 of 30** 

Data Mining Demands in Sports 12 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

255 This is due to the immediate succession of the events where it does not matter what 256 absolute times or rankings are achieved by the triathletes, but the time difference behind 257 the lead athlete in each component. Ranking second by a large time difference in any 258 triathlon component implies a rather small chance for winning the contest compared to 259 ranking fourth or fifth in any discipline with a much smaller time difference. Therefore, 260 pre-processing the times and converting them into differential times becomes crucial to 261 data mining in the triathlon. This is the approach Ofoghi, Zeleznikow, and MacMahon 262 (2011a) have taken for analyzing triathlon data and found that with a _∼_ 87% certainty, a 263 male triathlete can only win a medal if their differential running time is _≤_ 26 seconds. For 264 female triathletes, they found the certainty level is _∼_ 86% and the affordable differential 265 running time for winning a medal is 28 seconds. 

the times and converting them into differential times becomes the triathlon. This is the approach Ofoghi, Zeleznikow, and taken for analyzing triathlon data and found that with a _∼_ 87% can only win a medal if their differential running time is _≤_ 26 they found the certainty level is _∼_ 86% and the affordable for winning a medal is 28 seconds. _of number of players/athletes on sports data pre-processing_ . cannot be used alone to decide what type of pre-processing However, when considering the effect of this feature on descriptive one should take into consideration the different and _collaborations_ that occur in single-player versus team sports (e.g., fencing and singles’ table tennis) may require measures, to be converted only to the extent that enables interactions between the current athlete against his/her cases, the ultimate goal of performance analysis is to discover lead to defeating the opponents. For instance, the analysis data is carried out to find the best strategies that will result in 

266 _The effect of number of players/athletes on sports data pre-processing_ . The number of 267 players/athletes cannot be used alone to decide what type of pre-processing needs to be 268 conducted. However, when considering the effect of this feature on descriptive conversion 269 in data pre-processing, one should take into consideration the different characteristics of 270 the _interactions_ and _collaborations_ that occur in single-player versus team sports. 271 Single-player sports (e.g., fencing and singles’ table tennis) may require data, in the 272 form of the RTS measures, to be converted only to the extent that enables modeling the 273 dynamics of the interactions between the current athlete against his/her opponent/s. In 274 most of these cases, the ultimate goal of performance analysis is to discover the patterns 275 that may directly lead to defeating the opponents. For instance, the analysis of tennis 276 performance data is carried out to find the best strategies that will result in winning the 277 game against the opponent. Therefore, there is a little need for converting tennis data or 278 extracting new types of explicit data in single-player sports. 

279 Team sports, on the other hand, may necessitate data pre-processing towards 280 modeling the collaboration that occurs among different players in a team or selecting 281 variables that indicate team versus individual performance. In most such sports, while the 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 13 of 30** 

Data Mining Demands in Sports 13 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

282 ultimate goal of performance analysis is to provide information that can be used to 283 enhance the chance of winning, there are also intermediate goals or moderators in terms of 284 finding the best collaborative re/actions that may lead to more successful scenarios in 285 certain places or times of a game. Taking the game as a whole, this will increase the 286 winning chances of the team. Finding the best collaborative strategy to enhance moving 287 the ball towards the dangerous 16-meter penalty area in football is an example of such an 288 analysis. In these cases, data related to each athlete/player pertaining to different times 289 and/or places in the game require specific treatment before any actual analysis. For this, 290 depending on the particular problem, the status of the original data collected, and the 291 capabilities of the data analytical method to be employed, one may need: (a) to assign 292 pre-defined event labels to each data record (for each player) in the data collection (e.g., 293 score or non-score labels in hockey data or shot on goal in football data), and (b) to group 294 all events that occur in succession or recursion (by looking at the timestamps) for further 295 pattern mining. 296 In addition, when analyzing team sports, in contrast to single-athlete sports, different 297 data records may be sampled for different individual team members (e.g., in hockey, 298 defender vs. attacker, play-maker vs. striker and goalkeeper) or groups of members 299 (attackers, defenders, midfielders, etc.). Depending on the problem under study, these data 300 may also require certain descriptive conversion tasks. For instance, to understand the 301 common mistakes made by the defense of a football team, a coach may be interested in 302 knowing the formation or position of midfielders and attackers at the times that certain 303 mistakes that relate to them were made and find the best team strategy to reduce the 304 number of times that the team concedes a goal. In this particular case, there will be a need 305 for relating data records gathered for the players with respect to time of the contest. 

306 _The effect of the duration of an event on sports data pre-processing_ . The duration of 307 competitions is a factor that needs to be considered in combination with other specifics of 308 the sports when deciding about the type or amount of necessary data pre-processing. The 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 14 of 30** 

Data Mining Demands in Sports 14 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

309 RTS measures gathered in fixed-time and fixed-distance single-component single-player 310 sports e.g., judo, karate, fencing, and running, can potentially be the main data necessary 311 for performance analysis (this excludes multiple-component events such as triathlons 312 where, as mentioned before, times need to be converted to differential times). Other types 313 of fixed-time and fixed-distance events like football, hockey, rugby, and rowing may require 314 sophisticated pre-processing tasks such as those mentioned earlier in this paper. 315 In most variable-time events, RTS measures (i.e., pure times and scores referenced to 316 timestamps) are the main required data for actual data analysis. In tennis, for instance, it 317 is not necessarily required to convert time data related to balls (in tournaments played 318 under the International Tennis Federation rules, balls are changed after the first 9 games, 319 then after the next 11 games, then after the next 9 games, then after the next 11 games 320 etc.) or cumulative times of previous games into other formats. Similarly, the scores 321 (rather than times) are self-indicative of performances of athletes or teams in such sports. 322 In terms of multiple-effort sports, such as gymnastics and diving, the RTS measures, 323 as well as other performance measures e.g., body conformance in still rings or the amount 324 of water splash in diving (if explicitly available), are adequately evident of athletes’ 325 performances and may not require specific conversions or the extraction of new explicitly 326 available data. 

pre-processing tasks such as those mentioned earlier in this variable-time events, RTS measures (i.e., pure times and scores are the main required data for actual data analysis. In tennis, required to convert time data related to balls (in tournaments Tennis Federation rules, balls are changed after the next 11 games, then after the next 9 games, then after the next times of previous games into other formats. Similarly, the times) are self-indicative of performances of athletes or teams in of multiple-effort sports, such as gymnastics and diving, the performance measures e.g., body conformance in still rings or in diving (if explicitly available), are adequately evident of and may not require specific conversions or the extraction of _of winning criteria on sports data pre-processing_ . their effect in terms of data pre-processing, especially descriptive data are gathered, maintained, and reported during and after where scores decide the winner (e.g., karate and judo), in most 

327 _The effect of winning criteria on sports data pre-processing_ . Winning criteria in sports 328 demonstrate their effect in terms of data pre-processing, especially descriptive conversion, 329 in the way that data are gathered, maintained, and reported during and after major events. 330 In sports where scores decide the winner (e.g., karate and judo), in most cases, only 331 the scores are reported. In some cases, such as hockey, scores are tagged with timestamps. 332 Other statistics of games (e.g., forced/unforced turn overs, lost/gained positions) are also 333 reported. In general, however, if time-dependent aspects of the games are under question, 334 then certain data need to be converted or extracted. In football, for example, if one wants 335 to understand the likelihood of winning the game given that the team were behind in the 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 15 of 30** 

Data Mining Demands in Sports 15 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

336 first half, then analysts need to label other previous games with respect to the results of 337 the first halves, a task which may not be part of the original data collection. 

338 In sports where time is the winning criterion, such as marathon and middle-distance 339 running, time measures corresponding to each athlete (with their personal characteristics 340 and some physiological data) are mainly measured and reported. In some cases, this 341 requires an extensive search for athlete-specific data that are not explicitly reported. These 342 might include birth places and birth dates of subject athletes. Pre-processing is necessary 343 to analyze the more sophisticated aspects of these sports in terms of velocity and/or 344 time-related distance. An example of this is the work by Jones and Whipp (2002) in which 345 they calculated all the time-referenced velocity and distances from the paths taken by the 346 runners under study. 347 The nature of the pre-set number of scores to be achieved in variable-time sports, 348 such as in volleyball and tennis, makes the final scores to win less important compared to 349 other types of sports. This then puts the emphasis on during-the-game measures such as 350 the data related to individual athletes’ performances, individual scenarios of the games, or 351 the tactics that may lead to success. Some of these data are partially measured and 352 reported during major competitions and some can only be extracted from existing and 353 reported data. In terms of volleyball, the analysis of the probability of winning the game 354 given winning in certain sets (e.g., the first two sets) requires game tagging with respect to 355 the performances of the teams in the first and second sets as well as their final result. The 356 analysis of the capabilities of certain male tennis players in winning the grandslam tennis 357 games when they are behind by two sets, for example, also requires pre-processing of 358 existing data in terms of the results of each set in their games. This can be carried out by 359 labeling their games with the number of sets they have been behind (0, 1, or 2) as well as 360 their final result (won, lost). 

361 In multiple-effort sports, where only the scores of each attempt as well as the final 362 scores are reported, any data treatment may depend on the specific problem under study. 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 16 of 30** 

Data Mining Demands in Sports 16 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

363 Like in sports with pre-set numbers of scores (e.g., tennis and volleyball), in multiple-effort 364 events (e.g., diving), it may be necessary to extract during-the-game measures from 365 existing data before the data analysis step. The analysis of the likelihood of finishing an 366 event in 1<sup>_st_</sup> place given that the athlete had not performed their best in their first attempt 367 is an example of such analysis that requires extra data tagging with respect to the first 368 attempts and the final standings of the athletes. 

the final standings of the athletes. _Analysis_ earlier, the main data mining methods that have been are clustering, classification, relationship modeling, and rule is ultimately the questions posed in certain sports that drive method to be employed for performance analysis; however, the or individual sport must also be taken into consideration. **sport science viewpoint** , the analysis of sports performance analysis, is carried out with one (or a combination) of the performance patterns that describe how an athlete or a chances of finishing a competition in a certain position e.g., rowing races mostly finish each of the first three but this is not necessarily true for the last sector (Ofoghi et performances of an athlete or a team given information or training sessions e.g., a sport performance analyst whose horse has not participated in any major competition in 

369 _Sports Data Analysis_ 

370 As mentioned earlier, the main data mining methods that have been used in the 371 sports domain are clustering, classification, relationship modeling, and rule mining. We 372 believe that it is ultimately the questions posed in certain sports that drive the choice of 373 data mining method to be employed for performance analysis; however, the specifics of 374 each sport category or individual sport must also be taken into consideration. 375 **From a sport science viewpoint** , the analysis of sports performance data, in the 376 form of match analysis, is carried out with one (or a combination) of the following aims: 377 (a) Finding performance patterns that describe how an athlete or a team may 378 increase their chances of finishing a competition in a certain position e.g., boats that win 379 standard 2000-meter rowing races mostly finish each of the first three 500-meter sectors in 380 the fastest time, but this is not necessarily true for the last sector (Ofoghi et al., 2011b). 

381 (b) Predicting performances of an athlete or a team given information related to their 382 prior performances or training sessions e.g., a sport performance analyst might discover 383 that the rider whose horse has not participated in any major competition in the last three 384 months does not have a large chance of finishing a major horse riding race in the top three 385 positions. 

386 (c) Real-time decision-making on what re/actions or strategies to take in the course 387 of a current event e.g., how to adjust the positioning of football players on the field when 388 the team is one player short and one goal behind in the last 10 minutes of a major game. 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 17 of 30** 

Data Mining Demands in Sports 17 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

389 (d) Finding the main demands of certain sport competitions and selecting athletes 390 who can best address the demands e.g., the track cycling omnium is better performed by 391 riders with higher expertise in sprint-based events such as the flying time trial (Ofoghi et 392 al., 2010). 

393 While the first three items are mostly related to _short-term_ strategic planning for 394 achieving success in forthcoming or current events, the fourth item is mostly concerned 395 with a _long-term_ process towards talent identification, talent transfer (from one sport to 396 another), and athlete development to secure success in future competitions. 

in forthcoming or current events, the fourth item is mostly process towards talent identification, talent transfer (from athlete development to secure success in future competitions. **data analytical viewpoint** , each method within data mining clustering, etc.) can be implemented using different techniques be characterized in terms of three major characteristics: how easily the results achieved by employing a interpreted by data analytical experts and understood by who are not experts in the data analysis domain. how accurate and reliable are the results that are derived the degree to which a certain method can be utilized for problems with different parameters and/or different data. the aforementioned goals in sports performance analysis leads appropriate specific data analytical method while each data method has its characteristics in terms of 

397 **From a data analytical viewpoint** , each method within data mining 398 (classification, clustering, etc.) can be implemented using different techniques and each 399 technique can be characterized in terms of three major characteristics: 

400 i. Interpretability: how easily the results achieved by employing a certain method 401 can be interpreted by data analytical experts and understood by (sport) 402 professionals who are not experts in the data analysis domain. 

403 ii. Precision: how accurate and reliable are the results that are derived using this 404 technique. 

405 iii. Flexibility: the degree to which a certain method can be utilized for analyzing 406 certain problems with different parameters and/or different data. 

407 Each of the aforementioned goals in sports performance analysis leads to the necessity 408 of using an appropriate specific data analytical method while each data mining technique 409 for that specific method has its own characteristics in terms of interpretability, precision, 410 and flexibility. On the other hand, each sport performance analysis requirement demands 411 different levels of each technique characteristic. Therefore, to better describe this need, we 412 consider a rectangular model, as shown in Figure 1(b), for sports performance analysis. 

413 In this model, it is necessary to define two mappings in order to carry out insightful 414 performance analysis tasks: (a) the mapping between the data mining methods and the 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 18 of 30** 

Data Mining Demands in Sports 18 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

415 sports performance analysis requirements, and (b) the mapping between the sports 416 performance analysis requirements and the data mining technique characteristics. The 417 mapping between the data mining methods and data mining techniques, and also, the 418 mapping between the data mining techniques and the data mining technique 

419 characteristics, fall mostly in the computer science domain and, therefore, are out of the 420 scope of this study. 

study. (the top part) shows the mapping that we draw between the the sports performance analysis requirements. Performance is mainly carried out using clustering techniques and validated systems. Clustering techniques, in particular, are used when the performance has a major unknown component that is to be using clustering techniques for extracting performance patterns Jin, & Yan, 2007; Lamb, Bartlett, & Robins, 2010; Ofoghi & Bidgood, 2007). prediction, in comparison, is a task that is mainly addressed to predict an already known target class label for In the sports performance analysis context, performance data, it is then possible to predict the class label is no target performance class assigned. Predicting the three known categories novice, good [sub-elite], and elite) using linear discriminant analysis is a good example of 

421 Table 2 (the top part) shows the mapping that we draw between the data mining 422 methods and the sports performance analysis requirements. Performance pattern discovery 423 is a task that is mainly carried out using clustering techniques and validated by utilizing 424 classification systems. Clustering techniques, in particular, are used when the underlying 425 structure of performance has a major unknown component that is to be discovered. 426 Examples of using clustering techniques for extracting performance patterns are the works 427 in (Chen, Homma, Jin, & Yan, 2007; Lamb, Bartlett, & Robins, 2010; Ofoghi et al., 2010; 428 Woolf, Ansley, & Bidgood, 2007). 429 Performance prediction, in comparison, is a task that is mainly addressed using 430 classification systems and relationship modeling. Classification systems are suitable because 431 of their ability to predict an already known target class label for unseen/unknown data 432 instances. In the sports performance analysis context, once a classification system is trained 433 with labeled performance data, it is then possible to predict the class label for data records 434 for which there is no target performance class assigned. Predicting the performance level of 435 rowers (into three known categories novice, good [sub-elite], and elite) conducted by Smith 436 and Spinks (1995) using linear discriminant analysis is a good example of such analysis. 

437 Another avenue to performance prediction is relationship modeling between predictor 438 attributes and the dependent variable that represents performance. Major examples of this 439 approach include the studies carried out in (Edelmann-Nusser, Hohmann, & Henneberg, 440 2002; Johnson, Edmonds, Jain, & Jr., 2009; Kahn, 2003; Shao, 2009; Wilson et al., 2001). 441 Real-time decision-making (e.g., changing the line up or field positioning during a 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 19 of 30** 

Data Mining Demands in Sports 19 

1 2 3 4 442 game based on the progress during that contest) is a task that has been addressed to a 5 6 443 much lesser extent than other performance analysis areas. We believe the difficulty 7 8 444 involved in this task originates from the main barriers for using (semi) automated data 9 10 445 analytical methods in sports decision-making mentioned earlier. However, if this task is to 11 12 446 be tackled, then we believe it should mainly be addressed using relationship modeling 13 14 447 methods of data mining. Although there are sports in which some _basic_ descriptive 15 16 448 statistics are carried out and immediate inferences are made (e.g., having 3 inside 50s a 17 18 449 whole half, so obviously this is something to focus on in the second half), to perform 19 20 450 deeper analyzes in real time, there is not much space for conducting those that produce 21 22 451 results that are beneficial in the long term. Clustering, classification, and even rule mining 23 24 452 methods tend to produce results that can better be used prior to major events, such as 25 26 453 winning patterns, success event association and sequential patterns, and certain 27 28 454 performances likelihoods. Relationship modeling, in contrast, can be employed in real time 29 30 455 to integrate existing evidence based on the conditions and specifics of the current event and 31 32 456 produce likelihoods of certain outcomes based on which to re-adjust strategies, e.g., finding 33 34 457 the best strategy to maintain the lead in a football match in the last 20 minutes given the 35 36 458 opponent is not aggressively attacking. 37 38 459 There is a close relationship between performance pattern discovery and demand 39 40 460 analysis; therefore, demand analysis can also be more effectively conducted using clustering 41 42 461 and classification techniques. The relationship between the two tasks is mainly due to the 43 44 462 fact that performance patterns are, in many cases, among the most evident pieces of 45 46 47 463 information that impose demands on athletes to participate in specific sport competitions. 48 49 464 For instance, if in triathlon, the winning pattern implies finishing the running component 50 51 465 with the best performance, then the main demand (i.e., the key contributor to success in) 52 53 466 of this sport is to have excellence in running. Demand analysis for certain sports or 54 55 467 competitions may also be carried out in terms of other pieces of information such as 56 57 468 required prior training, nutrition, and physical strength that are not necessarily formulated 58 59 60 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 20 of 30** 

Data Mining Demands in Sports 20 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

469 in performance patterns. 

470 Table 2 (the bottom part) shows our mapping between the sports performance 471 analysis requirements and the data mining technique characteristics. In developing this 472 mapping, we considered three main aspects: (a) the amount of output information 473 generated by the analysis, (b) the rate of the reliance on the results by coaches and 474 athletes which is defined as how core the results are to making important decisions, and (c) 475 the time-frame within which the results produced by the analysis are to be utilized. These 476 three aspects influence the amount of the three technique characteristics required for sports 477 performance analysis. 

is defined as how core the results are to making important within which the results produced by the analysis are to be influence the amount of the three technique characteristics analysis. that generate large amounts of output information, generally, of the results. This enables end-users (i.e., those who science expertise, such as sports coaches) to better understand amounts of results of the analysis (e.g., the average RTS measures position in rowing). Whereas in cases where the output class label, for instance, there is less need for perfect example, in performance prediction in Alpine skiing, the output to predicted performances in terms of medal winner or does not necessitate much interpretability. of the reliance on the results mainly indicates the level of analysis requires to exhibit. Results that are core to decision to be relied on very heavily require a high level of precision. performance pattern discovery, although still the highest 

478 Processes that generate large amounts of output information, generally, need higher 479 levels of interpretability of the results. This enables end-users (i.e., those who may have 480 less computer science expertise, such as sports coaches) to better understand and make use 481 of the large amounts of results of the analysis (e.g., the average RTS measures required for 482 finishing in second position in rowing). Whereas in cases where the output information is 483 only a predicted class label, for instance, there is less need for perfect interpretability in the 484 results. As an example, in performance prediction in Alpine skiing, the output information 485 can be limited to predicted performances in terms of medal winner or non-medal winner 486 rankings which does not necessitate much interpretability. 487 The rate of the reliance on the results mainly indicates the level of precision that a 488 data mining analysis requires to exhibit. Results that are core to decision making and are 489 thus anticipated to be relied on very heavily require a high level of precision. In some 490 analyzes e.g., performance pattern discovery, although still the highest accuracy is desired 491 and the output information is insightful, there is some space for employing and developing 492 alternative plans (risk management). This reduces the rate of the reliability of the results 493 and therefore the required level of precision. 

494 The time-frame within which to utilize the results of the analyzes directly affects the 495 required level of flexibility characteristic of a technique. The longer the time-frame of 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 21 of 30** 

Data Mining Demands in Sports 21 

1 2 3 4 496 utilizing the results of the analyzes is, the more flexibility is desired and is useful to conduct 5 6 497 a series of experiments with different settings and data, testing and refining the results. In 7 8 498 short-term processes e.g., real-time decision-making tasks; however, less flexibility will 9 10 499 damage the effectiveness and efficiency of the performance analysis task to a lesser extent. 11 12 13 500 **Conclusion** 14 15 16 501 Performance analysis in terms of different elite sports implies different data 17 18 502 pre-processing and data analysis techniques. Data pre-processing is more influenced by the 19 20 503 category of sports where different features of the sports (i.e., the number of individual 21 22 504 events in a competition, the number of players in the games, the duration of the games, 23 24 505 and the winning criteria) necessitate different pre-processing tasks. 25 26 506 Data analysis that comes after data pre-processing is more influenced by the type of 27 28 507 problem being tackled in the sports performance analysis. Performance pattern discovery, 29 30 508 performance prediction, real-time decision-making, and demand analysis problems are 31 32 509 often better carried out using different data mining methods and require different 33 34 510 interpretability, precision, and flexibility measures. 35 36 511 To cover all of the aspects of sports performance analysis in a general structure, we 37 38 512 presented a rectangular model bringing together performance analysis requirements, data 39 40 513 mining methods, data mining techniques, and technique characteristics. This 41 42 514 inter-connected rectangular model requires sufficient attention before conducting practical 43 44 515 and useful performance analysis tasks. The mappings that we discussed between some of 45 46 516 the main elements in this model suggest what data mining methods and techniques suit for 47 48 517 which sports performance analysis problems. 49 50 518 Our review on the different data analytical demands of different elite sports is an 51 52 519 unprecedent effort to shed more light on different aspects of the use of sophisticated data 53 54 520 analysis and mining methods in the domain of sports performance analysis. This will 55 56 521 eventually assist both data analysts and sport professionals to more effectively collaborate 57 58 59 60 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 22 of 30** 

Data Mining Demands in Sports 22 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

522 and enhance their understanding of a variety of participant factors that contribute to 523 success in sport events at different levels. 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 23 of 30** 

Data Mining Demands in Sports 23 

1 2 

- 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 

21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

# **References** 

524 

- 525 Agrawal, R., Imielinski, T., & Swami, A. (1993, June). Mining association rules between 526 sets of items in large databases. _SIGMOD Rec._ , _22_ (2), 207–216, 

- 526 527 DOI: 10.1145/170036.170072. Available from 

- 527 528 `http://doi.acm.org/10.1145/170036.170072` 

& Srikant, R. (1995). Mining sequential patterns. In _Proceedings international conference on data engineering_ (pp. 3–14). Taipei, R. (2007). Different centre of pressure patterns within the analysis. _Journal of Sports Sciences_ , 757–770, 10.1080/02640410600874971. Colet, E., Parker, J., Pines, Z., Pratap, R., & Ramanujam, K. scout: Data mining and knowledge discovery in nba data. _Discovery_ , _1_ (1), 121–125, DOI: 10.1023/A:1009782106822. Performance analysis: What is performance analysis, and within the coaching process to benefit performance? _Peak_ from `http://www.pponline.co.uk/encyc/ sports-performance-analysis-coaching-and-training-39` H., Jin, C., & Yan, H. H. (2007). Identification of elite using cluster analysis. _International Journal of Sports Science_ , _2_ (3), 293–303, DOI: 10.1260/174795407782233083. R. (2002). An analysis of decathlon data. _Journal of the Society_ , _51_ (2), 179–187, DOI: 10.1111/1467-9884.00310. 

- 529 Agrawal, R., & Srikant, R. (1995). Mining sequential patterns. In _Proceedings of the_ 530 _eleventh international conference on data engineering_ (pp. 3–14). Taipei, Taiwan. 

- 531 Ball, K., & Best, R. (2007). Different centre of pressure patterns within the golf stroke i: 532 Cluster analysis. _Journal of Sports Sciences_ , 757–770, 533 DOI: 10.1080/02640410600874971. 

- 534 Bhandari, I., Colet, E., Parker, J., Pines, Z., Pratap, R., & Ramanujam, K. (1997). 535 Advanced scout: Data mining and knowledge discovery in nba data. _Data Mining_ 536 _and Knowledge Discovery_ , _1_ (1), 121–125, DOI: 10.1023/A:1009782106822. 

- 536 , 537 Bishop, D. (2003). Performance analysis: What is performance analysis, and how can it be 538 integrated within the coaching process to benefit performance? _Peak Performance_ , 539 4–7. Available from `http://www.pponline.co.uk/encyc/` 540 `sports-performance-analysis-coaching-and-training-39` 

541 Chen, I., Homma, H., Jin, C., & Yan, H. H. (2007). Identification of elite swimmers’ race 542 patterns using cluster analysis. _International Journal of Sports Science and_ 543 _Coaching_ , _2_ (3), 293–303, DOI: 10.1260/174795407782233083. 

544 Cox, T., & Dunn, R. (2002). An analysis of decathlon data. _Journal of the Royal_ 545 _Statistical Society_ , _51_ (2), 179–187, DOI: 10.1111/1467-9884.00310. 

- 546 Edelmann-Nusser, J., Hohmann, A., & Henneberg, B. (2002). Modeling and prediction of 

- 547 competitive performance in swimming upon neural networks. _European Journal of_ 548 _Sport Science_ , _2_ (2), 1–10, DOI: 10.1080/17461390200072201. 

549 Fayyad, U., Piatetsky-Shapiro, G., & Smyth, P. (1996). The kdd process for extracting 

550 useful knowledge from volumes of data. _Communications of the ACM_ , _39_ (11), 27–34, 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 24 of 30** 

1 2 3 4 5 6 7 8 9 10 

Data Mining Demands in Sports 24 

551 DOI: 10.1145/240455.240464. 

11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

- 552 Fiedler, K., Brinkmann, B., Betsch, T., & Wild, B. (2000). A sampling approach to biases 553 in conditional probability judgments: Beyond baserate neglect and statistical format. 554 _Journal of Experimental Psychology: General_ , _129_ (3), 399–418. 

554 

- 555 Gaudreau, P., & Blondin, J.-P. (2004). Different athletes cope differently during a sport 

a cluster analysis of coping. _Personality and Individual_ 1865–1877, DOI: 10.1016/j.paid.2003.08.017. Available from `http://www.sciencedirect.com/science/article/B6V9F-49TRJYD-9/ 2/3c8754c3b4426ec0e38d6032cd343bad` Mendoza, L., & Schllhorn, W. (2001). Analysis of the long jump from approach to takeoff based on time-continuous _Journal of Sport Science_ , _1_ (5), 1–11. Y., & Huiqun, Z. (2010). Study of association rule action of ball games. In _Proceedings of the 2010 international technology and mechatronics automation (icmtma 2010)_ (pp. China. Edmonds, W., Jain, S., & Jr., J. C. (2009). Analysis of elite and their respective between-gender differences over time. _Analysis in Sports_ , _5_ (4), Article 2, DOI: Whipp, B. (2002). Bioenergetic constraints on tactical decision distance running. _British Journal of Sports Medicine_ , _32_ , 10.1136/bjsm.36.2.102. 

556 competition: a cluster analysis of coping. _Personality and Individual Differences_ , 557 _36_ (8), 1865–1877, DOI: 10.1016/j.paid.2003.08.017. Available from 

558 `http://www.sciencedirect.com/science/article/B6V9F-49TRJYD-9/` 559 `2/3c8754c3b4426ec0e38d6032cd343bad` 

560 Jaitner, T., Mendoza, L., & Schllhorn, W. (2001). Analysis of the long jump technique in 561 the transitions from approach to takeoff based on time-continuous kinematic data. 562 _European Journal of Sport Science_ , _1_ (5), 1–11. 

562 , 563 Jing, S., Wenshuang, Y., & Huiqun, Z. (2010). Study of association rule mining on 564 technical action of ball games. In _Proceedings of the 2010 international conference on_ 565 _measuring technology and mechatronics automation (icmtma 2010)_ (pp. 539–542). 566 Changsha, China. 

567 Johnson, M., Edmonds, W., Jain, S., & Jr., J. C. (2009). Analysis of elite swimming 568 performances and their respective between-gender differences over time. _Journal of_ 569 _Quantitative Analysis in Sports_ , _5_ (4), Article 2, DOI: 10.2202/1559-0410.1186. 

570 Jones, A., & Whipp, B. (2002). Bioenergetic constraints on tactical decision making in 571 middle distance running. _British Journal of Sports Medicine_ , _32_ , 102–104, 572 DOI: 10.1136/bjsm.36.2.102. 

573 Kahn, J. (2003). _Neural network prediction of nfl games_ (Tech. Rep.). University of 574 Wisconsin Electrical and Computer Engineering Department. 

575 Kenny, I., Sprevak, D., Sharp, C., & Boreham, C. (2005). Determinants of success in the 576 olympic decathlon: Some statistical evidence. _Journal of Quantitative Analysis in_ 577 _Sports_ , _1_ (1), Article 3. 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 25 of 30** 

Data Mining Demands in Sports 25 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

- 578 Kline, C., Durstine, J., Davis, J., Moore, T., Devlin, T., Zielinski, M., & Youngstedt, S. 579 (2007). Circadian variation in swim performance. _Journal of Applied Physiology_ , 580 _102_ , 641–649, DOI: 10.1152/japplphysiol.00910.2006. 

- 581 Lamb, P., Bartlett, R., & Robins, A. (2010). Self-organising maps: An objective method 582 for clustering complex human movement. _International Journal of Computer Science_ 583 _in Sport_ , _9_ , 20–29. 

, _9_ , 20–29. Tactics analysis on women swimming athletes in the 800m race using speed coefficient theory. In _Proceedings of on knowledge discovery and data mining_ (pp. 453–456, 10.1109/WKDD.2008.145). Adelaide, Australia. _Motor learning and control: Concepts and applications_ McGraw-Hill. Zeleznikow, J., & MacMahon, C. (2011a). A machine learning component analysis. In _Proceedings of the international science in sport_ (pp. 30–33). Shanghai, China. Zeleznikow, J., & MacMahon, C. (2011b). Probabilistic modeling rowing split measures to support strategy and pacing in race _Journal of Performance Analysis in Sport_ , _11_ (2), 239–253. Zeleznikow, J., MacMahon, C., & Dwyer, D. (2010). A machine to predicting winning patterns in track cycling omnium. In _federation for information processing (ifip) conference and communication technology_ (pp. 67–76). Brisbane, 

- 584 Liao, T. (2008). Tactics analysis on women swimming athletes in the 800m freestyle 585 swimming race using speed coefficient theory. In _Proceedings of international_ 586 _workshop on knowledge discovery and data mining_ (pp. 453–456, 587 DOI: 10.1109/WKDD.2008.145). Adelaide, Australia. 

- 587 588 Magill, R. (2007). _Motor learning and control: Concepts and applications_ (8th ed.). New 589 York, NY: McGraw-Hill. 

- 590 Ofoghi, B., Zeleznikow, J., & MacMahon, C. (2011a). A machine learning approach to 591 triathlon component analysis. In _Proceedings of the international symposium on_ 592 _computer science in sport_ (pp. 30–33). Shanghai, China. 

593 Ofoghi, B., Zeleznikow, J., & MacMahon, C. (2011b). Probabilistic modeling to give advice 594 about rowing split measures to support strategy and pacing in race planning. 595 _International Journal of Performance Analysis in Sport_ , _11_ (2), 239–253. 596 Ofoghi, B., Zeleznikow, J., MacMahon, C., & Dwyer, D. (2010). A machine learning 597 approach to predicting winning patterns in track cycling omnium. In _Proceedings of_ 598 _the international federation for information processing (ifip) conference on advances_ 599 _in information and communication technology_ (pp. 67–76). Brisbane, Australia. 600 Pollard, G., & Pollard, G. (2010). Four ball best ball 1. _Journal of Sports Science and_ 601 _Medicine_ , _9_ (1), 86–91. 

602 Ransdell, L., Vener, J., & Huberty, J. (2009). Masters athletes: An analysis of running, 603 swimming and cycling performance by age and gender. _Journal of Exercise Science_ 604 _and Fitness_ , _7_ (2), S61–S73, DOI: 10.1016/S1728-869X(09)60024-1. 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 26 of 30** 

Data Mining Demands in Sports 26 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

605 Schumaker, R. P., Solieman, O. K., & Chen, H. (2010). _Sports data mining_ (Vol. 26). New 606 York, NY: Springer. 

607 Shao, S. (2009). Application of bp neural network model in sports aerobics performance 608 evaluation. In _Proceedings of the 2009 pacific-asia conference on knowledge_ 609 _engineering and software engineering_ (pp. 33–35). Shenzhen, China. 

& Spinks, W. L. (1995). Discriminant analysis of biomechanical novice, good and elite rowers. _Journal of Sports Sciences_ , _13_ M., & Sampaio, J. (2010). Rugby game-related statistics between winning and losing teams in irb and super twelve _of Sports Science and Medicine_ , _9_ , 51–55. V., Aggeloussis, N., Kasimatis, P., Christoforidis, C., Underwater stroke kinematics during breathing and swimming. _Journal of Sport Science and Medicine_ , _6_ , 58–62. (1988). Discriminant analysis of the physiques of schoolboy rugby and non-team members. _Journal of Sports Sciences_ , _6_ (2), M., & Ericsson, K. A. (2005). Perceptual-cognitive expertise in when applying the expert performance approach. _Human 24_ (3), 283–307, DOI: 10.1016/j.humov.2005.06.002. B., Cossor, J., Arellano, R., Chatard, J.-C., & Riewald, between stroke efficiency measures and freestyle swimming An analysis of freestyle swimming events at the sydney _of biomechanics symposia_ (pp. 79–82). University of San 

610 Smith, R. M., & Spinks, W. L. (1995). Discriminant analysis of biomechanical differences 611 between novice, good and elite rowers. _Journal of Sports Sciences_ , _13_ (5), 377–385. 612 Vaz, L., Rooyen, M., & Sampaio, J. (2010). Rugby game-related statistics that 

613 discriminate between winning and losing teams in irb and super twelve close games. 614 _Journal of Sports Science and Medicine_ , _9_ , 51–55. 

615 Vezos, N., Gourgoulis, V., Aggeloussis, N., Kasimatis, P., Christoforidis, C., & Mavromatis, 616 G. (2007). Underwater stroke kinematics during breathing and breath-holding front 617 crawl swimming. _Journal of Sport Science and Medicine_ , _6_ , 58–62. 

618 Watson, A. (1988). Discriminant analysis of the physiques of schoolboy rugby players, 619 hurlers and non-team members. _Journal of Sports Sciences_ , _6_ (2), 131–140. 620 Williams, A. M., & Ericsson, K. A. (2005). Perceptual-cognitive expertise in sport: Some 621 considerations when applying the expert performance approach. _Human Movement_ 622 _Science_ , _24_ (3), 283–307, DOI: 10.1016/j.humov.2005.06.002. 623 Wilson, B., Mason, B., Cossor, J., Arellano, R., Chatard, J.-C., & Riewald, S. (2001). 624 Relationships between stroke efficiency measures and freestyle swimming 625 performance: An analysis of freestyle swimming events at the sydney 2000 olympics. 626 In _Proceedings of biomechanics symposia_ (pp. 79–82). University of San Francisco. 

627 Woolf, A., Ansley, L., & Bidgood, P. (2007). Grouping of decathlon disciplines. _Journal of_ 628 _Quantitative Analysis in Sports_ , _3_ (4), Article 5, DOI: 10.2202/1559-0410.1057. 

629 Available from `http://ideas.repec.org/a/bpj/jqsprt/v3y2007i4n5.html` 

630 Zwols, Y., & Sierksma, G. (2009). Training optimization for the decathlon. _Journal of_ 631 _Operations Research_ , _57_ (4), 812–822, DOI: 10.1287/opre.1080.0616. 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 27 of 30** 

Data Mining Demands in Sports 27 

|1<br>2<br>3<br>4<br>5<br>6<br>7<br>|Table 1<br>_Utilization of cluste_<br>_domain_|_ring, classifcation, and relatio_|<br>_nship modeling tec_|<br>_hniques in the s_|
|---|---|---|---|---|
|8<br>9<br>|Method|Researcher|Technique|Sport|
|10<br>|Clustering|Gaudreau & Blondin (2004)|Ward|golf|
|11<br>12||Ball & Best (2007)|k-means|golf|
|13<br>14<br>||<br>Chen et al. (2007)|<br>average<br>linkage<br>(hierarchical)|<br>swimming|
|15<br>||<br>Woolf et al. (2007)|<br>mixed|<br>decathlon|
|16<br>17||<br><br>Lamb et al. (2010)|<br>self organizing|<br>basketball|
|18|||<br>maps||
|19<br>||<br>Ofoghi et al. (2010)|<br>k-means|<br>track cycling|
|20<br>21|<br>Classifcation|<br>Ofoghi et al. (2010)|<br>Naive Bayes|<br>track cycling|
|22||<br>Watson (1988)|<br>linear|<br>rugby|
|23|||<br>discriminant||
|24|||<br>analysis||
|25<br>||<br>Smith & Spinks (1995)|<br>linear|<br>rowing|
|26<br>27|||<br>discriminant||
|28|||<br>analysis||
|29||<br>Jaitner, Mendoza, &|<br>linear|<br>long jump|
|30<br>||<br>Schllhorn (2001)|<br>discriminant||
|31|||<br>li||
|32|||<br>anayss||
|33<br>|<br>Relationship<br>|<br>Wilson et al. (2001)|<br>linear regression|<br>swimming|
|34|<br>modeling||||
|35<br>||<br>Johnson et al. (2009)|<br>linear and|<br>swimming|
|36<br>37|||<br>polynomial<br>||
|38|||<br>regression||
|39<br>||<br>Edelmann-Nusser et al.<br>|<br>neural networks|<br>swimming|
|40||<br>(2002)|||
|41<br>42||<br><br>Shao (2009)|<br>neural networks|<br>aerobics|
|43||<br>Kahn (2003)|<br>neural networks|<br>football (NFL)|
|44|||||
|45<br>|||||
|46|||||
|47|||||
|48|||||
|49<br>50<br>51<br>52|||||
|53|||||
|54<br>55|||||
|56|||||
|57<br>58|||||
|59<br>60|||||



_Utilization of clustering, classification, and relationship modeling techniques in the sports domain_ 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 28 of 30** 

Data Mining Demands in Sports 28 

1 2 

3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

# Table 2 

_The mapping between sports performance analysis requirements and major data mining methods and the mapping between the sports performance analysis requirements and the data mining technique characteristics_ 

|Sports performance||Data mining|methods||
|---|---|---|---|---|
|<br>analysis requirements|<br>clustering<br>|<br>classifcation<br>|<br>relationship<br>modeling|<br>rule mining|
|<br>performance pattern|<br>_~~√~~_|<br>_~~√~~_|<br>–|<br>–|
|<br>discovery|||||
|<br>performance prediction|<br>–|<br>_√_|<br>_√_|<br>–|
|**r**<br>real-time<br>decision-making|<br>–|<br>–|<br>_√_|<br>_√_|
|<br>demand analysis|<br>_√_|<br>_√_|<br>–|<br>–|
||**e**<br>Data minin<br>|<br>g technique char|<br>acteristics<br>||
||<br>interpretability|<br>precision|<br>fexibility||
|<br>performance pattern|<br>high|<br>moderate|<br>moderate||
|<br>discovery|||||
|<br>performance prediction|<br>low|<br>high|<br>high||
|<br>real-time<br>decision-making|<br>very high|<br>high|<br>very low||
|<br>demand analysis|<br>moderate|**view**<br>moderate|**Only**<br>moderate||



**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 29 of 30** 

Data Mining Demands in Sports 29 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

# **Figure Captions** 

632 

633 _Figure 1._ (a) The sport performance analysis scheme involving the sports domain and the 634 data mining domain, (b) The rectangular model characterizing the data mining approach 635 towards sports performance analysis 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 

**Measurement in Physical Education and Exercise Science** 

**Page 30 of 30** 

Data Mining Demands in Sports 30 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

(a) **Sports space/domain DM space/domain** rules rankings regulations times tactics scores strategies ..................................... conditions pre-processing methods performances analysis methods abilities 

## performance analysis mapping 

domain knowledge inheritance (b) _clustering i.e., e.g., k-means classification decision trees relationship modeling bayesian networks rule mining_ **Major data mining Data mining** _support vector machines_ **methods techniques** _regression analysis etc._ Sports performance analysis using data mining methods **Sports performance analysis Data mining technique requirements characteristics** _performance pattern discovery interpretability i.e., performancereal-time decisionpredictionmaking i.e., precisionflexibility demand analysis_ 

**URL: http://mc.manuscriptcentral.com/hmpe  Email: t.lam@csuohio.edu** 


