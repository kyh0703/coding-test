from collections import deque
import sys
input = sys.stdin.readline


def bfs(v):
    q = deque()
    q.append(v)
    check[v] = 1
    calc = 0
    while q:
        nv = q.popleft()
        calc = check[nv]
        for i in range(len(graph[nv])):
            child = graph[nv][i]
            if check[child] == 0:
                check[child] = calc + 1
                q.append(child)


n = int(input().strip())
start, end = map(int, input().split())
m = int(input().strip())
graph = [[] * (n + 1) for _ in range(n + 1)]
check = [0] * (n + 1)
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v1].sort()
    graph[v2].append(v1)
    graph[v2].sort()
bfs(start)
if check[end] == 0 or check[start] == 0:
    print(-1)
else:
    print(abs(check[end] - check[start]))