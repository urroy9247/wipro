import os

file_path = "C:/Users/Administrator/Desktop/new_file.txt"
file = open(file_path, 'w')
file.write("Hello, World!")

print(f"A new file has been created at {file_path}")