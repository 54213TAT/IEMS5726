### 1155250136 Cheng Haotian

### a. Four different input data
- **Vehicle identity data:** License plate number, ETC code
- **Vehicle classfication data:** Vehicle type, physical characteristics
- **Tunnel passage data:** Time of entry, time of exit, tunnel location
- **Account payment data:** Bound payment account, account balance

### b. Type of the data analytics and the machine learning problem
- **Data analytics:** Discriminant Data Analytics. The core logic of vehicle identity recognition is that the system collects the characteristics of the vehicle (license plate image, ETC code, vehicle parameters, etc.), matches these characteristics with the stored massive vehicle identity sample library, and finally identifies the unique identity corresponding to the current vehicle (such as "license plate Jing A12345 belongs to the owner Zhang San").
- **Machine learning problem:** Multi-class Classification. In vehicle identity recognition, each vehicle is an independent and mutually exclusive "category" (such as license plates A, B, and C corresponding to categories 1, 2, and 3, respectively), and the system needs to accurately classify the collected vehicle features into the corresponding vehicle identity category.

### c. Three recommended machine learning models
- **Convolutional Neural Networks, CNN:** This is the industry standard model for processing image and video data. The most crucial step in vehicle identity recognition is license plate image recognition. CNN can accurately capture the character features of license plates and the unique visual characteristics of vehicle appearance, perfectly adapting to image based features for vehicle identity recognition, and is the mainstream choice in the industry.
- **Support Vector Machine (SVM):** If vehicle identity recognition is based on structured features such as ETC encoding features, numerical features of license plate characters, and vehicle parameter features, SVM can efficiently process these high-dimensional features and accurately segment feature samples of different vehicles; Moreover, the SVM model is simple and has strong generalization ability, making it suitable for lightweight deployment of tunnel toll systems.
- **Random Forest:** In actual tunnel toll collection systems, vehicle identity recognition often adopts multi feature fusion (such as combining license plate image features, ETC encoding, and vehicle type). Random forests can efficiently process such multidimensional and multi type mixed features, and the features collected in tunnel scenes are prone to a small amount of noise (such as camera blur and weak ETC signals). The anti-interference performance of RF ensures recognition accuracy and high adaptability.

### d. Two evaluation metrics
- **Accuracy:** Accuracy is the most basic and intuitive evaluation metric, which measures the ratio of the number of correctly classified samples to the total number of samples. In vehicle identity recognition, high accuracy is required to ensure that the system can accurately identify the unique identity of each vehicle.
- **Precision:** In vehicle recognition, FP (misidentification) can directly lead to incorrect deduction of fees (transferring the toll fee of car A to car B's account), which is a serious business problem; Precision can specifically measure the probability of a model's "correct judgment", for example, a 100% Precision rate for a certain license plate represents that there are no misidentifications in the samples judged by the model as that license plate, perfectly meeting the core requirements of the toll collection system.

### e. Two types of charts
- **Confusion Matrix Heatmap:** A confusion matrix heatmap is a visual representation of the confusion matrix, where each cell of the matrix is colored to represent the number of samples in that cell. The color intensity can be used to represent the relative frequency of samples in each cell, making it easier to identify the types of errors made by the model.
    - X-axis: Predicted vehicle identity category
    - Y-axis: True vehicle identity category
- **Macro-average Precision-Recall Curve:** Belonging to a two-dimensional line chart, it calculates the macro average precision and macro average recall of all vehicle identity categories for multi classification tasks, and draws lines with the two as the horizontal and vertical axes to reflect the trade-off relationship between precision and recall of the model under different judgment thresholds. It is an important performance chart for evaluating multi classification/sample imbalance tasks.
    - X-axis: Recall
    - Y-axis: Precision

### f. Two ways in determining the types of vehicle
- **Image-based Visual Recognition:** Collect vehicle appearance images through high-definition cameras at tunnel entrances/exits, and use computer vision models such as CNN (Convolutional Neural Network) to automatically extract the core visual features of the vehicle.
- **Registered Data Matching:** Match the official information of the vehicle's contingency plan in the backend database of the traffic management/toll system through the vehicle's ETC electronic tag or license plate number.

### g. 10-fold cross validation
Not entirely correct. He has correct basic operations. But He ignored two critical prerequisites for the valid implementation of 10-fold cross validation, which are essential for the car identity recognition task: 
1. **Shuffling the dataset before splitting**: The car recognition data is usually collected in order by time/lane. Without shuffling, the samples in each fold will be homogeneous, leading to a biased validation result that cannot reflect the model's generalizability.
2. **Stratified sampling for splitting**: The dataset has class imbalance (e.g., more small car samples, fewer truck samples). Stratified sampling ensures the **class proportion of each fold is the same as the original dataset**. Without it, some folds may lack minority class samples, and the average accuracy will overestimate the model's actual performance.

Without these two steps, the final 10-fold cross validation accuracy cannot truly reflect the model's performance on unseen car identity data.
