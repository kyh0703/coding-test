import sys
input = sys.stdin.readline


def dfs(v):
    global answer
    check[v] = True
    for i in graph[v]:
        if not check[i]:
            dfs(i)
            answer += 1


N = int(input().strip())
M = int(input().strip())
graph = [[] * (N + 1) for _ in range(N + 1)]
check = [False] * (N + 1)
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v1].sort()
    graph[v2].append(v1)
    graph[v2].sort()


answer = 0
dfs(1)
print(answer)