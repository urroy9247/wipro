#mathod 1
x=[2,3,4,5]
y=[]
for i in x:
    va=i+2
    y.append(va)
print(x)
print(y)

#method 2
x=[2,3,4,5]
y=map(lambda a:a+2, x)
print(list(y))

#method3
def add(val):
    return val + 2
x = [2,3,4,5]
y = list(map(add,x))
print(y)
