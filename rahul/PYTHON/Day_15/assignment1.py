import os
import re
 
folder = "C:/Users/Administrator/Desktop/rahul/PYTHON/Day_14/automation"
files = os.listdir(folder)
pattern = r"^test_.|._test$"
matching_files = [f for f in files if re.findall(pattern,f)]
 
for file in matching_files:
    print(file)