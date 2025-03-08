class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return ("stack is empty")
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        if not self.is_empty():
            return len(self.stack)
        return ("stack is empty")
        
    def display(self):
        if not self.is_empty():
            return self.stack
        return ("stack is empty")
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
print(s1.display())
s1.pop()
print(s1.display())
s1.pop()
print(s1.display())
print(s1.peek())
print(s1.display())