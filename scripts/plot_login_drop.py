import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/risk_logs.csv")
df['login_freq_drop'].hist(bins=10)
plt.title("Login Frequency Drop Distribution")
plt.xlabel("Drop %")
plt.ylabel("Number of Users")
plt.show()

