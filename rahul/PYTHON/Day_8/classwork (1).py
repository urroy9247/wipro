''' Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables methods to have the same name but behave differently based on the object that is calling them. '''

class Animal:
    def speak(self):
        pass
 
class Dog(Animal):
    def speak(self):
        return "Woof!"
 
class Cat(Animal):
    def speak(self):
        return "Meow!"
 
def animal_sound(animal):
    print(animal.speak())
 
# Creating objects
dog = Dog()
cat = Cat()
 
# Using polymorphism
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!