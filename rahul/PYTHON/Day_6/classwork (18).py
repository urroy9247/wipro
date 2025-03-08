import os

file_path =  "C:/Users/Administrator/Desktop/rahul/PYTHON/Day_3/classwork (1).py"
if os.path.exists(file_path):
    print(os.path.isfile(file_path))