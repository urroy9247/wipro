list1 = [10, 20, 30, 40]
 
list2 = [100, 200, 300, 400]

res = list(zip(list1,list2[::-1]))
print(res)