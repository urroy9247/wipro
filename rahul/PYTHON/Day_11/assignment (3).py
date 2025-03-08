class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]
    
    def display(self):
        return self.queue
    
q1 = Queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)

print(q1.display())

q1.dequeue()
q1.dequeue()

print(q1.display())
print(q1.peek())