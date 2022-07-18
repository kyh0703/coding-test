from collections import deque
import sys
input = sys.stdin.readline

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def is_validate_position(y, x):
    return 0 <= y < N and 0 <= x < N


def bfs(y, x):
    link = 1
    check[y][x] = True
    q = deque()
    q.append([y, x])
    while q:
        qy, qx = q.popleft()
        for i in range(4):
            ny, nx = qy + dy[i], qx + dx[i]
            if not is_validate_position(ny, nx):
                continue
            if not check[ny][nx] and graph[ny][nx] == '1':
                check[ny][nx] = True
                q.append([ny, nx])
                link += 1
    return link


N = int(input().strip())
graph = [input().strip() for _ in range(N)]
check = [[False] * N for _ in range(N)]
answer = []
for y in range(N):
    for x in range(N):
        if not check[y][x] and graph[y][x] == '1':
            answer.append(bfs(y, x))
answer.sort()
print(len(answer))
for i in answer:
    print(i)
