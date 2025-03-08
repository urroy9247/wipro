import requests
 
response=requests.get("https://api.github.com", timeout=1)
 
print(response)
 
response= requests.get("https://api.github.com", timeout=3.05)
 
print(response)