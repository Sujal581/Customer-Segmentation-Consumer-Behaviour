# 👥 Customer Segmentation & Consumer Behaviour Analysis

An interactive **Machine Learning and Data Analytics Dashboard** built with **Python, Streamlit, Plotly, and Scikit-Learn** to analyze customer behavior, identify customer segments, predict customer categories, and generate actionable business recommendations.

---

## 📌 Project Overview

Understanding customer behavior is crucial for businesses to improve customer retention, optimize marketing campaigns, and increase revenue.

This project applies **K-Means Clustering** to segment customers based on their:

* Age
* Annual Income
* Spending Score

The dashboard provides comprehensive customer insights through interactive visualizations, machine learning models, and business-focused recommendations.

---

## 🚀 Live Demo

🌐 **Application:** [Add Streamlit Link]

📂 **GitHub Repository:** [Add GitHub Link]

---

## 🎯 Project Objectives

* Analyze customer demographics and purchasing behavior
* Identify meaningful customer segments
* Predict customer segments using Machine Learning
* Generate business recommendations based on customer groups
* Create an interactive dashboard for stakeholders

---

# 🛠️ Tech Stack

| Category             | Technology               |
| -------------------- | ------------------------ |
| Programming Language | Python                   |
| Dashboard Framework  | Streamlit                |
| Data Manipulation    | Pandas, NumPy            |
| Data Visualization   | Plotly                   |
| Machine Learning     | Scikit-Learn             |
| Clustering Algorithm | K-Means                  |
| Prediction Model     | Random Forest Classifier |

---

# 📊 Dashboard Modules

## 🏠 Executive Overview

Provides a high-level summary of the customer dataset.

### KPIs

* Total Customers
* Average Age
* Average Income
* Average Spending Score
* Total Customer Segments

### Visualizations

* Gender Distribution
* Age Distribution
* Income Distribution
* Spending Score Distribution

---

## 👥 Customer Segmentation

Uses **K-Means Clustering** to group customers based on behavioral patterns.

### Features

* Elbow Method Analysis
* Cluster Visualization
* Segment Distribution
* Segment Summary

### Customer Segments

| Segment               | Description                        |
| --------------------- | ---------------------------------- |
| 💎 Premium Customers  | High Income, High Spending         |
| 🎯 Careful Customers  | High Income, Low Spending          |
| 🛍️ Impulse Customers | Moderate Income, High Spending     |
| 💰 Budget Customers   | Low Income, Low Spending           |
| 👥 Average Customers  | Moderate Income, Moderate Spending |

---

## 🎂 Age Analysis

Analyzes customer behavior across age groups.

### KPIs

* Young Customers
* Average Age
* Most Common Age
* Oldest Customer

### Insights

* Spending Behavior by Age
* Income by Age
* Age Group Distribution

---

## 💰 Income Analysis

Evaluates customer income patterns.

### KPIs

* Highest Income
* Average Income
* High Income Customers

### Visualizations

* Income Distribution
* Income vs Spending Score
* Income by Segment
* Income Categories

---

## 🚻 Gender Analysis

Compares customer behavior across genders.

### KPIs

* Male Customers
* Female Customers
* Average Spending by Gender

### Insights

* Gender Distribution
* Income by Gender
* Spending Score by Gender
* Segment Breakdown by Gender

---

## 🤖 Customer Segment Predictor

A Machine Learning model built using **Random Forest Classifier**.

### User Inputs

* Gender
* Age
* Annual Income
* Spending Score

### Output

Predicts customer segment:

* Premium Customer
* Careful Customer
* Budget Customer
* Impulse Customer
* Average Customer

### Additional Features

* Customer Profile Summary
* Marketing Recommendation Engine
* Personalized Business Insights

---

## 📊 Cluster Insights

Detailed analysis of customer clusters.

### Features

* Segment Distribution
* Cluster Performance
* Income vs Spending Analysis
* Customer Personas

### Business Insights

* Highest Value Segments
* Revenue Opportunities
* Segment Characteristics

---

## 💡 Customer Insights

Answers important business questions.

### Key Questions

* Which age group spends the most?
* Which segment generates the highest value?
* Which customers should marketing prioritize?
* Do higher-income customers always spend more?

---

## 🎯 Business Recommendations

Provides actionable strategies for each customer segment.

### Recommendations

#### 💎 Premium Customers

* Loyalty Programs
* VIP Memberships
* Exclusive Offers

#### 🎯 Careful Customers

* Upselling Campaigns
* Personalized Recommendations

#### 🛍️ Impulse Customers

* Flash Sales
* Limited-Time Offers

#### 💰 Budget Customers

* Discounts
* Value Bundles

#### 👥 Average Customers

* Engagement Campaigns
* Loyalty Programs

---

## 📂 Dataset Explorer

Explore dataset structure and quality.

### Features

* Dataset Preview
* Statistical Summary
* Missing Value Analysis
* Correlation Matrix
* Data Quality Checks
* Download Dataset

---

# 🤖 Machine Learning Workflow

### 1. Data Preprocessing

* Remove Duplicates
* Handle Missing Values
* Feature Scaling

### 2. Customer Segmentation

Algorithm:

```text
K-Means Clustering
```

Features Used:

```text
Age
Annual Income (k$)
Spending Score (1-100)
```

### 3. Customer Segment Prediction

Algorithm:

```text
Random Forest Classifier
```

Input Features:

```text
Gender
Age
Annual Income
Spending Score
```

Output:

```text
Predicted Customer Segment
```

---

# 📂 Project Structure

```text
Customer Segmentation & Consumer Behaviour
│
├── Overview.py
├── utils.py
├── styles.py
├── requirements.txt
├── Mall_Customers.csv
│
└── pages
    ├── 1_Customer Segmentation.py
    ├── 2_Age Analysis.py
    ├── 3_Income Analysis.py
    ├── 4_Gender Analysis.py
    ├── 5_Customer Segment Predictor.py
    ├── 6_Cluster Insights.py
    ├── 7_Customer Insights.py
    ├── 8_Business Recommendations.py
    └── 9_Dataset Explorer.py
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/customer-segmentation-dashboard.git
```

### Navigate to Project Folder

```bash
cd customer-segmentation-dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run Overview.py
```

---

# 📦 Requirements

```txt
streamlit
pandas
numpy
plotly
scikit-learn
openpyxl
```

---

# 📈 Future Enhancements

* Customer Lifetime Value (CLV) Analysis
* RFM Segmentation
* Advanced Recommendation System
* Model Performance Dashboard
* Real-Time Data Integration
* Customer Churn Prediction

---

# 👨‍💻 Author

**Sujal**

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
