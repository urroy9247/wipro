list1 = []
for i in range(10):
    num = float(input("enter number (int or float): "))
    list1.append(num)

x = float(input("Enter number to find in list: "))
flag = False
for i in list1:
    if i == x:
        flag = True
        break
if flag:
    print("Number is found at index:",list1.index(x))
    
else:
    print("Number not found")