'''create class staf with name  role , salary as instance variables. [ Role can be programmer, Developer etc ]
 
def netSalry() based on salary and rules are given below
 
hra=50% of basic
 
cca = 25 % of basic
 
totsalary = basic+hra+cca and create displayInfo() .
 
The output is like this
 
Name          :  ***************8
Role          :  *********
Salary        :  **********
Hra           :  **********
Cca           :  *********
TotalSalary   :  ******* '''


class staff:
    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.salary = salary
        self.hra = 0
        self.cca = 0
        self.Total_sal = 0
        
    def netSalary(self):
        hra = self.salary *(50/100)
        self.hra = hra
        cca = self.salary *(25/100)
        self.cca = cca
        total_sal = self.salary + hra +cca
        self.Total_sal = total_sal
        
    def displayInfo(self):
        print("Name   : ",self.name)
        print("Role   : ",self.role)
        print("Salary : ",self.salary)
        print("hra    : ",self.hra)
        print("cca    :",self.cca)
        print("Total salary: ",self.Total_sal)
        

s1 = staff("rahul","developer",50000)
s1.netSalary()
s1.displayInfo()