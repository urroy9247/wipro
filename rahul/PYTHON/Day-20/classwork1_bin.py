def countsetbits(n):
    bin_val = bin(n)
    return bin_val.count("1")
n=int(input(" Enter value for  n "))
# Function calling 
print( countsetbits(n))
