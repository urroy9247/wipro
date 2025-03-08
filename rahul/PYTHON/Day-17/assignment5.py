import pandas as pd
df = pd.read_csv("data_1.csv")

ranges = df[(df["Pulse"] == 120) & (df["Calories"] > 400)]

count = len(ranges)

print(ranges)
print(count)