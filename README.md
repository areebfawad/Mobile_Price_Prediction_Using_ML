# 📱 Mobile Price Classification using Machine Learning

## 🧠 Overview
This project focuses on predicting the **price range of mobile phones** based on their hardware specifications.  
A complete **machine learning pipeline** is implemented, starting from data cleaning and visualization to feature scaling and model training.

The project is designed at a **beginner-friendly academic level** and is suitable for **university submission**.

---

## 🎯 Problem Statement
Given multiple features of a mobile phone such as RAM, battery power, screen resolution, and weight, the task is to classify the phone into one of the following **price categories**:

| Price Range | Description |
|------------|-------------|
| 0 | Low Cost |
| 1 | Medium Cost |
| 2 | High Cost |
| 3 | Very High Cost |

---

## 📂 Dataset Description
The dataset is taken from **Kaggle – Mobile Price Classification Dataset**.

### Files Used
- `train.csv` → Used for training and validation  
- `test.csv` → Used for testing the trained model  

### Dataset Statistics
- Total records: **2000**
- Total features: **20** (but **only 5 key features** are used for model training: `battery_power`, `ram`, `px_width`, `px_height`, `mobile_wt`)
- Target variable: **price_range**
- Missing values: **None**
- Data type: **Fully numeric**

---

## 🛠️ Technologies & Libraries
- **Python**
- **Pandas** – Data handling & cleaning  
- **NumPy** – Numerical computations  
- **Matplotlib** – Basic visualizations  
- **Seaborn** – Advanced data visualizations  
- **Scikit-learn** – Machine learning models & preprocessing  
- **Streamlit** – Web-based UI for model deployment  

---

## 🔄 Project Workflow
1. Load dataset using Pandas  
2. Understand dataset structure and data types  
3. Perform data cleaning and duplicate handling  
4. Exploratory Data Analysis (EDA)  
5. Data visualization using Matplotlib & Seaborn  
6. Feature and target separation (**5 features used: `battery_power`, `ram`, `px_width`, `px_height`, `mobile_wt`**)  
7. Train–Test split  
8. Feature scaling using `StandardScaler`  
9. Model training using **Logistic Regression**  
10. Model evaluation using accuracy score and confusion matrix  
11. Deployment using **Streamlit** for interactive UI

---

## 📊 Exploratory Data Analysis
The following visualizations were performed:
- Distribution of price ranges  
- Correlation heatmap between features  
- Confusion matrix for classification results  

These visualizations help in understanding feature relationships and model performance.

---

## 🤖 Machine Learning Model
**Algorithm Used:** Logistic Regression  

### Why Logistic Regression?
- Suitable for **multi-class classification**
- Easy to interpret
- Beginner-friendly and efficient
- Performs well after feature scaling
- Trained on **5 most important features** for price prediction

---

## 🖥️ Streamlit UI
- Interactive interface to input **battery power, RAM, screen resolution, and mobile weight**  
- Predicts the price range instantly on the web browser  
- Displays results in **Low, Medium, High, and Very High** cost categories with descriptive labels and icons  

---

## 📈 Model Evaluation
- Metric Used: **Accuracy Score**
- Evaluation performed on unseen test data

---

## 📁 Project Structure
Mobile-Price-Classification/
│
├── train.csv
├── test.csv
├── mobile_price_classification.ipynb
├── logistic_model_5f.pkl
├── scaler_5f.pkl
├── app.py  # Streamlit UI
├── README.md

---

## ✅ Results
The trained model successfully classifies mobile phones into their respective price ranges with good accuracy using **5 key features**, demonstrating the effectiveness of feature scaling, logistic regression, and a simple interactive UI.

---

## 🚀 Future Enhancements
- Apply advanced models like Random Forest or SVM  
- Perform hyperparameter tuning  
- Enhance the Streamlit app with probability/confidence display  
- Add cross-validation for better evaluation  

---

## 👨‍🎓 Author
**Areeb Fawad**  
Machine Learning Project  
University Assignment

---
