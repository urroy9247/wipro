import os

file_path = "C:/Users/Administrator/Desktop/rahul/jan_26"
if os.path.exists(file_path):
    print("file exists")
else:
    print("file not exists")