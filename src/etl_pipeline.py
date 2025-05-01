
import pandas as pd

# Load raw data
sales = pd.read_csv('data/sales_inventory.csv')
products = pd.read_csv('data/products.csv')
stores = pd.read_csv('data/stores.csv')

# Join data
merged = sales.merge(products, on='product_id').merge(stores, on='store_id')
merged['date'] = pd.to_datetime(merged['date'])

# Aggregate daily sales and shortages
summary = merged.groupby(['store_id', 'product_id', 'date']).agg({
    'units_sold': 'sum',
    'units_short': 'sum',
    'units_restocked': 'sum',
    'ending_inventory': 'mean'
}).reset_index()

summary.to_csv('data/daily_inventory_summary.csv', index=False)
print("ETL complete. Output saved to data/daily_inventory_summary.csv")
