import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import matplotlib.pyplot as plt
from models.scorer import score

df = pd.read_csv("data/risk_logs.csv")
df['risk_level'] = df.apply(score, axis=1)
df['risk_level'].value_counts().plot(kind='bar', title='Risk Distribution')
# Export high-risk users
high_risk = df[df['risk_level'] == 'High']
high_risk.to_csv("data/high_risk_users.csv", index=False)
print(f"✅ Exported {len(high_risk)} high-risk users to data/high_risk_users.csv")


plt.tight_layout()
plt.savefig("reports/risk_distribution.png")
plt.show()

