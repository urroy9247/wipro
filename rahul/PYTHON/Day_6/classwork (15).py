import os

new_working_dir = "C:/Users/Administrator/Desktop/rahul/Feb_3"

os.chdir(new_working_dir)
print(f"Current working directory changed to: {os.getcwd()}")