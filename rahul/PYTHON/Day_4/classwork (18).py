import re

aadhar="hello is or why"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) characters, and an "o":

x= re.findall("is|why|or",aadhar)
print(x)
if x:

   print("valid")

else:

   print("Invalid")