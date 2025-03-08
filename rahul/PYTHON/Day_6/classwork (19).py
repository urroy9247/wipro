import os

file_path =  "C:/Users/Administrator/Desktop/rahul/PYTHON/Day_3"
if os.path.exists(file_path):
    print(os.path.isdir(file_path))