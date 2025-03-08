import os

file_path = "C:/Users/Administrator/Desktop/renamed.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file {file_path} has been deleted.")
else:
    print("file not exists")