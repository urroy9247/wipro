import json
with open("hello_frieda.json", mode="r", encoding="utf-8") as read_file:
       data = json.load(read_file)
print(type(data))
print("\n")
print(data["name"]+"\n")
print(data)