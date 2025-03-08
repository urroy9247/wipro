'''What Happens When say_hello() is Called:
Before calling the original function, the wrapper prints:
"Before calling the function."

The original say_hello() function is executed, printing:
"Hello!"

After calling the original function, the wrapper prints:
"After calling the function."'''

# Step 1: Define the decorator
def simple_decorator(func):
    # This is the wrapper function
    def wrapper():
        print("Before calling the function.")
        func()  # Call the original function
        print("After calling the function.")
    return wrapper()

# Step 2: Apply the decorator to a function
@simple_decorator  # This is how we "decorate" a function
def say_hello():
    print("Hello!")

# Step 3: Call the decorated function
say_hello