import json
 
data = {  "name": "Alice", "age": 25, "city": "New York" }
 
# Writing JSON to a file
 
with open("data.json", "w") as file:
 
    json.dump(data, file, indent=4)   # 'indent=4'   makes it readable
 
 
# json.dump(obj, file) → Write JSON to a file.