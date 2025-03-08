import os

dir_to_remove =  "C:/Users/Administrator/Desktop/new_folder"
if os.path.exists(dir_to_remove):
    os.rmdir(dir_to_remove)
    print(f"Directory {dir_to_remove} has been removed.")
else:
    print("The directory does not exist.")