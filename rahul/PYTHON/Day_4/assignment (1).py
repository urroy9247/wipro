import re

aadhar=input("Enter your pandcard no without spaces ") 

'''

It should have 12 digits.
It should not start with 0 and 1.
It should not contain any alphabet and special characters.
It should have white space after every 4 digits.

'''

x= re.search("[2-9]{4}\\s[0-9]{4}\\s[0-9]{4}",aadhar)
 
if x:

   print("valid aadhar")

else:

   print("Invalid aadhar")
 