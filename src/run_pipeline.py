
import subprocess
import sys

scripts = [
    "src/read_customers.py",
    "src/clean_products.py",
    "src/clean_orders.py",
    "src/clean_order_items.py",
]

for script in scripts:
    print(f"\n{'=' * 50}")
    print(f"Running: {script}")
    print("=" * 50)

    subprocess.run(
        [sys.executable, script],
        check=True
    )

print("\nPipeline completed successfully!")
