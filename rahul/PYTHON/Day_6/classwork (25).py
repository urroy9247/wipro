text = "helloroy.py"
 
# Basic usage

print(text.endswith(".py"))  # Output: True

print(text.endswith(".txt"))  # Output: False
 
# Using start and end index

print(text.endswith("roy", 0, 8))  # Output: True
 
# Checking multiple suffixes

print(text.endswith((".py", ".txt", ".java")))  # Output: True
