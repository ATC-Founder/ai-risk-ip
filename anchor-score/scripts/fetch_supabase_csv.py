import os
import csv
import subprocess
from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client
from supabase.lib.client_options import ClientOptions
import httpx

# Load environment variables
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
table = os.getenv("SUPABASE_TABLE", "scores")

# Set up Supabase client with extended timeout
options = ClientOptions(httpx_client=httpx.Client(timeout=httpx.Timeout(10.0)))
supabase = create_client(url, key, options=options)

# Pagination config
limit = 1000
offset = 0
all_rows = []

print("📡 Downloading data from Supabase...")

while True:
    response = supabase.table(table).select("*").range(offset, offset + limit - 1).execute()
    chunk = response.data
    if not chunk:
        break
    all_rows.extend(chunk)
    offset += limit
    print(f"📦 Fetched {len(chunk)} records... Total: {len(all_rows)}")

# Save to CSV and commit to Git
if all_rows:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = f"data/raw/scores_snapshot_{timestamp}.csv"

    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    fieldnames = all_rows[0].keys()
    with open(csv_path, "w", newline="") as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"✅ Saved {len(all_rows)} records to: {csv_path}")

    # Auto Git commit
    subprocess.run(["git", "add", csv_path])
    subprocess.run(["git", "commit", "-m", f"data: snapshot of {len(all_rows)} records from Supabase ({timestamp})"])
    print("📁 Committed snapshot to Git.")
else:
    print("⚠️ No data retrieved from Supabase.")
