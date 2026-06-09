# Employee Dataset Cleaning and Exploratory Data Analysis (EDA)

This project focuses on cleaning a messy employee dataset and performing a structured exploratory data analysis (EDA). The goal is to transform raw, inconsistent data into a clean, analysis‑ready dataset and extract meaningful insights through statistical and visual exploration.

---

## Project Structure

Messy_Employee_dataset.csv – Original raw dataset  
Clean_Employee_Dataset.csv – Cleaned dataset after preprocessing  
cleaning_script.py – Python script used for data cleaning  
employee_eda.ipynb – Jupyter Notebook containing full EDA  

---

## 1. Data Cleaning Overview

The raw dataset contained several issues that required preprocessing before analysis. These included missing values, inconsistent formatting, combined columns, negative phone numbers, duplicate entries, and mixed data types. The cleaning process was performed using pandas and focused on creating a consistent and reliable dataset.

### Cleaning Steps Performed

- Loaded the raw dataset  
- Split the combined Department_Region column into two separate columns  
- Filled missing Age values using the median  
- Filled missing Salary values using the median  
- Converted Join_Date into a proper datetime format  
- Fixed negative phone numbers by converting them to absolute values  
- Removed duplicate employees based on Email  
- Reset the index after cleaning  
- Dropped the original combined column  
- Saved the cleaned dataset for further analysis  

---

## 2. Exploratory Data Analysis (EDA)

The EDA was performed on the cleaned dataset to understand its structure, distributions, relationships, and potential anomalies.

### Descriptive Statistics

- Summary statistics were generated for all numerical features  
- Distribution analysis was performed for Age, Salary, and other variables  

### Visualizations

- Histograms  
- Bar charts  
- Boxplots  
- Correlation heatmap  

### Outlier Detection (IQR Method)

- No outliers were detected in Age, Salary, Years_At_Company, or Performance_Score_Num  
- All values fell within acceptable statistical ranges  

### Missing Values Analysis

- After cleaning, the dataset contained zero missing values  
- No additional imputation was required  

---

## Final EDA Summary

The dataset is clean, consistent, and well‑structured after preprocessing. No missing values or outliers remain, and correlations between features are generally weak, indicating low multicollinearity. The dataset is fully prepared for further analysis, feature engineering, or predictive modeling. This project demonstrates a complete and professional workflow for data cleaning and exploratory data analysis.

---

## Possible Future Improvements

- Feature engineering (salary bands, tenure groups, performance categories)  
- Predictive modeling (performance prediction, churn analysis)  
- Dashboard creation using Power BI or Tableau  
- Advanced statistical testing and deeper business insights  

---

## Author

Lazar  
Data Cleaning and EDA Project  
2026
