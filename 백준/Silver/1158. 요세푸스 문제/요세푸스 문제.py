from collections import deque

N, K = map(int, input().split())
circle = deque(range(1, N + 1))
answer = []
while 0 < len(circle):
    count = 1
    while count < K:
        v = circle.popleft()
        circle.append(v)
        count += 1
    answer.append(circle.popleft())
print("<", end='')
print(*answer, sep=', ', end='')
print(">")
