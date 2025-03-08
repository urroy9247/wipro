def outer_function():
    x = 50  # Enclosing variable
    def inner_function():
        x=x+1
        print("Inside inner function:",x)
    inner_function()
    print("Inside outer function:", x)
outer_function()

# variable declared in the outerfunction can be accessed inside the inner function but can not be modified.
# if we need to  modify , use the word nonlocal