import heapq as hq

pq = []
hq.heappush(pq, 123213)
hq.heappush(pq, -123)
hq.heappush(pq, 13)
hq.heappush(pq, 131)
hq.heappush(pq, 132)

print("pq", pq)
while len(pq) > 0:
    print(hq.heappop(pq))
