cel = [10,28,35,45,60,78]
fah_list = [ (1.8* i)+32 for i in cel ]
print(fah_list)

fah = [10,28,35,45,60,78]
cel_list = [ (i - 32)/1.8 for i in fah ]
print(cel_list)