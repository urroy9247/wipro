import re

aadhar="hello"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) characters, and an "o":

x= re.search("he.?o",aadhar)
 
if x:

   print("valid")

else:

   print("Invalid")