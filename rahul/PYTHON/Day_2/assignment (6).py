str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_string = [ i for i in str_list if type(i)==str and len(i)>=1]
print(new_string)