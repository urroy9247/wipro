import queue
priority_q = queue.PriorityQueue()
priority_q.put((1,'Hello'))
priority_q.put((3, 'AskPython'))
priority_q.put((2, 'from'))
for i in range(priority_q.qsize()):
    print(priority_q.get())
