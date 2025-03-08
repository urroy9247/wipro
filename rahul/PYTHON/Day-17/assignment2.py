import pandas as pd

df = pd.read_csv("data_1.csv")
calories_400 = df[(df["Calories"] >= 400) & (df["Calories"]<=450)]
print(calories_400)