import requests

# URL of the post you want to delete
url = "https://jsonplaceholder.typicode.com/posts/2"

# Sending the DELETE request
response = requests.delete(url)

# Checking if the delete operation was successful
if response.status_code == 200:
    # You can also perform a GET request to ensure it's deleted
    verify_response = requests.get(url)
    if verify_response.status_code == 404:  # 404 Not Found means it's deleted
        print("Post successfully deleted!")
    else:
        print("Post not deleted successfully.")
else:
    print("Failed to delete the post.")