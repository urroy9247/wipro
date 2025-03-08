string = "i am 24 years and 10 months old"
split_str = string.split(" ")
out_str = "".join([i for i in split_str if i.isdigit() ])
print(out_str)