import heapq

# Create a list of tasks with (priority, task_name)
tasks = [
    (3, "task 3"),
    (1, "task 1"),
    (2, "task 2")
]

# Convert the list into a heap
heapq.heapify(tasks)

print("Tasks in priority order:")
# Pop tasks in priority order
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Task: {task} (Priority: {priority})")