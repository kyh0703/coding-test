N, M = map(int, input().split())
answer = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for ij in range(i - 1, j):
        answer[ij] = k
print(*answer)
