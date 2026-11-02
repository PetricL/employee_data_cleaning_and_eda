from pathlib import Path

import pandas as pd

# Paths (works no matter which folder the script is run from)
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Load dataset
df = pd.read_csv(DATA_DIR / "messy_employee_dataset.csv")

# Split Department_Region into two columns
df[["Department", "Region"]] = df["Department_Region"].str.split("-", expand=True)

# Clean Age column (fill missing with median)
df["Age"] = df["Age"].fillna(df["Age"].median()).astype(int)

# Clean Salary column (fill missing with median)
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Convert Join_Date to datetime
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

# Fix negative phone numbers
df["Phone"] = df["Phone"].abs()

# Remove duplicate employees based on Employee_ID
# (Email is not unique: it is built from first and last name, so different employees share it)
before = len(df)
df = df.drop_duplicates(subset="Employee_ID", keep="first")
print(f"Duplicates removed: {before - len(df)}")

# Reset index after cleaning
df = df.reset_index(drop=True)

# Drop old combined column
df = df.drop(columns=["Department_Region"])

# Save cleaned dataset
df.to_csv(DATA_DIR / "clean_employee_dataset.csv", index=False)

print(f"Cleaning complete. {len(df)} employees saved to data/clean_employee_dataset.csv")
