import os

file_path =  "C:/Users/Administrator/Desktop/rahul/PYTHON/Day_6"
if os.path.exists(file_path):
    print(os.path.dirname(file_path))
