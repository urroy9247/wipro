def greet():
     
    # variable defined outside the inner function
 
    name = "John"
    # return a nested anonymous function
    return "Hi " + name
 
# call the outer function
 
message = greet
 
# call the inner function
 
print(message())