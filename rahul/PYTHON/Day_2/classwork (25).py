staff={"name" : "doss",

        "age" :  45 ,

        "loc" : "Bangalore"}

print("To print key value pairs \n")
 
for i in staff.items():  # items() method to print key value pairs 

    print(i)
 
print("To print key value pairs \n")

for i,j in  staff.items():

    print(i,"--->", j)

# dictionary values  are mutable - can be changed
 
staff["loc"]="Chennai"

print(staff)

 