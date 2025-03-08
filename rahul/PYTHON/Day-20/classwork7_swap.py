num = 73
bd = list(bin(num)[2:])
print(bd)
i = -int(input("enter a lsb bit: "))
j = -int(input("enter a msb bit: "))
bd[j],bd[i] = bd[i],bd[j]
print(("".join(bd)))