 
list1 = ["Hello ", "take "]
 
list2 = ["Dear", "Sir"]
 
new_list = [ i + j for i in list1 for j in list2]
print(new_list)