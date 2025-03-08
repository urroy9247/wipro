import requests
 
url = "https://jsonplaceholder.typicode.com/posts/1"
 
response = requests.get(url)
 
if response.status_code == 200:
 
    print("Response:", response.json())  # JSON response

else:

    print("Failed to fetch data")

 