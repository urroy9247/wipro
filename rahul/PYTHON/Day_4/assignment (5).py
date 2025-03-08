'''An Adam number is a number for which the square of the number, when its digits are reversed and
 
is equal to the square of the number obtained by reversing the digits. For example the number 22 is an adam number because,
 
the square of 22 is 484 and the reverse of 484 is also 484, So the reversed square and the square of the reversed number
 
are equal thus making it an adam number.'''

def int_num(n):
    str_num=str(n)
    return int(str_num[::-1])
    


num1 = int(input("Enter number: "))
num2 = int_num(num1)

sq_num1 = num1*num1
sq_num2 = num2*num2

sq_real_num = int_num(sq_num2)

if sq_num1 == sq_real_num or num1 == num2:
    print(f"number {num1} is Adam")
    
else:
    print("number is not Adam")
