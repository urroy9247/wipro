import requests
url = "https://api.github.com/users/octocat/repos"
params = {"per_page": 5, "page": 1} # 5 results per page
response = requests.get(url, params=params)
print(response.json())

