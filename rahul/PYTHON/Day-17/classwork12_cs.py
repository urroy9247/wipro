import pandas as pd
 
df = pd.read_csv("data1.csv")  # Reads CSV file into a DataFrame
print(df)
print("Columns " , df.columns)
print("Size    " , df.shape)