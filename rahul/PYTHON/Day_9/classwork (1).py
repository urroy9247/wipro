import pandas as pd
 
# Read JSON file into a Pandas DataFrame
df = pd.read_json("data.json")
# Display DataFrame
print(df)
print("\n Columns are  \n" , df.columns)
print(df.info())