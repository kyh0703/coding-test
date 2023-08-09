from math import ceil

H, W, N, M = map(int, input().split())
answer = 0
row = ceil(H / (N + 1))
col = ceil(W / (M + 1))
answer = row * col
print(answer)