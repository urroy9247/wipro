def netamt(amt, gst=18):  # default value , it is taken when we dont pass value

    return amt+amt*gst/100

print("Laptop price " , netamt(40000))  

print("Cake         " , netamt(300, 5))
 