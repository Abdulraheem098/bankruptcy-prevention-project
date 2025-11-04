# 🏦 Bankruptcy Prevention Project

## 📌 Project Overview
This project focuses on predicting the likelihood of company bankruptcy using **machine learning models**.  
It applies classification algorithms to analyze financial and operational indicators, helping stakeholders identify high-risk companies early.

---

## 🎯 Business Objective
To build a predictive system that:
- Accurately identifies companies at risk of bankruptcy  
- Helps investors, creditors, and management make data-driven financial decisions  
- Prevents economic losses through early intervention

---

## 📊 Dataset Information
- **Total Companies:** 250+
- **Features (Independent Variables):**
  - `industrial_risk`
  - `management_risk`
  - `financial_flexibility`
  - `credibility`
  - `competitiveness`
  - `operating_risk`
- **Target Variable:** `class` (bankruptcy / non-bankruptcy)

---

## ⚙️ Project Workflow
1. **Data Preprocessing**
   - Encoding categorical data  
   - Handling missing values & duplicates  
   - Standardization and feature selection

2. **Model Building**
   - Tried Logistic Regression, Decision Tree, and **KNN**
   - **KNN** achieved the best accuracy with 7-fold cross-validation

3. **Deployment**
   - Developed a **Streamlit web app** (`bankruptcy_app.py`)  
   - Takes user inputs (financial flexibility, competitiveness, credibility)  
   - Predicts whether the company is *Bankrupt* or *Non-Bankrupt*

---

## 🧠 Model Summary
- **Algorithm:** K-Nearest Neighbors (k=4)  
- **Cross-Validation:** 7 folds  
- **Reason for Selection:** Robust for categorical numerical values, less sensitive to outliers

---

## ▶️ How to Run the App
1. Clone this repository:
   ```bash
   git clone https://github.com/Abdulraheem098/bankruptcy-prevention-project.git
   cd bankruptcy-prevention-project
