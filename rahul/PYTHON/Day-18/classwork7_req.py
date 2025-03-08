import requests
response = requests.get("https://api.github.com")
dict=response.json()
print(dict)