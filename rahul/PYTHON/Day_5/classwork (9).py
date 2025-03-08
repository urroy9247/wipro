class Animal:                                 #animal is base class
    def speak(self):  
        print("Animal Speaking")
 
#child class Dog inherits the base class Animal 
class Dog(Animal):                           # dog is derived class 
    def bark(self):  
        print("dog barking")  
 
d = Dog()  
d.bark()  
d.speak()  
 
 
# by default it is public access modifier . Meaning all base class resources can be accessed in the derived class