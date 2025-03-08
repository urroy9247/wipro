f=open("marks.txt","w")
f.write("name"+"\t"+"m1"+"\t"+"m2"+"\t"+"total_marks\n")
for i in range(3):
    name = input("enter name: ")
    mark_1 = int(input("enter marks1: "))
    mark_2 = int(input("enter marks2: "))
    total_marks = mark_1 + mark_2
    f.write(name+"\t"+str(mark_1)+"\t"+str(mark_2)+"\t"+str(total_marks)+"\n")
f.close()
print("\n")
f=open("marks.txt")
print(f.read())
f.close()