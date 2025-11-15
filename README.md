# 🔍 Customer Churn Prediction - Machine Learning Project

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Business Context](#business-context)
- [Dataset Description](#dataset-description)
- [Technical Architecture](#technical-architecture)
- [Installation & Setup](#installation--setup)
- [Project Structure](#project-structure)
- [Methodology](#methodology)
- [Results & Insights](#results--insights)
- [Usage](#usage)
- [Future Improvements](#future-improvements)

## 🎯 Project Overview

This machine learning project focuses on predicting customer churn for a telecommunications company. The goal is to identify customers at high risk of leaving, enabling proactive retention strategies and reducing customer acquisition costs.

**Key Objectives:**
- Perform comprehensive exploratory data analysis (EDA)
- Build and compare multiple machine learning models
- Identify key factors influencing customer churn
- Provide actionable business insights

## 💼 Business Context

Customer churn (customer attrition) is a critical metric in the telecom industry. This project addresses:
- **High churn rates** in competitive markets
- **Cost implications** of customer acquisition vs retention
- **Data-driven decision making** for customer success teams

## 📊 Dataset Description

### Source & Characteristics
- **Source**: Telecom customer data
- **Records**: 7,043 customers
- **Features**: 20 independent variables
- **Target**: `Churn` (binary classification)

### Feature Categories
| Category | Features |
|----------|----------|
| **Demographic** | gender, SeniorCitizen, Partner, Dependents |
| **Account Info** | tenure, Contract, PaperlessBilling, PaymentMethod |
| **Services** | PhoneService, MultipleLines, InternetService |
| **Add-ons** | OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies |
| **Charges** | MonthlyCharges, TotalCharges |

## 🏗️ Technical Architecture

### Tech Stack
```yaml
Programming Language: Python 3.8+
Libraries:
  - Data Manipulation: pandas, numpy
  - Visualization: matplotlib, seaborn
  - Machine Learning: scikit-learn, xgboost
  - Environment: Jupyter Notebook

### Model Pipeline
Data Collection → EDA → Preprocessing → Feature Engineering → 
Model Training → Evaluation → Deployment Ready
⚙️ Installation & Setup
.Prerequisites
.Python 3.8 or higher

pip (Python package manager)

Step-by-Step Setup
1-Clone the Repository
git clone https://github.com/[votre-username]/projet-churn-prediction.git
cd projet-churn-prediction
