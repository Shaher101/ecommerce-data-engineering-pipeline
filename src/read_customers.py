
import pandas as pd

# Extract
customers = pd.read_csv("data/customers.csv")

original_count = len(customers)

# Transform: standardize empty values
customers = customers.replace(r"^\s*$", pd.NA, regex=True)

# Remove duplicate customer IDs
customers = customers.drop_duplicates(
    subset=["customer_id"],
    keep="first"
)

# Reject rows missing essential information
customers = customers.dropna(
    subset=["customer_id", "full_name", "email"]
).copy()

# Handle missing city values
customers["city"] = customers["city"].fillna("Unknown")

# Data quality summary
print("Original rows:", original_count)
print("Cleaned rows:", len(customers))
print("Rejected rows:", original_count - len(customers))
print("\nMissing values after cleaning:")
print(customers.isna().sum())

# Load: save cleaned data
customers.to_csv("data/customers_clean.csv", index=False)

print("\nCleaned data saved to data/customers_clean.csv")
print(customers)
