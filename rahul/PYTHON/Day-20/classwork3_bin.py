def bitlength(n):
    length = n.bit_length()
    print(length)

num = int(input("enter a number: "))
bitlength(num)