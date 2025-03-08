from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()
 
    def push(self, data):
        self.stack.append(data)
 
    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"
 
    def peek(self):
        return self.stack[-1] if self.stack else "Stack is empty"
 
    def is_empty(self):
        return len(self.stack) == 0
 
    def display(self):
        print(list(self.stack))
 
# Usage
s = Stack()
s.push(5)
s.push(15)
s.push(20)
s.display()     # Output: [5, 15]
print(s.pop())  # Output: 15