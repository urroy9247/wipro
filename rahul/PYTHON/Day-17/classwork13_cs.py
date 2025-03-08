import pandas as pd
 
data = [
    ["Alice", 25, "New York" , 50000],
    ["Bob", 30, "Los Angeles",45000],
    ["Charlie", 35, "Chicago" , 10000]
]
 
df = pd.DataFrame(data, columns=["Name", "Age", "City","Salary"])
 
df.to_csv("emp.csv", index=False)  # Save without index