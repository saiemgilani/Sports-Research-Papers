<!-- source: library/journals/Wharton Sports Analytics Journal/2026/2026 - Real-Time Basketball Jumpshot Detection on iOS A Comparative Analysis of Linear Regression and Random Forest Classification Using Apple s Vi - Meng.pdf -->
<!-- item: https://wsb.wharton.upenn.edu/real-time-basketball-jumpshot-detection-on-ios/ -->
<!-- issue: Wharton Sports Analytics Journal, Spring 2026 -->
<!-- authors: Davis Meng -->
<!-- machine conversion from the stored PDF via pdftotext + scripted reflow, 2026-10-04; equations, tables and figures are NOT preserved - consult the PDF for those -->

Real-Time Basketball Jumpshot Detection on iOS: A

Comparative Analysis of Linear Regression and Random

Forest Classification Using Apple's Vision Framework

By: Davis Meng

## 5 Author Biography

6 Davis Meng is currently a sophomore at The Groton School in Massachusetts with demonstrated 7 expertise in machine learning, computer vision, and iOS development. His research focuses on 8 applying artificial intelligence to sports analytics, with published work in the Curieux academic 9 journal on pose estimation for basketball shot analysis.

10 Abstract 11 Modern basketball increasingly demands the skill of precise shooting. However, accessible tools 12 for analyzing shooting mechanics remain limited due to the lack of resources and reliability. This 13 study addresses this gap by developing and comparing two machine learning approaches for real14 time basketball jumpshot detection on consumer iOS devices. Building upon previous MediaPipe15 based research that achieved basic success, this work transitions to Apple's native Vision 16 framework. It leverages hardware-optimized pose detection to enable practical on-device analysis.

17 Through systematic collection and annotation of basketball shooting footage, biomechanical 18 features were extracted from body pose landmarks. These features capture the essential mechanics 19 of any given jumpshot. Then, two contrasting machine learning architectures were developed and 20 evaluated. Linear Regression was chosen for computational efficiency versus Random Forest for 21 classification accuracy. They were evaluated for both predictive performance and real-world 22 computational feasibility on mobile hardware.

23 The findings reveal a fundamental trade-off in mobile sports analytics. Linear Regression enables 24 fluid, real-time feedback suitable for live training scenarios. Meanwhile, Random Forest provides 25 substantially superior accuracy for post-session video analysis. Feature importance analysis 26 consistently identified elbow positioning as the dominant biomechanical indicator across both 27 models. This validates fundamental basketball coaching principles. Most significantly, thoughtful 28 feature engineering based on domain knowledge produced dramatic improvements over generic 29 statistical approaches. It demonstrates that understanding sport-specific mechanics outweighs raw 30 computational power.

31 This research establishes that sophisticated basketball shot analysis can operate entirely on 32 smartphones without specialized equipment. This could potentially democratize access to 33 personalized coaching feedback for athletes at all levels.

34 Keywords: iOS Development, Apple Vision Framework, Sports Analytics, Pose Detection, 35 Linear Regression, Random Forest, Real-Time Classification, Basketball Shot Detection, Mobile 36 Machine Learning, On-Device Inference

## 37 Introduction

The evolution of mobile computing has fundamentally transformed what is possible in

39 sports training. Smartphones now possess computational capabilities that rival those of desktop

40 computers from just a few years ago. This allows for sophisticated machine learning applications

41 to run entirely locally on the device. For sports analytics, this shift from cloud-based to local

42 processing offers transformative advantages. These include real-time feedback with minimal

43 latency, enhanced privacy through local data processing, elimination of internet connectivity

44 requirements, and dramatically lower operational costs, having no need to run cloud services.

This study explores how these technological advances enable practical basketball shot

46 detection and analysis on iOS devices. Building upon previous research utilizing MediaPipe for

47 pose estimation (Meng 2024), this work leverages Apple's native Vision framework. This

48 framework is specifically optimized for iOS hardware through the Neural Engine, as it is used to

49 overcome the performance limitations inherent in cross-platform solutions.

The central challenge in mobile sports analytics lies in balancing classification accuracy

51 against computational constraints. Basketball jumpshot detection must process video at 30 to 60

52 frames per second, requiring extracting pose landmarks, engineering biomechanical features, and

53 performing model inference. All of this must happen while maintaining responsive real-time

54 feedback. This study directly compares two fundamentally different approaches to this challenge.

55 Linear Regression offers computational simplicity and speed. Random Forest Classification

56 provides superior accuracy through ensemble learning at a higher computational cost.

This research investigates three core questions. How do Linear Regression and Random

58 Forest models compare for jumpshot detection accuracy? Can either approach achieve true real-

59 time performance on modern iOS devices? Which biomechanical features extracted from pose data

60 most reliably predict jumpshot events? By answering these questions, this study establishes

61 practical guidelines for deploying machine learning based sports analytics on mobile platforms,

62 emphasizing the accuracy efficiency trade-offs that govern real-world deployment decisions.

## 63 Literature Review

The application of machine learning pose estimation to sports analytics has expanded

65 rapidly in recent years, though significant challenges remain. Roggio et al. (2024) conducted a

66 narrative review of major pose estimation models, including OpenPose, MediaPipe, BlazePose,

67 and HRNet, across clinical, sports, and ergonomic contexts. While they found compelling potential

68 for non-invasive, cost-effective biomechanical assessment, the review identified persistent

69 challenges in accuracy, data quality, and integration into existing practices, concluding that

70 standardized evaluation frameworks remain essential for reliable applications. Complementing

71 this broad survey, Dedhia et al. (2024) evaluated MediaPipe BlazePose as a virtual gym assistant

72 and found it achieved accuracy within 10% of IMU-based motion capture for curated fitness

73 movements, demonstrating practical applicability in training contexts. However, the authors noted

74 limitations in complex motion scenarios, suggesting that more dynamic movements like those in

75 competitive sports may demand further refinement.

The gap between controlled and competitive environments has been well documented.

77 Cronin et al. (2023) tested OpenPose on footage from the 2017 World Athletics Championships

78 long jump finals and found poor agreement with manual analysis, producing an average ICC

79 (Intraclass Correlation Coefficient) of only 0.17 across variables, concluding that the framework

80 is unsuitable for in-competition biomechanical analysis. In response to such accuracy limitations,

81 Xi et al. (2024) developed a dual-channel spatiotemporal transformer architecture integrated with

82 IoT devices for sports training, achieving mean per joint position scores of 42.2 mm and 29.1 mm

83 on the Human3.6M and MPI-INF-3DHP datasets, respectively, significantly outperforming

84 existing methods. Their work represents an important future direction for capturing temporal

85 dynamics in movement analysis.

Despite limitations in competitive settings, validation studies have demonstrated that pose

87 estimation can achieve acceptable accuracy for specific, well-defined tasks. Ino et al. (2024)

88 compared OpenPose against 3D motion analysis and human manual analysis for measuring knee

89 valgus during drop vertical jumps, finding no significant difference between AI-based and human-

90 based methods (mean absolute errors of 2.4° and 3.2°, respectively). Fukushima et al. (2024)

91 provided broader cross-sport validation by comparing OpenPose against marker-based motion

92 capture across seventeen athletic movements, including basketball chest passes. Their results

93 showed systematic joint angle errors during rapid or complex movements, reinforcing the need for

94 sport-specific validation rather than reliance on general accuracy benchmarks. Tharatipyakul et al.

95 (2024), reviewing 45 articles on pose estimation feedback systems, found that CNNs

96 (Convolutional Neural Networks) dominated pose detection while assessment methods ranged

97 from mathematical formulas to machine learning classification, and observed a notable shift from

98 OpenPose to MediaPipe as the most widely adopted framework.

The present study builds directly upon the author's prior research (Meng, 2024), which

100 used MediaPipe's 33-landmark model and Random Forest classification to predict basketball

101 shotmaking accuracy from single-camera video. That study achieved 100% training accuracy but

102 only 51.1% test accuracy on 126 annotated clips, identifying key limitations: the insufficiency of

103 static statistical feature aggregation for capturing shooting dynamics, limited dataset size, and

104 processing times incompatible with real-time feedback. The current work addresses these gaps by

105 transitioning to Apple's native Vision framework (Apple Developer Documentation, 2023), which

106 leverages the Neural Engine for hardware-optimized pose detection of 17 body landmarks. Though

107 fewer than MediaPipe's 33 points, this reduced landmark set, combined with domain-informed

108 biomechanical feature engineering, over 8,000 annotated frames, and a comparative evaluation of

109 Linear Regression versus Random Forest, yields both substantially improved accuracy and

110 practical guidelines for the accuracy–efficiency trade-offs governing real-time mobile deployment.

111 No prior study has systematically quantified these trade-offs for basketball shot detection on

112 consumer iOS hardware, establishing the gap this research fills.

## 113 Methodology

## 114 Data Collection and Annotation

Video footage was captured using the iPhone's rear camera at 1080p resolution and 30

116 frames per second. The camera was positioned approximately 12 feet from the shooting location

117 at chest height. Eight video sessions were recorded. Each contained 10 to 15 jumpshot attempts

118 interspersed with non-shooting movements. These included walking, dribbling, and standing. This

119 variety was essential to train models for distinguishing actual jumpshots from other basketball-

120 related activities.

Manual temporal annotation established ground truth labels. Jumpshot events were defined

122 from initial knee flexion through ball release. Annotations were compiled into CSV (Comma

123 Separated Value) files with precise timestamp ranges. This ultimately yielded 8,410 annotated

124 frames comprising 2,541 jumpshot frames and 5,869 non-jumpshot frames.

## 125 Pose Detection with Apple's Vision Framework

Unlike the MediaPipe implementation from previous research, this study utilized Apple's

127 Vision framework. This provides 17 body landmarks. These are the nose, eyes, ears, shoulders,

128 elbows, wrists, hips, knees, and ankles. The Vision framework processes frames asynchronously

129 through a specific API and returns normalized coordinates for each detected landmark along with

130 confidence scores.

A Python extraction pipeline processed annotated video segments frame by frame. It stored

132 landmark coordinates with associated metadata, including clip ID, frame number, timestamp, and

133 ground truth label.

## 134 Biomechanical Feature Engineering

Raw landmark coordinates alone provide insufficient discriminative power. This is because

136 absolute positions vary with camera placement, shooter height, and distance. To address this, 19

137 engineered features were computed from raw landmarks. These were designed to capture

138 biomechanical patterns invariant to these factors. Static spatial features included arm angles,

139 normalized wrist and head heights, elbow displacement components, knee bend angles, body

140 center position, head tilt, shoulder width, and body lean. Temporal dynamic features captured

141 movement patterns. This was done through velocity and acceleration measurements of key body

142 points across rolling time windows.

All spatial features were normalized using torso length as a reference measurement. This

144 enabled generalization across different shooters and camera configurations. Missing landmark data

145 occurred in approximately 3% of frames due to occlusion. This was handled through linear

146 interpolation with forward and backward filling.

## 147 Model Training and Comparison

The complete dataset was split 70/30 into training and testing sets. Stratified sampling was

149 used to maintain class distribution. Feature standardization was applied using StandardScaler.

150 Parameters were fitted exclusively on training data to prevent data leakage.

Linear Regression was implemented using scikit learn's LinearRegression class without

152 regularization. Despite the binary classification task, this approach was selected for its

153 computational simplicity and interpretability. Predictions were thresholded at 0.5 for binary

154 classification. Performance was evaluated using the R² score alongside traditional classification

155 metrics.

Random Forest Classification utilized scikit learn's RandomForestClassifier with 100

157 estimators and unrestricted depth. This ensemble approach aggregates predictions from 100

158 decision trees trained on bootstrap samples. This provides robustness to overfitting while

159 maintaining interpretability through feature importance scores. Both models were evaluated on 160 accuracy, precision, recall, F1 score, and 10-fold cross-validation performance.

161 iOS Integration and Performance Benchmarking

Models were exported for iOS integration. Linear Regression was exported as JSON

163 containing coefficients and scaler parameters. Random Forest was exported as Core ML format. It

164 was automatically converted to optimized Swift code by Xcode.

The iOS application implements a complete processing pipeline. This includes video

166 capture at 30 FPS through AVFoundation, pose detection via Vision framework, feature extraction

167 in Swift, model inference, and event clustering. Clustering groups of consecutive high probability

168 frames. Performance was measured on iPhone 13 Pro using Xcode's Instruments profiling tool. It

169 captured per-frame processing time, sustained frame rate, memory usage, battery consumption,

170 model size, and loading time.

## 171 Results and Discussion

## 172 Model Performance Comparison

The Random Forest Classifier substantially outperformed Linear Regression across all

174 metrics. Random Forest achieved strong test accuracy with high precision and good recall. Linear

175 Regression showed modest performance with R² scores indicating limited explanatory power. The

176 10-fold cross-validation confirmed Random Forest's robust generalization with minimal variance.

Linear Regression's relatively low accuracy suggests that jumpshot classification involves

178 substantial nonlinear relationships. These are not captured by linear models. The Random Forest

179 model's perfect training accuracy initially raised overfitting concerns. However, strong test

180 performance and cross-validation results indicate genuine learning of generalizable patterns.

## 181 Feature Importance Insights

Both models consistently identified elbow horizontal position as the dominant predictive

183 feature. Its importance scores far exceeded those of other variables. This finding validates

184 fundamental basketball coaching principles. These principles emphasize proper elbow alignment

185 during shooting form. Body center vertical position, elbow vertical position, and head tilt provided

186 secondary discriminative power.

Notably, spatial features capturing body configuration at individual time points dominated

188 over temporal features. Temporal features measure movement patterns across frames. This

189 suggests that jumpshot classification relies more on specific body positioning than on movement

190 dynamics. This is an insight with important implications for feature engineering in similar

191 applications.

## 192 Computational Performance Analysis

Linear Regression achieved genuine real-time performance on iPhone 13 Pro. It processed

194 frames with minimal latency. The breakdown is 35ms for pose detection, 9ms for feature

195 extraction, and just 3ms for inference. This enables 21 frames per second sustained processing. It

196 is suitable for live training applications with responsive feedback.

Random Forest's processing time totaled 89ms per frame. This was dominated by 45ms

198 inference time. This reflects the computational expense of evaluating 100 decision trees. This

199 yields 11 FPS sustained performance. This falls short of smooth real-time requirements but is

200 acceptable for offline video analysis.

Model sizes differed dramatically. Linear Regression was just 12 KB versus Random

202 Forest at 847 KB. However, both remain negligible in modern application contexts. Battery

203 consumption showed that Linear Regression consumed half the power of Random Forest during 204 continuous operation.

## 205 Comparison with the MediaPipe Approach

Previous research using MediaPipe achieved a limited test accuracy of 51.1%. It used 33

207 landmarks and statistical feature aggregation (Meng 2024). The current iOS implementation with

208 Random Forest achieved 92.9% accuracy. This is an 81% improvement. It used fewer landmarks,

209 17 versus 33, but with domain-informed biomechanical features.

This dramatic improvement demonstrates a fundamental principle in applied machine

211 learning. Thoughtful feature engineering based on domain knowledge yields far greater

212 performance gains than incremental advances in model architecture or raw data quantity. The shift

213 from generic statistical aggregates to biomechanical features capturing basketball shooting

214 mechanics proved transformative.

## 215 Practical Trade-offs and Use Case Recommendations

The results establish clear use case recommendations. Linear Regression excels for real-

217 time feedback applications. These require immediate shot detection to trigger coaching cues. It is

218 also good for battery-constrained scenarios during extended practice sessions, and for resource-

219 limited devices or embedded systems.

Random Forest is optimal for offline video analysis during post-practice review. It suits

221 high-accuracy requirements where minimizing false positives is critical. It is also good for

222 professional training contexts where accuracy justifies computational cost.

A hybrid approach combining both models shows promise. Linear Regression could

224 perform initial real-time detection with a low threshold. This would be followed by Random Forest

225 verification at a higher threshold for confirmed events. This architecture could achieve 226 approximately 15 to 18 FPS while maintaining Random Forest level accuracy for detected events.

## 227 Conclusion

## 228 Summary of Findings

This research successfully demonstrated the feasibility of real-time basketball jumpshot

230 detection on iOS devices using Apple's Vision framework. Two contrasting machine learning

231 approaches were developed, trained on over 8,000 annotated frames, and deployed on iOS

232 hardware for comprehensive evaluation.

Random Forest Classification achieved superior accuracy with high precision and good

234 recall. It substantially outperformed Linear Regression, which showed modest but interpretable

235 results. However, Linear Regression achieved true real-time performance. Meanwhile, Random

236 Forest's processing demands limited it to offline analysis applications.

Feature importance analysis revealed that elbow horizontal position dominates jumpshot

238 prediction across both models. This validates coaching principles emphasizing proper shooting

239 form alignment. Most significantly, domain-informed biomechanical feature engineering

240 produced an 81% improvement over generic statistical approaches from previous work.

## 241 Theoretical Contributions

This work advances sports analytics research through several avenues. It provides

243 platform-specific optimization, establishing iOS native performance benchmarks. It offers an

244 empirical model selection framework quantifying accuracy efficiency trade-offs. It demonstrates

245 that domain-informed feature engineering outperforms raw data quantity.

## 246 Practical Applications

The developed technology enables several immediate applications. These include real-time

248 shooting form feedback during individual training, automated shot counting and tracking, post-

249 practice video analysis with automatic shot detection, and remote coaching through analyzed video

250 submissions.

Extended applications include integration with smart basketball equipment, team-level

252 analytics aggregating multiple player data, injury prevention through biomechanical anomaly

253 detection, and gamification of training through automated statistics.

## 254 Future Directions

Future research should investigate several areas. These include sequential modeling

256 approaches like LSTMs (Long Short-term memory), Temporal Convolutional Networks, and

257 Transformers to capture temporal dependencies. It should integrate ball tracking for release point

258 and trajectory analysis. It should handle multi-person scenarios, dealing with occlusion and player

259 tracking. It should explore shot outcome prediction based on biomechanical features. Research

260 should work on generalization across diverse shooters and skill levels. Finally, it should pursue

261 edge computing optimization through model quantization and Neural Engine utilization.

## 262 Closing Perspective

This research establishes that sophisticated basketball shot analysis can operate entirely on

264 consumer smartphones without specialized equipment. The dramatic improvement over previous

265 cross-platform approaches demonstrates that platform-specific optimization and domain-informed

266 feature engineering substantially outweigh incremental model improvements.

The practical deployment of this technology on mobile devices represents a significant step

268 toward democratizing sports analytics in training. While traditional motion capture systems cost

269 tens of thousands of dollars and require dedicated facilities, smartphone-based analysis requires

270 only a device most athletes already own. This accessibility could transform skill development 271 processes and practice, particularly so in under-resourced communities where professional 272 coaching and advanced equipment remain inaccessible.

## References

274 Apple Developer. (2023). Detecting human body poses in images. Apple Developer

Documentation. https://developer.apple.com/documentation/vision/detecting-humanbody-poses-in-images

277 Cronin, N. J., Walker, J., Tucker, C. B., Nicholson, G., Cooke, M., Merlino, S., & Bissas, A.

(2024). Feasibility of OpenPose markerless motion analysis in a real athletics competition. Frontiers in Sports and Active Living, 5, Article 1298003. https://doi.org/10.3389/fspor.2023.1298003

281 Dedhia, U., Bhoir, P., Ranka, P., & Kanani, P. (2023). Pose estimation and virtual gym assistant using MediaPipe and machine learning. In 2023 International Conference on Network,

Multimedia and Information Technology (NMITCON) (pp. 1–7). IEEE. https://doi.org/10.1109/NMITCON58196.2023.10275938

285 Fukushima, T., Blauberger, P., Guedes Russomanno, T., & Lames, M. (2024). The potential of human pose estimation for motion capture in sports: A validation study. Sports

Engineering, 27, Article 19. https://doi.org/10.1007/s12283-024-00460-w

288 Ino, T., Samukawa, M., Ishida, T., Wada, N., Koshino, Y., Kasahara, S., & Tohyama, H. (2024).

Validity and reliability of OpenPose-based motion analysis in measuring knee valgus during drop vertical jump test. Journal of Sports Science and Medicine, 23(1), 515–525. https://doi.org/10.52082/jssm.2024.515

292 Meng, D. (2024). Predicting basketball shotmaking accuracy using single camera pose detection and random forest classification. Curieux Academic Journal. https://www.curieuxacademicjournal.com

295 Roggio, F., Trovato, B., Sortino, M., & Musumeci, G. (2024). A comprehensive analysis of the machine learning pose estimation models used in human movement and posture analyses:

A narrative review. Heliyon, 10(21), Article e39977. https://doi.org/10.1016/j.heliyon.2024.e39977

299 Tharatipyakul, A., Srikaewsiew, T., & Pongnumkul, S. (2024). Deep learning-based human body pose estimation in providing feedback for physical movement: A review. Heliyon,

10(17), Article e36589. https://doi.org/10.1016/j.heliyon.2024.e36589

302 Xi, X., Zhang, C., Jia, W., & Jiang, R. (2024). Enhancing human pose estimation in sports training: Integrating spatiotemporal transformer for improved accuracy and real-time performance. Alexandria Engineering Journal, 109, 144–156. https://doi.org/10.1016/j.aej.2024.08.072
