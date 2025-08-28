### Bank Term Deposit Subscription Predictor
This project uses machine learning to predict whether a bank customer will subscribe to a term deposit based on previous marketing campaign data. The app is deployed using Streamlit for interactive use and supports business decision-making in targeted marketing.

#### Project Features
* Binary classification using multiple models (Logistic Regression, Random Forest, SVM, Decision Tree)

* Feature engineering and preprocessing (SMOTE, scaling, one-hot encoding)

* Model evaluation using Accuracy, Precision, Recall, F1 Score, Confusion Matrix, and ROC-AUC

* User-friendly interface built with Streamlit

* Final model saved using joblib and loaded for real-time predictions

#### Problem Statement
Banks want to increase the number of term deposit subscriptions. By analyzing past marketing campaign data, this project aims to predict whether a client will subscribe, enabling better targeting and reducing marketing waste.

#### Dataset Overview
The dataset used includes the following types of features:

* Client Data: Age, Job, Marital status, Education

* Loan History: Housing loan, Personal loan, Credit default

* Campaign Data: Contact type, Last contact date & duration, Previous outcome

* Target: Whether the client subscribed (yes/no)

