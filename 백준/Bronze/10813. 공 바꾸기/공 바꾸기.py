n, m = map(int, input().split())
answer = [i for i in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    answer[i - 1], answer[j - 1] = answer[j - 1], answer[i - 1]
print(*answer)
