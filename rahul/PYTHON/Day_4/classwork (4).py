import re

txt = "Muruga doss"

#Check if the string if ends with doss :

# $ symbol is used to match at the end

x = re.findall("i", txt)   

# search method returns true if match , otherwise false

if x:

  print("Yes, the string ends  doss")

else:

  print("No  ")
 