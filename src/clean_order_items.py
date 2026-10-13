
import pandas as pd

# Extract
items = pd.read_csv("data/order_items.csv")

# Read valid order and product IDs
orders = pd.read_csv("data/orders_clean.csv")
products = pd.read_csv("data/products_clean.csv")

valid_order_ids = set(orders["order_id"])
valid_product_ids = set(products["product_id"])

print("Original rows:", len(items))

# Transform
items = items.drop_duplicates(
    subset=["order_item_id"],
    keep="first"
).copy()

# Convert numeric fields
items["quantity"] = pd.to_numeric(
    items["quantity"], errors="coerce"
)
items["unit_price"] = pd.to_numeric(
    items["unit_price"], errors="coerce"
)

# Remove missing or invalid quantities and prices
items = items[
    items["quantity"].notna()
    & (items["quantity"] > 0)
    & items["unit_price"].notna()
    & (items["unit_price"] >= 0)
].copy()

# Keep only rows linked to valid orders and products
items = items[
    items["order_id"].isin(valid_order_ids)
    & items["product_id"].isin(valid_product_ids)
].copy()

# Calculate line total
items["line_total"] = items["quantity"] * items["unit_price"]

# Load
items.to_csv("data/order_items_clean.csv", index=False)

print("Cleaned rows:", len(items))
print("\nCleaned order items:")
print(items)

print("\nMissing values:")
print(items.isna().sum())

print("\nSaved to data/order_items_clean.csv")
