
import pandas as pd

# Extract: read cleaned datasets
customers = pd.read_csv("data/customers_clean.csv")
products = pd.read_csv("data/products_clean.csv")
orders = pd.read_csv("data/orders_clean.csv")
items = pd.read_csv("data/order_items_clean.csv")

# Transform: join order items with orders
sales = items.merge(
    orders,
    on="order_id",
    how="inner"
)

# Join product details
sales = sales.merge(
    products[["product_id", "product_name", "category"]],
    on="product_id",
    how="inner"
)

# Join customer details
sales = sales.merge(
    customers[["customer_id", "full_name", "city"]],
    on="customer_id",
    how="inner"
)

# Exclude cancelled orders from sales revenue
sales = sales[sales["status"] != "Cancelled"].copy()

# Create a report by product category
category_report = (
    sales.groupby("category", as_index=False)
    .agg(
        total_quantity=("quantity", "sum"),
        total_revenue=("line_total", "sum")
    )
)

# Load: save reports
sales.to_csv("data/sales_report.csv", index=False)
category_report.to_csv("data/category_report.csv", index=False)

print("Sales details:")
print(sales[[
    "order_id",
    "full_name",
    "product_name",
    "quantity",
    "line_total",
    "status"
]])

print("\nRevenue by category:")
print(category_report)

print("\nTotal revenue:", sales["line_total"].sum())
print("\nReports saved successfully!")
