import sys

input = sys.stdin.readline
N, L = map(int, input().strip().split())
waters = [list(map(int, input().strip().split())) for _ in range(N)]
waters.sort()

count = 0
answer = 0
for start, end in waters:
    if end < start:
        continue
    if start < count:
        start = count
    while start < end:
        start += L
        answer += 1
    count = start
print(answer)