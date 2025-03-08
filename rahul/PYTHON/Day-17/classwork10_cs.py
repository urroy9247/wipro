import pandas as pd
 
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
 
df = pd.DataFrame(data)
 
df.to_csv("data1.csv", index=False)  # Save without index