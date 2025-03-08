import heapq
q = []
heapq.heappush(q, (2, 'from'))
heapq.heappush(q, (1, 'Hello'))
heapq.heappush(q, (3, 'AskPython'))
heapq.heappushpop(q, (4, 'AskPython'))
heapq.heapreplace(q, (2,'data'))
while q:
    # Keep popping until the queue is empty
    item = heapq.heappop(q)
    print(item)

