my_list = [1, 2, 3]
 
# Getting an iterator from the list
 
my_iterator = iter(my_list)
 
# Using next() to get items one by one
 
try:
    while True:
        item = next(my_iterator)
        print(item)
except StopIteration:
    print("Iteration has reached")
        