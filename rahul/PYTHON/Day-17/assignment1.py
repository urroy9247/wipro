import pandas as pd

'''Assignment-1
 
1. List rows  whose calories above 400
 
2. List rows  whose calories between 400 and 450
 
3. list columns Maxpluse and calories
 
4. List rows in the ascending order of calories
 
5. List rows whose pulse are 120 and calories above 400.
 
6. count rows whose pulse are 120 and calories above 400.'''

df = pd.read_csv("data_1.csv")

print(df[df["Calories"] >= 400])