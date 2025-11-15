#  Customer Churn Prediction - Machine Learning Project

##  Table of Contents
- [Project Overview](#project-overview)
- [Business Context](#business-context)
- [Dataset Description](#dataset-description)
- [Technical Architecture](#technical-architecture)
- [Installation & Setup](#installation--setup)
- [Methodology](#methodology)
- [Results & Insights](#results--insights)
- [Future Improvements](#future-improvements)

##  Project Overview

This machine learning project focuses on predicting customer churn for a telecommunications company. The goal is to identify customers at high risk of leaving, enabling proactive retention strategies and reducing customer acquisition costs.

**Key Objectives:**
- Perform comprehensive exploratory data analysis (EDA)
- Build and compare multiple machine learning models
- Identify key factors influencing customer churn
- Provide actionable business insights

##  Business Context

Customer churn (customer attrition) is a critical metric in the telecom industry. This project addresses:
- **High churn rates** in competitive markets
- **Cost implications** of customer acquisition vs retention
- **Data-driven decision making** for customer success teams

##  Dataset Description

### Source & Characteristics
- **Source**: Telecom customer data
- **Records**: 7,043 customers
- **Features**: 21 independent variables
- **Target**: `Churn` (binary classification)

### Feature Categories
| Category | Features |
|----------|----------|
| **Demographic** | gender, SeniorCitizen, Partner, Dependents |
| **Account Info** | tenure, Contract, PaperlessBilling, PaymentMethod |
| **Services** | PhoneService, MultipleLines, InternetService |
| **Add-ons** | OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies |
| **Charges** | MonthlyCharges, TotalCharges |

##  Technical Architecture

### Tech Stack
```yaml
Programming Language: Python 3.8+
Libraries:
  - Data Manipulation: pandas, numpy
  - Visualization: matplotlib, seaborn
  - Machine Learning: scikit-learn, xgboost
  - Environment: Jupyter Notebook 
 ``` 
### Model Pipeline
```text
Data Collection → EDA → Preprocessing → Feature Engineering → 
Model Training → Evaluation → Deployment Ready
```
## Installation & Setup
### Prerequisites
```text
Python 3.8 or higher
pip (Python package manager)
```
### Step-by-Step Setup
#### 1-Clone the Repository
```bash
git clone https://github.com/jamila704/projet-churn-prediction.git
cd projet-churn-prediction
```
#### 2-Create Virtual Environment (Recommended)
```bash
python -m venv churn_env
source churn_env/bin/activate  # On Windows: churn_env\Scripts\activate
```

#### 3-Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost jupyter...
```

#### 4-Launch Jupyter Notebook
```bash
jupyter notebook mll.ipynb
```
### Requirements
```txt
pandas>=1.5.0
numpy>=1.21.0
matplotlib>=3.5.0
seaborn>=0.11.0
scikit-learn>=1.0.0
xgboost>=1.7.0
jupyter>=1.0.0
```
## Methodology
### 1. Data Exploration & Analysis
- Data Loading: Import and initial inspection of the dataset
- Missing Values: Identified and handled empty values in TotalCharges
- Data Types: Analysis of categorical and numerical features
- Statistical Summary: Descriptive statistics and distributions
### 2. Data Preprocessing
```python
# Key preprocessing steps implemented:
- Label Encoding for categorical variables using LabelEncoder
- StandardScaler for feature normalization
- Train-test split (80-20 ratio)
- Handling of 'TotalCharges' conversion from object to numeric
```
### 3. Model Development
**Algorithms Implemented:**

- Logistic Regression: Baseline model with good interpretability
- Random Forest Classifier: Ensemble method with bagging
- XGBoost Classifier: Advanced gradient boosting for superior performance

**Training Approach:**

- Standard train-test validation (80-20 split)
- Feature scaling for Logistic Regression
- Default parameters with optimization potential
### 4.  Model Evaluation
**Metrics Used:**

- Accuracy
- Precision, Recall, F1-Score
- ROC-AUC Score
- Confusion Matrix Analysis

## Results & Insights
**Key Findings from Analysis**

*Data Characteristics:*
- Dataset Size: 7,043 customers, 21 features
- Churn Rate: Approximately 26.5% of customers churned
- Data Types: Mixed numerical and categorical variables

*Data Quality Issues Handled:*
- TotalCharges column contained empty strings converted to numerical
- Categorical variables encoded for machine learning
- Feature scaling applied for model consistency

*Business Insights Discovered:*
- Contract Type Impact: Month-to-month customers show higher churn rates
- Tenure Effect: Newer customers are more likely to churn
- Service Patterns: Customers with tech support and online security churn less
- Payment Methods: Electronic check users have higher churn probability
- Internet Service: Fiber optic customers have different churn patterns

## Future Improvements
***Technical Enhancements***
- Hyperparameter tuning for XGBoost (GridSearchCV)
- Implement cross-validation for robust evaluation
- Handle class imbalance with SMOTE or class weights
- Add neural networks for comparison
- Create ensemble voting classifiers
***Feature Engineering***
- Create interaction features between services
- Develop tenure-based customer segments
- Engineer customer lifetime value metrics
- Add temporal features from tenure

***Deployment Ready***
- Create prediction pipeline with all three models
- Build simple web interface for churn prediction
- Export trained models for production use
- Create API endpoints for real-time predictions

## Author
***JAMILA IGGUI***
- Student in Data Science/Machine Learning
- Project developed for academic purposes
- Contact: [igguijamila67@gmail.com]
