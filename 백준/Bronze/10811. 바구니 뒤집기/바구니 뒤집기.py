N, M = map(int, input().split())
answer = list(range(1, N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    answer[i-1:j] = answer[i-1:j][::-1]
print(*answer)
