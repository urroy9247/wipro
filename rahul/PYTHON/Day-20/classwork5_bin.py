def sumofbits(n):
    sums = 0
    for i in range(1,n+1):
        binary_val = bin(i)[2:]
        sums += binary_val.count('1')
    print(sums)

n = int(input('enter a number: '))
sumofbits(n)
