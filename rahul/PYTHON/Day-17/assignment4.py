import pandas as pd
df = pd.read_csv("data_1.csv")
ascen = df.sort_values(by = "Calories",ascending=False)
print(ascen)