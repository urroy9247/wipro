import requests
response = requests.get("https://api.github.com")
response.content
print(type(response.content))
print(response.content)