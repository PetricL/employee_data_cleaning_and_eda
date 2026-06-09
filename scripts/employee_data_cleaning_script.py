import pandas as pd

# Load dataset
df = pd.read_csv("Messy_Employee_dataset.csv")

# Split Department_Region into two columns
df[["Department", "Region"]] = df["Department_Region"].str.split("-", expand=True)

# Clean Age column (fill missing with median)
df["Age"] = df["Age"].fillna(df["Age"].median())

# Clean Salary column (fill missing with median)
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Convert Join_Date to datetime
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

# Fix negative phone numbers
df["Phone"] = df["Phone"].abs()

# Remove duplicate employees based on Email
df = df.drop_duplicates(subset="Email", keep="first")

# Reset index after cleaning
df = df.reset_index(drop=True)

# Drop old combined column
df = df.drop(columns=["Department_Region"])

# Save cleaned dataset
df.to_csv("Clean_Employee_Dataset.csv", index=False)

print("Cleaning complete. File saved as Clean_Employee_Dataset.csv")





