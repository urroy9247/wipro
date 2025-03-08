import sys

list1 = []

for i in range(1,len(sys.argv)):
    list1.append(sys.argv[i])

print(f"maximum value from {sys.argv[1:]} is: ",max(list1))

'''import sys
 
# total arguments
 
n = len(sys.argv)
 
 
bigger=int(sys.argv[1])
 
for i in range(2, n):
    if bigger < int(sys.argv[i]):
       bigger=int(sys.argv[i])
print("\n\nBiggest :", bigger)'''