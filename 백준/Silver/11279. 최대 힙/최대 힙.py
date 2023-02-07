import sys
import heapq as hq
input = sys.stdin.readline

pq = []
N = int(input().strip())
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        print(-hq.heappop(pq) if pq else 0)
        continue
    hq.heappush(pq, -x)
