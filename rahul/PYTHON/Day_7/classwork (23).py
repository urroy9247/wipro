def outer_function():
    x = 50  # Enclosing variable
    def inner_function(): #we can access local variable,but we cant modify it
        print("Inside inner function:",x)
    inner_function()
    print("Inside outer function:", x)
outer_function()

'''
def outer_function():
    x = 50  # Enclosing variable
    def inner_function():
        a=x+1
        print("Inside inner function:",a)
    inner_function()
    print("Inside outer function:", x)
outer_function()
'''