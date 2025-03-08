class Student: 

    """ This class Student stores name, id and age  """

    def __init__(self,name,id,age):    

        self.name = name;    

        self.id = id;    

        self.age = age  

    def display_details(self):    

        print("Name:%s, ID:%d, age:%d"%(self.name,self.id,self.age))  

s = Student("John",101,22) 

print(s.__doc__)    

print(s.__dict__) 
s.display_details()

 