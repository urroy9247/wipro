import requests
 
response = requests.get("https://api.github.com")
 
print(response.headers["content-type"])