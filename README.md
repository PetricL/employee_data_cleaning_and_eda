# Employee Data Cleaning and Exploratory Data Analysis (EDA)

## Project Overview

This project demonstrates a complete data cleaning and exploratory data analysis (EDA) workflow using Python and Pandas. The objective was to transform a messy employee dataset into a clean, analysis-ready dataset and uncover meaningful insights through statistical analysis and visualization.

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Project Structure

```text
employee_data_cleaning_and_eda/
│
├── data/
│   ├── messy_employee_dataset.csv
│   └── clean_employee_dataset.csv
│
├── notebooks/
│   └── employee_eda.ipynb
│
├── scripts/
│   └── cleaning_script.py
│
├── README.md
└── requirements.txt
```

---

## Data Cleaning Process

The raw dataset contained multiple data quality issues that required preprocessing.

### Cleaning Tasks Performed

* Loaded and inspected the raw dataset
* Split the combined `Department_Region` column into separate columns
* Filled missing values in `Age` using the median
* Filled missing values in `Salary` using the median
* Converted `Join_Date` to datetime format
* Corrected negative phone numbers using absolute values
* Removed duplicate employee records based on email addresses
* Reset the dataset index
* Removed unnecessary columns
* Exported the cleaned dataset

---

## Exploratory Data Analysis (EDA)

After cleaning, exploratory analysis was performed to better understand the dataset.

### Analysis Included

* Descriptive statistics
* Distribution analysis
* Missing values inspection
* Correlation analysis
* Outlier detection using the IQR method

### Visualizations

* Histograms
* Bar Charts
* Boxplots
* Correlation Heatmap

---

## Key Findings

* All missing values were successfully handled
* Duplicate employee records were removed
* No significant outliers were detected using the IQR method
* Feature correlations were generally weak, indicating low multicollinearity
* The dataset is clean and suitable for further analysis or predictive modeling

---

## Future Improvements

Potential extensions of this project include:

* Feature engineering
* Predictive modeling
* Employee performance prediction
* Employee churn analysis
* Interactive dashboards using Power BI or Tableau
* Advanced statistical analysis

---

## Author

**Lazar Petric**

Data Cleaning & Exploratory Data Analysis Project (2026)

