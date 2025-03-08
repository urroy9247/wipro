#write python script to validate indian mobile phone nos

import re 

phn_num = input("Enter the phone number (avoid spaces): +91")

x = re.search("^[7-9][0-9]{9}",phn_num)

if x:
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")