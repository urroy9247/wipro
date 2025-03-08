'''Assignment :
 
1. Read two complex numbers  a and b from the console
 
2. method 1 to add two complex nos
 
3. method 2 to subtract  b from a
 
4. displayComplex() to display complex no
 
 
a=  4+5i
b=  4+3i
 
sum=8+8i
 
use Operator overloading'''

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real  
        self.imag = imag 

    def __add__(self, other):
        real_sum = self.real + other.real  
        imag_sum = self.imag + other.imag  
        return ComplexNumber(real_sum, imag_sum)

  
    def __str__(self):
        return f"{self.real} + {self.imag}i"
# Create two complex numbers
num1 = ComplexNumber(5, 6) 
num2 = ComplexNumber(2, 3) 

add_result = num1 + num2  
print(f"Addition: {add_result}")  