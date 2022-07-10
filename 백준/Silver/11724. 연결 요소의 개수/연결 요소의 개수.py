import sys

sys.setrecursionlimit(10 ** 6)
N, M = map(int, sys.stdin.readline().strip().split())
graph = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: x - 1, map(int, sys.stdin.readline().strip().split()))
    graph[a][b] = graph[b][a] = 1

answer = 0
check = [False] * N

def dfs(now):
    for nxt in range(N):
        if graph[now][nxt] and not check[nxt]:
            check[nxt] = True
            dfs(nxt)

for i in range(N):
    if not check[i]:
        answer += 1
        check[i] = True
        dfs(i)

print(answer)
