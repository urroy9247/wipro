text = "Hello, world!"
 
# Basic usage

print(text.startswith("Hello"))  # Output: True

print(text.startswith("world"))  # Output: False
 
# Using start index

print(text.startswith("world", 7))  # Output: True
 
# Using start and end index

print(text.startswith("Hello", 0, 5))  # Output: True
 
# Checking multiple prefixes

print(text.startswith(("Hi", "Hello")))  # Output: True
