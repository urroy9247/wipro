import json

with open('details.json',mode='r',encoding='utf-8') as file:
    data = json.load(file)
    print(data['name'])