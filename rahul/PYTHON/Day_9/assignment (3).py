from collections import deque

# Initializing the deque
stack = deque()

# stack operations
stack.append(1)  # appending
stack.append(2)
stack.append(3)

stack.appendleft(0)  # appending left
stack.appendleft(-1)
stack.appendleft(-2)
print(stack)

stack.pop()  # pop
print(stack)

stack.popleft()  # popleft
print(stack)

stack.append(4)
stack.appendleft(5)
print(stack)

stack.rotate(1)  # rotate right by 1
print(stack)

stack.rotate(-1)  # rotate left by 1
print(stack)

# Print the stack 
print(list(stack))  # Converting deque to list to print it cleanly
