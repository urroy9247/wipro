class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real  
        self.imag = imag 

    def __sub__(self, other):
        real_sum = self.real - other.real  
        imag_sum = self.imag - other.imag  
        return ComplexNumber(real_sum, imag_sum)

  
    def __str__(self):
        return f"{self.real} - {self.imag}i"
# Create two complex numbers
num1 = ComplexNumber(5, 6) 
num2 = ComplexNumber(2, 3) 

sub_result = num1 - num2  
print(f"Subraction: {sub_result}")  
