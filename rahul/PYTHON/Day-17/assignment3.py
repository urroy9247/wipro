import pandas as pd
df = pd.read_csv("data_1.csv")
columns = df[["Maxpulse","Calories"]]
print(columns)