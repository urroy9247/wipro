import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.search("he.{2}o", txt)

if x:
    print("match")
else:
    print("no match")
