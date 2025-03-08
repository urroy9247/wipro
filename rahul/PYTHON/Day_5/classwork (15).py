class Animal:           #animal is base class
    def __speak(self):   # _speak is private, can be accessed within the class in which it is defiend          
        print("Animal Speaking")
 
#child class Dog inherits the base class Animal 
class Dog(Animal):                           # dog is derived class 
    def bark(self):  
        print("dog barking")  
 
d = Dog()  
d.bark()  
d.__speak()