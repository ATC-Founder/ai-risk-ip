# scripts/fetch_supabase_data.py
import os
from datetime import datetime
import json
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
table = os.getenv("SUPABASE_TABLE", "scores")

supabase = create_client(url, key)

response = supabase.table(table).select("*").limit(100000).execute()
records = response.data

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = f"data/raw/scores_snapshot_{timestamp}.json"

os.makedirs("data/raw", exist_ok=True)
with open(output_path, "w") as f:
    json.dump(records, f, indent=2)

print(f"✅ Saved {len(records)} records to {output_path}")
