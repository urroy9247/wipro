import re
import os

folder = "C:/Users/Administrator/Desktop/rahul/PYTHON/Day_14/automation"
files = os.listdir(folder)
pattern = "classwork"
files_list = [ file for file in files if (re.findall(pattern,file))]

for i in files_list:
    print(i)