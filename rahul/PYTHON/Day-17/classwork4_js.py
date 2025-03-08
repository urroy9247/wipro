# Appending data 
import json
 
with open("data.json", "r") as file:
    existing_data = json.load(file)
 
existing_data["email"] = "alice@example.com"  # Modify or add data
 
with open("data.json", "w") as file:
    json.dump(existing_data, file, indent=4)