import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import matplotlib.pyplot as plt
from models.scorer import score

df = pd.read_csv("data/risk_logs.csv")
df['risk_level'] = df.apply(score, axis=1)
df['risk_level'].value_counts().plot(kind='bar', title='Risk Distribution')
plt.tight_layout()
plt.savefig("reports/risk_distribution.png")
plt.show()

