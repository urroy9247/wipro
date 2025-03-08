import pandas as pd
 
df= pd.read_csv("data_1.csv")
 
print(type(df))
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print("\n")
print(df.isnull().sum())
print(df.columns)
print(df.shape)