import sys
from collections import deque


dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def validate(y, x):
    return (0 <= y < N and 0 <= x < M)

def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        qy, qx = q.popleft()
        for i in range(4):
            ny = qy + dy[i]
            nx = qx + dx[i]
            if validate(ny, nx) and graph[ny][nx] == 1:
                graph[ny][nx] = graph[qy][qx] + 1
                q.append((ny, nx))
    return graph[N - 1][M - 1]

input = sys.stdin.readline
N, M = map(int, input().strip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))
print(bfs(0, 0))
