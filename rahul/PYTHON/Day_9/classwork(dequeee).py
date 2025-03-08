#Importing and Creating a Deque
 
from collections import deque
 
# Creating an empty deque
dq = deque()
 
# Creating a deque with initial elements
dq = deque([1, 2, 3, 4])
print(dq)  # Output: deque([1, 2, 3, 4])
 
#Operations on Deque:
 
#1. Appending Elements
 
#append(x): Adds x to the right end.
 
#appendleft(x): Adds x to the left end.
 
dq.append(5)      # deque([1, 2, 3, 4, 5])
 
dq.appendleft(0)  # deque([0, 1, 2, 3, 4, 5])
 
 

#2. Removing Elements:
 
#pop(): Removes and returns the rightmost element.
 
#popleft(): Removes and returns the leftmost element.
 
 
dq.pop()      # Removes 5
dq.popleft()  # Removes 0
 

 
#3. Extending Deque
 
#extend(iterable): Adds elements from an iterable to the right.
 
#extendleft(iterable): Adds elements from an iterable to the left (in reverse order).
 
dq.extend([5, 6, 7])  # deque([1, 2, 3, 4, 5, 6, 7])
 
dq.extendleft([-2, -1])  # deque([-1, -2, 1, 2, 3, 4, 5, 6, 7])
 

print(dq)
#4. Rotating Deque
 
#rotate(n): Rotates elements n steps to the right (negative for left rotation).
 
dq.rotate(2)# Right rotation by 2
print(dq)
dq.rotate(-1)  # Left rotation by 1
print(dq)

 
#5. Limiting Deque Size
 
#deque(iterable, maxlen=n): Creates a deque with a fixed maximum length.
 
dq = deque([1, 2, 3], maxlen=5)  # Max size = 5
 
dq.append(4)
 
dq.append(5)
 
dq.append(6)  # Oldest element (1) is removed automatically
 
print(dq)  # Output: deque([2, 3, 4, 5, 6], maxlen=5)
 
#When to Use deque:
 
#When you need fast append/pop operations from both ends.