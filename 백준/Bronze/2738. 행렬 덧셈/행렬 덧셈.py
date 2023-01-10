N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for a, b in zip(A, B):
    print(*list(i + j for i, j in zip(a, b)))
