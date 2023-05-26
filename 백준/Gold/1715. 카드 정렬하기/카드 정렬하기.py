import sys
import heapq as hq

input = sys.stdin.readline

N = int(input().strip())
cards = [int(input().strip()) for _ in range(N)]

pq = []
for card in cards:
    hq.heappush(pq, card)

answer = 0
while len(pq) > 1:
    first = hq.heappop(pq)
    second = hq.heappop(pq)
    sum_value = first + second
    answer += sum_value
    hq.heappush(pq, sum_value)

print(answer)
