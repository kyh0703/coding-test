from itertools import combinations

N, M = map(int, input().split())
N = [i for i in range(1, N+1)]
for i in combinations(N, M):
    print(*i)
