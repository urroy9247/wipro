class Student:  
    count = 0          # count is a class variable 
    def __init__(self):    
        Student.count = Student.count + 1   
s1=Student()    
s2=Student()    
s3=Student()  
print("The number of students:",Student.count)