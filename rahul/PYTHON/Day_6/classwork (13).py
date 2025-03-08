import os

new_dir = "C:/Users/Administrator/Desktop/new_folder"

if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory {new_dir} created successfully!")
else:
    print("Directory already exists.")