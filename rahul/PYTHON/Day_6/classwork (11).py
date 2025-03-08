import os

old_name = "C:/Users/Administrator/Desktop/new_file.txt"
new_name = "C:/Users/Administrator/Desktop/renamed.txt"

os.rename(old_name, new_name)
print(f"File renamed from {old_name} to {new_name}")