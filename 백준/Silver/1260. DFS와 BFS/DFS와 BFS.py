from collections import deque
import sys
input = sys.stdin.readline


def dfs(v, answer):
    answer.append(v)
    check[v] = True
    for i in range(len(graph[v])):
        if graph[v][i] and not check[i]:
            dfs(i, answer)


def bfs(v, answer):
    answer.append(v)
    q = deque([v])
    check[v] = True
    while q:
        qv = q.popleft()
        for i in range(len(graph[qv])):
            if graph[qv][i] and not check[i]:
                check[i] = True
                q.append(i)
                answer.append(i)


N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2], graph[v2][v1] = True, True

answer = []
check = [False] * (N + 1)
dfs(V, answer)
print(*answer)

answer.clear()
check = [False] * (N + 1)
bfs(V, answer)
print(*answer)
