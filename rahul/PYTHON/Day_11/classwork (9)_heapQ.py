import heapq
q = []
heapq.heappush(q, (2, 'from'))
heapq.heappush(q, (1, 'Hello'))
heapq.heappush(q, (3, 'AskPython'))
while q:
    # Keep popping until the queue is empty
    item = heapq.heappop(q)
    print(item)

print(q)