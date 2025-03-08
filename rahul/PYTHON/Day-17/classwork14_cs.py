import pandas as pd
 
df = pd.read_csv("emp.csv")       # Reads CSV file into a DataFrame

print(df)

print("Columns " , df.columns)

print("Size    " , df.shape)  # how many rows and columns
 
print(df["Name"])  # Access single column
 
print(df[ ["Name", "Age"]  ])  # Access multiple columns
 
 
print(df.loc[0])        # Access first row using label-based indexing
 
print(df.iloc[1])     # Access second row using index-based position
 
print(df[df["Age"] > 25])     # Get rows where Age > 25
 
print(df[df["Salary"] >40000])
 
df["Age"] = df["Age"] + 1  # Increment all ages by 1
 
print(df)
 
df = df.drop(columns=["Salary"])  # Remove column
 
print(df)
print("\n\n")
print(df.describe())         # Summary statistics
print("\n")
print(df["Age"].mean())                # Column-wise mean
print(df["Age"].max())      # Max age
 
 
df_sorted = df.sort_values(by="Age", ascending=False)  # Sort by Age (Descending)

print(df_sorted)
 
df_grouped = df.groupby("City")["Age"].mean()

print(df_grouped)

