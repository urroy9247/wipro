import os

dir_path = "C:/Users/Administrator/Desktop/rahul"

contents = os.listdir(dir_path)
print("Directory contents:")
for item in contents:
    print(item)