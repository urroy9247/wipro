from collections import deque

# Create an empty deque
dq = deque()

# Adding elements to both ends
dq.append(10)         # Add 10 to the right end
dq.appendleft(20)     # Add 20 to the left end
dq.append(30)         # Add 30 to the right end
dq.appendleft(40)     # Add 40 to the left end

# Display the current deque
print("Current deque:", dq)

# Removing elements from both ends
dq.pop()              # Remove from the right end (30)
dq.popleft()          # Remove from the left end (40)

# Display the deque after removals
print("Deque after pop and popleft:", dq)
