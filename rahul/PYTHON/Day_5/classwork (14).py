class Animal:
    def __init__(self):
        print("Animal Initialized")
    def __speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def __init__(self):
        super().__init__()  # Calls the parent class's __init__()
        print("Dog Initialized")
        # You can't call __speak() directly in the constructor of Dog.

    def bark(self):
        print("Dog barking")
        # Can call __speak() here using name mangling
        self._Animal__speak()

d = Dog()
d.bark()
