class Stack:
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop(-1)
        return "stack is empty"

    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "stack is empty"
        
    def size(self):
        if not self.is_empty():
            return "size of stack:",len(self.stack)
        
s1 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)
s1.push(50)
print(s1.size())

print(s1.peek())
print(s1.pop())
print(s1.size())