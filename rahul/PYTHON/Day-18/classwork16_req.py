import requests
 
url = 'https://www.skillsugar.com/contact'
 
params = {'name': 'john', 'subject' : 'Programming', 'message': 'Hello', 'email': 'murugadoss@yahoo.com'}
 
result = requests.post(url, params=params)
 
print(result.headers)
 
 
data=requests.get(url)
 
 
# List content under  url = 'https://www.skillsugar.com/contact'