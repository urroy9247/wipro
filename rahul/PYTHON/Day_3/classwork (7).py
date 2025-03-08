# r for reading modes, which is default
# w for writing modes
# a for appending 
# write names of five into names.txt 
f=open("names.txt", "w") #names.txt is physical file and f is the logical file
# pointing to physical file 
for i in range(5):
    name=input("Enter name   ")
    f.write(name+"\n")
 
f.close()  