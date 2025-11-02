import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine
engine = create_engine(DATABASE_URL)

# Path to your extracted CSV folder
DATA_DIR = "D:/vighnesh-workspace/catalog-service/event-catalog-service/etsr_seed_dataset"

def load_csv_to_db(filename, table_name):
    csv_path = os.path.join(DATA_DIR, filename)
    df = pd.read_csv(csv_path)
    print(f"Loading {filename} → {table_name} ({len(df)} records)")
    df.to_sql(table_name, con=engine, if_exists="append", index=False)
    print(f"✅ Loaded {len(df)} rows into {table_name}")

def main():
    # Order is important due to foreign key dependencies
    load_csv_to_db("etsr_venues.csv", "venues")
    load_csv_to_db("etsr_events.csv", "events")
    # Optional: load_csv_to_db("etsr_seats.csv", "seat_templates")

if __name__ == "__main__":
    main()
