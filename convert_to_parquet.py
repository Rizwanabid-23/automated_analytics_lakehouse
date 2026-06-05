import pandas as pd
import os

# Define local directories
csv_dir = "./data"
output_dir = "./data/parquet_landing"

# Create the output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# List of files we want to convert for our Lakehouse
files_to_convert = [
    "olist_orders_dataset.csv",
    "olist_customers_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv"
]

print("Starting CSV to Parquet conversion...")

for file_name in files_to_convert:
    csv_path = os.path.join(csv_dir, file_name)
    
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        
        # Define clean output name
        clean_name = file_name.replace("olist_", "").replace("_dataset.csv", "") + ".parquet"
        parquet_path = os.path.join(output_dir, clean_name)
        
        # Save as Parquet using pyarrow engine
        df.to_parquet(parquet_path, engine="pyarrow", index=False)
        print(f"Converted {file_name} -> {clean_name}")
    else:
        print(f"Warning: {file_name} not found in ./data folder.")

print("Conversion complete! Your Parquet files are in ./data/parquet_landing")