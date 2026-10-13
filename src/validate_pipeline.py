
import subprocess
import sys

scripts = [
    "src/read_customers.py",
    "src/clean_products.py",
    "src/clean_orders.py",
    "src/clean_order_items.py",
    "src/sales_report.py",
    "src/validate_pipeline.py",
]

for script in scripts:
    print(f"\n{'=' * 50}", flush=True)
    print(f"Running: {script}", flush=True)
    print("=" * 50, flush=True)

    subprocess.run(
        [sys.executable, script],
        check=True
    )

print("\nPipeline completed successfully!", flush=True)
print("All data quality checks passed!", flush=True)
