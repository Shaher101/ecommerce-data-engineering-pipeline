
import pandas as pd

# Extract
products = pd.read_csv("data/products.csv")

print("Original rows:", len(products))

# Transform
products = products.drop_duplicates(
    subset=["product_id"],
    keep="first"
).copy()

# Convert price to numeric
products["price"] = pd.to_numeric(
    products["price"],
    errors="coerce"
)

# Keep only products with valid, non-negative prices
products = products[
    products["price"].notna()
    & (products["price"] >= 0)
].copy()

# Load cleaned data into a new CSV file
products.to_csv("data/products_clean.csv", index=False)

print("Cleaned rows:", len(products))
print("\nCleaned products:")
print(products)

print("\nMissing values:")
print(products.isna().sum())

print("\nSaved to data/products_clean.csv")
