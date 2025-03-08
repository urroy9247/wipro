import pandas as pd
import numpy  as np
 

 
# read_csv() method to read csv and convert into data frame
# dataframe is a kind of data set like RDBMS table having rows and columns
 
 
df=pd.read_csv('sl.csv')
 
print(df.head())  # head() method returns the first 5 rows
print(df.columns) 
print(df.describe())
print(df.info())