f=open("stud.txt", "w")

for i in range(3):

    name=input("Enter value for name  ")

    marks=input("Enter marks         ")

    f.write(name+" "+marks+"\n")
 
f.close()
 
f=open("stud.txt")

print("************************")

print("Name   Marks          ")

print("************************")

for i in f:

    str=i.split(" ")

    name=str[0]

    marks=str[1]

    print(name+"  "+marks)
 
print("************************")
 
f.close()

 