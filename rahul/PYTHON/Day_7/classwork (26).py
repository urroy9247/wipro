name = "alice"
age = 23
animal = "cat"
print("my name is %s and i am %d years old"%(name,age))
print("\n")
print("my name is {} and i am {} years old".format(name,age))
print("\n")
print("my name is {0} and i am {2} years old and i love {1}".format(name,age,animal))
print("\n")
print(f"my name is {name} and i am {age} years old and i love {animal}")

pi = 3.14159
print(f"Pi to two decimal places: {pi:.2f}")