N = int(input())
second = 0
K = 1
while True:
    if N == 0:
        break
    if N < K:
        K = 1
        continue
    N = N - K
    K = K + 1
    second += 1
print(second)