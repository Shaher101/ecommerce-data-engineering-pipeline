
import pandas as pd

# Extract
orders = pd.read_csv("data/orders.csv")

# Load cleaned customer IDs
customers = pd.read_csv("data/customers_clean.csv")
valid_customer_ids = set(customers["customer_id"])

print("Original rows:", len(orders))

# Transform: remove duplicate orders
orders = orders.drop_duplicates(
    subset=["order_id"],
    keep="first"
).copy()

# Validate dates
orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)

# Keep only orders with valid dates
orders = orders.dropna(subset=["order_date"]).copy()

# Keep only orders linked to known customers
orders = orders[
    orders["customer_id"].isin(valid_customer_ids)
].copy()

# Save cleaned orders
orders.to_csv("data/orders_clean.csv", index=False)

print("Cleaned rows:", len(orders))
print("\nCleaned orders:")
print(orders)

print("\nMissing values:")
print(orders.isna().sum())

print("\nSaved to data/orders_clean.csv")
