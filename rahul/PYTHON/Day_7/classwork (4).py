def fibonacci(n):

    if n <= 1:

        return n

    else:

        return fibonacci(n-1) + fibonacci(n-2)
 
for i in range(10):

    print(fibonacci(i), end=" ")
 
# Output: 0 1 1 2 3 5 8 13 21 34

'''
def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Example: Generate the first 10 Fibonacci numbers
n = 10
print(fibonacci(n))
'''