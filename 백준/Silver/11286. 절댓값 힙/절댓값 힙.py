import heapq as hq
import sys
input = sys.stdin.readline

N = int(input().strip())
pq = []
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        print(hq.heappop(pq)[1] if pq else 0)
    else:
        hq.heappush(pq, (abs(x), x))
