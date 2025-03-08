class Stack:
    def __init__(self):
        self.stack = []
 
    def push(self, data):
        self.stack.append(data)  # Add element to the top
 
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove the top element
        return "Stack is empty"
 
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Return top element without removing it
        return "Stack is empty"
 
    def is_empty(self):
        return len(self.stack) == 0
 
    def display(self):
        print(self.stack)
 
# Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()  # Output: [10, 20, 30]
print(s.pop())  # Output: 30
print(s.peek())  # Output: 20