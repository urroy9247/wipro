class Animal:           #animal is base class
    def _speak(self):   # _speak is protected method, can be accessed in the immediately derived class         
        print("Animal Speaking")
#child class Dog inherits the base class Animal 
class Dog(Animal):                           # dog is derived class 
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d._speak()  