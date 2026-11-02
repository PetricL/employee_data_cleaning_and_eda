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
│   ├── employee_data_cleaning_notebook.ipynb
│   └── employee_dataset_eda.ipynb
│
├── scripts/
│   └── employee_data_cleaning_script.py
│
├── README.md
└── requirements.txt
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/PetricL/employee_data_cleaning_and_eda.git
cd employee_data_cleaning_and_eda
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Data Cleaning Script

```bash
python scripts/employee_data_cleaning_script.py
```

The script reads `data/messy_employee_dataset.csv` and saves the result to `data/clean_employee_dataset.csv`.

### 4. Open the Jupyter Notebooks

Use the notebooks below to review the complete data cleaning process and exploratory data analysis:

```text
notebooks/employee_data_cleaning_notebook.ipynb
notebooks/employee_dataset_eda.ipynb
```

---

## Data Cleaning Process

The raw dataset contained multiple data quality issues that required preprocessing.

### Cleaning Tasks Performed

* Loaded and inspected the raw dataset
* Split the combined `Department_Region` column into separate columns
* Filled missing values in `Age` using the median (211 values, 21% of the data)
* Filled missing values in `Salary` using the median (24 values)
* Converted `Join_Date` to datetime format
* Corrected negative phone numbers using absolute values
* Checked for duplicate employees using `Employee_ID` (no duplicates found). `Email` was not used, because in this dataset it is built only from first and last name and is shared by many different employees
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

* The cleaned dataset contains all 1,020 employees, with no missing values and no duplicates
* Only about a third of employees (35%) are Active; the rest are Pending or Inactive
* Employees are spread fairly evenly across departments, regions and performance scores
* Remote work is almost evenly split (513 remote, 507 on-site)
* Salaries range from about 50,000 to 120,000, with mean and median both around 85,000
* No significant outliers were detected using the IQR method
* Correlations between numerical features are very weak, indicating low multicollinearity
* Age 30 is overrepresented because 211 missing ages were filled with the median (30)

### Lesson Learned

An earlier version removed duplicates based on `Email`. Because emails are built from first and last name, only 64 unique emails exist for 1,020 employees, and 956 real employees were removed by mistake. The rows sharing an email are clearly different people: they have different IDs, ages, departments, salaries and join dates. The cleaning now uses `Employee_ID`, the real unique identifier. In a real company, emails should be unique, so this would be reported as a data quality issue in the source system.

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




