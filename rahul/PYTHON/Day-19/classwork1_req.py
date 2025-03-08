import requests

req = requests.get("http://google.com")

for c in req.cookies:
    print(c.name,"==>",c.value)