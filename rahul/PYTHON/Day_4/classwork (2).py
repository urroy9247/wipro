import re
txt = "hello planet"
#Check if the string starts with 'hello':
x = re.search("^hello", txt)   # search method returns true if match , otherwise false
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")