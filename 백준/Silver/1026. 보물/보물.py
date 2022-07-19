N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0
for _ in range(N):
    min_v, max_v = min(A), max(B)
    answer += min_v * max_v
    A.pop(A.index(min_v))
    B.pop(B.index(max_v))
print(answer)