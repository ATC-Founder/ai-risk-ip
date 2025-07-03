import os
import json
from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client
from supabase.lib.client_options import ClientOptions
import httpx

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
table = os.getenv("SUPABASE_TABLE", "scores")

# Extended timeout
options = ClientOptions(httpx_client=httpx.Client(timeout=httpx.Timeout(10.0)))
supabase = create_client(url, key, options=options)

# Supabase max = 1000 per request
limit = 1000
offset = 0
all_rows = []

print("⏳ Downloading data from Supabase...")

while True:
    response = supabase.table(table).select("*").range(offset, offset + limit - 1).execute()
    chunk = response.data
    if not chunk:
        break
    all_rows.extend(chunk)
    offset += limit
    print(f"📦 Fetched {len(chunk)} records... Total: {len(all_rows)}")

# Save to file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"data/raw/scores_snapshot_{timestamp}.json"
with open(filename, "w") as f:
    json.dump(all_rows, f, indent=2)

print(f"✅ Saved {len(all_rows)} records to {filename}")