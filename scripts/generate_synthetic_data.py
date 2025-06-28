import pandas as pd
from faker import Faker
import random
from datetime import datetime

fake = Faker()
rows = []

for _ in range(100000):
    login_freq = random.randint(1, 20)
    login_drop = random.choice([0, 10, 30, 50, 70])
    event_count = random.randint(0, 200)
    timestamp = fake.date_time_between(start_date='-30d', end_date='now')
    rows.append({
        "user_id": fake.uuid4(),
        "department": random.choice(["HR", "IT", "Finance", "Legal"]),
        "event_count": event_count,
        "login_freq_drop": login_drop,
        "last_login": timestamp,
    })

df = pd.DataFrame(rows)
df.to_csv("data/risk_logs.csv", index=False)
print("✅ Data generated: data/risk_logs.csv")

