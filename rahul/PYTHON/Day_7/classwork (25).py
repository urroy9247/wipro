def outer_function():
    x = 50  # Enclosing variable
    def inner_function():
        nonlocal x
        x=x+1
        print("Inside inner function:",x)
    inner_function()
    print("Inside outer function:", x)
outer_function()