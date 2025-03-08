import re
txt = "welcome helo planet"
#Search for a sequence that starts with "he", followed by two (any) characters,
#and an "o":
x = re.search("he..o", txt)
if x:
   print("Match")
else:
   print("No match")   