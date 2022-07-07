import sys
import heapq as hq

q = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    X = int(sys.stdin.readline().strip())
    if X == 0:
        if len(q) == 0:
            print(0)
        else:
            print(hq.heappop(q))
    else:
        hq.heappush(q, X)
