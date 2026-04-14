# 一、初级面试题（必考简答 / 填空）
### 1. 什么是数据科学流程（Pipeline）？
问题定义 → 数据收集 → 预处理 → 建模 → 结果解释 → 进一步分析
Problem Definition → Data Collection → Preprocessing → Modeling → Result Interpretation → Further Analysis

### 2. 四种数据分析类型是什么？
- 描述性（发生了什么）
- 诊断性（为什么发生）
- 预测性（未来会怎样）
- 规范性（应该做什么）
- Descriptive (what happened)
- Diagnostic (why it happened)
- Predictive (what will happen in the future)
- Prescriptive (what should be done)

### 3. 监督学习 vs 无监督学习 的区别？
- 监督：有标签 → 分类、回归
- 无监督：无标签 → 聚类、降维
- Supervised: with labels → classification, regression
- Unsupervised: without labels → clustering, dimensionality reduction

### 4. 分类 vs 回归 的区别？
- 分类：预测离散标签（是/否、类别）
- 回归：预测连续数值（价格、温度、指数）
- Classification: Predicting discrete labels (yes/no, categories)
- Regression: Predicting continuous numerical values (prices, temperatures, indices)

### 5. 训练集 / 验证集 / 测试集 的作用？
- 训练集：训练模型
- 验证集：调参、选模型
- 测试集：最终评估，**不能用来调参**
- Training set: for model training
- Validation set: for parameter tuning and model selection
- Test set: for final evaluation and **must not be used for parameter tuning**

### 6. 过拟合是什么？怎么解决？
- 过拟合：模型在训练集表现极好，测试集很差
- 解决：正则化、早停、增加数据、降维、dropout
- Overfitting: The model performs extremely well on the training set but poorly on the test set
- Solutions: Regularization, early stopping, data augmentation, dimensionality reduction, dropout

### 7. 什么是正则化？L1 和 L2 的区别？（What is regularization）
- L2（Ridge）：缩小权重，防过拟合
- L1（Lasso）：可做**特征选择**，让部分权重变 0
- L2 (Ridge): Shrinks weights to prevent overfitting
- L1 (Lasso): Enables **feature selection** by driving some weights to 0

### 8. 什么是标准化（Standardization）？
将数据变成均值 0，方差 1，适合距离类模型（KNN、SVM、神经网络）
Normalize the data to a mean of 0 and a variance of 1, which is suitable for distance-based models (KNN, SVM, neural networks)

### 9. 什么是独热编码（One-hot）？
把分类变量变成 0/1 向量，避免顺序假设。
Convert categorical variables into 0/1 vectors to avoid sequential assumptions.

### 10. 缺失值处理方法有哪些？
- 删除
- 均值/中位数/众数填充
- 回归填充
- 多重填充
- Deletion
- Mean/Median/Mode Imputation
- Regression Imputation
- Multiple Imputation

---

# 二、中级面试题（期末场景题必考）
### 11. 准确率（Accuracy）为什么在不平衡数据中没用？
因为样本比例不均，模型全猜多数类也能准确率很高，但完全没预测能力。
应该用：精确率、召回率、F1、AUC、MCC。
Due to an imbalanced sample ratio, the model can achieve high accuracy simply by guessing the majority class all the time, yet it has no predictive capability at all.
The following metrics should be used: precision, recall, F1 score, AUC, and MCC.

### 12. 精确率、召回率、F1 的含义？
- 精确率：预测为正里，真正正的比例
- 召回率：真实为正里，被预测出来的比例
- F1：两者的调和平均
- Precision: The proportion of true positives among all predicted positive cases
- Recall: The proportion of true positives that are correctly predicted among all actual positive cases
- F1: The harmonic mean of precision and recall

### 13. 什么是 AUC-ROC？
衡量模型区分正负样本的能力，越接近 1 越好，0.5=瞎猜。
It measures the model's ability to distinguish between positive and negative samples. The closer the value is to 1, the better; 0.5 means random guessing.

### 14. 什么是混淆矩阵？
TP、TN、FP、FN 组成的矩阵，用于分类评估。
A matrix composed of TP, TN, FP, and FN, used for classification evaluation.

### 15. K-Means 步骤是什么？
1. 选 K 个质心
2. 把点分给最近质心
3. 更新质心
4. 重复直到收敛
1. Select K centroids
2. Assign points to the nearest centroid
3. Update the centroids
4. Repeat until convergence

### 16. 如何选择 K-Means 的 K 值？
肘部法则、轮廓系数（Silhouette Score）
Elbow Method, Silhouette Score

### 17. PCA 的作用？
无监督降维，最大化数据方差，保留主要信息。
Unsupervised dimensionality reduction maximizes data variance and preserves main information.

### 18. PCA vs LDA 区别？
- PCA：无监督，只看数据方差
- LDA：有监督，最大化类别区分度
- PCA: Unsupervised, focusing only on data variance
- LDA: Supervised, maximizing inter-class discrimination

### 19. 什么是词嵌入（Word Embedding）？
把词语转为低维稠密向量，捕捉语义关系。
Convert words into low-dimensional dense vectors to capture semantic relationships.

### 20. BERT vs GPT 的区别？
- BERT：编码器，**理解类任务**（分类、问答）
- GPT：解码器，**生成类任务**（写作、对话）
- BERT: Encoder, **understanding-oriented tasks** (classification, question answering)
- GPT: Decoder, **generation-oriented tasks** (writing, dialogue)

### 21. 推荐系统有哪些类型？
- 协同过滤
- 基于内容
- 混合推荐
- 矩阵分解
- 深度学习（DeepCoNN、Wide&Deep、GCN）
- Collaborative Filtering
- Content-Based
- Hybrid Recommendation
- Matrix Factorization
- Deep Learning (DeepCoNN, Wide&Deep, GCN)

### 22. 什么是冷启动问题？ What is the cold start problem?
新用户/新物品没有交互记录，推荐系统无法推荐。
New users or new items have no interaction records, making it impossible for the recommendation system to provide recommendations.

### 23. 强化学习的 5 要素？
Agent、Environment、State、Action、Reward

### 24. Q-Learning 是什么？
用 Q 表学习状态-动作价值，最大化长期奖励。
Learn state-action values using the Q-table and maximize long-term rewards.

### 25. 时间序列数据为什么不能随机划分？Why can't time series data be randomly split?
会引入未来信息，导致模型效果虚高，必须按时间切分或滚动窗口。
Random splitting introduces future information, leading to artificially inflated model performance. Time-based splitting or rolling windows must be used instead.

---

# 三、Python 编程高频面试题（考试 30%）
### 26. Pandas 如何查看缺失值？
`df.isnull().sum()`

### 27. 如何填充缺失值？
`df.fillna(df.median())`

### 28. 如何做 train-test split？
`train_test_split(X, y, test_size=0.2)`

### 29. 如何画热力图？
`sb.heatmap(df.corr(), annot=True)`

### 30. 如何做标准化？
`StandardScaler().fit_transform(X)`

---


# 45道机器学习算法面试题（带标准答案｜IEMS5726 期末专用）

---

# 一、基础必考题（初级）
1. **什么是监督学习？举3个算法。supervised learning**
有标签数据训练，预测输出。
算法：逻辑回归、SVM、决策树、随机森林。
Training with labeled data and predictive output.
Algorithms: Logistic Regression, SVM, Decision Tree, Random Forest.

2. **什么是无监督学习？举3个算法。Unsupervised Learning**
无标签，找数据结构。
算法：K-Means、PCA、层次聚类、异常检测。
No tags, find data structures.
Algorithms: K-Means, PCA, hierarchical clustering, anomaly detection.

3. **分类 vs 回归的区别？**
分类：预测**离散类别**（是/否、猫狗）。
回归：预测**连续数值**（价格、温度、指数）。
Classification: Predicting **discrete categories** (yes/no, cats and dogs).
Regression: Predicting **continuous numerical values** (prices, temperatures, indices).

4. **什么是过拟合？怎么解决？overfitting**
模型在训练集太好，测试集差。
解决：正则化、早停、增加数据、dropout、简化模型。
The model performs extremely well on the training set but poorly on the test set.
Solutions: regularization, early stopping, data augmentation, dropout, and simplifying the model.

5. **什么是欠拟合？怎么解决？underfitting**
模型太简单，训练测试都差。
解决：加特征、加模型复杂度、减少正则。
The model is too simple, performing poorly on both training and test data.
Solutions: add features, increase model complexity, reduce regularization.

6. **训练集/验证集/测试集作用？**
训练集：学参数。
验证集：调参、选模型。
测试集：最终无偏评估。
Training set: Learn parameters.
Validation set: Tune parameters and select models.
Test set: Conduct final unbiased evaluation.

7. **什么是交叉验证？cross-validation**
把数据分成多份，轮流训练验证，结果更稳定。
Divide the data into multiple parts, take turns for training and validation, resulting in more stable outcomes.

8. **为什么要特征缩放？feature scaling**
让数值特征同尺度，避免距离/梯度受大数值影响。
（KNN、SVM、神经网络必须做）
To bring numerical features to the same scale and prevent distances or gradients from being affected by large values.
(Mandatory for KNN, SVM, and neural networks)

9. **什么是独热编码？**
分类变量转0/1向量，不引入顺序关系。
Convert categorical variables into 0/1 vectors without introducing ordinal relationships.

10. **什么是特征选择？feature selection**
选出有用特征，减少维度、防过拟合、提速。
Select useful features, reduce dimensionality, prevent overfitting, and speed up the process.

---

# 二、经典算法题（中级必考）
11. **决策树原理？分裂指标？Principle of Decision Tree? Splitting Metrics?**
按特征递归分裂数据。
指标：信息熵、基尼系数、信息增益。
Recursively split data according to features.
Metrics: information entropy, Gini coefficient, information gain.

12. **随机森林为什么更好？Random Forest better?**
多棵树集成，降低方差，更稳，防过拟合。
It integrates multiple trees, reduces variance, is more stable, and prevents overfitting.

13. **Bagging vs Boosting？**
Bagging：并行训练，投票（随机森林）。
Boosting：串行训练，修正前序错误（XGBoost）。

14. **SVM是什么？核函数作用？**
找最大间隔超平面分隔数据。
核函数：把低维数据映射高维，处理非线性。
Find the maximum margin hyperplane to separate the data.
Kernel function: Map low-dimensional data to high dimensions to handle nonlinearity.

15. **KNN原理与缺点？**
看最近K个邻居投票。
缺点：大数据慢、高维效果差、对尺度敏感。
Vote by looking at the nearest K neighbors.
Disadvantages: slow performance with big data, poor effectiveness in high dimensions, and sensitivity to scale.

16. **线性回归假设？**
线性关系、误差独立同分布、无多重共线性。
Linear relationship, independently and identically distributed errors, and no multicollinearity.

17. **逻辑回归是回归还是分类？Is logistic regression regression or classification?**
分类！用sigmoid输出概率，做二分类。
Classification! Use sigmoid to output probabilities for binary classification.

18. **L1 vs L2 正则？**
L1：可**特征选择**，权重变0。
L2：缩小权重，防过拟合，计算稳定。
L1: Capable of **feature selection**, with weights becoming zero.
L2: Shrinks weights, prevents overfitting, and ensures stable computation.

19. **K-Means步骤？**
1) 选K个质心
2) 样本分到最近质心
3) 更新质心
4) 重复到收敛
1) Select K centroids
2) Assign samples to the nearest centroid
3) Update the centroids
4) Repeat until convergence

20. **怎么选K值？**
肘部法则（看SSE下降）、轮廓系数。
The elbow method (by observing the decline in SSE) and the silhouette coefficient.

21. **PCA作用？**
无监督降维，最大化方差，保留主要信息。
Unsupervised dimensionality reduction, maximizing variance and preserving key information.

22. **PCA vs LDA？**
PCA：无监督，只看数据方差。
LDA：有监督，最大化类别区分度。
PCA: unsupervised, focusing only on data variance.
LDA: supervised, maximizing class discrimination.

23. **协同过滤：用户-based vs 物品-based？**
用户-based：找相似用户推荐。
物品-based：找相似物品推荐。
User-based: Recommend by finding similar users.
Item-based: Recommend by finding similar items.

24. **矩阵分解用于什么？What is matrix factorization used for**
推荐系统，补全用户-物品评分矩阵。
Recommendation system, complement the user-item rating matrix.

25. **冷启动问题？怎么解决？cold start problem**
新用户/新物品无行为，无法推荐。
解决：基于内容、人口信息、热门推荐。
New users or new items have no behavior data, making recommendations impossible.
Solution: Content-based, demographic information-based, and popular item recommendations.

---

# 三、深度学习题（期末必考）
26. **什么是MLP？**
多层感知机，全连接神经网络，拟合非线性。
Multilayer perceptron, fully connected neural network, fitting nonlinearity.

27. **激活函数？ReLU为什么常用？activation function**
解决梯度消失，计算快，收敛快。
Solves the vanishing gradient problem, with fast computation and rapid convergence.

28. **前向传播 vs 反向传播？**
前向：算预测值。
反向：算梯度，更新权重。
Forward: Calculate predicted values.
Backward: Calculate gradients and update weights.

29. **自编码器用途？autoencoders**
无监督降维、去噪、特征学习、异常检测。
Unsupervised dimensionality reduction, denoising, feature learning, and anomaly detection.

30. **LSTM解决什么？**
解决RNN梯度消失，捕捉长时序依赖。
Solve the vanishing gradient problem of RNN and capture long-term temporal dependencies.

31. **Transformer核心？**
自注意力机制，并行处理，捕捉全局依赖。
Self-attention mechanism, parallel processing, and capturing global dependencies.

32. **自注意力机制？**
每个词关注句子所有词，理解上下文。
Each word focuses on all words in the sentence and understands the context.

33. **BERT vs GPT？**
BERT：编码器，**理解类任务**（分类、问答）。
GPT：解码器，**生成类任务**（写作、对话）。

34. **CNN用于什么？**
图像任务：特征提取、分类、检测。
Image tasks: feature extraction, classification, and detection.

35. **扩散模型原理？**
正向逐步加噪，逆向学习去噪，生成图像/音频。
Forward step-by-step noise addition, reverse learning denoising, and generation of images/audio.
---

# 四、模型评估题（必考！）
36. **准确率为何不适合不平衡数据？**
样本不均时，全猜多数类也能准确率高，但无效。
When the samples are imbalanced, guessing the majority class can also yield high accuracy, but it is ineffective.

37. **精确率/召回率/F1？**
精确率：预测为正中，真正正的比例。
召回率：真实为正中，被找出的比例。
F1：两者调和平均。
Precision: The proportion of true positives among all predicted positive cases.
Recall: The proportion of actual positive cases that are correctly identified.
F1: The harmonic mean of the two.

38. **AUC-ROC是什么？**
衡量模型区分正负样本能力，越接近1越好。
Measures the model's ability to distinguish between positive and negative samples; the closer to 1, the better.

39. **混淆矩阵？Confusion matrix?**
TP/TN/FP/FN表格，看分类错误类型。
TP/TN/FP/FN table for viewing classification error types.

40. **回归评估指标？**
MAE、MSE、RMSE、R²（越接近1越好）。
MAE, MSE, RMSE, R² (the closer to 1, the better).
---

# 五、强化学习题（期末必考）
41. **RL五要素？**
Agent、环境、状态、动作、奖励。

42. **Q-Learning？**
用Q表学习状态-动作价值，最大化长期奖励。
Learn state-action values using the Q-table and maximize long-term rewards.

43. **DQN？**
神经网络版Q-Learning，解决高维状态问题。
Neural network-based Q-Learning for solving high-dimensional state problems.

44. **Actor-Critic？**
Actor选动作，Critic评价值，训练更稳。
The Actor selects actions, and the Critic evaluates values, leading to more stable training.

45. **探索 vs 利用？**
探索：试新动作。
利用：选已知最好动作。
用ε-greedy平衡。
Exploration: trying new actions.
Exploitation: selecting the best known action.
Balanced using ε-greedy.

---

