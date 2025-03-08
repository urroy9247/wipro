def counttotalbits(n):
    num = bin(n)[2:]
    return [len(num),num]

number = 10
print(counttotalbits(number))