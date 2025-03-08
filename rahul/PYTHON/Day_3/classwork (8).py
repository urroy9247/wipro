#read whole data
f=open("names.txt" ) # r mode is the default 
print(f.read())   # read() reads entire file

#read given bytes
f=open("names.txt" )   # r mode is the default 

print(f.read(3))   # read 3 bytes

 