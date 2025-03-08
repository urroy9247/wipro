import re

aadhar="helo"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x= re.search("he.+o",aadhar)
 
if x:

   print("valid")

else:

   print("Invalid")
 