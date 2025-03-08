#readline
f=open("names.txt" ) # r mode is the default 
print(f.readline())   # read() reads entire file

#readlines
f=open("names.txt" )   # r mode is the default 

print(f.readlines())   # readlines returns list of  data read from the file 
